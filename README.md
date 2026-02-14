# tuiro

tuiro is a tiny terminal UI helper designed for clean, readable, and structured output in build scripts and command‑line tools. It provides simple utilities for sections, banners, status messages, and command logging without introducing heavy dependencies or complex abstractions.

tuiro began as an internal utility inside the TactileBrowser project (https://github.com/NellowTCS/TactileBrowser). It is now available as a standalone library for any script or tool that wants clear and consistent terminal output.

## Features

- Lightweight and dependency‑free
- ANSI color support with automatic disabling in CI environments
- Section and subsection headers
- Informational, warning, success, and error messages
- Command logging for build steps
- Centered banners for high‑visibility output
- Fully typed and PEP 561 compliant

## Installation

```
pip install tuiro
```

For development:

```
uv pip install -e .
```

## Usage

Basic example:

```python
from tuiro import TUI

tui = TUI()
tui.banner("Build")
tui.section("Environment")
tui.info("Checking dependencies")
tui.success("All checks passed")
```

Example output (missing color sadly since GitHub doesn't support that):

```
╔══════════════════════════════════════════════════════════╗
║                          Build                           ║
╚══════════════════════════════════════════════════════════╝

────────────────────────────────────────────────────────────
  Environment
────────────────────────────────────────────────────────────
[*] Checking dependencies
[OK] All checks passed
```

## CLI

tuiro includes a small demonstration CLI:

```
tuiro
```

This is intended as a quick verification that the package is installed and functioning.

## API

### `TUI(ci_mode: bool = False)`

Creates a new terminal UI helper.  
Colors are automatically disabled when running in non‑interactive environments.

### `section(title: str)`

Prints a high‑visibility section header.

### `subsection(title: str)`

Prints a smaller subsection header.

### `banner(title: str)`

Prints a centered banner.

### `info(message: str)`
### `success(message: str)`
### `warning(message: str)`
### `error(message: str)`

Prints a formatted status message.

### `command(cmd: str | list[str])`

Prints a command being executed.

### `result(label: str, value: str)`

Prints a key‑value result line.

## License

MIT License. See (LICENSE)[LICENSE] for details.
