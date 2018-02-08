from django import test
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from pseudo_cms import models, utils

__all__ = ('ContentModelTests', )


def get_content_model(save=False, **kwargs):
    m = models.Content(**kwargs)
    if save:
        m.save()
    return m


class ContentModelTests(test.TestCase):
    urls = 'pseudo_cms.tests.testing_urls'

    def test_cant_save_content_for_path_that_doesnt_exist(self):
        content = get_content_model(url="/tests/bad/path/")

        with self.assertRaises(ValidationError) as ctx:
            content.full_clean()

        self.assertEqual([u"'/tests/bad/path/' is not a valid url."],
                         ctx.exception.message_dict['url'])

    def test_url_must_be_unique(self):
        url = "/some/url/"
        get_content_model(save=True, url=url)
        with self.assertRaises(IntegrityError):
            get_content_model(save=True, url=url)

    def test_gets_content_for_page(self):
        url = "/some/url/"
        get_content_model(save=True, url=url)

        content_model = models.Content.get_for_page(url)
        self.assertEqual(url, content_model.url)

    def test_get_content_for_page_returns_none_when_not_found(self):
        content_model = models.Content.get_for_page("/random/")
        self.assertEqual(None, content_model)

    def test_orders_by_url(self):
        one = get_content_model(url="ZZZ", save=True)
        two = get_content_model(url="AAA", save=True)
        three = get_content_model(url="MMM", save=True)
        content_models = models.Content.objects.all()
        self.assertEqual([two, three, one], list(content_models))

    def test_body_html_gets_saved_when_html_type_is_used(self):
        body = "<h1>This is my body</h1>"

        c = get_content_model(save=True, body=body, content_format=utils.HTML)
        c.save()
        self.assertHTMLEqual(body, c.body_html)

    def test_body_html_gets_saved_when_rst_type_is_used(self):
        body = "This is a title\n"\
               "==============="

        c = get_content_model(save=True, body=body, content_format=utils.reST)
        c.save()
        self.assertTrue("<h4>This is a title</h4>" in c.body_html)

    def test_body_html_gets_saved_when_plain_text_is_used(self):
        body = "This is a title\n"\
               "And some content"

        c = get_content_model(
            save=True, body=body, content_format=utils.PLAIN_TEXT)
        c.save()
        self.assertTrue("This is a title<br />And some content" in c.body_html)
