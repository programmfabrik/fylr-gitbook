---
description: >-
  This guide provides initial orientation and contains the most frequently used
  functions in fylr.
---

# Getting Started

fylr is accessed via a web browser. Only a working internet connection and a current web browser are required. We recommend using the latest Google Chrome.

## Login

In most cases you are prompted with a login screen when accessing fylr. Simply enter your login (user name or email) and password to access fylr. Depending on your permissions, you are able to search for records (images, videos, audio or office files, ...), edit records, upload files or download and export data and much more.

Depending on the configuration, some fylr instances don't require a login to access data. You then land in the search, where you can search and view records. In some cases, you can even sign up to gain access to more data or functions.&#x20;

{% hint style="info" %}
The login screen can be individualized in the [base configuration](../for-administrators/readme/) (for example: add background image or a welcome text) or in the [messages](../for-administrators/messages.md) (for example: add terms & conditions).
{% endhint %}



## Layout

The general layout is always the same. You have a navigation on the left, followed by the quick access and the main part the search, and on the right the detail/edit view. On the top right, you have the user menu where you find your exports, user settings, and language settings.

<table><thead><tr><th width="75.66666666666666">Nr.</th><th width="168">Area</th><th>Function</th></tr></thead><tbody><tr><td>1</td><td>Menu</td><td>By clicking on the small arrow at the bottom, the menu can be opened for full display. Depending on your permissions, you can access different parts of fylr here, such as the user management, the data model or the CSV Importer.</td></tr><tr><td>2</td><td><a href="quick-access/">Quick Access</a></td><td>In the quick access you can create collection to save records for later use. Collections can also be shared with others. You find also your saved searches in the quick access.</td></tr><tr><td>3</td><td>Search</td><td>Use the fulltext search, expert search or the filter to search for records. You can change the layout of the search results or use the sorting. Click on records to view all the details and right click for more options, such as download.</td></tr><tr><td>4</td><td>Detail / Edit View</td><td>By clicking on a record in the search (or using the right click), you can display the record with a file preview and all the metadata on the right. Depending on your permissions, you can download/export/share the record or you can switch to the edit view and modify/add data.</td></tr><tr><td>5</td><td>User Menu</td><td>In the user menu you find your profile where you can also change your password, your language settings and your exports as well as additional helpful links, such as the documentation.</td></tr></tbody></table>

{% hint style="info" %}
A welcome text can be added to the search using the [messages](../for-administrators/messages.md). The layout (for example the width of panes, search result view, open/closed menu or filter) will be automatically saved in the user preferences. Use the [preferences for users](../for-administrators/permissions/groups.md#general) to set the defaults for new users.
{% endhint %}



## Search

The most space is reserved for the search, which contains the "Ressources", the fulltext search, the expert search, the filter and the search result.

The "Ressources" define the data set for your search. Think of it as folders on your computer, where you can define which folders should be included for your search. This is a great way to make a first selection of the data set that you are interested in right now.&#x20;

Then use the fulltext search to search for words, numbers or phrases. Enter one or more search terms and hit enter to start the search. fylr will search for the terms in all fields (that are included in the fulltext search) of the records. All terms will automatically be truncated on the right, meaning "house" will also find "houses", "houseboat" etc. Alternatively you can use an asterisk (\*) at the start or end of a word. To search for exact terms, wait for the autocompletion and then choose "Exact Match" or use single quotes. Put your words in quotes to search for a whole phrase (meaning the words have to be in the exact order for a match).&#x20;

Use the expert search to search for terms in specific fields or for technical data, such as filetype or file size. And as long as there are records in the search result, you can use the filter to narrow down the search.

Change layout & Sorting

Selecting



### View & Download

After finding the records you were looking for, click on one to reveal its details in the right panel.&#x20;

Use the mouse wheel or the "+" and "-" buttons in the preview to zoom images or the "play" button to start a video. Use the "expand" icon on the upper right to open the record and the file in the full view.

Depending on the setup you can open a map with the located image (the prerequisite is, that the image has the gps coordinates in their metadata).

If you have the necessary permissions, you can easily download the file by clicking on the "Download" button at the top of the detail view. Choose between the original file or automatically generated previews.&#x20;



### Export

Depending on your permissions, records can be exported as CSV, XML and JSON. Simply right click on a record or use the menu in the detail view and click on "Export". You can also select multiple records in the search and export them altogether. Exports can be scheduled and are then executed automatically (and send via email or to a FTP server).

You can access, modify and download all your exports in the user menu located at the top right.&#x20;



### Edit

When viewing the detail of a record, switch to the edit view if you wish to make changes or click on "Edit Record" in the context menu of the search. Here, you can update the metadata or change the file(s) if you have the necessary permissions. Each saving will create a new version of the record which can be accessed in the change history.



### Upload

To add new files to fylr or create new records, click on the big plus button on the top of the main menu (if you have the necessary permissions). Drag & drop or choose the files you want to upload on the left. On the right, choose the correct object type for your records and the pool you want to create them in. If you want to extract IPTC/XMP/EXIF metadata from your files, choose the appropriate metadata mapping profile (if configured). Depending on the data model, fylr can also detect versions (same filename but different filetypes) and series (same filename with an index number) and can create a single record with all files instead of a record for each file.&#x20;

Once the files have been uploaded you can navigate to the next screen and enter the metadata. Everything you enter on the template record will be written into each record that is shown below. To change/modify data for specific records, simply click on the record in the list on the left. You can also open a preview of the file on the right to zoom in. Fill out at least all mandatory fields.

When you're done, click "Save" in the lower right to create the records. These records will then be shown in the search and you can proceed with your work.



### Sharing

fylr allows users to share records with others, provided that they have been granted the necessary permissions. To share a file, select the record, and use the share option in the detail view, or create a [collection](quick-access/collections-and-presentations.md#sharing) with multiple records you want to share.



