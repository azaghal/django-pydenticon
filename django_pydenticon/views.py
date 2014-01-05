# Third-party Python library imports.
from pydenticon import Generator

# Django imports.
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

# Application imports.
from .settings import PYDENTICON_ROWS, PYDENTICON_COLUMNS, PYDENTICON_WIDTH, PYDENTICON_HEIGHT
from .settings import PYDENTICON_PADDING, PYDENTICON_FORMAT, PYDENTICON_FOREGROUND, PYDENTICON_BACKGROUND
from .settings import PYDENTICON_DIGEST, PYDENTICON_INVERT

def image(request, data):
    """
    Generates identicon image based on passed data.

    Arguments:

      data - Data which should be used for generating an identicon. This data
      will be used in order to create a digest which is used for generating the
      identicon. If the data passed is a hex digest already, the digest will be
      used as-is.

    Returns:

      Identicon image in raw format.
    """

    # Get image width, height, padding, and format from GET parameters, or
    # fall-back to default values from settings.
    try:
        width = int(request.GET.get("w", PYDENTICON_WIDTH))
    except ValueError:
        raise SuspiciousOperation("Identicon width must be a positive integer.")
    try:
        height = int(request.GET.get("h", PYDENTICON_HEIGHT))
    except ValueError:
        raise SuspiciousOperation("Identicon height must be a positive integer.")
    output_format = request.GET.get("f", PYDENTICON_FORMAT)
    try:
        padding = [int(p) for p in request.GET["p"].split(",")]
    except KeyError:
        padding = PYDENTICON_PADDING
    except ValueError:
        raise SuspiciousOperation("Identicon padding must consist out of 4 positive integers separated with commas.")
    if "i" in request.GET:
        inverted = request.GET.get("i")
        if inverted.lower() == "true":
            inverted = True
        elif inverted.lower() == "false":
            inverted = False
        else:
            raise SuspiciousOperation("Inversion parameter must be a boolean (true/false).")
    else:
        inverted = PYDENTICON_INVERT

    # Validate the input parameters.
    if not isinstance(width, int) or width <= 0:
        raise SuspiciousOperation("Identicon width must be a positive integer.")
    if not isinstance(height, int) or height <= 0:
        raise SuspiciousOperation("Identicon height must be a positive integer.")
    if not all([isinstance(p, int) and p >= 0 for p in padding]) or len(padding) != 4:
        raise SuspiciousOperation("Padding must be a 4-element tuple consisting out of positive integers.")

    # Set-up correct content type based on requested identicon format.
    if output_format == "png":
        content_type = "image/png"
    elif output_format == "ascii":
        content_type = "text/plain"
    else:
        raise SuspiciousOperation("Unsupported identicon format requested - '%s' % output_format")

    # Initialise a generator.
    generator = Generator(PYDENTICON_ROWS, PYDENTICON_COLUMNS,
                          foreground = PYDENTICON_FOREGROUND, background = PYDENTICON_BACKGROUND,
                          digest = PYDENTICON_DIGEST)

    # Generate the identicion.
    content = generator.generate(data, width, height, padding=padding, output_format=output_format, inverted=inverted)

    # Create and return the response.
    response = HttpResponse(content, content_type=content_type)

    return response
