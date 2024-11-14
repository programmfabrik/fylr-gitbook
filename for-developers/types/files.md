---
hidden: true
---

# files

The type `files` stores a list of files. One of the files must be marked as the preferred file. That is used in the standard rendering as well as other outputs.

## API

Files need to be uploaded into `fylr` via the [**/api/eas**](../api/endpoints/api-eas.md) endpoint. That endpoint will assign a unique ID to that file. That file ID can be used to link the file to an object using the API.

```json5
{
  "file": [
    {
      "_id": 10,
      "preferred": true,
      "name": "myfile",
      "frontend_prefs": {
         "myapp": {
           "custom 1": "value 1
         }
      },
      // when receiving there are plenty more properties here
    }
  ]
}
```

There are 3 properties which only belong to the relation between the object and the file: `preferred`, `name`, `frontend_prefs`.

API users must use the `frontend_prefs` starting with a top level property identifying themselves. In the above example, that would be myapp. To the API user unknown top level properties must be written back as read.&#x20;

## Index

Only the preferred file of the list of files will be stored in the index.

Export

The XML Export looks like this:

```xml
<file type="files" column-api-id="2">
  <files>
    <file>
      <eas-id>1</eas-id>
      <compiled>AI, 8 x 8 mm, 1 p., 1.1 MB</compiled>
      <class>image</class>
      <extension>ai</extension>
      <name>myfile</name>
      <class_extension>image.ai</class_extension>
      <preferred>true</preferred>
      <technical_metadata>
        <height type="int">22</height>
        <max_dimension type="int">22</max_dimension>
        <file_type_extension type="string">ai</file_type_extension>
        <colorprofile type="string">Coated FOGRA27 (ISO 12647-2:2004)</colorprofile>
        <width type="int">22</width>
        <aspect_ratio type="float64">1</aspect_ratio>
        <create_date type="string">2008-02-25T11:22:30+01:00</create_date>
        <mime_type type="string">application/pdf</mime_type>
        <date_time_original type="string">2008-02-25T11:22:30+01:00</date_time_original>
        <extension type="string">ai</extension>
        <sha256_hash type="string">4f6f16d751a8549e576e693926ef5edd1415af2c85adf91ada08f59ee26373c7</sha256_hash>
        <filesize type="int">1062969</filesize>
        <dimensions>
          <height type="float64">30.2347</height>
          <unit type="string">pts</unit>
          <width type="float64">30.2347</width>
        </dimensions>
        <pages type="int">1</pages>
        <format type="string">square</format>
      </technical_metadata>
      <versions>
           ....
      </versions>
    </file>
  </files>
</file>
```
