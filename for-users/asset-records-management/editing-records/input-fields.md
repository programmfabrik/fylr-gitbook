---
description: This article describes the different input fields to enter or modify data.
---

# Input Fields

{% hint style="info" %}
Please note that further restrictions may have been configured for these fields (such as input length or unique constraints).
{% endhint %}



## Single-Line & Multi-Line Text Field

A **Single-Line Text Field** allows you to input a brief line of text, while a **Multi-Line Text Field** accommodates larger blocks of text (including line breaks), such as descriptions.&#x20;



## Multilingual Single-Line & Multi-Line Text Field

**Multilingual Fields** allow you to enter and manage texts in multiple languages within a single-line or multi-line text field. For each language an input field with the language code will be displayed. Click on the language code to change your language settings and hide/show more available languages.&#x20;

The available languages are defined by administrators in the [base configuration](../../../for-administrators/readme/languages.md). You can narrow these down in the language settings at the top right.



## String Field

The string field allows users to enter a single line of text. In opposite to the single-line text field, the content of the string field is only indexed as a whole, meaning it's only searchable as a whole string. This field is typically used for inventory numbers.&#x20;



## Date Field

The date field allows the input of a full date (day, month & year), just a month and year, or just a year. Alternatively to the manual input, you can choose the date from a calendar by clicking on the little calendar icon on the right of the field.



## Date Range Field

The date range field allows the input of a start and end date. Each field can accommodate a full date (day, month & year), just a month and year, or just a year. Alternatively to the manual input, you can choose the date from a calendar by clicking on the little calendar icon on the right of the field.

When entering a start date, the end date is automatically set to the same date. The end date can then be modified if needed. If one of the fields is left empty, it means it is an open range.&#x20;

Depending on the data model the date range field supports the textual input of dates. You can switch between the textual input and the field input by clicking on the text "Date Input" and "Text Input".



## Date & Time Field

The date field allows the input of a full date (day, month & year) with a time (HH:MM:SS), a full date, just a month and year, or just a year. Alternatively to the manual input, you can choose the date and time from a calendar and clock by clicking on the little calendar icon on the right of the field.



## Integer Field

The integer field accepts whole numbers without any decimal places. This type of field is ideal for inputs like counts, quantities, or any scenario where fractional values are not appropriate. You can input values manually or increase/decrease the value using the up and down arrows on the keyboard.



## Decimal Number Field

The decimal number field allows for the entry of numbers that include decimal places. This type of field is essential for inputs that require precision, such as measurements or financial data. Like the integer field, you can manually input values or use the keyboard arrows to adjust the number.



## Double Field

The double field is used to handle floating-point numbers with double precision. This type of field can store very large and very small numbers with decimal points, making it suitable for scientific calculations and high-precision financial data. Values can be entered manually or adjusted using the keyboard arrows.



## File Upload Field

The file upload field allows you to upload one or more files from your local device. This field supports various file types, depending on the [configuration](../../../for-administrators/readme/file-worker/) and [permissions](../../../for-administrators/permissions/). Each file is processed and stored according to the application's requirements. You can drag and drop files into the field or use the 3-dot-menu button to select files manually.

Once a field has been uploaded, additional options become available in the 3-dot-menu.&#x20;



## Checkbox (Boolean)

The checkbox field allows you to select or deselect an option. This field is typically used for boolean values (true/false). You can check the box to select a true value or leave it unchecked for false.



## Simple Link Field

A simple link field allows you to choose records from a list (such as persons, locations and keywords) to link to the record. You can either enter the text directly and wait for the suggestions to choose from, or you can open the whole list by clicking on the 3-dot-menu on the right of the field to access the search. There you can use the fulltext and expert search and all other search options to navigate the list and choose the record(s) you want to add by selecting it and clicking "Select".

Once a record was selected, you can change or remove this record by clicking on the 3-dot-menu again and either click on "Search" to link another record or click on "Remove" to remove the record from the field (the record will not be deleted from the list).

Depending on your permissions, you can add, modify or delete records from the list.



## Pulldowns

Pulldowns, also known as dropdown menus, provide a list of predefined options from which you can select.&#x20;



## Repeatable Fields

Repeatable fields, also called "nested fields", allow you to add multiple instances of a particular form field. This is useful for scenarios where you need to enter the same type of information multiple times, for example, adding multiple keywords, categories or persons.

If a repeatable field consists of just one field, an empty field is always shown automatically. For repeatable fields that consist of multiple fields (such as a person and a role), you can add a new row by clicking on the plus button. The trash bin icon allows you to remove a row from the record. Depending on the configuration, the entries are either sorted alphabetically or you can set your own order by using the 3-line drag handle icon in the front.



## Repeatable Fields as Popup

Usually all fields in a repeatable field are shown directly in the editor (see above). If there are many fields in a repeatable field, it might make sense to hide them in a popover. In the editor only a summary of the values is shown and the actual values can be then edited in a popover by clicking on the little pencil icon in each row. New rows can be added by clicking on "Add" at the end of the list. And existing rows can be deleted by clicking on the trash bin in each row.

The popup functionality and the fields that should appear in the summary can be configured in the mask in the data model.



## Tags

Tags help in categorizing and organizing content efficiently.  You can assign multiple tags to records, making it easier to filter and search for relevant information or to give certain users access to specific records. They are structured in groups, which define if you can assign multiple tags  (checkboxes) or just one tag (radio button) from a group to the record.

Tags are configured by administrators, so please refer to your administrator for their specific uses.



## Permissions

Permissions help in controlling who can view, edit, or delete records and usually this is defined globally by administrators. In some cases permissions can also be set directly for individual records for a fine-tuned control. For each permission you can define the user or user group and define which access they should get (by either choosing a preset or by defining the detailed permissions yourself).&#x20;

{% hint style="info" %}
Please refer to [Permissions](../../../for-administrators/permissions/) for a detailed description of the permissions.
{% endhint %}



## Plugins

Additionally to the above mentioned standard input fields, plugins can offer a different way of entering data. Please refer to the plugin documentation for each description of how to use the field.
