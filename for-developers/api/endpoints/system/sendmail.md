# /api/v1/system/sendmail

Sends an email through the fylr server's mail infrastructure, composed as
a multipart message with separate HTML and text bodies and optional
attachments. Each send writes an `EMAIL_SENT` or `EMAIL_SENT_FAILED` event.
Requires `system.sendmail` (or `system.root`).

### `POST /system/sendmail` — This endpoint sends an mail using the fylr server infrastructure. The mail is composed as multipart mail with separate HTML and text bodies. The user needs the `system.sendmail` or `system.root` system right. After sending an email `EMAIL_SENT` or `EMAIL_SENT_FAILED` event is written.
{% swagger src="../fylr-openapi.yml" path="/system/sendmail" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
