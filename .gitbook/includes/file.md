---
title: file
---

<table>
        <thead>
            <tr>
                <th width="300">Field</th>
                <th width="155">Format</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody><tr>
        <td><code>_duplicates</code></td>
        <td><code>array<code></td>
        <td><p>If set, this attribute can hold an array of duplicates.</p>
</td>
    </tr><tr>
        <td><code>_id</code></td>
        <td><code>int64<code></td>
        <td><p>The <code>_id</code> is <strong>created</strong> <em>when</em> a file is uploaded into the fylr server.</p>
</td>
    </tr><tr>
        <td><code>_linked_objects</code></td>
        <td><code>array<code></td>
        <td><p>When a file is uploaded and linked to a collection via <a href="https://docs.fylr.io/for-developers/api/endpoints/api-eas"><code>/api/eas</code></a>, the attribute contains a list of objects created based on the upload settings of that collection.</p>
</td>
    </tr><tr>
        <td><code>_mapped_metadata</code></td>
        <td><code>object<code></td>
        <td><p>A rendered version of the object data retrived and mapped from this file's metadata. It can be used to create objects based on a pre-configured metadata mapping.</p>
</td>
    </tr><tr>
        <td><code>best_date</code></td>
        <td><code>timestamp<code></td>
        <td><p>Best date is a compiled UTC timestamp from the technical metadata. <strong>fylr</strong> uses the first set date from <code>technical_metadata.date_time_original</code>, <code>technical_metadata.create_date</code>, <code>date_uploaded</code>.</p>
</td>
    </tr><tr>
        <td><code>children</code></td>
        <td><code>array<code></td>
        <td><p>For originals which use a pageable format, like <code>PDF</code>, this attribute contains the pages available underneath the original. The format is string and the value is using the file's <code>_id</code> and the page number (starting at <code>0</code>) separated by <code>/</code>.</p>
</td>
    </tr><tr>
        <td><code>class</code></td>
        <td><code>string<code></td>
        <td><p>The compiled class of the file. The classes are set by the recipe. Standard recipes of fylr include <code>image</code>, <code>audio</code>, <code>office</code>, <code>video</code>. The fylr frontend uses the class to pick the general player to view the file. A class <code>unknown</code> is assigned if no matching recipe was found but the upload accepts <em>unknown types</em>.</p>
</td>
    </tr><tr>
        <td><code>class_extension</code></td>
        <td><code>string<code></td>
        <td><p>A compiled concatenation of <code>class</code>, <code>version</code>, joined by <code>.</code>. This is used for aggregations of files</p>
</td>
    </tr><tr>
        <td><code>class_version_status</code></td>
        <td><code>string<code></td>
        <td><p>A compiled concatenation of <code>class</code>, <code>version</code> and <code>status</code>, joined by <code>.</code>. This is used for aggregations of file status.</p>
</td>
    </tr><tr>
        <td><code>compiled</code></td>
        <td><code>string<code></td>
        <td><p>A compiled version of the metadata for this file. For images this looks like this: <code>	JPG, 1920 x 1285 px, 569.5 kB</code>.</p>
</td>
    </tr><tr>
        <td><code>compiled_props</code></td>
        <td><code>object<code></td>
        <td><p>A fielded version of <code>compiled</code>. Frontends can use this to beatify the compiled output of the metadata.</p>
</td>
    </tr><tr>
        <td>    <code>dimensions</code></td>
        <td><code>string<code></td>
        <td><p>The rendered dimensions for this file. This may include a unit. For page sizes European paper sizes like A4 will be recognised.</p>
</td>
    </tr><tr>
        <td>    <code>duration</code></td>
        <td><code>string<code></td>
        <td><p>Runtime of the audio or video file.</p>
</td>
    </tr><tr>
        <td>    <code>extension</code></td>
        <td><code>string<code></td>
        <td><p>The upper cased version of the <code>extension</code>.</p>
</td>
    </tr><tr>
        <td>    <code>pages</code></td>
        <td><code>string<code></td>
        <td><p>The number of pages followed by a <code> p.</code>. Frontends may localize this manually.</p>
</td>
    </tr><tr>
        <td><code>date_uploaded</code></td>
        <td><code>timestamp<code></td>
        <td><p>The UTC timestamp when this file was uploaded.</p>
</td>
    </tr><tr>
        <td><code>eas_parent_id</code></td>
        <td><code>int64<code></td>
        <td><p>The <code>eas_parent_id</code> is the id of the file this file is derived from. When using <strong>/api/produce</strong>, the newly produced files will get the parent id set to the file they are produced from.</p>
</td>
    </tr><tr>
        <td><code>extension</code></td>
        <td><code>string<code></td>
        <td><p>The compiled extension of the file. This is matched by parsing available recipes at the time of the metadata generation. Extensions are matched by longer length first. So for a file <code>flower.webdvd.zip</code> the extension matched would be <code>.webdvd.zip</code> and not <code>.zip</code> if there is an available recipe.</p>
</td>
    </tr><tr>
        <td><code>filesize</code></td>
        <td><code>int64<code></td>
        <td><p>The file size in bytes.</p>
</td>
    </tr><tr>
        <td><code>frontend_prefs</code></td>
        <td><code>object<code></td>
        <td><p>Set only in relation to an object. This map can contain custom attributes and values.</p>
</td>
    </tr><tr>
        <td><code>hash</code></td>
        <td><code>string<code></td>
        <td><p>The <code>hash</code> is a non unique identifier of the file. For remote files, it is the <a href="https://en.wikipedia.org/wiki/Md5sum"><strong>md5sum</strong></a> of the URL, for local files it is the <a href="https://en.wikipedia.org/wiki/SHA-2"><strong>SHA-256</strong></a> of the binary file data. It is calculated together with the metadata for the file and a copy of <code>technical_metadata.sha256_hash</code>. The <code>hash</code> is used for duplicate detection.</p>
</td>
    </tr><tr>
        <td><code>is_original</code></td>
        <td><code>boolean<code></td>
        <td><p>Set to true if the file is an original. It is false if the file is a generated or uploaded rendition. Produced files are registered as originals underneath the original they are produced from.</p>
</td>
    </tr><tr>
        <td><code>last_status_at</code></td>
        <td><code>timestamp<code></td>
        <td><p>The UTC timestamp when the last status change was last written to the database.</p>
</td>
    </tr><tr>
        <td><code>lookup:_id</code></td>
        <td><code>object<code></td>
        <td></td>
    </tr><tr>
        <td>    <code>reference</code></td>
        <td><code>string<code></td>
        <td><p>The <code>reference</code> of the file to look up.</p>
</td>
    </tr><tr>
        <td><code>metadata</code></td>
        <td><code>object<code></td>
        <td></td>
    </tr><tr>
        <td>    <code>groupnames</code></td>
        <td><code>array<code></td>
        <td><p>Sorted list of metadata group names found in <code>groups</code>.</p>
</td>
    </tr><tr>
        <td>    <code>groups</code></td>
        <td><code>object<code></td>
        <td></td>
    </tr><tr>
        <td><code>name</code></td>
        <td><code>string<code></td>
        <td><p>Custom name of the file. This is set in the relation to the object. When retrieving the file via <a href="https://docs.fylr.io/for-developers/api/endpoints/api-eas"><code>/api/eas</code></a>.</p>
</td>
    </tr><tr>
        <td><code>original_filename</code></td>
        <td><code>string<code></td>
        <td><p>The filename as set by <code>original_filepath</code> minus the path.</p>
</td>
    </tr><tr>
        <td><code>original_filename_basename</code></td>
        <td><code>string<code></td>
        <td><p>The filename as set by <code>original_filepath</code> minus the path and the detected <code>extension</code>.</p>
</td>
    </tr><tr>
        <td><code>original_filepath</code></td>
        <td><code>string<code></td>
        <td><p>Filename of the file as set during the upload. On Windows, this can contain drive letters and backslashes.</p>
</td>
    </tr><tr>
        <td><code>pages_allowed</code></td>
        <td><code>boolean<code></td>
        <td><p>Indicates that the file has pages.</p>
</td>
    </tr><tr>
        <td><code>preferred</code></td>
        <td><code>boolean<code></td>
        <td><p>This may be set if the file is in the context of an object. If set, preferred indicates that this version is the preferred one in a list of other versions.</p>
</td>
    </tr><tr>
        <td><code>reference</code></td>
        <td><code>string<code></td>
        <td><p>If set, this reference string is a unique string identifying the file. If the reference contains a <code>sha244:&lt;hash&gt;</code> or <code>sha256:&lt;hash&gt;</code>, the provided hash can be checked against the file's checksum using an action triggerable in <strong>/inspect/files</strong>. Other parts of the reference can be added but must be separated by <code>:</code>.</p>
</td>
    </tr><tr>
        <td><code>status</code></td>
        <td><code>string<code></td>
        <td><p>The status of the file. Known states are: <code>pending</code>, <code>processing</code>, <code>sync</code>, <code>done</code>, <code>failed</code>. Files and renditions can be accessed in status <code>sync</code> and <code>done</code>. Only files in state <code>done</code> can be exported.</p>
</td>
    </tr><tr>
        <td><code>technical_metadata</code></td>
        <td><code>object<code></td>
        <td><p>An object to describe technical aspects of the file. See <a href="https://docs.fylr.io/for-developers/system-data-types/file#technical_metadata">Technical Metadata</a> for details.</p>
</td>
    </tr><tr>
        <td><code>upload_user</code></td>
        <td><code>object<code></td>
        <td><p>The user who uploaded this file into the system. If the upload happens via Hotfolder, the uploader is the owner of the upload collection.</p>
</td>
    </tr><tr>
        <td>    <code>_basetype</code></td>
        <td><code>string<code></td>
        <td><p><strong>&quot;user&quot;</strong>. More info can be found <a href="./user.md">here</a> <a href="../system-data-types/user.md">here2</a> <a href="../../for-developers/system-data-types/user.md">here3</a> <a href="https://docs.fylr.io/for-developers/system-data-types/user">here4</a></p>
</td>
    </tr><tr>
        <td>    <code>user</code></td>
        <td><code>object<code></td>
        <td><p>This will show a short representation of <a href="https://docs.fylr.io/for-developers/system-data-types/user">user</a>.</p>
</td>
    </tr><tr>
        <td><code>versions</code></td>
        <td><code>object<code></td>
        <td><p><code>versions</code> contains a map with renditions for the file. Depending on the users permissions, not all versions might be accessible.</p>
</td>
    </tr></tbody>
    </table>