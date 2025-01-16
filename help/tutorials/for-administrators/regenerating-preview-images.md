---
description: How to regenerate versions for a particular image.
---

# Regenerating preview images

If you need to regenerate versions created in the Fylr [file-worker](../../../for-administrators/readme/file-worker/ "mention")  for a given asset (or many assets), follow these steps:

{% hint style="info" %}
To use Fylrs inspect mode, you need root access!
{% endhint %}

## A single file

In an assets detail view, open the "info" panel and in the "general" tab follow the link to `/inspect/files`  (next to your assets ID)

<figure><img src="../../../.gitbook/assets/Screenshot 2024-12-17 at 16.32.00.png" alt=""><figcaption></figcaption></figure>

1. select the file you want to regenerate versions for - mostly you want to use the original as the source for generated versions
2. select the action that suits your needs, often a basic resync will suffice
3. confirm the the action

{% hint style="info" %}
Hover the select options for more detail on what an action produces
{% endhint %}

<figure><img src="../../../.gitbook/assets/Screenshot 2024-12-17 at 16.34.18.png" alt=""><figcaption></figcaption></figure>

Now new versions will be generated. To confirm the creation look in the detail view where we started the process and find your newly created versions.



## Multiple files&#x20;

1. open the `/inspect/files` page of your Fylr instance
2. use the search and the filters to find the versions you want to regenerate versions for&#x20;
3. either select all on page, the entire search result or select the files you need
   1. when selecting a child version (any version that's not the original file), the action will regenerate all versions based on the original file.
4. select the action that suits your needs, often a basic resync will suffice
5. confirm the the action

Depending on the number of selected files the resync can take some time. To confirm the successful generation of new versions find a record in the Fylr frontend and inspect the versions in the details Info tab. Alternatively inspect the detailed logs in the Fylr console located at the URL `/your-instance.com/inspect/system/console` .



