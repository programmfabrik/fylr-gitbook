---
description: Errors when using docker-compose
---

# ContainerConfig error

## Symptoms

When recreating a container, e.g. during an update, with docker-compose:

<pre><code><strong>Recreating postgresql ...
</strong><strong>
</strong><strong>ERROR: for postgresql  'ContainerConfig'
</strong>Traceback (most recent call last):
  File "/bin/docker-compose", line 33, in &#x3C;module>
    sys.exit(load_entry_point('docker-compose==1.29.2', 'console_scripts', 'docker-compose')())
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[...]

    File "/usr/lib/python3/dist-packages/compose/service.py", line 1579, in get_container_data_volumes
    container.image_config['ContainerConfig'].get('Volumes') or {}
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 'ContainerConfig'
</code></pre>



## Causes

As far as we know, docker changed something so that `docker-compose` does not work with containers that were created with an older version `docker-compose`.\


But as `docker-compose` is considered <mark style="color:red;">deprecated</mark> and should be replaced with `docker compose` (note the missing `-` . It is now a plugin to `docker` instead of a stand-alone program named `docker-compose`), we just switch to `docker compose` instead of investigating the situation further with the deprecated `docker-compose`.



## Solutions

Stop and remove all running containers. For good measure you can also restart the docker service, but for us this was not needed in all cases.

Make sure the docker plugin for compose is installed. E.g. in the Debian package `docker-compose-plugin`.

Create all desired containers, but with `docker compose` instead of `docker-compose` (Note the difference: `-`) \


In our recommended installation page, we now recommend docker compose.

Our provided example maintain script now also uses docker compose, you can get the updated version like:

```
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/maintain -o maintain
chmod a+x maintain
```

