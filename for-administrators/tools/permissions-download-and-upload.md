---
description: >-
  Download and upload a JSON file to transfer groups, tags, workflows, object
  type permissions, pool permissions and presets from one FYLR to another.
---

# Permissions Download & Upload

{% hint style="info" %}
This feature is a plugin called "[easydb-basemigration-plugin](https://github.com/programmfabrik/easydb-basemigration-plugin)". It's activated by default. If you don't see this feature in the menu, please make sure to have it enabled in the plugin manager.
{% endhint %}



| OPTION   | DESCRIPTION                                                                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------------------- |
| Download | Downloads a JSON file that contains all groups, tags, workflows, object type permissions, pool permissions and presets. |
| Upload   | Upload the JSON file and transfer the permissions to the instance in the next screen.                                   |

The screen consists of 3 parts:

* **Source** - choose what you want to transfer
* **Settings** - additional settings for the transfer
* **Protocol** - a protocol / log of the transfer

{% hint style="info" %}
Please note: you have to hit "Transfer" before clicking on the next source or closing the dialogue.&#x20;
{% endhint %}



We recommend to transfer the sources top to bottom as some of them depend on each other. For example, you can't transfer permissions for object types when you haven't transferred the groups first.

For most cases you can choose between "Replace" and "Add". "Replace" will for example overwrite all groups in the target FYLR, whereas "Add" would add all new groups to the existing groups in the target FYLR.



## Groups

Click on "Groups" to transfer all groups (system groups and own groups). Own groups can be added or replaced, system groups will only be updated. Choose if you want to transfer permissions and/or system rights as well. Open "Groups" if you want to transfer only all system groups or only all own groups. Dive deeper to transfer only single groups from the source.

## Tags

Click on "Tags" to transfer all tag groups with their tags. Choose if you want to transfer tag permissions as well. Open "Tags" if you want to transfer only single tag groups with their tags.

## Workflows

Click on "Workflows" to replace or add all workflows.&#x20;

## Object Types

Click on "Object Types" to replace or add all object type permissions. Open "Object Types" if you want to transfer only permissions of single object types from the source.

{% hint style="info" %}
Please note: all other object type settings can't be transferred at the moment and have to be set manually.
{% endhint %}

## Pools

Open "Pools" and select a pool from the source and one for the target to replace or add permissions of a pool. Source and target pool don't have to be the same, meaning you can transfer the permissions from one pool to a different pool.&#x20;

{% hint style="info" %}
Please note: pools itself can't be transferred and have to be created manually before transferring the settings & permissions.
{% endhint %}

## Presets

Click on "Presets" to replace or add all record and collection presets. Open "Presets" if you want to transfer only all record presets or only all collection presets. Dive deeper to transfer only single presets from the source.

