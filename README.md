CNRGlab@UWaterloo webpage
=========================

This repository contains code and sources files
to generate [CNRGlab's static website](http://compneuro.uwaterloo.ca/).
If you want to adapt it to your own purposes,
check out HACKING.md.

Editing content
---------------

CNRGlab members with access to this repository
should focus on the `ctn_waterloo/content/` subdirectory,
where all the text on the site lives.
New blog articles can be created by adding
a Markdown file in the `ctn_waterloo/content/blog/` directory,
and so on. In general, look at the existing
files in those directories to see what your file
should look like, and if you have any questions, concerns,
or feature requests, please create an issue
or [talk to me](mailto:tbekolay@gmail.com).

This repository is set up such that when you
push a commit a build is initiated through
[Travis-CI](https://travis-ci.org/ctn-waterloo/website).
The build generates all the static files,
and ``rsync``'s them to the webserver.
This may take a few moments,
but the site should always be in sync with this repository.
Please try not to break this build,
as it will mean that our website could be in a broken state!
If you're doing something that you're not sure about,
please try your change out locally first
by installing the packages in `requirements.txt`
and then running `python manage.py run`
from the root of this repository.

Images and other files
----------------------

This repository should not be used to store
files or images. Doing so would cause the repository
to become large, increasing the amount of time
it takes to generate the website.
Ideally, when content is changed it should show up
almost immediately; keeping the repository
small helps do that.

### Where to put files

Obviously we want plenty of images and other files on the site.
The best place to put them is on the same server,
just not in the git repository.
Currently, the `files/` directory
in `cnrglab`'s home on WatArts
is symlinked such that it is accessible
at `compneuro.uwaterloo.ca/files`.
Please ask someone how to get your files
into that directory, and then link
to them appropriately.

The other option is to put images on an image sharing site,
as long as they allow directly linking to those images on external sites.
For example, I can upload a screenshot to [imgur](http://imgur.com/)
and use it in my content pages like so:

`![Screenshot](http://i.imgur.com/2WpbV.png)` = ![Screenshot](http://i.imgur.com/2WpbV.png)

Under the hood
--------------

In general, you shouldn't need to read past this.
The content in `ctn_waterloo/content/` should be straightforward
to edit and add to; if you disagree,
please say something rather than read any further!
However, if you're curious...

### How pages work

Pages consist of two sections: metadata and content.
The first blank line separates the metadata from content.
In other words, if your page contains only metadata
(common for publications), then it should contain no blank lines,
or only one blank line at the end of the file.
For pages that only contain content (none for this site),
the first line of content should be prefaced by a blank line.

Metadata is a dictionary that contains
information about the content.
Metadata is made available to templates separate from the content.
Metadata can be expressed in two ways (at the moment): YAML or BibTeX.
For YAML, this means that the metadata is key-value pairs.
If you want a list, then it should be accessible by some key.
For example,

    title: About me
    links:
        - url: http://facebook.com/tbekolay
          title: Facebook
        - url: http://bekolay.org
          title: Homepage
        - url: http://compneuro.uwaterloo.ca
          title: Lab webpage

    This is my about me page. Check out the links on the right.

The metadata for this page is the following Python dictionary.

    {'title': 'About me',
     'links': [
         {'url': 'http://facebook.com/tbekolay',
          'title': 'Facebook'},
         {'url: 'http://bekolay.org',
          'title': 'Homepage'},
         {'url': 'http://compneuro.uwaterloo.ca',
          'title': 'Lab webpage'}]}

Metadata can also be written in BibTeX, as this format
may be more familiar or easily available for scholarly publications.
Note that this BibTeX metadata **cannot** contain blank lines,
even in comments and the abstract!

As an example, the following BibTeX contains metadata
about two publications.

    @article{Eliasmith2012,
        author = {Eliasmith, Chris and Stewart, Terrence C and Choo, Xuan and Bekolay, Trevor and DeWolf, Travis and Tang, Yichuan and Tang, Charlie and Rasmussen, Daniel},
        doi = {10.1126/science.1225266},
        journal = {Science},
        keywords = {Behavior, Brain, Neural Networks},
        number = {6111},
        pages = {1202--5},
        pmid = {23197532},
        title = {{A large-scale model of the functioning brain}},
        volume = {338},
        year = {2012}
    }
    @phdthesis{Bekolay2011,
        author = {Bekolay, Trevor},
        school = {University of Waterloo},
        title = {{Learning in large-scale spiking neural networks}},
        type = {Masters Thesis},
        url = {http://uwspace.uwaterloo.ca/handle/10012/6195},
        year = {2011}
    }

    This is the full text for one of the publications.

The metadata for this page is the following Python dictionary.

    {'publications': [{
            'citekey': 'Eliasmith2012',
            'type': 'article',
            'author': 'Eliasmith, Chris and Stewart, Terrence C and Choo, Xuan and Bekolay, Trevor and DeWolf, Travis and Tang, Yichuan and Tang, Charlie and Rasmussen, Daniel',
            'doi': '10.1126/science.1225266',
            'journal': 'Science',
            'keywords': 'Behavior, Brain, Neural Networks',
            'number': '6111',
            'pages': '1202--5',
            'pmid': '23197532',
            'title': 'A large-scale model of the functioning brain',
            'volume': '338',
            'year': '2012'
        }, {
            'citekey': 'Bekolay2011',
            'at_type': 'phdthesis',
            'author': 'Bekolay, Trevor',
            'school': 'University of Waterloo',
            'title': 'Learning in large-scale spiking neural networks',
            'type': 'Masters Thesis',
            'url': 'http://uwspace.uwaterloo.ca/handle/10012/6195',
            'year': '2011'}]}

Content is written in Markdown format.
If you want to include the full text of paper
directly on the webpage,
you can put the citation information above in BibTeX,
and then include the content in Markdown format.
You can include math formatted the same way as in LaTeX
(`$...$` for inline and `$$...$$` for blocks).
Images are included with `![alt text](link to image)`.
Arbitrary HTML is also allowed, as Markdown
is a superset of HTML.
Please see
[this introduction](http://daringfireball.net/projects/markdown/basics)
for more information.
