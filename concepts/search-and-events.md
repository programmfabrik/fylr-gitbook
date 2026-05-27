# Search and events

This page is about two of fylr's most-used facilities and how they sit alongside each other. **Search** is how you find records; **events** are how fylr tells you what happened. Both run against the same data, but they answer different questions and have different shapes.

## Search vs lookup-by-id

There are two ways to fetch a record out of fylr, and they aren't interchangeable.

- **Lookup-by-id** is the cheap, exact path: you already have a record's id (or a known shortname / UUID / reference), and you want the record itself. The lookup endpoint returns it from the live row directly. No indexing, no scoring, no concept of "matches" — just the record.
- **Search** is what you use when you don't have an id. It runs against fylr's search index — a separate, optimised data structure that the database keeps up to date via [reindex events](the-datamodel.md). Search supports full-text matching, facets, aggregations, sorting on derived fields, range queries on dates, geo queries, and combinations of those into compound boolean queries. It returns ranked hits, not whole tables.

The two paths exist because they have different costs. Lookup is constant-time and predictable. Search is fast for its job, but it asks a search engine to answer your question, and a search engine answers in terms of relevance and aggregations rather than exact rows. Mixing them — "give me record 42, but also use search ranking" — doesn't quite type-check; pick the right tool per call.

## How fields choose to be searchable

A field on an objecttype is not automatically all kinds of searchable at once. The datamodel lets the modeller pick, per field, which of the search facilities a field opts into.

- **Expert-searchable.** The field is exposed to fylr's expert-search syntax (the "name contains X and year > Y" boolean editor in the UI). Use this for fields a power user expects to filter by name.
- **Fulltext-searchable.** The field's text is included in the instance's full-text index, so a typed phrase will match it via the simple search bar. Use this for narrative fields where users type words rather than build queries: title, caption, description, transcript.
- **Facetable.** The field is exposed as a search facet — a sidebar list of distinct values the user can click to filter by. Use this for low-cardinality categorical fields: type, publication, year, language.
- **Nested-searchable.** Only meaningful on fields whose underlying column is a nested table or a reverse-nested view (see [Nested and reverse-nested tables](nested-and-reverse-nested.md)). Lets a search ask about the nested rows as if they were their own records, while still matching the parent: "find any Invoice whose lines contain a charge over 1,000".

A single field can opt into several at once. None of them are on by default — each is a deliberate per-field choice that affects index size and the search experience.

## Search contexts

A **search context** is the lens fylr searches through. It selects which kinds of object are eligible to match — sometimes records of a particular objecttype, sometimes the catalogue of pools, sometimes collections, sometimes events themselves — and which permissions apply.

The most common context is "indexed user-content records": the search engine looks across every objecttype that the datamodel marks as part of the main search. Other contexts let you search specifically against pools, collections, events, messages, users, groups or ACL grants — each with its own object shape in the response. Picking the right context matters because the result shapes differ; a hit in the pool context is a pool, a hit in the events context is an event.

## Aggregations

A search request can ask for **aggregations** alongside the hits. An aggregation is a summary over the matching set: how many hits fall into each value bucket of a field ("12 photos by Anna, 7 by Bertram, 3 by Catherine"), the range of values seen ("dates from 1928 to 1953"), an average or sum. Aggregations are how facet sidebars are populated and how dashboards count things.

The client picks which aggregations to compute and names them; the response carries each named aggregation's results alongside the hits.

## Point-in-time

A search request usually runs against the index as it is _right now_. For deep paging — fetching the third page of a 50 000-hit result — that becomes a problem: by the time the third page is requested, new records may have been inserted and old records may have been re-indexed, shifting the offsets so that page three skips or duplicates results.

A **point-in-time** is a frozen snapshot of the index. The client opens one, runs every page of its paginated query against the same snapshot, and closes it when done. While the snapshot is open, the search results are stable across requests. Snapshots have a configurable keep-alive and are released either explicitly or automatically when the keep-alive expires.

## The event log

fylr records almost every server-side change as an **event**: object inserts, object updates, object deletes, ACL changes, collection edits, login attempts, email sends, plugin actions, transitions running. Each event carries a monotonically-increasing id, a UTC timestamp, the kind of event, the affected object (where applicable), and a structured payload describing what changed (old value, new value).

The event log is **append-only**. Events are never edited or removed; the log is the durable record of what happened, and it's what fylr uses to:

- Drive the front-end's live updates (a change made in one tab refreshes another).
- Run **event transitions** ([Tags and transitions](tags-and-transitions.md)) — workflow steps that fire on a matching event.
- Reconstruct change history per record: every old/new pair for every field, with timestamps, in order, by whom.

## Polling and streaming

Clients consume the event log in one of two shapes.

- **Polling** is a long-poll loop: the client gives fylr the last event id it has seen, and fylr either returns new events that have happened since (if any are available) or holds the connection open until one arrives or a server-side timeout elapses. The next call uses the highest id seen as the new cursor. Polling is what clients use when they can't keep a persistent connection open — most HTTP toolchains support it out of the box.
- **Streaming** is a server-sent event stream: fylr keeps the connection open and pushes each new event over it as it happens, one per message. Streaming is what the front-end uses for live updates. It is more efficient for high-volume streams but requires a longer-lived connection.

Both paths return the same events; the choice is operational. The system right `system.event` gates access to either.

## Recovering history from events

Because events carry the affected object's id, the field that changed, and both old and new values, the event log is what fylr uses to **show the change history of a record**: who edited the caption, when, what it said before, what it says now. Reading a record's history is, mechanically, filtering the event log to the events that mention this record.

This is also why the event log is the source of truth for audit: every change is in there, with a timestamp and the user who made it, and it can't be edited after the fact.

## User events

Beyond the events fylr writes on its own, a client can write its own **user event** — a custom log entry on a record. Use this when something happened outside fylr that the audit trail should still reflect ("export delivered to client", "permission verbally cleared by Director on date X"), or when a plugin wants to record its own activity in a way that fits into the same timeline.

User events show up in the event log alongside system-written events, with the same shape and the same id sequence; they're distinguished by their kind. Writing one requires a system right (`system.event`); reading them follows the same rules as reading any other event.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what gets indexed and observed.
- [The datamodel](the-datamodel.md) — datamodel changes that trigger reindexing.
- [Tags and transitions](tags-and-transitions.md) — workflow steps that hang off event-log entries.
- [Permissions](permissions.md) — the system right that gates writing user events.
