# Changelog

All notable changes to tuiro will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2026-02-14

### Added
- **Spinner support** for long-running operations with animated circle quarters (◐◓◑◒)
  - Context manager usage: `with tui.spinner("Building"): ...`
  - Manual control: `spinner.start()`, `spinner.stop()`, `spinner.succeed()`, `spinner.fail()`, `spinner.warn()`
  - Automatic degradation to static messages in CI mode or non-TTY environments
  - Theme-aware coloring
- New `spinner.py` module containing the `Spinner` class

### Changed
- Bumped version to 0.2.0
- Updated README with comprehensive spinner documentation and examples
- Added "spinner" to package keywords

## [0.1.0] - 2026-02-14

### Added
- Initial release of tuiro
- Terminal UI utilities: sections, subsections, banners
- Status messages: info, success, warning, error
- Command logging and result output
- Simple two-column tables
- Step context manager for build phases
- Theme support with built-in themes: default, mono, pastel
- Custom palette support
- CI mode for color-free output
- Minimal CLI for testing and demonstration
- Zero dependencies

[0.2.0]: https://github.com/NellowTCS/tuiro/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/NellowTCS/tuiro/releases/tag/v0.1.0