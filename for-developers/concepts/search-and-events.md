# Search and events

This page covers two facilities: finding records (search), and the record of what happened (events).

## Search and lookup

There are two ways to fetch a record.

**Lookup** is the exact path: when a record's ID (or a known reference or UUID) is already held, the record is returned directly. There is no scoring or matching.

**Search** is used when no ID is held. It runs against fylr's search index — a separate structure kept up to date as records change. Search supports full-text matching, facets, aggregations, sorting, range queries on dates, and combinations of these into a single query. It returns ranked results rather than whole tables.

The two have different costs. Lookup is constant-time. Search asks a search engine, which answers in terms of relevance and aggregations rather than exact rows.

## How a field is searchable

A field opts into the search facilities individually, set per field in the datamodel.

- **Expert-searchable** — available in the expert search, the field-by-field query editor in the interface.
- **Fulltext-searchable** — included in the full-text index, so a phrase typed in the search bar matches it. Used for narrative fields: title, caption, description.
- **Facetable** — available as a facet, a sidebar of distinct values to filter by. Used for categorical fields: type, year, language.
- **Nested-searchable** — for fields whose column is a nested table or reverse-nested view (see [Nested and reverse-nested tables](nested-and-reverse-nested.md)). A search can match the nested rows while returning the parent: "any invoice whose lines contain a charge over 1,000".

A field can opt into several. None are on by default.

## Suggestions and terms

As a phrase is typed into the search bar, fylr offers completions — words and short values drawn from what records actually contain. These suggestions come from a dedicated **term list**, kept separately from the full-text index. Every time a record is saved, fylr extracts the terms from its values and stores them together with how many records carry each term. Suggestions reflect current records only; terms that exist solely in deleted records are not offered.

How a value turns into terms is decided by its field's column type:

- A **one-line or multi-line text** value is split into words; each word becomes a term. Localized text is split per language.
- A **string** value is never split: the whole value is one term. String is the type for codes, identifiers and addresses, where fragments carry no meaning.
- A **number** contributes its formatted value.
- A **file** field contributes the filename.
- Dates, booleans and linked records contribute no terms of their own. A record's comments, however, are split into terms like text.

For **custom data types** — field types provided by plugins — the plugin's manifest maps some of the subfields of the custom value onto standard column types. Exactly those mapped subfields produce terms, each following the rule for the type it is mapped to. The full-text content a plugin generates for its values plays no part here: it feeds the full-text index only, never the term list.

The mapping choice matters. Take a plugin that stores a reference to an external vocabulary, including its URI. Mapped as one-line text, the URI is split into words, and the term list fills with fragments — the protocol, pieces of the address, slices of identifiers — that no one will ever want as a suggestion. Mapped as string, the whole URI stays a single term. When a vocabulary of suggestions grows implausibly large, the mapped types of custom fields are the first place to look.

[Masks](masks.md) play no role in any of this: terms are extracted from all fields of a record, regardless of which masks show the field and regardless of the field's fulltext setting in the datamodel. Those settings govern the full-text index, not the term list.

Because terms are written when a record is saved, a change to a plugin's mapping or to the datamodel changes a record's terms only once that record is saved again.

## Search contexts

A **search context** sets what a search looks across and which permissions apply. The common context is indexed data records, across the objecttypes marked as part of the main search. Other contexts search pools, collections, events, messages, users, groups or permission grants. Each context returns objects of its own kind, so the result shape depends on the context.

## Aggregations

A search can request **aggregations** alongside its results. An aggregation summarises the matching set: how many results fall into each value of a field, the range of values, an average or a sum. Aggregations populate facet sidebars and dashboard counts. The client names each aggregation it requests, and the response returns each named result with the hits.

## Point-in-time

A search runs against the index as it is at request time. For deep paging through a large result, records inserted or reindexed between requests shift the offsets, so pages can skip or repeat results. A **point-in-time** is a frozen snapshot of the index. A client opens one, runs each page against the same snapshot, and closes it when done. Snapshots have a keep-alive and are released explicitly or when it expires.

## The event log

fylr records most server-side changes as **events**: record inserts, updates and deletes, permission changes, collection edits, logins, email sends, plugin actions, transitions. Each event has an increasing ID, a timestamp, a type, the affected object where applicable, and a payload describing the change, including old and new values.

The event log is append-only. Events are not edited or removed. fylr uses it to:

- Update the interface live, so a change in one place refreshes another.
- Run **event transitions** ([Tags and transitions](tags-and-transitions.md)).
- Reconstruct the change history of a record.

## Polling and streaming

A client reads the event log in one of two ways.

- **Polling** — the client gives the ID of the last event it has seen; fylr returns events since then, or holds the connection until one arrives or a timeout passes. The next request uses the highest ID seen. Used by clients that cannot hold a persistent connection.
- **Streaming** — fylr holds the connection open and sends each event as it happens. Used by the interface for live updates.

Both return the same events. Access to either is gated by a system right.

## Recovering history from events

Because an event carries the affected record, the field that changed, and the old and new values, the event log is what fylr uses to show a record's change history: who edited a field, when, and what it held before and after. Reading a record's history filters the event log to events for that record. The log is also the basis for audit, since every change is recorded with its time and user and cannot be edited afterwards.

## User events

A client can write its own **user event** — a custom log entry on a record. It is used to record something that happened outside fylr but should appear in the trail ("export delivered to client"), or for a plugin to record its activity in the same timeline. User events appear in the event log alongside fylr's own, with the same shape, distinguished by their type. Writing one requires a system right; reading them follows the same rules as other events.

## In the API

- A lookup is a [`/db`](../api/endpoints/api-db.md) read: `/db/{objecttype}/{mask}/{objectId}`.
- Search is the [`/search` endpoint](../api/endpoints/api-search.md). Query-language strings are parsed by `/search/parse`, and `/search/point_in_time` opens and closes the snapshots deep paging uses.
- Suggestions come from the [`/suggest` endpoint](../api/endpoints/api-suggest.md).
- The event log is the [`/event` endpoint](../api/endpoints/api-event.md): `/event/poll/{fromEventId}` for polling, `/event/stream` for streaming, and a POST to `/event` writes a user event.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what is indexed and observed.
- [The datamodel](the-datamodel.md) — changes that trigger reindexing.
- [Tags and transitions](tags-and-transitions.md) — transitions that run on event-log entries.
- [Permissions](permissions.md) — the system right that gates writing user events.
