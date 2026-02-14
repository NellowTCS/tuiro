from . import TUI

def main():
    tui = TUI()
    tui.banner("tuiro")
    tui.section("Demo")
    tui.success("tuiro is installed and working!")
    tui.info("You're ready to build beautiful CLI scripts.")
