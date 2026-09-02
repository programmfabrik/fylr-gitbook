---
description: >-
  The default feature set of FYLR can be extended using plugins which can be
  managed here.
---

# Plugin Manager

## Introduction to Plugins

Plugins are **installed** from the **marketplace**, **uploaded** as a **ZIP** or added via an **URL**. Some plugins are **available** for **all** customers, others were only **developed** for specific **customers**.

Up to fylr 6.34, a set of plugins was shipped with **every** release (type "disk") and could not be removed, only disabled. **fylr 6.35 will no longer ship plugins on disk**: the plugins installed in an instance will be migrated to url plugins at the upgrade — see [Disk to URL plugin migration](../../plugins/disk-to-url-migration.md). Loading **your own** plugins from a directory stays supported, see [Load Custom Plugins](../../for-system-administrators/configuration/custom-plugin.md).

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
From fylr **6.34.0**, the WordPress, Drupal and TYPO3 integrations are no longer shipped as bundled "disk" plugins. They are maintained as separate plugins (`fylr-plugin-wordpress`, `fylr-plugin-drupal`, `fylr-plugin-typo3`) and are installed from the marketplace. Instances that relied on the former `easydb-wordpress-plugin`, `easydb-drupal-plugin` or `easydb-typo3-plugin` have to install the corresponding `fylr-plugin-*` plugin after updating — the [disk to URL migration](../../plugins/disk-to-url-migration.md) does it for an instance coming from 6.33 or earlier.

All three are **licensed** plugins: they install freely, but your fylr license has to grant them by name before they can be enabled. If you use one of these connectors, obtain an updated license from Programmfabrik **before** you upgrade.
{% endhint %}


## Working with the Plugin Manager

Use the **search** to search for the internal or display **names** of plugins and click on a plugin so see all **details**. There, you can also **disable** or **enable** plugins, as well as **upload** a new version or define **automatic updates**:

<table><thead><tr><th width="192.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>automatic (daily)</td><td>The plugin source is checked once a day; a new version is installed when one is found. This is the default for a plugin installed from a URL.</td></tr><tr><td>always (development)</td><td>The source is checked every 10 seconds. Meant for developing a plugin, not for production.</td></tr><tr><td>never</td><td>The plugin is not updated automatically. Its source is still probed, so a broken URL is still reported — but a new version is not installed.</td></tr></tbody></table>

A **ZIP** plugin has no update policy: it is the bytes you uploaded, so the setting is fixed to *never* and the dropdown is disabled. Replacing it means uploading a newer ZIP.

A **failed** update attempt (unreachable URL, broken download, invalid ZIP) leaves the **installed** version running untouched. From fylr **6.35.0** such an attempt is **retried** every **10 seconds** — with every update policy, so a repaired release is picked up within seconds instead of at the next daily check — and no longer leaves files behind: the broken download is **removed** again, as is the **previous** plugin ZIP after a successful update.

### Plugin timestamps

The *General* tab of a plugin shows three timestamps. From fylr **6.35.0** they have a fixed meaning:

<table><thead><tr><th width="192.5">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Created At</td><td>When the plugin was installed.</td></tr><tr><td>Updated At</td><td>When the stored plugin <strong>content</strong> last changed: set at install and whenever a new version is stored. Saving <strong>settings</strong> only (<em>Active</em>, the update policy) does <strong>not</strong> change it.</td></tr><tr><td>Last Checked At</td><td>When fylr last <strong>completed</strong> a check of the plugin source for updates. A failed update attempt does not change it.</td></tr></tbody></table>

### Plugin README tab

From fylr **6.35.0**, a plugin that ships a `README.md` next to its `manifest.yml` gets a **README** tab in the Plugin Manager showing the plugin's documentation — the same file the [Plugin Marketplace](#plugin-marketplace) shows as **more information** before installing. Plugins built with `fylr-build-plugin` bundle their repository README automatically. fylr detects the file when it reads the plugin content, so the tab appears from install or the plugin's next update.

### Managing Plugins

To **install** a plugin, click on the **plus** button in the lower left. From fylr **6.35.0** this opens the **Plugin Marketplace** (see below); uploading your own plugin as a **ZIP** file or from a **URL** is still available there. Please make sure to **enable** the plugin afterwards.

To **remove** a plugin, **select** it and click on the **minus** button in the lower left.

{% hint style="info" %}
Please note, some plugins may come with custom settings. Please check the [base configuration](../readme/plugins.md).
{% endhint %}

### Plugin Marketplace

From fylr **6.35.0**, the **plus** button opens the **marketplace** — a curated catalog of installable plugins, grouped by **category**, each with a localized **description** and a **more information** view that shows the plugin's README. **Installing** a plugin from the marketplace also installs any plugins it **depends on**; conversely, a plugin that an enabled plugin depends on can **not** be **disabled** or **deleted** while that dependent plugin is enabled.

**Paid** and **private** plugins are delivered **sealed** (encrypted) and are decrypted by fylr during the install. Whether such a plugin can be **enabled** is decided by your **license** (see below).

{% hint style="info" %}
The catalog is served by `GET /plugin/marketplace`. Programmfabrik's curated catalog is **pulled from a published catalog sheet** at request time and cached, so the offer can change without a fylr update; a system administrator can configure additional sources in `fylr.yml` (`plugin.marketplace.sources`). Should the catalog be unreachable before fylr ever loaded it, the marketplace reports itself as **temporarily unavailable** — try again a little later. For the design behind sealed delivery, see the [white paper](../../for-developers/concepts/white-papers/secure-plugin-delivery.md).
{% endhint %}

### License-gated plugins

From fylr **6.35.0**, the fylr **license** can determine which plugins an instance may **enable** — see [License management](../../license-management.md). A plugin the license does not permit is flagged in the Plugin Manager with a red **warning triangle** in the *Active* column, its *General* tab shows the license state, and its **Active** toggle is disabled. The plugin's stored configuration is **preserved** and the plugin re-enables by itself once the license grants it again.

### Network access in restricted setups

Important for e.g. Kubernetes clusters or any other firewalled / egress-controlled setups:

For the plugin manager to install and automatically update a plugin from a URL, fylr must be able to reach that URL. In environments with restricted outbound network access, every host below has to be allowed explicitly — each one fails on its own:

<table><thead><tr><th width="290">HOST</th><th>NEEDED FOR</th></tr></thead><tbody><tr><td><code>docs.google.com</code></td><td>The <strong>marketplace catalog</strong>, which fylr reads from a published sheet when the shop is opened. Without it the marketplace reports itself as temporarily unavailable — plugins already installed keep working and updating.</td></tr><tr><td><code>programmfabrik.github.io</code></td><td>The install ZIP of every <strong>paid or private</strong> plugin, which is served from GitHub Pages.</td></tr><tr><td><code>github.com</code> and <code>*.githubusercontent.com</code></td><td>The install ZIP of every plugin published as a <strong>GitHub release</strong>. The <code>releases/latest/download/…</code> URL redirects to a <code>githubusercontent.com</code> host, so allowing <code>github.com</code> alone is not enough.</td></tr></tbody></table>

Without the relevant entry the plugin download and its automatic updates fail; the plugin manager marks the plugin with a warning triangle and says why. A plugin that could never be downloaded at all can still be installed through the browser — see [Installations without internet access](../../plugins/disk-to-url-migration.md#installations-without-internet-access).
