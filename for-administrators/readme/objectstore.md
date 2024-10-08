---
description: >-
  Connect multiple FYLR instances to an objectstore to sync the data model
  between these instances and to make sure it can only be edited in one instance
  at a time.
---

# Objectstore

### Server

URL of the objectstore server. Usually provided by Programmfabrik GmbH.

### UID

Identifier of the data model. It is chosen during objectstore configuration. Usually provided by Programmfabrik GmbH.

### Instance

Identifier of this FYLR instance. Each connected FYLR instance should use a different identifier. Hard to guess identifiers are more secure. Usually provided by Programmfabrik GmbH.

{% hint style="info" %}
It is possible to configure read-only instances which can only pull the data model from the objectstore server but cannot push the data model to the objectstore server. These instances must be given the suffix “-pull-only”.
{% endhint %}



### Tutorial

See our tutorial [here](https://docs.fylr.io/tutorials/objectstore) for more information.
