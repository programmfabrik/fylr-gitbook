# /api/v1/xmlmapping

Manage XML import/export **mappings** — transformations between fylr objects and external XML formats (METS/MODS, LIDO, custom profiles, ...). A mapping pairs an XML profile with field-level bindings; profiles describe the structure of the external XML.

### `GET /xmlmapping/list` — List all profiles with the mappings built from each.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/xmlmapping/list" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /xmlmapping/tags` — List the metadata tags the exif-list recipe knows about.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/xmlmapping/tags" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /xmlmapping/profile/{profile}` — Retrieve a single XML profile.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/xmlmapping/profile/{profile}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /xmlmapping/mapping` — Create a new mapping.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/xmlmapping/mapping" method="put" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /xmlmapping/mapping/{mapping}` — Retrieve an XML mapping.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/xmlmapping/mapping/{mapping}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /xmlmapping/mapping/{mapping}` — Update an existing XML mapping.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/xmlmapping/mapping/{mapping}" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /xmlmapping/mapping/{mapping}` — Delete an XML mapping.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/xmlmapping/mapping/{mapping}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
