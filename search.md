---
description: How to use the search in fylr
---

# Search

### Sources

<figure><img src=".gitbook/assets/Screenshot 2025-06-17 at 17.09.05.png" alt=""><figcaption><p>A fylr search with an open sources menu, the filtering options for object types and pools are not expanded.</p></figcaption></figure>

Select the object types and pools you want to search in the current session.&#x20;

**Tipp:** use `CMD+click` to quickly de/select all object types or pools

{% hint style="info" %}
To see object types in the select list, the search option needs to be enabled for the object type in the datamodel.&#x20;
{% endhint %}

### Search Syntax

fylr uses a common layout of search operators to allow users to apply different search strategies to their queries.&#x20;

{% hint style="info" %}
The following examples will test a simple text field with the content **"My cat is the best".**
{% endhint %}

#### Wildcard operators

* `cat` (without any syntax)
* `"cat"`
* `*cat*`

They all deliver the same result, because those search enclose the query with the \* wildcards under the hood. We can delimit our search by a \* wildcard:

* `*cat*best*` finds our sentence
* `cat*best` uses the same search, also finds our sentence

#### Exact Search

* &#x20;`'cat'` searches for exact, full matches, delimited by spaces.
* doesn't not find 'catalogue'
* does find the example sentence

Searching with Backticks matches against the entire text fields content and will deliver only results for full matches.

* only `` `my cat is the best` `` would result in our sentence

{% hint style="success" %}
All these strategies can be applied by just typing into the search bar and clicking on a suggested syntax, this will update the search result with the typed term using the selected technique.
{% endhint %}

### Logical Operators

| Key        | Search Operator | Explanation                                       |
| ---------- | --------------- | ------------------------------------------------- |
| `-` or `!` | NOT             | The following search term is searched with “Not”. |
| `+`        | AND             | The following search term is combined with “And”. |
| `,`        | OR              | The following search term is combined with “Or”.  |
| `(`        | `(`             | Parenthesis for logical groupings.                |
| `)`        | `)`             | Parenthesis for logical groupings.                |
