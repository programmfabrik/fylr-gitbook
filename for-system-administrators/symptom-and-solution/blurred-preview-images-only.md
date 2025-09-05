---
description: If in fylr frontend, all images are only shown heavily blurred
---

# blurred preview images only

## Background knowledge

1. Blurred previews can be displayed from the SQL database without needing any access to the actual asset images or asset previews. Whenever there is a problem accessing preview images, fylr falls back to just showing the blurred previews from the tiny "blur hash" saved in SQL database.
2. In fylr, assets and previews are strongly linked to the URL. So if you change fylr's URL, only blurred previews are available. This can be remedied with a re-index, which updates the URL associated with assets and their previews.

## Possible causes:

* You changed the URL, for example http instead https or vice versa, or you changed the domain name in fylr's `externalURL` setting. This can be remedied with a re-index (which will take time)
* There is a routing or firewalling problem so that asset previews cannot be shown. This would be additionally indicated by error messages in ...&#x20;
  * in your browsers development tools (errors in "console" of "dev-tools" visibel with the `F12` key)&#x20;
  * or in error messages in the fylr log (accessible as fylr output or container output on the sysadmin level, or in https://your-fylr.example.co&#x6D;**/inspect/system/console/** (needs fylr root account access).\
