---
description: How to set up PDF creation in fylr
---

# PDF Creator

{% hint style="warning" %}
The PDF-Creator is officially supported and guaranteed only in Google Chrome. In Firefox and other browsers, the PDF-Creator generally works as well, but full functionality—especially the preview—is not guaranteed, and related issues are not covered by support.
{% endhint %}

## Installation (if not yet installed)

1. Go to the **Plugin Manager** and press the **+** button at the bottom to open the marketplace.

![](<../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png>) (click to enlarge)

2. Install **PDF Creator** (`pdf-creator`) and make sure it is **enabled**.

{% hint style="warning" %}
**Do not install the PDF Server (`server-pdf`) alongside it.** PDF Creator used to send its HTML to that plugin to be rendered; from PDF Creator **1.1.0** it renders the PDF itself. Running both is not merely redundant: they declare the same custom events, only one plugin can hold an event name, and the loser's declaration is dropped. fylr 6.35 switches `server-pdf` off for you where PDF Creator is enabled — see [PDF Creator and the PDF Server](../plugins/disk-to-url-migration.md#pdf-creator-and-the-pdf-server).
{% endhint %}

### Create a PDF template

4. Go to **Rights Management** (the 3 people icon, _NOT_ the gear cogs icon) - **Object Types** - choose one object type - go to the tab named **PDF Creator** (see screenshot)

![](<../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png>) (click to enlarge)

5. Click the **+** button.
6. Name your template.
7. Do not forget to click **Save** at the end.

### Usage

8. Go to **Lists** - **Object Types** - choose a type with template - Select one Object - right click - **Print**

![](<../.gitbook/assets/image (3) (1).png>) (click to enlarge)

9. In **Custom Layouts** - open the dropdown - choose one (pdf template 1 in below example) - click **Print**

![](<../.gitbook/assets/image (4).png>) (click to enlarge)

Then a PDF is created and downloaded.

If the PDF is too empty, you can edit the template and add content: **Rights Management** (the 3 people icon) - **Object Types** - choose the object type - go to the tab named **PDF Creator**.





{% hint style="info" %}
The PDF-Creator is officially supported and guaranteed only in Google Chrome. In Firefox and other browsers, the PDF-Creator generally works, but full functionality is not guaranteed.

Related issues are not covered by support.
{% endhint %}
