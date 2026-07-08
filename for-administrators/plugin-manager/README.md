---
description: >-
  The default feature set of FYLR can be extended using plugins which can be
  managed here.
---

# Plugin Manager

## Introduction to Plugins

Some **plugins** will be shipped with **every** release by **default** (type "disk") and can't be removed (only disabled). Others can be **uploaded** as a **ZIP** or via an **URL**. Some plugins are **available** for **all** customers, others were only **developed** for specific **customers**.

{% hint style="info" %}
Please refer to the official [Programmfabrik GmbH GitHub](https://github.com/orgs/programmfabrik/repositories?q=plugin) account for all Open Source plugins that were either developed by us or our partners. Download links and documentation for each plugin can be found there.
{% endhint %}

{% hint style="info" %}
For a technical introduction to plugins, please click [here](../../for-developers/plugin.md).
{% endhint %}

{% hint style="info" %}
For a overview over all publicly available plugins, please click [here](../../plugins/overview.md).
{% endhint %}

{% hint style="warning" %}
From fylr **6.34.0**, the WordPress, Drupal and TYPO3 integrations are no longer shipped as bundled "disk" plugins. They are maintained as separate plugins (`fylr-plugin-wordpress`, `fylr-plugin-drupal`, `fylr-plugin-typo3`) and must be installed as **URL plugins**. Instances that relied on the former `easydb-wordpress-plugin`, `easydb-drupal-plugin` or `easydb-typo3-plugin` have to install the corresponding `fylr-plugin-*` release after updating.
{% endhint %}


## Working with the Plugin Manager

Use the **search** to search for the internal or display **names** of plugins and click on a plugin so see all **details**. There, you can also **disable** or **enable** plugins, as well as **upload** a new version or define **automatic updates**:

<table><thead><tr><th width="192.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Never</td><td>The plugin will not be updated automatically.</td></tr><tr><td>Daily</td><td>The version of the plugin will be checked every 24 hours and if there is a new version available, the plugin will be updated.</td></tr><tr><td>Immediately</td><td>The version of the plugin will be checked every 10 seconds and if there is a new version available, the plugin will be updated.</td></tr></tbody></table>

### Managing Plugins

To **upload** a plugin, click on the **plus** button in the lower left and either upload the **ZIP** file or enter the **URL** to the ZIP file. Please make sure to **enable** the plugin afterwards.

To **remove** a plugin, **select** it and click on the **minus** button in the lower left.

{% hint style="info" %}
Please note, some plugins may come with custom settings. Please check the [base configuration](../readme/plugins.md).
{% endhint %}

### Network access in restricted setups

Important for e.g. Kubernetes clusters or any other firewalled / egress-controlled setups:

For the plugin manager to install and automatically update a plugin from a URL, fylr must be able to reach that URL. In environments with restricted outbound network access the install/update URL host must be explicitly allowed.

For GitHub Pages install URLs that host is `programmfabrik.github.io`. Without this allowlist entry, the plugin download and its automatic updates fail.
