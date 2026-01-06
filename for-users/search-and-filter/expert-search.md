# Expert Search

The **expert search** provides full control over your search by giving access to **all enabled fields**. It allows you to define precise search criteria for each field, making it possible to locate records based on very specific combinations of data. This feature is designed for advanced users who need more granular control than the standard search or filters provide.

Once you have defined your search criteria and applied the expert search, the system converts your selections into **search tokens** that are added to the **full-text search**. These tokens function just like any other search term, allowing you to combine them with additional full-text search queries.

After applying the expert search, you can **reopen the popover at any time** to add more fields. This flexibility enables iterative searching and fine-tuning of your results without starting over.

## Field Options

### All Fields

For every field in the Expert Search, you can choose to search for records that **have data** in the field or that **have no data**. This makes it possible to include or exclude records based on whether a particular field is populated.

### Hierarchical Lists

For hierarchical lists, you can choose whether you only want results that match the selected entry, or those who are connected to the subordinate entries. By default, subordinate entries are included. To only search for records that reference the chosen entry, disable the checkbox next to the field.

### Date Fields

**Date fields** are always displayed as a **date range**, allowing you to search for records within a specific range of dates. To search for a single, specific date, you must enter the same value in both the **"From"** and **"To"** fields. If only one field is filled, the search will perform an **open-ended range**, returning either all records **older than** or **newer than** the entered date, depending on which field is specified.

In addition, you can switch to **more options** to select **relative dates**, such as **"Today"**, **"In 7 days"**, or define a **custom relative range**. This feature enables quick filtering based on dynamic time frames without manually entering exact dates.

### File Fields

For **file upload fields**, several **file-specific attributes** are automatically indexed and available for searching. These attributes allow you to search not only for the presence of a file, but also for technical details, metadata, and content-related properties of the uploaded file. This makes it possible to precisely locate records based on file characteristics.

<table><thead><tr><th width="185.22265625">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><strong>Class</strong></td><td>The general category of the file (for example image, video, audio, or document). Depending on the class, different fields will be shown.</td></tr><tr><td><strong>Type</strong></td><td>The specific file type (for example JPEG, PNG, PDF, MP4). Only shows file types that have been uploaded.</td></tr><tr><td><strong>Unit</strong></td><td>The measurement unit used for technical properties, such as pixels or file sizes.</td></tr><tr><td><strong>Size</strong></td><td>The file size. This field is searchable as a <strong>range</strong>, allowing you to find files within a specific size span (for example from 1 MB to 10 MB). Leaving one boundary empty performs an open-ended range search.</td></tr><tr><td><strong>Width</strong></td><td>The width of the file. This field is searchable as a <strong>range</strong>, allowing you to find files within specific width boundaries. Leaving one boundary empty performs an open-ended range search.</td></tr><tr><td><strong>Height</strong></td><td>The height of the file. This field is searchable as a <strong>range</strong>, allowing you to find files within specific height boundaries. Leaving one boundary empty performs an open-ended range search.</td></tr><tr><td><strong>Format</strong></td><td>The orientation of the file. Possible values are <strong>Landscape</strong>, <strong>Portrait</strong>, and <strong>Square</strong>.</td></tr><tr><td><strong>Status</strong></td><td>The processing or availability status of the file.</td></tr><tr><td><strong>Filename</strong></td><td>The original name of the uploaded file.</td></tr><tr><td><strong>Date</strong></td><td>The file-related date, choose between <strong>Upload Date</strong> or <strong>Creation Date</strong>. This field is searchable as a <strong>date range</strong>. Entering only one boundary performs an open-ended range search.</td></tr><tr><td><strong>Asset ID</strong></td><td>The unique identifier assigned to the file by the system.</td></tr><tr><td><strong>Search in File</strong></td><td>Enables <strong>full-text search within the file content</strong> for supported file types.</td></tr></tbody></table>



