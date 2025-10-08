---
label: Packaging and Release of Plugins
description: >-
  Plugins can be uploaded to fylr using the Plugin Manager in a specific ZIP archive.
  This page describes how to build the ZIP and how to integrate this into a github release workflow.
---


# Packaging and Release of Plugins

Plugins can be uploaded to fylr in the Plugin Manager. Either a ZIP file is uploaded directly, or the URL to a publicly hosted ZIP file is entered. In both cases the same ZIP file can be used.

Building the ZIP file can be integrated into a release workflow of (public) github repositories. Then a static URL which always links to the latest release can be used in the Plugin Manager. After every new release, this URL automatically links to the ZIP file with the latest plugin version. fylr checks this URL and updates the plugin if a newer version is available.

This page describes the necessary [structure](#zip-archive-structure) of the ZIP file, how to integrate the ZIP [build process](#building-the-zip-archive) into the Makefile and how to setup a github [release workflow](#github-release-workflow). All examples mentioned here are referring to the [fylr example plugin](https://github.com/programmfabrik/fylr-plugin-example). For more examples and details please refer to this plugin.


## ZIP archive structure

For all following examples it is assumed that `make build` creates a local directory named `build` inside the plugin folder, which contains all (compiled) files which are necessary for the plugin to run.

The complete content of the `build` folder, including the `manifest.yml`, must be stored in the ZIP file in a top level folder. This folder must have the same name as the plugin, as defined in the plugin manifest.


**Example:**

Content of the `build` folder after `make build`:

* `build/`
  * `fylr_example/`
    * `server/`
      * [...]
    * `webfrontend/`
      * `FylrExample.js`
      * [...]
    * `l10n/`
      * `example-loca.csv`
    * `manifest.yml`
    * [...]

The actual files depend on the functionality of the plugin. `webfrontend` or `server` might not exist, and other files/folders might also be part of the plugin.

{% hint style="info" %}
Please note that in this example, there is already a sub directory with the plugin name (`fylr_example`) inside the build folder.

It is not necessary to do it this way, it depends how the ZIP archive is actually built.
{% endhint %}

The ZIP file must then contain `fylr_example` as a single top level directory which contains all the necessary folders and files:

* `fylr_example.zip`
  * `fylr_example/`
    * [...]
    * `manifest.yml`


## Building the ZIP archive

It is recommended to add a new build target to the Makefile, which can then be executed by the release workflow.

### Makefile target `zip`

Extend the Makefile with a new target `zip`. This target needs to build a valid ZIP archive with the above mentioned [structure](#zip-archive-structure). If, how in this example, there is already a sub folder with the plugin name, then it is as easy as putting the complete folder into the ZIP file:

**Example:** [`Makefile`](https://github.com/programmfabrik/fylr-plugin-example/blob/main/Makefile)

```Makefile
PLUGIN_NAME = $(PLUGIN_NAME)
ZIP_NAME = $(PLUGIN_NAME).zip
BUILD_DIR = build

# [...]

zip: build
    cd $(BUILD_DIR)
    zip $(ZIP_NAME) -r $(PLUGIN_NAME)
```

If there is no top level folder already, use a temporary folder and remove it afterwards:

```Makefile
zip: build
    cp -r $(BUILD_DIR) $(PLUGIN_NAME)
    zip $(ZIP_NAME) -r $(PLUGIN_NAME)
    rm -rf $(PLUGIN_NAME)
```


## github Release Workflow

You can host the plugin ZIP file at any URL and use this URL to update the plugin in fylr.

You can also add a release workflow to the plugin, and every time a new release is published, the ZIP file is built and hosted in github.


### Define release workflow in plugin

Create a top level folder `.github` in the plugin folder and define the release steps in a YAML file:

* `.github/`
  * `workflows/`
    * `release.yaml`

**Example:** [`release.yaml`](https://github.com/programmfabrik/fylr-plugin-example/blob/main/.github/workflows/release.yaml)

```yaml
jobs:
  build:
    steps:

      # [...]

      - name: Extract repository name
        run: echo "REPOSITORY_NAME=$(echo '${{ github.repository }}' | awk -F '/' '{print $2}')" >> $GITHUB_ENV

      - name: Set zip file name
        run: echo "ZIP_NAME=${{env.REPOSITORY_NAME}}.zip" >> $GITHUB_ENV

      - name: Build and package zip file
        run: make zip

      # [...]
```

There are multiple other steps, mostly for setting up the build environment and installing third party tools if necessary.

Here the file name of the generated ZIP file is taken from the repository name, but this is optional. The ZIP file can have any name, as long as the internal structure is correct.

The most relevant step here is calling the `zip` target which has been defined in the Makefile.


### Create a new release in github

When a new release is created in github, the workflow from the `.github` folder is executed. For every tagged release a ZIP file is stored under a release URL and can be downloaded.

See [external documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

### URL for automatic update of plugin in fylr

Every release produces a specific URL where the ZIP file can be downloaded. This can be used to upload a specific plugin version to fylr.

The URL for the initial release is

```
https://github.com/programmfabrik/fylr-plugin-example/releases/tag/v1.0.0
```

so the generated plugin ZIP file (`fylr-plugin-example.zip`) for this release is

```
https://github.com/programmfabrik/fylr-plugin-example/releases/download/v1.0.0/fylr-plugin-example.zip
```


But this URL can not be used to utilize the automatic update of URL plugins in the plugin manager. Each github repository has a stable URL for all releases. For this plugin, the latest ZIP file can always be downloaded at

```
https://github.com/programmfabrik/fylr-plugin-example/releases/latest/download/fylr-plugin-example.zip
```

This URL redirects to the latest release. If this URL is used in the plugin manager, fylr will detect changes in the ZIP file and automatically update the plugin.

{% hint style="info" %}
Please note that fylr can not use any kind of authentication when loading plugins. The plugin URL must be reachable directly.

Using github URLs only works if the repository is public!
{% endhint %}

