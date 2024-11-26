# boolean

The type `boolean` can be used to store two states, `false` and `true`. The default is `false`.

## API

A boolean looks like this when send and received over the API:

```json
{
    "bool": true
}
```

The above example has the value _true_ for column `bool`.

## Index

The indexed document contains an entry with `false` or `true`. It is mapped as type [`boolean`](https://www.elastic.co/guide/en/elasticsearch/reference/current/boolean.html).

## Sorting

The ascending order of the sort is `false`, `true`. The sorting is independent of the requested search language.

## Export

The **XML representation** looks like this:

```xml
<bool type="boolean" column-api-id="2">true</bool>
```

This is for a column `bool` and the value `true`. `false` is also always rendered.

The **CSV representation** is `false` or `true`, resp.

The **JSON representation** is a JSON boolean.

{% hint style="info" %}
The storage inside the **fylr** server distinguishes between `null` and `false`, but this is not visible over the API.
{% endhint %}
