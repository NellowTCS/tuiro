# tuiro

tuiro is a tiny terminal UI helper designed for clean, readable, and structured output in build scripts and command‑line tools. It provides simple utilities for sections, banners, status messages, command logging, spinners, and themed output without introducing heavy dependencies or complex abstractions.

> tuiro began as an internal utility inside the [TactileBrowser](https://github.com/NellowTCS/TactileBrowser) project. It is now available as a standalone library for any script or tool that wants clear and consistent terminal output.

## Features

- Lightweight and dependency‑free
- ANSI color support with optional CI mode
- Built‑in themes and user‑defined palettes
- Section and subsection headers
- Informational, warning, success, and error messages
- Command logging for build steps
- Animated spinners for long-running operations
- Centered banners with automatic terminal width detection
- A simple step context manager for build phases
- A minimal CLI for quick verification and theme testing

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

Example output (colors omitted):

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

### Spinners

Spinners provide visual feedback for long-running operations:

```python
# Context manager (automatic success)
with tui.spinner("Downloading packages"):
    download()

# Context manager with custom message
with tui.spinner("Building project") as s:
    build()
    s.succeed("Build completed in 3.2s")

# Manual control
spinner = tui.spinner("Running tests")
spinner.start()
run_tests()
spinner.stop(status="success", final_message="42 tests passed")

# Convenience methods
spinner.succeed("Done!")
spinner.fail("Something went wrong")
spinner.warn("Completed with warnings")
```

Spinners automatically degrade to static messages in CI mode or non-TTY environments.

## Themes

tuiro supports both built‑in themes and user‑defined palettes.

### Built‑in themes

- default  
- mono  
- pastel  

Use a theme by name:

```python
tui = TUI(theme="pastel")
```

### Custom palettes

Palettes live in `tuiro.palette`. Users can define their own palette by subclassing `Palette`:

```python
from tuiro.palette import Palette
from tuiro.colors import Colors

class MyPalette(Palette):
    success = Colors.BRIGHT_GREEN
    info = Colors.BRIGHT_CYAN
```

Then pass it to TUI:

```python
tui = TUI(theme=MyPalette)
```

or:

```python
tui = TUI(theme=MyPalette())
```

Note: The CLI `--theme` flag accepts only built‑in theme names from `PROFILES`. Custom palettes must be provided from Python code.

## CLI

tuiro includes a small demonstration CLI:

```
tuiro
```

Flags:

```
tuiro --ci
tuiro --no-color
tuiro --theme pastel
tuiro --help
tuiro --version
```

Behavior:

- `--ci` disables colors
- `--no-color` also disables colors
- If both are provided, colors remain disabled
- `--theme NAME` selects a built‑in theme
- `--help` lists available themes

Example:

```
tuiro --ci --theme mono
```

## API

### `TUI(ci_mode: bool = False, theme: str | Palette = "default")`

Creates a new terminal UI helper.

### `section(title: str)`

Prints a high‑visibility section header.

### `subsection(title: str)`

Prints a smaller subsection header.

### `banner(title: str)`

Prints a centered banner.

### Status messages

```
info(message: str)
success(message: str)
warning(message: str)
error(message: str)
```

### `command(cmd: str | list[str])`

Prints a command being executed. Lists are joined with spaces.

### `result(label: str, value: str)`

Prints a key‑value result line.

### `table(rows: list[tuple[str, str]])`

Prints a simple two‑column table aligned on the left column.

### `spinner(message: str) -> Spinner`

Creates an animated spinner for long-running operations. Returns a `Spinner` instance that can be used as a context manager or controlled manually.

**Context manager usage:**
```python
with tui.spinner("Processing"):
    do_work()
```

**Manual usage:**
```python
spinner = tui.spinner("Processing")
spinner.start()
do_work()
spinner.succeed("Done!")
```

**Spinner methods:**
- `start()`: Begin animation
- `stop(status="success", final_message=None)`: Stop and show status
- `succeed(message=None)`: Stop with success status
- `fail(message=None)`: Stop with error status
- `warn(message=None)`: Stop with warning status

### `step(title: str)`

Context manager for build steps:

```python
with tui.step("Compiling"):
    run_compiler()
```

## License

MIT License. See [LICENSE](LICENSE) for details.
