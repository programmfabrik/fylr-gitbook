---

---


# Starting the migration

## Complete Manifest

After all payloads have been created and the filenames have been added to the payload list, this is the manifest we use to migrate all basetypes and objects:

```json
{
  "source": "Example Migration",
  "batch_size": 100,
  "payload_base_uri": "",
  "eas_type": "url",
  "eas_skip_errors": true,
  "eas_replace_url": "",
  "skip_head_request": true,
  "mapping": null,
  "payloads": [
    "basetype-tags.json",
    "basetype-groups.json",
    "basetype-users.json",
    "basetype-pools.json",
    "userobject-orte-level-0.json",
    "userobject-orte-level-1.json",
    "userobject-orte-level-2.json",
    "userobject-personen.json",
    "userobject-schlagwoerter.json",
    "userobject-bilder-0.json",
    "userobject-objekte-0.json",
    "userobject-objekte-1.json",
    "basetype-collection-0.json",
    "userobject-bilder-0-version-2.json"
  ]
}
```

## Import process

In the frontend, open the [JSON Importer](..#json-importer). Enter the URL of the manifest, and click "Load". The Importer will list all Payloads, and preselect some settings that were saved in the manifest.

{% hint style="info" %}
If the manifest can not be loaded, check if the browser might be blocking the request. For more information, see: [Handling problems with Mixed Content](../README.md#handling-problems-with-mixed-content)
{% endhint %}

### Asset Upload

For uploading assets, select the upload type in the dropdwon menu "File upload type":

* *Direct*: The assets are uploaded using the browser. This may have an impact on the performance and the migration duration
* *URL (remote put)*: The assets are loaded by the EAS using the URL. This might be the faster type of upload
* *Ignore files*: No assets are imported. Use this option if you want to run a faster test migration

This can be preselected by defining `eas_type` in the manifest file.

If the assets are stored on a different server, and you want to specify this server only for the migration process, you can use `http://localhost` as the server url for all assets in the `eas:url` entries in the payloads. The actual server path is set in the field "File replace url". If this field is not empty, `http://localhost` will be replaced by this URL.

In the examples above, the URLs could also have been specified in the form

```json
"eas:url": "http://localhost/photo-1560930950-5cc20e80e392?w=800&q=80"
```

and the actual URL `https://images.unsplash.com` would be set in the JSON Importer.

## Run import

After all settings are done, click "Prepare". The payloads are loaded into the JSON Importer and are parsed and validated. This might take some time, depending on the size and number of payloads.

After this, click "Start" to run the migration.

## Result of the migration

If the import of the migration was successful, we expect the following objects in the main search in the frontend:

* Object `bilder`, with link to `objekte` `"112233"`
* Object `bilder`, with updated link to `objekte` `"987654321"`
* Object `objekte` with reverse edit link to `bilder` `"bild_01"`
* Object `objekte` with reverse edit link to `bilder` `"bild_02"`
