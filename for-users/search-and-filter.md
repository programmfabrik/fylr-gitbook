---
description: Learn everything you need to know about searching and filtering.
---

# Search & Filter

## Introduction

fylr offers several tools to search and filter for records. From defining your sources, to powerful full text searches and expert options, this article explains the possibilities.

## Sources



## Full Text Search

Full-text search provides several options to precisely define search queries and narrow down results. The following features can be used individually or combined, depending on your use case.

When typing a word into the search field, you get suggestions where you can pick from or simply continue writing.

<table><thead><tr><th width="218.359375">OPTION</th><th>EXPLANATION</th></tr></thead><tbody><tr><td>Fulltext</td><td></td></tr><tr><td>Exact Match</td><td></td></tr><tr><td>Word Suggestions</td><td></td></tr><tr><td>Lists</td><td></td></tr></tbody></table>

### Searching for a Specific Word

#### Case Sensitivity

By default, full-text search is **case-insensitive**. This means that search results are returned regardless of capitalization.

Examples:

* `report`, `Report`, and `REPORT` return the same results.
* Searching for `programmfabrik` also matches `Programmfabrik`.

A case-sensitive search is only possible with the exact search. As the exact search matches the whole string, you need to add wildcards like  `` `*programmfabrik*` ``.

Example:

* `` `*programmfabrik*` `` does **not** match `Programmfabrik` or `PROGRAMMFABRIK`.

#### Exact Search



### Phrase Search

Phrase search allows you to search for an **exact sequence of words**. The words must appear in the specified order and directly next to each other.

To perform a phrase search, enclose the phrase in **quotation marks**.

Example:

```
"Berliner Fernsehturm"
```

This search returns only records where the complete phrase appears exactly as entered.

**Notes:**

* Case sensitivity is ignored.
* No additional words may appear between the phrase terms.
* Phrase search is especially useful for quotes, fixed expressions, or known text fragments.

### Boolean Operators

Boolean operators allow you to logically combine multiple search terms.

#### AND

The **AND** operator returns only records that contain **all** specified terms. It is not necessary to use the **AND** operator explicitly. By default, all search terms are automatically combined using an implicit **AND**. Therefore, records will only be returned if they contain all specified terms.

Example:

```
contract AND termination
```

Result: Only records containing both _contract_ and _termination_.

#### OR

The **OR** operator returns records that contain **at least one** of the specified terms.

Example:

```
invoice OR receipt
```

Result: Records containing _invoice_, _receipt_, or both.

#### NOT

The **NOT** operator excludes records that contain a specific term.

Example:

```
report NOT draft
```

Result: Records that contain _report_ but **not** _draft_.

#### Combining and Grouping Operators

Boolean operators can be combined and grouped using parentheses.

Example:

```
(contract OR agreement) AND termination
```

### Wildcard Search

Wildcard search allows you to find terms when parts of the word are unknown or variable.

#### Single-Character Wildcard (?)

The question mark `?` represents **exactly one arbitrary character**.

Example:

```
Ma?er
```

Matches, for example:

* Mayer
* Maier
* Mauer

**Notes:**

* Each `?` replaces exactly one character.
* Multiple `?` characters can be used within a single term.

#### Multi-Character Wildcard (\*)

The asterisk `*` represents **zero, one, or multiple characters**.

Examples:

```
Auto*
```

Matches:

* Auto
* Automatic
* Automobile

```
*report
```

Matches:

* annualreport
* auditreport

**Notes:**

* The `*` wildcard can be used at the beginning, middle, or end of a word.
* Searches with a leading `*` may impact performance.

## Expert Search

## Filter
