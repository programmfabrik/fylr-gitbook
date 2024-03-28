---
description: How to overwrite files that are compiled into fylr
---

# Overlay Resource



## Example 1: resource filesystem

Assume that you want to increase the timeout for re-sizing video assets form one hour to two hours.

This is done in the compiled-in file `baseconfig/fas/cookbooks/video.yml`.

### Extract original file

For a [recommended Linux installation](../for-system-administrators/installation/linux-docker-compose.md), the command would be:

```
docker exec fylr /fylr/bin/fylr resources --fs=fylr.resources --copy=video.yml baseconfig/fas/cookbooks/video.yml
```

Please be aware that, as the command does not specify the configuration file with `-c /fylr/config/fylr.yml`, fylr will start with defaults and thus not see any `resources:` setting in `fylr.yml`. So this command will extract the default file even if there is already an overlay

### Prepare replacement

Find `3600` in the file `video.yml` and and change it to `7200`.

Create the directory structure: (in `/srv/fylr`, as in the [recommended Linux installation](../for-system-administrators/installation/linux-docker-compose.md))

```
mkdir -p /srv/fylr/config/fylr/resources/baseconfig/fas/cookbooks
```

Move the file to the correct position:

```
mv video.yml /srv/fylr/config/fylr/resources/baseconfig/fas/cookbooks/
```

### Overlay

1. Configure fylr to overlay, in fylr.yml:

```
fylr+:
  resources: "/fylr/config/resources"
```

2. Restart fylr to run it with the new configuration.

### Check that overlay is being done

For a [recommended Linux installation](../for-system-administrators/installation/linux-docker-compose.md), the command would be:

```
docker-compose exec fylr /fylr/bin/fylr resources -c /fylr/config/fylr.yml --fs=fylr.resources

+--------------------------------------------------+----------+----------------------+
|                       PATH                       |   SIZE   |        SOURCE        |
+--------------------------------------------------+----------+----------------------+
...
| baseconfig/fas/cookbooks/video.yml               |   4.4 kB |              overlay |
| baseconfig/fas/cookbooks/audio.yml               |   3.0 kB |                embed |
...
```

In the `SOURCE` column, `overlay` is now shown, instead of `embed`.



Please not that in this case, the configuration file has to be specified with `-c /fylr/config/fylr.yml`, because this is the path in the fylr container. Otherwise fylr will start with defaults and thus ignore your `resources:` setting in `fylr.yml`. And it has to be specified after the `resources` command.



**To extract the overlayed file:**

```
docker exec fylr /fylr/bin/fylr resources -c /fylr/config/fylr.yml --fs=fylr.resources --copy=- baseconfig/fas/cookbooks/video.yml
```

&#x20;(... with this example command, the file contents is shown as output, and not saved anywhere, due to `--copy=-`)&#x20;



## Example 2: web filesystem

Let us assume that the file robots.txt needs to be changed:

### Extract original file

For a [recommended Linux installation](../for-system-administrators/installation/linux-docker-compose.md), the command to show this, would be:

```
docker-compose exec fylr /fylr/bin/fylr resources --fs=fylr.services.webapp.path --copy=robots.txt robots.txt
```

### Prepare the replacement

Change the extracted robots.txt.

Create the directory structure of the overlay:

```
mkdir -p /srv/fylr/config/fylr/web
```

Move the file to the correct position:

```
mv robots.txt /srv/fylr/config/fylr/web/
```

### Overlay

1. Configure fylr to overlay, in fylr.yml:

```
fylr+:
  services+:
    webapp+:
      path: "/fylr/config/web"
```

2. Restart fylr to run it with the new configuration.

##

## More info

### Command syntax

How to show the command syntax and options of your fylr version.

For a [recommended Linux installation](../for-system-administrators/installation/linux-docker-compose.md), the command to show this, would be:

```
docker-compose exec fylr /fylr/bin/fylr resources --help
```

###

### Show all resources that can be overlayed

To list all resources, let fylr give you a list of each overlay-able filesystem. Currently (fylr v6.9.3), there are two such filesystems. For a [recommended Linux installation](../for-system-administrators/installation/linux-docker-compose.md), the commands to list both, would be:

```
docker-compose exec fylr /fylr/bin/fylr resources --fs=fylr.resources

+--------------------------------------------------+----------+--------+
|                       PATH                       |   SIZE   | SOURCE |
+--------------------------------------------------+----------+--------+
| .                                                |      DIR |  embed |
| baseconfig                                       |      DIR |  embed |
| baseconfig/fas                                   |      DIR |  embed |
| baseconfig/fas/cookbooks                         |      DIR |  embed |
| baseconfig/fas/cookbooks/audio.yml               |   3.0 kB |  embed |
... ~ 400 more ...
| pages.csv                                        |  90.3 kB |  embed |
+--------------------------------------------------+----------+--------+

docker-compose exec fylr /fylr/bin/fylr resources --fs=fylr.services.webapp.path

+------------------------------------------------------+----------+--------+
|                         PATH                         |   SIZE   | SOURCE |
+------------------------------------------------------+----------+--------+
| .                                                    |      DIR |  embed |
| cui                                                  |      DIR |  embed |
| cui/cui.js                                           |   2.3 MB |  embed |
| favicon.ico                                          |   1.3 kB |  embed |
| index.html                                           |  23.7 kB |  embed |
| maintenance.html                                     |   1.8 kB |  embed |
| robots.txt                                           |     26 B |  embed |
| web                                                  |      DIR |  embed |
| web/build_info.json                                  |    202 B |  embed |
| web/css                                              |      DIR |  embed |
| web/css/ez5_debug.css                                |  42.2 kB |  embed |
| web/css/ez5_fylr.css                                 |   1.8 MB |  embed |
| web/css/ez5_mockup.css                               | 408.7 kB |  embed |
| web/css/ez5_ng.css                                   | 454.0 kB |  embed |
| web/css/ez5_print.css                                |  23.7 kB |  embed |
| web/css/font-awesome                                 |      DIR |  embed |
| web/css/font-awesome/css                             |      DIR |  embed |
| web/css/font-awesome/css/font-awesome.min.css        |  31.0 kB |  embed |
| web/css/font-awesome/fonts                           |      DIR |  embed |
| web/css/font-awesome/fonts/FontAwesome.otf           | 134.8 kB |  embed |
| web/css/font-awesome/fonts/fontawesome-webfont.eot   | 165.7 kB |  embed |
| web/css/font-awesome/fonts/fontawesome-webfont.svg   | 444.4 kB |  embed |
| web/css/font-awesome/fonts/fontawesome-webfont.ttf   | 165.5 kB |  embed |
| web/css/font-awesome/fonts/fontawesome-webfont.woff  |  98.0 kB |  embed |
| web/css/font-awesome/fonts/fontawesome-webfont.woff2 |  77.2 kB |  embed |
| web/error.html                                       |     83 B |  embed |
| web/iframe_tester.html                               |   1.0 kB |  embed |
| web/img                                              |      DIR |  embed |
| web/img/easydb-logo-150x30.png                       |   2.2 kB |  embed |
| web/img/ez5-placeholder.png                          |    296 B |  embed |
| web/js                                               |      DIR |  embed |
| web/js/easydb5.js                                    |   2.8 MB |  embed |
| web/js/easydb5_login.js                              |  78.1 kB |  embed |
| web/js/easydb5_start.js                              |  19.4 kB |  embed |
| web/js/thirdparty_all.js                             |  56.9 kB |  embed |
| web/l10n                                             |      DIR |  embed |
| web/l10n/cs-CZ.json                                  | 344.4 kB |  embed |
| web/l10n/cultures.json                               |    446 B |  embed |
| web/l10n/da-DK.json                                  | 350.4 kB |  embed |
| web/l10n/de-DE.json                                  | 364.9 kB |  embed |
| web/l10n/en-US.json                                  | 344.5 kB |  embed |
| web/l10n/es-ES.json                                  | 346.4 kB |  embed |
| web/l10n/fi-FI.json                                  | 354.4 kB |  embed |
| web/l10n/fr-FR.json                                  | 375.5 kB |  embed |
| web/l10n/it-IT.json                                  | 365.9 kB |  embed |
| web/l10n/pl-PL.json                                  | 347.9 kB |  embed |
| web/l10n/ru-RU.json                                  | 375.0 kB |  embed |
| web/l10n/sv-SE.json                                  | 351.5 kB |  embed |
| web/l10n/uz-UZ.json                                  | 348.0 kB |  embed |
| web/login.html                                       |    873 B |  embed |
| web/sso_authentication_required.html                 |    649 B |  embed |
| web/success.html                                     |     85 B |  embed |
| web/webdvd.inject.html                               |   1.3 kB |  embed |
+------------------------------------------------------+----------+--------+

```
