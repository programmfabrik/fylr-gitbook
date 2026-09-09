# /api/v1/db

The `/db` endpoint is **datamodel-driven**. `{objecttype}` is the name of an object type defined in this instance's datamodel. For every object type, **fylr** exposes the same set of operations:

* `POST /db/{objecttype}` — create or update objects.
* `GET /db/{objecttype}/{mask}/{objectId}` — read a single object.
* `GET /db/{objecttype}/{mask}/list` — list objects.
* `DELETE /db/{objecttype}` — delete objects.

Every object is shaped by a _mask_ of its object type. The mask selects which fields are present and whether each one is writable or read-only.

These operations are documented generically here. When the instance has object types defined, the sections below additionally describe each object type concretely, with its real masks and field schemas. If only this generic overview is shown, no object types have been defined yet.

### `POST /db/{objecttype}` — Create or update objects of any object type.

#### Base fields only group edits

From **6.35.0** the query parameter `base_fields_only=1` changes tags or pools for records that are editable through different masks in one request. Send the group-edit `_id` array without `_mask`; ordinary fields, parents, owners and record ACLs stay unchanged. Write permission, the tag-edit policy and the pool permissions still apply. Repeated tag and pool edits share unchanged value sets between record versions, so a large group edit writes far less to the database; bidirectional links are kept, and an unchanged file needs no replacement permission.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/db/{objecttype}" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /db/{objecttype}` — Delete objects of any object type.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/db/{objecttype}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /db/{objecttype}/{mask}/{objectId}` — Read a single object of any object type.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/db/{objecttype}/{mask}/{objectId}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /db/{objecttype}/{mask}/list` — List objects of any object type.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/db/{objecttype}/{mask}/list" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
