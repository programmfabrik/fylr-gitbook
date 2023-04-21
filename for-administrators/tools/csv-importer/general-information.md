# General Information

The CSV file must be **UTF-8** or **UTF-16** encoded (otherwise Umlaute and special characters will not be imported correctly).

**Comma**, **semicolon** or **tabulator** can be used as column **separator** (detection is done automatically by FYLR).

Texts containing **commas, semicolons, tabs** or breaks must be **enclosed** by double or single **quotes** (detection is done by FYLR automatically).

The CSV has to contain **column headers**. They can be freely chosen (mapping of source and target fields must then be done manually, see options).

If you use the **internal FYLR field names** as column headers in the CSV file, the **mapping** is done **automatically** (to get the internal FYLR field names it is best to download a record as CSV  first and copy the column headers).

If possible always use a **unique identifier**, because only this identifier can be used to **update** existing datasets later on.

When importing **quotes**, please note the following:

| TEXT TO BE IMPORTED                                                         | TEXT IN THE CSV FILE                                                              |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| "Plain text enclosed in quotes to be imported."                             | """Plain text enclosed in quotes to be imported."""                               |
| Simple text that contains "quotation marks".                                | "Simple text that contains ""quotation marks""."                                  |
| "Plain text in quotation marks, but which also contains "quotation marks"." | """Plain text in quotation marks, but which also contains ""quotation marks"".""" |
| "This is a quote." said Person Z.                                           | """This is a quote."" said Person Z."                                             |
| Person Z said "This quote."                                                 | "Person Z said ""This quote."""                                                   |

