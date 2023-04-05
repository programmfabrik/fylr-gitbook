# How to load your own plugin into fylr

Assuming you installed fylr via docker-compose.

1. Connect a new folder via docker-compose.yml
{% code title="fylr.yml" %}
```yaml
fylr:
    ...
    volumes:
      - "./plugins:/fylr/files/plugins/custom"
´´´

2. Set the fylr UID on the local "plugins" folder:
```
chown 1000 plugins
´´´

3. Add a new plugin path to fylr.yml

```yaml
fylr:
[...]
  plugin:
    # load plugins at startup. the loader crawls the given directories
    # and loads given files for plugin config files, ending in ".yml".
    # "*" and "?" are allowed as placeholders, unmatched directories or
    # files are silently skipped.
    paths:
      - "/fylr/files/plugins/custom"
      - [...other directory...]
´´´

