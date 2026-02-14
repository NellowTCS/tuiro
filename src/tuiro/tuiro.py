"""tuiro: tiny terminal UI utility for clean, colorful build output."""

from __future__ import annotations

import shutil
import sys
from contextlib import contextmanager
from .colors import Colors
from .palette import PROFILES, Palette


class TUI:
    """Core TUI class for the tuiro terminal UI library.

    Provides structured terminal output for build scripts,
    developer tooling, and lightweight CLIs.
    """

    def __init__(self, ci_mode: bool = False, theme: str | Palette = "default") -> None:
        """Initialize the TUI.

        Args:
            ci_mode: If True, disable colors.
            theme: A theme name or a Palette subclass.
        """
        self.ci_mode = ci_mode

        if isinstance(theme, str):
            theme_cls = PROFILES.get(theme, PROFILES["default"])
            self.palette = theme_cls()
        else:
            self.palette = theme()

        if ci_mode or not sys.stdout.isatty():
            Colors.disable()

    # ------------------------------------------------------------
    # Sections and headings
    # ------------------------------------------------------------

    def section(self, title: str) -> None:
        width = shutil.get_terminal_size().columns
        width = max(40, min(width, 120))
        line = "─" * width
        c = self.palette.accent
        print(f"\n{c}{Colors.BOLD}{line}{Colors.RESET}")
        print(f"{c}{Colors.BOLD}  {title}{Colors.RESET}")
        print(f"{c}{Colors.BOLD}{line}{Colors.RESET}")

    def subsection(self, title: str) -> None:
        c = self.palette.accent
        print(f"\n{c}{Colors.BOLD}▶ {title}{Colors.RESET}")

    # ------------------------------------------------------------
    # Message types
    # ------------------------------------------------------------

    def success(self, message: str) -> None:
        print(f"{self.palette.success}[OK]{Colors.RESET} {message}")

    def info(self, message: str) -> None:
        print(f"{self.palette.info}[*]{Colors.RESET} {message}")

    def warning(self, message: str) -> None:
        print(f"{self.palette.warning}[!]{Colors.RESET} {message}")

    def error(self, message: str) -> None:
        print(f"{self.palette.error}[ERROR]{Colors.RESET} {message}")

    # ------------------------------------------------------------
    # Utility output
    # ------------------------------------------------------------

    def command(self, cmd: str | list[str]) -> None:
        cmd_str = " ".join(cmd) if isinstance(cmd, list) else cmd
        print(f"{self.palette.dim}$ {cmd_str}{Colors.RESET}")

    def result(self, label: str, value: str) -> None:
        print(f"{self.palette.text}{label}:{Colors.RESET} {value}")

    def table(self, rows: list[tuple[str, str]]) -> None:
        if not rows:
            return
        left_width = max(len(label) for label, _ in rows)
        for label, value in rows:
            print(f"{label.ljust(left_width)}  {value}")

    # ------------------------------------------------------------
    # Banner
    # ------------------------------------------------------------

    def banner(self, title: str) -> None:
        width = shutil.get_terminal_size().columns
        width = max(40, min(width, 120))
        c = self.palette.accent

        print(f"\n{c}{Colors.BOLD}")
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
    # Step context manager
    # ------------------------------------------------------------

    @contextmanager
    def step(self, title: str):
        self.info(f"{title}...")
        try:
            yield
            self.success(f"{title} completed")
        except Exception:
            self.error(f"{title} failed")
            raise

    # ------------------------------------------------------------
    # Representation
    # ------------------------------------------------------------

    def __repr__(self) -> str:
        return "<tuiro.TUI: aesthetic terminal UI helper>"
