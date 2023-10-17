---
description: >-
  User accounts are necessary to access the system. Manage your local or
  third-party users and then assign permissions.
---

# User

## Working with User

Each FYLR installation comes with some predefined [**system user**](user.md#system-user) that cannot be deleted but can be used to assign system rights and permissions to. You can add your **own** users by clicking on the **plus** button on the lower **left**. To **delete** a user, select it and click the **minus** button. Depending on your [configuration](../readme/user-management.md#handling-when-deleting-users), the user will then be **archived** or **deleted**. You can **copy** a user by selecting it and click on "Copy" on the lower right of the user settings.&#x20;

You can also use the **filter** to search for users**:**

<table><thead><tr><th width="217.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Type</td><td>Filter for user type (see below).</td></tr><tr><td>Groups</td><td>Filter for users of specific groups. Enable "Exclude Selected Groups" to show users that do not belong to the selected groups.</td></tr><tr><td>Plugin Groups</td><td>Filter for users of a specific group that's managed by custom plugins.</td></tr><tr><td>Show Archived</td><td>If enabled, only archived users are shown.</td></tr><tr><td>Archived After</td><td>Only show users that were archived after this selected date.</td></tr><tr><td>Archived Before</td><td>Only show users that were archived before this selected date.</td></tr><tr><td>Deactivated Users</td><td>Choose if you want to see active and/or deactivated users. </td></tr><tr><td>Filter By</td><td>Select all fields which should be included in the search.</td></tr><tr><td>Show</td><td>Select which fields should be displayed in the user search result. Use the drag handle to change the order.</td></tr></tbody></table>



## **User Types**

There are 8 different **types** of users.

{% hint style="info" %}
User types can be extended with custom plugins.&#x20;
{% endhint %}

<table><thead><tr><th width="238.5">TYPE</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>system</td><td>Predefined system users that can't be deleted. See below.</td></tr><tr><td>easydb</td><td>Local users that were created by administrators in the FYLR application.</td></tr><tr><td>easydb_self_register</td><td>Users that signed up. Must be enabled in the <a href="../readme/access.md#registration">base configuration</a>.</td></tr><tr><td>email</td><td>Users to whom a collection has been shared using only an email.</td></tr><tr><td>ldap</td><td>Users that signed in via LDAP. Must be enabled in the <a href="../readme/user-management.md#ldap">base configuration</a>.</td></tr><tr><td>sso</td><td>Users that signed in via SSO. Must be enabled in the <a href="../readme/user-management.md#saml">base configuration</a>.</td></tr><tr><td>anonymous</td><td>Users that accessed FYLR without an account. Must be enabled in the <a href="../readme/access.md#allow-guest-access">base configuration</a>. Not displayed in the user list.</td></tr><tr><td>collection</td><td>Users that were invited to access a collection without an account. Not displayed in the user list.</td></tr></tbody></table>



## System User

Each FYLR installation comes with the following **predefined system user**:

<table><thead><tr><th width="189.5">USER</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>root</td><td>Has always full access to the whole system. Should be used carefully.</td></tr><tr><td>deep_link</td><td>User that's used to check the permissions for <a href="../readme/export-and-deep-links.md#deep-link-settings">deep links</a>. Assign permissions to this user to enable deep links for all or specific records.</td></tr><tr><td>deleted_user</td><td>Whenever a user is deleted or archived that is the owner of a record or one that created / updated a record, the deleted user is replaced by deleted_user.</td></tr><tr><td>oai_pmh</td><td>User that's used for <a href="../readme/export-and-deep-links.md#oai-pmh">OAI/PMH</a>. Assign permissions to this user to make records available for OAI/PMH.</td></tr></tbody></table>



## User Settings

{% hint style="info" %}
User settings can be extended with custom plugins.&#x20;
{% endhint %}

### General

<table><thead><tr><th width="215.5">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>ID</td><td>User identifier. Will be assigned automatically.</td></tr><tr><td>Owner</td><td>Name of the user who created the user account. Gets full access (read, write, delete) to the user record. Can only be changed by root.</td></tr><tr><td>Type</td><td>Type of the user. See above. Can be changed (except type "system"). If the type "ldap" or "sso" is changed into another type, the users will no longer be able to login in with LDAP or SSO.</td></tr><tr><td>Login</td><td>Login of the user. Can be empty, but then an emails has to be set which then can be used for login.</td></tr><tr><td>First Name</td><td>First name of the user.</td></tr><tr><td>Last Name</td><td>Last name of the user.</td></tr><tr><td>Display Name</td><td>Define how the user should be displayed in the frontend. If empty, the user will be shown with first and last name. If they are empty, the login will be used.</td></tr><tr><td>Company</td><td>Company of the user.</td></tr><tr><td>Department</td><td>Department of the user.</td></tr><tr><td>Phone</td><td>Phone number of the user.</td></tr><tr><td>Reference</td><td>Reference of the user. Has to be unique.</td></tr><tr><td>Profile Picture</td><td>Upload a profile picture.</td></tr><tr><td>Internal Comment</td><td>Internal comment for the user. Will not be shown anywhere else.</td></tr><tr><td>Created</td><td>Date and time the user was created.</td></tr><tr><td>Last Updated</td><td>Date and time of the last update of the user.</td></tr><tr><td>Last Active</td><td>Date and time of the last log in of the user.</td></tr></tbody></table>

### Address

Add an **address** to the user. All fields are only **visible** to **administrators** who can access the user and to the user **itself** (if configured).



### Email

Enter an **email** for users so they can log in with their email and get email **notifications**, such as collection **sharing** or finished **exports**.

<table><thead><tr><th width="329.5">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Email</td><td>Enter a valid email for the user.</td></tr><tr><td>Ask the User to Confirm Their Email</td><td>If set, the user will be send a confirmation email. They won't be able to log in unless they confirmed their email address.</td></tr><tr><td>Email Confirmation Request Sent At</td><td>Date and time the email confirmation request was sent.</td></tr><tr><td>Email Confirmed At</td><td>Date and time the email was confirmed.</td></tr><tr><td>Send Welcome Email</td><td>If set, the user will be send a welcome email. </td></tr><tr><td>Welcome Email Sent At</td><td>Date and time the welcome email was sent.</td></tr></tbody></table>

#### Schedule

If you don't want to receive email **notifications** instantly, but only on specific days or at specific times, you can set up a **schedule**. Emails will then be **queued** and send as a bunch on your **preferred** day and time.

<table><thead><tr><th width="174.5">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Preset</td><td>Choose a preset which then can be modified.</td></tr><tr><td>Day of Month</td><td>Select all days of the month you want to receive email notifications. Should only be used when no weekday is selected.</td></tr><tr><td>Weekday</td><td>Select all weekdays of the month you want to receive email notifications. Should only be used when no day of the month is selected.</td></tr><tr><td>Hour</td><td>Select at which hour you want to receive the email notifications.</td></tr><tr><td>Timezone</td><td>Select your timezone.</td></tr></tbody></table>

### Password

<table><thead><tr><th width="244.5">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Valid From</td><td>Select a date from which the login should be enabled automatically. Before that date, the user cannot log in. If no date is set, the login is enabled immediately.</td></tr><tr><td>Valid To</td><td>Select a date when the login should be disabled automatically. After that date, the user cannot log in anymore. If no date is set, the login is enabled indefinitely.</td></tr><tr><td>Login Deactivated</td><td>Enable to deactivate the user account. When activated the user cannot log in anymore.</td></tr><tr><td>Set Password</td><td>Enable, if you want to set a (new) password for the user.</td></tr><tr><td>Password</td><td>Only enabled when "Set Passwort" is enabled. Enter the (new) password for the user. Password requirements might apply (if <a href="../readme/access.md#password">configured</a>), but can be overwritten.</td></tr><tr><td>Force User to Set New Password on Next Login</td><td>If enabled, the user will be forced to set a new password after they log in with the current one.</td></tr></tbody></table>

### Groups

**Assign** groups to the current **user** or see in which automatic groups they are.

<table><thead><tr><th width="211.5">TYPE</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Groups</td><td>List of all local groups.</td></tr><tr><td>Other Groups</td><td>Groups that are managed by custom plugins.</td></tr><tr><td>Automatic Groups</td><td>Groups that are automatically assigned to LDAP or SSO users (if <a href="groups.md#authentication-services">configured</a>). Groups are assigned/removed whenever a LDAP or SSO user signs in. They can't be removed manually.</td></tr></tbody></table>



### System Rights

Define which **parts** the user should be allowed to **access** and which **features** they should be allowed to use. Please refer to the general overview of [system rights](./) for more details.

### Permissions

Define which other **users** or user groups should be able to **access** (read, write, delete) this **user**. Please refer to the general overview of the [permissions](./) for more details.



## User Export

Users can be **exported** by clicking on the **settings** icon in the lower left of the user search. The file will **contain** all **user** accounts from the current **search**.&#x20;

{% hint style="info" %}
Please note, that user passwords will not be exported.
{% endhint %}

<table><thead><tr><th width="282.5">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>user._id</td><td>Unique identifier of the user record.</td></tr><tr><td>user._version</td><td>Version of the user record.</td></tr><tr><td>user.login</td><td>Login.</td></tr><tr><td>user.type</td><td>User type.</td></tr><tr><td>user.frontend_language</td><td>Frontend language the user has selected.</td></tr><tr><td>user.database_languages</td><td>Database languages the user has selected.</td></tr><tr><td>user.search_languages</td><td>Search languages the user has selected.</td></tr><tr><td>user.frontend_prefs</td><td>User settings as JSON.</td></tr><tr><td>user.custom_data</td><td>Custom data from plugins as JSON.</td></tr><tr><td>user.first_name</td><td>First name.</td></tr><tr><td>user.last_name</td><td>Last name.</td></tr><tr><td>user.displayname</td><td>Display name the user entered.</td></tr><tr><td>user.company</td><td>Company.</td></tr><tr><td>user.department</td><td>Department.</td></tr><tr><td>user.phone</td><td>Phone number.</td></tr><tr><td>user.remarks</td><td>Internal comment.</td></tr><tr><td>user.address_supplement</td><td>Extra Address Line.</td></tr><tr><td>user.street</td><td>Street.</td></tr><tr><td>user.house_number</td><td>No. / App.</td></tr><tr><td>user.town</td><td>City.</td></tr><tr><td>user.state</td><td>State.</td></tr><tr><td>user.country</td><td>Country.</td></tr><tr><td>user.login_disabled</td><td>Login deactivated. "true" for deactivated, "false" or empty for not deactivated.</td></tr><tr><td>user.login_valid_from</td><td>Login valid from.</td></tr><tr><td>user.login_valid_to</td><td>Login valid to.</td></tr><tr><td>user.require_password_change</td><td>Force User to Set New Password on Next Login.</td></tr><tr><td>user.mail_schedule</td><td>Email schedule of the user as JSON.</td></tr><tr><td>user.email</td><td>Email.</td></tr><tr><td>user.confirm_email</td><td>"true" if the user should get an email confirmation mail. "false" or empty if not.</td></tr><tr><td>user.confirm_email_sent_at</td><td>Date and time the email confirmation was sent.</td></tr><tr><td>user.welcome_email</td><td>"true" if the user should get a welcome mail. "false" or empty if not.</td></tr><tr><td>user._generated_displayname</td><td>Display name which was generated automatically.</td></tr><tr><td>user.picture</td><td>Profile picture data as JSON.</td></tr><tr><td>_groups#find</td><td>IDs of the groups the user is assigned to.</td></tr><tr><td>_groups#easydb</td><td>Groups the user is assigned to.</td></tr></tbody></table>



## User Import

**Import**, **update** or **delete** users by clicking on the **settings** icon in the lower left of the user search. After **uploading** the previously exported **CSV** file, all settings for updating or deleting users are already configured. You just have to click "**Prepare**" and then decide wether you want to **update** existing users or want to **delete** the users that are in the CSV file. If you want to **import** new users, you have to change the "**Update Field**" on the "Import Settings" tab to "**- Add new -**". **Passwords** can be added to the CSV file in **plain text** (column name should be **\_password**) and will be saved as a **hash** in the database after the import.

{% hint style="info" %}
Please refer to the [csv importer options](../tools/csv-importer/options.md) for a general description.
{% endhint %}

