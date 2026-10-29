---
description: >-
  A frontend plugin type that adds buttons next to "Copy" and "Open" of a
  collection's share links.
---

# Collection Share Link Plugin

From fylr **6.36.0**, a plugin can add its own buttons to the **Link** column of a collection's **Sharing** tab, next to the built-in **Copy** and **Open**. The same buttons show next to **Sharing Link** in the options editor of the row.

A typical use is handing a share link to an external platform, for example copying it wrapped in the URL of a portal.

## How it works

* The plugin extends `ez5.CollectionShareLinkPlugin` and registers the class on `CollectionStorable.shareLinkPlugins`.
* The frontend creates one instance of the class each time the link of a row is rendered, with that row and its link.
* The buttons go into a button group of their own, apart from **Copy** and **Open**.
* While the link cannot be used yet, because the row is not active or has unsaved changes, the buttons are disabled and show the same tooltip as **Copy** and **Open**.
* Rows shared by email have no link, so they get no plugin buttons either.

## Methods to override

| Method | Default | Description |
| --- | --- | --- |
| `getButtons()` | `[]` | The buttons of the row. Each entry is either the options of a `CUI.Button` or a `CUI.Button` instance. |
| `isAvailable()` | `true` | Return `false` to leave the link of this row without the plugin's buttons. |
| `getGroup()` | `"share-plugins"` | The button group of the buttons that do not set a `group` of their own. |

## Context of the row

| Method | Returns |
| --- | --- |
| `getUrl()` | The share link, the same one **Copy** copies: `<base>/collection/<uuid>` plus the login parameters of the recipient. `<base>` is the share URL of the row's permission preset if it has one, otherwise the frontend's own address. |
| `getWho()` | The recipient of the row: `AclWhoCollection` for a link for external access, `AclWhoUser`, `AclWhoGroup`, ... |
| `getShareLinkProblem()` | `null` if the link can be used, otherwise the reason it cannot, as shown in the tooltip of the disabled buttons. |
| `getAclItem()` | The sharing row. |
| `getCollection()` | The collection. |

## Example

A button only for links for external access, which copies the link wrapped in the URL of an external portal:

```coffeescript
class MyCollectionShareLinkPlugin extends ez5.CollectionShareLinkPlugin

	isAvailable: ->
		@getWho() instanceof AclWhoCollection

	getButtons: ->
		[
			loca_key: "my.plugin.collection.share_link.portal.button"
			onClick: (ev, button) =>
				url = "https://portal.example.com/?fylr_collection=" + encodeURIComponent(@getUrl())
				ez5.copyToClipboard(url)
				Asset.showCopyTooltip(url, button, ev)
				return
		]

ez5.session_ready ->
	CollectionStorable.shareLinkPlugins.registerPlugin(MyCollectionShareLinkPlugin)
```

The loca key carries `|icon` and `|tooltip` and no `|text`, so the button is an icon like **Copy** and **Open**.

[fylr-plugin-example](https://github.com/programmfabrik/fylr-plugin-example) ships this example in `webfrontend/FylrExampleCollectionShareLinkPlugin.coffee`, with its loca keys in `l10n/example-loca.csv`.
