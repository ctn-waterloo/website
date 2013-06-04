import inspect
import itertools
import os
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

import flask
import markdown
import yaml
import werkzeug
import pybtex.database.input.bibtex
import pybtex.style.formatting.plain
import pybtex.backends.plaintext

from .markdown_extensions import AddAnchorsExtension, MathJaxExtension


def bibtex_to_dict(text):
    """Add BibTeX data to metadata."""
    def _format_person(person):
        von_last = ' '.join(person._prelast + person._last)
        jr = ' '.join(person._lineage)
        first = ' '.join(person._first + person._middle)
        return ' '.join(part for part in (first, von_last, jr) if part)

    parser = pybtex.database.input.bibtex.Parser()
    bib_data = parser.parse_stream(StringIO(text))

    plain_style = pybtex.style.formatting.plain.Style()
    plain_render = pybtex.backends.plaintext.Backend()
    formatted_entry = next(plain_style.format_entries(bib_data.entries.values()))

    # It is possible to parse out multiple BibTeX entries
    # in one go! But, I'm assuming that the metadata
    # contains information about only one publication.

    citekey = bib_data.entries.keys()[0]
    entry = bib_data.entries[citekey]
    meta = {
        'citekey': citekey,
        'type': entry.type,
        'authors': [_format_person(person)
                    for person in entry.persons['author']],
        'cite_info': entry.fields,
        'cite_bibtex': text,
        'cite_plain': formatted_entry.text.render(plain_render),
    }

    # Get important stuff from cite_info
    extract = ('title', 'abstract', 'pdf', 'url', 'year', 'keywords')
    for key in extract:
        if entry.fields.has_key(key):
            meta[key] = meta['cite_info'].pop(key)

    # Add editors to cite_info, if they exist
    if entry.persons.has_key('editor'):
        meta['cite_info']['editors'] = [_format_person(person)
                                        for person in entry.persons['editor']]

    return meta


def markdown_to_html(text):
    extensions = ['fenced_code', 'codehilite', 'attr_list',
                  AddAnchorsExtension({}), MathJaxExtension({})]
    md = markdown.Markdown(extensions=extensions, output_format="html5")
    return md.convert(text)


def ipython_notebook_to_html(text):
    pass


class Page(object):
    def __init__(self, path, metadata, body, html_renderer):
        self.path = path
        self._metadata = metadata
        self.body = body
        self.html_renderer = html_renderer

    def __getitem__(self, key):
        return self.meta[key]

    def __html__(self):
        """In a template, ``{{ page }}`` is equivalent to
        ``{{ page.html|safe }}``.

        """
        return self.html

    def __repr__(self):
        return '<Page %r>' % self.path

    @werkzeug.cached_property
    def html(self):
        return self.html_renderer(self.body)

    @werkzeug.cached_property
    def meta(self):
        # Should do this more properly, but for now, if metadata
        # starts with @ we'll consider it bibtex.
        if self._metadata.startswith('@'):
            meta = bibtex_to_dict(self._metadata)
        else:
            meta = yaml.safe_load(self._metadata)

        if not isinstance(meta, dict):
            raise ValueError("Metadata in %s is not a dict." % self.path)

        return meta


class FlatPages(object):
    default_config = (
        ('root', 'content'),
        ('renderers', {'.md': markdown_to_html,
                       '.bib': markdown_to_html,
                       '.ipynb': ipython_notebook_to_html}),
        ('encoding', 'utf-8'),
        ('auto_reload', 'if debug'),
    )

    def __init__(self, app=None):
        self._file_cache = {}
        if app is not None:
            self.init_app(app)

    def __iter__(self):
        return self._pages.itervalues()

    def init_app(self, app):
        for key, value in self.default_config:
            config_key = 'FLATPAGES_%s' % key.upper()
            app.config.setdefault(config_key, value)

        app.before_request(self._conditional_auto_reset)
        self.app = app

    def config(self, key):
        return self.app.config['FLATPAGES_%s' % key.upper()]

    def get(self, path, default=None):
        pages = self._pages
        try:
            return pages[path]
        except KeyError:
            return default

    def get_or_404(self, path):
        page = self.get(path, None)
        if page is None:
            flask.abort(404)
        return page

    def reload(self):
        try:
            # This will "unshadow" the cached_property.
            # The property will be re-executed on next access.
            del self.__dict__['_pages']
        except KeyError:
            pass

    @property
    def root(self):
        return os.path.join(self.app.root_path, self.config('root'))

    def _conditional_auto_reset(self):
        auto = self.config('auto_reload')
        if auto == 'if debug':
            auto = self.app.debug
        if auto:
            self.reload()

    def _load_file(self, path, filename):
        mtime = os.path.getmtime(filename)
        cached = self._file_cache.get(filename)
        ext = os.path.splitext(filename)[1]
        if cached and cached[1] == mtime:
            page = cached[0]
        else:
            with open(filename) as fd:
                content = fd.read().decode(self.config('encoding'))
            page = self._parse(content, path, ext)
            self._file_cache[filename] = page, mtime
        return page

    @werkzeug.cached_property
    def _pages(self):
        def _walk(directory, path_prefix=()):
            for name in os.listdir(directory):
                full_name = os.path.join(directory, name)

                if os.path.isdir(full_name):
                    _walk(full_name, path_prefix + (name,))
                elif any([name.endswith(ext) for ext in extensions]):
                    name_without_extension = os.path.splitext(name)[0]
                    path = u'/'.join(path_prefix + (name_without_extension, ))
                    pages[path] = self._load_file(path, full_name)

        extensions = self.config('renderers').keys()
        pages = {}

        # Fail if the root is a non-ASCII byte string. Use Unicode.
        _walk(unicode(self.root))

        return pages

    def _parse(self, string, path, ext):
        lines = iter(string.split(u'\n'))
        meta = u'\n'.join(itertools.takewhile(unicode.strip, lines))

        content = u'\n'.join(lines)
        html_renderer = self.config('renderers')[ext]

        if not callable(html_renderer):
            html_renderer = werkzeug.import_string(html_renderer)
        return Page(path, meta, content, html_renderer)
