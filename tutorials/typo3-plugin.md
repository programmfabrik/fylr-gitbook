---
description: How to use images from fylr in a TYPO3.
---

# TYPO3 plugin

#### Requirements to setup

Full access to a **TYPO3 instance**

* to install the extension
* to use the `Filelist` in the administrative interface

Permissions in a **fylr instance**

* to enable plugins (required system right: _"Access plugin manager"_)
* to download the images you want to use in TYPO3 (required during [#usage](typo3-plugin.md#usage "mention"))

The TYPO3 plugin is shipped by default with each fylr instance, the plugin must be enabled before usage.

#### fylr setup

1. In the plugin manager of fylr, find the TYPO3 plugin,  `enable` the plugin and  `Save`.\
   ![](<../.gitbook/assets/image (9).png>)
2. In the plugin configuration, enable `Activate API` and click `Save`.\
   The configuration can be found in the plugin manager and the base config plugin section.\
   ![](<../.gitbook/assets/image (10).png>)
   1. _Optional_: Setup a metadata mapping to be applied when loading fylr content into TYPO3, see also [#forward-fylr-metadata-to-typo3](typo3-plugin.md#forward-fylr-metadata-to-typo3 "mention")

#### Typo3 setup

1. install the extension `easydb TYPO3 integration`: [https://extensions.typo3.org/extension/easydb](https://extensions.typo3.org/extension/easydb)
2. in the extension configuration set the URL of your fylr instance _(the login is done later)_\
   ![](<../.gitbook/assets/image (11).png>)

#### Usage

1. In the  `Filelist`, Click on the button `Add files from easydb`:\
   ![](<../.gitbook/assets/image (12).png>)
2. You will now be presented with the login page of fylr. Log in.
3. You will be shown a fylr page marked at the top with `TPO3 file selection`.\
   Select one or more files, click the `TYPO3` button, click `Send`\
   ![](<../.gitbook/assets/image (13).png>)\
   \
   You can then close this window and the files appear in the `Filelist`.

### Forward fylr metadata to TYPO3

* Setup a new TYPO3 metadata mapping in _Administration_ > _Metadata Mapping_ > TYPO3 _Metadata_
* Select an Object type and provide a descriptive name for the mapping
* Map your media files fields to the TYPO3 metadata
* Set your mapping in the plugin manager. See a) in [#fylr-setup](typo3-plugin.md#fylr-setup "mention")

## Good to know

* Changed or deleted data records in fylr are not synchronized with TYPO3. Changes to the data record must be transferred to TYPO3 manually.
* The name of the plugin may change its name from easydb to fylr.
