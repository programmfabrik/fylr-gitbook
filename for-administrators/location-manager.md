---
description: manage permanent storage locations
---

# Location Manager

<figure><img src="../.gitbook/assets/image (14) (1).png" alt=""><figcaption><p>How to reach the location manager in the black menu and an example view of the location manager</p></figcaption></figure>

## Working with the Location Manager

To **create** a new location, click on the **plus** button in the lower **left** and enter the details (see below). By **clicking** on a **location**, you can see and edit the details. To **remove** a location, **click** on the desired **location** and on the **minus** button in the lower **left**.

## Default storage locations

Click on the **settings** ![](<../.gitbook/assets/image (15).png>) icon in the lower **right** to configure the **default** storage locations.

This configures in which locations _new_ files will be stored. Locations marked as read-only cannot be used here.

_Already existing_ files are still used in all locations, not only the default locations.

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

## Connection status

fylr tests the connection to each storage location and shows the result in the **Status** column of the list, and in the location's detail form. `connected` is the working state. `error` means the location could not be reached, and the message shown next to it is the reason the storage reported — a bucket that does not exist, credentials that are refused, a directory that cannot be created. The same status and message are shown for every location under `/inspect/system/locations/`.

**From version 6.35.0**, a location that is not `connected` is retried in the background, every 5 to 30 seconds, for as long as it stays unreachable, and fylr writes a line to its log when the location recovers. A location that was simply not available yet when fylr started — an S3 bucket, or the user fylr authenticates as, being created moments after the instance — therefore turns `connected` on its own. Before 6.35.0 such a location stayed in `error` until the instance was restarted or somebody saved the location again, and every file written to it failed in the meantime.

## Details

| OPTION            | DESCRIPTION                                                                                                                                                                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                | an unique number for each location                                                                                                                                                                                                                                        |
| Status            | the connection state of the storage location, see [#connection-status](location-manager.md#connection-status)                                                                                                                                                             |
| Prefix            | an optional path preceding each file, for example to separate from other data                                                                                                                                                                                             |
| Allow Purge       | when purging this fylr instance, shall the files also be deleted?                                                                                                                                                                                                         |
| Allow Redirect    | whether to hide S3 URLs behind fylr's own URL                                                                                                                                                                                                                             |
| Read Only         | Prevents changes made by fylr. Can not be set for locations that are currently configured as Default Storage Locations.                                                                                                                                                   |
| Type              | Filesystem, S3 Bucket or Azure blob storage                                                                                                                                                                                                                               |
| Directory         | A path - only for type `Filesystem`. Either an absolute path on the system visible to fylr (might be in a container); or a path relative to the fylr executable (e.g. in a container, it is relative to `/fylr/bin/`, which is not recommended, so use an absolute path). |
| Access Key        | Credentials for type S3                                                                                                                                                                                                                                                   |
| Secret Key        | Credentials for type S3                                                                                                                                                                                                                                                   |
| Bucket Name       | Needed for type S3                                                                                                                                                                                                                                                        |
| Endpoint          | URL for type S3                                                                                                                                                                                                                                                           |
| Region            | For type S3, defined by your S3 provider                                                                                                                                                                                                                                  |
| SSL               | Whether to use https with S3                                                                                                                                                                                                                                              |
| Account Name      | Credentials for Azure Blob storage                                                                                                                                                                                                                                        |
| Account Key       | Credentials for Azure Blob storage                                                                                                                                                                                                                                        |
| Endpoint Suffix   | For Azure Blob storage                                                                                                                                                                                                                                                    |
| Connection String | For Azure Blob storage, this is an _alternative_ to giving Account Name, Account Key and Endpoint Suffix separately. Do **not** give _both_.                                                                                                                              |
| Container         | For Azure Blob storage                                                                                                                                                                                                                                                    |

