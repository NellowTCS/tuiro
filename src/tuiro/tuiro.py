"""tuiro: tiny terminal UI utility for clean, colorful build output."""

from __future__ import annotations
import sys
from .colors import Colors


class TUI:
    """Core TUI class for the tuiro terminal UI library.

    Provides structured terminal output for build scripts,
    developer tooling, and lightweight CLIs.
    """

    def __init__(self, ci_mode: bool = False) -> None:
        """Initialize the TUI.

        Args:
            ci_mode: If True, disable colors (useful for CI environments).
        """
        self.ci_mode = ci_mode
        if ci_mode or not sys.stdout.isatty():
            Colors.disable()

    # ------------------------------------------------------------
    # Sections & Headings
    # ------------------------------------------------------------

    def section(self, title: str) -> None:
        """Print a section header."""
        line = "─" * 60
        print(f"\n{Colors.CYAN}{Colors.BOLD}{line}{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}  {title}{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}{line}{Colors.RESET}")

    def subsection(self, title: str) -> None:
        """Print a subsection header."""
        print(f"\n{Colors.BRIGHT_BLUE}{Colors.BOLD}▶ {title}{Colors.RESET}")

    # ------------------------------------------------------------
    # Message Types
    # ------------------------------------------------------------

    def success(self, message: str) -> None:
        """Print a success message."""
        print(f"{Colors.GREEN}[OK]{Colors.RESET} {message}")

    def info(self, message: str) -> None:
        """Print an informational message."""
        print(f"{Colors.CYAN}[*]{Colors.RESET} {message}")

    def warning(self, message: str) -> None:
        """Print a warning message."""
        print(f"{Colors.YELLOW}[!]{Colors.RESET} {message}")

    def error(self, message: str) -> None:
        """Print an error message."""
        print(f"{Colors.RED}[ERROR]{Colors.RESET} {message}")

    # ------------------------------------------------------------
    # Utility Output
    # ------------------------------------------------------------

    def command(self, cmd: str | list[str]) -> None:
        """Print a command being executed."""
        cmd_str = " ".join(cmd) if isinstance(cmd, list) else cmd
        print(f"{Colors.DIM}$ {cmd_str}{Colors.RESET}")

    def result(self, label: str, value: str) -> None:
        """Print a key-value result."""
        print(f"{Colors.BRIGHT_WHITE}{label}:{Colors.RESET} {value}")

    # ------------------------------------------------------------
    # Banner
    # ------------------------------------------------------------

    def banner(self, title: str) -> None:
        """Print a centered banner."""
        width = 60
        print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}")
        print("╔" + "═" * (width - 2) + "╗")
        padding = (width - 2 - len(title)) // 2
        print(
            "║"
            + " " * padding
            + title
            + " " * (width - 2 - padding - len(title))
            + "║"
        )
        print("╚" + "═" * (width - 2) + "╝")
        print(f"{Colors.RESET}")

    # ------------------------------------------------------------
    # Representation
    # ------------------------------------------------------------

    def __repr__(self) -> str:
        return "<tuiro.TUI: aesthetic terminal UI helper>"
