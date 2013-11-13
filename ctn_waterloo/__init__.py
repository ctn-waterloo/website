import datetime

from flask import Flask, Markup
from flask import abort, g, render_template, url_for
from flask import request, send_from_directory

from .filters import get_headings, lead_paragraph, nice_date, slugify, youtubify
from .pages import FlatPages
from .model import Model

DEBUG = True
SITE_NAME = "CNRGlab @ UWaterloo"
FREEZER_BASE_URL = 'http://compneuro.uwaterloo.ca/'

app = Flask(__name__)
app.config.from_object(__name__)
app.jinja_env.filters['lead_paragraph'] = lead_paragraph
app.jinja_env.filters['nice_date'] = nice_date
app.jinja_env.filters['slugify'] = slugify
pages = FlatPages(app)
model = Model(pages)

### Index

@app.route('/')
@app.route('/index.html')
def index():
    g.topic = 'index'
    page = pages.get('index')
    page.teaser = page['teaser']
    page.teaser_image = page['teaser_image']
    page.videolink = Markup(youtubify(page['video'], 320))
    pubs = pages.get('publications_index')
    page.publications = [model.publication(pages.get('publications/' + citekey))
                         for citekey in pubs['highlight']]
    page.blogposts = model.blogposts(end=5)
    return render_template('index.html', page=page)

### About

@app.route('/about.html')
def about():
    g.topic = 'about'
    paths = ('index', 'faq', 'history', 'press')
    sections = [pages.get(path) for path in paths]
    return render_template('about.html', sections=sections)

### Blog

@app.route('/blog.html')
@app.route('/blog_index_<int:back>.html')
def blog_index(back=0):
    if back < 0:
        raise ValueError("back is negative. Don't do that.")

    g.topic = 'blog'
    posts_per_page = 5
    start = back
    end = back + posts_per_page
    page = pages.get('blog_index')
    page.blogposts = model.blogposts(start=start, end=end)
    posts = sum([post.path.startswith('blog/') for post in pages])

    if back > 0:
        page.newer = url_for('blog_index', back=max(0, back - posts_per_page))
    else:
        page.newer = None
    if back < posts - posts_per_page:
        page.older = url_for('blog_index', back=min(posts - 1, end))
    else:
        page.older = None

    return render_template('blog_index.html', page=page)


@app.route('/blog_archive.html')
def blog_archive():
    g.topic = 'blog'
    page = pages.get('blog_archive')
    blogposts = model.blogposts()
    years = set([post['date'][:4] for post in blogposts])
    page.years = sorted([
        {'year': year, 'blogposts': [
            post for post in blogposts if post['date'].startswith(year)
        ]} for year in years], reverse=True, key=lambda year: year['year'])

    return render_template('blog_archive.html', page=page)

@app.route('/blog/<slug>.html')
def blog_post(slug):
    g.topic = 'blog'
    blogposts = model.blogposts()
    post = next(bp for bp in blogposts if slugify(bp['title']) == slug)
    post.headings = get_headings(post.html)
    return render_template('blog_post.html', post=post)


### Meetings

@app.route('/meetings.html')
def meetings():
    g.topic = 'meetings'
    page = pages.get('meetings_index')
    page.meetings = model.meetings()
    page.calendar = Markup(page['calendar'])
    return render_template('meetings.html', page=page)


### People

@app.route('/people.html')
def people_index():
    g.topic = 'people'
    page = pages.get('people_index')
    groups = ('Faculty', 'Postdocs', 'Grad students', 'Undergrad students')
    page.groups = [{'title': group, 'people': model.people(group)}
                   for group in groups]
    return render_template('people_index.html', page=page)

@app.route('/people/<slug>.html')
def people_page(slug):
    g.topic = 'people'
    person = pages.get('people/' + slug)
    person.publications = model.publications(author=person['name'])
    person.blogposts = model.blogposts(author=person['name'])
    return render_template('people_page.html', person=person)


### Publications

@app.route('/publications.html')
def publications_index():
    g.topic = 'publications'
    page = pages.get('publications_index')
    page.publications = model.publications()
    return render_template('publications_index.html', page=page)


@app.route('/publications/<citekey>.html')
def publications_page(citekey):
    g.topic = 'publications'
    pubs = model.publications()
    publication = next(pub for pub in pubs if pub['citekey'] == citekey)
    return render_template('publications_page.html', publication=publication)


### Research

@app.route('/research.html')
def research_index():
    g.topic = 'research'
    page = pages.get('research_index')
    page.topics = [model.research(topic) for topic in page['topics']]
    return render_template('research_index.html', page=page)


@app.route('/research/<topic>.html')
def research_topic(topic):
    g.topic = 'research'
    page = model.research(topic)
    return render_template('research_topic.html', page=page)


@app.route('/research/<topic>/<slug>.html')
def research_page(topic, slug):
    g.topic = 'research'
    topicpage = model.research(topic)
    try:
        page = next(a for a in topicpage.articles
                    if slugify(a['title']) == slug)
    except StopIteration:
        raise ValueError(slug + ".md could not be found. "
                         "Either the title or the filename is wrong.")
    page.headings = get_headings(page.html)
    return render_template('research_page.html', page=page)


### Redirects

redirects = {
    '/bookinfo.html': '/research/nef/neural-engineering-book.html',
    '/cnrglab/index.html': '/index.html',
    '/about/index.html': '/about.html',
    '/blog/index.html': '/blog.html',
    '/meetings/index.html': '/meetings.html',
    '/people/index.html': '/people.html',
    '/publications/index.html': '/publications.html',
    '/research/index.html': '/research.html',
}

def redirect_url():
    return render_template('redirect.html', new_url=redirects[request.path])

for url in redirects:
    app.add_url_rule(url, 'redirect_url', redirect_url)

### Other

# @app.route('/feed.atom')
# def atom_feed():
#     articles = sorted(
#         [(article.meta.get('modified', article['created']), article)
#          for article in mdpages], reverse=True)
#     if len(articles) > 25:
#         articles = articles[:25]
#     feed_updated, _ = articles[0]
#     xml = render_template('atom.xml', **locals())
#     return app.response_class(xml, mimetype='application/atom+xml')


serve_static = [
    '/favicon.ico',
    '/humans.txt',
    '/robots.txt',
]

def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

for url in serve_static:
    app.add_url_rule(url, 'static_from_root', static_from_root)


if __name__ == '__main__':
    app.run()
