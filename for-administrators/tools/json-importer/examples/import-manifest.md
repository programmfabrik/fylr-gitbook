---

---

# Import Manifest

Create a file named `manifest.json` with the following content:

```json
{
  "source": "Example Migration",
  "batch_size": 100,
  "payload_base_uri": "",
  "eas_type": "url",
  "eas_skip_errors": true,
  "eas_replace_url": "",
  "mapping": null,
  "payloads": []
}
```

This manifest is used to preload the migration data in the JSON Importer. All information in the manifest can also be changed in the frontend, so a manifest file is not needed, but very helpful.

* `source`: A name to identify the migration, can be freely chosen
* `batch_size`: Maximum number of objects from a payload that are posted in a single request
  * If the payloads contain more objects, the payloads are uploaded in parts
  * This value is necessary to control the request size
  * For complex objects which take a long time to be saved, it is possible that the request might time out. In this case, the batch size needs to be decreased
  * The internal limit of the server is `1000`
* `payload_base_uri`:
  * If the payloads are not stored in the same folder as the manifest (or on another server), this is needed to build absolute paths from the payload file names
  * This value needs to be the relative path to the payload folder
* `eas_type`: Preselect the asset upload type in the import dialog:
  * `direct`: The assets are uploaded using the browser (`put`)
  * `url`: Remote put: assets are loaded by the EAS using the URL (`rput`)
  * `ignore`: No assets are imported
* `skip_head_request`: Skip HEAD request in `rput` in **fylr**
* `eas_skip_errors`: Ignore file errors
  * If there are any errors during file upload, the error will not stop the import process
  * the error will only be logged
* `eas_replace_url`: optional server url for each file
  * If you use `http://localhost` in the urls in the payloads, this will be replaced by this server url
* `mapping`: optional mapping id
  * If this is an import mapping, during the import this mapping is applied for any matching objecttypes that have file fields
* `payloads`: List of the filenames of all payloads, in the order they are posted
