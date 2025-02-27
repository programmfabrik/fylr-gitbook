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

In fylrs right management section, we need to setup correct rights for the system user `deep_link.`This user is included in a fylr instance per default.

It's likely you'll set these permissions for a Pool managing more than one Object Type. Depending on your usage of the datamodel, it's possible you the deep\_link user permissions have to be set for an Object Type directly.



<figure><img src="../../../.gitbook/assets/Screenshot 2025-02-27 at 11.03.09.png" alt=""><figcaption><p>Rights Management > Permissions Tab: example configuration for deep_link user permissions</p></figcaption></figure>

The required Permissions are:

* View Records
  * select the Object Types you want to share with the deep\_link user
* Allowed Masks
  * for those Object Types, select the Masks you want the deep\_link user to hace access to
* View Versions
  * the versions the user is allowed to see
  * Only versions with checked rights management checkbox are listed here: see [file-worker](../../../for-administrators/readme/file-worker/ "mention") ( Base Configuration > File Worker > renditions tables "rights management" checkbox)
* Download Versions
  * mark the versions the deep\_link user should be able to download (required for deep linking versions)

### Using Deeplinks

<figure><img src="../../../.gitbook/assets/Screenshot 2025-02-06 at 17.46.34.png" alt=""><figcaption><p>Using the three-dot menu at a records file field to access deep links.</p></figcaption></figure>

To enable sharing URLs for the deep\_link user, we need to also assign the permissions:

* View Versions
  * select the versions of your object types corresponding file class you want the deep\_link user to have access to (this example uses images only)
* Download Versions
  * select the you want the deep\_link user to be allowed to download

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

