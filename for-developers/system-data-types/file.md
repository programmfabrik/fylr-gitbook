# file

The system data type `file` stores all files used throughout the fylr system:

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

### Fields

{% include "../../.gitbook/includes/file.md" %}

### Technical Metadata

{% include "../../.gitbook/includes/technical_metadata.md" %}

### File Versions

{% include "../../.gitbook/includes/file_version.md" %}





|      |   |                                             |
| ---- | - | ------------------------------------------- |
| Henk |   | <p>Horst<br>s3ioj<br>osqjwo<br>ijojsqwi</p> |
|      |   |                                             |
|      |   |                                             |
|      |   |                                             |
|      |   |                                             |
