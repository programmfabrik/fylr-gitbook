# /resync

From version 6.36.0. Compare the produce config the renditions of the existing files were produced with against the produce config fylr runs now, and produce the renditions that differ again.

fylr keeps a fingerprint of the produce config per class, rendition and extension: the recipe, the values of the params its commands use (an empty or missing param counts as its default), the source rendition and the custom metadata of the entry that produces the rendition for the extension (a class can configure a rendition more than once, each entry for its own extensions). Display settings (display name, group, standard, rights management, watermark marker) and timeouts are not part of it. The fingerprint moves on when a re-sync is queued, or when no file is left whose renditions differ. A `POST /config` that changes the produce config asks the same question as `POST /eas/resync` (see the `produce_resync` parameter there).

An instance that updates from a fylr before 6.36 on the default produce config compares against the 6.35 default, so the defaults an update changes are offered for a re-sync. Nothing is re-synced on its own.

Requires the `system.config` system right (`system.root` always satisfies it).

### `GET /eas/resync`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/resync" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /eas/resync`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/resync" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
