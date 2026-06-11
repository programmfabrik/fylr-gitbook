---
description: >-
  Reference of all server event types: when each event is created and which
  data is stored in its info field.
---

# Event Type Reference

Every action the fylr server logs is stored as an **event**. Besides the type and the timestamp, an event record can carry:

* the **acting user** — only for event types marked _user-logged_ below, and only if the event's group is enabled in the base configuration (user settings, `user_in_event_group`); selected user fields can additionally be copied into the event (`copy_to_event`). Login events always store the user, regardless of this setting.
* **record references** — for events about records or base objects: object ID, version, object type or basetype, and the global object ID.
* **`info`** — a JSON object with additional data, different per event type. This is what the largest part of this page describes.
* the **remote address** of the request that caused the event.

Events marked _pollable_ can be retrieved by clients through the event poll API (`GET /api/v1/event/poll`) to react to changes; all events can be searched in the [Events](../events.md) manager and through `GET /api/v1/event/list`.

This reference reflects fylr 6.34.0. Events are listed by their group as defined by the server.

## ADMIN

### BACKUP_DONE

Created when a [backup](../backup-manager.md) started via the Backup Manager finishes successfully. _User-logged, pollable._

`info`:

* `Started` — when the backup started
* `Elapsed` — how long the backup took
* `BackupOpts` — the backup options (format, whether events were included)

### BACKUP_FAILED

Created when a backup fails. _User-logged, pollable._

`info`: same as `BACKUP_DONE`, plus:

* `Error` — what failed

### BASE_CONFIG_UPDATE

Created when the [base configuration](../readme/README.md) is saved successfully. _User-logged, pollable._

`info`:

* `ScopedNames` — the configuration sections that were saved
* `Method` — HTTP method of the request (`POST` or `PATCH`)
* `Path` — the configuration path that was saved (`/` for the whole configuration)

### BASE_CONFIG_ERROR

Created when saving the base configuration fails (validation or save error). _User-logged._

`info`:

* `Error` — the error message
* `Method`, `Path` — as above

### DATAMODEL_COMMIT

Created when a data model change is committed. _User-logged, pollable._

`info`:

* `version` — the committed data model version
* `committed_at` — the commit timestamp

## SYSTEM

### CUSTOM_DATA_TYPE_UPDATER

Created when a custom data type updater run (background update of custom data type values, usually provided by a plugin) finishes successfully. _User-logged._

`info`:

* `log` — log lines of the run
* `stats` — counts: `total`, `updated`, `de_duplicated`

### CUSTOM_DATA_TYPE_UPDATER_ERROR

Created when a custom data type updater run fails. _User-logged._

`info`: same as `CUSTOM_DATA_TYPE_UPDATER`, plus:

* `error` — the error message

### EMAIL_SENT

Created when the server sends an email successfully.

`info`:

* `Template` — name of the email template
* `To`, `Cc`, `Bcc` — recipient addresses
* `Subject` — the subject line
* `Attachments` — per attachment: `ContentType`, `Filename`, `Size` (human readable), `Filesize` (bytes)

### EMAIL_SENT_FAILED

Created when sending an email fails.

`info`: same as `EMAIL_SENT`, plus:

* `Error` — the error message

### FILE_METADATA

Created when technical metadata is successfully extracted from an uploaded file. _User-logged._

`info`:

* `recipe` — name of the metadata recipe used
* `metadata` — the job receipt of the metadata job (commands run, timing; secrets removed)

### FILE_METADATA_ERROR

Created when metadata extraction for a file fails. _User-logged._

`info`:

* `recipe` — name of the metadata recipe attempted
* `receipt` — the job receipt (secrets removed)
* `body` — raw response body, only present when the response could not be parsed

### FILE_PRODUCE

Created when a file version (rendition) is successfully produced from an original.

`info`:

* `recipe` — name of the production recipe used
* `receipt` — the job receipt of the production job (secrets removed)
* `connInfos` — connection information of the executing server

### FILE_PRODUCE_ERROR

Created when producing a file version fails.

`info`: same as `FILE_PRODUCE`.

### FILE_DELETE

Created when a file is deleted from storage (e.g. by the janitor after it is no longer referenced).

`info`:

* `location_key`, `location_id` — the storage location
* `filename` — the deleted file
* `log` — log lines of the deletion

### FILE_DELETE_ERROR

Created when deleting a file from storage fails.

`info`: same as `FILE_DELETE`, plus:

* `error` — the error message

### FILE_MOVE

Created when a remote file is copied or moved into a fylr storage location (e.g. after an `rput` upload that referenced a remote URL).

`info`:

* `remote_url` — where the file came from
* `location_key`, `location_id` — the target storage location
* `startet`, `took` — start time and duration
* `size` — the transferred size (human readable)

### FILE_MOVE_ERROR

Created when copying/moving a remote file fails.

`info`:

* `remote_url`, `location_key`, `location_id` — as above
* `error` — the error message

### NOTIFICATION_SCHEDULER_FAILED

Created when the background notification scheduler (which compiles and sends scheduled notification emails) fails.

`info`:

* `Error` — the error message

### LICENSE_VALIDATION_FAILED

Created when the periodic license validation fails.

`info`:

* `Error` — the error message

### LICENSE_EXPIRATION_EMAIL

Created when a license expiration reminder email is sent to the administrators.

`info`:

* `expire_type` — phase of the expiry: `valid_to` (license still valid), `valid_to_grace` (in the grace period) or `expired`
* `days` — days until the expiry the email refers to
* `valid_to`, `grace_to` — end of the license period and of the grace period
* `external_url` — URL of the instance
* `email_to`, `email_cc` — recipients

### LICENSE_BINARY_TOO_NEW_EMAIL

Created when a reminder email is sent because the installed fylr binary is newer than the license allows.

`info`:

* `version` — the running fylr version
* `binary_release_date` — release date of the running binary
* `valid_to` — the license's valid-to date (if present)
* `external_url` — URL of the instance

### OBJECT_INSERT / OBJECT_UPDATE / OBJECT_DELETE

Created when a record is saved through the API or frontend: `OBJECT_INSERT` for a new record (version 1), `OBJECT_UPDATE` for a new version of an existing record, `OBJECT_DELETE` when a record is moved to the trash (deleted, but not yet purged). The record references (object ID, version, object type, global object ID) are stored on the event. _User-logged, pollable._

`info`:

* `standard` — the rendered standard (short display text) of the record in the database languages

### OBJECT_UNDELETE

Created when a record is restored from the trash. _User-logged, pollable._

`info`: same as above (`standard`).

### OBJECT_PURGE

Created when a record is permanently purged from the trash. _User-logged, pollable._

`info`: same as above (`standard`).

### USER_INSERT / USER_UPDATE / USER_DELETE

Created when a [user](../permissions/user.md) is created, updated or deleted. The user's ID and version are stored on the event (basetype `user`). _User-logged, pollable._

`info`:

* `login` — the user's login name
* `displayname` — the user's display name
* `reference` — the user's reference

### GROUP_INSERT / GROUP_UPDATE / GROUP_DELETE

Created when a [group](../permissions/groups.md) is created, updated or deleted. _User-logged, pollable._

`info`:

* `name` — the group name
* `displayname` — the group's display name
* `reference` — the group's reference

### POOL_INSERT / POOL_UPDATE / POOL_DELETE

Created when a [pool](../permissions/pools.md) is created, updated or deleted. A `POOL_UPDATE` is also created for a parent pool when its children change; deleting a pool cascades to its child pools. _User-logged, pollable._

`info`:

* `displayname` — the pool's name
* `shortname` — the pool's shortname
* `reference` — the pool's reference

### TAG_INSERT / TAG_UPDATE / TAG_DELETE

Created when a [tag](../permissions/tags-and-workflows.md#tags) is created, updated or deleted. _User-logged, pollable._

`info`:

* `displayname` — the tag's display name
* `shortname` — the tag's shortname
* `reference` — the tag's reference

### MESSAGE_INSERT / MESSAGE_UPDATE / MESSAGE_DELETE

Created when a [message](../messages.md) is created, updated or deleted. _User-logged, pollable._

`info`:

* `title` — the message title
* `message` — the message content
* `reference` — the message's reference

### OBJECTTYPE_UPDATE

Created for every object type whose definition changes during a data model commit (fields, masks, tags, workflows etc.). _User-logged, pollable._

`info`: none — the object type is identified by the references stored on the event.

### COLLECTION_INSERT / COLLECTION_UPDATE / COLLECTION_DELETE

Created when a [collection](../../for-users/quick-access/collections-and-presentations.md) is created, updated or deleted. Deleting a collection also creates events for its deleted child collections. _User-logged, pollable._

`info`:

* `displayname` — the collection's display name
* `shortname` — the collection's shortname (if set)
* `reference` — the collection's reference (if set)

### COLLECTION_UPLOAD

Created when files are uploaded into an upload collection (e.g. through the [hotfolder](../../for-system-administrators/integration/hotfolder.md)). One upload batch creates several of these events; all of them carry `path` (the file path of the upload). Depending on what happened, the events carry: _User-logged, pollable._

* per created or updated record: `object_in_batch` (position in the batch), `file_eas_id`, `file` (filename), `filesize`
* if a metadata mapping was applied: `metadata_mapping_profile`, `file_eas_id`, `file`, `filesize`
* if records were linked into a hierarchy from the directory structure: `file_eas_id`, `path`, `file`, `filesize`
* if an upload plugin ran: per log entry `log_entry`, `plugin` and the plugin's log fields (`file`, `file_eas_id`, `filesize`, `msg`, `status`, `system_object_id`)

### TRANSITION_INSERT / TRANSITION_UPDATE / TRANSITION_DELETE

Created when a [workflow](../permissions/tags-and-workflows.md#workflows) (transition) is created, updated or deleted. _User-logged, pollable._

`info`:

* `type` — the workflow type
* `operation_insert`, `operation_update`, `operation_delete` — which operations the workflow applies to
* `comment` — the workflow's comment

### MAPPING_INSERT / MAPPING_UPDATE / MAPPING_DELETE

Created when a [metadata mapping](../metadata-mapping.md) is created, updated or deleted (deletion also removes the mapping from collections that reference it). _User-logged, pollable._

`info`:

* `displayname` — the mapping's display name
* `profilename` — the mapping profile

### JANITOR

Created when a run of a [janitor](../readme/services.md) (periodic background maintenance, e.g. deleting unreferenced files or expired sessions) finishes successfully **and** processed at least one item — idle runs are not logged.

`info`:

* `type` — which janitor ran
* `run_time` — when the run started
* `batch_size` — the batch size used
* `count` — how many items were processed
* `log` — detailed log of the run

### JANITOR_ERROR

Created when a janitor run fails.

`info`: same as `JANITOR`, plus:

* `error` — the error message
* `count` — items processed before the error

### WEBHOOK

Created when a [workflow webhook](../readme/workflow-webhooks.md) is called and answers with a success status.

`info`:

* `webhook` — name of the webhook
* `response` — the webhook's JSON response, or `response_no_json` with the raw body if the response was not valid JSON

### WEBHOOK_ERROR

Created when a webhook call fails or answers with an error status.

`info`: same as `WEBHOOK`, plus:

* `error` — the error message or HTTP status

## INDEX

### OBJECT_INDEX

Created when a record or base object (user, group, pool, collection, message) is queued for indexing with elevated priority — routine background indexing is not logged.

`info`:

* `Priority` — the priority of the indexing job

### OBJECT_INDEX_ERROR

Created when the search cluster rejects a document during bulk indexing (e.g. disk full, mapping error).

`info`:

* `IndexName` — the target index
* `DocID` — the document that failed
* `Error` — the error reported by the search cluster

### OBJECT_INDEX_REQUEUE

Created when a document is rejected because the search cluster is overloaded and the document is automatically queued again.

`info`: same as `OBJECT_INDEX_ERROR`.

### INDEX_SWITCH

Created when the indexer finishes filling new indices and switches reading over to them. _Pollable._

`info`:

* `IndexNames` — the new read/write index names
* `Deleted` — old indices that were removed
* `Errors` — errors during the switch, if any

### REINDEX_START

Created when a full reindex starts. _Pollable._

`info`:

* `Datamodel` — the data model version being indexed
* `BlockFrontend` — whether the frontend is blocked during the reindex

### REINDEX_QUEUED

Created when all records and base objects have been queued for the new indices (from this point on, normal operation continues while the indexer works through the queue).

`info`:

* `Counts` — per indexed type, how many items were queued
* `IndexVersions` — the index versions created for this reindex
* `Took` — duration from reindex start until queueing finished

### REINDEX_DONE

Created when a full reindex finishes and the indices have been switched. _Pollable._

`info`:

* `BlockFrontend` — whether the frontend was blocked
* `IndexVersionsQueued`, `IndexVersions` — the index versions at queue time and after the switch
* `Took` — total duration of the reindex

### REINDEX_ERROR

Created when a full reindex fails during preparation. _Pollable._

`info`:

* `Error` — the error message

### REINDEX_INDEX_PURGED

Created when a leftover index from an earlier, unfinished reindex is purged before a new reindex starts.

`info`:

* `Indexes` — the purged index

## FRONTEND — events sent by the web frontend

The events of this group are not created by the server: the web frontend sends them via `POST /api/v1/event`. The server stores their `info` as sent — so any API client may post these types with its own `info` — but the standard web frontend sends the payloads documented here. All are _user-logged_.

### DETAIL_VIEW

Sent when a user opens the detail view of a record.

`info`:

* `global_object_id` — the viewed record
* `object_id`, `objecttype` — the record's ID and object type
* `pool` — for records in a pool: the pool's `id`, `shortname` and `name`; additionally `pool.1` … `pool.N` with the same keys for every level of the pool path
* `connector_name`, `connector_url` — for records viewed from a connected remote instance: its name and URL

### SEARCH

Sent after a search with a non-empty query returns.

`info`:

* `request` — the executed search: `search` (the full search definition), `offset`, `limit`
* `response` — `count` (number of hits) and `timings` (`request_time` on the server, `client` in the browser)
* `version` — version of the frontend's search-state format

### FRONTEND_ERROR

Sent when a JavaScript error occurs in the frontend.

`info`:

* `message` — the error message
* `stack` — the JavaScript stack trace
* `navigator` — the browser's user agent

### ASSET_DOWNLOAD_CONFIRMATION_MESSAGE

Sent when a user confirms a download confirmation dialog (an admin message of type _download_ with "send confirmation event" enabled) before downloading assets.

`info`:

* `identifier` — the confirmation identifier configured on the admin message
* `choices` — the options the user selected in the dialog (`reference`, `text`)
* `assets` — the assets the confirmation covers
* `global_object_ids` — the records the assets belong to

## TASK

### TASK_INSERT / TASK_UPDATE

Created when a background task (e.g. a scheduled metadata update) is created or updated. _User-logged._

`info`:

* `module` — the task module
* `description` — the task description

### TASK_DELETE

Defined, but currently never created by the server.

### TASK

Created when a background task finishes successfully. _User-logged._

`info`:

* `task_module` — the task module
* `params` — the task parameters (with defaults applied)
* `status` — the final status (`DONE`)
* `status_msg` — status message, if any
* `start`, `end`, `took` — start time, end time and duration

### TASK_ERROR

Created when a background task fails or is canceled. _User-logged._

`info`: same as `TASK` (`status` is `ERROR` or `CANCELED`), plus:

* `error` — the error message

## EXPORT

All export events carry `state` in `info` — the status of the export at the time of the event. All are _user-logged_.

### EXPORT_START

Created when an [export](../../for-users/download-and-export/exporting.md) starts.

`info`:

* `state` — the export status
* `lastRunAt` — when the export ran the last time (only for re-runs)

### EXPORT_FINISH

Created when an export finishes successfully with at least one exported record.

`info`:

* `totalCount` — number of exported records
* `warnings` — warnings, if any
* `plugin_log` — log of the export plugin, if one ran

### EXPORT_FINISH_EMPTY

Created when an export finishes but matched no records (`totalCount` is `0`). `info`: same as `EXPORT_FINISH`.

### EXPORT_FAILED

Created when an export fails.

`info`:

* `error` — the error message
* `job_receipt` — receipt of the plugin job, if one ran

### EXPORT_CANCELED

Created when a user stops a running export.

`info`: only `state`.

### EXPORT_TRANSPORT

Defined, but currently never created by the server (see the two events below).

### EXPORT_TRANSPORT_FINISH

Created for each transport of an export (e.g. copy to another server, send by email) that finishes successfully.

`info`:

* `transport` — the transport configuration
* `transport_state` — the transport result (`DONE` or `DONE_WITH_WARNINGS`)
* `transport_log` — log of the transport plugin
* `job_receipt` — receipt of the transport job, if available
* `email_sent_to` — recipients, if the transport sent emails
* `email_sent_error` — error while sending emails, if any

### EXPORT_TRANSPORT_FAILED

Created when a transport fails.

`info`: same as `EXPORT_TRANSPORT_FINISH` (with `transport_state` = `FAILED`), plus:

* `error` — the error message

## UPLOAD

### FILE_UPLOAD

Created when a file upload via `POST /api/v1/eas/put` completes successfully. _User-logged._

`info`:

* `file` — the complete file object (ID, filename, filesize, hash, MIME type, uploading user, storage location, …)

### FILE_UPLOAD_REMOTE

Created when a remote file is registered via `POST /api/v1/eas/rput` — whether the file is fetched or left on the remote server. _User-logged._

`info`:

* `file` — the file object, including the remote URL and whether the file stays on the remote server

### FILE_UPLOAD_ERROR

Created when a file upload fails (size limit, interrupted transfer, storage error, missing rights). _User-logged._

`info`:

* `error` — the error message
* `file` — the (possibly partial) file object

## DOWNLOAD

### FILE_DOWNLOAD

Created when a file is delivered as a download (download disposition, as opposed to inline display, e.g. for previews) via `/api/v1/eas/download`. _User-logged._

`info`:

* `file` — the complete file object
* `bytes_count` — bytes delivered
* `statuscode` — HTTP status of the delivery
* `url` — the request URL (access tokens removed)
* `produce_params` — the conversion parameters, if a custom version was produced on the fly

### FILE_DOWNLOAD_ERROR

Created when a file download fails or is aborted (file missing, connection lost, …). _User-logged._

`info`: same as `FILE_DOWNLOAD`, plus:

* `error` — the error message

### OBJECT_DOWNLOAD

Created once per record whenever records are delivered through the export machinery — e.g. exports to JSON/XML/CSV/XLSX/HTML and OAI-PMH harvesting. The record references are set on each event. _User-logged._

`info` (for exports):

* `export_type` — the export format
* `export_id` — the export, if it was saved
* `export_user_id` — who started the export
* `export_producer`, `export_has_schedules` — export details
* `url` — the request URL

`info` (for OAI-PMH): `url`, `oai_pmh` (the harvesting request) and any keys the harvester passed in the `event.info` query parameter.

### EXPORT_DOWNLOAD

Created when an export result is downloaded — a single file or the whole export packed as ZIP or tar.gz. _User-logged._

`info`:

* `state` — the export status
* `url` — the request path
* `bytes_count` — bytes delivered
* `export` — `name`, `is_archive`, `format` (`file`, `zip` or `tar_gz`)
* `files` — the contained files (`path`, and for assets `_id` and `bytes`)

### EXPORT_DOWNLOAD_ERROR

Created when an export download fails before or during delivery. _User-logged._

`info`: same as `EXPORT_DOWNLOAD`, plus:

* `error` — the error message

## LOGIN_LOGOUT

### LDAP_DEBUG / SAML_DEBUG

Created after a **successful** [LDAP](../readme/user-management.md#ldap) or [SAML](../readme/user-management.md#saml) login **when debug logging is enabled** in the login method's configuration. _User-logged._

`info`:

* `log` — the full log of the login: connection, user lookup, attribute mapping, group assignment, user synchronization

### LDAP_ERROR / SAML_ERROR

Created when an LDAP or SAML login fails at any stage (connection, bind, user search, group lookup, user synchronization). _User-logged._

`info`:

* `log` — the log of the login up to and including the error

### USER_LOGIN

Created after every successful login, with any method (password, email, LDAP, SAML, anonymous/guest, collection link, action code, "keep me logged in", plugin user). With two-factor authentication enabled, the event is created only after the second factor was completed. The acting user is always stored.

`info`:

* `method` — the authentication method
* `client` — the OAuth2 client used
* `groups` — the user's groups
* `two_factor` — the second factor used (`email`, `totp`, `passkey`), or `<none>` if 2FA was active but not required for this login; omitted when 2FA is disabled
* `login` / `email` — the login name or email address used (depending on the method)
* `loginused` — for root-on-behalf logins (`root/password` form): the root login used
* `idp` — the identity provider URL (SAML logins)

### USER_LOGIN_FAILED

Created when a login fails because of wrong credentials, or when an account is temporarily locked after too many failed attempts. Other failure reasons (unknown user, disabled account, license problems) do not create this event. The acting user is always stored (when known).

`info`:

* `method` — the authentication method attempted
* `error` — why the login failed
* `attempt` — the failed-attempt count within the current blocking window (when the user is known)
* `groups` — the user's groups (empty if the user is unknown)
* `client` — the OAuth2 client (token endpoint logins)

### USER_LOGOUT

Created when a user ends the session by revoking the access token (`/api/oauth2/revoke`). The acting user is always stored.

`info`:

* `client` — the OAuth2 client of the revoked token
* `method` — the original authentication method, if known
* `groups` — the user's groups
* `error` — only present if the revocation itself reported an error

## PLUGIN

Plugins can declare their own event types in their manifest (`custom_events`). These types are registered when the plugin is loaded and behave like frontend events: they are posted through `POST /api/v1/event`, and their `info` is entirely defined by the plugin.
