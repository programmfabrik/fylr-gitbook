---
description: This article describes the workflow of how records can be deleted.
---

# Deleting Records

{% hint style="info" %}
Deleting records in fylr requires that the user has the necessary permissions. If you do not have the appropriate permissions, you will not be able to delete records. Please contact your system administrator if you need access.
{% endhint %}

{% hint style="danger" %}
Deleting records is a permanent action. Once a record is deleted, it cannot be recovered.
{% endhint %}

## **Deleting a Single Record**

Use the search functionality to locate the record you wish to delete. You can use various filters and search terms to find the specific record.

Once you have located the desired record in the search results, click on the record and enter the edit mode.

In the editor, open the 3-dot-menu in the upper right and click "Delete". Confirm the deletion when prompted. The record will be permanently deleted from the system.

## **Deleting Multiple Records**

Use the search functionality to locate the records you wish to delete. You can refine your search to include all the records you want to remove.&#x20;

In the search results, select the records you wish to delete. This can be done by using the lasso to select multiple records, by holding CTRL/COMMAND and clicking on the records or by using the "Select Page" / "Select All" options in the 3-dot-menu of the search.

Once you have selected the desired records, right-click on the selected records and click on "Delete Records" or enter the group mode by choosing "Group Editor". This mode allows you to perform actions on multiple records simultaneously. In the group editor, you find the "Delete" button in the lower right. Please note that users additionally need the system right "Batch Delete" to see these buttons.

Confirm the deletion when prompted. All selected records will be permanently deleted from the system.

{% hint style="danger" %}
Use caution when deleting multiple records at once to avoid accidental loss of important data.
{% endhint %}

## Deleting Referenced Records

If you delete a record that is referenced by another record (for example a keyword that is linked in an image record), you will receive a message and have to decide what you want to do.

You can delete the record and let fylr remove all references in the other records automatically (if the data model allows that). Please note, that if there is a NOT NULL Constraint on the field, this option will be disabled and the record cannot be deleted. You will have to fix this problem manually by searching for these records and linking a different record first. When all references are removed, you will be able to delete the record.

If you are trying to delete a record from a hierarchical object type that has subordinate records, you can also choose the option to delete the record and delete all subordinate records.

You can also abort the deletion by either clicking on the "X" in the upper right, or you can let fylr create a collection with all records that prevent the deletion. The collection can be found in the quick access. It's named "Deletion \<date & time of the creation>". The record(s) that were tried to be deleted are linked in the top level collection.

The records that prevent the deletion are linked in the following collections:

<table><thead><tr><th width="244">COLLECTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></tbody></table>

