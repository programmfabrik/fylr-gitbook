---
description: >-
  Build precise, field-aware searches by typing a structured query into the
  search bar with the ql: prefix.
---

# Query Language

The **query language** lets you express a search as a compact, structured
expression instead of clicking through the [Expert Search](expert-search.md)
form. It is the most precise way to search: you name the exact field, choose how
it should be compared, and combine any number of conditions with logical
operators.

{% hint style="info" %}
This is an **advanced feature**. For everyday searching — wildcards, phrases,
`AND`/`OR`/`NOT`, and quoting — see [Full Text Search](full-text-search.md).
The query language adds **per-field** comparisons, ranges, relative dates,
linked-record searches and geo searches on top of that.
{% endhint %}

## Using the Query Language

Type the prefix **`ql:`** into the search bar, directly followed by your query:

```
ql:book.title =@ "annual report" && book.year >= 2020
```

As you type, the query is **validated live**. An invalid query is marked in red
and shows the reason; a valid query turns into a **`QL` search element** that you
can move, copy or combine with other search elements just like any other search
criterion. **Double-click** the element to reopen it in a multi-line editor that
re-checks the query as you edit and only applies it once it is valid again.

Several search elements in the bar are combined with **AND**. To express **OR**,
put it _inside_ a single query with `||`.

{% hint style="warning" %}
The prefix is **`ql:`** by default, but it is configurable per installation. If
`ql:` does nothing in your system, ask your administrator which prefix is
active.
{% endhint %}

## Anatomy of a Query

A single condition has three parts:

```
   field      operator    value
──────────    ────────   ────────
book.title       =@       "report"
```

Conditions are combined with the logical operators `&&` (and), `||` (or) and
`!` (not), and grouped with parentheses `( … )`:

```
(asset.class == "image" || asset.class == "video") && asset.year >= 2020
```

## Referencing Fields

A field is referenced by its **object type** and **field name**, separated by a
dot:

```
objecttype.field
```

| Reference                       | Meaning                                                  |
| ------------------------------- | ------------------------------------------------------- |
| `book.title`                    | The `title` field of the `book` object type             |
| `book.author.name`              | The `name` sub-field reached through `author`           |
| `book.link.url`                 | The `url` part of a custom data type field `link`       |
| `book._id`                      | The object ID                                           |
| `_last_modified`                | When the record was last changed                        |
| `_changelog.date_created`       | When the record was created                             |

{% hint style="info" %}
Field and object-type names are **lowercase** and must be written exactly as
they appear in the data model. An unknown field name makes the whole query
invalid. The easiest way to look up the exact name — and which operators a field
supports — is the **data-model inspector** (`/inspect/datamodel/…`): open an
object type and read the _Api Name_ column of its **Search Fields** table. You
can also build a criterion once in the [Expert Search](expert-search.md) and see
which field it produces.
{% endhint %}

### Linked Records: Alias Fields

For every **linked** field, fylr automatically provides an **alias** under the
plain field name, so you can search the linked record without naming its internal
fields. What the alias searches depends on the value you give it:

| Query                     | Finds records where the linked record…                       |
| ------------------------- | ------------------------------------------------------------ |
| `book.author =@ "Smith"`  | has _Smith_ in its **standard info** (title, subtitle, …)    |
| `book.author == 1234`     | is the one with that **ID**                                  |
| `book.author == null`     | is **absent** — nothing is linked in that field              |
| `book.author != null`     | is **present** — something is linked in that field            |

Under the hood the alias expands to the linked record's real search fields, which
you can also use directly if you need to be specific:

* a **text** value searches the record's **standard info** text —
  `book.author._standard.1.text` (the main title),
  `book.author._standard.2.text` (a subtitle) and
  `book.author._standard.3.text` (internal information to be used in exports);
* a **number** or `null` searches the linked record's ID,
  `book.author._system_object_id`.

These aliases — and the fields they expand to — are listed as **Search Alias
Fields** in the data-model inspector. To require several conditions on the same
linked record, use a [sub-search](#sub-search).

### Custom Data Type Fields

A custom data type — for example a _link_ field — exposes its own **sub-fields**.
Reference them with an additional dot, `objecttype.field.subfield`:

```
book.link.url == "http://www.programmfabrik.de"
```

The available sub-fields and their exact names appear in the **Search Fields**
table of the data-model inspector.

## Operators

| Operator | Name             | Matches when the field…                                   | Example                       |
| -------- | ---------------- | --------------------------------------------------------- | ----------------------------- |
| `==`     | equals           | is exactly the value (see _null_ below)                   | `book._id == 583`             |
| `!=`     | not equals       | is anything other than the value                          | `book.status != "archived"`   |
| `=@`     | matches          | contains the word(s); **case-insensitive**, wildcards ok  | `book.title =@ "report"`       |
| `!@`     | does not match   | does not contain the word(s)                              | `book.title !@ "draft"`        |
| `=*`     | contains         | contains the value anywhere; **case-sensitive**           | `book.code =* "AB"`           |
| `!*`     | does not contain | does not contain the value                                | `book.code !* "XX"`           |
| `=^`     | starts with      | starts with the value; **case-sensitive**                 | `asset.filename =^ "IMG_"`    |
| `!^`     | does not start   | does not start with the value                             | `asset.filename !^ "tmp_"`    |
| `>=`     | from / at least  | is greater than or equal to the value                     | `book.year >= 2000`           |
| `<=`     | up to / at most  | is less than or equal to the value                        | `book.year <= 2010`           |
| `>`      | greater than     | is strictly greater than the value                        | `book.price > 100`            |
| `<`      | less than        | is strictly less than the value                           | `book.price < 100`            |

The `=@` operator supports the same `*` and `?` wildcards as the
[Full Text Search](full-text-search.md):

```
asset.filename =@ "*C02-21*.jpg"
asset.filename =@ "C0?-21-1168.jpg"
```

## Values

The value on the right side of an operator is one of the following types.

### Text

Text values are always wrapped in **double quotes**:

```
book.title == "Annual Report"
```

To use a literal double quote inside the text, escape it with a backslash:

```
book.note =@ "say \"hello\""
```

### Numbers

Numbers are written without quotes and may be negative or decimal:

```
book.year >= 2000
book.price < 19.99
book.temperature > -5
```

### Empty / not empty (`null`)

Use the keyword **`null`** (without quotes) to find records where a field has
**no value**, or — negated — where it **has** a value. `null` works only with
`==` and `!=`:

```
book.photographer == null      # no photographer linked
book.keywords != null          # has at least one keyword
```

### Dates

Dates can be given as plain ISO values…

```
book.date <= "2012"
book.date >= "2024-01-01"
```

…or as **relative placeholders**, which are resolved at search time. This is
ideal for [Saved Searches](../quick-access/saved-searches-and-lists.md) that
should always be relative to "now".

| Placeholder      | Anchor                                       |
| ---------------- | -------------------------------------------- |
| `$now`           | The current date **and time**                |
| `$today`         | The start of the current day                 |
| `$startOfMinute` | The start of the current minute              |
| `$startOfHour`   | The start of the current hour                |
| `$startOfDay`    | The start of the current day                 |
| `$startOfWeek`   | Monday of the current week                   |
| `$startOfMonth`  | The first day of the current month           |
| `$startOfYear`   | January 1st of the current year              |
| `$month`         | The current month                            |
| `$year`          | The current year                             |

Add an offset to a placeholder with `+` or `-`, a number, and an optional unit.
Several offsets can be chained:

```
_last_modified >= "$now-7d"          # last 7 days
book.date < "$startOfMonth"          # before this month
book.date >= "$startOfMonth+1M-1d"   # up to the last day of this month
```

| Unit | Meaning |
| ---- | ------- |
| `s`  | seconds |
| `m`  | minutes |
| `h`  | hours   |
| `d`  | days    |
| `w`  | weeks   |
| `M`  | months  |
| `y`  | years   |

{% hint style="info" %}
If you omit the unit, **days** are assumed: `$now-2` means two days ago.
{% endhint %}

### Geo coordinates

Geo fields can be searched with a bounding box, given either as two
`[latitude, longitude]` corners or as one or two
[geohash](https://en.wikipedia.org/wiki/Geohash) prefixes. Geo values work only
with `==` and `!=`:

```
asset.location == [71.18507, -25.2966][34.7982, 41.7102]
asset.location == ["gkw", "syj"]
asset.location == ["gkw"]
```

## Combining Conditions

| Operator | Meaning | Example                                          |
| -------- | ------- | ------------------------------------------------ |
| `&&`     | AND     | `asset.class == "image" && asset.year >= 2020`   |
| `\|\|`   | OR      | `asset.class == "image" \|\| asset.class == "video"` |
| `!`      | NOT     | `!(book.status == "archived")`                   |
| `( … )`  | group   | `(a \|\| b) && c`                                |

Use parentheses to make the precedence explicit whenever you mix `&&` and `||`:

```
(asset.class == "image" || asset.class == "video") && asset.year >= 2020
```

## Sub-Search

A **sub-search** matches records by the _content of the records they link to_.
Write the linking field, then `== ?( … )` with a full query inside the
parentheses:

```
book.author == ?( person.country == "FR" )
```

fylr runs the inner query as an independent search over the linked object type,
collects the IDs of the records it finds, and returns the records that link to
any of them. Here: find every `person` in France, then return the `book` records
linked to one of them.

A sub-search always follows a **link** to another record. That link may sit
directly on the object type, or **inside a nested field** — in the nested case
the field path is simply longer (look it up in the data-model inspector's
**Search Fields** table). The mechanism is the same either way.

### Why a sub-search and not two conditions?

Every condition inside the parentheses is evaluated against the **same** linked
record, so a sub-search is the only way to require that several conditions hold
for _one and the same_ linked entry:

```
book.author == ?( person.role == "editor" && person.country == "FR" )
```

This finds books whose author is a person who is **both** an editor **and**
based in France. Splitting the conditions outside the sub-search would instead
allow them to be satisfied by two _different_ linked records (one editor, and a
separate French one).

The inner query is complete in its own right, so it can use every operator,
boolean logic, and even further sub-searches.

## Full-Text Search

A bare text value with **no field and no operator** runs a full-text search
across all searchable fields — the same as typing the words directly into the
search bar:

```
"berlin"
```

## Examples

| Goal                                              | Query                                                   |
| ------------------------------------------------- | ------------------------------------------------------- |
| Title contains "report"                           | `book.title =@ "report"`                                |
| Exact object ID                                   | `book._id == 583`                                       |
| File name starts with `IMG_`                      | `asset.filename =^ "IMG_"`                              |
| Keyword field is empty                            | `book.keywords == null`                                 |
| Has at least one keyword                          | `book.keywords != null`                                 |
| Years 2000 to 2010                                | `book.year >= 2000 && book.year <= 2010`                |
| Changed in the last week                          | `_last_modified >= "$now-7d"`                           |
| Created this year                                 | `_changelog.date_created >= "$startOfYear"`             |
| Image or video, from 2020 on                      | `(asset.class == "image" \|\| asset.class == "video") && asset.year >= 2020` |
| Linked author by standard info (alias field)      | `book.author =@ "Smith"`                                |
| No author linked                                  | `book.author == null`                                   |
| Custom data type sub-field (link URL)             | `book.link.url == "http://www.programmfabrik.de"`       |
| Linked author from France (sub-search)            | `book.author == ?( person.country == "FR" )`            |

## Errors

If a query cannot be parsed — a missing quote, an unknown field, an invalid date
placeholder — the search bar marks the `QL` element as invalid and the search is
not run. Hover the element to read the exact reason and correct it.
