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

Define if the "purge" button should be enabled in /inspect/system to reset the whole fylr. Note that you may need to enable this in your `fylr.yml`:

```
fylr:
  # set to true to allow /api/settings/purge. dont use on production systems!
  allowpurge: true
```

### Delete files from storage locations

Define if the files should be deleted from the storage after the purge.

## Logging

Define the log level for the server, e.g. to get more or less information when developing plugins.

### Level

Each level also includes all the more severe levels above it — `info` for example also logs `warn` and `error` messages. The levels get more verbose from top to bottom.

| OPTION | DESCRIPTION |
| ------ | ----------- |
| empty  | No level is set here. The server uses the log level from its `fylr.yml` / command-line configuration (`info` by default). Leave empty on production systems. |
| error  | Only errors — something failed and needs attention. |
| warn   | Warnings and errors, but no regular operational messages. |
| info   | Normal operational messages plus warnings and errors. This is the usual default. |
| debug  | Detailed diagnostic messages on top of `info`. Useful when developing plugins or tracking down a problem. |
| trace  | The most verbose level. Logs very fine-grained internal steps and produces a lot of output — use it only temporarily while diagnosing a specific issue. |

### Response timings

When enabled, the server additionally logs how long it took to answer requests. This is helpful when investigating slow responses, but it adds a log line per request, so leave it off in normal operation.
