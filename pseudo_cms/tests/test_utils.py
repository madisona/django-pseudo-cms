from django.test import TestCase

from pseudo_cms import utils


class ConvertToHTMLTests(TestCase):

    reST_text = "This is text\n"\
                "==============="
    plain_text = "This is text\nThat's Cool"
    html = "<h4>This is the title</h4>"

    def test_turns_rst_to_html(self):
        self.assertTrue(
            "<h4>This is text</h4>" in utils.reST_to_html(self.reST_text))

    def test_turns_text_to_html_line_breaks(self):
        self.assertEqual("This is text<br />That&#39;s Cool",
                         utils.text_to_html(self.plain_text))

    def test_convert_to_html_uses_rst(self):
        result = utils.convert_to_html(self.reST_text, utils.reST)
        self.assertTrue("<h4>This is text</h4>" in result)

    def test_convert_to_html_uses_html(self):
        result = utils.convert_to_html(self.html, utils.HTML)
        self.assertTrue("<h4>This is the title</h4>" in result)

    def test_convert_to_html_uses_plain_text(self):
        result = utils.convert_to_html(self.plain_text, utils.PLAIN_TEXT)
        self.assertTrue("This is text<br />That&#39;s Cool" in result)
