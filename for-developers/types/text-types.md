# Text types

Text types are used to store text. We support `text`, `text_oneline`, `string`, `l10n_text` and `l10n_text_oneline`.

## text, text\_online

`text` and `text_oneline` store characters in one language. In the server, these types are treated the same, text\_oneline is only a hint for frontends on how to display the data. So it is possible (over the API) to use newlines in a text\_online column.

Text are stored as received, so a leading or trailing space is preserved. Frontends are requested to trim texts before sending them to the API.

Text must be encoded in [UTF-8](https://en.wikipedia.org/wiki/UTF-8) and stores in all [normalization forms](https://unicode.org/reports/tr15/#Norm\_Forms). There is not limit on the length of storable text.

### Index

Normalization is performed as part of the indexer documentation creation where all text is run through a `icu_normalizer`.&#x20;

In the indexer, text is stored using a custom analyzer `icu_text` which works as follows:

```json
{
  "analysis": {
   "icu_text": {
     "type": "custom",
     "tokenizer": "custom_icu_tokenizer",
     "filter": [
       "icu_folding"
     ],
     "char_filter": [
       "icu_normalizer"
     ]
  },
  "tokenizer": {
    "custom_icu_tokenizer": {
      "type": "pattern",
      "pattern": "([[^\\p{L}\\p{Digit}\\uD800-\\uDFFF\\u2F00-\\u2FDF]&&[^&%§\\$€]])"
    }
  }
}
```

Text is normalized using the [`icu_normalizer`](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu-normalization-charfilter.html) and tokenized into tokens using the above pattern.&#x20;

What gets included in tokens:

* All alphabetic letters from any language.
* All numeric digits.
* Characters in the Unicode surrogate pair range and Kangxi Radicals.
* Symbols: `&`, `%`, `§`, `$`, and `€`.

What causes token separation:

* Punctuation marks (except the specified symbols).
* Whitespace characters.
* Other symbols and control characters not specified.

Tokens are then turned into terms using the [`icu_folding`](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu-folding.html) token filter. The filter removes all punctuation and turns all characters into lower case. So the token _Bär_ is stored as _bar_.

Using the API, searches for text can be performed either on the analysed value (matching the terms), or on the unanalysed value, which is stored alongside with all terms. The unanalysed value stores the data _as is._ There is no normalisation taking place.

All text for indexed documents is split into chunks of 8000 UTF-8 characters. When matching full texts in analysed form, text cannot easily be matched if they exceed 8000 characters.

### Sorting

Sort strings are compiled using the Go library [collate](https://pkg.go.dev/golang.org/x/text/collate). It uses the first configured database language as assumption in what language the text is in. Numbers are recognised so that _Car 100_ sorts after _Car 11_. Text is normalised by the collate library. Internally we use the hex representation of that string to work around anomalies in Elasticsearch. Some special replacement is [always done](text-types.md#sorting-2).&#x20;

### Export

Text is exported as is, keeping spaces & normalisation.

The **XML export** looks like this for a column names `title` and a value _Title_ for type `text_oneline`. The `column-api-id` in this example _29_.&#x20;

```xml
<title type="text_oneline" column-api-id="29">Title</title>
```

For type text type is `text`.

Output in **CSV** is as is, same for **JSON**.

## string

The `string` type's main difference to the text type is how it's indexed. It is recommended to use string types for identification strings which may contain special characters which would be dropped by the analyzer.&#x20;

### Index

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

### Sorting

The sorting of string values works like for `text`. In addition to the text sorting a pure alphanumerical version is stored in the index alongside with the numerically sortable variant. With that, sorting can sort _Car 10_, _Car 11_, _Car 12_, _Car 100_. Some special replacement is [always done](text-types.md#sorting-2).&#x20;

### Export

The **XML** looks like for `text`.

```xml
<ref type="string" column-api-id="346">hall/7$</ref>
```

In this example the column `ref` is exported using value _hall/7$_.

The **CSV** and **JSON** export the string _as is_.

## text\_l10n, text\_l10n\_oneline

The types `text_l10n` and `text_l10n_oneline` are designed to store localized values. The format is a JSON object consisting of the language as key and the text as value.

```json
{
  "title_loca": {
    "de-DE": "German",
    "en-US": "English"
  }
}
```

The API is not checking the passed language. So, load and save of an unconfigured database language is supported.

### Index

Indexing is done the same way `text` format is indexed. Only enabled database languages are mapped into the index, other languages are ignored. After changing the settings for the database languages a reindex is required.

### Sorting

Sorting is performed using a collate string produced by the Go library [collate](https://pkg.go.dev/golang.org/x/text/collate). The language is parsed as [BCP 47](https://www.rfc-editor.org/info/bcp47) string and passed to the library. Some special replacement is done:

```go
'ʾ': '@', //     02BE    Hamza (vorne offen) @ sorts this before A
'ʿ': '@', //     02BF    Ayn (hinten offen) @ sorts this before A
```

### Export

**XML exported data** looks like this:

```xml
<title_loca type="text_l10n" column-api-id="81">
  <de-DE>German</de-DE>
  <en-US>English</en-US>
</title_loca>
```

The example shows the XML snippet for a column `title_loca` with the type `text_l10n`.

In **CSV the values** are exported like this:

| title\_loca.de-DE | title\_loca.en-US |
| ----------------- | ----------------- |
| German            | English           |

For each language exported a suffix `.<code>` is added to the column name.
