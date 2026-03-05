---
description: >-
  With this plugin, images can be transferred from fylr to a Wordpress CMS. In
  Wordpress, they appear in the media gallery and can be used from there as
  usual.
---

# Wordpress

{% hint style="info" %}
At least Wordpress version 4.7 is required.
{% endhint %}

## Preparation of Wordpress

For your chosen Wordpress account, create an "Application Password" to use in fylr.\
![](<../../.gitbook/assets/image (2).png>)



With the WordPress plugin for fylr, which is included in fylr 6.29, the following is still required. But with the recommended newer versions, as described below, this is no longer needed:

1. Go to _Settings > Permalinks_.
2. Select a permalink structure other than “Plain.”
3. Save the changes.

## Installation & Configuration

### 1. Use the newest version of the plugin

Make sure to use the newest version of the plugin. E.g. in fylr 6.29, an old version of the plugin is included that has since been updated independently from fylr. To get the newest version:

Go to Administration - Plugin-Manager - select the easydb-wordpress-plugin (type **disk**)

Click the minus ( `-` )button as shown below:

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Then click the plus (+) button and add a plugin of type URL:

![](<../../.gitbook/assets/image (1).png>)



### 2. Configuration

After the plugin was installed successfully, go to its settings. Here you can add and connect one or more Wordpress installation(s):\
![](<../../.gitbook/assets/image (3).png>)

For each Wordpress installation you need to configure the following:

<table><thead><tr><th width="208">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Instance Name</td><td>Name for the Wordpress installation. Will be shown in fylr when choosing the target for the export.</td></tr><tr><td>URL</td><td>URL of the Wordpress installation.</td></tr><tr><td>Authentication Type</td><td>Choose "HTTP Authentication", not OAuth 1.0.</td></tr><tr><td>Login</td><td>Username to log into Wordpress and upload files automatically. Only available for type "HTTP Authentication".</td></tr><tr><td>Password</td><td>Password to log into Wordpress account. Use a Wordpress "Application Password" instead of the main password.  Only available for type "HTTP Authentication".</td></tr><tr><td>Client Key</td><td>Client Key for Wordpress. Only available for type "OAuth 1.0".</td></tr><tr><td>Client Secret</td><td>Client Secret for Wordpress. Only available for type "OAuth 1.0".</td></tr><tr><td>Token</td><td>Token for Wordpress. Only available for type "OAuth 1.0".</td></tr><tr><td>Token Secret</td><td>Token Secret for Wordpress. Only available for type "OAuth 1.0".</td></tr></tbody></table>

### 3. Permissions

By default, the plugin is disabled for all users except root. To grant selected users/groups access to the plugin, you need to assign them the system right "Allow Wordpress Export". This can be done in the [user](../permissions/user.md)/[group](../permissions/groups.md) editor on the tab "System Rights" > "Plugins".<br>

## Usage

After a successful installation and configuration, authorized users can create a Wordpress transport via the exporter:

1.  To transfer selected images to Wordpress, select the records in the search and right click on a record and choose "Export".&#x20;

    <figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>
2. Define which versions should be used and click on the little truck icon in the lower right. \
   ![](<../../.gitbook/assets/image (26).png>)
3.  Add a transport there and choose the type "Wordpress" <br>

    <figure><img src="../../.gitbook/assets/fylr-transport-wordpress.png" alt=""><figcaption></figcaption></figure>
4.  as well as your desired Wordpress installation under "Options". <br>

    <figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>
5. Hit "Apply" and "Export" to send the files to Wordpress.

You can then go to your Wordpress installation and use the files from the media gallery for your website.

{% hint style="warning" %}
Please note, that only images are currently supported and that the deletion of files in Wordpress is currently not supported.
{% endhint %}
