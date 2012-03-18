from django.conf.urls.defaults import patterns, url
from django.http import HttpResponse

def test_path_view(request):
    return HttpResponse("OK")

urlpatterns = patterns('',
    url("^tests/path-one/$", test_path_view, name="test_path"),
)
