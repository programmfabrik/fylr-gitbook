# API docs audit log

Working document. **Not linked in `SUMMARY.md`** — it is a curation log, not a
published page. It records what was checked when the OpenAPI source under
`resources/apidocs/` (in the `fylr` code repo) was verified against the actual
handler code, plus the cross-cutting things learned along the way.

The product owner curates this; the AI appends verified findings per endpoint
area. Every claim here is tied to a concrete code location so it can be
re-checked. **easydb 5** (`https://docs.easydb.de/en/technical/api/`) is the
human-written reference for the same API contract and is used as a cross-check.

## Status

| Endpoint area | Verified against code | Notes |
| --- | --- | --- |
| `db` | ✅ pilot, render-verified | 6 fixes (forbidden example, dry_run, id-gaps, skip_reverse_nested save semantics, concrete 202s + `DbPost202`/`DbDelete202` examples, neutral `package`); locked-error confirmed correct (a wrong "fix" was reverted); verified live via `spec.json` + HTML page |
| all 28 non-`db` areas | ✅ done, render-verified | fan-out in 4 waves of 7 (config/export/webdav/system/plugin/eas/suggest · mask/task/user/collection/objecttype/pool/schema · event/group/objects/right/message/search/transitions · db_info/l10n/oai/publish/settings/tags/xmlmapping). Plus a global `package` neutralization (27 schemas). See "Fan-out summary" below. |

## Fan-out summary

Done in 4 parallel-agent waves (one read-only audit pass over all 28 areas, then
4 apply waves; every bug re-verified against code, each wave render-verified on a
live instance, committed per area). **Totals:** 277 fixes applied, **24 audit
"bugs" rejected as false positives** (with code reasons), 17 registered-but-
undocumented routes documented (product owner: document them all), 72 examples
added from real `test/api`/loca sources, **93 items flagged** for human review.
Commit prefix `apidocs:`; the apidocs YAML lives in the `fylr` code repo.

### Lesson added mid-fan-out: error-envelope `parameters`

`parameters` = the error's generated `*Params` struct, and the codegen adds
`Realm` + `StatusCode` to **every** such struct — so an error example's
`parameters` must list the code-specific fields **plus** `realm` + `statuscode`.
Several agents stripped them after misreading **partial** apitest fixtures
(fixtures assert presence, not absence). Six schemas were corrected (a dedicated
commit) and the rule baked into the later wave prompts. Verify the field set from
the `*Params` struct in `errors.go`, never from a fixture.

### Punch-list — likely CODE / product issues surfaced (not doc fixes)

These were documented as-is but look like real code or product questions:

- **`/system/reindex` has no ACL/auth** (`api_system.go:163`, `search.IndexAll`) —
  anonymous callers can trigger a full reindex.
- **`/suggest` handler bug** — `suggestGET` calls `writeError` on a body-decode
  failure but does **not `return`** (`api_suggest.go:31`).
- **`/task` handlers swallow `acl.Require` errors** — `if err != nil { return }`
  without `writeError` (`api_task.go:39`), same class as suggest.
- **`DELETE /event/list` with no filters** is an unbounded delete of the whole
  event log (no guard).
- **`/objects` HEAD runs a full export** (handler binds GET+HEAD to one func);
  the `version=date/<ISO>` selector **panics** ("VersionDate not implemented").
- **`message` save with empty `_groups` clears** the group set (replace, not
  merge).
- **`GET /publish` and `GET /event/list`** return all rows unbounded (no
  limit/offset).
- **Access-control doc claims with no code enforcement:** `mask` `_all_fields`
  (claimed `system.root`) and `HEAD` reads (claimed `system.datamodel`) have **no**
  such gate; `pool` GET of a missing pool returns a generic `400`, not `404`.
- Public-by-design but worth confirming: `GET /plugin`, `GET /l10n/static`,
  `GET /suggest` (no auth).

## Method (per endpoint area)

For each area `resources/apidocs/endpoints/<area>/`:

1. **Routes.** Read the route registration (`internal/server/api/api_<area>.go`,
   `registerRoutes(... r.PathPrefix("/<area>").Subrouter())`). Confirm every
   documented path + HTTP method exists, and that no registered route is
   undocumented.
2. **Parameters.** For each handler, list what it actually reads from
   `req.URL.Query()` / `mux.Vars` / the decoded struct (often via
   `golib.JsonUnmarshalQuery`). Match names, enums, defaults, and required-ness
   against the docs. Enums must come from the real constants, not prose.
3. **Request / response bodies.** Trace the decode target and the
   `s.writeJSON(...)` payload type to confirm the documented schema shape.
4. **Errors — the priority.** For every error response, find the code site that
   raises it and record: the `code` (the type's `ErrorCode()` or the
   `errors.yml` key), the `Package()`, the message template, and the
   `parameters` the error type actually carries. The example in the schema must
   match what the running server returns — **never invent one.**
5. **easydb 5 cross-check.** Where fylr keeps the easydb 5 contract, confirm the
   shape against the easydb 5 technical API docs.
6. **Verify the served output, not just the source.** The rendered spec is
   **cached until fylr restarts** — editing the `.yml` does not change what
   `/inspect/apidocs/` shows until a restart. After editing, confirm the change
   reached the served bundle (`curl <backend>/inspect/apidocs/spec/spec.json |
   grep ...`), and for any claim "added to both X and Y" re-read the final file
   and cite each location. A grep hit in the source, or an editor success, is not
   proof the consumer sees it. (Trace correctness claims from the handler down,
   too — a symbol existing is not the endpoint reaching it.)

## How errors work (cross-cutting)

- Error envelopes are generated from per-package `errors.yml` files (codegen →
  `errors.go`). The envelope serialised to JSON has: `code`, `error` (the
  rendered message **plus** a `\n\nPackage: <pkg>\nCode: <code>` footer),
  `package`, `parameters`, `realm`, `statuscode`.
- The `code` is the `errors.yml` key (= the type's `ErrorCode()`); the
  `package:` value is the `package:` declared at the top of that `errors.yml`
  (= the type's `Package()`), **not** the package that calls the constructor.
  Errors raised deep in a pipeline keep their *origin* package.
- `parameters` mirrors `realm`/`statuscode` plus whatever typed params the error
  carries (the `p:` block in `errors.yml`). An error with no extra params shows
  only `realm` + `statuscode` there.
- **Database-driver errors are translated centrally**, not in the handlers, by
  `ferrors.ConvertToApiError` (`internal/ferrors/api.go`). PostgreSQL: `23505` →
  `DatabaseUniqueKeyViolation` (carrying the constraint name), `55P03`
  (lock_not_available) → `DatabaseLockError` (423), any other `pgErr` →
  `DatabaseError`; SQLite unique violations are matched by `checkSqliteError`.
  So on **any write endpoint** a `400 DatabaseUniqueKeyViolation` or a
  `423 DatabaseLockError` originates here — look for it in the converter, not in
  the endpoint's own error sites. Reuse the same canonical example for these two
  across write areas rather than re-deriving per area.
- Known error `errors.yml` homes seen so far:
  - `internal/ferrors/errors.yml` — package `ferrors`: the broad shared catalogue
    (`ReadOnlyMode`, `LookupFoundTooMany`, `LookupNotFound`,
    `DatabaseUniqueKeyViolation`, `SchemaInconsistent`, `ObjectInsufficientRights`,
    `UserRequired`, …).
  - `internal/api/acl/errors.yml` — package `acl` (`SystemRightRequired`, …).
  - `internal/api/object/save/errors.yml` — package `save` (`ResourceLocked` →
    423, `ResourceNotFound` → 404, …).
  - `internal/server/api/errors.yml` — package `api` (`UnknownObjecttype`,
    `DeepLinkAccessDisabled`, EAS errors, …).
- **Footnote on message rendering:** a right is rendered
  `needs right "{{ .RightDisplayname }}" ({{ .Right }})` — display name in
  quotes, machine key in parentheses (e.g. `"Write" (write)`). Getting the two
  the wrong way round in an example is an easy mistake (it was wrong in the
  `db` forbidden example — see below).
- **`package` is for clients to ignore.** The internal Go package name
  (`ferrors`, `acl`, `save`, `api`, `dbinfo`, …) is meaningless to an API
  consumer. Do **not** explain it per-code or enumerate "`api` for X, `ferrors`
  for the rest." Every error schema's `package` description should read like:
  "internal origin marker for fylr support; not part of the API contract —
  branch on `code`, not `package`." **Done so far:** the base/shared envelopes
  (`error.yml`, `unauthorized_error.yml`, `forbidden_error.yml`,
  `not_found_error.yml`) and the five `db_*` schemas. **Still carrying the old
  prose — fix in each area:** the area-specific `*_error.yml`
  (`grep -rl 'package that raised the error' resources/apidocs/schemas/` — ≈16:
  collection, eas, pool, group, user, task, search, share_link, email_send,
  tags, db_info, …). The HTML render is what surfaced that the *shared* 401/404
  schemas, not just the `db_*` ones, render on the `db` page — verify the served
  page, not only the files you edited.
- **202 (`response_202`) is a confirm-and-resend protocol, document it
  concretely.** Body is `{tasks:[{title,message,form?,buttons[]}]}`
  (`internal/ferrors/repsonse202.go`). A button or form option carries the query
  parameter to resend in `name` and the value in `value`. For every endpoint
  that can 202, list the actual cases with the real `param=value` to resend
  (e.g. `revoke=yes`, `delete_policy=remove`), not "resend with the matching
  parameter." **Never put an endpoint-specific example on the shared
  `response_202`** — it is `$ref`'d by POST, DELETE and `config`, which return
  different tasks. For a concrete example, make a dedicated per-operation schema
  that composes it: `allOf: [$ref "response_202.yml"]` + a schema-level
  `example:` (see `db_post_202.yml` / `db_delete_202.yml`). Composition by file
  `$ref` is a proven pattern here (`task.yml` → `schedule.yml`). Same rule for
  any shared schema reused across endpoints with differing real payloads.

## How writes allocate ids (cross-cutting)

Applies to **every create endpoint**, not just `/db`.

- New `_id` (per object type), `_system_object_id` (per instance) and other
  auto-increment ids (`object.id`, `value.id`, `publish.id`, …) are drawn from
  the `sequence` package (`internal/util/sequence/sequence.go`) via
  `sequence.GetNewIds(...)`, called from inside `ol.Save()`
  (`internal/api/object/object_save.go:245,337,458,475`).
- **The sequence is not part of the request transaction (Postgres).**
  `newSequence` opens its own transaction on a second handle
  (`global.G.DB2.Begin()` + `LOCK TABLE sequence`, `sequence.go:48-58`) and
  `commit()` commits it independently (`sequence.go:249`). So once ids are
  drawn they are spent even if the request later rolls back → permanent gaps,
  ids never reused. (On SQLite it is instead a `SAVEPOINT` on the *main* tx,
  `sequence.go:59-68`, so there it would roll back — dev/test only.)
- **`dry_run` allocates nothing** because it returns before `ol.Save()`
  (`save_objects.go:187`). A `dry_run` create therefore returns an object with
  no `_id` / `_system_object_id`. Do not document `dry_run` as "rolls back a
  full save" — nothing is written, so there is nothing to roll back.

## Doc-source conventions worth remembering

(From `resources/apidocs/README.md`; repeated here because they bite during an
audit.)

- A schema with `code` enums lives in its own `schemas/*.yml` and is registered
  in `api.yml`. Endpoint files reference it via `$ref`.
- Examples render only from a schema-level `example:`. A `$ref`'d schema cannot
  carry a sibling example in some render paths — that is why each error has its
  own dedicated schema.
- `x-path` on a path item gives brace-containing paths (`/db/{objecttype}`) a
  clean page URL; operations sharing an `x-path` render on one page.
- Datamodel-driven files (`{{ range $.Datamodel.Tables }}`) emit one concrete
  path per object type **and** a static generic `/db/{objecttype}` fallback so
  the area is always documented even on an empty instance.

---

# Findings by area

## `db` — record create / read / update / delete (pilot)

Source: `resources/apidocs/endpoints/db/`. Handler:
`internal/server/api/api_db.go`. Routes registered:

- `POST /db/{objecttype}` → `dbPOST`
- `GET /db/{objecttype}/{mask}/{objectId}` and
  `GET /db/{objecttype}/{mask}/{objectId}/{objectId2}` → `dbGET`
  (`objectId == "list"` re-dispatches to `dbListGET`; `objectId2` carries the
  ID for the `system_object_id` / `global_object_id` addressing forms)
- `DELETE /db/{objecttype}` → `dbDELETE`

### Fixed

1. **`schemas/db_forbidden_error.yml` — example message had the right reversed.**
   `ObjectInsufficientRights` renders
   `The object #{{.SystemObjectID}} [{{.Objecttype}}] needs right
   "{{.RightDisplayname}}" ({{.Right}})`
   (`internal/ferrors/errors.yml`, `ObjectInsufficientRights.o`). With
   `right: write` / `rightdisplayname: Write` the real line is
   `needs right "Write" (write)`; the example had `"write" (Write)`. Corrected.
2. **`db.yml` `dry_run` description — described the wrong behaviour.** It said
   fylr "runs the complete save … but rolls the transaction back." In fact
   `SaveObjects` returns at `save_objects.go:187` (`if sctx.DryRun { return
   ol.Delivered(), nil }`) **before** `ol.Save()` — it runs the schema /
   constraint / permission validation, persists nothing, and commits an empty
   transaction (there is no rollback). Crucially, since `ol.Save()` is the only
   id allocator, **a created object gets no `_id` / `_system_object_id` under
   `dry_run`**. Rewrote the param to say so.
3. **`db.yml` POST descriptions — added the id-numbering note.** `_id` and
   `_system_object_id` come from the `sequence` package, which on Postgres
   commits on a **separate** connection (`global.G.DB2.Begin()`,
   `internal/util/sequence/sequence.go:48`) — not the request transaction. So a
   real save that draws ids and then fails leaves permanent gaps; ids are never
   reused. Documented on both the generic and per-objecttype POST.
4. **`db.yml` POST `skip_reverse_nested` — described only the response, missed
   the save semantics.** On POST this param sets `lctx.SkipReverseNested`
   (`api_db.go:167`), which `load_context.go:61` documents as "Ignore reverse
   nested during **load & save**." Default behaviour (`ExpandForSave`,
   `object_api_list.go:735-815`): the top-level object **governs** its
   reverse-nested; any reverse-nested it still has but that is **omitted** from
   the payload is **deleted** (`DeletedAt`, comment `<reverse nested delete:
   …>`, line 810). A reverse-nested is **kept** if it is resent (matched by
   `_system_object_id` or `table_api_id`+`object_id`, lines 754/761 — a stub
   with the unchanged `_version` suffices), if its top-level path parent was
   skipped for an unchanged `_version` (782), or if its mask field is read-only
   (801). `skip_reverse_nested=true` skips the whole reconciliation (735) **and**
   ignores reverse-nested in the payload for saving (656) — the top level is
   saved alone. Rewrote the POST param to say this; left the **GET/list** copy
   (`dbReadQueryParams`, response-only) unchanged — correct there, since GET has
   no save path. NB: the param is defined twice in `db.yml`; only the
   `dbPostParams` copy was the bug.
5. **`db.yml` 202 responses — too generic; now describe real cases + values.**
   A 202 is a `ferrors.Response202` = `{tasks:[{title,message,form?,buttons[]}]}`
   (`internal/ferrors/repsonse202.go`); a button/form option carries the query
   parameter to resend in `name` and the value in `value`. Documented the
   concrete cases with their real values: POST → revoke (`revoke=yes`,
   `save_objects.go:305`), transition (`confirmTransition=…`,
   `transition.go:323`), reverse-pool (form `reverse_pool_changed_mode` with
   `…_always`/`…_never`, `object_api_list.go:96`); DELETE → delete-policy (form
   `delete_policy` = `remove`/`setnull`/`create_collection`,
   `object_delete.go:526-585`), transition (preserves a chosen `delete_policy`
   as a hidden button, `object_delete.go:764`). **Examples:** `response_202` is
   **shared** — POST, DELETE and `config` all `$ref` it — so an endpoint-specific
   example on it would be wrong on the other two. Left `response_202` example-free
   and created dedicated `schemas/db_post_202.yml` and `schemas/db_delete_202.yml`,
   each `allOf: [$ref response_202.yml]` + its own real `example:` (POST = revoke
   task; DELETE = delete-policy task; English loca from `resources/fylr.csv`
   `object.Save.Revoke.*` / `object.Delete.*`). POST/DELETE 202s now `$ref` those
   (registered in `api.yml`); `config` keeps the generic `response_202`.
   **Property descriptions:** added a description to **every** `response_202`
   property (16/16 leaves), grounded in `repsonse202.go` — emphasising the ones a
   frontend turns into the confirmation URL: a button's `name`/`value`
   (`ConfirmKey`/`ConfirmValue`) and a form field's `name` + option `value`. Got
   the operative-vs-decorative split right per code: the server reads `revoke` /
   `confirmTransition` / `revoke:confirmTransition` (buttons) and `delete_policy`
   / `reverse_pool_changed_mode` (form), but **not** the generic `confirm` submit
   button. Render-verified: the property descriptions carry through the `allOf`
   into `DbPost202`/`DbDelete202` on the live HTML page — so composing a shared
   schema with `allOf` preserves both `example` and per-property descriptions.
6. **`package` field — removed the Go-package noise from all five `db` error
   schemas + the base `schemas/error.yml`.** The internal Go package name
   (`ferrors`, `acl`, `save`, `api`) is meaningless to an API consumer, and the
   per-code mapping ("`api` for `UnknownObjecttype`, `ferrors` for the rest") is
   pure noise. Replaced with: "internal origin marker for fylr support; not part
   of the API contract — branch on `code`, not `package`."

### Verified correct — and a trap to avoid

- **`schemas/db_locked_error.yml` is correct as-is** and must not be "fixed":
  `code: DatabaseLockError`, package `ferrors`, `423`, message
  `Unable to acquire a lock for resource "".`, param `object`
  (`internal/ferrors/errors.go:540`, `errors.yml` key `DatabaseLockError`).
  The 423 a `/db` write can return is produced centrally by
  `ferrors.ConvertToApiError` (`internal/ferrors/api.go:86`) when PostgreSQL
  returns `55P03` (lock_not_available) inside the `ExecWriteTX`. `.Object` is
  left empty on that path, hence `object: ""`.
- **Trap (a first pass got this wrong and had to revert):**
  `internal/api/object/save/` also defines `ErrResourceLocked()` — code
  `ResourceLocked`, package `save`, also `423`. But its call sites
  (`lock.go`, `unlock.go`, `put.go`, `delete.go`) are **WebDAV `Resource`
  methods**, firing on a lock-token mismatch against the `webdav_lock` table —
  they are *not* reachable from the `/db` JSON handlers. Lessons: (1) the
  `save` package holds both the object-save pipeline **and** WebDAV resource
  code — same package, unrelated callers, so a grep hit in a package is not
  proof of the call path; (2) grep `LockError` as well as `Locked` (the `/db`
  type is `DatabaseLockError`, which the word `Locked` does not match).

### Confirmed correct (left unchanged)

- **POST query params** all match `dbPOST` (`api_db.go:66`–`183`):
  `format` (default `standard`), `dry_run`, `collection`, `collection_policy`
  (`setinvalid`/`remove`), `file_url_expire`, `skip_reverse_nested`,
  `skip_bidirectional_update`, `skip_index`, `skip_constraints`, `skip_plugins`,
  `skip_events`, `confirmTransition`, `revoke` (`yes`),
  `revoke:confirmTransition` (value `yes:<token>`), `reverse_pool_changed_mode`.
- `skip_plugins` / `skip_events` requiring `system.root` is real
  (`api_db.go:79`).
- **GET query params** match `dbGetUrlParams` (`api_db.go:224`): `format`
  (default `full`), `file_url_expire`, `skip_reverse_nested`, `all_versions`,
  `latest_linked`, `version`, `merge_linked_objects`, `merge_max_depth`.
- `merge_linked_objects` enum (`none`, `in_main_search`, `not_in_main_search`,
  `not_in_main_search_unless_reverse`, `all`) matches the real constants in
  `SetMergeDepth` (`internal/api/fcontext/output.go:896`). NB: the *Go struct
  comment* at `api_db.go:231` is stale (`"not_in_main_search", …, "all"` and
  omits `in_main_search`) — the docs are right, the comment is wrong.
- `reverse_pool_changed_mode` enum (`reverse_pool_changed_always`,
  `reverse_pool_changed_never`) matches `MASK_MODE_REVERSE_POOL_CHANGED_*`
  (`internal/api/datamodel/mask_api.go:21`). The internal `_ask` mode is
  correctly *not* offered as a query value — it is a mask config that triggers
  the 202.
- **DELETE** body is `[object_id, version, comment]` triples (`delTripleArr`,
  `api_db.go:522`); query params `delete_policy` (`setnull` / `remove` /
  `create_collection` / `undelete` / `purge`, from
  `object_delete.go:26`) and `confirmTransition` (`DeleteOpts.TransitionConfirm`,
  `object_delete.go:35`). Trash policies `undelete` / `purge` require
  `system.trash_access[level=…]` (`api_db.go:611`).
- **DELETE 200 body** matches `DeleteAnswer` (`object_delete.go:40`): `policy`,
  `removed`, `setnull`, `create_collection`.
- All referenced error codes exist with the documented packages:
  `UnknownObjecttype` (`api`), `SystemRightRequired` (`acl`), and
  `ReadOnlyMode` / `LookupFoundTooMany` / `LookupNotFound` /
  `DatabaseUniqueKeyViolation` / `SchemaInconsistent` / `ObjectInsufficientRights`
  (`ferrors`).
