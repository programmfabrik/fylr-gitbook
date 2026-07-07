---
description: >-
  How to build a POST /api/v1/search request — the top-level parameters, the
  search array element types, bool contexts and boost, and aggregations (facets).
---

# Building a Search Request

Search is a `POST` of a JSON body to [`/api/v1/search`](api/endpoints/api-search.md). The body describes _what_ to match (the `search` array), _how_ to order and page it, and optionally which _facets_ to compute. This page is the practical companion to the [Search and events](concepts/search-and-events.md) concept.

```json
{
  "objecttypes": ["person"],
  "format": "standard",
  "offset": 0,
  "limit": 25,
  "generate_rights": true,
  "search": [
    { "type": "match", "mode": "fulltext", "string": "lovelace", "bool": "must" },
    { "type": "range", "field": "person.born", "from": "1800", "to": "1900" }
  ],
  "sort": [{ "field": "_score", "order": "desc" }],
  "aggregations": {
    "types": { "type": "term", "field": "_objecttype", "limit": 10 }
  }
}
```

The response carries `count`, `offset`, `limit` and `objects` (each a [record](record-json.md) with a `_score`), plus `aggregations` and, when used, `point_in_time`.

## Top-level parameters

| Parameter | Type | Purpose |
| --- | --- | --- |
| `search` | array | The query — a list of search elements (see below). |
| `type` | string | The search **domain**: empty = indexed objects; otherwise `pool`, `collection`, `event`, `message`, `user`, `group` or `acl`. |
| `objecttypes` | string[] | Restrict an object search to these object types (empty = all). |
| `format` | string | Render format of each hit: `standard`, `long`, `short`. |
| `offset` / `limit` | int | Paging window. |
| `sort` | array | Sort criteria; sort by the field `_score` for relevance order. |
| `search_after` | array | Deep-pagination cursor — the `_sort` values of the last hit of the previous page. |
| `point_in_time` | object | `{id, keep_alive}` — a stable snapshot for consistent deep paging. |
| `aggregations` | object | Facets / aggregations, keyed by a name you choose (see below). |
| `generate_rights` | bool | Emit each hit's effective rights (`_generated_rights`). |
| `include_fields` / `exclude_fields` | string[] | Project the returned fields. |
| `fields` | array | Collect specific field values per hit. |
| `merge_linked_objects` | string | How deeply to embed linked objects: `none`, `in_main_search`, `not_in_main_search`, `not_in_main_search_unless_reverse`, `all`. |
| `merge_max_depth` | int | Embed depth for merged links. |
| `include_deleted` | bool | Include trashed objects. |
| `languages` | string[] | Languages to load. |
| `best_mask_filter` | bool | Reduce each hit to the best mask the user may see. |

## The `search` array

Each element has a `type` and, optionally, a `bool` context and a `boost`. The element types:

| `type` | Matches | Key fields |
| --- | --- | --- |
| `match` / `text` | full-text against one or more fields | `fields`, `string`, `mode` (`fulltext` / `wildcard` / `token`), `phrase` |
| `in` | a field against a set of values, an object type, or a sub-search | `fields`, `in` (values), `objecttype`, `subsearch`, `include_path` |
| `range` | a range on one field | `field`, `from`, `to`, `from_equals`, `to_equals` |
| `changelog_range` | by change-history entries | `field`, `from`, `to`, `operation`, `comment`, `user` |
| `complex` | a group of nested `search` elements as one boolean sub-query | `search`, `bool` |
| `nested` | like `complex`, scoped to a nested `path` | `path`, `search` |
| `geo_bounding_box` | a geo field inside a box (needs the geo capability) | `field`, `geo_bounding_box` |
| `geo_shape` | a geo field inside a polygon (needs the geo capability) | `field`, `geo_shape` |

Id lookups use `type: "in"` with `fields: ["_system_object_id"]` (or `["_uuid"]`); there is no separate `ids` element. Full-text is `type: "match"` / `"text"`.

## `bool` contexts

Every element combines into the overall query through its `bool`:

* **`must`** (the default) — the element must match.
* **`should`** — the element _may_ match; at least one `should` across the query must match, and matching ones raise `_score`.
* **`must_not`** — the element must not match (excludes; does not affect `_score`).

Nest `complex` elements to build `AND` / `OR` trees — a `complex` with `bool: should` holding several sub-elements is an `OR` group.

## `boost`

Every element accepts a `boost` (number, default `1`, from fylr **6.34.0**). A value other than `1` scales how much a matching element contributes to a hit's `_score`; negative values are rejected. Combine `bool: should` elements with different boosts and sort by `_score` to rank preferred matches first. Boost has no effect on `must_not` clauses.

## Aggregations (facets)

`aggregations` is a map keyed by names you choose; each value requests one aggregation:

```json
"aggregations": {
  "by_type":  { "type": "term", "field": "_objecttype", "limit": 10, "sort": "count" },
  "by_pool":  { "type": "linked_object", "field": "_pool", "objecttype": "pool" },
  "by_year":  { "type": "date_range", "field": "person.born",
                "ranges": [{ "to": "1900" }, { "from": "1900" }] }
}
```

Aggregation `type`s include `term`, `term_stats`, `date_range`, `linked_object`, and the geo aggregations `geo_bounds`, `geotile_grid`, `geohash_grid`. Common fields: `field`, `limit` (default 10), `offset`, `sort` (`count` or `term`), `order`, `include` (anchored regex), `ranges` (for `date_range`), `objecttype` (for `linked_object`).

The response returns each aggregation under the same key: a `term` aggregation yields `{ field, terms: [{ count, term }] }`; a `linked_object` aggregation yields `{ count, linked_objects: [{ count, _id, _path }] }`.

## Other entry points

* `GET /api/v1/search` takes the same body as a URL-encoded JSON string.
* `POST /api/v1/search/parse` turns a natural-language / [query-language](../for-users/search-and-filter/query-language.md) string into a `search` request you can inspect or run.

## See also

* [Search and events](concepts/search-and-events.md) — how search differs from lookup; the term list and suggestions.
* [Anatomy of a record](record-json.md) — the shape of each hit.
* [`/api/v1/search`](api/endpoints/api-search.md) — the endpoint reference.
