---
description: This article explains how to configure captions for image previews in fylr.
---

# Configuring Captions for Image Previews

In **fylr**, you can render dynamic captions directly onto **preview images**. Captions can display fixed values or values from the record, giving context and improving visual identification of files. The available options allow you to customize both the content and appearance of the captions.

## Preconditions

Captions are applied to **watermarked renditions**. By default, every fylr instance includes a watermarked rendition, which can be found in the **Base Configuration > Fileworker**. Additional watermark versions can be added through the Fileworker, but it is important to ensure that any new versions are correctly marked as "**watermarked"** in the rendition configuration to enable captions.

{% hint style="info" %}
Since preview renditions must be generated, it is recommended to first test the settings using a small pool. This ensures that rendering is quick and avoids placing excessive load on the server while creating new renditions.
{% endhint %}

## Caption Configuration

For **object types that are not pool managed**, enable & configure captions in:

* Rights Management > Object Types > \[_Select_ _Object Type_] > Watermark tab

For **pool-managed object types**, enable & configure captions in:

* Rights Management > Pools > \[_Select Pool_] > Watermark tab



Start by adding a row in the **Fields** table and selecting the file field for which you want to create captions. In the next column, enter the caption text, which can be either static text or include **placeholders** to dynamically render values from the record.

You can also customize the appearance of captions using the following options:

* **Size** – Set the font size in **px** or **%**.
* **Padding** – Set spacing around the caption in **px**.
* **Multiline** – Recommended for long captions; wraps text to the next line.
* **Overlay** – Determines whether the caption is rendered **on top of the image** or appended **below** it.

{% hint style="warning" %}
When you save a caption configuration, the system prompts you to **resync all affected records** (in the pool or object type) to create or update the renditions. It is **recommended to perform this immediately**. Resync can also be triggered later via **/inspect/files**.&#x20;
{% endhint %}

{% hint style="info" %}
Captions of reverse-linked records are configured in the **source object type** (with file/EAS field).
{% endhint %}
