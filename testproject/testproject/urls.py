from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Django Pydenticon.
import django_pydenticon.urls

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # URLs for Django Pydenticon.
    url(r'^identicon/', include(django_pydenticon.urls)),
)
