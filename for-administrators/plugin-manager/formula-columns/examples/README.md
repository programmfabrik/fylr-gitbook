---
description: Ready-to-use snippets for the Formula Columns plugin.
---

# Examples

These examples are complete snippets you can paste into the **Formula Columns** option of a column (see [Formula Columns](../README.md) for how to configure one). Each page explains the use case, the snippet, and what to watch out for.

* [Set the object UUID on first save](set-uuid-on-first-save.md) — generate and assign the object's `_uuid` when the object is created.
* [Combine fields into one value](combine-fields.md) — build a single display value from several text fields.
* [Calculate a value from other fields](calculate-from-fields.md) — compute a number (e.g. a total) from other columns.
* [Read a value from a linked object](value-from-linked-object.md) — copy a field from a linked object using `apiSearchBySIDs`.

{% hint style="info" %}
Remember: the snippet is the body of `async function (objNew, objCurr, dataPath, dataPathCurr)`, its **return value** becomes the column value, your own fields are on `objNew`, and the **system fields** (`_uuid`, …) are on the envelope `dataPath[0]`.
{% endhint %}
