# /api/eas/iiif

Serve the [IIIF Image Information](https://iiif.io/api/image/2.0/#image-information)
(`info.json`) for a file `version`, per the
[IIIF Image API 2.0](https://iiif.io/api/image/2.0/). Reading the image
requires `RIGHT_ASSET_SHOW`. Tiles and image derivatives are served from the
sibling `.../{region}/{size}/{rotation}/{quality}.{format}` paths.

### `GET /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/info.json`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/info.json" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/info.json`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/info.json" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/info.json`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/info.json" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/info.json`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/info.json" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}/info.json`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}/info.json" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}/info.json`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}/info.json" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/{version}/info.json`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{version}/info.json" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/{version}/info.json`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{version}/info.json" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/{region}/{size}/{rotation}/{quality}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/{region}/{size}/{rotation}/{quality}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/{region}/{size}/{rotation}/{quality}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/{region}/{size}/{rotation}/{quality}.{format}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/{version}/{region}/{size}/{rotation}/{quality}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{version}/{region}/{size}/{rotation}/{quality}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/{version}/{region}/{size}/{rotation}/{quality}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{version}/{region}/{size}/{rotation}/{quality}.{format}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}` — Redirect to the IIIF `info.json`.
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}` — Redirect to the IIIF `info.json`.
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}` — Redirect to the IIIF `info.json`.
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}` — Redirect to the IIIF `info.json`.
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}` — Redirect to the IIIF `info.json`.
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}` — Redirect to the IIIF `info.json`.
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/iiif/{fileId}/{hash}/{version}` — Redirect to the IIIF `info.json`.
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{version}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/iiif/{fileId}/{hash}/{version}` — Redirect to the IIIF `info.json`.
{% swagger src="../fylr-openapi.yml" path="/eas/iiif/{fileId}/{hash}/{version}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
