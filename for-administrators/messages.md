---
description: >-
  Messages have different purposes, such as showing a custom message on the
  login screen, adding a custom button with text to the navigation or showing a
  text before downloading files.
---

# Messages

## Working With Messages

Messages are a great way to add individual text to the application. Typical use cases are:

* add terms & conditions to the login process
* add a help to the header and/or the main navigation
* add individual text to the login and/or registration page
* show a copyright text when users are downloading files
* show a welcome/overview text after login instead of the records
* ...

Messages are always assigned to groups which enables you to define different messages for different groups.



## Messages

To **create** a new message, click on the **plus** button in the lower **left** and enter the details (see below). By **clicking** on a **message**, you can see and edit the details. To **remove** a message, **click** on the desired **message** and on the **minus** button in the lower **left**.

All messages are **sorted** **alphabetically** and you can use the filter to **search** for the message **title** and the **message** itself.

## Settings

### General

Mandatory fields are marked with an asterisk "\*".

<table><thead><tr><th width="200">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Type*</td><td>Defines where/how the message is shown. For a description of the available types, please see below. </td></tr><tr><td>Active From</td><td>Select a date from which the message should be enabled automatically. Before that date, the message is not shown. If no date is set, the message is enabled immediately.</td></tr><tr><td>Active Until</td><td>Select a date when the message should be disabled automatically. After that date, the message is not shown anymore. If no date is set, the message is enabled indefinitely.</td></tr><tr><td>Icon</td><td>Optionally add an icon to your message which will be shown either in the header before the title or on the button before the title. Supported icons: <a href="https://fontawesome.com/v4/icons/">FontAwesome</a>.</td></tr><tr><td>Title*</td><td>Title of the message. Will be shown in the list of messages, the header of the message and on the button.</td></tr><tr><td>Message*</td><td>Actual message. Supports markdown.</td></tr><tr><td>Reference</td><td>Reference of the message. Has to be unique.</td></tr><tr><td>Pools</td><td>Select one or more pools if the message should only be used for specific pools.</td></tr><tr><td>Tag Filter</td><td>Define a tag filter if the message should only be shown for records with specific tags.</td></tr><tr><td>Client IDs Filter</td><td></td></tr><tr><td>Link</td><td>Link to the message. Will be shown after saving.</td></tr><tr><td>Created</td><td>Date and time the message was created.</td></tr><tr><td>Last Updated</td><td>Date and time of the last update of the message.</td></tr></tbody></table>

### Confirmation

This tab is only available for type "Message After Logging In" and "Message Before Download".

#### Confirmation Options

| FIELD                     | DESCRIPTION                                                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Confirm Every New Version | If this option is activated, the user must confirm the message again if the confirmation text/settings has been changed.    |
| Confirmation Text         | This text appears with a checkbox the user has to enable in order to proceed.                                               |
| Hint in Footer            | This text is shown in the footer in the popover for type "Message Before Download" as long as the message is not confirmed. |

#### Choices

These choices are only available for the message type "Message Before Download". For example they can be used to force the user to state the intended use of the files before downloading.

| FIELD                | DESCRIPTION                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| Choice Group Header  | This text is shown before the actual options. It supports Markdown.                                   |
| Type                 | Choose between "Checkboxes" (multiple answers allowed) and "Radio Buttons" (only one answer allowed). |
| Min. Enabled Options | Specify the minimum number of options the user can activate in order to proceed with the download.    |
| Max. Enabled Options | Specify the maximum number of options the user can activate in order to proceed with the download.    |
| Choices              |                                                                                                       |
| Choice Group Footer  | This text is shown after the actual options. It supports Markdown.                                    |

#### Event

| FIELD            | DESCRIPTION                                            |
| ---------------- | ------------------------------------------------------ |
| Log Event        | If enabled, an event is created for this confirmation. |
| Event Idenfifier |                                                        |



### Groups

It's necessary to select at least one group for the messages to work. Multiple groups can be selected. All local groups and system groups are available.



## Types

The message types define where/how the messages are shown:

<table><thead><tr><th width="315">TYPE</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Message After Logging In</td><td>This message is shown after a user logs in. Also available for anonymous users (message is shown directly when opening the application). Depending on the settings in the "Confirmation" tab, the message can simply be closed or have to be accepted to continue to the search. If not accepted, the user will be directed back to the login page.</td></tr><tr><td>Welcome Message in Search</td><td>This message will be shown in the search after a user logged in (or an anonymous user opened the application).</td></tr><tr><td>Permanent Message in Main Menu</td><td>This message creates a link under "Info" in the main menu which opens the message in a popover when clicked.</td></tr><tr><td>Permanent Message in Header</td><td>This message creates a button in the header (next to the user settings and export manager) which opens the message in a popover when clicked.</td></tr><tr><td>Permanent Message on the Login Page</td><td>This message creates a link on the login page which opens the message in a popover when clicked.</td></tr><tr><td>Permanent Message on Self-Registration Page</td><td>This message creates a link on the self-registration page which opens the message in a popover when clicked.</td></tr><tr><td>Message Before Download</td><td>This message is shown when a user downloads a file. Depending on the settings in the "Confirmation" tab, the message can simply be closed or have to be accepted to continue the download. If not accepted, the file will not be downloaded.</td></tr><tr><td>Maintenance Warning</td><td>This message is shown after a user logs in and it also appears as a permanent message in the header. It's supposed to inform the user that a maintenance will be happening soon where they are not able to use the application.</td></tr><tr><td>Maintenance Message</td><td>This message is shown after a user logs in informing them that they're not able to access the system as there is a maintenance currently happening. Only the root user will be able to access the system while this message is active. We recommend to set a date so this message will be activated and deactivated automatically.</td></tr></tbody></table>
