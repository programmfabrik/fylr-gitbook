---
description: >-
  How to publish records over OAI/PMH: switch the interface on, give the system
  user oai_pmh read rights, offer your own formats and sets, and check what a
  harvester gets.
---

# Setting up OAI/PMH

OAI/PMH lets other services, so-called harvesters, collect the metadata of your records. In fylr it takes three things:

1. the interface switched on in the base configuration,
2. read rights for the system user `oai_pmh`, because harvesters get exactly what this user may see,
3. the formats and sets you want to offer.

This tutorial goes through them in that order and ends with the requests a harvester sends. The settings themselves are described in [Export & Deep Links](../../../for-administrators/readme/export-and-deep-links.md#oai-pmh), the interface in [OAI/PMH](../../../for-administrators/oai.md).

## 1. Switch the interface on

1. In the **Base Configuration**, open **Export & Deep Links** and go to **OAI/PMH**.
2. Check **Enabled**.
3. Fill in **Repository Name** and at least one **Administrator Email**. Harvesters see both in the answer to `Identify`, and the OAI/PMH standard expects an email address.
4. Optionally, enter a **Namespace**, for example `museum`. The identifiers of your records then read `oai:museum:<uuid>`, without a namespace `oai:<uuid>`.
5. Save.

The interface is now reachable at `https://<your-fylr>/api/v1/oai`. Open

```
https://<your-fylr>/api/v1/oai?verb=Identify
```

It answers with the repository name. As long as the interface is off, every request answers with the error "The OAI/PMH endpoint is not enabled."

## 2. Give the system user `oai_pmh` read rights

Harvesters do not log in. fylr answers them as the system user `oai_pmh`, so they get the records this user may see, and nothing else. Without rights, every harvest comes back empty.

In **Rights Management**, open the pool that holds the records, or the objecttype for objecttypes without pools, and go to the tab **Permissions**. Add the user `oai_pmh` and grant:

* **View Records**, with the objecttypes you want to publish.
* **Allowed Masks**: for each of these objecttypes, the masks whose fields harvesters may get. Without an allowed mask, `oai_pmh` sees no record of that objecttype.
* **View Pool**, if harvesters should be able to harvest the pool as a set.

Save, then open

```
https://<your-fylr>/api/v1/oai?verb=ListIdentifiers&metadataPrefix=oai_dc
```

It lists the identifiers of the records `oai_pmh` may see. Records missing here are missing for every harvester.

{% hint style="info" %}
Open these URLs without an `access_token`. A request that carries a token is answered with the rights of the token's user, not with those of `oai_pmh`, and shows more than a harvester gets.
{% endhint %}

## 3. Choose the metadata formats

Each request names exactly one format with the argument `metadataPrefix`. fylr offers:

| `metadataPrefix` | Content |
| ---------------- | ------- |
| `oai_dc` | Dublin Core, always offered. It is filled by the [Dublin Core profile](../../../for-administrators/oai.md#dublin-core) of the objecttype. Without a profile, each record only carries its UUID and the title "NO OAI-DC PROFILE CONFIGURED". |
| `easydb` | The record as fylr XML. From fylr 6.35.0 it can be switched off with **Offer metadataPrefix "easydb"**. |
| `xslt-<Name>` | A format of your own, made by an XSLT, for example LIDO. |

To offer a format of your own:

1. In **Export & Deep Links**, go to **XSL Transformations** and add a row.
2. **XSLT File**: upload the stylesheet. Its output has to be XML.
3. **Name**: a short technical name of letters, digits, `-` and `_`, for example `lido`. Harvesters request the format as `xslt-lido`; the name is case-sensitive. A row without a name is offered as just `xslt-`.
4. Check **Use for OAI/PMH**.
5. **XPath Query**: only needed if the XSLT wraps all records in one element, as LIDO does with `lido:lidoWrap`. Enter the XPath of the elements that hold one record each, with their namespace prefix, for example `lido:lidoWrap/lido:lido`. See [XPath Query](../../../for-administrators/readme/export-and-deep-links.md#xpath-query).
6. Optionally, enter **Namespace** and **Schema** of the format. Harvesters see them in `ListMetadataFormats`.
7. Save, then open

   ```
   https://<your-fylr>/api/v1/oai?verb=ListMetadataFormats
   ```

   It lists `xslt-lido` next to `oai_dc` and `easydb`.

{% hint style="info" %}
The **Display Name** of the row is only shown in the export dialog. Harvesters use the **Name**.
{% endhint %}

## 4. Offer sets (optional)

A harvester can limit a harvest to a set with the argument `set`. fylr offers these sets by itself, following the rights of `oai_pmh`:

| Set | `setSpec` |
| --- | --------- |
| An objecttype | `objecttype:<objecttype>` |
| A pool, with all its subpools | `pool:<id>:<id>:…`, the ids of the whole path from the root pool |
| An objecttype in a pool | `objecttype:<objecttype>:pool:<id>:<id>:…` |
| A collection | `collection:<id>` |

Sets of your own are made with tags. In **OAI/PMH**, under **Tag-Sets**, add a row with a **Set Name**, for example `published`, and a **Tag Filter**. The set holds the records that match the tag filter and that `oai_pmh` may see. Harvesters request it as `set=tagset:published`.

Open

```
https://<your-fylr>/api/v1/oai?verb=ListSets
```

From fylr 6.35.0, it lists every set that has at least one record for `oai_pmh`; before, it listed empty sets too. Request a set exactly as `ListSets` spells it, prefix included: `set=tagset:published`, not `set=published`. From fylr 6.35.0, a set spelled any other way answers `badArgument`.

## 5. Check what a harvester gets

These requests show what a harvester gets. Put `https://<your-fylr>/api/v1/oai` in front of each.

| Request | Answer |
| ------- | ------ |
| `?verb=Identify` | Repository name and administrator email. |
| `?verb=ListMetadataFormats` | The formats on offer. |
| `?verb=ListSets` | The sets with records. |
| `?verb=ListRecords&metadataPrefix=xslt-lido` | All records in your format. |
| `?verb=ListRecords&metadataPrefix=xslt-lido&set=tagset:published` | The records of one set in your format. |
| `?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:museum:<uuid>` | One record. |

`ListRecords` answers in pages of **Maximum Number of Records for ListRecords** (100 unless set otherwise). A page that is not the last one ends with a `resumptionToken`; the harvester sends `?verb=ListRecords&resumptionToken=<token>` for the next page.

## Troubleshooting

| What you see | What to do |
| ------------ | ---------- |
| An empty `ListRecords`, or fewer records than expected | Grant `oai_pmh` **View Records** and **Allowed Masks** for the records, see step 2. |
| `ListMetadataFormats` shows `xslt-` without a name | Enter a **Name** in the row of the XSLT, see step 3. |
| `cannotDisseminateFormat` | The `metadataPrefix` is not on offer: check its spelling against `ListMetadataFormats`, and that **Use for OAI/PMH** is checked. |
| `badArgument` for a set | Spell the set as `ListSets` does, with its prefix, for example `tagset:published`. |
| `badArgument` with "metadataPrefix missing" | `ListRecords` and `GetRecord` need a `metadataPrefix`. |
| The format you asked for is ignored | The format is chosen with `metadataPrefix` alone. fylr ignores arguments it does not know, such as `metadataFormat`. |
| `ListRecords` with your format answers with an internal error | The XSLT does not write XML, or the **XPath Query** does not find exactly one element per record. |
