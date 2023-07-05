# How To Use As A Windows User

Collections can be used for **uploads** via the webdav protocol, so for example via a webdav client program like [Cyberduck](https://cyberduck.io/webdav/) or Windows Explorer. All uploaded files will then be linked to the collection.

With **Upload**, files will be consumed by fylr and disappear from webdav view as soon as imported. As an upside, uploading via this "**Upload**" feature is a lot faster than File System Connect.

With **File System Connect** on the other hand, while uploading is also possible, it is slower. As an upside, files will stay in the webdav view after being imported. Also, files that are already in the collection will become visible (only if they are of the one chosen Object Type). All visible files can be downloaded. That is why we also refer to FIle System Connect as "Read & Write".

## Requirements for using this

1. An administrator has to enable these features. As a Tutorial: [How To Set Up As Administrator](how-to-set-up-as-administrator.md)
2. You have to get the URL from the settings of the collection:

![](<../../.gitbook/assets/image (5).png>) right click on a collection label and choose Settings

![](<../../.gitbook/assets/image (4).png>) example of the Settings menu with the URLs

Make sure to copy the URL you need:

* "`Webdav URL (read & write)`" for **File System Connect**
* "`Hotfolder URL (Write only)`" for **Upload**



## Use with Windows Explorer

1. Open Windows Explorer (... the file manager. Do not confuse with Internet Explorer, the browser.)
2. Right-click on This PC or Network. In the menu choose Map network drive.![](<../../.gitbook/assets/image (3).png>)Screenshot, German.
3. Paste the https-URL of Upload/File Sysetm Connect you copied earlier

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption><p>Example Dialog to map network drive, in German Windows 11.</p></figcaption></figure>

## Use with Cyberduck

[Cyberduck](https://cyberduck.io/webdav/) is a free program that is a dedicated webdav client.

1. Open Cyberduck
2. Click into the Quick Access field and paste the https-URL you copied earlier (see above, Requirements)

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption><p>Cyberduck User Interface with green border to hint at where Quick Access is. German</p></figcaption></figure>

3. E.g. drag and drop files into the white space below `Dateiname` / `Filename` . Or, if you used a **File System Connect** URL, you may also download files that are in the collection. Only files _of the object type chosen_ in the collection settings will be visible.

If you used an **Upload** URL (has the world `hotfolder` in it when seen in the collection settings), the dropped files start to disappear after ca. 30 seconds. You may need to reload to see the change.

If you used a **File System Connect** URL (has the word `webdav` in it when seen in the collection settings), uploaded files stay after uploading.
