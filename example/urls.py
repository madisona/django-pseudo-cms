
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import View

admin.autodiscover()


class TestView(View):

    def get(self, request):
        return HttpResponse("IT Worked!!")


urlpatterns = [
    url(r'^$', TestView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
]

# serve media files for sample stuff to work.
if settings.DEBUG:
    urlpatterns.extend(static(settings.STATIC_URL))
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
