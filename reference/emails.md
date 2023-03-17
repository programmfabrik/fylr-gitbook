# Emails

## Template Functions

### LocaHTML *KEY*

Gets *KEY* from loca for the current user's frontend language. Expects the key to be HTML.

### LocaText *KEY*

Gets *KEY* from loca for the current user's frontend language. Expects the key to be regular text.

### LocaData *LocaValue*

Gets the best loca for the current user's database languages. *LocaValue* is a map with localized values.

### LocaFrontend *LocaValue*

Gets the best loca for the current user's frontend language. *LocaValue* is a map with localized values.


## transition_reject, transition_resolve


### To

The email is sent to the the transition configured recipient of the email. For groups, the emails of all users in that group are used.

### Attachments

This email attaches the browser thumb for each object being rejected (if available). Currently there is no check whether if the attachment is actually used in the HTML output or not. The attachment is marked as HTML, so if not referenced inside HTML, mail agents may not show the attachment.

### Replacements

Various replacements can be used inside the Email templates when rendering. Available information depends on the context on configuration of the transition and action executed for this email.

| Variable | Description |
|---|---|
|`.Action`| Struct containing all information of the curent action.|
|`.Action.Subject` | Confirured subject for the email.
| `.Action.Message` | Configured message for the email.
| `.Transition` | Struct containing all information of the current transition.
| `.Transition.Confirm` | Configured onfirmation text.
| `.Info.Objects` | List of objects affected by this transition. Each object has a number of properties accessible for rendering. To output standard info of the object use:
 | `.Info.Objects.#.Standard.One.Text` | Output the standard 1 textual information.
 | `.Info.Objects.#.Standard.BrowserThumb.Filename` | Output the filename of the browser thumb as used in the attachments.

