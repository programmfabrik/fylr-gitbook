# /api/db

The `/db` endpoint is **datamodel-driven**. `{objecttype}` is the name of an
object type defined in this instance's datamodel. For every object type,
**fylr** exposes the same set of operations:

  * `POST /db/{objecttype}` — create or update objects.
  * `GET /db/{objecttype}/{mask}/{objectId}` — read a single object.
  * `GET /db/{objecttype}/{mask}/list` — list objects.
  * `DELETE /db/{objecttype}` — delete objects.

Every object is shaped by a *mask* of its object type. The mask selects
which fields are present and whether each one is writable or read-only.

These operations are documented generically here. When the instance has
object types defined, the sections below additionally describe each object
type concretely, with its real masks and field schemas. If only this
generic overview is shown, no object types have been defined yet.

### `POST /db/{objecttype}` — Create or update objects of any object type.
{% swagger src="./fylr-openapi.yml" path="/db/{objecttype}" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /db/{objecttype}` — Delete objects of any object type.
{% swagger src="./fylr-openapi.yml" path="/db/{objecttype}" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /db/{objecttype}/{mask}/{objectId}` — Read a single object of any object type.
{% swagger src="./fylr-openapi.yml" path="/db/{objecttype}/{mask}/{objectId}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /db/{objecttype}/{mask}/list` — List objects of any object type.
{% swagger src="./fylr-openapi.yml" path="/db/{objecttype}/{mask}/list" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
