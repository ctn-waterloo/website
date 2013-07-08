import datetime

from flask import Flask, Markup
from flask import abort, g, render_template, url_for
from flask import request, send_from_directory

from .filters import get_headings, lead_paragraph, nice_date, slugify, youtubify
from .pages import FlatPages

DEBUG = True
SITE_NAME = "CNRGlab @ UWaterloo"
FREEZER_BASE_URL = 'http://compneuro.uwaterloo.ca/'

app = Flask(__name__)
app.config.from_object(__name__)
app.jinja_env.filters['lead_paragraph'] = lead_paragraph
app.jinja_env.filters['nice_date'] = nice_date
app.jinja_env.filters['slugify'] = slugify
pages = FlatPages(app)

### Index

@app.route('/')
@app.route('/index.html')
def index():
    g.topic = 'index'
    page = pages.get('index')
    page.teaser = Markup(page['teaser'])
    page.teaser_image = _expand_static(page['teaser_image'])
    page.videolink = Markup(youtubify(page['video'], 320))
    page.publications = _get_all_pub_info(pages, 5)
    page.blogposts = _get_all_blogpost_info(pages, 5)
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
    page.blogposts = _get_all_blogposts(pages, start=start, end=end)
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
    blogposts = _get_all_blogpost_info(pages)
    years = set([post['date'][:4] for post in blogposts])
    page.years = sorted([
        {'year': year, 'blogposts': [
            post for post in blogposts if post['date'].startswith(year)
        ]} for year in years], reverse=True, key=lambda year: year['year'])

    return render_template('blog_archive.html', page=page)

@app.route('/blog/<slug>.html')
def blog_post(slug):
    g.topic = 'blog'
    blogposts = _get_all_blogposts(pages)
    post = next(bp for bp in blogposts if slugify(bp['title']) == slug)
    post.headings = get_headings(post.html)
    return render_template('blog_post.html', post=post)


### Meetings

@app.route('/meetings.html')
def meetings():
    g.topic = 'meetings'
    page = pages.get('meetings_index')
    page.meetings = _get_all_meetings(pages)
    page.calendar = Markup(page['calendar'])
    return render_template('meetings.html', page=page)


### People

@app.route('/people.html')
def people_index():
    g.topic = 'people'
    page = pages.get('people_index')
    groups = ('Faculty', 'Postdocs', 'Grad students', 'Undergrad students')
    page.groups = [{'title': group, 'people': _get_all_people(pages, group)}
                   for group in groups]
    return render_template('people_index.html', page=page)

@app.route('/people/<slug>.html')
def people_page(slug):
    g.topic = 'people'
    person = pages.get('people/' + slug)
    person.publications = _get_all_pub_info(pages, author=person['name'])
    person.blogposts = _get_all_blogpost_info(pages, author=person['name'])
    return render_template('people_page.html', person=person)


### Publications

@app.route('/publications.html')
def publications_index():
    g.topic = 'publications'
    page = pages.get('publications_index')
    page.publications = _get_all_pubs(pages)
    return render_template('publications_index.html', page=page)


@app.route('/publications/<citekey>.html')
def publications_page(citekey):
    g.topic = 'publications'
    pubs = _get_all_pubs(pages)
    publication = next(pub for pub in pubs if pub['citekey'] == citekey)
    return render_template('publications_page.html', publication=publication)


### Research

@app.route('/research.html')
def research_index():
    g.topic = 'research'
    page = pages.get('research_index')
    page.topics = [_get_research_topic(pages, t) for t in page['topics']]
    return render_template('research_index.html', page=page)


@app.route('/research/<topic>.html')
def research_topic(topic):
    g.topic = 'research'
    page = _get_research_topic(pages, topic)
    return render_template('research_topic.html', page=page)


@app.route('/research/<topic>/<slug>.html')
def research_page(topic, slug):
    g.topic = 'research'
    topicpage = _get_research_topic(pages, topic)
    page = next(a for a in topicpage.articles if slugify(a['title']) == slug)
    page.headings = get_headings(page.html)
    return render_template('research_page.html', page=page)


### Redirects

redirects = {
    '/cnrglab/': '/index.html',
    '/cnrglab/index.html': '/index.html',
}

def redirect_url(url):
    return render_template('redirect.html', new_url=redirects[url])

for url in redirects:
    app.add_url_rule(url, url, view_func=lambda: redirect_url(url))

### Other

@app.errorhandler(404)
def not_found(e):
    """This only gets seen locally..."""
    return render_template('404.html')


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

@app.route('/favicon.ico')
@app.route('/humans.txt')
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


TYPE_IMAGES = {
    'techreport': 'static/img/placeholder.png',
    'inbook': 'static/img/placeholder.png',
    'proceedings': 'static/img/placeholder.png',
    'book': 'static/img/placeholder.png',
    'mastersthesis': 'static/img/placeholder.png',
    'article': 'static/img/journal.gif',
}

TYPE_TEXT = {
    'techreport': 'CTN Tech Report',
    'inbook': 'Book Chapter',
    'proceedings': 'Conference Proceedings',
    'book': 'Book',
    'mastersthesis': 'Thesis',
    'article': 'Journal Article',
}


def _expand_static(url):
    if url.startswith('static'):
        return url_for('static', filename=url[url.index('/') + 1:])
    return url


def _get_authorlink(name):
    if pages.get('people/' + slugify(name)) is not None:
        return Markup('<a href="' + url_for('people_page', slug=slugify(name))
                      + '">' + name + '</a>')
    else:
        return name


def _get_all_pubs(pages, end=None, start=None, author=None):
    if author is None:
        test = lambda p: p.path.startswith('publications/')
    else:
        test = lambda p: (p.path.startswith('publications/')
                          and author in p['authors'])

    allpubs = sorted([pub for pub in pages if test(pub)],
                     reverse=True, key=lambda pub: pub['year'])

    for pub in allpubs:
        if pub.meta.has_key('url'):
            pub.fulltext = pub['url']
        pub.url = url_for('publications_page', citekey=pub['citekey'])
        pub.type = TYPE_TEXT.get(pub['type'], pub['type'])
        pub.type_image = TYPE_IMAGES.get(pub['type'], 'static/img/placeholder.png')
        pub.type_image = _expand_static(pub.type_image)

    if end is not None and len(allpubs) > end:
        allpubs = allpubs[:end]
    if start is not None:
        allpubs = allpubs[start:]
    return allpubs


def _get_all_pub_info(*args, **kwargs):
    return [{'url': pub.url, 'year': pub['year'], 'title': pub['title']}
            for pub in _get_all_pubs(*args, **kwargs)]


def _get_all_blogposts(pages, end=None, start=None, author=None):
    if author is None:
        test = lambda p: p.path.startswith('blog/')
    else:
        test = lambda p: p.path.startswith('blog/') and author in p['author']

    blogposts = sorted([post for post in pages if test(post)],
                       reverse=True, key=lambda post: post['date'])

    for post in blogposts:
        post.url = url_for('blog_post', slug=slugify(post['title']))
        post.authorlink = _get_authorlink(post['author'])

    for p1, p2 in zip(blogposts[:-1], blogposts[1:]):
        p1.older = url_for('blog_post', slug=slugify(p2['title']))
        p2.newer = url_for('blog_post', slug=slugify(p1['title']))

    if end is not None and len(blogposts) > end:
        blogposts = blogposts[:end]
    if start is not None:
        blogposts = blogposts[start:]
    return blogposts


def _get_all_blogpost_info(*args, **kwargs):
    return [{'url': post.url, 'date': post['date'], 'title': post['title']}
            for post in _get_all_blogposts(*args, **kwargs)]


def _get_all_meetings(pages):
    return sorted([mtg for mtg in pages if mtg.path.startswith('meetings/')],
                  reverse=True, key=lambda mtg: mtg['year'])


def _get_all_people(pages, group=None):
    if group is None:
        test = lambda p: p.path.startswith('people/')
    else:
        test = lambda p: p.path.startswith('people/') and p['group'] == group

    people = sorted([person for person in pages if test(person)],
                    key=lambda person: person['name'])
    for person in people:
        person.url = url_for('people_page', slug=slugify(person['name']))
        person.picture = _expand_static(person['picture'])
    return people


def _get_research_topic(pages, topic):
    def _recursive_map(f, data):
        if isinstance(data, list):
            return [_recursive_map(f, elem) for elem in data]
        else:
            return f(data)
    def _flatten(l):
        for el in l:
            if isinstance(el, list):
                for sub in _flatten(el):
                    yield sub
            else:
                yield el

    page = pages.get('research/' + topic + '_index')
    page.url = url_for('research_topic', topic=topic)
    page.picture = _expand_static(page['picture'])
    page.toc = _recursive_map(
        lambda title: {'title': title,
            'url': url_for('research_page', topic=topic, slug=slugify(title))},
        page['toc'])

    page.articles = [pages.get('research/' + topic + '/' + slugify(p['title']))
                     for p in _flatten(page.toc)]
    for article in page.articles:
        article.topic = url_for('research_topic', topic=topic)
    for a1, a2 in zip(page.articles[:-1], page.articles[1:]):
        a1.next = url_for('research_page', topic=topic,
                          slug=slugify(a2['title']))
        a2.prev = url_for('research_page', topic=topic,
                          slug=slugify(a1['title']))

    return page

if __name__ == '__main__':
    app.run()
