# Downloading

## General Info

The **download functionality** in fylr allows users to retrieve files from records in different contexts, including **single records**, **selections**, and **entire collections**. All downloads follow the configured **rights management rules**, ensuring that users can only download files and renditions they are authorized to access. Downloads may include the original file, one or more renditions, metadata, and file variants, depending on system configuration and user permissions. The file is then downloaded to your device according to the selected settings.

{% hint style="info" %}
Users need the system right "Download" and "Download Versions" to be able to download files.
{% endhint %}

## Download Options

When downloading, users can configure several **download options**. These options apply consistently whether downloading a single file, a selection of files, or an entire collection.

<table><thead><tr><th width="188.7734375">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Renditions</td><td>All files are grouped in file classes. Select which <strong>rendition(s)</strong> should be downloaded, such as the original file or a specific preview or watermarked version. Only those with appropriate <strong>download permissions</strong> are shown.</td></tr><tr><td>Metadata Mapping</td><td>Choose between <strong>Default</strong>, which applies the metadata mapping configured by the administrator, <strong>Unchanged</strong>, which downloads the file with its original embedded metadata, <strong>Delete</strong>, which removes metadata from the file, or a <strong>specific metadata mapping</strong>.</td></tr><tr><td>File Name</td><td>For <strong>file naming</strong>, choose between the <strong>standard template</strong> configured by the administrator, the <strong>original file name</strong>, or enter a <strong>custom static text</strong>.</td></tr><tr><td>Download as ZIP</td><td>When downloading multiple files, choose to <strong>download the files as a ZIP archive</strong>, which bundles all files into a single compressed file.</td></tr><tr><td>Include File Variants</td><td>If records contain <strong>file variants</strong>, decide whether these variants should be included in the download.</td></tr></tbody></table>



## Downloading of Single Files

Single files can be downloaded directly from a record, for example from search results (right click on a record), a collection view, or the detail view. The download action opens the download options, allowing you to select the desired rendition, metadata profile, and file name before starting the download.&#x20;

## Downloading of Selections

To download multiple files at once, you can create a **selection** in search results or within a collection by using the lasso or CMD+Click. After selecting the desired records, the download action opens the same download options available for single files.

## Downloading of Collections

Downloading a collection allows you to retrieve **all accessible files** contained in that collection. The download can be initiated from the collection detail and uses the same set of download options as other download types. Only files and renditions you are authorized to access are included.

## Download Message and User Confirmation

fylr supports displaying a **custom message before downloading** for specific users or user groups. This message appears as part of the download process and must be acknowledged before the download can proceed. It can be used to display **copyright notices**, **license terms**, or to ask users to **confirm the intended use** of the downloaded files. This can be configured in the "[Messages](../../for-administrators/messages.md)".



