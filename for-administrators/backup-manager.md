---
description: Create and download copies of your data, to supplement bug reports.
---

# Backup Manager

{% hint style="danger" %}
Please note, that the copies here only include SQL data. Asset files are not included. For a full backup, that can be restored in case of emergency, please [follow this routine](../for-system-administrators/backup.md).
{% endhint %}

## Working with the Backup Manager

Backups are **sorted** chronologically with the **latest** backup at the **top**. To **create** a new backup, click on the **plus** button in the lower **left** and choose between the following **formats** in the next screen:

<table><thead><tr><th width="179.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>sqlite3</td><td>Plain text SQL to manually reimport into a sqlite3 database (gzipped).</td></tr><tr><td>postgres</td><td>Plain text SQL to manually reimport into a postgres database (gzipped).</td></tr><tr><td>sqlite3_db</td><td>Ready to use SQLite database file (a local FYLR binary can startup using that db).</td></tr></tbody></table>

You can see that **status** of each backup in the backup **list**. By **clicking** on a **backup**, you can also access the **logs** to get details on the **status** or **error**. In the backup **detail**, you can also **download** the backup. To **remove** a backup, **click** on the desired **backup** and on the **minus** button in the lower **left**.

## Typical workflow

1. You notice a problem and report it to the developer, e.g. support@programmfabrik.de
2. In response you are asked to supply a copy of your data(base)
3. in the backup manager, you click the plus button to create a fresh copy
4. you select and download this copy
5. you upload the copy to the developer via their ticket system or other means

## Restore

Typically, we, the developer, restore such a copy, to analyze your problem. Just in case that you want to use it yourself, here a few hints:

{% hint style="info" %}
Please note, that these backups cannot be restored in the FYLR frontend.
{% endhint %}

If you restore a copy in the postgres format, the postgres user needs superuser privileges. This is unusual but O.K. because this is part of debugging and development, not production use.\
\
For a full backup in production, that can be restored in case of emergency, please [follow this routine](../for-system-administrators/backup.md).
