---
description: Find settings that no longer exist before they quietly stop working
---

# Checking the configuration

A key in `fylr.yml` that fylr does not know is ignored. Until version 6.35.0 it
was ignored silently: a typo, or a setting that a fylr upgrade renamed or
dropped, simply had no effect, and nothing said so. The configuration kept
looking configured.

**From version 6.35.0** every configuration file is checked against the settings
fylr actually has. Two kinds of key are reported:

* **unknown** — fylr has no such setting, so whatever it was meant to configure
  has no effect
* **deprecated** — the key still works, but it is on its way out; the report
  names what to use instead

The same list reaches you in three places.

## At startup

The server logs one warning per key and starts normally — a stale configuration
never keeps an instance from booting:

```
WRN Config: unknown key "fylr.services.webapp.prt" (from fylr.yml): fylr has no such setting, it has no effect
WRN Config: deprecated key "fylr.debug.disableHttp2Client" (from fylr.yml): use fylr.debug.http.disableHttp2, this key is still honored
```

## On the /inspect config page

`/inspect/config` shows the same keys in a **Config Problems** table, with the
configuration file each key stands in. The section only appears when there is
something to report.

## Without starting a server

`fylr config check` reads the configuration exactly the way the server does and
reports the keys without starting anything:

```bash
fylr config check fylr.yml
```

```
unknown key "fylr.services.webapp.prt" (from fylr.yml): fylr has no such setting, it has no effect
["fylr.yml"]: 1 unknown key(s), 0 deprecated key(s)
```

Pass the files in the same order as to the server (`fylr config check a.yml
b.yml`); they are merged on top of the built-in default configuration the same
way. The exit code is non-zero when a key is unknown or the configuration does
not load at all, so the command can guard a restart or run in a CI pipeline that
renders a configuration — a Kubernetes ConfigMap, for instance. `--strict` makes
it fail on deprecated keys as well.

Values are not the subject of this check: a value fylr cannot use, such as an
unparsable URL, keeps the server from starting anyway, and `fylr config check`
reports it too.

## What is checked, and what is not

Every file is checked on its own, so the file a stale key stands in is named
even when a later file overwrites the key or removes it again.

Configuration set with `-s` on the command line is checked the same way: a path
that does not exist in the configuration is reported instead of ignored.
Environment variables are not checked, because a container commonly carries
`FYLR_` prefixed variables that are not meant to be configuration.
