---
label: Changes 5 > 6
---

# easydb 5

## Changes from easydb 5 to fylr

### Architectural changes

#### General

The general architecture of fylr is different from easydb5. The main server is written in [Go](https://go.dev) based on a microservices architecture. This should allow better scaling and use less hardware resources than easydb5.

#### Indexer

fylr uses OpenSearch as its primary indexing tool, but also supports ElasticSearch (same as in easydb5).

#### Database

fylr supports [PostgreSQL](https://postgresql.org) and (for development/testing) [Sqlite](https://sqlite.org) as database backend. Other backends can be added more easily as we no longer use database stored procedure or triggers any more.

All objects are stored in a key-value based system, which makes API commit much faster and lighter. It also enables us to have pool based datamodel specifics and a later point.

All history objects are stored in the same key-value based system which makes it much easier and faster to access history version.

#### File storage

fylr uses a database for metadata and can use [S3 ](https://en.wikipedia.org/wiki/Amazon\_S3)storage or traditional file storage for assets and previews.

#### Export

The export is not using disk space anymore to export objects. When starting an export, only a list of files is computed. When the file is requested, its being generated on the fly.

* export/stop is not supported any more
* assert export attributes does nothing with "JSON" and "EASParentId" attributes
* \_log loads only events from the last run
* csv subfield separator has changed from "#" to "."
* csv field syntax has changed, there is no longer output into a nested collection cell using \[]
* csv option "empty\_columns" is no longer supported
* FILE\_DOWNLOAD & OBJECT\_DOWNLOAD are new events. "event.info" can be passed via url for additional log entries in the event.info field

**Mapping + XSLT**

* Mapping can be used with `xml_one_object_per_file=false`
* Mapping can be used together with XSLT processing

#### File worker chain

The file worker chain (formerly easydb-asset-server) is new and rethought. The chain can now be configured using base config. The worker system can employ any program to generate any versions for any file. So besides the standard setup for images, videos, and office files, you can easily extend this system to configure preview generations of your choice, such as 3D, CAD, or other files.

### Upgrade

Upgrade from easydb5 to fylr requires a complete backup & restore. The `fylr` binary provides a command line facility to export an easydb 5 (or fylr) and restore into a fylr using the API.

### API facing changes

Most of the API will stay unchanged in fylr. In most cases all API accessing programs including the easydb Webfrontend should work as before.

#### Rightsmanagement

The `extensions` setting for `allow_upload` is gone. Only `classes` can now be configured. All `extensions` which are configured for the specific class are then allowed to be uploaded.

`collection.BAG_CREATE[inherit_owner]` is not supported by fylr. `inherit_owner` is always assumed.

Remove `UNLINK` from `_generated_rights` of objects (api/db & api/db\_info). The `UNLINK` right exists for pools as well as collections, so it is ambigious in the context of an object.

#### `_standard`-Rendering

If `_standard.1` has no data, the fallback to `#<system-object-id>` is set even if there is `_standard.2` or `_standard.3`. In easydb 5 we would not set `_standard.1` if either one was set.

When rendering linked objects the `_standard.1-3` is merged with the top level's on each standard level.

fylr only supports 1 hop for `_standard`-Rendering.

```
    OK object.lk_artist_id -> artist.name
    OK object.lk_artist_id -> artist.nested_alternatives.aname
NOT OK object.lk_artist_id -> artist.nested_synonym.lk_synonym_id -> synonym.name
```

The reason for this change is that fylr does not keep `_standard` around, it computes this for every request.

Also, the `_standard` render rule has changed, the separator is now a rule for "before" and not for "after".

#### xml format `easydb_flat`

This format is no longer supported in fylr. It has been a format which used the internal tables in easydb 5 and dumped them. We could mimic this in fylr, but since that format is not in widespread use, we removed support for it.

### Custom Data Type Updater

* "plugin\_info" is gone, use "%info.json%" command line replacement instead.
* updater scripts can return event log information
* new action "end\_event"
* state is map\[string]interface{}
* `log` can be delivered, this will be added to `event.info.Log`

#### OAI/PMH

The **XSLT** is applied to the full output of the verb, not only to one record.

The easydb XML elements are not prefixed using **easydb:** anymore. Instead we set **xmlns** on the top level easydb XML element.

We support sets for collections now. Also, the set names might have changed. The collection sets reported for each record are not filtered by the rightsmanagement of the user.

Non spec "limit" url parameter.

New endpoint **/oai**

#### /api/db

Format **full**:

* includes empty fields (easydb 5 did not include empty fields in format **full**.)
* `_changelog` contains different fields than easydb 5, for versions changelog is also complete (with all versions)
* date\_range type aggreates in the middle (from+to/2) and not at "from"
* no "base\_types\_only" support in group mode

Additional support:

* \_version:auto\_increment: true
* \_tags.\_id:lookup.reference (check: is this really new?)
* \_create\_user: system.root can set the creating user (used for migrations), \_create\_user is also in the output
* skipConstraints: allows to skip unique checks & no pool storage (for migrations)

#### /api/db\_info

* /update: "\_available\_tags" are not including "is\_default" any more. This is not very useful with multiple pools as the pools can define their own defaults for the tags.
* output of \_generated\_rights includes more rights than in easydb 5

#### /api/eas

* class\_version\_extensions is no longer being indexed
* metadata groups have a new "value" next to "print"
* \_not\_allowed is not used, instead version is skipped
* format: `short` does not return versions, new format `standard` does
* POST /eas/put on longer supports mapping, use GET /eas instead
* GET /eas?mapping always requires objecttype
* rput has a "delete\_url" now to pass in an url which is called upon delete of the file

#### /api/export

* new url parameter `format` can be used to filter output for `_log`
* `_log` is now sorted `ASC`

#### /api/group

* `_ipv4_subnet_filter` renamed to `_ip_subnet_filter`, added support for ipv6

#### /api/mask

The format=**xml** is no longer supported.

* System fields `_acl`, `_tags`, `_collection`, `_owner`, `_published` are hidden from API if configured not to be shown.
* `_all_fields` mask sets standard for 1st file field and all text fields.

#### /api/right/preset

* Getting a single preset via ID is new

#### /api/pool

* `_compiled_tags` got a new attribute `_origin` which shows the origin of the tag.

#### /api/search

* fields.with\_path is new, fields collecting for path items has changed. One entry is presented as individual array containing one element per path element, whereas easydb 5 would return individual path elements in one big array.
* sort.with\_path defaults to **false**
* include\_deleted is a new switch, which allows to also search deleted objects
* `changelog_range` understands `query` to set the type of the comment search
* type: event allows searching in events, "info" is searchable
* removed `class_version_extension` + `class_version_filesize`
* moved `technical_metadata.date_time_original`, `technical_metadata.create_date`
* colorprofile includes other, like sRGB
* `_linked._asset` supports the same fields as regular eas fields
* some `_linked._asset` are available in regular aggregations (like date fields)
* removed aggregation type `asset`. Use type `term` instead with `_linked._asset.` as prefix for the fieldname
* removed `search.highlight`, this is not supported in FYLR
* new sub search feature for type `in`. Take `field` to fetch and `subsearch` to perform a subsearch to fill the `in` parameter
* type `range` has new `from_equals` and `not_equals`
* new output formats: `standard_extended`, `long_inheritance`, `full_inheritance`
* new `point_in_time` feature
* new `search_after` feature
* `language` was changed to `languages`
* linked\_object facet has now `_linked_object`
* removed `format` from `date_range` aggregation
* new sort by "\_standard\_parent", "\_standard\_parents"

#### /api/schema

The format=**xml** is no longer supported.

* exclude/include always implies format "long" (TBD)

#### /api/settings

This endpoint loses all subpaths, as they have been moved to **/api/system**.

#### /api/system

New endpoint which offers:

* /purgeall: purge all data and start over, includes "set\_password"
* /reindex: initiate reindex
* /backup: perform a backgrounded backup
* /errortest: store a test error
* /status: status info about the server

#### /api/objects

The **column** can also target nested fields, but not reverse.

#### /api/eas

Renamed **skip\_extension\_check** to **produce\_versions=false**.

Format for "short" changed. Use "standard" for compability.

#### /api/objecttype

Added `_filename_replacements` as new top level attribute. This lists the available replacements for files.

Added `_compiled_tags` as new top level attribute.

#### api/eas/produce

The **transform** body parameter is no longer an array but a single transform entry

#### /api/session

* This endpoint was removed. Use OAUTH2 and /api/user/session instead

#### /api/event

* url parameter **base\_type** has been renamed to **basetype**
* POST /api/event is now symetric. It receives the event as an object inside the top level object's `event` property.
* DELETE /api/event/list is new, removed DELETE /api/event (url + body post)
* DELETE /api/event/_id_ is new
* url parameter "background=1" can be used to background event writing (use from within plugins to not dead lock sqlite installations)

#### /api/user

* default delete policy in base config is "ask" (not "delete")
* new endpoint /api/user/change\_password (moved from /api/user/session)
* include\_password=1 returns `_password_hash`, which includes method:hash (this is writable). This also throws an error if the user is not root. ez5 would not output the \_password\_hash in that case.
* GET /api/user/session returns the current session for the token
* user.created\_timestamp -> `_created_at`
* user.last\_updated\_timestamp -> `_updated_at`
* new: `_last_seen_at`

#### /api/collection

* Deep-Link changed for type collection and email users: login and password swapped for collection and for email the user logs in with email & uuid instead of email & acl uuid
* New API create\_object.linked\_object\_pools

#### /api/config

* Separate `system` and `plugin` config. New object layer `config`.
* Can be filtered accessed via path
* Supports partial updates now

## Unsorted (German)

* fylr ist in Go programmiert, nicht mehr in C++ wie die easydb 5. Dadurch läuft das theoretisch auf allen Betriebssystemen nativ
* fylr Binary ist 58MB und beinhaltet alle Services
* Neues Frontend-Design, ansonsten dasselbe wie in der easydb 5 mit kleineren neuen Modulen
* Einige Plugins sind in den Core gewandert: OAI/PMH, Webdav Support
* Webdav ist jetzt Read / Write, nicht nur Write und wird direkt von fylr unterstützt
* Es gibt keinen Apache + Easydb Asset Server (EAS) mehr
* Asset-Links sind nicht mehr Apache -> Platte sondern auch über fylr , d.h. sind auch rechtegemanagt
* fylr verbraucht weniger CPU/RAM als easydb 5 und ist horizontal skalierbar
* Alles was externe Programme betrifft ist in den fylr-Execserver ausgelagert, ein skalierbarer Mikroservice zum Ausführen von “Jobs”, zB Bilder kleinrechnen, Metadaten ziehen
* Sämtliche Plugin-Callbacks laufen auch über den Execserver. Plugins können dadurch in beliebigen Programmiersprachen entwickelt werden
* Exporter läuft auch über den Execserver so dass zb XSLT 3.0 benutzt werden kann
* FYLR läuft unter Docker / Kubernetes, docker-compose / Helm files verfügbar
* Filestorage läuft jetzt ausschliesslich über das S3 Protokoll. Soll weiterhin auf Platte direkt geschrieben werden braucht es einen Service wie Minio.
* Elastic haben wir immer noch, liefern es aber nicht mehr selber aus
* Alles was mit Dateien passiert und passieren kann (also Formatsumwandlungen, Metadata-Extraction, egal was), ist über .yml Recipes vom Administrator des System scriptbar. D.h. wir haben da nichts mehr hard-gecoded. Sogar die Metadata Extraction läuft über den Execserver (allerdings in unserem eigenen Binary welches wiederum exiftool aufruft, das kann man aber wrappen und erweitern)
* Metadataextraktion kann vom Typ abhängig gemacht werden
* Replacement von Original während Inject möglich
* CLI tool: fylrctl, wir noch ausgebaut. Soll eine Scriptzugriff auf die API bereitstellen
* fylrctl hat ein eingebautes “backup” + “restore” für API und DB basierte Migrationen
* der neue /inspect view ist ein Bare Metal DB View auf die Strukturen und Daten in fylr
* Aktuelle DBs sind Postgres + Sqlite. Wir wollen auch noch CockroachDB supporten (das gestaltet sich allerdings nicht so einfach, da die mit einem anderen TRANSACTION mode als Postgres unterwegs sind)
* Schema Updates in FYLR werden NICHT mehr in der SQL DB reflektiert, dort ist alles in einem Key-Value Verfahren gespeichert. D.h. die Anzahl der DB Tabellen in fylr ist fix und ändert sich nicht mit dem User Schema
* Plugins können über die Base Config aktiviert / deaktiviert werden. Auch können Plugins direkt im Frontend nachinstalliert werden
* Integrierter IIIF Support (Presentation API 3.0, Image API 2.0), Tiler konfigurierbar über den Execserver (d.h. ihr könnt zB alles auf JP2 umstellen, oder layered TIFFs)
* Integrieter Bilder-Zoom wird auf den IIIF Endpoint gemappt
* Front end plugins sind kompatibel mit easydb 5, die Server Plugin müssen angepasst werden. Hybrid Server Plugins mit shared Python Code sind möglich (so unser FTP Transport Plugin)
* Exporte werden in Echtzeit generiert und verbrauchen keine extra Plattenplatz mehr
* Die API hat einige für Migrationen sinnvolle Erweiterungen bekommen: Extern setzbare UUID, System Object ID, Object ID, verlinkung von "deferred" Objekts, d.h. ein Promise dass ein verlinktes Objekt später migriert wird
* Support von Polyhierarchien
* Support von automatischen Numerierungen zur Realisierung von Tektoniken
* Event sind jetzt auch in der Elastic und maximal schneller suchbar als in easydb 5
* Visuelles Backuptool im Inspect Backend (da sind wir noch nicht am Ende, schauen wir mal wo das Tool wirklich landet)
* Speicherplatzarmes ablegen der Custom Data inkl externer UUID. Ein Datum wird nur einmal abgelegt und dann verlinkt. In easydb5 wurde das in jeder Zelle als Kopie gehalten
* Datenmodell + Lokalisierung + Mappings sind jetzt auch in der Datenbank, d.h. es gibt "auf Platte" keine Dateien mehr die durch die Applikation angelegt werden
* "suggest" wird durch einen Term splitter in der DB unterstützt und braucht deshalb keine periodischen Index-Rebuilts mehr
* Schnelleres Rechtemanagement, Abfragen mit "generate\_rights: true" sind genauso schnell wir ohne
* Authentifizierung ist komplett neu und auf OAUTH2 umgestellt. Erweiterung auf OpenID ist vorgesehen, aber noch nicht umgesetzt. OpenID Client Unterstützung ist möglich, aber nicht umgesetzt.
* Geplant: Feldvererbungen in Hierarchien: Unbelegte Felder erben auf Wunsch automtisch die Einträge vom Vater bzw Großvater
* Geplant: Neue Limits für Gruppeneditor
* Idee: Asynchrone /api/db calls
