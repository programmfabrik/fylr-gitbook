# /produce

This endpoint is used to produce a new version of the file. It allows to crop and rotate images, and to trim, crop, rotate, scale, mute and color-correct videos. The new file gets a new id. The `produce_version` setting from the parent is inherited.

The file is produced asynchronously: the response returns the new file in `pending` state, poll its status until it reaches `done` (or `failed`). Values the request accepts but the conversion cannot apply — a video rotation that is not a multiple of 90 degrees, a color value outside its range — fail there, not on the request.

Differs from easydb 5: easydb 5 accepts a `description` field (optional l10n) in the produce body; **fylr** ignores it — the request only reads `eas_parent_id`, `format`, `transform`, `trim`, `mute`, `color` and `height`.

### Image and video parents

From version 6.35.0 the parent file may be a video; before that, only images were accepted. Which options apply — and which target formats are valid — depends on the class of the parent:

* **Image parents** accept `format` (`jpg`, `jpeg`, `jp2`, `png`, `tif`, `tiff`, `bmp`, `gif`, `psd`, `webp`) and `transform` (`rotate-z` by any angle, `rotate-x` / `rotate-y` to mirror, `crop`).
* **Video parents** accept `format` (`mp4`, `mov`, `m4v`) and `transform` with the same semantics, but restricted to rotations in steps of 90 degrees and with crop width and height rounded down to even values (a codec requirement). In addition they accept `trim` (`start` / `end` in seconds on the source timeline), `mute` (drop all audio streams), `height` (scale to that height, keeping the aspect ratio) and `color`.

`color` is the classic set of grading controls — `temperature`, `tint`, `exposure`, `contrast`, `highlights`, `shadows`, `whites`, `blacks`, `saturation`, `vibrance` and `hue`. Every one of them is neutral at `0`, omitted ones keep the source value, and unless documented otherwise the valid range is `-100` to `100`. They are applied after the transformations, in the order white balance, tone curve, saturation and hue, vibrance.

Which extensions can be produced at all is decided by the produce recipes of the file worker, one per class; from version 6.35.0 that recipe's extension list is the only gate, which also makes `webp` sources producible.

### `POST /eas/produce`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/produce" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
