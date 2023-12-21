---
description: >-
  In this section you can enable/disable various background services, like
  workflow emails, automatically recurring exports or the janitor who cleans up
  old data.
---

# Services

## E-Mail Notifications

This service sends emails such as welcome emails, collection share emails or emails triggered by workflows (if configured under "Tags & Workflows"). If not enabled, no emails will be send.

{% hint style="info" %}
Please make sure that you set up [emailing](email.md).
{% endhint %}



## Exporter

This service executes automated exports (if a schedule is defined for an export). If not enabled, scheduled exports will not be executed automatically.



## Custom-Data-Type Updater

This services automatically updates data stored in custom data type fields. For example: [GND](https://github.com/programmfabrik/easydb-custom-data-type-gnd), [Geonames](https://github.com/programmfabrik/easydb-custom-data-type-geonames) or [Getty](https://github.com/programmfabrik/easydb-custom-data-type-getty). If not enabled, the data that was copied into FYLR when linking to an external thesaurus will not be updated.

{% hint style="info" %}
For more configuration of each plugin, please see "Plugins".
{% endhint %}



## Documentation

### Activate /docs



### GitHub Token





## Janitor

This service regularly cleans up data.

### Active

Enable/Disable the Janitor.

### Remove Unused Files After n Days

Specify after how many days unused files should be deleted from the storage. Unused files are files that has been uploaded to FYLR but have never been linked to a record. Enter "0" to remove unused files with every janitor run (every 10 minutes).

{% hint style="danger" %}
Please note, this also applies to files which where uploaded but not yet been saved. We recommend to use at least an interval of 1 day.
{% endhint %}

### Settings For Users

#### Archive Inactive Users After n Days

Specify after how many days user accounts that have not logged in should be archived. Enter "0" to archive inactive users with every janitor run (every 10 minutes).

{% hint style="info" %}
Attention: archived users will not be able to log in. Archived users can be re-activated but their collections will be deleted when archiving the user account.
{% endhint %}

#### Types of Users To Be Archived

Specify the types of users that should be automatically archived after the above specified number or days.

#### Delete Archived Users After n Days

Specify after how many days archived user accounts should be deleted. Enter "0" to delete archived users with every janitor run (every 10 minutes).

{% hint style="info" %}
Attention: deleted users will be removed from the system and can't be re-activated. This also includes the users collections. See also "[User Management](user-management.md)".
{% endhint %}



### Settings For Events

Specify after how many days the events should be deleted. Enter "0" to delete the events with every janitor run (every 10 minutes).

#### Delete IP Address From Events After n Days

Specify after how many days the IP addresses of users should be deleted from the events. Enter "0" to delete the IP address with every janitor run (every 10 minutes).



