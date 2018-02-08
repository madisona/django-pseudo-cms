from django.contrib import admin

from image_helper.fields import SizedImageField
from image_helper.widgets import AdminImagePreviewWidget

from pseudo_cms import models


class ContentAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'url', 'title', 'page_title']
    search_fields = ['title', 'page_title', 'body', 'meta_description']
    exclude = ('body_html', )

    fieldsets = (('', {
        'fields': ('url', )
    }), ('Search Engine Fields', {
        'fields': ('title', 'meta_description'),
    }), ('Page Content', {
        'fields': ('page_title', 'page_tagline', 'content_format', 'body',
                   'image'),
    }))

    def thumbnail(self, obj):
        """Thumbnail for list display preview"""
        if obj.image:
            thumbnail_url = obj.image.thumbnail.url()
            return '<img src="{0}" width="100" alt="thumbnail" />'.format(
                thumbnail_url)
        else:
            return ''

    thumbnail.allow_tags = True

    formfield_overrides = {
        SizedImageField: {
            'widget': AdminImagePreviewWidget
        }
    }


admin.site.register(models.Content, ContentAdmin)
