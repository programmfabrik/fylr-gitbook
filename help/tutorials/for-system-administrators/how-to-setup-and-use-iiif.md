---
description: >-
  How to configure the International Image Interoperability Framework built into
  fylr
---

# How to setup and use IIIF

Activating IIIF

1. In the base configuration of fylr, go to the section "Export & Deep Links"
2. Under Deep Links Settings, enable the service by checking the respective checkbox

<figure><img src="../../../.gitbook/assets/Screenshot 2025-02-06 at 17.06.17.png" alt=""><figcaption></figcaption></figure>

Refer to the documentation on [export-and-deep-links.md](../../../for-administrators/readme/export-and-deep-links.md "mention") for further explanation on the individual options.

{% hint style="info" %}
**Please note:** you have to assign permissions to the system user "Deep Link" so the links are working. Users also need the system right "Deep Links" to access the links in the detail view.
{% endhint %}

### Settings up rights management for Deep Links

{% hint style="warning" %}
WIP
{% endhint %}

## Using Deeplinks



<figure><img src="../../../.gitbook/assets/Screenshot 2025-02-06 at 17.46.34.png" alt=""><figcaption></figcaption></figure>

The links are shared with the Deep-Link user. If some URLs appear to be unavailable, this is because they are not shared.&#x20;

{% hint style="warning" %}
**WIP**
{% endhint %}

## Adding custom IIIF viewers

In the base config, we can add custom IIIF viewers using template replacement for fylr to generate manifests and embeddable templates.

{% hint style="info" %}
**The default viewer used in fylr is the** [**Mirador Viewer**](https://projectmirador.org/)
{% endhint %}

This example uses the [Curation Viewer](https://codh.rois.ac.jp/software/iiif-curation-viewer/demo/).

**Label:**

A name for the label, such as "Universal Viewer", "Curation Viewer," would be appropriate.

**HTML Code:**

We define a template used by the server to generate an HTML snippet that embeds a standalone IIIF viewer (e.g., Mirador or Curation Viewer). This snippet can then be externally integrated.

{% code overflow="wrap" %}
```html
<iframe 
    width="100%" 
    height="600" 
    src="https://codh.rois.ac.jp/software/iiif-curation-viewer/demo/?manifest=%iiif_presentation_manifest.url%">
</iframe>
```
{% endcode %}

The fylr server will replace the template `%iiif_presentation_manifest.url%`  with  the actual manifest URL.



**Usage**

<figure><img src="../../../.gitbook/assets/Screenshot 2025-02-06 at 17.44.14.png" alt="" width="375"><figcaption><p>FInd the custom IIIF viewer in the sharing dialog</p></figcaption></figure>

* You can copy the generated code from the sharing dialog of a dataset and test it by putting inside the  [W3Schools iframe test](https://seleniumbase.io/w3schools/iframes) and pressing "Run."
* This link can also be integrated into other web pages

