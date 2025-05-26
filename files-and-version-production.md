---
description: >-
  This page gives a overview over the file handling and file version production
  in fylr. Different file states and actions are explained in a how-to for the
  /inspect/files page.
---

# Files and version production

{% hint style="warning" %}
This page is a work in progress and not complete.
{% endhint %}

## `/inspect/files` page

Open `<fylr url>/inspect/files`. The page shows a list of all files and their children. For each original file which has been uploaded, or is inserted via URL, children are calculated in the background. The number of children depends on recipes which are triggered by file types and other file meta data. Each original and child file has different states which show what is done in the background, and also give information about errors.

## File States

Changes between different states are done in order. Internal states ("Status") are grouped into API states ("Status API").

<table><thead><tr><th width="70" align="center">Step</th><th width="326">Status</th><th>Status API</th><th>Description</th></tr></thead><tbody><tr><td align="center">1</td><td><code>pending</code></td><td><code>pending</code></td><td>The file is in the queue, but has not yet been picked up by any file worker</td></tr><tr><td align="center">2</td><td><p><code>processing</code></p><p><code>pending_produce_internal</code></p><p><code>pending_manual_produce_internal</code></p><p><code>pending_original_produce_internal</code></p><p><code>pending_metadata_internal</code></p></td><td><code>processing</code></td><td>A worker is processing the file. </td></tr><tr><td align="center">3</td><td><p><code>sync</code></p><p><code>pending_copy_internal</code></p><p><code>pending_move_internal</code></p><p><code>pending_checksum</code></p></td><td><code>sync</code></td><td><p>Processing of the file in file workers is done. Further information are still calculated for the database.</p><p></p><p>Files in states <code>sync</code> and <code>pending_checksum</code> can already be exported.</p></td></tr><tr><td align="center">4</td><td><code>done</code></td><td><code>done</code></td><td><p>The file and all children have been successfully converted.</p><p></p><p>Files in this state can be exported.</p></td></tr><tr><td align="center">4</td><td><code>error</code></td><td><code>failed</code></td><td>There was an error during conversion. See <a data-mention href="files-and-version-production.md#errors-and-solutions">#errors-and-solutions</a> for more information and possible solutions.</td></tr></tbody></table>

## File Actions

## File Queue

## File Locations

## Errors and solutions
