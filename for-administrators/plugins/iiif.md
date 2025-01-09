# IIIF

The **International Image Interoperability Framework (IIIF)** is a powerful standard for sharing, presenting, and analyzing high-resolution digital images. Fylr leverages IIIF to enhance image accessibility, interoperability, and customization, making it an ideal platform for institutions that handle digital collections. Below is an integrated overview combining Fylr's IIIF features with an explanation of IIIF server functionality.

FYLR supports the [Presentation API 3.0](https://iiif.io/api/presentation/3.0). The manifest is assembled automatically depending on the mask requested. You should use the [required statement](https://iiif.io/api/presentation/3.0/#requiredstatement) for copyright information and general information about your database.

***

### Introduction to IIIF Integration in Fylr

Fylr seamlessly supports IIIF, enabling users to create and share deep links to images in a standardized format compatible with any IIIF-compliant viewer. Its robust configuration options allow institutions to customize IIIF integration according to their needs, enhancing image sharing and accessibility.

#### Key Features in Fylr

1. **Preconfigured IIIF Access:**
   * Fylr eliminates the need for separate IIIF installation. Basic configuration and rights management activate its features.
2. **Deep Link Generation:**
   * **Manifest File Creation:** Users can export a `manifest.json` file, enabling images and metadata to be displayed in IIIF viewers.
   * **Built-in Mirador Viewer Integration:** Fylr includes an option to open IIIF manifests directly in the Mirador viewer online.
3. **Custom IIIF Viewer Support:**
   * Administrators can embed external IIIF viewers (e.g., Universal Viewer) by adding configurable HTML or URL links. This feature enables the sharing of tailored viewers or HTML code for external use.
4. **Flexible Configuration:**
   * Administrators can hide default IIIF links and replace them with custom options, giving institutions more control over the sharing experience.

These features empower institutions like libraries, archives, and museums to optimize their workflows for IIIF compatibility and customization.

***

### What is a IIIF Server?

A **IIIF server** delivers images according to IIIF standards, facilitating the sharing, presentation, and detailed analysis of high-resolution images online. IIIF servers are widely used in various fields, including libraries, archives, museums, and educational institutions, to enhance the accessibility and interactivity of digital collections.

#### Core Functions of a IIIF Server

1. **Image Delivery in Various Resolutions:**
   * A IIIF server dynamically delivers images in different sizes, crops, and resolutions without requiring multiple stored versions. Users can zoom into image details without loading the entire image in high resolution.
2. **Interoperability:**
   * Images served by a IIIF server can be integrated into diverse IIIF-compatible applications and tools, enabling unified viewing, comparison, and analysis of images from multiple sources.
3. **Metadata Enrichment:**
   * A IIIF server supports the inclusion of metadata alongside images, providing essential information like image content, copyright, and other contextual details.
4. **Annotation Support:**
   * IIIF allows users to annotate images, ranging from simple comments to intricate scientific observations.

***

### Applications of IIIF

* **Digital Libraries and Archives:** Institutions can share high-resolution scans of books, manuscripts, and other documents for research and public access.
* **Museums and Art Galleries:** Digitized artworks can be explored in detail, providing viewers an immersive experience.
* **Education:** Historical documents and teaching materials become interactive resources for learning and research.

***

### Conclusion

Fylr’s IIIF integration, combined with the functionality of a IIIF server, offers a powerful, flexible solution for managing and presenting digital images. Together, they enhance accessibility, interoperability, and customization, making them indispensable tools for digital image management in cultural, educational, and research institutions.
