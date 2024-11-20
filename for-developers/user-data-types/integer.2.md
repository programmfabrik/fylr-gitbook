# integer.2

The `integer.2` type is like a currency type. The value is stored with a 2-digit fraction without loss. Internally fylr stored this as integer. Representations of the value in export and standard info display the fractions. For example the value `1234` will display and be rendered as `12.34`. The limits for this type are the same as for [`number`](number.md).

## API

A number looks like this when send and received over the API:

```json
{
    "integer_2": 567
}
```

The above example has the value `5.67` for column `integer.2`.

## Index&#x20;

The index stores the `integer.2` as [`long`](https://www.elastic.co/guide/en/elasticsearch/reference/current/number.html).

## Sorting

The sorting is independent of the requested search language.

## Export

The XML Export looks like this:

```xml
<integer_2 type="integer.2" column-api-id="4">5.67</integer_2>
```

This shows the example export for column `integer_2` and a value of `5.67`.

**CSV** export uses `5.67` whereas the JSON exports the value as `567`.
