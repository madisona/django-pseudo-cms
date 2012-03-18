
from django.contrib import admin

from image_helper.fields import SizedImageField
from image_helper.widgets import AdminImagePreviewWidget

from pseudo_cms import models

class ContentAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'url', 'title', 'page_title']
    search_fields = ['title', 'page_title', 'body', 'meta_description']

    fieldsets = (
        ('', {
            'fields': ('url',)
        }),
        ('Search Engine Fields', {
            'fields': ('title', 'meta_description'),
        }),
        ('Page Content', {
            'fields': ('page_title', 'body', 'image'),
        })
    )

    def thumbnail(self, obj):
        thumbnail_url = obj.image.thumbnail.url()
        return '<img src="{0}" width="100" alt="thumbnail" />'.format(thumbnail_url)
    thumbnail.allow_tags = True

    formfield_overrides = {
        SizedImageField: {'widget': AdminImagePreviewWidget}
    }


admin.site.register(models.Content, ContentAdmin)
