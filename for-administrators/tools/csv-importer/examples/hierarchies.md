---
description: >-
  Hierarchical lists contain records that can have parent and child records.
  These hierarchical lists can consist of only one field, or of several fields.
---

# Hierarchies

The CSV file must contain a column header. This can be freely assigned. It is recommended to use meaningful names, as these names will be used later during the mapping. If the column headers in the CSV file correspond to the internal field names in FYLR, the field mapping is done automatically.

{% hint style="info" %}
Please also check to the [general information](../general-information.md).
{% endhint %}

## Example Files "Locations"

<table><thead><tr><th width="75">ID</th><th>LEVEL 1</th><th>LEVEL 2</th><th>LEVEL 3</th></tr></thead><tbody><tr><td>1</td><td>Germany</td><td></td><td></td></tr><tr><td>2</td><td></td><td>Berlin</td><td></td></tr><tr><td>3</td><td></td><td>Brandenburg</td><td></td></tr><tr><td>4</td><td></td><td></td><td>Potsdam</td></tr><tr><td>5</td><td>United Kingdom</td><td></td><td></td></tr><tr><td>6</td><td></td><td>Scotland</td><td></td></tr><tr><td>7</td><td></td><td></td><td>Glasgow</td></tr><tr><td>8</td><td></td><td>England</td><td></td></tr><tr><td>9</td><td></td><td></td><td>London</td></tr><tr><td>10</td><td></td><td></td><td>Brighton</td></tr><tr><td>11</td><td></td><td></td><td>Manchester</td></tr></tbody></table>

Alternatively, the data can also be structured as follows. However, it is important that each level appears in its own row in the CSV file (lines 1, 3, 5, 6, 8 must not be omitted):

<table><thead><tr><th width="73">ID</th><th>LEVEL 1</th><th>LEVEL 2</th><th>LEVEL 3</th></tr></thead><tbody><tr><td>1</td><td>Germany</td><td></td><td></td></tr><tr><td>2</td><td>Germany</td><td>Berlin</td><td></td></tr><tr><td>3</td><td>Germany</td><td>Brandenburg</td><td></td></tr><tr><td>4</td><td>Germany</td><td>Brandenburg</td><td>Potsdam</td></tr><tr><td>5</td><td>United Kingdom</td><td></td><td></td></tr><tr><td>6</td><td>United Kingdom</td><td>Scotland</td><td></td></tr><tr><td>7</td><td>United Kingdom</td><td>Scotland</td><td>Glasgow</td></tr><tr><td>8</td><td>United Kingdom</td><td>England</td><td></td></tr><tr><td>9</td><td>United Kingdom</td><td>England</td><td>London</td></tr><tr><td>10</td><td>United Kingdom</td><td>England</td><td>Brighton</td></tr><tr><td>11</td><td>United Kingdom</td><td>England</td><td>Manchester</td></tr></tbody></table>

In addition, it is possible to import the hierarchies as follows. However, it is important that each level appears in its own line in the CSV file (lines 1, 3, 5, 6, 8 must not be omitted):



<table><thead><tr><th width="83.66666666666669">ID</th><th>PARENT RECORD</th><th>NAME</th></tr></thead><tbody><tr><td>1</td><td></td><td>Germany</td></tr><tr><td>2</td><td>Germany</td><td>Berlin</td></tr><tr><td>3</td><td>Germany</td><td>Brandenburg</td></tr><tr><td>4</td><td>Brandenburg</td><td>Potsdam</td></tr><tr><td>5</td><td></td><td>United Kingdom</td></tr><tr><td>6</td><td>United Kingdom</td><td>Scotland</td></tr><tr><td>7</td><td>Scotland</td><td>Glasgow</td></tr><tr><td>8</td><td>United Kingdom</td><td>England</td></tr><tr><td>9</td><td>England</td><td>London</td></tr><tr><td>10</td><td>England</td><td>Brighton</td></tr><tr><td>11</td><td>England</td><td>Manchester</td></tr></tbody></table>

In the import mapping, the field "id\_parent" must be selected for the column "PARENT RECORD" and the corresponding field for the column "NAME". If your file contains parent records that are not yet available in your database, you have to perform the import twice. In the first step all records are created and in the second import run the links between parent and new child records are created. In that case it is required that in the import settings the "Field for Updates" was selected over which the matching should take place (in our example e.g. "ID").

{% hint style="info" %}
If you want to export a hierarchical list from FYLR and import it afterwards, you have to select "Hierarchies as Columns" when exporting.
{% endhint %}

## Example File "Categories"

<table><thead><tr><th width="61">ID</th><th>LEVEL 1</th><th>LEVEL 2</th><th>COMMENT</th></tr></thead><tbody><tr><td>1</td><td>Persons</td><td></td><td>This category includes, for example, employee photos or photos of events.</td></tr><tr><td>2</td><td>Buildings</td><td></td><td></td></tr><tr><td>3</td><td></td><td>Building #1</td><td>This building was the former seat of the department XYZ. Currently, the department ABC is located there.</td></tr><tr><td>4</td><td></td><td>Building #2</td><td>The building was built in 1986.</td></tr></tbody></table>

## Import Procedure

* first **open** the CSV importer&#x20;
* **upload** your CSV file&#x20;
* select "**1st Row**" for "CSV Field Names"
* select the target **object type** and the corresponding **mask**&#x20;
* switch to the tab "**Import Mapping**" and select the same **target field** for each column containing hierarchical data and enter the **level number** (attention: the first level must start with 0)&#x20;
* &#x20;for all other **columns** in the CSV also select the corresponding **target fields** (e.g. for "Comment")&#x20;
* switch back to the "**Import Settings**" tab and select the "**Update Field**" if there are already records in the list that should be updated if necessary&#x20;
* click on "**Prepare**" and you will get an overview of how many rows will be imported or updated&#x20;
* then the actual import / update can be started
