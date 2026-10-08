---
description: This section is about settings in the configuration file fylr.yml.
---

# Configuration

In the fylr.yml configuration you find settings that are not present in the frontend.&#x20;

A relative path is resolved against the directory of the config file that sets it, against the work dir when it is set with `-s` / `--set` or an environment variable, and against the directory of the fylr executable for a built-in default.

And some settings in `fylr.yml` can be set in the frontend once fylr is installed. For _those_, `fylr.yml` only can give an initial value, but not override frontend settings.
