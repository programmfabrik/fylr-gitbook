---
description: finding records by meaning, by words, and by both at once
---

# Semantic and hybrid search

An ordinary fulltext search finds the records that contain the words you typed. A **semantic** search finds the records that mean what you asked for, whether or not they use your words: "ein kleiner Vogel" finds *House Sparrow on Wooden Surface*.

Both have a weakness the other does not, so fylr can run them together.

## How a record becomes searchable by meaning

1. A record is indexed. Its **subject** — its own standard texts and the title, categories and keywords of its files — is what its vector stands for.
2. If semantic search is on, fylr checks whether the stored vector still matches that text. If not, an **embedding job** is queued.
3. The job asks the embedding model for the vector and stores it. The record is re-indexed with the vector in it.

A record whose text has not changed is never embedded twice, and a re-index of an unchanged instance costs nothing.

{% hint style="info" %}
**Why the subject and not the whole text.** Every AI caption in an archive is built the same way — "a close-up of X on a Y background" — so a vector of the caption encodes *"this is an image caption"* more strongly than it encodes X. Measured on a 100-record archive, that squeezed everything into a 0.03-wide band of similarity: chewing gum scored 0.619 against "a chair, a bench, furniture to sit on" and the bench itself 0.647, and no floor could separate them. Nouns separate; prose does not. A record with no subject to speak of falls back to its whole fulltext, because a weak vector beats none — and the word-based side keeps the prose either way, since that is what BM25 is good at.
{% endhint %}

## The picture, too

What a record says about itself and what its picture shows are different evidence, and the picture is the half nobody wrote down. A second model — a **joint image/text** one, of the CLIP family — embeds the picture the record's standard asset shows, into its own index field.

Configure it as the **Picture model** in the [AI configuration](configuration.md). Since one model puts words and pictures in the same space, the vectors can be searched from either end:

```json
{ "type": "similar", "system_object_id": 4711 }
{ "type": "similar", "file_id": 815 }
{ "type": "similar", "query": "a bench in the fog" }
```

* by **record** — "more like this": the records whose picture looks like this one's. The reference record is never among its own answers.
* by **file** — the same, with one picture of a record as the reference. That is what the detail sends: the picture on display, not the record, which may show several. Pass the record alongside to keep it out of the answer.
* by **phrase** — the pictures a description fits, whether or not anyone wrote it down. Asked for "a black and white photograph" on an archive whose captions never say so, the picture side answers with greyscale images; the word side answers with whatever caption happens to contain "white".

A file with no picture — an audio file — simply has no vector; the job ends without one rather than failing.

{% hint style="warning" %}
No vendor fylr knows serves an image embedding model on its own endpoint: OpenAI's embedding models are text-only and Anthropic has none. Point a provider's **Base URL** at a service that does — Jina's `jina-clip-v2`, or a CLIP server of your own. They speak the same `/v1/embeddings` shape, with `{"image": "<data URI>"}` in place of a string.
{% endhint %}

## Searching

The search element:

```json
{ "type": "semantic", "query": "a small bird on a fence", "terms": "bird wildlife" }
```

* `query` is the descriptive phrase. It is embedded and matched against the records' vectors.
* `terms` are single words. They are matched by the ordinary fulltext search.
* `cut` overrides how hard the fused list is cut, 0 keeping everything the neighbour search returned. It is what answers "find me five pictures" with five.
* With both, the search is **hybrid**: the two result lists are fused by reciprocal rank — a record near the top of both leads, a record only one of them knows still comes through. That is what lets a category word in the keywords count even when no sentence contains it.

The `_score` of a hybrid search is the fused rank, 1.0 meaning first in both lists. Sort by it:

```json
"sort": [ { "field": "_score", "order": "DESC" } ]
```

Everything else about the request is unchanged: the objecttype restriction, the pool filters, the user's read rights and the best-mask filter all apply, and they apply *inside* the neighbour search — otherwise a k-NN query would return its k nearest records overall and the filters would only thin them out afterwards.

## In the frontend

The [AI assistant](assistant.md) searches this way, and its result set can be handed to the search app with **Show in search**: the search bar carries a token with exactly those hits, and they become an ordinary search — facets, sorting, filters, saved searches.

A record's 3-dot menu offers **Find similar pictures**, which does the same for the picture the asset browser is showing.

Both are rankings, so the search shows them ordered by relevance rather than by the default sort — until you pick a sort of your own, which is then yours to keep.

## What to expect

Semantic search is good at "something like this" and bad at exactness. It has no notion of "no match", so a floor or the hybrid fusion decides what is close enough. It is only as good as what the records say about themselves, which is why [tagging](tagging.md) matters: a stock of photographs with no captions has little to embed — beyond their pictures, which is what the picture model is for.

Two honest limits worth knowing. A text vector of an AI caption is largely redundant with a word search over that same caption: the tagging is doing most of the work, and the vector earns its keep on the cases the words miss — a caption saying "doves" answering a search for birds. And the words are literal in the other direction: a picture whose caption happens to mention birds is a correct hit for "bird" even when the birds are specks on a lake.
