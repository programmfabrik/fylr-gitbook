# file

The system data type file stores all files used throughout the fylr system:

* Objects
* Plugins
* Logo & Background, XSLT files in the base configuration
* User picture and custom data
* Pool watermark and custom data
* Objecttype custom data

{% hint style="info" %}
Files are generally uploaded to the endpoint [**/api/eas/put**](../api/endpoints/api-eas.md). **fylr** can also upload files by copying from remote URLs when using the endpoint [**/api/eas/rput**](../api/endpoints/api-eas.md). Files can also be uploaded via **WebDAV** or by the [**/api/plugin/manage** ](../api/endpoints/api-plugin.md)for plugins with type `url`.
{% endhint %}

Files are stored in configurable locations, like **S3** or **disk** storage.

**fylr** can also manage purley **remote stored files**. In that case only the URL is stored for the file.

**fylr** runs programs to discover metadata for each file. Plugins can extend the list of programs run to find metadata.

## Fields


<table>
        <thead>
            <tr>
                <th width="300">Field</th>
                <th width="155">Format</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody><tr>
        <td><code>_id</code></td>
        <td><code>int64<code></td>
        <td><p>The <code>_id</code> is <strong>created</strong> <em>when</em> a file is uploaded into the fylr server.</p>
</td>
    </tr><tr>
        <td><code>eas_parent_id</code></td>
        <td><code>int64<code></td>
        <td><p>The <code>eas_parent_id</code> is the id of the file this file is derived from. When using <strong>/api/produce</strong>, the newly produced files will get the parent id set to the file they are produced from.</p>
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
        <td><code>upload_user</code></td>
        <td><code>object<code></td>
        <td><p>The user who uploaded this file into the system. If the upload happens via Hotfolder, the uploader is the owner of the upload collection.</p>
</td>
    </tr><tr>
        <td>    <code>_basetype</code></td>
        <td><code>string<code></td>
        <td></td>
    </tr><tr>
        <td>    <code>user</code></td>
        <td><code>object<code></td>
        <td></td>
    </tr><tr>
        <td>        <code>_generated_displayname</code></td>
        <td><code>string<code></td>
        <td><p>The generated displayname of the user. This uses <code>login</code> and <code>email</code>.</p>
</td>
    </tr><tr>
        <td>        <code>_id</code></td>
        <td><code>int64<code></td>
        <td><p>The id of the user. It is automatically assigned.</p>
</td>
    </tr></tbody>
    </table>

{% content-ref url="../types/boolean.md" %}
[boolean.md](../types/boolean.md)
{% endcontent-ref %}

# Include 1

{% include ".gitbook/includes/test1.md" %}

# Include 2

{% include "for-developers/types/boolean.md" %}
