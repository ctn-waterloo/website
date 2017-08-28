import datetime

from flask import Flask, Markup
from flask import abort, g, render_template, url_for
from flask import request, send_from_directory

from .filters import get_headings, lead_paragraph, nice_date, slugify, youtubify


TYPE_TEXT = {
    'techreport': 'CTN Tech Report',
    'incollection': 'Book Chapter',
    'inproceedings': 'Conference Proceedings',
    'proceedings': 'Conference Proceedings',
    'book': 'Book',
    'mastersthesis': 'Thesis',
    'phdthesis': 'Thesis',
    'article': 'Journal Article',
}

class Model(object):
    def __init__(self, pages_instance):
        self.pages = pages_instance

    def blogposts(self, end=None, start=None, author=None):
        if author is None:
            test = lambda p: p.path.startswith('blog/')
        else:
            test = lambda p: p.path.startswith('blog/') and author in p['author']

        blogposts = sorted([post for post in self.pages if test(post)],
                           reverse=True, key=lambda post: post['date'])

        for post in blogposts:
            post.url = url_for('blog_post', slug=slugify(post['title']))
            post.authorlink = self.authorlink(post['author'])

        for p1, p2 in zip(blogposts[:-1], blogposts[1:]):
            p1.older = url_for('blog_post', slug=slugify(p2['title']))
            p2.newer = url_for('blog_post', slug=slugify(p1['title']))

        if end is not None and len(blogposts) > end:
            blogposts = blogposts[:end]
        if start is not None:
            blogposts = blogposts[start:]
        return blogposts


    def meetings(self):
        return sorted([mtg for mtg in self.pages
                       if mtg.path.startswith('meetings/')],
                      reverse=True, key=lambda mtg: mtg['year'])

    def person(self, person):
        person.url = url_for('people_page', slug=slugify(person['name']))
        return person

    def people(self, group=None):
        if group is None:
            test = lambda p: p.path.startswith('people/')
        else:
            test = lambda p: p.path.startswith('people/') and p['group'] == group

        people = sorted([self.person(p) for p in self.pages if test(p)],
                        key=lambda p: p['name'])
        return people

    def publication(self, pub):
        if pub.meta.has_key('url'):
            pub.fulltext = pub['url']
        if pub['cite_info'].has_key('journal'):
            pub.journal = pub['cite_info']['journal']
        elif pub['type'] == 'techreport':
            pub.journal = "Tech Report"
        elif 'thesis' in pub['type']:
            pub.journal = "Thesis"  # fallback
            if 'type' in pub['cite_info']:
                ctype = pub['cite_info']['type'].lower()
                if "master" in ctype or "master's" in ctype:
                    pub.journal = "Master's Thesis"
                elif "phd" in ctype:
                    pub.journal = "PhD Thesis"
        elif 'book' in pub['type']:
            pub.journal = pub['cite_info']['publisher']
        elif pub['cite_info'].has_key('booktitle'):
            pub.journal = pub['cite_info']['booktitle']

        pub.authors = [self.authorlink(name) for name in pub['authors']]
        pub.url = url_for('publications_page', citekey=pub['citekey'])
        pub.type = TYPE_TEXT.get(pub['type'], pub['type'])
        return pub

    def publications(self, end=None, start=None, author=None):
        if author is None:
            test = lambda p: p.path.startswith('publications/')
        else:
            test = lambda p: (p.path.startswith('publications/')
                              and author in p['authors'])

        allpubs = sorted([self.publication(pub) for pub in self.pages
                          if test(pub)],
                         reverse=True, key=lambda pub: pub['year'])

        if end is not None and len(allpubs) > end:
            allpubs = allpubs[:end]
        if start is not None:
            allpubs = allpubs[start:]

        return allpubs

    def research(self, topic):
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

        page = self.pages.get('research/' + topic + '_index')
        page.url = url_for('research_topic', topic=topic)
        page.toc = _recursive_map(
            lambda title: {'title': title,
                           'url': url_for('research_page', topic=topic, slug=slugify(title))},
            page['toc'])

        page.articles = [self.pages.get('research/' + topic + '/' + slugify(p['title']))
                         for p in _flatten(page.toc)]
        page.articles = [a for a in page.articles if a is not None]

        for article in page.articles:
            article.topic = url_for('research_topic', topic=topic)

        for a1, a2 in zip(page.articles[:-1], page.articles[1:]):
            a1.next = url_for('research_page', topic=topic,
                              slug=slugify(a2['title']))
            a2.prev = url_for('research_page', topic=topic,
                              slug=slugify(a1['title']))

        return page

    def courses(self, topic):
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

        page = self.pages.get('courses/' + topic + '_index')
        page.url = url_for('courses_topic', topic=topic)
        page.toc = _recursive_map(
            lambda title: {'title': title,
                           'url': url_for('courses_page', topic=topic, slug=slugify(title))},
            page['toc'])

        page.articles = [self.pages.get('courses/' + topic + '/' + slugify(p['title']))
                         for p in _flatten(page.toc)]
        page.articles = [a for a in page.articles if a is not None]

        for article in page.articles:
            article.topic = url_for('courses_topic', topic=topic)

        for a1, a2 in zip(page.articles[:-1], page.articles[1:]):
            a1.next = url_for('courses_page', topic=topic,
                              slug=slugify(a2['title']))
            a2.prev = url_for('courses_page', topic=topic,
                              slug=slugify(a1['title']))

        return page

    def authorlink(self, name):
        if self.pages.get('people/' + slugify(name)) is not None:
            return Markup('<a href="' + url_for('people_page',
                                                slug=slugify(name))
                          + '">' + name + '</a>')
        else:
            return name


if __name__ == '__main__':
    app.run()
