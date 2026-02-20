# Copilot Instructions

This project is a minimal webpage that displays a Bitfocus Companion variable for QLab cue **time remaining**.

## Current Goal

- Keep a single `index.html` as the main working file.
- Wrap the single-page app as a self-contained desktop app for macOS and Windows using Electron.
- Display four Companion variables in a fixed layout:
	- Top-left: current time (`$(internal:time_hms)`)
	- Top center near the top: current cue name (`$(qlabfb-local:r_name)`)
	- Next-line close under cue name: cue notes (`$(qlabfb-local:r_notes)`)
	- Center middle (large): countdown/time remaining (`$(qlabfb-local:r_left)`)
	- Center bottom (next-line close to countdown): elapsed time (`$(qlabfb-local:e_time)`)
	- Bottom center: next cue info (`$(qlabfb-local:n_name)`)
- Add top-right icons for:
	- Fullscreen toggle
	- Open settings panel
- Settings panel (slide-in from right, half-overlay) should include:
	- Set background color
	- Set font color
	- Companion Host/IP setting (default `127.0.0.1`)
	- Default colors button (black background, white font)
	- Inverse colors button (white background, black font)
	- Companion QLab Connection Label setting (default `qlabfb`)
	- Visibility toggles for: cue name, notes, elapsed time, next cue, and clock
	- Collapsible setup instructions at the bottom (below Save), including where to find the QLab label, Companion Host/IP usage guidance, and guidance to keep `Use Tenths?` OFF
	- Centered logo below instructions: `https://www.desertdog.nl/images/logo/logo_full_white.png`
	- Centered Buy Me a Coffee button below the logo: `https://www.buymeacoffee.com/desertdog`
	- Instructions text should use comfortable spacing/line-height for readability
	- Settings panel text should stay white regardless of selected page font color
- Show current app version on screen (bottom-right) for quick benchmark/build identification.
- Show `DeserDog` in the bottom-left corner of the timer page using small text style (matching version text size).
- Keep implementation simple (no frontend frameworks/build step for the UI; Electron packaging is allowed).
- Keep settings integrated in `index.html` (no separate `settings.html`).

## Working Assumptions (to update when new info arrives)

- Companion is reachable over HTTP on the same network.
- Companion API port is likely `8000` (confirm if different).
- Confirmed Companion connection label is `qlabfb-local`.
- Default configurable Companion connection label in settings is `qlabfb`.
- Default configurable Companion Host/IP in settings is `127.0.0.1`.
- Default visibility settings are:
	- Show current cue name: ON
	- Show notes: OFF
	- Show elapsed time: OFF
	- Show next cue: OFF
	- Show clock: ON
- Confirmed cue-name variable reference is `$(qlabfb-local:r_name)`.
- Confirmed cue-notes variable reference is `$(qlabfb-local:r_notes)`.
- Confirmed time-left variable reference is `$(qlabfb-local:r_left)` (label `qlabfb-local`, name `r_left`).
- Confirmed elapsed-time variable reference is `$(qlabfb-local:e_time)`.
- Confirmed next-cue variable reference is `$(qlabfb-local:n_name)`.
- Confirmed internal clock variable reference is `$(internal:time_hms)`.
- Buy Me a Coffee button target is `https://www.buymeacoffee.com/desertdog` and appears centered below the settings logo.
- Bottom-left timer page helper label text is `DeserDog`.
- Documented Companion HTTP route for module variables is `GET /api/variable/<connectionLabel>/<name>/value`.
- Browser can reach Companion directly (CORS/network/firewall may need adjustment).

## Known Behavior / Benchmarks

- Baseline smooth behavior: timer display updates smoothly at 1-second pace when QLab module setting `Use Tenths?` is **OFF**.
- Observed stutter behavior: when `Use Tenths?` is **ON**, updates can be irregular (sometimes too fast, sometimes delayed), causing visible stutter.
- Active benchmark cadence in code is `pollMs = 1000` (fixed interval), matching rollback target `v0.2.2`.
- Adaptive strategy from `v1.0.0` was tested and rolled back due to unsatisfactory behavior in practice.
- Treat `v0.2.2` as the current stable benchmark.

## Update Rules

When new user instructions or environment details are provided:

1. Update `index.html` to match the new requirement.
2. Update this file's assumptions and goals.
3. Add a new dated entry in `CHANGELOG.md` describing the change.

## Implementation Notes

- Prefer small, targeted edits.
- Avoid adding dependencies unless explicitly requested (Electron/electron-builder are now explicitly requested for desktop packaging).
- For this project, read values directly from:
	- `/api/variable/qlabfb-local/r_name/value`
	- `/api/variable/qlabfb-local/r_notes/value`
	- `/api/variable/qlabfb-local/r_left/value`
	- `/api/variable/internal/time_hms/value`
	- `/api/variable/qlabfb-local/e_time/value`
	- `/api/variable/qlabfb-local/n_name/value`
- Desktop app packaging commands:
	- `npm start` (run Electron app locally)
	- `npm run dist:mac` (build minimized macOS installer artifact: arm64 DMG only)
	- `npm run dist:win` (build Windows installer artifacts; recommended on Windows or CI)
- Signed/notarized mac release steps are documented in `RELEASE-CHECKLIST.md`.  
- For GitHub publishing, keep source code only; publish installers separately outside git.