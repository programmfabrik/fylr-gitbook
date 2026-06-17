---
description: Compute a number from other columns, e.g. a line total.
---

# Calculate a value from other fields

## Use case

You want a column to hold a number derived from other columns — for example a line **total** computed from `amount` and `price`.

## Snippet

```javascript
// Treat missing values as 0 so the result is always a number.
const amount = objNew.amount || 0;
const price = objNew.price || 0;
return amount * price;
```

## Notes

* Give the formula column a numeric type so the result is stored as a number.
* Guarding with `|| 0` avoids `NaN` when one of the inputs is empty.
* Only fields that are part of the object's data (on `objNew`) are available. To use a value from a **linked** object, see [Read a value from a linked object](value-from-linked-object.md).
