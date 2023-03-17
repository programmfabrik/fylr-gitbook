---
description: >-
  In this section you will find helpful settings if you develop plugins or
  translate the frontend, for example.
---

# Development

## Localization

Specify Google Sheets with localization that should be loaded additionally to fylr.csv. This is very helpful, when you're working on the translation of FYLR. By enabling the localization you can see your translations instead of the current released translations.

### Activated

Enable/Disable loading of additional Google Sheets.

### Google Sheet

#### Key

Copy the key of the Google Spreadsheet that should be loaded. You can find the key in the sharing url.

#### GID

Copy the GID of the sheet that should be loaded. You can find the GID in the sharing url.



## Purge

### Allow /api/settings/purge

Define if the "purge" button should be enabled/disabled in /inspect/system to reset the whole system.

### Delete files from storage locations

Define if the files should be deleted from the storage after the purge.



## Logging

Define the log level for the server, e.g. to get more or less information when developing plugins.

### Level

| OPTION | DESCRIPTION |
| ------ | ----------- |
| empty  |             |
| error  |             |
| warn   |             |
| info   |             |
| debug  |             |
| trace  |             |
