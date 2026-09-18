---
description: >-
  An upload fails with "No location configured", although a default location is
  configured
---

# No location configured

## Symptoms

Uploading a file fails, and the message says that no location is configured for
`originals`:

```
NewLocationKey: No location configured for "originals"
```

Installing a plugin shows the same thing, wrapped in the steps that lead to it —
a plugin's zip is stored like any other file:

```
Unable to copy file: Error uploading file: storing location: NewLocationKey: No location configured for "originals"
```

`System > Locations` shows a default location for `originals` all the same.
Creating a backup can fail the same way, then naming `backups`.

## Causes

Each of the three storage roles — `originals`, `versions` and `backups` — points
at one location. fylr can only use that location if it is writable and still
exists. Two situations leave a role without one although the setting is filled
in:

* the location is **read only**. A location attached from a migrated instance is
  the usual case: the instance it came from keeps writing to that storage, so
  this instance may only read it.
* the location was **deleted** while a role still pointed at it.

Up to version 6.34, the first role in this state also cost the roles behind it
theirs: `originals`, `versions` and `backups` were all left without a location,
which is why backups could fail on an instance where only the originals location
was read only. Whatever the actual cause, the message was always the one above.

## Solutions

From version 6.35.0 the message names the cause instead:

```
NewLocationKey: The location configured for "originals" cannot be used: The location "s3-migrated" is read only and cannot be configured as default location.
```

Depending on which of the two cases it names:

* take the read-only flag off the location in `System > Locations`, or point the
  role at a writable location,
* point the role at a location that exists.

A location that is read only cannot be configured as a default location — the
API refuses it with `LocationReadOnlyCannotBeDefault` — so a role's location can
only end up in this state after it was configured: by flagging the location read
only afterwards, by deleting it, or by restoring a database that carries another
instance's locations.
