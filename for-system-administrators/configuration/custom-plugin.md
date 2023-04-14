# How to load your own plugin into fylr

Assuming you installed fylr via docker-compose.

1. Have a plugin folder with fylr's unix user id:
```bash
mkdir plugins
chown 1000 plugins
```

2. Connect the new folder via `docker-compose.yml`
```yaml
  fylr:
    ...
    volumes:
      - "./plugins:/fylr/files/plugins/custom"
```

3. Add the new plugin path to `fylr.yml`

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
```

