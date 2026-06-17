---
description: Build a single display value from several text fields.
---

# Combine fields into one value

## Use case

You have separate columns — for example `first_name` and `last_name` — and want a single column that always holds the combined value, kept in sync automatically whenever the object is saved.

## Snippet

```javascript
// Join the parts that are filled, separated by a space.
return [objNew.first_name, objNew.last_name]
    .filter(Boolean)
    .join(" ");
```

`filter(Boolean)` drops empty parts, so an object with only a `first_name` does not produce a trailing space.

## Notes

* Your own columns are read from `objNew` (`objNew.first_name`, `objNew.last_name`).
* Give the formula column a text type (e.g. `text_oneline`) so it can hold the result.
* The value is recomputed on every save, so editing it by hand has no effect.
