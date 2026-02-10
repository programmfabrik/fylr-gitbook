---
label: Packaging and Release of Plugins
description: >-
  Plugins can be uploaded to fylr using the Plugin Manager in a specific ZIP
  archive. This page describes how to build the ZIP and how to integrate this
  into a github release workflow.
---

# fylr Plugins: Packaging and Release

Plugins can be uploaded to fylr in the Plugin Manager. Either a ZIP file is uploaded directly, or the URL to a publicly hosted ZIP file is entered. In both cases the same ZIP file can be used.

Building the ZIP file can be integrated into a release workflow of (public) github repositories. Then a static URL which always links to the latest release can be used in the Plugin Manager. After every new release, this URL automatically links to the ZIP file with the latest plugin version. fylr checks this URL and updates the plugin if a newer version is available.

This page describes the necessary [structure](release.md#zip-archive-structure) of the ZIP file, how to integrate the ZIP [build process](release.md#building-the-zip-archive) into the Makefile and how to setup a github [release workflow](release.md#github-release-workflow). All examples mentioned here are referring to the [fylr example plugin](https://github.com/programmfabrik/fylr-plugin-example). For more examples and details please refer to this plugin.

## ZIP archive structure

For all following examples it is assumed that `make build` creates a local directory named `build` inside the plugin folder, which contains all (compiled) files which are necessary for the plugin to run.

The complete content of the `build` folder, including the `manifest.yml`, must be stored in the ZIP file in a top level folder. This folder must have the same name as the plugin, as defined in the plugin manifest.

**Example:**

Content of the `build` folder after `make build`:

* `build/`
  * `fylr_example/`
    * `server/`
      * \[...]
    * `webfrontend/`
      * `FylrExample.js`
      * \[...]
    * `l10n/`
      * `example-loca.csv`
    * `manifest.yml`
    * \[...]

The actual files depend on the functionality of the plugin. `webfrontend` or `server` might not exist, and other files/folders might also be part of the plugin.

{% hint style="info" %}
Please note that in this example, there is already a sub directory with the plugin name (`fylr_example`) inside the build folder.

It is not necessary to do it this way, it depends how the ZIP archive is actually built.
{% endhint %}

The ZIP file must then contain `fylr_example` as a single top level directory which contains all the necessary folders and files:

* `fylr_example.zip`
  * `fylr_example/`
    * \[...]
    * `manifest.yml`

## Building the ZIP archive

It is recommended to add a new build target to the Makefile, which can then be executed by the release workflow.

### Makefile target `zip`

Extend the Makefile with a new target `zip`. This target needs to build a valid ZIP archive with the above mentioned [structure](release.md#zip-archive-structure). If, how in this example, there is already a sub folder with the plugin name, then it is as easy as putting the complete folder into the ZIP file:

**Example:** [`Makefile`](https://github.com/programmfabrik/fylr-plugin-example/blob/main/Makefile)

```makefile
PLUGIN_NAME = $(PLUGIN_NAME)
ZIP_NAME = $(PLUGIN_NAME).zip
BUILD_DIR = build

# [...]

zip: build
    cd $(BUILD_DIR)
    zip $(ZIP_NAME) -r $(PLUGIN_NAME)
```

If there is no top level folder already, use a temporary folder and remove it afterwards:

```makefile
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

### Include the github release tag in build info

To include the current release tag, the Makefile and the release workflow must be updated, so that the release tag is passed into the Makefile and written into the build-info.json:

```make
# extend the buildinfojson target: add new key "release"
buildinfojson:
	repo=`git remote get-url origin | sed -e 's/\.git$$//' -e 's#.*[/\\]##'` ;\
	rev=`git show --no-patch --format=%H` ;\
	lastchanged=`git show --no-patch --format=%ad --date=format:%Y-%m-%dT%T%z` ;\
	builddate=`date +"%Y-%m-%dT%T%z"` ;\
	release=$(if $(strip $(RELEASE_TAG)),'"$(RELEASE_TAG)"','null') ;\
	echo '{' > build-info.json ;\
	echo '  "repository": "'$$repo'",' >> build-info.json ;\
	echo '  "rev": "'$$rev'",' >> build-info.json ;\
	echo '  "release": '$$release',' >> build-info.json ;\
	echo '  "lastchanged": "'$$lastchanged'",' >> build-info.json ;\
	echo '  "builddate": "'$$builddate'"' >> build-info.json ;\
	echo '}' >> build-info.json
```

The variable `RELEASE_TAG` is coming from the release workflow. The workflow must be extended so that it is passed into the `make zip` target:

```yaml
      - name: Build and Package
        shell: bash
        run: |
          export RELEASE_TAG=${{ steps.get_version.outputs.VERSION }}
          make zip
```

### Create a new release in github

When a new release is created in github, the workflow from the `.github` folder is executed. For every tagged release a ZIP file is stored under a release URL and can be downloaded.

See [external documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

#### Important: Format of the release tag

The release tag must have the format `v*.*.*` (for example `v1.2.3`), matching the definition in the `release.yaml` file, otherwise the release workflow will not be triggered in github. Other formats could theoretically be defined here, but this is not recommended!

```yaml
on:
  push:
    tags:
      - "v*.*.*"
```

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

## Release of private plugins to github pages

### Prepare repository

1. Open repository settings in github: `https://github.com/programmfabrik/<plugin>/settings`
2. Configure pages:
   1. Select "Pages"
   2. Under "Build and deployment" select Source "**GitHub Actions**"
3. Configure environments
   1. Select "Environments"
   2. Select "**github-pages**"
   3. Click "(+) Add deployment branch or tag rule"
      1. Select "Ref type: Tag"
      2. Enter "Name pattern:" `v*.*.*`
      3. "Add Rule"

### Add/update github release workflow

1. If there is no workflow in `.github/workflows/release.yaml`, [add a new workflow](release.md#define-release-workflow-in-plugin)
2. The following updates are relevant:
   1.  Store the zip file name of the public zip file: update the step `Set zip file env name` , make sure to replace `UUID` with some random string to make the URL hard to guess:

       ```yaml
       - name: Set zip file name
         run: |
           echo "ZIP_NAME=${{env.REPOSITORY_NAME}}.zip" >> $GITHUB_ENV
           echo "ZIP_HASH_NAME=${{env.REPOSITORY_NAME}}-UUID-latest.zip" >> $GITHUB_ENV
       ```
   2.  Add two new steps to upload the zip file to the public pages below step `Build and Package`:

       ```yaml
       - name: Prepare Github Pages upload
         shell: bash
         run: |
           mkdir -p public
           cp build/${{ env.ZIP_NAME }} public/${{ env.ZIP_HASH_NAME }}

       - name: Upload to Github Pages
         uses: actions/upload-pages-artifact@v3
         with:
           path: ./public
       ```
   3.  Add a new Job under `jobs`:

       ```yaml
         deploy:
           if: "!github.event.release.prerelease"
           needs: build
           runs-on: ubuntu-latest
           permissions:
             contents: read
             pages: write
             id-token: write
           environment:
             name: github-pages
             url: ${{ steps.deployment.outputs.page_url }}
           steps:
           - name: Deploy to GitHub Pages
             id: deployment
             uses: actions/deploy-pages@v4
       ```

### Public URL for automatic update of private plugin in fylr

After the release was run, the public obscured ZIP URL of the plugin is

`https://programmfabrik.github.io/<plugin>/<ZIP_HASH_NAME>`

1. replace `<plugin>` with the plugin name, same as in the repository url
2. replace `<ZIP_HASH_NAME>` with the zip file name which was defined in `release.yaml`

This URL is stable for each release and can be used in the fylr plugin manager for a URL plugin
