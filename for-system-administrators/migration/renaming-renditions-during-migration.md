---
description: if rendition names differ between source and target
---

# renaming renditions during migration

## Via /inspect/migration

Upcoming feature, soon to be documented.

## Via command line

```
--rename-versions=,...        Rename versions before uploading. This affects
                                    uploaded rights as well as file versions.
                                    The versions need to be given in the notation
                                    "<cls>.<version>:<new version>", e.g.
                                    "image.preview:640px" would replace the "preview"
                                    version of image to "640px". If the "<new version>"
                                    is omitted, the version is removed.
```
