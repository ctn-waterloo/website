import re

import markdown

from .filters import slugify


def unique(id, ids):
    """ Ensure id is unique in set of ids. Append '_1', '_2'... if not """
    IDCOUNT_RE = re.compile(r'^(.*)_([0-9]+)$')
    while id in ids or not id:
        m = IDCOUNT_RE.match(id)
        if m:
            id = '%s_%d'% (m.group(1), int(m.group(2))+1)
        else:
            id = '%s_%d'% (id, 1)
    ids.add(id)
    return id


def itertext(elem):
    """ Loop through all children and return text only.

    Reimplements method of same name added to ElementTree in Python 2.7

    """
    if elem.text:
        yield elem.text
    for e in elem:
        for s in itertext(e):
            yield s
        if e.tail:
            yield e.tail


class MathJaxPattern(markdown.inlinepatterns.Pattern):
    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(self, r'(?<!\\)(\$\$?)(.+?)\2')

    def handleMatch(self, m):
        node = markdown.util.etree.Element('mathjax')
        node.text = markdown.util.AtomicString(
            m.group(2) + m.group(3) + m.group(2))
        return node


class MathJaxExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        # Needs to come before escape matching
        # because \ is pretty important in LaTeX
        md.registerExtension(self)
        md.inlinePatterns.add('mathjax', MathJaxPattern(), '<escape')


class AddAnchorsTreeprocessor(markdown.treeprocessors.Treeprocessor):
    IDs = set()

    def run(self, doc):
        toadd = []
        for ix, elem in enumerate(doc.getiterator()):
            if elem.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                id = slugify(''.join(itertext(elem)))
                anchor = markdown.util.etree.Element(
                    'a', {'class': 'anchor', 'id': unique(id, self.IDs)})
                toadd.append((ix - 1, anchor))

        # Go in reverse because inserting will mess up indices
        for ix, anchor in reversed(toadd):
            doc.insert(ix, anchor)


class AddAnchorsExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        self.processor = AddAnchorsTreeprocessor()
        self.processor.md = md
        if 'attr_list' in md.treeprocessors.keys():
            # insert after attr_list treeprocessor
            md.treeprocessors.add('headerid', self.processor, '>attr_list')
        else:
            # insert after 'prettify' treeprocessor.
            md.treeprocessors.add('headerid', self.processor, '>prettify')

    def reset(self):
        self.processor.IDs = set()
