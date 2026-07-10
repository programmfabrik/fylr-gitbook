---
description: >-
  Register the collectors that fylr records may be published to. A collector is
  an external target that hosts the publication; fylr only records that a
  publication exists and links back to the source record.
---

# Publications

**Publishing** exposes a record — or a collection's records — outside the instance, at a public URL produced by a **collector**. fylr has no publishing layer of its own: the publication itself (for example a DataCite DOI, a repository entry or a public gallery page) is produced and hosted elsewhere. fylr only records that the publication exists, through which collector, and links back to the source record.

For the underlying concept see [Publishing](../../for-developers/concepts/collections-and-publishing.md#publishing); publications are created and removed through the [`/api/v1/publish`](../../for-developers/api/endpoints/api-publish.md) endpoint.

## Collector

Here you register the collectors that may be used. Each row in the table defines one collector. A publication created through [`/api/v1/publish`](../../for-developers/api/endpoints/api-publish.md) must name a collector defined here — otherwise it is rejected with `PublishUnknownCollector`.

### Display Name

The name of the collector as shown in the frontend. Can be entered in multiple languages.

### Internal Name

The technical name of the collector. This is the value a publication references (the `collector` sent to [`/api/v1/publish`](../../for-developers/api/endpoints/api-publish.md)), so it must be unique and should not be changed once publications refer to it.

### URL

The base URL of the collector — the external system where the publications live.

### Type

A short type or category for the collector (for example the kind of identifier it issues). It is used together with the **Display Format** below to label a publication.

### Prefix

A URL prefix, which must end with a slash (`/`). It is combined with the identifier of a published record to build the public link that resolves to the publication.

### Logo

An image (PNG or JPG) shown for this collector in the frontend, for example next to a published record.

### Display Format

How a publication of this collector is labelled in the frontend:

| OPTION | EXAMPLE |
| ------ | ------- |
| Name | the collector's display name only |
| Name: Type | display name and type |
| Name: Type – &lt;DOI/URN&gt; | display name, type and the identifier (default) |
| Type | the type only |
