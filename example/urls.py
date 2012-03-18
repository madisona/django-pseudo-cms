
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import View

admin.autodiscover()

class TestView(View):

    def get(self, request):
        return HttpResponse("IT Worked!!")

urlpatterns = patterns('',
    url(r'^$', TestView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

# serve media files for sample stuff to work.
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), 'django.views.static.serve', kwargs={
            'document_root': settings.MEDIA_ROOT,
        }),
    )
