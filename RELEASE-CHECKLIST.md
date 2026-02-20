# Release Checklist (macOS Signed + Notarized)

Use this checklist when preparing a distributable macOS build that avoids Gatekeeper warnings.

## 1) Apple prerequisites

- Active Apple Developer Program membership
- Team ID available
- App-specific password created for your Apple ID (recommended)
- Certificates installed in Keychain:
  - Developer ID Application
  - Developer ID Installer (optional for PKG flows; DMG usually only needs Application cert)

## 2) Local machine prerequisites

- Xcode Command Line Tools installed
- `electron-builder` dependencies installed (`npm install` already done in this project)
- Signing identity visible:
  - `security find-identity -v -p codesigning`

## 3) Environment variables (shell/CI secrets)

Set these before running release builds:

- `APPLE_ID` = your Apple ID email
- `APPLE_APP_SPECIFIC_PASSWORD` = app-specific password
- `APPLE_TEAM_ID` = Apple developer Team ID
- `CSC_NAME` = exact signing identity name (Developer ID Application)

Optional (if using a certificate file in CI):

- `CSC_LINK` = base64/P12 path or URL
- `CSC_KEY_PASSWORD` = P12 password

## 4) Build and sign

- Build command (current project):
  - `npm run dist:mac`
- Current output target:
  - arm64 DMG only (smallest practical artifact for this project)

Expected output path:

- `dist/QLab Timer-<version>-arm64.dmg`

## 5) Notarization + staple verification

`electron-builder` notarizes automatically on macOS when Apple env vars are set.

After build completes:

- Verify app signature:
  - `codesign --verify --deep --strict --verbose=2 "dist/mac-arm64/QLab Timer.app"`
- Verify notarization ticket:
  - `xcrun stapler validate "dist/QLab Timer-<version>-arm64.dmg"`
- Gatekeeper assessment:
  - `spctl -a -vv "dist/mac-arm64/QLab Timer.app"`

## 6) Final release sanity checks

- Launch app on a clean machine/user profile
- Confirm Companion host/IP and connection label defaults
- Confirm timer updates smoothly with QLab `Use Tenths?` OFF
- Confirm fullscreen and settings panel actions
- Confirm on-screen version matches package version

## Notes on installer size

- Electron bundles Chromium + Node runtime, so installer sizes around ~80–120MB for single-arch mac builds are normal.
- This project already uses size-minimizing settings:
  - arm64-only
  - DMG-only
  - maximum compression
