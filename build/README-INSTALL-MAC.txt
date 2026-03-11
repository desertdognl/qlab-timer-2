QLab Timer macOS install notes

If macOS says the app is damaged or should be moved to Trash, this is usually
Gatekeeper blocking an unsigned app distributed outside the App Store.

Install steps:
1. Open the DMG and drag QLab Timer to Applications.
2. Eject the DMG.
3. In Finder, go to Applications.
4. Right-click QLab Timer.app and choose Open.
5. Click Open again in the security prompt.

If the app is still blocked, run this Terminal command once:

xattr -dr com.apple.quarantine "/Applications/QLab Timer.app"

Then open the app again.

Optional check in System Settings:
- Privacy & Security -> allow the blocked app if an allow button is shown.

Note:
A fully trusted, warning-free distribution requires Apple code signing and
notarization (Apple Developer account).
