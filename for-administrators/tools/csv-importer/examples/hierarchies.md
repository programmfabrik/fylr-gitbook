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

| ID | LEVEL 1        | LEVEL 2     | LEVEL 3    |
| -- | -------------- | ----------- | ---------- |
| 1  | Germany        |             |            |
| 2  |                | Berlin      |            |
| 3  |                | Brandenburg |            |
| 4  |                |             | Potsdam    |
| 5  | United Kingdom |             |            |
| 6  |                | Scotland    |            |
| 7  |                |             | Glasgow    |
| 8  |                | England     |            |
| 9  |                |             | London     |
| 10 |                |             | Brighton   |
| 11 |                |             | Manchester |

Alternatively, the data can also be structured as follows. However, it is important that each level appears in its own row in the CSV file (lines 1, 3, 5, 6, 8 must not be omitted):

| ID | LEVEL 1        | LEVEL 2     | LEVEL 3    |
| -- | -------------- | ----------- | ---------- |
| 1  | Germany        |             |            |
| 2  | Germany        | Berlin      |            |
| 3  | Germany        | Brandenburg |            |
| 4  | Germany        | Brandenburg | Potsdam    |
| 5  | United Kingdom |             |            |
| 6  | United Kingdom | Scotland    |            |
| 7  | United Kingdom | Scotland    | Glasgow    |
| 8  | United Kingdom | England     |            |
| 9  | United Kingdom | England     | London     |
| 10 | United Kingdom | England     | Brighton   |
| 11 | United Kingdom | England     | Manchester |

In addition, it is possible to import the hierarchies as follows. However, it is important that each level appears in its own line in the CSV file (lines 1, 3, 5, 6, 8 must not be omitted):



| ID | PARENT RECORD  | NAME           |
| -- | -------------- | -------------- |
| 1  |                | Germany        |
| 2  | Germany        | Berlin         |
| 3  | Germany        | Brandenburg    |
| 4  | Brandenburg    | Potsdam        |
| 5  |                | United Kingdom |
| 6  | United Kingdom | Scotland       |
| 7  | Scotland       | Glasgow        |
| 8  | United Kingdom | England        |
| 9  | England        | London         |
| 10 | England        | Brighton       |
| 11 | England        | Manchester     |

In the import mapping, the field "id\_parent" must be selected for the column "PARENT RECORD" and the corresponding field for the column "NAME". If your file contains parent records that are not yet available in your database, you have to perform the import twice. In the first step all records are created and in the second import run the links between parent and new child records are created. In that case it is required that in the import settings the "Field for Updates" was selected over which the matching should take place (in our example e.g. "ID").

{% hint style="info" %}
If you want to export a hierarchical list from FYLR and import it afterwards, you have to select "Hierarchies as Columns" when exporting.
{% endhint %}

## Example File "Categories"

| ID | LEVEL 1   | LEVEL 2     | COMMENT                                                                                                  |
| -- | --------- | ----------- | -------------------------------------------------------------------------------------------------------- |
| 1  | Persons   |             | This category includes, for example, employee photos or photos of events.                                |
| 2  | Buildings |             |                                                                                                          |
| 3  |           | Building #1 | This building was the former seat of the department XYZ. Currently, the department ABC is located there. |
| 4  |           | Building #2 | The building was built in 1986.                                                                          |

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
