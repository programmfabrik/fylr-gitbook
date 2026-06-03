# /api/oaipmh

[OAI-PMH](https://www.openarchives.org/OAI/openarchivesprotocol.html)
endpoint. Implements the Open Archives Initiative Protocol for
Metadata Harvesting (version 2.0) so external harvesters can pull
metadata from fylr. The protocol uses a single URL with a `verb`
query parameter and returns XML.

Must be enabled in the base config (`fylr.oai_pmh.enabled = true`),
otherwise every request returns HTTP 400 with `code: OAIpmhNotEnabled`.
Protocol-level errors are returned inside the XML response body as an
`<error code="…">` element AND carry the matching HTTP status:
`badArgument` / `badVerb` / `cannotDisseminateFormat` /
`badResumptionToken` → 400, `idDoesNotExist` → 404, internal failures
→ 500. Only a successful harvest is `200 OK`.

The endpoint requires no rights and accepts anonymous requests: when no
user can be derived from the session, the built-in `system:oai_pmh`
user is used. There is no read-only-mode guard. A `ListRecords` or
`GetRecord` harvest logs an `OBJECT_DOWNLOAD` event per record (written
in a background transaction), but the request itself runs in a read
transaction — nothing else is persisted.

### `GET /oai` — OAI-PMH protocol entry point.
{% swagger src="./fylr-openapi.yml" path="/oai" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `HEAD /oai` — HEAD on the OAI-PMH endpoint.
{% swagger src="./fylr-openapi.yml" path="/oai" method="head" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
