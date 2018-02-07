from django import test
from django import template

from pseudo_cms import models

__all__ = ('PageContentTagTests', )


class PageContentTagTests(test.TestCase):
    def test_adds_page_content_to_context(self):
        url = "/path/to/something/"
        content = models.Content.objects.create(url=url, title="My Title")

        t = template.Template(
            """{% load pseudo_cms_tags %}{% page_content path as content %}
        <h1>{{ content.title }}</h1>
        """)
        result = t.render(template.Context({'path': url}))

        self.assertHTMLEqual("<h1>{0.title}</h1>".format(content), result)
