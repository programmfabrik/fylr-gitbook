---
description: >-
  A fylr instance can be connected to an objectstore. The data model is then uploaded to the objectstore, or downloaded from the objectstore.
  Typically used to connect multiple fylr instances to the same objectstore UID: They then share the
  same data model. The objectstore makes sure that the data model is only edited in one instance  at a time and syncs it.
---

# Objectstore

### Server
URL of the Objectstore server. From the documentation or administrator of the used Objectstore.


### UID
Identifier of the data model. It is chosen during objectstore configuration. So get this from the administrator of the used Objectstore.


### Instance
Identifier of this fylr instance. Each connected fylr instance should use a different identifier. Hard to guess identifiers are more secure. You also get this from the administrator of the objecstore, or can propose one to them.
