import django
from django.test import TestCase

from pseudo_cms import utils


class ConvertToHTMLTests(TestCase):

    reST_text = "This is text\n"\
                "==============="
    plain_text = "This is text\nThat's Cool"
    html = "<h4>This is the title</h4>"

    def _strip_tag(self, val):
        # django 2.0 uses plain <br>. Prior uses <br />
        return val.replace("<br />", "<br>")

    def test_turns_rst_to_html(self):
        self.assertTrue(
            "<h4>This is text</h4>" in utils.reST_to_html(self.reST_text))

    def test_turns_text_to_html_line_breaks(self):
        if django.VERSION[0] < 3:
            self.assertEqual("This is text<br>That&#39;s Cool",
                             self._strip_tag(utils.text_to_html(self.plain_text)))
        else:
            self.assertEqual("This is text<br>That&#x27;s Cool",
                             self._strip_tag(utils.text_to_html(self.plain_text)))

    def test_convert_to_html_uses_rst(self):
        result = utils.convert_to_html(self.reST_text, utils.reST)
        self.assertTrue("<h4>This is text</h4>" in result)

    def test_convert_to_html_uses_html(self):
        result = utils.convert_to_html(self.html, utils.HTML)
        self.assertTrue("<h4>This is the title</h4>" in result)

    def test_convert_to_html_uses_plain_text(self):
        result = utils.convert_to_html(self.plain_text, utils.PLAIN_TEXT)

        if django.VERSION[0] < 3:
            self.assertTrue(
                "This is text<br>That&#39;s Cool" in self._strip_tag(result))
        else:
            self.assertTrue(
                "This is text<br>That&#x27;s Cool" in self._strip_tag(result))
