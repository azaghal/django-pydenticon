.. _usage:

Usage
=====

Django Pydenticon is targeted at developers who wish to integrate an identicon
service in their Django projects. This chapter covers details on how an
identicon image is served, and how to integrate Django Pydenticon with other
applications.

Requesting identicons
---------------------

Identicon images are served through specially formatted URL. Whenever such URL
is submitted to Django Pydenticon application, an identicon image is created on
the fly.

The format of URL is ``/image/USER_DATA`` (relative to prefix URL assigned for
the application), where **USER_DATA** can be either in hashed or raw format. For
example, if Django Pydenticon application is reachable under ``/identicon/``,
identicon images can be requested using the following URLs:

* ``/identicon/image/somedataforhashing`` (raw data)
* ``/identicon/image/55d207ea47247b375dc1f495517f1332`` (pre-hashed data using
  *md5*)

.. warning::
   Keep in mind that if user data is submitted in pre-hashed form, the digest
   used should match with the digest configured for Django Pydenticon
   application. If digest does not match, the user data will be treated as any
   other user data, and it will be hashed once again.

URL instance namespaces
-----------------------

When resolving Django Pydenticon URLs, you should always use the URL names in
conjunction with application instance namespace.

Default application instance namespace is ``django_pydenticon``. Alternative
instance namespace can be specified by passing an (optional) argument to
``django_pydenticons.urls.get_patterns`` function.

For example, if default namespace is in use, the ``image`` URL would be
referenced as ``django_pydenticon:image`` in template tag ``url`` or function
call ``reverse``.

Generating identicon URLs in templates
--------------------------------------

If the data (whether raw or hashed) is available in template's context, an
identicon URL can be easily generated from within the template itself. This can
be achieved via ``url`` tag.

The URL for serving the identicons is named ``image``. It should always be
referenced in conjunction with an application instance namespace. The
application namespace defaults to ``django_pydenticon``, unless custom instance
namespace is passed when including the application URLs via
``django_pydenticon.urls.get_patterns``. In case of default namespace, that
means the URL would be referenced to as ``django_pydenticon:image``.

For example, let's say that it's necessary to show an identicon based on
username next to every comment. Related template snippet could look something
similar to the following::

  <ul>
  {% for comment in comments %}
    <li><img src="{% url 'django_pydenticon:image' comment.user.username %}"/>{{ comment.text }}</li>
  {% endfor %}
  </ul>

Generating identicon URLs programatically
-----------------------------------------

The URLs can be generated programtically, using Python code. Afterwards those
URLs can be either passed into template's rendering context, or used inside of
code for whatever other purposes. This is achieved by using the ``reverse`` URL
resolver (from ``django.core.urlresolvers``).

The URL for serving the identicons is named ``image``. It should always be
referenced in conjunction with an application instance namespace. The
application namespace defaults to ``django_pydenticon``, unless custom instance
namespace is passed when including the application URLs via
``django_pydenticon.urls.get_patterns``. In case of default namespace, that
means the URL would be referenced to as ``django_pydenticon:image``.

For example, let's say that it's necessary to show an identicon based on
username next to every comment. A special context variable could be passed into
template that would contain a list of comments, where each comment consists out
of identicon URL and comment itself. The Python code could look something
similar to::

  comments_context = []

  for comment in comments:
      identicon_url = reverse("django_pydenticon:image",
                              kwargs={"data": comment.user.username})
      comments_context.append({"text": comment.text,
                               "identicon_url": identicon_url})

  return render_to_response('myapp/comments.html',
                            {"comments": comments_context})

With the above context set-up, the ``myapp/comments.html`` template could
contain a snippet similar to::

  <ul>
  {% for comment in comments %}
    <li><img src="{{ comment.identicon_url }}"/>{{ comment.text }}</li>
  {% endfor %}
  </ul>

Overriding identicon parameters
-------------------------------

By default, the identicon generator will use parameters from project settings
for each request, falling back to application defaults if none were defined. In
addition to this static configuration, some parameters can be overridden per
request.

Per-request identicon generator parameters are passed via *GET* parameters. The
following *GET* parameters are available:

w
  Specifies the width of generated identicon image in pixels. Overrides the
  ``PYDENTICON_WIDTH`` configuration option.

h
  Specifies the height of generated identicon image in pixels. Overrides the
  ``PYDENTICON_HEIGHT`` configuration option.

f
  Specifies the format of generated identicon. Overrides the
  ``PYDENTICON_FORMAT`` configuration option.

p
  Specifies the padding that will be added to the generated identicon image. The
  value should be provided as 4 comma-separated positive integers.

i
  Specifies whether the background and foreground colour in generated identicon
  should be inverted (swapped) or not. The value passed for this parameter
  should be ``true`` or ``false``.

Passing an invalid parameter value via *GET* parameter will result in a
``SuspiciousOperation`` exception being raised.

For example, the following request would generate an identicon with width of
``320``, height of ``240``, format ``PNG``, padding (top, bottom, left, right)
of ``10, 10, 20, 20``, and with inverted foreground and background colours::

  /identicon/image/somedata?w=320&h=240&f=png&p=10,10,20,20&i=true
