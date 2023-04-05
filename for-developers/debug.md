# Release v6.3.0

## Highlights

Changes and improvements all over the place. Our Zoomer got a lot faster now (make sure to use our latest iiif service configuration, see below) and we added a re-sync button to produce new file versions easily.

## New

* `/inspect/files` got a new `Re-sync done` button. It can be used to **re-sync** done originals. That is helpful after the base config was changed to update all auto produced versions.
* Includes **public OAUTH2 clients** for integrators & our mobile App.
* New endpoint `/api/event/stream` allows to open a Websocket listening to fylr's event stream. Latest web frontend uses that too, so no more polling for events. With this change, updating the search after updating a record should be almost immediate.
* `fylr.services.api.oauth2Server.allowHttpRedirects`: This new settings allows to configure **OAUTH2 in HTTP only environments**. Before this was only supported for `http://*.localhost`. This is useful in intranet environments where it is hard to obtain HTTPS certificates regularly.
* Introducing chain loaded `fylr.yml`. Now it is possible to use multiple `-c` on the command line to pass in more than one `fylr.yml`. A new internal `fylr.default.yml` is a starting point which can be used for most configurations. It includes a fully configured execserver (for Linux & Mac OS systems). The new `.yml` format allows to replace, add and delete value from config files which were loaded first. Current `fylr.yml` setups continue to work, as the new syntax requires a top level property `fylr+:` to use the merge functionality. More information can be found in `fylr.example.yml`.

## Improved

* **Much faster tile production for IIIF and Zoomer output**. The new code uses a BMP interim format and fast system memory mapping to achieve fast tile production, especially for big images. You need to add the `convert` command to the `iiif` service in your fylr.yml:
```yaml
fylr:
  services:
    execserver:
      services:
        iiif:
          commands:
            convert:
              prog: convert
```
* Zoomer endpoint now also supports `.png` output.
* Support encrypted data in export plugin transport options. If a property ends in `:secret` it's value will be stored safely in fylr's database and only decrypted when presented to the transport plugin.
* Actually use password requirements as defined in the base config. Before we only stored the regexps, but never enforced them. Administrators can overwrite the policy and have the server ignore it.
* Added preview for `pptx`. Before we only had `ppt` support.
* No more standard cached are used on `/api/db` endpoint. This makes sure that linked object data gets merged from the current database rather than from the standard cache which follow the indexer.
* Fast indexer wake-ups in system which have the indexer running on the same fylr binary as the API service. This makes the indexer less laggy and together with the new event stream facility, the web frontend can show changes almost immediately.

## Fixes

* Reading images width & height was buggy if the EXIF data contained different values. Fixed by relying solely on `exiftool` Composite information about the file size. This causes the Zoomer to behave erratically.
* Parallel access to WebDAV volumes has been fixed. `rclone` easily runs 8-10 parallel tasks to sync files, that caused our WebDAV endpoint to produce errors pretty quickly.
* Certmagic now works on Port 80 to pose the Let's encrypt challenge. With that issuing HTTPS certificates gets easier behind certain firewall configurations.
* `/api/search/parse` got more syntax fixed. This time a simple `OR` case failed to compile correctly.
* Fixed aggregations in hierarchies. If hierarchies were filtered by parent, in bigger lists the filter was filtering the wrong data and not returning any results.
