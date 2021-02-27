import codecs
import inspect
import itertools
import latexcodec
import os
import re

import flask
import markdown
import yaml
import werkzeug

import pybtex.database
import pybtex.style.formatting.plain
import pybtex.style.formatting.unsrt
import pybtex.backends.plaintext
import pybtex.richtext
from pybtex.style.template import FieldIsMissing, optional, href, join, node, words

from .markdown_extensions import AddAnchorsExtension, MathJaxExtension

DOI_URL_RE = re.compile(R"^(https?://((.*?)\.)?)?doi.org/(.*?)/?$")
ARXIV_URL_RE = re.compile(R"^(https?://)?arxiv.org/abs/(.*?)/?$")

@node
def raw_field(children, data, name, apply_func=None):
    """Return the raw contens of the bibliography entry field.

    This function does not decode special LaTeX characters."""
    assert not children
    try:
        field = data.fields[name]
    except KeyError:
        raise FieldIsMissing(name, data)
    else:
        if apply_func:
            field = applay_func(field)
        return field


class NonURLDecodingPlainStyle(pybtex.style.formatting.plain.Style):
    """Plain text pybtex style which does not attempt to latex decode URLs."""

    def __enter__(self):
        return self

    def __exit__(self ,type, value, traceback):
        pass

    def format_url(self, e):
        return words [
            'URL:',
            href [
                raw_field('url'),
                join(' ') [
                    raw_field('url')
                ]
            ]
        ]


class ResidualPlainStyle(pybtex.style.formatting.plain.Style):
    """Formats everything but authors, title, and URLs."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._in_format_editor = False
        self._old_date_children = None

    def __enter__(self):
        self._old_date_children = pybtex.style.formatting.unsrt.date.children
        pybtex.style.formatting.unsrt.date.children = tuple()
        return self

    def __exit__(self ,type, value, traceback):
        pybtex.style.formatting.unsrt.date.children = self._old_date_children
        pass

    def format_author_or_editor(self, e):
        return optional [
            self.format_editor(e),
        ]

    def format_editor(self, e, as_sentence=True):
        self._in_format_editor = True
        try:
            return super().format_editor(e, as_sentence)
        finally:
            self._in_format_editor = False

    def format_names(self, role, as_sentence=True):
        if self._in_format_editor:
            return super().format_names(role, as_sentence)
        return pybtex.richtext.String("")

    def format_title(self, e, which_field, as_sentence=False):
        return pybtex.richtext.String("")

    def format_btitle(self, e, which_field, as_sentence=True):
        if not as_sentence: # inbook, inproceedings, incollection...
            return super().format_btitle(e, which_field, as_sentence)
        else: # book
            return pybtex.richtext.String("")

    def format_url(self, e):
        return pybtex.richtext.String("")

    def format_pubmed(self, e):
        return pybtex.richtext.String("")

    def format_doi(self, e):
        return pybtex.richtext.String("")

    def format_eprint(self, e):
        return pybtex.richtext.String("")


def _extract_identifier_from_url(meta, url_key, meta_key, url_re, url_re_group_idx):
    if (url_key in meta['cite_info']):
        match = url_re.match(meta['cite_info'][url_key])
        if match:
            if not (meta_key in meta['cite_info']):
                meta['cite_info'][meta_key] = match.groups()[url_re_group_idx]
            del meta['cite_info'][url_key]


def _canonicalize_identifier(meta, meta_key, url_re, url_re_group_idx):
    # Test whether the special service identifier is actually a URL, if yes,
    # extract the identifier
    if meta_key in meta['cite_info']:
        match = url_re.match(meta['cite_info'][meta_key])
        if match:
            if not (meta_key in meta['cite_info']):
                meta['cite_info'][meta_key] = match.groups()[url_re_group_idx]


def bibtex_to_dict(text):
    """Add BibTeX data to metadata."""
    def _format_person(person):
        von_last = ' '.join(person.prelast_names + person.last_names)
        jr = ' '.join(person.lineage_names)
        first = ' '.join(person.first_names + person.middle_names)
        fullname = ' '.join(part for part in (first, von_last, jr) if part)
        # Handle escaped LaTeX characters
        return codecs.decode(fullname, 'ulatex')

    bib_data = pybtex.database.parse_string(text, 'bibtex')

    # Render the BibTeX entry in plain text. Once completely, and once including
    # only data that is not already extracted in another form.
    plain_render = pybtex.backends.plaintext.Backend()

    with NonURLDecodingPlainStyle() as plain_style:
        formatted_entry = next(plain_style.format_entries(list(bib_data.entries.values())))
        cite_plain = formatted_entry.text.render(plain_render)

    with ResidualPlainStyle() as plain_style:
        formatted_entry = next(plain_style.format_entries(list(bib_data.entries.values())))
        cite_plain_residual = formatted_entry.text.render(plain_render)

    # It is possible to parse out multiple BibTeX entries
    # in one go! But, I'm assuming that the metadata
    # contains information about only one publication.

    citekey = list(bib_data.entries.keys())[0]
    entry = bib_data.entries[citekey]
    meta = {
        'citekey': citekey,
        'type': entry.type,
        'authors': [_format_person(person)
                    for person in entry.persons['author']],
        'cite_info': {
            k.lower(): v.render_as('plaintext')
            for k, v in entry.rich_fields.items()
        },
        'cite_bibtex': text,
        'cite_plain': cite_plain,
        'cite_plain_residual': cite_plain_residual,
    }

    # If the URL points at a special service, construct the corresponding
    # cite_info key instead. Also, sanitize existing cite_info keys.
    for url_key in ['url', 'eprint']:
        _extract_identifier_from_url(meta, url_key, 'doi', DOI_URL_RE, 3)
        _extract_identifier_from_url(meta, url_key, 'arxiv', ARXIV_URL_RE, 1)
    _canonicalize_identifier(meta, 'doi', DOI_URL_RE, 3)
    _canonicalize_identifier(meta, 'arxiv', ARXIV_URL_RE, 1)

    # Get important stuff from cite_info
    extract = ('title', 'abstract', 'pdf', 'url', 'year', 'keywords',
               'poster', 'presentation')
    for key in extract:
        if key in meta['cite_info']:
            meta[key] = meta['cite_info'].pop(key)

    decode = ('title', 'abstract', 'keywords')
    for key in decode:
        if key in meta:
            meta[key] = codecs.decode(meta[key], 'ulatex')

    # Add editors to cite_info, if they exist
    if 'editor' in entry.persons:
        meta['cite_info']['editors'] = ", " .join(
            [_format_person(person) for person in entry.persons['editor']])

    # If this is an arXiv publication, set the type to "preprint"
    if ('journal' in meta['cite_info']) and ('arxiv' in meta['cite_info']['journal'].lower()):
        entry.type = 'preprint'
        meta['type'] = 'preprint'

    # Extract a few more cite_info keys
    if ('arxiv' in meta['cite_info']):
        meta['arxiv'] = meta['cite_info']['arxiv']
    if ('doi' in meta['cite_info']):
        meta['doi'] = meta['cite_info']['doi']

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

    @werkzeug.utils.cached_property
    def html(self):
        return self.html_renderer(self.body)

    @werkzeug.utils.cached_property
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
        return iter(self._pages.values())

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
            with open(filename, 'rb') as fd:
                content = str(fd.read(), self.config('encoding'))
            page = self._parse(content, path, ext)
            self._file_cache[filename] = page, mtime
        return page

    @werkzeug.utils.cached_property
    def _pages(self):
        def _walk(directory, path_prefix=()):
            for name in os.listdir(directory):
                full_name = os.path.join(directory, name)

                if os.path.isdir(full_name):
                    _walk(full_name, path_prefix + (name,))
                elif any([name.endswith(ext) for ext in extensions]):
                    name_without_extension = os.path.splitext(name)[0]
                    path = '/'.join(path_prefix + (name_without_extension, ))
                    pages[path] = self._load_file(path, full_name)

        extensions = list(self.config('renderers').keys())
        pages = {}

        # Fail if the root is a non-ASCII byte string. Use Unicode.
        _walk(str(self.root))

        return pages

    def _parse(self, string, path, ext):
        lines = iter(string.split('\n'))
        meta = '\n'.join(itertools.takewhile(str.strip, lines))

        content = '\n'.join(lines)
        html_renderer = self.config('renderers')[ext]

        if not callable(html_renderer):
            html_renderer = werkzeug.import_string(html_renderer)
        return Page(path, meta, content, html_renderer)
