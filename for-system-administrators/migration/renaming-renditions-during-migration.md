---
description: if rendition names differ between source and target
---

# renaming renditions during migration

## Via /inspect/migration

{% hint style="info" %}
This is available in fylr from version **6.33.0**.
{% endhint %}

The Restore form on `/inspect/migration/` exposes a **Rename Versions** table with three columns:

| File class | Source version | Target version |
| ---------- | -------------- | -------------- |
| `image`    | `preview`      | `640px`        |
| `video`    | `1920p`        | `1080p`        |
| `image`    | `thumbnail`    | _(empty)_      |

* one row per rename mapping; the table auto-grows a new empty row as soon as the last one is filled
* leave **Target version** empty to remove the version on the target
* rows with an empty **File class** or empty **Source version** are ignored on submit
* when a backup is selected, the table is pre-populated from the restore parameters of the previous run for that backup
* on submit, the rows are serialized into the single `rename-versions` parameter (`<cls>.<version>:<new version>`, comma-separated) and passed to `fylr restore --rename-versions`

## Via command line

```
fylr restore --help

      --rename-versions=,...        Rename versions before uploading. This affects
                                    uploaded rights as well as file versions.
                                    The versions need to be given in the notation
                                    "<cls>.<version>:<new version>", e.g.
                                    "image.preview:640px" would replace the "preview"
                                    version of image to "640px". If the "<new version>"
                                    is omitted, the version is removed.
```
