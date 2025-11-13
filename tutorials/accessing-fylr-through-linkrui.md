---
description: >-
  Integrating fylr into various third party services such as Google Worksuite,
  Figma and Adobe
---

# Accessing fylr through LinkrUI

{% hint style="info" %}
**BETA**: fylr integration is currently in active development from [Santa Cruz Software](https://santacruzsoftware.com/)
{% endhint %}

## Required

Fylr requires linkrui capabilities in license. **Not part of fylr by default.** Contact support to obtain a new license including linkrui. The underlying fylr instance needs no additional configuration for the LinkrUI extension to work.

* **Authentication:** A login to a appropriately licensed fylr instance
* **Rights Management:** Permissions to see and download at least one object type with a file field

## Setup (for Google Workspace)

1. Install the "LinkrUI for Google Workspace" Add-On in your extension of choice
2. Open the LinkrUI Extension
3. Provide the fylr server URL, authenticate with your login

<figure><img src="../.gitbook/assets/Screenshot 2025-11-13 at 14.58.50.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Current authentication bug:** If the authenticate page opening shows errors, copy the generated authentication link in the extension, update the URLs `client_id` parameter from `santa-cruz` to `linkrui` , then paste the URL and authenticate.&#x20;
{% endhint %}

## Usage

* Filter by pool, Object Type and file extension
* Search by text in your fylr instances media assets

<figure><img src="../.gitbook/assets/Screenshot 2025-11-13 at 15.21.41.png" alt=""><figcaption><p>A simple search in the linkrui extension, result in grid view, filters highlighted</p></figcaption></figure>



* Place assets by accessing the 3dot-menu at the record, or by drag and dropping them onto the open project

<figure><img src="../.gitbook/assets/Screenshot 2025-11-13 at 15.24.12.png" alt=""><figcaption><p>Open detail view with bottom toolbar options</p></figcaption></figure>

* **Bottom toolbar**: View options for search result, access detail view with link to fylr record



### **Supported file formats for exporting back to fylr**

The file types supporting the **"New Version"** option vary depending on the product the extension is used in.&#x20;

* **Google Docs:** docx, pdf, odt
* **Google Sheets:** xlsx, pdf, ods
* **Google Slides:** pptx, pdf&#x20;
* **Adobe Express:** pdf, jpg, png, mp4&#x20;
* **Figma:** jpg, png, svg, pdf&#x20;

The according file format may be exported back into fylr as a new variant of the original asset:

**Export**: via 3-dot menu at the record in extension

Open the record in fylr, at the file field find the variants with a new addition.

{% hint style="danger" %}
**Currently unsupported:**

* Accessing collections and saved searches in extension
* Exporting into new records&#x20;
* Complex field types missing from object type (linked records in nesteds, reverse linked records etc.)
{% endhint %}
