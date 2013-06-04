**Do not touch**
================

The only images that should be going in this directory
(and therefore in the git repository) are **small**,
**very frequently used** images.
Examples of good candidates are the images already in this
directory; e.g., the images used in the publications page
to indicate the type of publication.

Where to put images
===================

Obviously we want plenty of images on the site.
The best place to put them is on the same server,
just not in the git repository.
I'll set it up such that the directory of files
on the server is symlinked such that files can
be uploaded to a certain place, and made available to pages.
The only downside to this is that you'll have to get
the login credentials for compneuro, and SSH
in to upload things, which isn't super convenient.

The other option is to put images on an image sharing site,
as long as they allow directly linking to those images on external sites.
For example, I can upload a screenshot to [imgur](http://imgur.com/)
and use it in my content pages like so:

`![Screenshot](http://i.imgur.com/2WpbV.png)` = ![Screenshot](http://i.imgur.com/2WpbV.png)
