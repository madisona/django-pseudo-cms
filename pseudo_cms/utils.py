from docutils.core import publish_parts

from django.conf import settings
from django.utils.encoding import smart_str
from django.template.defaultfilters import linebreaksbr

HTML = u"html"
PLAIN_TEXT = u"text"
reST = u"reST"
CONTENT_FORMAT_CHOICES = (
    (HTML, u'Raw HTML'),
    (reST, u'reStructuredText'),
    (PLAIN_TEXT, u"Plain Text"),
)

DOCUTILS_SETTINGS = getattr(settings, 'DOCUTILS_SETTINGS', {
    'doctitle_xform': False,
    'initial_header_level': 4,
    'id_prefix': 's-',
})


def reST_to_html(text):
    return publish_parts(
        source=smart_str(text),
        writer_name="html",
        settings_overrides=DOCUTILS_SETTINGS)['fragment']


def text_to_html(text):
    return linebreaksbr(text)


def convert_to_html(text, content_type):
    if content_type == PLAIN_TEXT:
        html = text_to_html(text)
    elif content_type == reST:
        html = reST_to_html(text)
    else:
        html = text
    return html
