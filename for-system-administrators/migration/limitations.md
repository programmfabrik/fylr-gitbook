---
description: >-
  This page gives an overview of technical limitations of the migration process and differences between the source and target instance.
---

# Limitations and differences

Due to technical reasons, and especially due to different implementation details between the easydb5 API and the fylr API, a restored instance is not a 100% true copy of the source instance. There will be more differences between easydb5 and fylr instances, but also between restored fylr instances.

{% hint style="warning" %}
The differences mentioned on this page are not exhaustive!

Other differences between source and target instances might occur.
{% endhint %}

## General differences

IDs can not always be restored. In general, sequential IDs are assigned to inserted basetypes and records by the target fylr instance. This is necessary to avoid possible collisions between imported IDs and IDs which have been assigned during the purge process, or are already in the system during partial migrations.

A few exceptions are made, but these are limited to a few IDs and a few record types. For all other relations between records and basetypes, lookups to unique references are used. Existing references are restored, but missing references are generated during the migration process. This means that any restored basetype will have a reference, either the original reference, or a new reference:

| Basetype | Restored IDs | Fallback for missing `reference` |
|---|---|---|
| User | - | `user:<source ID>` |
| Group | - | `group:<source ID>` |
| Pool | - | `pool:<source ID>` |
| Tag Group | - | `taggroup:<source ID>` |
| Tag | Tag ID | `tag:<source ID>` |
| Collection | - | `collection:<source ID>` |
| Message | - | `message:<source ID>` |

For records, the System ID (`_system_object_id`) and the UUID (`_uuid`) are restored. The Global Object ID (`_global_object_id`) is partially restored, the old instance ID is replaced by the new instance ID, but the System ID part is not changed: `<System ID>@<Source Instance ID>` will become `<System ID>@<Target Instance ID>`. The Object ID (`_id`) is not restored, but lookups referencing the System ID are used.

{% hint style="warning" %}
Since IDs are generally not restored, scripts which use hard coded IDs are not recommended!

Lookups should be used instead. References are unique, and all restored objects will either have a reference or a System ID.
{% endhint %}

## Differences between easydb5 and fylr

In addition to IDs, there are more differences between easydb5 and fylr. Since there are different technologies and concepts behind the systems, some data can not be restored at all, and will be ignored or changed.


### Migration of the Base Configuration

Due to different implementations, fylr uses a base configuration which has some differences compared to the base configuration of the easydb5. This is the reason why the base configuration can **not be migrated 1:1**. Some settings are not used in fylr and will be automatically ignored during the migration process.

Other settings from the easydb5 have a different format in fylr and will be migrated if there is a corresponding setting in fylr. The following list shows the corresponding settings which will be transferred.

{% hint style="warning" %}
This list is not complete. There still might be other settings which are not migrated.
{% endhint %}

| Setting in easydb5 | Setting in easydb5 (internal) | Setting in fylr | Setting in fylr (internal) |
|---|---|---|---|
| "Extended functions" ▸ "Logo and Header" | `system.logo` | "General" ▸ "Appearance" | `system.config.appearance.logo` |
| "Login" ▸ "Anonymous access from internet" ▸ "Anonymous from internet allowed" | `system["login.internet"].value` | "Access" ▸ "Login" ▸ "Allow guest access" | `system.config.login.guest` |
| "Login" ▸ "Information next to the login" ▸ "Information (Markdown)" | `system["login.welcome_info"].message` | "Access" ▸ "Login" ▸ "Login Info Text (Markdown)" | `system.config.login.info` |
| "Login" ▸ "Welcome text (Markdown)" | `system["login.welcome_text"].value` | "Access" ▸ "Login" ▸ "Login Label" | `system.config.login.label` |
| "Login" ▸ "User can initiate a forgotten password process" ▸ "Show request dialog in login" | `system["login.forgotten_password_process"].show_in_login_dialog` | "Access" ▸ "Password" ▸ "Hint for Supported Passwords" | `system.config.password.showforgot` |
| "Login" ▸ "Password check" ▸ "Regular expression" | `system["login.password_policy"].policy[].expression` | "Access" ▸ "Password" ▸ "Password Requirements" | `system.config.password.check[].regexp` |
| "Login" ▸ "Password check" ▸ "Hint" | `system["login.password_policy"].hint` | "Access" ▸ "Password" ▸ "Show 'Forgot password?' on login page" | `system.config.password.hint` |


### Migration of Events

If events are migrated (see parameter [`--include-events`](#--include-events)), there are differences between easydb5 and fylr. For some events, the eventtype or the basetype is changed. Also there are events in easydb5 which have no matching event in fylr, these events are not migrated at all.

The event info block will be migrated without any changes. IDs which relate to objects, files, etc., are replaced during the restore process. This is done for IDs on top level (`object_id`), and known IDs in the info block.

In the following table, all migrated events are listed, including changes which are automatially done during the restore process. Events which are not listed here are **never migrated** from easydb5 to fylr.


<!--

part below was auto generated
source: https://docs.google.com/spreadsheets/d/1FkbU1t-WuDQ6YSRKUu2VYR8Hdg3x6ZPBntFFmI4VUM4/export?format=csv&gid=0
timestamp: 2025-06-27 08:34:25 (UTC)

-->

| Eventtype in easydb5 | Eventtype in fylr | Notes |
|---|---|---|
| `ASSET_DOWNLOAD_CONFIRMATION_MESSAGE` | `ASSET_DOWNLOAD_CONFIRMATION_MESSAGE` | <ul><li>Basetype is set to `message`, there was no basetype in easydb5<li>The following IDs in the info block are replaced: <ul><li>`assets.#.id`: The ID is replaced with the new file ID</ul></ul> |
| `CUSTOM_TYPE_UPDATER_RESPONSE` | `CUSTOM_DATA_TYPE_UPDATER` | <ul><li>Eventtype is changed</ul> |
| `CUSTOM_TYPE_UPDATER_START` | `CUSTOM_DATA_TYPE_UPDATER` | <ul><li>Eventtype is changed</ul> |
| `CUSTOM_TYPE_UPDATER_RESPONSE_ERROR` | `CUSTOM_DATA_TYPE_UPDATER_ERROR` | <ul><li>Eventtype is changed</ul> |
| `CUSTOM_TYPE_UPDATER_RESPONSE_FAILED` | `CUSTOM_DATA_TYPE_UPDATER_ERROR` | <ul><li>Eventtype is changed</ul> |
| `SCHEMA_COMMIT` | `DATAMODEL_COMMIT` | <ul><li>Eventtype is changed</ul> |
| `DETAIL_VIEW` | `DETAIL_VIEW` |  |
| `EMAIL_SENT` | `EMAIL_SENT` |  |
| `DOWNLOAD_EXPORT` | `EXPORT_DOWNLOAD` | <ul><li>Eventtype is changed</ul> |
| `ASSET_DOWNLOAD` | `FILE_DOWNLOAD` | <ul><li>Eventtype is changed<li>Basetype is changed from `asset` to `file`<li>The following IDs in the info block are replaced: <ul><li>`export._id`: The related record is not migrated, the ID is set to `null`<li>`export_user_id`: The ID is replaced with the new user ID</ul></ul> |
| `ASSET_EXPORT_DOWNLOAD` | `FILE_DOWNLOAD` | <ul><li>Eventtype is changed<li>Basetype is changed from `asset` to `file`<li>The following IDs in the info block are replaced: <ul><li>`export._id`: The related record is not migrated, the ID is set to `null`<li>`export_user_id`: The ID is replaced with the new user ID</ul></ul> |
| `OBJECT_DELETE` | `OBJECT_DELETE` |  |
| `OBJECT_INSERT` | `OBJECT_INSERT` |  |
| `OBJECT_UPDATE` | `OBJECT_UPDATE` |  |
| `SEARCH` | `SEARCH` |  |
| `USER_CREATED` | `USER_INSERT` | <ul><li>Eventtype is changed<li>Basetype is set to `user`, there was no basetype in easydb5</ul> |
| `USER_LOGIN` | `USER_LOGIN` | <ul><li>Basetype is set to `user`, there was no basetype in easydb5</ul> |
| `USER_LOGOUT` | `USER_LOGOUT` | <ul><li>Basetype is set to `user`, there was no basetype in easydb5</ul> |
| `WEBHOOK_OK` | `WEBHOOK` | <ul><li>Eventtype is changed</ul> |
| `WEBHOOK_ERROR` | `WEBHOOK_ERROR` |  |

<!--

part above was auto generated

-->

