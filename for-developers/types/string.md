# string

The `string` type's main difference to the text type is how it's indexed. It is recommended to use string types for identification strings which may contain special characters which would be dropped by the analyzer.&#x20;

## API

String looks like this when send and received over the API:

```json
{
    "ref": "A$5667"
}
```

The above example has the value $5667 for column `ref`.

## Index

String values are normalised and lowercased for the index document.&#x20;

```json
{
  "analyzer": {
    "keyword_lowercase": {
      "tokenizer": "keyword",
      "filter": [
        "icu_folding"
      ],
      "char_filter": [
         "icu_normalizer"
      ]
   }
}
```

Strings are normalized using the [`icu_normalizer`](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu-normalization-charfilter.html) and converted to lower case using the  using the [`icu_folding`](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu-folding.html) token filter.

All strings for indexed documents is split into chunks of 8000 UTF-8 characters. When matching full texts in analysed form, text cannot easily be matched if they exceed 8000 characters.

## Sorting

The sorting of string values works like for `text`. In addition to the text sorting a pure alphanumerical version is stored in the index alongside with the numerically sortable variant. With that, sorting can sort _Car 10_, _Car 11_, _Car 12_, _Car 100_. Some special replacement is [always done](text\_l10n-text\_l10n\_oneline.md#sorting).&#x20;

## Export

The **XML** looks like for `text`.

```xml
<ref type="string" column-api-id="346">hall/7$</ref>
```

In this example the column `ref` is exported using value _hall/7$_.

The **CSV** and **JSON** export the string _as is_.
