# export

## Assets

### eas_fields

Check if the field name is requested in **eas_fields**. If yes, proceed.

### assets

1. Check for a rule in **assets**. A rule applies if any file in the array of files has an explicit rule.

1. If a rule applies but no explicit rule is defined, the file is exported only if it is *preferred*.

1. The explicit rule **false**, says to not export the file.

1. The explicit rule **true** applies the default rule to the asset. The default rule is in **eas_field** for the matched field name.

1. Any other rule must be a list of versions which versions of that file are exported.

1. A rule in assets always exports actual file version data, not just the **url** as it is possible with **eas_field**.

### eas_field

The **eas_field** exports actual file data if **files** is set to *true*. The version is determined by the **versions** array.

If **eas_field** specifies **data** to be exported, the **data** array contains a list of versions for which no actual file version data is exported, but only the **url** to the files as well as other information.

### element name

The element name for the exported file is the column name. It can be overwritten in **fields**.

### Example output

```xml
<file type="files" column-api-id="204">
    <files>
        <file>
            <eas-id>10</eas-id>
            <compiled>&lt;file 10&gt;</compiled>
            <class>image</class>
            <extension>jpg</extension>
            <class_extension>image.jpg</class_extension>
            <preferred>true</preferred>
            <technical_metadata>
                <width>1920</width>
                <height>1280</height>
                <aspect_ratio>1.5</aspect_ratio>
                <max_dimension>1920</max_dimension>
                <file_type_extension>JPG</file_type_extension>
                <mime_type>image/jpeg</mime_type>
                <format>landscape</format>
            </technical_metadata>
            <versions>
                <version name="original">
                    <path>files/sid-10-file-10-berlin.jpg</path>
                </version>
                <version name="big">
                    <url>http://localhost/apitest/api/v1/eas/download/11/big</url>
                </version>
                <version name="small">
                    <url>http://localhost/apitest/api/v1/eas/download/28/small</url>
                </version>
            </versions>
        </file>
    </files>
</file>
```

