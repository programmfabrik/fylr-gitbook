---
description: >-
  Connect multiple FYLR instances to an objectstore to sync the data model
  between these instances and to make sure it can only be edited in one instance
  at a time.
---

# Objectstore

### Server

URL of the objectstore server. From the documentation or administrator of the used objectstore.

### UID

Identifier of the data model. It is chosen during objectstore configuration. So get this from the administrator of the used objectstore.

### Instance

Identifier of this FYLR instance. Each connected FYLR instance should use a different identifier. Hard to guess identifiers are more secure. You also get this from the administrator of the objecstore, or can propose one to them.
