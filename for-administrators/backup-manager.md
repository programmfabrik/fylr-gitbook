# Backup Manager

## Working with the Backup Manager

Backups are **sorted** chronologically with the **latest** backup at the **top**. To **create** a new backup, click on the **plus** button in the lower **left** and choose between the following **formats** in the next screen:

<table><thead><tr><th width="179.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>sqlite3</td><td>Plain text SQL to manually reimport into a sqlite3 database (gzipped).</td></tr><tr><td>postgres</td><td>Plain text SQL to manually reimport into a postgres database (gzipped).</td></tr><tr><td>sqlite3_db</td><td>Ready to use SQLite database file (a local fylr binary can startup using that db).</td></tr></tbody></table>

You can see that **status** of each backup in the backup **list**. By **clicking** on a **backup**, you can also access the **logs** to get details on the **status** or **error**. In the backup **detail**, you can also **download** the backup. To **remove** a backup, **click** on the desired **backup** and on the **minus** button in the lower **left**.
