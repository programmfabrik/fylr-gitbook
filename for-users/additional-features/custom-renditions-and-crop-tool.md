# Custom Renditions & Crop Tool

Custom renditions let you create additional versions of images with your own settings. You can control the output size, file format, and other export options. When using **Resize/Crop**, you can also define a crop individually for each image before downloading.

{% hint style="info" %}
Please note, that the custom renditions and crop tool are currently only available to users that can access the original file.
{% endhint %}

## Using Custom Renditions

The [Download Manager](../download-and-export/downloading.md) lists all available standard renditions (pre-calculated) and pre-defined custom renditions (calculated on demand).

Pre-defined custom renditions are created by your administrator and are available to all users. To include a pre-defined custom rendition in the download, select its checkbox.

If the preset supports cropping, a **Crop** button becomes available after the rendition is selected. Clicking it opens the Crop Editor, where you can adjust the crop for each image. If you use a crop-enabled rendition without adjusting it, the image is cropped automatically using a centered crop.

Additionally a **Custom rendition** can be created for the current download only. Select the **Custom rendition** entry to open the Crop Editor and configure your own export settings. These settings are not saved and are available only for the current download. You can optionally start from an existing preset and modify its settings.

## The Rendition Editor

The Rendition Editor contains three sections:

* **Settings** – Configure the rendition.
* **Files** – Choose which images the rendition applies to.
* **Preview** – Preview the selected image and edit its crop.

### Settings

The Settings section defines how the exported images are created.

{% hint style="info" %}
Please note that pre-defined renditions provided by your administrator cannot be modified. Only the crop can be adjusted.
{% endhint %}

#### Start from Preset

Select a pre-defined custom rendition and all settings will be pre-filled. You can adjust all settings individually.

#### Size

The selected size mode determines how the exported image is generated.

**Resize/Crop** lets you define both the crop area and the output size. The crop determines **which part** of the image is used. The size settings determine **how large** the exported image will be.

You can specify:

* Both width and height for an exact output size.
* Only a width.
* Only a height.
* Neither, to keep the cropped area at its original resolution.

The following modes resize the entire image without cropping:

* Long side
* Short side
* Width
* Height
* Unchanged

#### Files Section

The Files list shows all images included in the rendition.

For each image, you can:

* Select the image to preview and edit it.
* Exclude it from the current rendition by clearing its checkbox.
* Identify additional file variants when they are included in the download.
* See whether a crop has already been applied.

Each image can have its own crop.

#### Preview and output size

The Preview displays the selected image together with the Crop Tool.

An output badge shows the final pixel dimensions that will be exported for the selected image.

{% hint style="info" %}
If the requested output size is larger than the available image resolution, the preview displays an **Upscaling** warning.
{% endhint %}

### Crop Tool

The Crop Tool is available only when the rendition uses **Resize/Crop**. It lets you select exactly which part of an image will be included in the exported file. Zooming and panning only change the view. They do not affect the crop itself.

#### Basic controls

<table data-search="false"><thead><tr><th width="185.875">ACTION</th><th>SHORTCUT / GESTURE</th><th>EFFECT</th></tr></thead><tbody><tr><td><strong>Zoom</strong></td><td>Mouse wheel / pinch</td><td>Zoom the view in/out. Crop unchanged.</td></tr><tr><td><strong>Pan</strong></td><td>Right‑drag, or left‑drag on empty canvas</td><td>Move the view. Crop unchanged.</td></tr><tr><td><strong>Move crop</strong></td><td>Left‑drag inside the frame</td><td>Reposition the crop over the image.</td></tr><tr><td><strong>Resize crop</strong></td><td>Drag the edge/corner handles</td><td>Resize; the opposite edge stays anchored (directional).</td></tr><tr><td><strong>Keep proportions</strong></td><td><strong>Shift</strong> while resizing</td><td>Locks the current ratio during the drag.</td></tr><tr><td><strong>Resize from center</strong></td><td><strong>Alt</strong> while resizing</td><td>Symmetric around the crop center.</td></tr><tr><td><strong>Crop follows view</strong></td><td><strong>Alt</strong> + wheel / <strong>Alt</strong> + drag</td><td>"Viewfinder" mode: the frame stays fixed on screen and the crop region follows the zoom/pan.</td></tr><tr><td><strong>Fit toggle</strong></td><td>Double‑click</td><td>Alternates between <em>fit the crop</em> (centered, large) and <em>fit the whole image</em>.</td></tr><tr><td><strong>Rotate 90°</strong></td><td>Toolbar rotate‑left / rotate‑right</td><td>90° steps.</td></tr><tr><td><strong>Straighten (fine)</strong></td><td>Bottom dial, or the <strong>straighten tool</strong> (draw a line along an edge that should be level)</td><td>Fine rotation; the exported result is rotated then cropped.</td></tr><tr><td><strong>Select whole image</strong></td><td>Toolbar "whole image" button</td><td>Crop = the entire image (honoring the ratio).</td></tr><tr><td><strong>Fit view</strong></td><td>Toolbar "fit" button</td><td>Fit the whole image in the view.</td></tr><tr><td><strong>Shortcuts help</strong></td><td><strong>?</strong> button (top‑right)</td><td>Opens a popover cheat sheet of these shortcuts.</td></tr></tbody></table>

#### Aspect ratios

The crop can use either:

* A free aspect ratio.
* A fixed aspect ratio.

When a fixed aspect ratio is selected, the crop always maintains that ratio while it is resized.

#### Rotating and straightening

In **Resize/Crop** mode, you can adjust the image orientation before export.

The Crop Tool supports:

* Rotation in 90° steps.
* Fine straightening using the rotation control.
* Automatic straightening by drawing a reference line along an edge or horizon.

These adjustments are applied to the exported image before it is cropped.
