# Standard Python library imports.
import collections
import hashlib

# Django imports
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Read project settings for Pydenticon, or fall-back to default values.
PYDENTICON_ROWS = getattr(settings, "PYDENTICON_ROWS", 5)
PYDENTICON_COLUMNS = getattr(settings, "PYDENTICON_COLUMNS", 5)
PYDENTICON_WIDTH = getattr(settings, "PYDENTICON_WIDTH", 200)
PYDENTICON_HEIGHT = getattr(settings, "PYDENTICON_HEIGHT", 200)
PYDENTICON_PADDING = getattr(settings, "PYDENTICON_PADDING", (20, 20, 20, 20))
PYDENTICON_FORMAT = getattr(settings, "PYDENTICON_FORMAT", "png")
PYDENTICON_FOREGROUND = getattr(settings, "PYDENTICON_FOREGROUND", ( "rgb(45,79,255)",
                                                                     "rgb(254,180,44)",
                                                                     "rgb(226,121,234)",
                                                                     "rgb(30,179,253)",
                                                                     "rgb(232,77,65)",
                                                                     "rgb(49,203,115)",
                                                                     "rgb(141,69,170)" ))
PYDENTICON_BACKGROUND = getattr(settings, "PYDENTICON_BACKGROUND", "rgb(224,224,224)")
PYDENTICON_DIGEST = getattr(settings, "PYDENTICON_DIGEST", hashlib.md5)
PYDENTICON_INVERT = getattr(settings, "PYDENTICON_INVERT", False)

# Validate the settings.
if not isinstance(PYDENTICON_ROWS, int) or PYDENTICON_ROWS <= 0:
    raise ImproperlyConfigured("Setting PYDENTICON_ROWS must be a positive integer.")

if not isinstance(PYDENTICON_COLUMNS, int) or PYDENTICON_COLUMNS <= 0:
    raise ImproperlyConfigured("Setting PYDENTICON_COLUMNS must be a positive integer.")

if not isinstance(PYDENTICON_WIDTH, int) or PYDENTICON_WIDTH <= 0:
    raise ImproperlyConfigured("Setting PYDENTICON_WIDTH must be a positive integer.")

if not isinstance(PYDENTICON_HEIGHT, int) or PYDENTICON_HEIGHT <= 0:
    raise ImproperlyConfigured("Setting PYDENTICON_HEIGHT must be a positive integer.")

if not all([isinstance(p, int) and p >= 0 for p in PYDENTICON_PADDING]) or len(PYDENTICON_PADDING) != 4:
    raise ImproperlyConfigured("Setting PYDENTICON_PADDING must be a 4-tuple where each element is a non-negative integer.")

if PYDENTICON_FORMAT not in ("png", "ascii"):
    raise ImproperlyConfigured("Setting PYDENTICON_FORMAT must be set to one of: 'png', 'ascii'.")

if not all([isinstance(f, str) for f in PYDENTICON_FOREGROUND]):
    raise ImproperlyConfigured("Setting PYDENTICON_FOREGROUND must be a tuple where each element is string representation of colour.")

if not isinstance(PYDENTICON_BACKGROUND, str):
    raise ImproperlyConfigured("Setting PYDENTICON_BACKGROUND must be a string representation of colour")

if not isinstance(PYDENTICON_DIGEST, collections.Callable):
    raise ImproperlyConfigured("Setting PYDENTICON_DIGEST must be a callable digest (usually from hashlib module).")

if not isinstance(PYDENTICON_INVERT, bool):
    raise ImproperlyConfigured("Setting PYDENTICON_INVERT must be a boolean.")
