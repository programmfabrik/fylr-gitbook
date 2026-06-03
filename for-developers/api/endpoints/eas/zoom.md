# /api/eas/zoom

The endpoint zoom is used to deliver tiles for images. Use the `/api/db` and `/api/search` endpoints to retrieve the base URL to zoom and add the parameters to pick the tile accordingly. Tiles can be of any size and position. This endpoint uses the default tile size `320`.

### `GET /eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}`
{% swagger src="../fylr-openapi.yml" path="/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
