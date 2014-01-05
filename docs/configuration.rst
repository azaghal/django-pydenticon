.. _configuration:

Configuration
=============

A number of configuration options can be set in Django project that affect the
identicon generation. Each configuration option comes with a default value
that's used if it's not specified explicitly in project settings.

The application will verify configuration options, and raise an
``ImproperlyConfigured`` exception in case of a problem.

``PYDENTICON_ROWS``
-------------------

Specifies how many *block* rows a generated identicon should have. The value
should be a positive integer.

**Default value:** ``5``

``PYDENTICON_COLUMNS``
----------------------

Specifies how many *block* columns a generated identicon should have. The value
should be a positive integer.

**Default value:** ``5``

``PYDENTICON_WIDTH``
--------------------

Specifies the width of generated identicon images in pixels (without
padding). The value should be a positive integer.

**Default value:** ``200``

``PYDENTICON_HEIGHT``
---------------------

Specifies the height of generated identicon images in pixels (without
padding). The value should be a positive integer.

**Default value:** ``200``

``PYDENTICON_PADDING``
----------------------

Specifies the padding that will be added to the generated identicon image. The
padding is specified as tuple containing 4 elements, where each element is a
positive integer.

Each element of the tuple is used for padding the identicon image along one of
the edges. The order is: *top*, *bottom*, *left*, *right*.

**Default value:** ``(20, 20, 20, 20)``

``PYDENTICON_FORMAT``
---------------------

Specifies the default format of the generated identicons. The value should be a
string. Supported values are:

* ``"png"`` (for PNG images)
* ``"ascii"`` (for ASCII/textual representation of identicon)

**Default value:** ``"png"``

``PYDENTICON_FOREGROUND``
-------------------------

Specifies a list or tuple of foreground colours that should be used when
generating the identicons. Each element of list/tuple should be a string
conformant to colour specification from the `Pillow
<http://pillow.readthedocs.org/en/latest/reference/ImageColor.html>`_ library.

**Default value:** ``("rgb(45,79,255)", "rgb(254,180,44)", "rgb(226,121,234)",
"rgb(30,179,253)", "rgb(232,77,65)", "rgb(49,203,115)", "rgb(141,69,170)")``

``PYDENTICON_BACKGROUND``
-------------------------

Specifies a (single) background colour that should be used when generating the
identicons. This should be a string conformant to colour specification from the
`Pillow <http://pillow.readthedocs.org/en/latest/reference/ImageColor.html>`_
library. The value should be a string.

**Default value:** ``"rgb(224,224,224)"``

``PYDENTICON_DIGEST``
---------------------

Specifies digest class that should be used for generating the identicons. Digest
class should support accepting a single constructor argument for passing the
data on which the digest will be run. Instances of the class should also support
a single hexdigest() method that should return a digest of passed data as a hex
string. The value should be a callable.

**Default value:** ``hashlib.md5``

``PYDENTICON_INVERT``
---------------------

Specifies whether the background and foreground colour in generated identicons
should be inverted (swapped) or not. The value should be a boolean (``True`` or
``False``).

**Default value:** ``False``
