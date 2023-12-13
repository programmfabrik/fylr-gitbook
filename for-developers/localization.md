---
description: >-
  The fylr frontend can be used in multiple languages. Therefor in the code are
  only keys used and the translations are stored in different Google Sheets.
---

# Localization

## How to work on translations / keys

Programmfabrik provides the German and English translations. Other languages were provided by our partners or external translators who got write access to the following files.&#x20;

## Files

### [easydb l10n master](https://docs.google.com/spreadsheets/d/1glXObMmIUd0uXxdFdiPWRZPLCx6qEUaxDfNnmttave4/edit#gid=1441851860)

This Google Sheet contains the main translations as well as translations for our plugins (that are not Open Source).

### [easydb l10n github public master](https://docs.google.com/spreadsheets/d/1Z3UPJ6XqLBp-P8SUf-ewq4osNJ3iZWKJB83tc6Wrfn0/edit#gid=480475519)

This Google Sheet contains all translations for all Open Source plugins that were developed by us or our partners or customers.

### [fylr localization](https://docs.google.com/spreadsheets/d/1L0TusEEmerNqAW8k6w3893kcYjjpDi3OSoeKsOaPB4U/edit#gid=0)

This Google Sheet contains all translations for the fylr server part.

## Important / Hints

* Headers must not be deleted
* Columns that are not related to a language should not be added
* Do not translate anything inside "**%(...)"**
* Do not leave empty spaces between rows
* You can use markdown syntax in some places, i.e. to make text bold
* If you remove a translation from the Google Sheet or leave it empty, the key will be shown in the frontend instead
* If you don’t want the text / key to be shown in the frontend just enter "-" instead of leaving the cell empty

## New keys and modified translations

If a new key is added to the Google Sheet, the checkboxes in the columns “R” (for “Review”) are set to indicate that the translation in this language needs to be checked. The German and English translations are checked by Programmfabrik. Once the translation was added/modified, the checkbox "R" has to be disabled.

## Add new languages

New frontend languages in fylr can only be added by Programmfabrik. Please create a ticket if you need a new frontend language. Data languages can be added in the [base configuration](../for-administrators/readme/languages.md#data-languages).

## Find the right keys

If you can’t find the text you want to change in the Google Sheet, open a fylr instance and open the debug menu (STRG+CTRL+D or CONTROL+OPTION+D) and enable “Show localization keys”. Instead of the translations you see the keys now. For small buttons, you might have to use the browser developer tools and inspect the html and look for “ez5-loca-key”.

## Release

New translations will be included in the general fylr release. Some translations are already visible after a frontend reload or an automatic plugin update:

* Add the Google Sheet ID & GID to the [base configuration](../for-administrators/readme/development.md#localization) to see your changes after re-loading the frontend (applies only to [web-frontend-localization](https://docs.google.com/spreadsheets/d/1glXObMmIUd0uXxdFdiPWRZPLCx6qEUaxDfNnmttave4/edit#gid=1441851860) and [Server](https://docs.google.com/spreadsheets/d/1L0TusEEmerNqAW8k6w3893kcYjjpDi3OSoeKsOaPB4U/edit#gid=0))
* Translations for plugins are updated according to the update settings for each plugin in the [plugin manager](../for-administrators/plugin-manager.md). After a plugin update, a reload of the frontend is required.
