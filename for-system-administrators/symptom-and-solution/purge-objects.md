# Purge objects

**fylr** cannot currently actually purge objects from database. All objects are stored in historic versions, also deleted objects are kept in the database with a flag deleted. These objects can be linked to files. Those files are not deleted by the file janitor as **fylr** considers them to be _in use._

This article describes a method to purge objects using SQL access to the fylr database. After the purge of objects, the file janitor will acknowledge the deleted file links and eventually remote the files and free disk space.

{% hint style="info" %}
Make sure to have a **backup before** using this procedure. This is a very dangerous tool and can easily lead to data loss. The SQL here is provided as is, with **no warranty and responsibility.**

**Use at your own risk!**
{% endhint %}

The simple form of the deleting command looks like this:

<pre class="language-sql"><code class="lang-sql"><strong>BEGIN;
</strong><strong>DELETE FROM "object" WHERE "system_object_id" IN (
</strong>  SELECT "system_object_id" 
    FROM "object" WHERE "latest_version" AND "deleted_at" IS NOT NULL
);
ROLLBACK;
</code></pre>

In case the above throws a foreign key violation, you need to remove links to existing objects first.

```sql
BEGIN;
-- DELETE links to objects to be deleted
DELETE FROM "value" WHERE "linked_system_object_id" IN (
   SELECT "system_object_id" 
     FROM "object" WHERE "latest_version" AND "deleted_at" IS NOT NULL
);
-- DELETE objects in all versions where the latest object is deleted
DELETE FROM "object" WHERE "system_object_id" IN (
  SELECT "system_object_id" 
    FROM "object" WHERE "latest_version" AND "deleted_at" IS NOT NULL
);
ROLLBACK;
```

You need to replace the `ROLLBACK` with  `COMMIT` to really put this into effect.

The `WHERE` clauses can be changed here, to limit the delete run to certain pools (`pool_id`) or object types (`table_api_id`).

After you are done make sure to do a re-index using `/inspect/system`.
