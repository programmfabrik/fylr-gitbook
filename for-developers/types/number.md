# number

The type `number` stores integers between `-(2**53)+1` and (`2**53)-1`. This follows the recommendation in [RFC 8259](https://datatracker.ietf.org/doc/html/rfc8259). The range is between -`9,007,199,254,740,991` and `9,007,199,254,740,991` (incl.).

## Index&#x20;

The index stores the `number` as [`long`](https://www.elastic.co/guide/en/elasticsearch/reference/current/number.html).

## Sorting

The sorting is independent of the requested search language.

## Export

The XML Export looks like this:

```xml
<number type="number" column-api-id="10">1234</number>
```

This shows the example export for column `number` and a value of `1234`.

**CSV** and **JSON** export the number as is.
