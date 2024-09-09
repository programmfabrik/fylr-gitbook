---
description: How to use fylr-images in a typo3.
---

# typo3 plugin

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
6. You will now be presented with the login page of fylr. Login
7. You will be shown a fylr page marked at the top with `TPO3 file selection`.\
   Select one or more files, \
   press the `TYPO3` button,\
   click `Send`\
   ![](<../.gitbook/assets/image (13).png>)\
   \
   You can then close this window and the files appear in Typo3 `Filelist`.



