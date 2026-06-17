---
description: Copy a field from a linked object using apiSearchBySIDs.
---

# Read a value from a linked object

## Use case

Your object links to another object, and you want a column that holds a field of that **linked** object (for example its `category`), kept up to date on each save.

The linked object's full data is not part of the object being saved, so you look it up by its system object id with the `apiSearchBySIDs` helper.

## Snippet

```javascript
console.info("Fetching the linked object by sid");

if (!objNew.linked) {
    return "No linked object provided.";
}

// The link field carries the linked object's _system_object_id.
const sid = objNew.linked._system_object_id;
const found = await apiSearchBySIDs(sid);

if (found && found.length > 0) {
    // The fields of the linked object are under its own object type key.
    const objecttype = found[0]._objecttype;
    return found[0][objecttype].category;
}

return "Linked object not found.";
```

## Notes

* `apiSearchBySIDs(sids, mode)` accepts a single id or an array, and the formats `long`, `short`, `long_inheritance`, `full`, `standard`. It returns an array of objects (empty if none match).
* The snippet runs in an `async` function, so `await` works directly. You can also use `fetch` to call an external API the same way.
* `console.info(...)` output goes to the server log; use `log.push(...)` to attach data to the debug event instead.
