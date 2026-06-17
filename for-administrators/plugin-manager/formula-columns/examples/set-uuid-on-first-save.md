---
description: Generate and assign the object's _uuid when the object is created.
---

# Set the object UUID on first save

## Use case

You want every new object to receive a UUID that you control, available from the moment the object is created (for example to build a stable external reference).

The object's `_uuid` is a **system field**, so it lives on the envelope `dataPath[0]`, not on `objNew`. On the **first** save it is still empty: the server generates a `_uuid` only while it writes the object to the database, which happens **after** the `db_pre_save` formula runs. Because it is empty at that point, the formula can set it — and the value it sets is kept (the server only auto-generates a UUID when none is present).

## Snippet

```javascript
// On the first save the object has no _uuid yet, so generate one and assign it
// to the envelope. The "formula-" prefix makes it recognisable that the formula
// set this UUID. On later saves _uuid is already present, so leave it untouched.
if (!dataPath[0]._uuid) {
    dataPath[0]._uuid = "formula-" + require("crypto").randomBytes(16).toString("hex");
}
return dataPath[0]._uuid;
```

The same value is returned, so it is also stored in this column — handy for checking the result.

{% hint style="info" %}
📷 _Screenshot:_ the detail view of a freshly created object, showing the formula column value equal to the object's `_uuid`.
{% endhint %}

## How it works

* `dataPath[0]` is the object **envelope**, where `_uuid` lives. Assigning `dataPath[0]._uuid` changes the UUID the object is created with.
* The `if (!dataPath[0]._uuid)` guard makes this happen **only on the first save**. On every later save the UUID already exists, so it stays stable and is never regenerated.
* The server keeps a `_uuid` that is already set and only generates one when it is empty, so the value from the formula survives the save.

## Common mistakes

These do **not** work:

```javascript
// objNew is the object's DATA fields, not the envelope — _uuid is ignored here.
objNew._uuid = require("crypto").randomUUID();

// objCurr is null on the first save (no previous version), so this throws.
// The error is swallowed by the plugin and nothing is set.
objCurr._uuid = require("crypto").randomUUID();

// This only fills the formula's own column, never the object's _uuid.
return require("crypto").randomUUID();
```

Always assign to **`dataPath[0]._uuid`** (the envelope), not to `objNew`.
