---
description: >-
  How to setup up fylr to use Optical Character Recognition (OCR) to write the
  human-readable contents of a pixel-based file into the index, thus making in
  searchable.
---

# Search Text in images or office files

{% hint style="warning" %}
Large files / large amount of files may temporarily slow down your instance due to increased processing requirements.&#x20;

Some OCR jobs may fail to produce correct output because of source quality (fonts, external artifacts, DPI).&#x20;

Special characters, pages structures and editorial features (tables, headers, footnotes etc.) are not filtered and may produce nonsensical contents.
{% endhint %}

By default, OCR is only applied to PDF files. This Tutorial will expand on adding other file types besides PDF.

1. navigate to [readme](../../../for-administrators/readme/ "mention"), into the [file-worker](../../../for-administrators/readme/file-worker/ "mention")
2. Uncheck "Use Default Settings"
3. Expand "CUSTOM METADATA"
4. You will find the OCR Recipe configured to only write PDFs file contents to the index
5. Add the extensions you want OCR applied to and written to the index

<figure><img src="../../../.gitbook/assets/Screenshot 2025-04-17 at 14.38.40.png" alt="" width="563"><figcaption><p>Example configuration of OCR to include JP(E)G, PNG, EPUBS</p></figcaption></figure>

The recipe configuration offers more options, those are not necessarily required to run OCR on new files.

### Asserting OCR output is indexed

* Create a new record using the plus-icon
* As soon as you save, the OCR is beginning
* Locate the newly created record and open in detail view



<figure><img src="../../../.gitbook/assets/Screenshot 2025-04-17 at 14.10.27.png" alt=""><figcaption><p>fylr detail view of example record</p></figcaption></figure>

* use the highlighted Info section to access the data available in index
* in the "advanced" tab, you will find the indexed contents of the image under "\_fulltext"

<figure><img src="../../../.gitbook/assets/Screenshot 2025-04-17 at 14.15.26.png" alt=""><figcaption><p>Info section of a fylr record displaying the indexed OCR output</p></figcaption></figure>

To leverage OCR in the fylr search, make sure include the textual contents of your files in the search result by enabling the checkbox inside the menu at the far right end of the searchbar.

<figure><img src="../../../.gitbook/assets/Screenshot 2025-04-17 at 14.19.04.png" alt=""><figcaption></figcaption></figure>



Now you can find records by searching the human readable contents of files - just type in the search bar as usual.



