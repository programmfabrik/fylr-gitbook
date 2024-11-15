---
hidden: true
---

# Schema

## Settings

The settings work as follows:

### edit.mode

The mode can be

* **edit**
* **show**
* **off**

#### edit.mode\[edit]

This mode allows a field to be read and written using the API and it tells frontends to make this field visible to the user for editing.

#### edit.mode\[show]

This mode allows the field to be read using the API, it is not allowed to write that field. It tells frontends to show the field to the user.

## output

### output.detail

This setting tells frontends to show the field in the detail view.

### output.text

This setting tells frontends to show the field in the text view.

### output.table

This setting tells frontends to show the field in the table view.

### output.standard.order

The standard information is collected for this field, if the value is one of:

* 1 - The main title of the object
* 2 - A subtitle for the object
* 3 - An internal information to be used in exports

In each collection multiple fields can be collected. The data of the fields are rendered by concatenating them, as set by \*_output.standard.format_.

### output.standard.format

Examples are given for _value1_ and _value2_.

Format can be one of:

| format                | output                                    |
| --------------------- | ----------------------------------------- |
| **comma** _default_   | _value1_, _value2_                        |
| **space**             | _value1_ _value2_                         |
| **colon**             | _value1_: _value2_                        |
| **semicolon**         | _value1_; _value2_                        |
| **newline**           | <p><em>value1</em><br><em>value2</em></p> |
| **brackets**          | {_value1_}                                |
| **round-parentheses** | (_value1_)                                |
| **square-brackets**   | \[_value1_]                               |
| **dash**              | _value1_ - _value2_                       |
| **pipe**              | _value1_ \| _value2_                      |

### search.fulltext

This setting makes the data available in the **\_fulltext** search field.

### search.expert

This setting tells frontends to present the field in an expert search.

### search.nested

This setting is for nested fields only. It is a setting for the mapping of the document in Elastic. In Elastic nested documents are created, allowing the search to find exact pairings of data which would otherwise be lost, as Elastic flattens all data into a _key_-_value_ index.

## Search

The search is performed using an indexer (Elastic). All objects are rendered as documents do be stored in the index.

The documents are created per mask.

A field is rendered into the document if any of these settings are set:

* edit.mode\[edit]
* edit.mode\[show]
* output.detail
* output.text
* output.table
* output.standard.order
* search.fulltext
* search.expert
* search.facet

The same applies for nested fields.

If a field is rendered in a document, it means it is searchable using /api/search.
