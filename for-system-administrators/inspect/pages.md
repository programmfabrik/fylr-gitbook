---
description: The /inspect/pages tool — render page and email templates, and send a test email.
---

# Pages

The **Pages** page (`/inspect/pages/`) renders fylr's HTML page and email templates with sample data, so you can preview how a rendered login page, notification or email will look.

## Actions

* **`/inspect/pages/page/<template>`** and **`/inspect/pages/email/<template>`** render a page / email template.
* **`/inspect/pages/sendmail`** actually **sends** an email through the configured mail server — a live send, use it to verify email delivery end to end.

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
