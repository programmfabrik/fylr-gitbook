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

## Installation & Configuration

To use the plugin, it needs to be installed and configured in fylr.&#x20;

### 1. Installation



### 2. Configuration

After the plugin was installed successfully, go to the [base configuration](../readme/) and look for "easydb-wordpress-plugin". Here you can add and connect one or more Wordpress installation(s).&#x20;

For each Wordpress installation you need to configure the following:

<table><thead><tr><th width="208">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Instance Name</td><td>Name for the Wordpress installation. Will be shown in fylr when choosing the target for the export.</td></tr><tr><td>URL</td><td>URL of the Wordpress installation.</td></tr><tr><td>Authentication Type</td><td>Choose between "HTTP Authentication" and "OAuth 1.0".</td></tr><tr><td>Login</td><td>Login for Wordpress. Only available for type "HTTP Authentication".</td></tr><tr><td>Password</td><td>Password for Wordpress. Only available for type "HTTP Authentication".</td></tr><tr><td>Client Key</td><td>Client Key for Wordpress. Only available for type "OAuth 1.0".</td></tr><tr><td>Client Secret</td><td>Client Secret for Wordpress. Only available for type "OAuth 1.0".</td></tr><tr><td>Token</td><td>Token for Wordpress. Only available for type "OAuth 1.0".</td></tr><tr><td>Token Secret</td><td>Token Secret for Wordpress. Only available for type "OAuth 1.0".</td></tr></tbody></table>

### 3. Permissions

By default, the plugin is disabled for all users except root. To grant selected users/groups access to the plugin, you need to assign them the system right "Allow Wordpress Export". This can be done in the [user](../permissions/user.md)/[group](../permissions/groups.md) editor on the tab "System Rights" > "Plugins".\


## Usage

After a successful installation and configuration, authorized users can create a Wordpress transport via the exporter.

To transfer selected images to Wordpress, select the records in the search and right click on a record and choose "Export". Define which versions should be used and click on the little truck icon in the lower right. Add a transport there and choose the type "Wordpress" as well as your desired Wordpress installation under "Options". Hit "Apply" and "Export" to send the files to Wordpress.

You can then go to your Wordpress installation and use the files from the media gallery for your website.



{% hint style="warning" %}
Please note, that only images are currently supported and that the deletion of files in Wordpress is currently not supported.
{% endhint %}

