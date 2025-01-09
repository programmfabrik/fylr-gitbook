---
description: manage permanent storage locations
---

# Location Manager

<figure><img src="../.gitbook/assets/image (14) (1).png" alt=""><figcaption><p>How to reach the location manager in the black menu and an example view of the location manager</p></figcaption></figure>

## Working with the Location Manager

To **create** a new location, click on the **plus** button in the lower **left** and enter the details (see below). By **clicking** on a **location**, you can see and edit the details. To **remove** a location, **click** on the desired **location** and on the **minus** button in the lower **left**.

## Default storage locations

Click on the **settings** ![](<../.gitbook/assets/image (15).png>) icon in the lower **right** to configure the **default** storage locations.

This configures in which locations _new_ files will be stored.&#x20;

_Already existing_ files are still used in all locations, not only the default locations.

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

## Details

| OPTION            | DESCRIPTION                                                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                | an unique number for each location                                                                                                           |
| Status            | fylr tests the connection to the storage location and displays the result here                                                               |
| Prefix            | an optional path preceding each file, for example to separate from other data                                                                |
| Allow Purge       | when purging this fylr instance, shall the files also be deleted?                                                                            |
| Allow Redirect    | whether to hide S3 URLs behind fylr's own URL                                                                                                |
| Type              | Filesystem, S3 Bucket or Azure blob storage                                                                                                  |
| Directory         | Path, only for type Filesystem                                                                                                               |
| Access Key        | Credentials for type S3                                                                                                                      |
| Secret Key        | Credentials for type S3                                                                                                                      |
| Bucket Name       | Needed for type S3                                                                                                                           |
| Endpoint          | URL for type S3                                                                                                                              |
| Region            | For type S3, defined by your S3 provider                                                                                                     |
| SSL               | Whether to use https with S3                                                                                                                 |
| Account Name      | Credentials for Azure Blob storage                                                                                                           |
| Account Key       | Credentials for Azure Blob storage                                                                                                           |
| Endpoint Suffix   | For Azure Blob storage                                                                                                                       |
| Connection String | For Azure Blob storage, this is an _alternative_ to giving Account Name, Account Key and Endpoint Suffix separately. Do **not** give _both_. |
| Container         | For Azure Blob storage                                                                                                                       |

