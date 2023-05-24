---
description: >-
  Tags are labels that can be assigned to records. They can be used to reflect
  (editorial) workflows or give users access to selected records.
---

# Tags & Workflows

## Use Cases

Tags & workflows can be used for several different use cases. Some common use cases are:

<table><thead><tr><th width="188.5">USE CASE</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Editing Status</td><td>Imagine finishing records takes longer because the necessary data has to be gathered over a longer period of time, or you want to quickly upload files with just a minimal set of data and then work on the details later. To keep track of status of the records simply create tags for each state (i.e. "new", "in progress" or "finished"). Using permissions with tag filters, you could even define that specific user groups can only access or download finished records.</td></tr><tr><td>Publish Records</td><td>Imagine you want to offer a frontend for external users that don't have to log in to see parts of your records. Simply create a tag to flag records that should be accessed by anonymous users (i.e. "External" or "Published") and use permissions and tag filters to make sure they only see what you want them to see.</td></tr><tr><td>Editorial Workflow</td><td>Imagine records need to be reviewed and approved by someone before they can be published. Then set up a group (i.e. "Editors"), a tag (i.e. "For Review") and define a workflow so that the editors get an email whenever a new record was tagged. Also make sure, that not all users can set the "Published" tag by defining a workflow that forbids certain groups to set the tag.</td></tr><tr><td>Automatic Exports</td><td>Imagine you want regularly to export a part of your records to external websites or portals. Then simply create a tag (i.e. "Export to portal 1"), tag your records and set up an export with a schedule for all tagged records.</td></tr></tbody></table>



## Tags

**Tags** are always structured in so called **tag groups**. It's essential to create a tag group first by clicking on the **plus** button on the lower left. To add a tag, a tag group has to be selected, only then you can click on the plus button and choose "Tag". To **remove** tags or tag groups, select them and click on the **minus** button in the lower left.&#x20;

{% hint style="info" %}
Please note, that tags / tag groups can only be deleted when they're not used in any records or permissions.
{% endhint %}

By **default**, the tags that are defined here, will be **available** for **all object types** with enabled tag management and for **all users** in **all pools**. For object types and pools you can use the option "**Use individual tags**" to only use some of the tags.

If you want to **hide** all tags from specific **users**, you can define a **mask** and set the tags to "**Hide**". In case you only want to **prevent** specific **users** to **set/unset** a tag, please define a **workflow** (see below).

The **order** of tag groups and tags can be changed by using the little **drag handle** in front of the display name. They will be displayed in this order when assigning tags to records or viewing tags of records.

Use the following **options** to set up tags and tag groups:

<table><thead><tr><th width="195.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Display Name</td><td>Add a name of the tag group and the tags.</td></tr><tr><td>Type</td><td>For the tag groups choose if the tags should be radio buttons (only one tag of the tag group can be set for a record) or checkboxes (multiple tags of the tag group can be set for a record). </td></tr><tr><td>Display</td><td>Choose wether the tag should be shown in the editor, detail, search and/or filter. Choose "hidden" when you want to work with hidden tags in workflows or you only need them for the API.</td></tr><tr><td>Additional Info</td><td>Define a reference or short name for a tag group or tag. Both have to be unique. This can be helpful when importing data with tags or working with the API. For tags you can additionally add a description which will be shown when hovering over the tag.</td></tr><tr><td>Enabled</td><td>Only enabled tags can be used. Disable a tag to hide it from the tag selection. This setting can be overwritten by individual tags for pools or object types.</td></tr><tr><td>Default</td><td>Activate if the tag should be set automatically when creating new records.</td></tr><tr><td>Persistent</td><td>Activate if the tag (settings) should not be overwritten by individual tags for pools or object types.</td></tr><tr><td>Icon</td><td>Choose an icon from the list (the list can be extended in the <a href="../readme/general.md#font-awesome-icons">base configuration</a>). The icon will be shown together with the name of the tag in the editor and detail. In the standard search result only the icon will be shown. If no icon is set, the first letter of the tags name will be used.</td></tr><tr><td>Color</td><td>Choose a color from the list. The tag and the tag icon will be shown in this color.</td></tr><tr><td>Permissions</td><td>Add permissions to a tag. Those permissions apply to all records where this tag is set. For example, if you assign read access to a group here, these users will be able to see all records with this tag, no matter in which pool the records are.</td></tr></tbody></table>



## Workflows

A workflow is triggered when:

* the operation matches,
* the currently logged in user matches the defined user / group,
* the state before and after saving matches,
* and the user confirms the workflow (if configured)

By **default**, the workflows that are defined here, will be **available** for **all object types** with enabled tag management and for **all users** in **all pools**. For object types and pools you can use the option "**Use individual workflows**" to define workflows that are only available in that context.

To **add** a workflow, click on the **plus** on the lower left and on the **minus** to **delete** a selected workflow. To **copy** a workflow, click on it and then click the copy icon on the lower left.

The **order** of workflows can be **changed** by using the little **drag handle** in the front row. This is **important** because depending on the **type** of a workflow this can make a **difference**.

Use the following **options** to set up a workflow:

<table><thead><tr><th width="220.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Insert</td><td>Activate, if the workflow should be checked when a user creates a new record. If not enabled, the workflow will be ignored when a user creates a new record.</td></tr><tr><td>Update</td><td>Activate, if the workflow should be checked when a user modifies an existing record. If not enabled, the workflow will be ignored when a user modifies an existing record.</td></tr><tr><td>Delete</td><td>Activate, if the workflow should be checked when a user deletes a record. If not enabled, the workflow will be ignored when a user deletes a record.</td></tr><tr><td>Type</td><td>The type of a workflow determines whether the configured workflow is allowed and the user can save the record, or whether it is rejected and saving is prevented. See below for more details.</td></tr><tr><td>Object Types</td><td>Choose the object type(s) for which the workflow should be checked.</td></tr><tr><td>User / Groups</td><td>Add all users and / or groups this workflow should be checked for. For all other users / groups this workflow will be skipped. If you want to define a workflow for all users, simply choose the system group "All users" here.</td></tr><tr><td>Comment</td><td>Add an internal comment to note what the workflow is about. Will not be shown anywhere else.</td></tr><tr><td>State Before Saving</td><td>Define the state of the tags before saving a record. Allows you, for example, to forbid changing the tags of a record from tag "a" to tag "b".</td></tr><tr><td>State After Saving</td><td>Define the state of the tags after saving a record. Allows you, for example, to forbid changing the tags of a record from tag "a" to tag "b".</td></tr><tr><td>Confirmation Text</td><td>Add a text that should be shown to the user when the workflow applies. </td></tr><tr><td>Action</td><td>Define what should happen when this workflow is triggered. See below for more details.</td></tr><tr><td>Persistent</td><td>Activate if the workflow should not be overwritten by individual tags for pools or object types.</td></tr></tbody></table>



Choose between the following **types**:

<table><thead><tr><th width="175.5">TYPE</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>NORMAL</td><td>The action of the configured workflow is triggered and the subsequent workflows are checked. If no "Reject" or "Exit Reject" is received, the record will be saved.</td></tr><tr><td>RESOLVE &#x26; EXIT</td><td>The configured action is triggered and the record will be saved. All subsequent workflows will be ignored.</td></tr><tr><td>REJECT &#x26; EXIT</td><td>The configured action is triggered and saving the record will be rejected. All subsequent workflows will be ignored.</td></tr><tr><td>RESOLVE &#x26; CONTINUE</td><td>The action of the configured workflow is triggered and the subsequent workflows are checked. If no "Reject" or "Exit Reject" is received, the record will be saved.</td></tr><tr><td>REJECT &#x26; CONTINUE</td><td>The action of the configured workflow is triggered and the subsequent workflows are checked. If no "Exit Resolve" is received, the saving of the record will be rejected.</td></tr></tbody></table>



Choose between the following **actions**:

<table><thead><tr><th width="170.5">ACTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Email</td><td>An email will be send when the workflow is triggered. Choose one or more recipients and add a subject and a message. Enable "Support Batched Mailing" to send workflow emails according to the users email schedule. If no schedule is set for the user, the email notifications will be send directly. Please note, if records are edited with the batch editor, only one mail with all records will be send.</td></tr><tr><td>Tags</td><td>Set or unset tags when the workflow is triggered. One click adds the tag (plus icon), second click removes the tag (minus icon) and third click doesn't change the tag.</td></tr><tr><td>Webhook</td><td>Please see <a href="../readme/workflow-webhooks.md">base configuration</a>.</td></tr></tbody></table>

{% hint style="info" %}
You can add more actions by developing plugins. Such as automatically add a comment to the change history or update a field of the record.
{% endhint %}

