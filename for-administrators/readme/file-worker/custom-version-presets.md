---
description: >-
  Custom version presets are named, ready-to-use download formats that users can
  pick in the download dialog. The rendition is produced on demand. This article
  describes how to configure them.
---

# Custom Version Presets

{% hint style="info" %}
Custom version presets are available from fylr **6.34.0**.
{% endhint %}

A **custom version preset** is a named set of on-demand rendition options for image files — for example "Web large (2000px JPEG)" or a square thumbnail with a watermark. Unlike preview [versions](preview-configuration.md), presets are **not produced on upload**: the rendition is created the moment a user selects the preset in the download dialog, and the downloaded file is named after the preset. Presets are shared by all users; there is no per-group filtering.

## Configuration

Presets are configured in the base config on the **File Worker** tab, in the **Custom Version Presets** block. The block holds a table of presets. Use the plus button to add a preset, the pencil button to edit one, and the minus button to delete the selected preset.

Each preset has the following settings:

<table><thead><tr><th width="206.66015625">SETTING</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Name</td><td>Internal name of the preset, used in the API. Must be unique within the configuration.</td></tr><tr><td>Display Name</td><td>Localizable name shown to users in the download dialog. Required.</td></tr><tr><td>Options</td><td>The rendition options (see below). At least one option must have an effect, otherwise the preset is rejected on save.</td></tr></tbody></table>

### Options

The option fields are the same as the custom-version options in the download dialog:

<table data-search="false"><thead><tr><th width="211.109375">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Rendition Name</td><td>Internal name of the rendition.</td></tr><tr><td>Display Name</td><td>Name of the renditions that's shown in the download options.</td></tr><tr><td>Format</td><td>Output file format. "Unchanged" leaves the format of the source file unchanged.</td></tr><tr><td>Size</td><td>"Unchanged" leaves the dimensions unchanged, or choose "Resize/Crop" to scale the rendition.</td></tr><tr><td>Color Space</td><td>Output color space. "Unchanged" leaves the color space unchanged.</td></tr><tr><td>DPI</td><td>Target DPI.</td></tr><tr><td>Color Profile</td><td>Embed one of the configured <a href="custom-.icc-color-profiles.md">.icc color profiles</a>.</td></tr><tr><td>Watermark</td><td>Apply the configured watermark to the rendition.</td></tr></tbody></table>



{% hint style="warning" %}
A preset must have a display name **and** at least one effective option. The editor disables **Apply** for an invalid preset, and the server rejects an invalid preset on save.
{% endhint %}

## Using a preset

When a preset applies to a file, it appears in the **Renditions** list of the download options alongside the standard renditions. See [Downloading](../../../for-users/download-and-export/downloading.md#custom-version-presets) for the user's perspective.
