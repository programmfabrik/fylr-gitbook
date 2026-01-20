---
description: How to use images from fylr in a typo3.
---

# typo3 plugin

#### Requirements

Permissions in a **typo3**

* to install an extension (unless that is already done).
* to use the `Filelist` in the administrative interface.

Permissions in a **fylr instance**

* to activate a plugin (unless that is already done).
* to download the images you want to use in typo3 (see _step 6)_.

The typo3-plugin is shipped by default with each fylr instance, the plugin must be enabled before usage.

#### fylr setup

1. In the plugin manager of fylr, find the typo3 plugin,  `enable` the plugin and  `Save`.\
   ![](<../.gitbook/assets/image (9).png>)
2. In the plugin configuration, enable `Activate API` and click `Save`.\
   The configuration can be found in the plugin manager and the base config plugin section.\
   ![](<../.gitbook/assets/image (10).png>)

#### Typo3 setup

1. In your Typo3, install the extension `easydb TYPO3 integration`: [https://extensions.typo3.org/extension/easydb](https://extensions.typo3.org/extension/easydb)
2. In your Typo3 Settings, set the URL of your fylr: _(the login is done later)_\
   ![](<../.gitbook/assets/image (11).png>)

#### Usage

1. In your Typo3 `Filelist`, Click on the button `Add files from easydb`:\
   ![](<../.gitbook/assets/image (12).png>)
2. You will now be presented with the login page of fylr. Log in.
3. You will be shown a fylr page marked at the top with `TPO3 file selection`.\
   Select one or more files, click the `TYPO3` button, click `Send`\
   ![](<../.gitbook/assets/image (13).png>)\
   \
   You can then close this window and the files appear in Typo3 `Filelist`.

### Forwarding fylr metadata to typo3

* Setup a new typoo3 metadata mapping under _Administration_ > _Metadata Mapping_
* Select an Object type and provide a descriptive name for the mapping
* Map your media files fields to the typo3 metadata

## Good to know

* Changed or deleted data records in fylr are not synchronized with TYPO3. Changes to the data record must be transferred to TYPO3 manually.
* The name of the plugin may change its name from easydb to fylr.
