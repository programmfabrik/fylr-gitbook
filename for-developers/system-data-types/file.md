# file

The system data type `file` stores all files used throughout the fylr system:

* Objects
* Plugins
* Logo & Background, XSLT files in the base configuration
* User picture and custom data
* Pool watermark and custom data
* Objecttype custom data

{% hint style="info" %}
Files are generally uploaded to the endpoint [**/api/eas/put**](../api/endpoints/eas/). **fylr** can also upload files by copying from remote URLs when using the endpoint [**/api/eas/rput**](../api/endpoints/eas/). Files can also be uploaded via **WebDAV** or by the [**/api/plugin/manage** ](../api/endpoints/plugin/)for plugins with type `url`.
{% endhint %}

Files are stored in configurable locations, like **S3** or **disk** storage.

**fylr** can also manage purley **remote stored files**. In that case only the URL is stored for the file.

**fylr** runs programs to discover metadata for each file. Plugins can extend the list of programs run to find metadata.

### Fields

{% include "../../.gitbook/includes/file.md" %}

### Technical Metadata

Three keys were added in **6.35.0**: `projection_type` marks 360° media (for example `equirectangular`), `alpha` is present and `true` only for a file or rendition with an alpha channel, and `vector` carries the counts of embedded images and shadings of an EPS or AI file. See [Metadata extraction](../file-worker.md#6-metadata-extraction).

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
