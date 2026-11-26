# Security Policy

## Supported versions

Only the latest version of Keel gets security fixes. Keel updates itself, so the fix reaches you through its normal
update check.

## Reporting a problem

Please **don't open a public issue** for a security problem.

Report it privately instead: on this repository's **Security** tab, choose **Report a vulnerability**. Only the
developer sees the report. Please include the Keel version (Keel › About Keel), your macOS version, and the steps
that show the problem.

You'll get a reply within 7 days. Once a fix is released, the release notes say what was fixed, and you're credited
if you'd like to be.

## What Keel already does

- **Keel's own updates** are signed with Keel's EdDSA key. Keel refuses an update whose signature doesn't verify.
- **Keel's app catalog** is signed with the same key, and Keel refuses a catalog that doesn't verify.
- **Updates of your apps** are checked before installing: the download's code signature and developer must match
  the copy you have, and a download signed less strongly than that copy is refused. Where the developer publishes
  a checksum or an EdDSA signature, Keel checks that too.
- **Backups:** Keel keeps the old version of every app it updates, so an update can be undone.
- **Your GitHub token**, if you add one, is kept in the macOS Keychain and sent only to api.github.com.

See also the [privacy policy](https://kavyamufc.github.io/keel-releases/privacy.html).
