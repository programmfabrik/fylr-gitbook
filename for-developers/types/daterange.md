# daterange

The `daterange` type stores a lower and upper value of a date range. Either one can be omitted to store an open range.

## API

The API uses an object with from and to for the daterange type:

```json
{
  "daterange": {
    "from": "2001",
    "to": "2010",
    "text": {
      "de-DE": "Die erste Dekade im neuen Millennium",
      "en-US": "The first decade in the new millenium"
    }
  }
}
```

Parsing of the dates works the same as for the [`date, datetime`](date-datetime.md#api) type.  Thus, a `daterange` can store the full set of widths available for the dates in fylr. The shortest date is the year and the longest the full time including a timezone with seconds.

Alongside with the date values, a textual value for the `daterange` can be set. The format of the text property matches the format of the [text\_l10n](text\_l10n-text\_l10n\_oneline.md) type.

## Index

The index works the same as for the [`date, datetime`](date-datetime.md#index) type. Internally **fylr** always works with date ranges to store values.

## Sorting

Sorting works the same as described in for the [`date, datetime`](date-datetime.md#sorting) type.

## Export

The XML Export for the above example looks like this:

```xml
<daterange type="daterange" column-api-id="4">
  <from>2001</from>
  <to>2010</to>
  <text>
    <de-DE>Die erste Dekade im neuen Millennium</de-DE>
    <en-US>The first decade in the new millenium</en-US>
  </text>
</daterange>
```

The **JSON** exports the data like this:

```json
{
  "daterange": {
    "from": "2001",
    "to": "2010",
    "text": {
      "de-DE": "Die erste Dekade im neuen Millenium",
      "en-US": "The first decade in the new millenium"
    }
  }
}
```

**CSV** exports like this:

<table><thead><tr><th>daterange.from</th><th width="136">daterange.to</th><th width="212">daterange.text.de-DE</th><th>daterange.text.en-US</th></tr></thead><tbody><tr><td>2001</td><td>2010</td><td>Die erste Dekade im neuen Millennium</td><td>The first decade in the new millenium</td></tr></tbody></table>

