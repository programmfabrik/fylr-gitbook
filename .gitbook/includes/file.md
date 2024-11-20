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
        <td><p><strong>&quot;user&quot;</strong>. More info can be found <a href="./user.md">here</a> <a href="../system-data-types/user.md">here2</a></p>
</td>
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