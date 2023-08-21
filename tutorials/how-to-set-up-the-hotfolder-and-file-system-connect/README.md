---
description: >-
  These tutorials describe how to set up and use the Hotfolder and the File
  System Connect. (System) Administrator permissions are required for setting it
  up.
---

# Hotfolder & File System Connect

## Upload Collections

**Collections** can be used to **upload** bulks of **files**. Files can either be **dropped** on the collection in the **frontend** or in the **Hotfolder** or **File System Connect**. All files will be **imported** to FYLR and **linked** to the **collection**. Please refer to the [tutorial](setting-up-an-upload-collection.md) on how to **set up** an upload collection and to the [upload settings](../../for-users/quick-access/collections-and-presentations.md#upload-and-file-system-connect) for all **details**.



## Differences Between Hotfolder & File System Connect

**Both** the Hotfolder and the File System Connect **use** the **WebDAV** protocol and both can be used to **upload** **files**. But **only** the **File System Connect** supports **uploading**, **editing** and **downloading** files, whereas the **Hotfolder** only supports **uploading** files.&#x20;

When you only want to **upload** files into your FYLR, you **should** always **use** the **Hotfolder** as it's a lot **faster** than the File System Connect. Once you **dragged** **files** into the **Hotfolder** and they are successfully **imported**, the **files** will be **deleted** from the **WebDAV** **folder**. You may need to reload to see the change. In case an **error** occurred, the file will be **renamed** and a **text** **file** with more **details** will be created. All **uploaded** **files** can be **accessed** in FYLR **according** to the configured **permissions** and are automatically **linked** to the **collection** that was used for uploading.

With the **File System Connect** on the other hand, while uploading is also possible, it is **slower**. As an **upside**, files will **stay** in the **WebDAV folder** after being imported. Also, files that are already in the collection will be shown in the WebDAV folder. All visible files can be **downloaded** and **edited** (edited files will be updated in FYLR).

{% hint style="danger" %}
Please be **careful** with the **File System Connect**: when you **delete** a **file** from the **WebDAV folder**, it will also be **deleted** from **FYLR** and cannot be restored!
{% endhint %}



## Read More

If you are a (system) **administrator** and want to **enable** the Hotfolder and / or the File System Connect in your FYLR installation, please [continue here](preparations-before-usage.md).

If you want to **learn** how to **set up** an **upload collection**, please [continue here](setting-up-an-upload-collection.md).

If you want to **learn** how to **use** the Hotfolder or File System Connect on a **Mac** or **Windows** system, please [continue here](importing-files.md).

