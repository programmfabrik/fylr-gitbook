---
description: Tutorial on how to get images from a fylr into a google document
---

# Use fylr in Google docs via CI HUB

## Required

* Login to a fylr instance with permission to see at least on image asset.
* This fylr needs to have CI HUB in its fylr license.

## Steps

1. Open a Google document on [https://docs.google.com](https://docs.google.com)
2. Open the `Extensions` menu and `Get Extensions`
3. There, search for `CI HUB` and click `install`.
4. In the `Extensions` menu again, then `CI HUB Connector` and `Open`. <img src="../.gitbook/assets/image.png" alt="" data-size="original">
5.  In the appearing panel (right hand side of the document) Login or Register for a free trial with CI HUB.&#x20;

    <figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
6. In the CI HUB side panel, search for fylr and click the plus button (marked in green below):![](<../.gitbook/assets/image (16).png>)
7.  Choose ANY\* fylr URL (where you have a login) and click Login:

    (\*=There may be a few fylrs that do not have the OAuth client ci-hub configured, but it is configured by default)
8. Log in to the appearing fylr login dialog with your fylr credentials.
9. Go back to the Google doc. In the side panel e.g. click on the magnifying glass
10. Click on the magnifying class below the first one, to search for any asset in fylr.
11. Click on one preview once, then click on it a _2nd time_ and **drag** it into your document.

Wait a few seconds for the transfer. (There is a spinning circle in the preview as long as CI HUB is working on it.)

### Known errors

* After clicking `Login` in Step 6:\
  <mark style="color:red;">Authorization failed</mark>\ <mark style="color:red;">Sorry, an unexpected error ocurred:</mark>\ <mark style="color:red;">TypeError: Cannot destructure property 'systemUrl' of '(intermediate value)' as it is undefined.</mark>\
  When trying again a few minutes later, it worked.
* when dragging an image from the CI HUB panel into the document:\
  <mark style="color:red;">Error: executePanelCommand failed: Exception: The image in the BlobSource could not be retrieved. Please make sure the image is valid.</mark>\
  Seems to be a kind of timeout with bigger images. Did work when I tried it the 2nd time.

## References

CI HUB official User Guide: [https://ci-hub.com/hubfs/CI%20HUB%20Connector%20User%20Guide%20v1.1.pdf](https://ci-hub.com/hubfs/CI%20HUB%20Connector%20User%20Guide%20v1.1.pdf)
