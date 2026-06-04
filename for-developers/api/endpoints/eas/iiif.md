# /api/v1/eas/iiif

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

### URL templates

These GET, HEAD endpoints embed parameters inside a path segment (e.g. `{quality}.{format}`), which the interactive API panel can't render — they are listed here as URL templates instead. All live under the `/api/v1` base path.

```
/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}
/eas/iiif/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/{region}/{size}/{rotation}/{quality}.{format}
/eas/iiif/{fileId}/{hash}/{x-fylr-signature}/{version}/{region}/{size}/{rotation}/{quality}.{format}
/eas/iiif/{fileId}/{hash}/{version}/{region}/{size}/{rotation}/{quality}.{format}
```

**Path parameters**

* `fileId` — The ID of the file.
* `hash` — The `hash` is the `file.hash` as described [here](https://docs.fylr.io/for-developers/system-data-types/file#hash).
* `obj_uuid` — The `_uuid` of the object the file is linked into. This is used for the permission check.
* `x-fylr-signature` — The signature to omit file permission checks. It will be added to the URL when retrieved through `/api/db`, `/api/search` or other endpoints which deliver fylr URLs.
* `version` — The `file.class_extension` as described [here](https://docs.fylr.io/for-developers/system-data-types/file#hash).
* `region` — The [IIIF region](https://iiif.io/api/image/2.0/#region) is a string with `x,y,w,h` and other format. Check the link for more information.
* `size` — The [IIIF size](https://iiif.io/api/image/2.0/#size) parameter determines the dimensions to which the extracted region is to be scaled. Check the link for more information.
* `rotation` — The [IIIF rotation](https://iiif.io/api/image/2.0/#rotation) specifies mirroring and rotation. A leading exclamation mark (“!”) indicates that the image should be mirrored by reflection on the vertical axis before any rotation is applied. The numerical value represents the number of degrees of clockwise rotation, and may be any number from 0 to 360. **fylr** only supports integer numbers for rotation. More information can be found in the link.
* `quality` — The [IIIF format](https://iiif.io/api/image/2.0/#quality) parameter determines whether the image is delivered in color, grayscale or black and white. Click on the link for more information.
* `format` — The [IIIF size](https://iiif.io/api/image/2.0/#size) parameter determines the dimensions to which the extracted region is to be scaled. Check the link for more information. Formats `jpg` and `png` are delivered with fast code if the quality is set to `color` or `default` and no `rotation` is requested.
