"""Spinner utilities for tuiro."""

from __future__ import annotations

import sys
import threading
import time
from contextlib import contextmanager
from typing import TYPE_CHECKING

from .colors import Colors

if TYPE_CHECKING:
    from .tuiro import TUI


class Spinner:
    """Animated spinner for long-running operations.
    
    Displays a rotating animation during execution and shows
    a final status message when complete. Automatically degrades
    to static messages in CI mode or non-TTY environments.
    """

    FRAMES = "◐◓◑◒"

    def __init__(self, tui: TUI, message: str) -> None:
        """Initialize a spinner.

        Args:
            tui: The TUI instance for palette and CI mode.
            message: The message to display while spinning.
        """
        self.tui = tui
        self.message = message
        self.running = False
        self.thread: threading.Thread | None = None

    def start(self) -> None:
        """Start the spinner animation."""
        if self.tui.ci_mode or not sys.stdout.isatty():
            # In CI mode or non-TTY, just print the message statically (no animation)
            print(f"[*] {self.message}")
            return

        self.running = True
        self.thread = threading.Thread(target=self._spin, daemon=True)
        self.thread.start()

    def _spin(self) -> None:
        """Internal method that animates the spinner."""
        i = 0
        while self.running:
            frame = self.FRAMES[i % len(self.FRAMES)]
            c = self.tui.palette.info
            sys.stdout.write(f"\r{c}{frame}{Colors.RESET} {self.message}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

    def stop(self, status: str = "success", final_message: str | None = None) -> None:
        """Stop the spinner and show final status.

        Args:
            status: One of "success", "error", "warning", or "info".
            final_message: Optional message to display. Uses original message if None.
        """
        self.running = False
        if self.thread:
            self.thread.join()

        msg = final_message or self.message

        # In CI mode or non-TTY, don't clear the line
        # Just print the final status message directly
        if self.tui.ci_mode or not sys.stdout.isatty():
            # Show final status without clearing
            if status == "success":
                print(f"[OK] {msg}")
            elif status == "error":
                print(f"[ERROR] {msg}")
            elif status == "warning":
                print(f"[!] {msg}")
            else:
                print(f"[*] {msg}")
            return

        # In interactive mode, clear the spinner line and show colored status
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()

        # Show final status with colors
        if status == "success":
            self.tui.success(msg)
        elif status == "error":
            self.tui.error(msg)
        elif status == "warning":
            self.tui.warning(msg)
        else:
            self.tui.info(msg)

    def succeed(self, message: str | None = None) -> None:
        """Stop with success status."""
        self.stop(status="success", final_message=message)

    def fail(self, message: str | None = None) -> None:
        """Stop with error status."""
        self.stop(status="error", final_message=message)

    def warn(self, message: str | None = None) -> None:
        """Stop with warning status."""
        self.stop(status="warning", final_message=message)

    def __enter__(self):
        """Context manager entry."""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        if exc_type is not None:
            self.fail()
        else:
            self.succeed()
        return False