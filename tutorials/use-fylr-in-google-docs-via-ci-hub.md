---
description: Tutorial on how to get images from a fylr instance into a google document
---

# Use fylr in Google docs via CI HUB

## Required

* Login to a fylr instance with permission to see some media content
  * This fylr needs to have the CI HUB capability in its fylr license. This is not part of all fylr licenses.
  * By default all fylr installations have the "OAuth client" named "ci-hub" configured, so this should not be an issue. However, during a fylr installation, this _could_ theoretically be changed. If you have problems to connect CI HUB to fylr, consult the instances administrator.

## Setup

1. Open a Google document on [https://docs.google.com](https://docs.google.com)
2. Open the `Extensions` menu and select `Get Add-ons`.
3. In this new dialog, search for `CI HUB` and install it. This will then happen automatically inside Google docs and not on your computer's local storage.
4. In the `Extensions` menu again, select `CI HUB Connector` and `Open`:<img src="../.gitbook/assets/image (2).png" alt="" data-size="original">
5.  In the appearing panel (right hand side of the document) `Login` either with an existing CI HUB ID or `Register` for a free trial with CI HUB:&#x20;

    <figure><img src="../.gitbook/assets/image (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
6. After you logged in with your CI HUB ID, the side panel should change (you may have to re-open it).&#x20;
7.  In the CI HUB side panel, search for `fylr` and click the plus button (marked in green below):

    <figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>
8. Enter any fylr URL (where you have a login) and click `Login`: ![](<../.gitbook/assets/image (1) (1) (2).png>)
9. Log in to the appearing fylr login dialog with your _fylr_ credentials.
10. Go back to the Google document. In the side panel e.g. click on the magnifying glass.
11. Then  click on the magnifying class _below the first one_, to search for any asset in fylr. Both magnifying glasses are marked in green here:&#x20;

    <figure><img src="../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
12. If nothing is found, you may have to choose an Object Type in the drop down menu `Object Type`.
13. Click on one preview image once, then click on it a _2nd time_ and **drag** it into your document before releasing the click.

Wait a few seconds for the transfer. (There is a spinning circle in the preview as long as CI HUB is working on it.)

### Known errors

* After clicking `Login` in Step 8:\
  <mark style="color:red;">`Authorization failed`</mark> \
  <mark style="color:red;">`Sorry, an unexpected error ocurred:`</mark> \
  <mark style="color:red;">`TypeError: Cannot destructure property 'systemUrl' of '(intermediate value)' as it is undefined.`</mark>\
  \
  **When trying again a few minutes later, it worked.**



* When dragging an image from the CI HUB panel into the document:\
  <mark style="color:red;">`Error: executePanelCommand failed: Exception: The image in the BlobSource could not be retrieved. Please make sure the image is valid.`</mark>\
  \
  Seems to be a kind of timeout with bigger images. **Did work when I tried it the 2nd time.**

## References

CI HUB official User Guide: [https://ci-hub.com/hubfs/CI%20HUB%20Connector%20User%20Guide%20v1.1.pdf](https://ci-hub.com/hubfs/CI%20HUB%20Connector%20User%20Guide%20v1.1.pdf)
