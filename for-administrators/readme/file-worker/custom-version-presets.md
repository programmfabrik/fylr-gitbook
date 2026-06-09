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

A **custom version preset** is a named set of on-demand rendition options for
image files — for example "Web large (2000px JPEG)" or a square thumbnail with a
watermark. Unlike preview [versions](preview-configuration.md), presets are
**not produced on upload**: the rendition is created the moment a user selects
the preset in the download dialog, and the downloaded file is named after the
preset. Presets are shared by all users; there is no per-group filtering.

## Configuration

Presets are configured in the base config on the **File Worker** tab, in the
**Custom Version Presets** block. The block holds a table of presets. Use the
plus button to add a preset, the pencil button to edit one, and the minus button
to delete the selected preset.

Each preset has the following settings:

| SETTING | DESCRIPTION |
| --- | --- |
| Name | Internal name of the preset, used in the API. Must be unique within the configuration. |
| Display Name | Localizable name shown to users in the download dialog. Required. |
| Options | The rendition options (see below). At least one option must have an effect, otherwise the preset is rejected on save. |

### Options

The option fields are the same as the custom-version options in the download
dialog:

| OPTION | DESCRIPTION |
| --- | --- |
| Watermark | Apply the configured watermark to the rendition. |
| Format | Output file format. *Keep* leaves the format of the source file unchanged. |
| Quality | Compression quality for lossy formats (for example JPEG). |
| Color Space | Output color space. *Keep* leaves the color space unchanged. |
| Color Profile | Embed one of the configured [.icc color profiles](custom-.icc-color-profiles.md). |
| Size | *Keep* leaves the dimensions unchanged, or choose *custom* to scale the rendition. Custom sizing can be given as a relative size, as pixel dimensions (width and/or height), or via a target DPI. |
| Transform | Rotate / flip the rendition. |

{% hint style="warning" %}
A preset must have a display name **and** at least one effective option.
The editor disables **Apply** for an invalid preset, and the server rejects an
invalid preset on save.
{% endhint %}

## Using a preset

When a preset applies to a file, it appears in the **Renditions** list of the
download options alongside the standard renditions. See
[Downloading](../../../for-users/download-and-export/downloading.md#custom-version-presets)
for the user's perspective.
