Hacking on this site
====================

This was the developers' first foray into web-stuff, so it's a little bit
awkward.

Basically, it pursues a model-view design. Where the Markdown files are the
model, which get converter into views by Flask by filling out the HTML templates
and parsing the Markdown files using `model.py`. The properties of the pages,
such as which pages are to be included, can be found in `__init__.py`.
