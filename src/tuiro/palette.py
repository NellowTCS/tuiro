from .colors import Colors

class Palette:
    """Base color palette for tuiro."""
    info = Colors.CYAN
    success = Colors.GREEN
    warning = Colors.YELLOW
    error = Colors.RED
    accent = Colors.BRIGHT_BLUE
    dim = Colors.DIM
    text = Colors.BRIGHT_WHITE


class Mono(Palette):
    """Monochrome palette."""
    info = Colors.WHITE
    success = Colors.WHITE
    warning = Colors.WHITE
    error = Colors.WHITE
    accent = Colors.WHITE
    text = Colors.WHITE


class Pastel(Palette):
    """pristine pastel palette."""
    info = Colors.BRIGHT_CYAN
    success = Colors.BRIGHT_GREEN
    warning = Colors.BRIGHT_YELLOW
    error = Colors.BRIGHT_MAGENTA
    accent = Colors.BRIGHT_BLUE
    text = Colors.BRIGHT_WHITE

PROFILES = {
    "default": Palette,
    "mono": Mono,
    "pastel": Pastel,
}
