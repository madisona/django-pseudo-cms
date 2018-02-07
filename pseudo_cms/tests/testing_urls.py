from django.conf.urls import url
from django.http import HttpResponse


def test_path_view(request):
    return HttpResponse("OK")


urlpatterns = [
    url("^tests/path-one/$", test_path_view, name="test_path"),
]
