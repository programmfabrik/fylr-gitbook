---
description: >-
  At this point you will find an example of data preparation in CSV format for
  each data type that is available in FYLR.
---

# All Data Types

## Pools

If you only want to import records into one pool, you do not have to enter the pool in the CSV file, but simply select it in the import settings. However, if you have records that should go in different pools or if you want to change the pool for records that already exist in the system, you must add the pool in the CSV file. You can use the ID, short name or reference of the pool in the CSV file. If no pool is specified for a record in the CSV file, the pool from the import settings is used.

<table><thead><tr><th width="86.66666666666669">ID</th><th width="306">TITLE</th><th>POOL</th></tr></thead><tbody><tr><td>1</td><td>Berlin by Night</td><td>Pool A</td></tr><tr><td>2</td><td>Berliner Fernsehturm</td><td></td></tr><tr><td>3</td><td>Berliner Dom</td><td>Pool B</td></tr></tbody></table>

In the import mapping, select “\_pool” for the column containing the pool and the “ID”, “Short name” or “Reference” field, depending on what you used in your CSV file.

## Tags

If you want to import tags, please make sure, that the tags are available in your system. You can use the ID or the display name of the tags in the CSV file.

<table><thead><tr><th width="86.66666666666669">ID</th><th width="306">TITLE</th><th>TAG</th></tr></thead><tbody><tr><td>1</td><td>Berlin by Night</td><td>TAG A</td></tr><tr><td>3</td><td>Berliner Dom</td><td>TAG B</td></tr></tbody></table>

In the import mapping, select “\_tags” for the column containing the tag and the “ID” or “Display Name” field, depending on what you used in your CSV file. On the "Import Settings" tab choose, if the tags should be added to existing tags or should replace them when updating existing records.

## Single Line & Multi Line Text, Simple Text (String) <a href="#single-line--multi-line-text-simple-text-string" id="single-line--multi-line-text-simple-text-string"></a>

It is recommended to enclose the texts in double quotation marks. If a text contains a comma, semicolon, backslash, tab or a break, double quotes must be used so that they are not interpreted as column separators.

<table><thead><tr><th width="84">ID</th><th width="206">TITLE (single line text)</th><th>DESCRIPTION (multiline text)</th><th>SIGNATURE (string)</th></tr></thead><tbody><tr><td>1</td><td>Berlin by Night</td><td>The image shows the illuminated Alexanderplatz at night.</td><td>signature_2019_001</td></tr><tr><td>2</td><td>Berlin Cathedral</td><td>“The Berlin Cathedral in the midday sun.<br><br>Many people lie on the lawn in front of the Berlin Cathedral.”</td><td>SIgnature_2018_002</td></tr><tr><td>3</td><td>Berlin from above</td><td></td><td>Signature_2017_003</td></tr></tbody></table>

In the mapping, only the corresponding target fields have to be selected in each case. There are no further options.

## Single Line & Multiline Text (multilingual)

For multilingual fields, the contents for the different languages are stored internally in separate fields. Therefore, the languages must also be written in different columns in the CSV file.

<table><thead><tr><th width="88">ID</th><th>TITLE DE</th><th>TITLE EN</th><th>TITLE ES</th></tr></thead><tbody><tr><td>1</td><td>German title</td><td>English title</td><td>Título en español</td></tr><tr><td>2</td><td>Only a German title is available here</td><td></td><td></td></tr><tr><td>3</td><td>Titel in Deutsch und Englisch</td><td>Title in German and English</td><td></td></tr></tbody></table>

In the mapping, the same target field must first be selected for both columns (i.e. "TITLE"). Then the corresponding language can be selected. If a language is not displayed in the pulldown, it must first be activated by the administrator in the [base configuration](../../../readme/languages.md).

## Date, Date + Time <a href="#date-date--time" id="date-date--time"></a>

When importing dates, both the German and American formats are supported.

<table><thead><tr><th width="85.66666666666669">ID</th><th>CREATE DATE (date)</th><th>CREATE DATE (date + time)</th></tr></thead><tbody><tr><td>1</td><td>2019-12-06</td><td>2019-12-09 13:39:00</td></tr><tr><td>2</td><td>24.12.2019</td><td></td></tr><tr><td>3</td><td>2018-11</td><td>2019-12-09</td></tr><tr><td>4</td><td>2017</td><td></td></tr></tbody></table>

In the mapping, only the corresponding target fields have to be selected in each case (i.e. "CREATE DATE"). There are no further options.

## Date (Range) <a href="#date-range" id="date-range"></a>

The date range field is characterized by the fact that the values are stored internally in two fields. There is a “from” and “to” field. Therefore, the start and end date must also be written in two columns in the CSV file. Again, the German as well as the American format are accepted.

<table><thead><tr><th width="80.66666666666669">ID</th><th>DATE FROM</th><th>DATE TO</th></tr></thead><tbody><tr><td>1</td><td>2019-10-01</td><td>2019-10-08</td></tr><tr><td>2</td><td>2016-01</td><td>2018-12</td></tr><tr><td>3</td><td>2009</td><td>2019-12-31</td></tr></tbody></table>

In the mapping, the same target field must first be selected for both columns. Then it can be selected whether the data should be written in “from” or “to”.

## Number (integer), Decimal Number (2 digits), Double <a href="#number-integer-decimal-number-2-digits" id="number-integer-decimal-number-2-digits"></a>

When importing decimal numbers, both the period and the comma are supported. Thousands separators (point or comma) may not be used currently.

<table><thead><tr><th width="75.66666666666669">ID</th><th>NUMBER (number)</th><th>VALUE (decimal number)</th></tr></thead><tbody><tr><td>1</td><td>1</td><td>1.40</td></tr><tr><td>2</td><td>2</td><td>5,80</td></tr><tr><td>3</td><td>3</td><td>35</td></tr></tbody></table>

In the mapping, only the corresponding target fields have to be selected in each case. There are no further options.

## Yes/No Field (Boolean) <a href="#yesno-field-boolean" id="yesno-field-boolean"></a>

Fields of type “Yes/No field (Boolean)” are displayed as checkbox in the FYLR frontend. The two states “enabled” and “disabled” can be set by “true” or “1” and “false” or “0” during import. Empty fields in the CSV correspond to “false”.

<table><thead><tr><th width="76.5">ID</th><th>VALUE</th></tr></thead><tbody><tr><td>1</td><td>true</td></tr><tr><td>2</td><td>false</td></tr><tr><td>3</td><td></td></tr></tbody></table>

Only the corresponding target field has to be selected in the mapping. There are no further options.

## Simple Linking to Flat Lists <a href="#simple-linking-with-flat-list" id="simple-linking-with-flat-list"></a>

If a field connects to a list, these links can also be imported via CSV. The record you want to link can, but does not have to exist in the list in FYLR.

<table><thead><tr><th width="72.5">ID</th><th>CATEGORY</th></tr></thead><tbody><tr><td>1</td><td>Persons</td></tr><tr><td>2</td><td>Buildings</td></tr><tr><td>3</td><td>Events</td></tr></tbody></table>

In the mapping, first select the corresponding target field. Then select the field from the linked object type. FYLR uses this field to check whether the record already exists in the list. If yes, the existing record will be linked. If not, a new record will be created in the list and linked (provided that the checkbox “Create Linked Records” is activated on the “Import Settings” tab during CSV import).

## Simple Linking to Hierarchical Lists <a href="#simple-linking-with-hierarchical-list" id="simple-linking-with-hierarchical-list"></a>

If a field connects to a hierarchical list, these links can also be imported via CSV. The record you want to link can, but does not have to exist in the list in FYLR.

<table><thead><tr><th width="91.5">ID</th><th>LOCATION</th></tr></thead><tbody><tr><td>1</td><td>Germany > Berlin</td></tr><tr><td>2</td><td>Ireland > Dublin</td></tr><tr><td>3</td><td>United Kingdom > Scotland > Glasgow</td></tr></tbody></table>

In the mapping, first select the corresponding target field. Then select the field from the linked object type. FYLR uses this field to check whether the record already exists in the list. If yes, the existing record will be linked. If not, a new record will be created in the list and linked (provided that the checkbox “Create Linked Records” is activated on the “Import Settings” tab during CSV import). When importing hierarchical lists, the separator used can be selected (">" or “/”) to build a hierarchy.

## Repeatable Text Fields <a href="#repeatable-free-text-field" id="repeatable-free-text-field"></a>

If the target field is a so-called nested field (i.e. several entries can be made per record), all records in the CSV file must be written in one cell and separated with a break. Use double quotes to import texts that contain a break.

<table><thead><tr><th width="69.5">ID</th><th>REPEATABLE TEXT</th></tr></thead><tbody><tr><td>1</td><td>First text<br>Second text<br>Third text</td></tr><tr><td>2</td><td>“Text that contains a break.<br>Continued after the break."<br>“Text without a break, but with a comma.”</td></tr></tbody></table>

Only the corresponding target field has to be selected in the mapping. There are no further options.

{% hint style="info" %}
Alternatively, each entry of the repeatable field can also be written into a separate column. When importing, however, it should be noted that this must be done in several stages, since the target field may only ever be selected once during mapping. In the first run, the first column is mapped and imported. In the second run, only the second, etc. It is important that in this case the option “Append Nested Fields” is activated under “Import Settings”, so that the entries in the multiple field are added and not overwritten each time.
{% endhint %}

## Nested Fields <a href="#nested-fields" id="nested-fields"></a>

If the target field is a so-called nested field in which another object type is referenced, all records to be linked in the CSV file must be written in one cell and separated with a break. Use double quotes to import entries that contain a break or separator.

<table><thead><tr><th width="83.5">ID</th><th>KEYWORDS</th></tr></thead><tbody><tr><td>1</td><td>Sun<br>Moon<br>Stars</td></tr><tr><td>2</td><td>“City, Country, River Game”<br>“Children’s Games”</td></tr></tbody></table>

This works even if the linked object type is hierarchical:

<table><thead><tr><th width="87.5">ID</th><th>FORMER LOCATIONS</th></tr></thead><tbody><tr><td>1</td><td>Germany > Berlin<br>Ireland > Dublin<br>United Kingdom > Scotland > Glasgow</td></tr></tbody></table>

In the mapping, first select the corresponding target field. Then select the field from the linked object type. FYLR uses this field to check whether the record already exists in the list. If yes, the existing record will be linked. If not, a new record will be created in the list and linked (provided that the checkbox “Create Linked Records” is activated on the “Import Settings” tab during CSV import). When importing hierarchical lists, the separator used can still be selected (">” or “/”) to build a hierarchy.

{% hint style="info" %}
Alternatively, each entry of the repeatable field can also be written into a separate column. When importing, however, it should be noted that this must be done in several stages, since the target field may only ever be selected once during mapping. In the first run, the first column is mapped and imported. In the second run, only the second, etc. It is important that in this case the option “Append Nested Fields” is activated under “Import Settings”, so that the entries in the multiple field are added and not overwritten each time.
{% endhint %}

## Nested Fields with Multiple Fields <a href="#nested-field-with-multiple-fields" id="nested-field-with-multiple-fields"></a>

If the target field is a so-called nested field, which contains more than one field, these fields must be divided into individual columns. If more than one record is to be linked to a record, these must again be entered in a cell and separated by a break.

<table><thead><tr><th width="65.66666666666669">ID</th><th>OTHER IDS</th><th>ID TYPES</th></tr></thead><tbody><tr><td>1</td><td>IDA123<br>ID1XYZ<br>IDA1B2C3</td><td>Altsystem XY<br><br>Portal XY</td></tr></tbody></table>

{% hint style="info" %}
Alternatively, each record of the repeatable field can also be written into its own column. In our example, there would be a total of 6 columns for the three entries (“OTHER ID 1”, “OTHER ID 1 TYPE”, “OTHER ID 2”, “OTHER ID 2 TYPE”, “OTHER ID 3”, “OTHER ID 3 TYPE”). When importing, however, it should be noted that this must be done in multiple steps, since you may only ever select the target field once during the mapping. So in the first run you map and import the first two columns. In the second run, only the third and fourth, etc. It is important that in this case the option “Append Nested Records” is activated under “Import settings”, so that the entries in the multiple field are supplemented and not overwritten each time.
{% endhint %}

## Files

The import of files is explained in the [examples](files.md).

## Plugins

To import content into Custom Data Fields, it is best to first manually create a record in FYLR and export it as CSV. There you can have a look at the structure of the content. This varies depending on the plugin. Sometimes not all information is needed for the import, but can be added automatically by the Custom-Data-Updater. You can find more information at the respective [Plugins](https://github.com/programmfabrik).

The following information is sufficient for the GND custom data type:

{% code overflow="wrap" lineNumbers="true" %}
```json
{
  "conceptURI": "http://d-nb.info/gnd/118868284",
  "conceptName": "Jobs, Steve  (1955 - 2011)"
}
```
{% endcode %}

The following information is sufficient for the GVK custom data type:

{% code overflow="wrap" lineNumbers="true" %}
```json
{
  "conceptURI": "http://uri.gbv.de/document/gvk:ppn:1039947670",
  "conceptName": "K. Lynch, „Steve Jobs“. Harvard Common Press, Minneapolis, 2018."
}
```
{% endcode %}

Only the corresponding target field has to be selected in the mapping. There are no further options.<br>
