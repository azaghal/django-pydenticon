# Django imports.
from django.conf.urls import patterns, url

# Application imports.
from .views import image

urlpatterns = patterns(
    'django_pydenticon.views',

    # View for rendering an identicon image.
    url(r'^image/(?P<data>.+)$', image, name="image")
    )
