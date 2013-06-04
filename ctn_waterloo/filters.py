from datetime import datetime
import re
import unicodedata


def get_headings(html):
    """Kind of a hack, but we're looking for headings so that we
    can add them to a nav element.
    The html returned here is not a legit document, it's just
    the markdown. So we'll just use a simple regex to
    find ids.

    """
    return re.findall(r'<h\d>(.+)</h\d>', html)


def lead_paragraph(html):
    """
    Makes the first <p> tag have the "lead" class.
    """
    return re.sub(r'(<p>)', r'<p class="lead">', html, count=1)


def nice_date(date_str):
    """Dates in the system should always be done in the following form:
      YYYY-MM-DD HH:mm
    using a 24-hour clock.
    This transforms that to something a bit nicer for human eyes.

    """
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    return dt.strftime("%B %d, %Y").replace(' 0', ' ')


def slugify(value, separator='-'):
    """ Slugify a string, to make it URL friendly. """
    if type(value) == unicode:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = re.sub('[^\w\s-]', '', value.decode('ascii')).strip().lower()
    return re.sub('[%s\s]+' % separator, separator, value)


def youtubify(video_id, width=320, widescreen=False):
    if widescreen:
        height = width * 9 / 16
    else:
        height = width * 3 / 4

    return '<iframe id="ytplayer" type="text/html" width="%d" height="%d" src="http://www.youtube.com/embed/%s" frameborder="0"></iframe>' % (width, height, video_id)
