---
description: >-
  How to setup up fylr to use Optical Character Recognition (OCR) to write the
  human-readable content of a pixel-based file into the index, thus making in
  searchable.
---

# Search in Text of Images or Office Files

{% hint style="warning" %}
Large files / large amount of files may temporarily slow down your instance due to increased processing requirements.&#x20;

Some OCR jobs may fail to produce correct output because of source quality (fonts, external artifacts, DPI).&#x20;

Special characters, pages structures and editorial features (tables, headers, footnotes etc.) are not filtered and may produce nonsensical contents.
{% endhint %}

By default, OCR is disabled for all files. This tutorial will expand on adding file types.

1. Navigate to [readme](../../../for-administrators/readme/ "mention"), into the [file-worker](../../../for-administrators/readme/file-worker/ "mention")
2. Uncheck "Use Default Settings"
3. Expand "CUSTOM METADATA"
4. Add the extensions you want OCR applied to and written to the index

<figure><img src="../../../.gitbook/assets/Screenshot 2025-04-17 at 14.38.40.png" alt="" width="563"><figcaption><p>Example configuration of OCR to include JP(E)G, PNG, EPUB, PDF</p></figcaption></figure>

The recipe configuration offers more options, those are not necessarily required to run OCR on new files.

### Verify OCR is Working

* Create a new record using the plus-icon
* As soon as you save, the OCR is beginning
* Locate the newly created record and open in detail view



<figure><img src="../../../.gitbook/assets/Screenshot 2025-04-17 at 14.10.27.png" alt=""><figcaption><p>fylr detail view of example record</p></figcaption></figure>

* Use the "Info" button to access the data available in index
* In the "Advanced" tab, you will find the indexed content of the file under "\_fulltext"

<figure><img src="../../../.gitbook/assets/Screenshot 2025-04-17 at 14.15.26.png" alt=""><figcaption><p>Info section of a fylr record displaying the indexed OCR output</p></figcaption></figure>



To search for the extracted content, make sure that the OCR-recognizable text of your files is included in the search result by activating the checkbox in the 3-dot menu on the far right of the search bar.

<figure><img src="../../../.gitbook/assets/Screenshot 2025-04-17 at 14.19.04.png" alt=""><figcaption></figcaption></figure>



Now you can find records by searching the human readable content of files - just type in the search bar as usual.

### Applying OCR on Already Existing Records

OCR image-to-text will run when indexing a file. Consult [regenerating-preview-images.md](regenerating-preview-images.md "mention") for a tutorial on how to reindex one or more existing records.&#x20;

