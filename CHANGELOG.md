# Changelog

All notable changes to this project will be documented in this file.

## Versioning

- This project now uses explicit versions in this changelog.
- Format: `vMAJOR.MINOR.PATCH`.
- Use a new version entry for each meaningful change so behavior can be compared across versions.

## [v0.3.14] - 2026-02-20

### Changed

- Switched GitHub publishing policy to source-only (no installer artifacts in git).
- Updated `.gitignore` to ignore entire `dist/` output.
- Updated project instructions to publish installers separately outside the repository.

## [v0.3.13] - 2026-02-20

### Added

- Added `.gitignore` rules to publish source plus selected distributables only:
	- include `dist/mac-arm64/QLab Timer.app/**`
	- include `dist/*.exe`
	- exclude other `dist` outputs

### Changed

- Updated project instructions with GitHub publishing artifact scope.

## [v0.3.12] - 2026-02-20

### Added

- Added `RELEASE-CHECKLIST.md` with a practical macOS signed/notarized release flow:
	- Apple prerequisites and certificate requirements
	- required signing/notarization environment variables
	- build/sign/notarize verification commands
	- final release sanity checks

### Changed

- Linked the release checklist from project instructions.
- Updated on-screen app version label to `v0.3.12`.
- Updated package version metadata to `0.3.12`.

## [v0.3.11] - 2026-02-20

### Changed

- Optimized mac packaging for smaller output:
	- mac target now builds `DMG` only (removed `ZIP`)
	- mac build limited to `arm64` architecture
	- enabled `electron-builder` compression mode `maximum`
- Updated package version metadata to `0.3.11`.
- Updated on-screen app version label to `v0.3.11`.

## [v0.3.10] - 2026-02-20

### Changed

- Removed legacy `settings.html` and kept settings fully integrated in `index.html`.
- Updated Electron packaging file list to remove `settings.html`.
- Updated on-screen app version label to `v0.3.10`.
- Updated project/package version metadata to `0.3.10`.

## [v0.3.9] - 2026-02-20

### Added

- Added Electron desktop app scaffold for self-contained macOS and Windows builds:
	- `package.json` with `electron` + `electron-builder` scripts/config
	- `main.js` Electron main process loading `index.html`

### Changed

- Updated on-screen app version label to `v0.3.9`.
- Updated project instructions with desktop run/build commands for Electron packaging.

## [v0.3.8] - 2026-02-20

### Changed

- Updated default settings to:
	- Companion QLab Connection Label: `qlabfb`
	- Companion Host/IP: `127.0.0.1`
	- Show current cue name: ON
	- Show notes: OFF
	- Show elapsed time: OFF
	- Show next cue: OFF
	- Show clock: ON
- Updated on-screen app version label to `v0.3.8`.

## [v0.3.7] - 2026-02-20

### Added

- Added `Companion Host/IP` setting (default `127.0.0.1`) in the settings panel.

### Changed

- Main page API requests now use the configured Companion Host/IP, enabling use from another computer on the same network.
- Updated on-screen app version label to `v0.3.7`.

## [v0.3.6] - 2026-02-20

### Changed

- Made the settings Save button more prominent with stronger contrast, full-width layout, and clearer hover/focus states.
- Updated on-screen app version label to `v0.3.6`.

## [v0.3.5] - 2026-02-20

### Changed

- Improved readability of the settings instructions block using more comfortable typography spacing:
	- Increased content padding
	- Increased line-height (targeted for easier reading)
	- Added clearer spacing between list items and summary/content
- Updated on-screen app version label to `v0.3.5`.

## [v0.3.4] - 2026-02-20

### Added

- Added centered logo below the instructions section in the settings panel:
	- `https://www.desertdog.nl/images/logo/logo_full_white.png`

### Changed

- Updated on-screen app version label to `v0.3.4`.

## [v0.3.3] - 2026-02-20

### Changed

- Moved collapsible setup instructions to the bottom of the settings panel, below the Save button.
- Rewrote instructions to explain what each setting does and how to use it.
- Added explicit guidance on where to find the Companion QLab connection label (Companion → Connections).
- Added explicit recommendation to keep `Use Tenths?` set to `OFF` for smoother timer updates.
- Updated on-screen app version label to `v0.3.3`.

## [v0.3.2] - 2026-02-20

### Fixed

- Settings panel font color is now fixed to white, independent of selected page font color.

### Changed

- Updated on-screen app version label to `v0.3.2`.

## [v0.3.1] - 2026-02-20

### Changed

- Replaced separate settings-page flow with a slide-in right-side settings panel that half-overlays the timer page.
- Reordered settings so Companion QLab Connection Label appears at the top.
- Moved color pickers to the bottom and added adjacent `B/W` and `W/B` quick color buttons.
- Added extra top margin to the Save button.

## [v0.3.0] - 2026-02-20

### Added

- Settings page now includes:
	- Default colors button (sets background to black and font to white)
	- Companion QLab Connection Label input (default `qlabfb`)
	- Visibility toggles for current cue name, notes, elapsed time, next cue, and clock

### Changed

- Main page now reads QLab variables using the configured connection label from settings.
- Main page now shows/hides cue name, notes, elapsed, next cue, and clock based on settings toggles.
- Updated on-screen app version label to `v0.3.0`.

## [v0.2.9] - 2026-02-20

### Fixed

- Fixed top-right icon click behavior by raising control z-index above page overlays.
- Wired settings icon to explicit navigation to `settings.html`.
- Kept fullscreen icon wired to browser fullscreen toggle.

### Changed

- Updated on-screen app version label to `v0.2.9`.

## [v0.2.8] - 2026-02-20

### Added

- Added two top-right icons on the timer page:
	- Fullscreen toggle
	- Settings page shortcut
- Added new `settings.html` page with:
	- Background color setting
	- Font color setting
	- Collapsible section with usage instructions

### Changed

- Timer page now applies saved background/font colors from settings via `localStorage`.
- Updated on-screen app version label to `v0.2.8`.

## [v0.2.7] - 2026-02-20

### Changed

- Kept current time in top-left corner.
- Moved cue name and cue notes to top-center and centered their text.
- Updated on-screen app version label to `v0.2.7`.

## [v0.2.6] - 2026-02-20

### Changed

- Moved cue name and cue notes from center stack to the top-left area.
- Positioned cue name and notes directly under current time with tight next-line spacing.
- Kept countdown and elapsed time centered.
- Updated on-screen app version label to `v0.2.6`.

## [v0.2.5] - 2026-02-20

### Changed

- Converted displayed variable fields in the center stack to individual `div` elements for independent spacing control.
- Reduced spacing so cue notes render as an immediate next line under cue name.
- Reduced spacing so elapsed time renders as an immediate next line under remaining time.
- Updated on-screen app version label to `v0.2.5`.

## [v0.2.4] - 2026-02-20

### Changed

- Removed cue state display and variable usage (`$(qlabfb-local:r_stat)`).
- Moved cue notes (`$(qlabfb-local:r_notes)`) directly under cue name.
- Tightened spacing so elapsed time sits closer under remaining time.
- Updated on-screen app version label to `v0.2.4`.

## [v0.2.3] - 2026-02-20

### Changed

- Moved elapsed time closer to the countdown display.
- Added current cue state above countdown using `$(qlabfb-local:r_stat)`.
- Added running cue notes under cue state using `$(qlabfb-local:r_notes)`.
- Added next cue info at the bottom using `$(qlabfb-local:n_name)`.
- Updated on-screen app version label to `v0.2.3`.

## [Rollback to v0.2.2] - 2026-02-20

### Changed

- Reverted adaptive-sync implementation from `v1.0.0`.
- Restored fixed `1000ms` polling behavior used by `v0.2.2`.
- Restored on-screen app version label to `v0.2.2`.

### Notes

- This rollback is now the active working baseline.

## [v0.2.2] - 2026-02-20

### Added

- Added a visible on-screen version label in `index.html` (bottom-right) for quick benchmark/build identification.

### Notes

- Current displayed version label is `v0.2.2`.

## [v0.2.1] - 2026-02-20

### Changed

- Set `pollMs` to `1000` in `index.html` to enforce 1-second polling cadence.

### Notes

- Marked as benchmark rollback point for smooth mode testing with `Use Tenths? OFF`.
- If future timing changes regress smoothness, return to `v0.2.1` settings.

## [v0.2.0] - 2026-02-20

### Changed

- Reworked `index.html` layout to requested structure:
	- Top-left: current time
	- Center top: cue name
	- Center middle (large): countdown/time remaining
	- Center bottom: elapsed time
- Replaced single-variable fetch logic with four Companion variable reads using documented endpoint `GET /api/variable/<connectionLabel>/<name>/value`.

### Added

- Added support for these variables:
	- `$(internal:time_hms)`
	- `$(qlabfb-local:r_name)`
	- `$(qlabfb-local:r_left)`
	- `$(qlabfb-local:e_time)`

## [v0.1.1] - 2026-02-20

### Added

- Added benchmark note: current implementation is considered smooth when Companion QLab setting `Use Tenths?` is `OFF`.
- Added observed behavior note: enabling `Use Tenths?` can cause irregular update cadence and visible stutter.

### Notes

- Use `v0.1.1` as the reference baseline when validating future UI/update-timing changes.

## [v0.1.0] - 2026-02-20

### Added

- Created `index.html` with a minimal live dashboard for showing a Companion variable as QLab cue time remaining.
- Added configurable Companion connection settings (`host`, `port`, `protocol`, `variableName`, polling interval).
- Implemented polling with fallback API endpoint list and flexible variable extraction logic.
- Added `.github/copilot-instructions.md` with project goals, assumptions, and update rules.

### Changed

- Updated `index.html` to use confirmed variable `$(qlabfb-local:r_left)`.
- Improved variable matching logic to support both wrapped and unwrapped forms (for compatibility with Companion payload formats).
- Updated `.github/copilot-instructions.md` with confirmed connection label and variable details.
- Switched variable fetching to Companion documented endpoint: `GET /api/variable/<connectionLabel>/<name>/value`.
- Simplified `index.html` config to explicit `connectionLabel` + `variableName` (`qlabfb-local` + `r_left`).