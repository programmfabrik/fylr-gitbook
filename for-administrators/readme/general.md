---
description: >-
  In this section you find settings regarding the general appearance of the fylr
  installation.
---

# General

## Name

### Internal Name

A short technical name for this fylr installation. It is used internally in a few places rather than in the regular interface: as the identifier of the installation in **backups**, as the repository name returned by the **OAI-PMH `Identify`** response, and as the label of generated **IIIF manifests**.

### Title

The title of the fylr installation will be shown in the browser tab.

### Description

A short description of this fylr installation. It is used as the HTML meta description of the public start page, so it is what a messenger or social network shows when a link to the fylr website is unfurled into a preview (for example in Slack).


## Appearance

### Logo

Upload your own logo to replace our fylr logo in the upper right and in emails.

### Favicon

Upload an SVG or PNG file, from fylr 6.35.0 also an ICO file, to replace the fylr icon in the browser tab.

### Background Image

Upload an image which will be used as the background on the login and register page.&#x20;

### Background Color

Set a color which will be used as the background color on the login and registration page. Supports hex code only. Example: #ff5724. If no color is specified, a light grey will be used.

### Marker Color

Set a color which will be used when selecting records or for buttons and menu entries, etc. Supports hex code only. Example: #ff5724. If no color is specified, the fylr orange will be used.

## Tags & Labels

{% hint style="info" %}
Available from version 6.36.0. Up to version 6.35 the custom icons and colors were part of **Appearance**, as **Font-Awesome Icons** and **Tag Colors**. The update moves them here, and tags keep their icons and colors.
{% endhint %}

The icons and colors in this block are offered for tags, for the tagging of records in the additional settings of a pool, and for the [labels of permissions](../permissions/labels-and-notes.md). The icon and color selects there name every entry, show a custom color with its hex code, and list the entries under the headings **Built-in** and **Custom**.

### Custom Icons

Icons from Font-Awesome, in addition to the built-in icons, which are shown below the hint. Supported icons can be found here: [https://fontawesome.com/v4/icons/](https://fontawesome.com/v4/icons/). Enter the name of the icon, for example `fa-cloud-download`. If an unsupported text is entered, the first letter of the text will be shown as the icon.

A tag or label keeps its icon when the icon is removed from this list.

### Custom Colors

Colors in addition to the built-in colors, which are shown below the hint. A color is a hex code: `#RGB` or `#RRGGBB`, or with transparency `#RGBA` or `#RRGGBBAA`, for example `#ff5724`.

A tag or label refers to the row of its color, not to its position in the list. Adding a color, changing the order of the colors or removing one leaves the colors of all other tags and labels as they are. Changing the hex code of a color changes it on every tag and label that uses this color. A tag whose color is removed shows no color.

### Permission Labels

The labels offered in the permissions of pools, groups, users, object types, tags and records. Each label has a name, which can be entered per language, an icon and a color, picked from the built-in ones and the custom ones above. A label marks permission entries that belong together and grants nothing. See [Labels and Notes](../permissions/labels-and-notes.md).

Only logged-in users can read the labels. Users with the system right **Manage Base Configuration** or **Full Access to the System** can also edit them from the permissions, with **Edit Labels…** in the label select of an entry.
