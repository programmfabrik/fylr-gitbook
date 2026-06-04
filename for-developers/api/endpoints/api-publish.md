# /api/v1/publish

Record **publishings** of fylr objects in external systems.
**fylr has no publishing layer of its own** — the publication
itself (for example a DataCite DOI, an external gallery page or a
share link) is produced and hosted elsewhere. A publish entry is
fylr's record of such a publication: it ties an object's
`system_object_id` to the **collector** it was published through
(a target configured in the base config, e.g. `datacite`) and to
the external `publish_uri` where the publication lives, plus a
deep-link back into fylr (`easydb_uri`). These endpoints create,
list and delete those records — they do not generate or serve the
published artifacts.

### `GET /publish` — List publish records.
{% swagger src="./fylr-openapi.yml" path="/publish" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /publish` — Record one or more publishings.
{% swagger src="./fylr-openapi.yml" path="/publish" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /publish/{systemObjectId}` — Retrieve a single publish record by its id.
{% swagger src="./fylr-openapi.yml" path="/publish/{systemObjectId}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /publish/{publishId}` — Delete a publish record.
{% swagger src="./fylr-openapi.yml" path="/publish/{publishId}" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
