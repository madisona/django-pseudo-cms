from django.core.exceptions import ValidationError
from django.core.urlresolvers import resolve
from django.http import Http404


def internal_path_exists(path):
    """
    Validates that url path is registered and can properly be resolved
    in a django configuration.
    """
    try:
        resolve(path)
    except Http404:
        raise ValidationError("'{0}' is not a valid url.".format(path))
