Installation
============

Django Pydenticon can be installed through one of the following methods:

* Using *pip*, which is the easiest and recommended way for production websites.

Requirements
------------

Django Pydenticon depends on the following Python packages:

* `Django <https://www.djangoproject.com/>`_ web framework.
* `Pydenticon <https://github.com/azaghal/pydenticon>`_ library, which is used for generating
  the identicons.

Using pip
---------

In order to install latest stable release of Django Pydenticon using *pip*, run
the following command::

  pip install django-pydenticon

In order to install the latest development version of Django Pydenticon from
Github, use the following command::

  pip install -e git+https://github.com/azaghal/django-pydenticon#egg=django_pydenticon

.. warning::

   You will need to update the ``pip`` installation in your virtual environment
   if you get the following error while running the above command::

     AttributeError: 'NoneType' object has no attribute 'skip_requirements_regex'

   You can update ``pip`` to latest version with::

     pip install -U pip

After this you should proceed to :ref:`configure your Django installation <configuring-django>`.

.. _configuring-django:

Configuring your Django installation
====================================

Once Django Pydenticon has been installed, you need to perform the following
steps in order to make it available inside of your Django project:

#. Edit your project's settings configuration file (``settings.py``), and update
   the ``INSTALLED_APPS`` to include application ``django_pydenticon``.

#. Edit your project's URL configuration file (``urls.py``), and add the
   following line to top of the file::

     import django_pydenticon.urls

#. Edit your project's URL configuration file (``urls.py``), and add the
   following line to the ``urlpatterns`` setting::

     url(r'^identicon/', include(django_pydenticon.urls.get_patterns())),

.. note::
   It is not mandatory to use ``identicon/`` as prefix. You can use any prefix
   as with any other Django application.

After this the Django Pydenticon application will be available under the
``/identicon/`` path (relative to your Django project's base URL), or under any
custom prefix path you have selected for deploying the application.

Where to go next?
=================

After Django Pydenticon has been installed, you should learn :ref:`how to use
the application <usage>`, and may also be intersted to change one of default
:ref:`configuration options <configuration>`.

.. warning::

   It is highly recommended to have a look at documentation covering
   :ref:`privacy <privacy>` if you have not done so before. The chapter covers
   some common privacy issues when using personally-identifiable information for
   generating identicons (like e-mails or names).
