# Full Text Search

Full-text search provides several options to **precisely define search queries** and narrow down results. The following features can be used **individually or combined**, depending on your use case.

When typing a word into the search field, you get suggestions where you can pick from or simply continue writing (for more details see below):

<table><thead><tr><th width="218.359375">OPTION</th><th>EXPLANATION</th></tr></thead><tbody><tr><td>Fulltext</td><td>Automatically adds wildcards left and right. Example: <code>*turm*</code></td></tr><tr><td>Exact Match</td><td>A case-sensitive search that only finds records where the whole value of a field match. Example: <code>`Fernsehturm`</code></td></tr><tr><td>Word Suggestions</td><td>Shows words from the index and searches without wildcards. Example: <code>'Berlin'</code></td></tr><tr><td>Lists</td><td>Shows entries from lists, vocabularies and thesauri.</td></tr></tbody></table>

### Searching for a Specific Word

#### Case Sensitivity

By default, full-text search is **case-insensitive**. This means that search results are returned regardless of capitalization.

Examples:

* `report`, `Report`, and `REPORT` return the same results.
* Searching for `programmfabrik` also matches `Programmfabrik`.

A case-sensitive search is only possible with the exact search (see below).

#### Word Search

The **word search** allows you to search for **exact word matches** across all searchable fields. The search is **not case-sensitive** and finds records where the specified word appears **anywhere within a text**, as long as it matches the complete word.

You can select a word directly from the **autocomplete suggestions**, or you can manually enter a word by enclosing it in **single quotes**, for example `'automobile'`. Using single quotes ensures that the term is treated as a whole word rather than part of a longer string.

#### Exact Search

The **exact search** allows you to find records where a specific field matches **exactly** the search term you enter. This type of search is **case-sensitive** and does not return partial matches or variations (add wildcards to achieve this).

If the field contains `fylr documentation`:

<table><thead><tr><th width="276.671875">Search Term</th><th>Result</th></tr></thead><tbody><tr><td><code>`FYLR`</code></td><td>❌ No match</td></tr><tr><td><code>`fylr documentation`</code>   </td><td>✅ Match</td></tr><tr><td><code>`documentation`</code></td><td>❌ No match</td></tr><tr><td><code>`Fylr Documentation`</code>  </td><td>❌ No match</td></tr><tr><td><code>`fylr*`</code></td><td>✅ Match</td></tr></tbody></table>

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

<table><thead><tr><th width="128.5234375">KEY</th><th width="187.8515625">SEARCH OPERATOR</th><th>EXPLANATION</th></tr></thead><tbody><tr><td><code>-</code> or <code>!</code></td><td>NOT</td><td>The following search term is searched with “Not”.</td></tr><tr><td><code>+</code></td><td>AND</td><td>The following search term is combined with “And”.</td></tr><tr><td><code>,</code></td><td>OR</td><td>The following search term is combined with “Or”.</td></tr><tr><td><code>(</code></td><td><code>(</code></td><td>Parenthesis for logical groupings.</td></tr><tr><td><code>)</code></td><td><code>)</code></td><td>Parenthesis for logical groupings.</td></tr></tbody></table>

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

### Searching for Dates

{% hint style="info" %}
**From version 6.35.0**, date, time and date range fields are part of the full-text search. As before, a field only takes part in the full-text search if it is included in the full text by the mask. Existing installations need a re-index for dates in existing records to become searchable.
{% endhint %}

A date value can be found by **any of its renderings** — you do not have to know in which format it was entered:

<table><thead><tr><th width="276">Search Term</th><th>Finds</th></tr></thead><tbody><tr><td><code>12.03.2026</code>, <code>3/12/2026</code></td><td>The date, rendered in any of the database languages</td></tr><tr><td><code>2026-03-12</code></td><td>The same date in ISO notation</td></tr><tr><td><code>2026</code></td><td>Every record with a date in 2026 — including dates entered as a year only</td></tr><tr><td><code>1000</code> or <code>1000 BC</code></td><td>A B.C. date, by its displayed year or full rendering</td></tr><tr><td><code>1972</code></td><td>A date range like <code>1970 - 1975</code> — every year the range covers matches</td></tr></tbody></table>

Time fields can additionally be found by their rendered date and time. If a date range carries a **textual representation** (for example *frühes 15. Jahrhundert*), its words are searchable like regular text — searching `Jahrhundert` finds the record.

**Notes:**

* **Word suggestions** only offer a date the way it is **displayed on the record**: the localized renderings, or the year for a year-only date. The ISO form and the years derived from full dates or ranges still match in the full-text search, but are never offered as suggestions. Typing a year still surfaces the renderings that contain it — typing `2026` offers `12.03.2026`.
* B.C. dates are found by their **displayed** year: a date stored as ISO `-0999` is found by searching `1000`, not `-0999` or `0999`.

## Others

To search for a question within a text or word, use:

```
`*\?*`
```

To search for other characters within a text or word, use:

```
`*~*`
```
