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
    if type(value) == str:
        # Transform the string to NFKC before perfoming any operation on it.
        # This is important as e.g. umlauts have a distinct Unicode codepoint,
        # but may be represented as two Unicode codepoints in the input (e.g.
        # when using the US-International keyboard layout and typing the
        # character as diacritic mark followed by the character itself.)
        value = unicodedata.normalize('NFKC', value)

        # Implement proper transliteration of German umlauts.
        replacement_dict = ({
            chr(0xE4): "ae",
            chr(0xF6): "oe",
            chr(0xFC): "ue",
            chr(0xC4): "Ae",
            chr(0xD6): "Oe",
            chr(0xDC): "Ue",
            chr(0xDF): "ss",
        })
        for src, tar in replacement_dict.items():
            value = value.replace(src, tar)

        # Decompose any remaining unicode codepoints and transform to ASCII,
        # throwing away anything outside the Basic Latin block.
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')

    value = re.sub('[^\w\s-]', '', value.decode('ascii')).strip().lower()
    return re.sub('[%s\s]+' % separator, separator, value)


def youtubify(video_id, width=320, widescreen=False):
    if widescreen:
        height = width * 9 / 16
    else:
        height = width * 3 / 4

    return '<iframe id="ytplayer" type="text/html" width="%d" height="%d" src="http://www.youtube.com/embed/%s" frameborder="0"></iframe>' % (width, height, video_id)
