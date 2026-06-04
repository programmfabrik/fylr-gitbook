# /api/v1/search

Run searches over the indexed objects, or over a different domain selected
by the request `type` (`pool`, `collection`, `event`, `message`, `user`,
`group` or `acl`). `POST /search` takes a `SearchRequest` body; `GET
/search` takes the same request as a JSON string in the `BODY` query
parameter so the call can be cached. Both return a `SearchResponse` with the
total `count` and the requested page of `objects`, restricted to what the
requesting user may read.

Differs from easydb 5: the searchable domains are `pool`, `collection`,
`event`, `message`, `user`, `group` and `acl` (plus the default object
search). easydb 5 has no `event` domain, and **fylr** has no
`pool_management` domain (easydb 5 documents `pool_management` to search
pools with `bag_write`).

### `GET /search` — Search for objects (cacheable).
{% swagger src="./fylr-openapi.yml" path="/search" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /search` — Search for objects.
{% swagger src="./fylr-openapi.yml" path="/search" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /search/parse` — Parse a query string into a search request.
{% swagger src="./fylr-openapi.yml" path="/search/parse" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /search/parse` — Parse a query string into a search request.
{% swagger src="./fylr-openapi.yml" path="/search/parse" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /search/point_in_time` — Close point-in-time search contexts.
{% swagger src="./fylr-openapi.yml" path="/search/point_in_time" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
