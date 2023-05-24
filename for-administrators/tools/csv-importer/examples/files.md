---
description: >-
  Files can also be imported via the CSV importer. If the files are already
  accessible via the web, you can simply use this URL in the CSV file.
---

# Files

If the files are located locally on your computer, they must first be made available via a web server, since web browsers do not support direct access to files on your computer.

{% hint style="info" %}
Alternatively you can upload the files using upload collections. Either upload all files first and then update the records using the CSV importer or import the data using the CSV importer first and then add the files using an upload collection.
{% endhint %}

## Preparation

In order to import files that are located in the local file system using the CSV importer, it is necessary to make them available on a local server. For example, see this list of web servers: [https://slashdot.org/software/p/Tiny-Web-Server/alternatives](https://slashdot.org/software/p/Tiny-Web-Server/alternatives).

In your CSV file you then enter the URL, e.g. http://127.0.0.1:887/my-image.png.

## Example Files

<table><thead><tr><th width="71">ID</th><th>TITLE</th><th>CREATE DATE</th><th>FILE</th></tr></thead><tbody><tr><td>1</td><td>Rome</td><td>2020-01-01</td><td><a href="https://upload.wikimedia.org/wikipedia/commons/c/c0/Rome_Montage_2017.png">https://upload.wikimedia.org/wikipedia/commons/c/c0/Rome_Montage_2017.png</a></td></tr><tr><td>2</td><td>Laptop</td><td>2007-02-01</td><td>http://127.0.0.1:887/my-image.png</td></tr></tbody></table>

If your data model allows multiple files to be uploaded per record, then enter all URLs into one cell separated by a break:

<table><thead><tr><th width="72">ID</th><th>TITLE</th><th>CREATE DATE</th><th>FILES</th></tr></thead><tbody><tr><td>1</td><td>Trevi Fountain</td><td>2020-02-17</td><td>http://127.0.0.1:8887/Trevi-001.JPG<br>http://127.0.0.1:8887/Trevi-002.JPG</td></tr></tbody></table>

If in your FYLR the object and image information are managed in separate object types (e.g. "collection objects" and "images"), please import both information separately. Create a CSV file with all information about the objects incl. unique identifier and import it. In the second CSV file, enter all information about the images including the URL to the file and the unique identifier for the associated object and import it.

## Import Procedure

* first **open** the CSV importer&#x20;
* **upload** your CSV file&#x20;
* select "**1st Row**" for "CSV Field Names"&#x20;
* select the target **object type**, **pool** and the corresponding **mask**&#x20;
* switch to the tab "**Import Mapping**" and select the corresponding **target field** for the column containing the **URLs**&#x20;
* for "**Type**" select "**url**" to import new files&#x20;
* switch back to the tab "**Import Settings**" and select the "**Update Field**" if there are already records in the list that should be updated if necessary&#x20;
* click on "**Prepare**" and you will get an overview how many rows will be imported or updated&#x20;
* then the import / update can be started
