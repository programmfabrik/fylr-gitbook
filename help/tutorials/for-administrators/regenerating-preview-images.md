---
description: How to regenerate versions for a particular image.
---

# Regenerating preview images

If you need to regenerate versions created in the Fylr [file-worker](../../../for-administrators/readme/file-worker/ "mention") for a given asset (or many assets), follow these steps:

{% hint style="info" %}
* To use Fylrs inspect mode root access is required
* **Hover the individual actions** for more information on the action
{% endhint %}

## A single file

In an assets detail view, open the "info" panel and in the "general" tab follow the link to `/inspect/files` (next to your assets ID)

<figure><img src="../../../.gitbook/assets/Screenshot 2024-12-17 at 16.32.00.png" alt=""><figcaption></figcaption></figure>

1. select the file you want to regenerate versions for - mostly you want to use the original as the source for generated versions
2. select the action that suits your needs, often a basic resync will suffice
3. confirm the the action

{% hint style="info" %}
Hover the select options for more detail on what an action produces
{% endhint %}

<figure><img src="../../../.gitbook/assets/Screenshot 2024-12-17 at 16.34.18.png" alt=""><figcaption></figcaption></figure>

Now new versions will be generated. To confirm the creation look in the detail view where we started the process and find your newly created versions.

## Multiple files

#### Generating a newly created rendition for existing records

After adding a new rendition to the fileworker, the new rendition is not produced automatically and will be generated for each new file uploaded to the instance.

To produce the new rendition for existing records, follow this list:

1. open the `/inspect/files` page of your Fylr instance
2. apply a class filter to only target files of the newly created renditions file class
3. use the  `Version` select to filter only for original files.  select only `Parents`  to only show originals and not the existing renditions.
4. Refresh the result list by clicking `search`  (list should show only Originals now)&#x20;
5. either select all on page, the entire search result or select the files you need
6. select action `resync`  to generate missing renditions for the selected files
7. confirm the the action

#### Generating renditions for all files

If renditions turn out erroneous it's best to produce a new set versions using the action `produce versions` . **This will produce versions for all selected files**.&#x20;



***

&#x20;

Depending on the number of selected files the resync can take some time. To confirm the successful generation of new versions find a record in the Fylr frontend and inspect the versions in the details Info tab.&#x20;

Alternatively inspect the detailed logs in the Fylr console located at the URL `<fylr url>/inspect/system/console` .
