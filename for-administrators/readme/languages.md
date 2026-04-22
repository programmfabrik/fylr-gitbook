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

Add the language code according to BCP 47, e.g. "en-US".

#### Display Name

Add how the language should be displayed in the frontend. Supports multiple languages.

#### Date, Time & Number Format

Select the date, time and number format you want to use in this language.

#### Analyzer Settings

#### Remove Diacritics

Removes diacritics from terms for the index (see [ICU folding token filter](https://docs.opensearch.org/latest/analyzers/token-filters/icu-folding/)).

#### Synonyms

Define how different terms are treated as synonyms to improve search results. It supports two types of rules: **equivalent synonyms** (bidirectional) and **explicit mappings** (one-way normalization).

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
