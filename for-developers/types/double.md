# double

The type `double` supports store and load for a floating point number with 64 bits (Go type `float64`). The range for that number is approximately `-1.7976931348623157e+308` to `1.7976931348623157e+308`. Go adheres to [IEEE 754](https://en.wikipedia.org/wiki/IEEE\_754) for storing the values.

## API

Double looks like this when send and received over the API:

```json
{
    "double": 1234.5678
}
```

Numbers are guaranteed  to keep their value, but the JSON parser may change `1e4` into `10000` upon load.

## Index

The type `double` is stored as type [`double`](https://www.elastic.co/guide/en/elasticsearch/reference/current/number.html) in the indexer.

## Sorting

The sorting is independent of the requested search language.

## Export

The export of the value is not localized.

The XML Export looks like this:

```xml
<double type="double" column-api-id="2">1234.56789</double>
```

This shows the example export for column `double` and a value of `1234.56789`.

**CSV** and **JSON** export the number as is.
