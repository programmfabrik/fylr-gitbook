---
description: >-
  Whenever a file is uploaded to fylr, preview versions are generated. This
  article describes the options for the configuration of preview versions.
---

# Preview Configuration

## Use Default Settings

If this checkbox is enabled, the default versions are used. This includes:

| FILE TYPE | VERSION | DESCRIPTION |
| --------- | ------- | ----------- |
|           |         |             |
|           |         |             |
|           |         |             |



If you want to use other versions, you have to disable the checkbox and then you'll be able to define your own set of preview versions. You can always go back to the default versions by enabling the checkbox. Your settings for the custom versions will not be overwritten, so you can also go back to your custom versions at any time.

{% hint style="warning" %}
Please note: when changing version settings, these changes are only applied for newly uploaded files, already existing preview versions are not updated automatically. You have to go to /inspect/files and start a re-sync.
{% endhint %}



## Allow Upload of Unknown File Types

Enable this checkbox, if you want to allow the upload of files with extensions not explicitly listed below. Otherwise these unknown or not supported file types are declined during the upload process.

## Max. upload file size

Set the maximum file size allowed for all uploads (for example: 500MB, 2GB). This value determines the upper limit on the size of each individual file that can be uploaded to the system. Make sure to consider user needs and system capabilities when configuring this setting.

## Extensions

For each file class (Audio, Image, Office & Video) the allowed file types can be (de-)activated. Only for activated extensions the upload is allowed and preview versions are generated. The allowed maximum file size for uploads can be set here again and overwrite the value defined above.

## Versions

All configured versions are shown in a table with their most important details. Hover over a version and click the little pencil button to edit the version settings (see below) or select a version and click the minus button on the bottom of the table to delete the version. You can add new versions by clicking on the plus button.

### Override original

If enabled, the original file won't be saved in fylr. Instead it will be replaced by the biggest version.

### Version name

Internal name of the version.

### Recipes

Recipes define the options available for generating the preview versions. Each file class brings their own recipes.

<table><thead><tr><th width="241">RECIPE</th><th width="559">DESCRIPTION</th></tr></thead><tbody><tr><td><strong>preview</strong> (audioconverter)</td><td>Creates preview images from audio files.</td></tr><tr><td><strong>convert</strong> (audioconverter)</td><td>Converts audio files into a different audio format.</td></tr><tr><td><strong>vectortosvg</strong> (imageconverter)</td><td>Converts vector files to SVG files.</td></tr><tr><td><strong>browserthumbs</strong> (imageconverter)</td><td>Converts image files.</td></tr><tr><td><strong>preview_pool_watermark</strong>  (imageconverter)</td><td>Creates preview images with watermarks.</td></tr><tr><td><strong>browserthumbs</strong> (officeconverter)</td><td></td></tr><tr><td><strong>font</strong> (officeconverter)</td><td>Creates preview images for font files.</td></tr><tr><td><strong>pdf</strong> (officeconverter)</td><td>Creates a pdf file from a document.</td></tr><tr><td><strong>preview</strong> (officeconverter)</td><td></td></tr><tr><td><strong>pdfpages</strong> (pdfconverter)</td><td>Creates preview images for all pages in a pdf file.</td></tr><tr><td><strong>resize</strong> (videoconverter)</td><td>Converts video files.</td></tr><tr><td><strong>thumbnail</strong> (videoconverter)</td><td>Creates preview images from videos.</td></tr></tbody></table>

### Extensions

Each recipe brings its own extension options. Enable all extensions you want the preview version to be generated for.&#x20;

### Recipe Configuration

Each recipe brings its own recipe options.&#x20;



<table><thead><tr><th width="139">FILE TYPE</th><th width="241">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></tbody></table>



### Version Settings

Furthermore you have the following settings for versions:

<table><thead><tr><th width="208">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Standard</td><td>If enabled, this version is used as the standard for an object type. The version is then shown in the search result for example. Please note, that "standard" needs to be enabled in the data model for the file field. </td></tr><tr><td>Rights Management</td><td>If enabled, the version can be used in the permissions for pools etc. Otherwise the version is always accessible to all users.</td></tr><tr><td>Watermark</td><td>If enabled, watermarked versions can be generated automatically and used for rights management. This needs additional configuration for the version and rights management.</td></tr><tr><td>Display Name</td><td>Name of the version that is used in fylr. Shown in the download manager for example.</td></tr><tr><td>Group</td><td>Choose a group that is used when exporting URLs to a CSV or XML file.</td></tr></tbody></table>
