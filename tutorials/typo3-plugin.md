---
description: How to use images from fylr in a typo3.
---

# typo3 plugin

To do the following steps, you need:

* Enough access in a typo3 to install an extension (unless that is already done).
* Enough access in a typo3 to use the `Filelist` in the administrative interface.
* Enough access in a fylr to activate a plugin (unless that is already done).
* Enough access in a fylr to download the images you want to use in typo3 _for step 6_.



The typo3-plugin for fylr is shipped with fylr, but it is disabled by default.

1. In the plugin manager of fylr, search for typo and `enable` the plugin and click `Save`.\
   ![](<../.gitbook/assets/image (9).png>)
2. In the frontend configuration of the plugin, check `Activate API` and click `Save`.\
   Currently, this frontend configuration is in the `Base Configuration`, but we plan to move it to the `Plugin Manager`.\
   ![](<../.gitbook/assets/image (10).png>)
3. In your Typo3, install the extension `easydb TYPO3 integration`: [https://extensions.typo3.org/extension/easydb](https://extensions.typo3.org/extension/easydb)
4. In your Typo3 Settings, set the URL of your fylr:   _(the login is done later)_\
   ![](<../.gitbook/assets/image (11).png>)
5. In your Typo3 `Filelist`, Click on the button `Add files from easydb`:\
   ![](<../.gitbook/assets/image (12).png>)
6. You will now be presented with the login page of fylr. Log in.
7. You will be shown a fylr page marked at the top with `TPO3 file selection`.\
   Select one or more files, \
   press the `TYPO3` button,\
   click `Send`\
   ![](<../.gitbook/assets/image (13).png>)\
   \
   You can then close this window and the files appear in Typo3 `Filelist`.

## Good to know

* Changed or deleted data records in fylr are not synchronized with TYPO3. Changes to the data record must be transferred to TYPO3 manually.
* The name of the plugin may change its name from easydb to fylr.



