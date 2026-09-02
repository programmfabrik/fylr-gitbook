---
description: finding records by meaning, by words, and by both at once
---

# Semantic and hybrid search

An ordinary fulltext search finds the records that contain the words you typed. A **semantic** search finds the records that mean what you asked for, whether or not they use your words: "ein kleiner Vogel" finds *House Sparrow on Wooden Surface*.

Both have a weakness the other does not, so fylr can run them together.

## How a record becomes searchable by meaning

1. A record is indexed. Its **fulltext** — the record's own texts, its linked records' standard texts, and the `ai` metadata of its files — is what it stands for.
2. If embeddings are on, fylr checks whether the stored vector still matches that text. If not, an **embedding job** is queued.
3. The job asks the embedding model for the vector and stores it. The record is re-indexed with the vector in it.

A record whose text has not changed is never embedded twice, and a re-index of an unchanged instance costs nothing.

## Searching

The search element:

```json
{ "type": "semantic", "query": "a small bird on a fence", "terms": "bird wildlife" }
```

* `query` is the descriptive phrase. It is embedded and matched against the records' vectors.
* `terms` are single words. They are matched by the ordinary fulltext search.
* With both, the search is **hybrid**: the two result lists are fused by reciprocal rank — a record near the top of both leads, a record only one of them knows still comes through. That is what lets a category word in the keywords count even when no sentence contains it.

The `_score` of a hybrid search is the fused rank, 1.0 meaning first in both lists. Sort by it:

```json
"sort": [ { "field": "_score", "order": "DESC" } ]
```

Everything else about the request is unchanged: the objecttype restriction, the pool filters, the user's read rights and the best-mask filter all apply, and they apply *inside* the neighbour search — otherwise a k-NN query would return its k nearest records overall and the filters would only thin them out afterwards.

## In the frontend

The [AI assistant](assistant.md) searches this way, and its result set can be handed to the search app with **Show in search**: the search bar then carries an `ai:` token with the same query, and the hits become an ordinary search — facets, sorting, filters, saved searches.

## What to expect

Semantic search is good at "something like this" and bad at exactness. It has no notion of "no match", so a floor or the hybrid fusion decides what is close enough. It is only as good as what the records say about themselves, which is why [tagging](tagging.md) matters: a stock of photographs with no captions has nothing to embed.
