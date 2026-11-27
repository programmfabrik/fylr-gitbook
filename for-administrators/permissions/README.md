# Permissions

The **permission system in fylr** provides a flexible and highly granular way to control **who can access what**, **where**, and **how**. It is designed to scale from small teams to complex organisations while remaining predictable and maintainable.

At its core, fylr is based on **users and groups**. Users authenticate to the system and inherit permissions primarily through their **group memberships**, allowing administrators to model organisational roles and functional responsibilities without managing permissions on a per-user basis.

Access to content is structured using **pools**, which define the scope of records and files users can work with. Pools can be organised hierarchically and combined with permissions to reflect departments, projects, workflows, or confidentiality levels. Additional control is provided through **object types** and **masks**, ensuring that users only see and interact with relevant record structures and fields.

For editorial processes and collaboration, fylr offers **tags and workflows**, which can influence visibility, permissions, and automated actions such as notifications or exports. **Permission presets** and explicit sharing mechanisms allow access to be granted temporarily or selectively, supporting cross-team and external collaboration scenarios.

Together, these components form a layered permission framework in which **users and groups define roles**, **pools define access scope**, **object types and masks define structure**, and **tags, workflows, and presets refine behavior and exceptions**. The following articles explain each of these elements in detail and how they interact within the overall permission model.

## Labels and Notes

{% hint style="info" %}
Available from version 6.36.0.
{% endhint %}

Every entry in the permissions of a pool, group, user, object type, tag or record can have a **label** and a **note**, which say what the entry is for and grant nothing. A filter line narrows the entries down by user or group and by a search text, and a compact view hides the permissions of each entry. See [Labels and Notes](labels-and-notes.md).
