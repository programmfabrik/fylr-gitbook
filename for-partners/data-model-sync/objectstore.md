---
description: >-
  As partner you can use our objectstore infrastructure to transfer fylr (and easydb 5) data models between fylr instances.
---

# Data Model Sync

This can be used, for example, to develop a data model on a fylr staging instance of fylr and then transfer it to the fylr production instance.

If you want to use this service,

1. please create a support ticket.:
* Tell us the name of the instance.
* Ask for a unique identifier, which will be used as the objectstore-ID.
* Tell us about the usage type of each instance using the same data model. Examples: production, staging, test. But you are free to choose any term.

2. We will then provide you with an objectstore ID and a string describing the instance usage. They serve to identify and allow access. Therefore we will make them into strings which conform to our syntax and may contain a part that is not easy to guess.

3. They must be entered into the fylr base configuration (frontend):

* Server: https://schema.easydb.de/objectstore
* `UID`: `<objectstore-ID>`
* `Instance`: `<instance-usage-string>`

Yes, "easydb" in the objectstore's store URL is correct. This will be changed at a later time to reflect the current product fylr.

If you setup a new fylr instance, the objectstore's configuration can be entered (initially only) in the fylr.yml, too:

```yaml
default_client:
  datamodel:
    uid: <objectstore-ID>
    server: https://schema.easydb.de/objectstore
    instance: <instance-usage>
```

We decided to offer this service without a fee for now. We will reevaluate this based on the usage in the end of 2024.

Please let us know via support ticket if you have any questions.

