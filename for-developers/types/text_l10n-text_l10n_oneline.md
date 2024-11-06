# text\_l10n, text\_l10n\_oneline

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

## Index

Indexing is done the same way `text` format is indexed. Only enabled database languages are mapped into the index, other languages are ignored. After changing the settings for the database languages a reindex is required.

## Sorting

Sorting is performed using a collate string produced by the Go library [collate](https://pkg.go.dev/golang.org/x/text/collate). The language is parsed as [BCP 47](https://www.rfc-editor.org/info/bcp47) string and passed to the library. Some special replacement is done:

```go
'ʾ': '@', //     02BE    Hamza (vorne offen) @ sorts this before A
'ʿ': '@', //     02BF    Ayn (hinten offen) @ sorts this before A
```

## Export

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
