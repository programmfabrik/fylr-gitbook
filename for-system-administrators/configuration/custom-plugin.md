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
    # load plugins at startup. each entry is a literal directory, searched
    # recursively for "manifest.yml" files — one plugin per manifest.
    # a directory that does not exist is logged as a warning and skipped.
    paths:
      - "/fylr/files/plugins/custom"
      - [...other directory...]
```

{% hint style="info" %}
Plugin paths are **literal directory names** — placeholders such as `*` and `?` are not supported. Every directory is searched recursively and each `manifest.yml` found becomes one plugin; the search does not descend further into a plugin once its manifest is found. Directories whose name begins with `.` are skipped.

Two plugins with the **same name in their manifest** cannot be loaded together, no matter which directories they come from — fylr stops with an error naming the plugin.
{% endhint %}

