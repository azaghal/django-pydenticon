# Django imports.
from django.conf.urls import url

# Application imports.
from .views import image

urlpatterns = [
    # View for rendering an identicon image.
    url(r'^image/(?P<data>.+)$', image, name="image")
    ]

def get_patterns(instance="django_pydenticon"):
    """
    Generates URL patterns for Django Pydenticon application. The return value
    of this function can be used directly by the django.conf.urls.include
    function.

    Arguments:

      instance - Instance namespace that should be assigned to generated URL
      patterns.

    Returns:

      Tuple consisting out of URL patterns, instance namespace, and application
      namespace.
    """

    return urlpatterns, instance, "django_pydenticon"
