Release notes
=============

0.2
---

Update introduces support for Django 1.8+ and some documentation improvements.

New features:

* `DJPYD-7: Update application for use in Django 1.8, 1.9, and Django 1.10
  <https://projects.majic.rs/django-pydenticon/issues/DJPYD-7>`_

  Minimum requirement for Django is now 1.8.x. Fixes are compatible with Django
  1.9.x and 1.10.x as well.

Enhancements:

* `DJPYD-8: Update Pydenticon requirement to version 0.3
  <https://projects.majic.rs/django-pydenticon/issues/DJPYD-8>`_

  Introduced explicit dependency on Pydenticon 0.3, which also introduces
  ability to handle transparency in PNGs.

0.1
---

Initial release of Django Pydenticon. Implemented features:

* Serving of identicons through designated URL.
* User data for generating identicons passed via URL.
* Sane configuration defaults for identicon generator for zero-configuration.
* Ability to set parameters of generated identicons.
* Ability to override some of the identicon generation attributes per-request
  via *GET* parameters.
* Full documentation covering installation, usage, privacy. API reference
  included as well.
