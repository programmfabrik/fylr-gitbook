---
description: >-
  Lists contain records that are all on the same level. These lists can consist
  of only one field, or they can consist of multiple fields, such as first and
  last name for persons.
---

# Lists

The CSV file must contain a column header. This can be freely assigned. It is recommended to use meaningful names, as these names will be used later during the mapping. If the column headers in the CSV file correspond to the internal field names in FYLR, the field mapping is done automatically.

{% hint style="info" %}
Please also check to the [general information](../general-information.md).
{% endhint %}

## Example File "Keywords"

| KEYWORD |
| ------- |
| sun     |
| moon    |
| stars   |

## Example File "Persons"

| FIRST NAME | LAST NAME  | COMMENT                  |
| ---------- | ---------- | ------------------------ |
| Steve      | Jobs       | Co-founder of Apple Inc. |
| Bill       | Gates      | Founder of Microsoft.    |
| Mark       | Zuckerberg | Founder of Facebook Inc. |

## Import Procedure

* first **open** the CSV importer&#x20;
* **upload** the CSV file&#x20;
* select "**1st Row**" for "CSV Field Names"
* select the target **object type** and the corresponding **mask**
* switch to the "**Import Mapping**" tab and **select** the corresponding **target fields**
* switch back to the "**Import Settings**" tab and select the "**Field For Update**" if there are already entries in the list that should be updated if necessary&#x20;
* click on "**Prepare**" and you will get an overview of how many rows will be imported or updated&#x20;
* then the actual import / update can be started
