import os
import sys
from . import TUI

def main():
    args = sys.argv[1:]

    if "--ci" in args:
        ci = True

    tui = TUI(ci_mode=ci)

    tui.banner("tuiro")
    tui.section("Demo")
    tui.success("tuiro is installed and working!")
    tui.info("You're ready to build beautiful CLI scripts.")
    if ci:
        tui.warning("CI mode active!")
