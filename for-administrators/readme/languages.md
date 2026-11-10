---
description: >-
  Define in which languages the frontend should be available and in which
  languages you want to store your data.
---

# Languages

## Languages

### Application

Enable/Disable all languages for the frontend. Users will be able to choose from the activated languages. Use the drag handle to order the languages.

### Data Languages

Add/Remove all languages for multi-language fields (they must be defined in the data model). Each multi-language field will be available in the selected languages. Users will be able to choose their own languages form the activated languages.

#### Language Code (BCP 47)

The code of a data language that has been saved is **read-only** (from 6.35.0): renaming it would leave every value stored under the old code invisible. Add the new language and remove the old one instead. Removing a language keeps its values in the database; they reappear once the language is added again.

Add the language code according to BCP 47, e.g. "en-US".

#### Display Name

Add how the language should be displayed in the frontend. Supports multiple languages.

#### Date, Time & Number Format

Select the date, time and number format you want to use in this language.

#### Analyzer Settings

Configure how text in this language is processed for searching. These settings affect how records are indexed and matched.

#### Remove Diacritics

Normalizes text using ICU folding (see [ICU folding token filter](https://docs.opensearch.org/latest/analyzers/token-filters/icu-folding/)) by removing accents and standardizing characters (e.g., case, ligatures, width), enabling more consistent and language-independent matching. This improves search results, especially when users omit accents or use different keyboard layouts.

Examples:\
`Café` → `cafe`

`RÉSUMÉ` → `resume`

&#x20;`Æsop` → `aesop`

#### Synonyms

Define how different terms are treated as synonyms to improve search results. It supports two types of rules: **equivalent synonyms** (bidirectional) and **explicit mappings** (one-way normalization).

Synonyms apply where text is indexed with the language's analyzer: in multi-language fields, and in the full-text search also in a record's standard info (title, subtitle, …, as set in the mask's Standard column), including the standard info of linked records. Single-line text, multi-line text and string fields have no language and get no synonyms, neither in the full-text search nor in a search in the field. To use synonyms for such content, make the field multi-language.

While equivalent synonyms treat all terms as interchangeable (searching for "notebook" finds "laptop" and the other way around), explicit mappings normalize different terms into one standard term (searching for "notebook" finds "laptop", but "laptop" doesn't find "notebook").

Use the word search to still be able to find specific terms (for example, search for `'notebook'` to find "notebook" instead of "laptop").

**Example:**

```
# Comments start with #
# Blank lines are ignored

# 1. Equivalent synonyms (comma-separated)
# All terms on a line are treated as interchangeable
laptop, notebook, portable computer, macbook
tv, television, telly
car, automobile, vehicle, auto
smartphone, mobile phone, cellphone, iphone, android phone

# 2. Explicit mapping (one-way or replacement)
ipod, i-pod, i pod => ipod
new york, ny, nyc => new york
uk, u.k., united kingdom => united kingdom
grey, gray => grey
laptop, notebook, macbook => laptop
```



#### Synonym Text File

Alternatively, upload the synonym configuration as a text file.

A changed synonym list or file applies to existing records only after a full [re-index](../../for-system-administrators/inspect/system.md#re-index).

## Indexer

### Default Analyzer Settings

These settings apply to every field without a language: single-line and multi-line text, string, and the base types such as users, groups and pools.

#### Remove Diacritics

The same folding as **Remove Diacritics** of a data language, for the fields without a language. With it, a search for `Savinon` finds `Saviñon` and `Cadiz` finds `Cádiz`. It is off by default.

For text that is part of a record's standard info, the full-text search also matches through the data languages, so there **Remove Diacritics** of a data language already ignores diacritics. For all other text in these fields, in the full-text search and in a search in the field, this switch is needed.

A change applies to existing records only after a full [re-index](../../for-system-administrators/inspect/system.md#re-index).
