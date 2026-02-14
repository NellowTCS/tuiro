import sys
from . import TUI
from .version import __version__
from .palette import Palette, PROFILES


def main():
    args = sys.argv[1:]

    # Help
    if "--help" in args or "-h" in args:
        print("Usage: tuiro [--ci] [--no-color] [--theme NAME] [--help] [--version]")
        print("Available themes:", ", ".join(PROFILES.keys()))
        return

    # Version
    if "--version" in args:
        print(f"tuiro {__version__}")
        return

    # Flags
    force_ci = "--ci" in args
    force_no_color = "--no-color" in args

    # Theme
    theme = "default"
    if "--theme" in args:
        idx = args.index("--theme")
        if idx + 1 < len(args):
            theme = args[idx + 1]

    ci_mode = force_ci or force_no_color

    tui = TUI(ci_mode=ci_mode, theme=theme)

    tui.banner("tuiro")
    tui.section("Demo")
    tui.success("tuiro is installed and working!")
    tui.error("There is no error")
    tui.info("You are ready to build clean CLI scripts.")
    if ci_mode:
        tui.warning("CI mode active")
