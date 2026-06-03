# /api/system/sendmail/test

Sends a test email to a single `to` address to verify the mail
configuration. Each send writes an `EMAIL_SENT` or `EMAIL_SENT_FAILED`
event. Requires `system.sendmail` (or `system.root`).

Differs from easydb 5: the dedicated `system.sendmail` right grants this
operation. In easydb 5 the equivalent `POST /api/v1/settings/sendmail`
required "an authenticated session with the `system.root` privilege".

### `POST /system/sendmail/test` — This endpoint sends a test email to one mail address. The user needs the `system.sendmail` or `system.root` system right. After sending an email `EMAIL_SENT` or `EMAIL_SENT_FAILED` event is written.
{% swagger src="../fylr-openapi.yml" path="/system/sendmail/test" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
