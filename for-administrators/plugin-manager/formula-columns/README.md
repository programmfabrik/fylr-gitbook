---
description: >-
  Compute the value of a column with a small JavaScript snippet that runs on the
  server every time an object is saved.
---

# Formula Columns

The **Formula Columns** plugin (`formula-columns`) lets you fill a column with a value that is **computed** from a small **JavaScript** snippet instead of being entered by hand. The snippet runs on the server during every save, so the calculated value is stored with the object like any other field value.

Typical uses are combining several fields into one display value, calculating a number from other fields, copying a value from a linked object, or generating an identifier. See [Examples](examples/) for ready-to-use snippets.

## Enabling the plugin

`formula-columns` ships with every release. Make sure it is enabled in the [Plugin Manager](../README.md). Once enabled, a new option group **"Formula Columns"** appears in the column settings of the data model.

## Configuring a formula

Open **Data model → Object type → Columns**, select the column that should hold the computed value, and open its **Option** tab. Enter the snippet under **Formula Columns**.

{% hint style="info" %}
📷 _Screenshot:_ the **"Formula Columns"** option group in **Data model → Object type → Columns → Option**, showing the script editor and the **Debug** toggle.
{% endhint %}

A column with a formula is still a normal column, so give it a type that fits the value you return (for example a text type for strings, a number type for numbers).

{% hint style="warning" %}
The value of a formula column is **overwritten on every save** with the result of the snippet. Do not let users edit it by hand — whatever they type is replaced the next time the object is saved.
{% endhint %}

## How the snippet runs

The plugin is a **`db_pre_save`** callback: it runs on `/api/db` **before** the object is written to the database, using the `_all_fields` mask so all object data is available. Your snippet is the **body** of an `async` function, so you can use `await`:

```javascript
async function (objNew, objCurr, dataPath, dataPathCurr) {
    // ... your snippet ...
}
```

The **return value** of the snippet becomes the value of the formula column. The snippet is run with `eval` inside a `try…catch` (see [Debugging](#debugging-and-logging) below).

### Available parameters

<table><thead><tr><th width="180">PARAMETER</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><code>objNew</code></td><td>The new data of the object being saved — i.e. the <strong>fields of the object type</strong> (for a top-level object, its record; for a nested object, the nested record). This is where your own columns live, e.g. <code>objNew.title</code>.</td></tr><tr><td><code>objCurr</code></td><td>The data as currently stored in the database (the previous version). It is <code>null</code> on the <strong>first</strong> save, because there is no previous version yet.</td></tr><tr><td><code>dataPath</code></td><td>The path to the current data, starting at the top level. <code>dataPath[0]</code> is the <strong>object envelope</strong> — this is where the <strong>system fields</strong> such as <code>_uuid</code>, <code>_id</code> and <code>_system_object_id</code> live.</td></tr><tr><td><code>dataPathCurr</code></td><td>The same as <code>dataPath</code>, but for the current (stored) object data.</td></tr></tbody></table>

{% hint style="warning" %}
**Data fields vs. system fields.** Your own columns are on `objNew` (e.g. `objNew.title`). The **system fields** (`_uuid`, `_id`, `_system_object_id`, …) are **not** on `objNew` — they live on the **envelope**, `dataPath[0]`. Reading or writing `objNew._uuid` does nothing; use `dataPath[0]._uuid`. See [Set the object UUID on first save](examples/set-uuid-on-first-save.md).
{% endhint %}

{% hint style="info" %}
A known limitation: when the formula runs for a **nested record**, it does not know which record index it is currently in.
{% endhint %}

## Utility functions and async

The formula runs inside an `async` function, so you can use `await` and standard browser/Node APIs such as `fetch`.

### `apiSearchBySIDs(sids, mode)`

An `async` helper to look up objects by their system object id (`_system_object_id`). It accepts a single id or an array of ids and supports the formats `long`, `short`, `long_inheritance`, `full` and `standard`. It returns an array of the found objects (empty if none are found). See [Read a value from a linked object](examples/value-from-linked-object.md).

## Debugging and logging

Two tools help while you develop a formula:

* **Debug option** — enable **Debug** on the column to store an event of type **`FORMULA_COLUMNS_DEBUG`** for each calculation, containing the input data and the result.
* **Errors** — if the snippet throws, the error is caught and stored as an event of type **`FORMULA_COLUMNS_ERROR`**. The column is not changed in that case.

Inside the snippet you also have:

* `log` — push messages that are stored in the system event, e.g. `log.push({ info: info });`
* `info` — instance information such as the API `url`, useful for API calls.

{% hint style="info" %}
📷 _Screenshot:_ a `FORMULA_COLUMNS_DEBUG` event in **Events**, showing the logged input and result.
{% endhint %}

## Examples

See [Examples](examples/) for complete, copy-ready snippets:

* [Set the object UUID on first save](examples/set-uuid-on-first-save.md)
* [Combine fields into one value](examples/combine-fields.md)
* [Calculate a value from other fields](examples/calculate-from-fields.md)
* [Read a value from a linked object](examples/value-from-linked-object.md)
