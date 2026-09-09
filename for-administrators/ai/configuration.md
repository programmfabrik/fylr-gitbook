---
description: the instance-wide AI settings, and the request log
---

# AI Configuration

The **AI configuration** app (black menu → **AI configuration**) has three tabs: the [providers](providers.md), the settings below, and the log. It needs the `system.root` right.

These settings are not in the base configuration because they need live feedback from the providers — which embedding models are on offer, which model can be the assistant — and that list changes as providers are enabled and disabled.

## Semantic search

An embedding is a vector: a record's text turned into numbers, so that two records that mean similar things sit close together. fylr stores one vector per record and puts it into the index, which is what makes [semantic search](semantic-search.md) possible.

Embedding and searching are one setting, because neither is any use alone: a search by meaning needs the vectors, and vectors nobody searches for are tokens spent for nothing.

<table data-header-hidden><thead><tr><th width="230"></th><th></th></tr></thead><tbody>
<tr><td><strong>Find records by meaning</strong></td><td>The switch. On, every indexed record is embedded and the <code>semantic</code> search element may be used; off, the API refuses the element and the assistant says so.</td></tr>
<tr><td><strong>Embedding model</strong></td><td>The model, as <code>&lt;provider&gt;/&lt;model&gt;</code>. Only embedding models of enabled providers are offered; the dimension follows from the model.</td></tr>
<tr><td><strong>Data languages</strong></td><td>Which languages of a record's text are embedded — at least one. Embedding six translations of the same sentence costs six times as much and helps nothing, so pick the languages your users actually search in.</td></tr>
<tr><td><strong>Picture model</strong></td><td>A joint image/text model that embeds what a record's picture shows, in the same space as its words. It is what makes <a href="semantic-search.md#the-picture-too">"more like this"</a> possible, and it finds what no description mentions. None means only the text is embedded. Only models that can embed pictures are offered here — and only text models are offered above.</td></tr>
<tr><td><strong>Neighbours per search (k)</strong></td><td>How many nearest records a vector search returns. A k-NN search always returns k records, however unlike they are — see the note below.</td></tr>
<tr><td><strong>Minimum similarity</strong></td><td>A floor between 0 and 1. With a floor, the search returns every record above it instead of the k nearest, which is what turns "the 20 closest" into "everything that actually matches". 0 keeps all k.</td></tr>
<tr><td><strong>Search assistant</strong></td><td>A completion model that turns a chat request into a retrieval query before searching. Empty means the chat searches the words as typed. Several models may be named, comma separated — see <a href="#a-model-may-be-a-chain">A model may be a chain</a>.</td></tr>
</tbody></table>

{% hint style="warning" %}
Changing the model, the picture model, their dimensions or the languages invalidates every stored vector and the index mapping. Saving therefore asks to **rebuild the index**; until that has run, semantic search works with what is still there.
{% endhint %}

{% hint style="info" %}
A pure vector search has no notion of "no match": ask for k neighbours and you get k, the last of them arbitrarily unrelated. Either give it a floor, or use the hybrid search, whose fusion with the word-based side is its own cut.
{% endhint %}

## A model may be a chain

Wherever fylr asks for a completion model, several may be named instead of one, comma separated and in the order they should be tried:

```
claude/claude-opus-4-8, openai/gpt-4.1
```

fylr calls the first. If that call fails for a reason that is the *provider's* — no credit, an expired key, a rate limit, a gateway error, an endpoint that does not answer — it moves on to the next and the request still gets an answer. An error that is the request's own, a picture the model refuses for instance, is not retried elsewhere: another model would refuse it too.

Which model actually answered is in the log, so a chain that has quietly been running on its fallback for a week is visible rather than a surprise on the invoice.

The search assistant above takes a chain, and so does [tagging](tagging.md) — the embedding models do not, neither the text one nor the picture one: vectors of two different models cannot be compared, so a fallback would silently poison the index.

## The log

The **Log** tab lists what fylr sent and what it cost: the time, the user, the type of request (`tagging`, `field_prompt`, `search`, `embed`), the model, the subject, the tokens in and out, and the status. Every AI call in fylr writes such a row, including the ones a background job made — see [Queue, log and costs](operations.md).
