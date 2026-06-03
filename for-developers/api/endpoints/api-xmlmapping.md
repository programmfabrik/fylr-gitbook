# /api/xmlmapping

Manage XML import/export **mappings** — transformations between
fylr objects and external XML formats (METS/MODS, LIDO, custom
profiles, ...). A mapping pairs an XML profile with field-level
bindings; profiles describe the structure of the external XML.

### `GET /xmlmapping/list` — List all profiles with the mappings built from each.
{% swagger src="./fylr-openapi.yml" path="/xmlmapping/list" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /xmlmapping/tags` — List the metadata tags the exif-list recipe knows about.
{% swagger src="./fylr-openapi.yml" path="/xmlmapping/tags" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /xmlmapping/profile/{profile}` — Retrieve a single XML profile.
{% swagger src="./fylr-openapi.yml" path="/xmlmapping/profile/{profile}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `PUT /xmlmapping/mapping` — Create a new mapping.
{% swagger src="./fylr-openapi.yml" path="/xmlmapping/mapping" method="put" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /xmlmapping/mapping/{mapping}` — Retrieve an XML mapping.
{% swagger src="./fylr-openapi.yml" path="/xmlmapping/mapping/{mapping}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /xmlmapping/mapping/{mapping}` — Update an existing XML mapping.
{% swagger src="./fylr-openapi.yml" path="/xmlmapping/mapping/{mapping}" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /xmlmapping/mapping/{mapping}` — Delete an XML mapping.
{% swagger src="./fylr-openapi.yml" path="/xmlmapping/mapping/{mapping}" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
