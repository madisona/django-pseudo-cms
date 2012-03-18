
from django.conf import settings
from django.db import models
from django.utils.encoding import force_unicode

from image_helper.fields import SizedImageField

from pseudo_cms.validators import internal_path_exists

# You may change the image size in settings if you wish.
IMAGE_SIZE = getattr(settings, "PSEUDO_CMS_IMAGE_SIZE", (600, 450))
THUMBNAIL_SIZE = getattr(settings, "PSEUDO_CMS_THUMBNAIL_SIZE", (176, 132))


class Content(models.Model):
    url = models.CharField(max_length=200, unique=True, validators=[internal_path_exists],
                           help_text="URL endpoint of page content belongs to.")
    title = models.CharField(max_length=60, help_text="Title that shows on searches / browser tab.")
    meta_description = models.CharField(max_length=200, help_text="Description that shows in search engine.")

    page_title = models.CharField(max_length=60, help_text="Title that shows on page.")
    body = models.TextField()

    image = SizedImageField(blank=True, upload_to="cms/content", size=IMAGE_SIZE, thumbnail_size=THUMBNAIL_SIZE)

    class Meta(object):
        ordering = ('url',)

    def __unicode__(self):
        return force_unicode(self.url)

    @classmethod
    def get_for_page(cls, page_url):
        try:
            return cls.objects.get(url=page_url)
        except cls.DoesNotExist:
            return None
