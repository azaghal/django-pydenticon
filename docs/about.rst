About Django Pydenticon
=======================

Django Pydenticon is a Django application that provides an identicon
generator. The implementation uses Pydenticon library for generating the
identicons:

* https://github.com/azaghal/pydenticon/
* https://projects.majic.rs/pydenticon

Django Pydenticon comes with some pre-defined sane defaults for generating the
identicons, but is configurable, letting the user generate identicons with
custom parameters.

Why was this application created?
---------------------------------

A number of web-based applications written in Python have a need for visually
differentiating between users by using avatars for each one of them.

This functionality is particularly popular with comment-posting since it
increases the readability of threads.

The problem is that lots of those applications need to allow anonymous users to
post their comments as well. Since anonymous users cannot set the avatar for
themselves, usually a random avatar is created for them instead.

There is a number of free (as in free beer) services out there that allow web
application developers to create such avatars. Unfortunately, this usually means
that the users visiting websites based on those applications are leaking
information about their browsing habits etc to these third-party providers.

Django Pydenticon was written in order to resolve such an issue for one of the
applications (Django Blog Zinnia, in particular), and to allow the author to set
up his own avatar/identicon service. It was developed to be used in combination
with Pydenticon library for generating identicons.

Features
--------

Django Pydenticon has the following features:

* Uses Pydentcion library for generating the identicons.
* User data used for generating the identicons is read from URL.
* Passed user data can be pre-hashed in order to avoid leakage of important
  information.
* All aspects of Pydenticon generator can be configured via project settings.
* Some parameters for generated identicons can be overridden per-request.
* Comes with sane default configuration options. No special configuration is
  necessary beyond installing and enabling the application in project.
