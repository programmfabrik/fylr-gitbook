# /api/eas/zoom

The endpoint zoom is used to deliver tiles for images. Use the `/api/db` and `/api/search` endpoints to retrieve the base URL to zoom and add the parameters to pick the tile accordingly. Tiles can be of any size and position. This endpoint uses the default tile size `320`.

### URL templates

These GET endpoints embed parameters inside a path segment (e.g. `{quality}.{format}`), which the interactive API panel can't render — they are listed here as URL templates instead. All live under the `/api/v1` base path.

```
/eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}
/eas/zoom/{fileId}/{hash}/obj_uuid/{obj_uuid}/{x-fylr-signature}/{version}/zoom{zoom_viewport}/size{zoom_tile_size}/avoid_interpolation/part{zoom_x}x{zoom_y}.{format}
```

**Path parameters**

* `fileId` — The ID of the file.
* `hash` — The `hash` is the `file.hash` as described [here](https://docs.fylr.io/for-developers/system-data-types/file#hash).
* `version` — The `file.class_extension` as described [here](https://docs.fylr.io/for-developers/system-data-types/file#hash).
* `zoom_viewport` — The viewport is the width of the desired rectangle for the tile selection. The minimum is 100. If the original image width is 4000px and the viewport is 40000px, the zoom factor will be 10. The image is zoomed so that the width of the resulting image is as large as this parameter.
* `zoom_x` — Within the viewport zoomed image `zoom_x` is the tile number on the x-axis on a tought grid. The tile size is 320 unless given otherwise. If an image is 3200px (width) x 16000px (height) and the viewport is 32000px, we have a zoom factor of 10. With a tile size of 320, this results in a grid of 100 x 50 tiles.
* `zoom_y` — Within the viewport zoomed image `zoom_y` is the tile number on the y-axis on a tought grid. The tile size is 320 unless given otherwise. If an image is 3200px (width) x 16000px (height) and the viewport is 32000px, we have a zoom factor of 10. With a tile size of 320, this results in a grid of 100 x 50 tiles.
* `format` — The output format of a tile. The internal compute chain works with a `BMP` without alpha channel. So, the zoomer will not support transparency for `PNG`, but use a white background instead.
* `zoom_tile_size` — The tile size for the zoom responses in pixels. Default is `320`.
* `x-fylr-signature` — The signature to omit file permission checks. It will be added to the URL when retrieved through `/api/db`, `/api/search` or other endpoints which deliver fylr URLs.
* `obj_uuid` — The `_uuid` of the object the file is linked into. This is used for the permission check.
