# Keel

Keel keeps the apps on your Mac up to date, and checks every download before it installs it: the developer's
signature or checksum has to match, and the new copy has to come from the same developer as the one you have.
It also covers Homebrew packages and macOS updates, and keeps a backup so you can undo an update.

Keel is free.

## Download

**[Download Keel (Keel-latest.dmg)](https://kavyamufc.github.io/keel-releases/Keel-latest.dmg)**

Keel updates itself after that.

## Install

1. Open `Keel-latest.dmg` and drag **Keel** to **Applications**.
2. Open Keel. The first time, macOS stops it because Keel isn't notarized by Apple yet: open
   **System Settings › Privacy & Security**, scroll down and click **Open Anyway** next to the message about Keel,
   then confirm.
3. Turn on **App Management**, so Keel can replace apps when it updates them: **System Settings › Privacy & Security ›
   App Management**, turn on Keel (or click **+** and choose Keel from Applications). Keel's Permissions page shows
   whether it is on.

## Feedback

- [Report a bug](https://github.com/kavyamufc/keel-releases/issues/new?template=bug_report.yml)
- [Suggest a feature](https://github.com/kavyamufc/keel-releases/issues/new?template=feature_request.yml)

In Keel, **Help › Send Feedback…** opens a bug report with your Keel and macOS versions filled in. Keel sends nothing
itself.

## For Keel itself

- Update feed: `https://kavyamufc.github.io/keel-releases/appcast.xml`
- Every zip in the feed is signed with Keel's EdDSA key; Keel refuses any update that doesn't verify. The DMGs
  (`Keel-latest.dmg`, `downloads/`) are for first installs and aren't part of the feed.
