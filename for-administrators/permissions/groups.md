---
description: >-
  User groups can be used to structure users and assign permissions. You can
  create your own groups or use predefined system groups. They can be assigned
  to users manually or automatically.
---

# Groups

## Working with Groups

Each FYLR installation comes with some predefined [**system groups**](groups.md#system-groups) that cannot be deleted but can be used to assign system rights and permissions to. You can add your **own** groups by clicking on the **plus** button on the lower **left**. To **delete** a group, select it and click the **minus** button. You can **copy** a group by selecting it and click on "Copy" on the lower right of the group settings. Use the **search** **filter** to search for the **name**, **internal name, internal comment** and **reference** of groups. You can also **filter** for the **group types** "easydb" and "system".

Typical groups are:

* Administrators
* Editors / Power User
* Reader / Staff

As users can be assigned to **multiple** groups, you can also have a group called "Authorized to download" for example that only grants the users the permission to download files. User can then be added to the group "Reader" (which gives them access to records without being able to download them) and the group "Authorized to download" (which additionally gives them download permissions).

If you are working with **different** departments / projects that should only work in their own **pools**, you should create the editor and reader group for **each** department / project.

## System Groups

Each FYLR installation comes with the following **predefined system groups**, that will be automatically assigned to users:

<table><thead><tr><th width="301.5">GROUP</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>All Users</td><td>This group includes all users. Even system user, anonymous user, LDAP &#x26; SSO user and local users.</td></tr><tr><td>All Users Except System Users</td><td>This group includes all users except system users like "root", "deep_link" and "oai_pmh".</td></tr><tr><td>Anonymous Users</td><td>This group includes all users that access the system without a user account. External access needs to be enabled in the <a href="../readme/access.md#allow-guest-access">base configuration</a>.</td></tr><tr><td>Anonymous Collection Users (formerly "Pseudo users to see single collections")</td><td>This group includes all users that were created when <a href="../../for-users/quick-access/collections-and-presentations.md#sharing">sharing a collection</a> to external users that don't require a log in.</td></tr><tr><td>Fallback Group</td><td>This group does not include any users. When a group is deleted that is the owner of records, this fallback group is set as the owner instead.</td></tr><tr><td>LDAP Users</td><td>This group includes all users that sign in via LDAP.</td></tr><tr><td>Local Users</td><td>This group includes all users that were created locally in FYLR.</td></tr><tr><td>Self-Registered Users</td><td>This group includes all users that signed up. This possibility needs to be enabled in the <a href="../readme/access.md#registration">base configuration</a>.</td></tr><tr><td>SSO Users</td><td>This group includes all users that sign in via SSO.</td></tr><tr><td>Users Accessing Via External Connection</td><td></td></tr><tr><td>Users Accessing Via Internal Connection</td><td></td></tr><tr><td>Users Invited by Email</td><td>This group includes all users that were created when <a href="../../for-users/quick-access/collections-and-presentations.md#sharing">sharing a collection</a> or an export to an email address.</td></tr></tbody></table>

## Group Settings

{% hint style="info" %}
Group settings can be extended with custom plugins.&#x20;
{% endhint %}

### General

<table><thead><tr><th width="256.14472252448314">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>ID</td><td>Group identifier. Will be assigned automatically.</td></tr><tr><td>Type</td><td>Type of the group. Local groups will be of type "easydb". Groups of type "system" cannot be deleted.</td></tr><tr><td>Owner</td><td>Name of the user who created the group.</td></tr><tr><td>Name</td><td>Name of the group.</td></tr><tr><td>Internal Comment</td><td>Internal comment for the group. Will not be shown anywhere else.</td></tr><tr><td>Internal Name</td><td>Internal name for the group. Will not be shown anywhere else.</td></tr><tr><td>Reference</td><td>Reference of the group. Has to be unique.</td></tr><tr><td>IP Subnet Filter</td><td>Add IP subnet filter if the user should only be assigned to this group if they log in from specific IP subnets. CIDR notation is accepted, example: <code>192.168.0.0/16, 2001:db8::/32</code>. For more see the documentation <a href="https://pkg.go.dev/net#ParseCIDR">https://pkg.go.dev/net#ParseCIDR</a></td></tr><tr><td>Preferences for New Users</td><td>Shows the default frontend preferences for new users of this group. If none are set, the system defaults are used.<br>Includes:<br>- search result settings<br>- pools for the search<br>- object types for the search<br>- data languages<br>- search languages<br>- filter on/off<br><br>If a user is in several groups with preferences, they will receive the preferences of the first group.</td></tr><tr><td>Use Preferences of User</td><td>Choose an existing user which frontend preferences should be used as a default for new users of this group.</td></tr><tr><td>Created</td><td>Date and time the group was created.</td></tr><tr><td>Last Updated</td><td>Date and time of the last update of the group.</td></tr></tbody></table>

### System Rights

Define which parts the users of the user group should be allowed to access and which features they should be allowed to use. Please refer to the general overview of [system rights](./) for more details.

### Permissions

Define which other users or user groups should be able to access (read, write, delete) this group and/or the users of this group. Please refer to the general overview of the [permissions](./) for more details.

### Pseudonymization

Define which data of a user of this group should be kept, deleted or pseudonymized when archiving it.

<table><thead><tr><th width="142">OPTION</th><th width="360">DESCRIPTION</th><th>AVAILABLE FOR FIELD</th></tr></thead><tbody><tr><td>Keep</td><td>When the user is archived, the content of the field is kept.</td><td><ul><li>Login</li><li>First Name</li><li>Last Name</li><li>Department</li><li>Email</li></ul></td></tr><tr><td>Randomize</td><td>When the user is archived, the content of the field is replaced by a random string.</td><td><ul><li>Login</li><li>First Name</li><li>Last Name</li><li>Department</li></ul></td></tr><tr><td>Clear</td><td>When the user is archived, the content of the field is deleted.</td><td><ul><li>Login</li><li>First Name</li><li>Last Name</li><li>Department</li><li>Email</li></ul></td></tr></tbody></table>

### Authentication Services

If you're using a third party user management like LDAP or SSO, you can define a group mapping here and automatically map groups used in SSO or LDAP to groups in FYLR whenever a user signs in.

<table><thead><tr><th width="267.5">METHOD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Group Name (eq)</td><td>Group name from LDAP/SSO needs to match this string exactly.</td></tr><tr><td>Regular Expression (regexp)</td><td>Group names from LDAP/SSO need to match with the regular expression. Example: <code>students.*</code> will match the LDAP/SSO group <code>students</code> and the group <code>students-alumni</code> but not a group named <code>student</code>. For more see the documentation <a href="https://pkg.go.dev/regexp#Match">https://pkg.go.dev/regexp#Match</a></td></tr></tbody></table>

### User

View all users that are in this group.
