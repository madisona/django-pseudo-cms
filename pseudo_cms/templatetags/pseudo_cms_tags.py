from django import template

from pseudo_cms.models import Content

register = template.Library()


@register.assignment_tag
def page_content(page_url):
    return Content.get_for_page(page_url)
