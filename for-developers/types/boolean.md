# boolean

The type `boolean` can be used to store two states, `false` and `true`. The default is `false`.

## Index

The indexed document contains an entry with `false` or `true`. It is mapped as type [`boolean`](https://www.elastic.co/guide/en/elasticsearch/reference/current/boolean.html).&#x20;

## Sorting

The ascending order of the sort is `false`, `true`. The sorting is independent of the requested search language.

## Export

&#x20;The **XML representation** looks like this:

```xml
<bool type="boolean" column-api-id="2">true</bool>
```

This is for a column `bool` and the value `true`. `false` is also always rendered.

The **CSV representation** is `false` or `true`, resp.

The **JSON representation** is a JSON boolean.

_The storage inside the fylr server distinguished between `null` and `false`, but this is not visible over the API._
