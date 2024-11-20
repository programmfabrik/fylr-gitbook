# date, datetime

The types `date` and `datetime` are used to load and store dates and datetimes defined in [ISO8601](https://en.wikipedia.org/wiki/ISO\_8601). Note that **fylr** doesn't support a type to store a duration or just a time or date without year.

**fylr** does support storing just the calendar year or year and month. These dates are stored as date range internally, so e.g. `2000` would be stored as range from `2000-01-01 00:00:00` to `2000-31-12 25:59:59`.&#x20;

The supported range for dates is between years `-292,277,022,399` and `292,277,022,399`.  This is roughly UNIX seconds stored in a 64-bit integer.

## API

The API treats the types date and datetime the same. So it is possible to store a datetime in a date value. The type is merely a hint for frontends to render the value accordingly.

The longest possible form of the value contains the timezone as shown in this example:

```json
{
  "date": {
    "value": "2010-12-10T12:45:00+01:00:00"
  }
}
```

This stores the date `2010-12-20` with time `12:45:00` in time zone `+01:00:00`. Time zones must be given using the offset. fylr keeps the time zone. If a value without a time zone is given, fylr assumes UTC as time zone.

The shortest possible date value looks like this:

```json
{
  "date": {
    "value": "2010"
  }
}
```

This has the date `2010` spanning a range from `2010-01-01 00:00:00` to `2010-31-12 25:59:59`.&#x20;

The API can parse a wide variety of formats. This includes parsing fractional seconds. Fractional seconds are discarded.

The output are always as follows:

```go
YEAR              = "2006"
YEAR_MONTH        = "2006-01"
DATE              = "2006-01-02"
DATE_TIME         = "2006-01-02T15:04"
DATE_TIME_SEC     = "2006-01-02T15:04:05"
DATE_TIME_SEC_TZ  = "2006-01-02T15:04:05Z07:00"
DATE_TIME_SEC_TZS = "2006-01-02T15:04:05Z07:00:00"
```

The left side reflects the recognized width of the value.

{% hint style="info" %}
The parser does not support sending a timezone for shortened date strings. For shorter date strings, the stored time zone is always UTC.
{% endhint %}

## Index

**fylr** calculates all dates to index based on the UNIX seconds computed for the UTC time zone of the given date. The values are stored as [`long`](https://www.elastic.co/guide/en/elasticsearch/reference/current/number.html) in the indexer. Various values are calculated to reflect the range every date creates. Alongside with the `from` and `to` values, a `from_to` value is stored which allows for aggregations using the middle value of a date.

## Sorting

Sorting can be done by using the stored subfield `from`, `to` or `from_to` (default). Using the API sort values can be adjusted to match a specific date width (`day`, `week`, `month`, `year`). With that, values spanning two years in UTC (this New Year's Eve in Sydney and Los Angeles), can be adjusted to be sorted by the same value using width `year`.&#x20;

Sort values can also be adjusted to a specific timezone using the API.

## Export

The XML contains the date rendered according to the stored width of the date.

```xml
<date type="date" column-api-id="2">2010-12-10T12:45:00+01:00:00</date>
```

The example shows the output for a column date with date value `2010-12-10T12:45:00+01:00:00`.

The same value is used to the export in **CSV** and **JSON**.
