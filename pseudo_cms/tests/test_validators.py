from django import test
from django.core.exceptions import ValidationError

from pseudo_cms import validators

__all__ = ('ValidURLExistsTests', )


@test.override_settings(ROOT_URLCONF='pseudo_cms.tests.testing_urls')
class ValidURLExistsTests(test.TestCase):
    def test_returns_none_when_url_path_exists(self):
        path = "/tests/path-one/"
        self.assertEqual(None, validators.internal_path_exists(path))

    def test_raises_validation_error_when_path_doesnt_exist(self):
        path = "/tests/bad-path/"
        self.assertRaises(ValidationError, validators.internal_path_exists,
                          path)
