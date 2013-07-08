import os
import mimetypes

from . import app, redirects
from flask.ext.frozen import Freezer, walk_directory

# Seems to be available only on some systems...
mimetypes.add_type('application/atom+xml', '.atom')

freezer = Freezer(app)

@freezer.register_generator
def redirect_url_generator():
    return redirects.keys()
