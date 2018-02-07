from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from image_helper.fields import SizedImageField

from pseudo_cms.validators import internal_path_exists
from pseudo_cms import utils

# You may change the image size in settings if you wish.
IMAGE_SIZE = getattr(settings, "PSEUDO_CMS_IMAGE_SIZE", (600, 450))
THUMBNAIL_SIZE = getattr(settings, "PSEUDO_CMS_THUMBNAIL_SIZE", (176, 132))


@python_2_unicode_compatible
class Content(models.Model):
    url = models.CharField(
        max_length=200,
        unique=True,
        validators=[internal_path_exists],
        help_text="URL endpoint of page content belongs to.",
        db_index=True)
    title = models.CharField(
        max_length=100,
        help_text="Title that shows on searches / browser tab.")
    meta_description = models.CharField(
        max_length=200, help_text="Description that shows in search engine.")

    page_title = models.CharField(
        max_length=60, help_text="Title that shows on page.")
    page_tagline = models.CharField(
        max_length=120, help_text="Tagline / Subtitle for page", blank=True)
    content_format = models.CharField(
        choices=utils.CONTENT_FORMAT_CHOICES,
        max_length=50,
        default=utils.PLAIN_TEXT)
    body = models.TextField()
    body_html = models.TextField()

    image = SizedImageField(
        blank=True,
        upload_to="cms/content",
        size=IMAGE_SIZE,
        thumbnail_size=THUMBNAIL_SIZE)

    class Meta(object):
        ordering = ('url', )

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        self.body_html = utils.convert_to_html(self.body, self.content_format)
        return super(Content, self).save(*args, **kwargs)

    @classmethod
    def get_for_page(cls, page_url):
        try:
            return cls.objects.get(url=page_url)
        except cls.DoesNotExist:
            return None
