import os
import mimetypes

from . import app, pages, redirects, serve_static
from .filters import slugify
from flask_frozen import Freezer

# Seems to be available only on some systems...
mimetypes.add_type('application/atom+xml', '.atom')

freezer = Freezer(app)

@freezer.register_generator
def redirect_url_generator():
    return redirects.keys()

@freezer.register_generator
def static_url_generator():
    return serve_static

@freezer.register_generator
def people_page():
    for person in pages:
        if person.path.startswith('people/'):
            yield {'slug': slugify(person['name'])}
