---
description: The /inspect/license tool — license info, validation, and the expiration-mail simulator.
---

# License

The **License** page (`/inspect/license/`) shows the installed license and lets you simulate its lifecycle.

## What it shows

The license's edition, its validity dates, the **grace-to** date (end date + the two-month grace), and the enabled capabilities.

## Simulate

* **`/inspect/license/simulate/`** renders the expiration warning mails at a chosen point in time, so you can preview what administrators will receive — _paid-period-ending_, _grace-period-ending_, _license-expired_, _binary-too-new_ — without waiting for the real dates.
* **`/inspect/license/validate`** returns the validation as JSON; passing `now` / `valid_to` overrides evaluates the license at a simulated time. With `send=1` it actually sends the reminder mail.

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
* [License management](../../license-management.md) — the licensing model and the warning schedule.
