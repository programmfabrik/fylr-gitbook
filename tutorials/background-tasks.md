---
description: How to use background tasks in fylr
---

# Background tasks

Enables users to configure and schedule server-side jobs.&#x20;

### Overview

Open the **Background Tasks** section in the header bar of your fylr instance.

<figure><img src="../.gitbook/assets/Screenshot 2025-08-22 at 14.19.16.png" alt="background tasks manager located in the header bar of fylr" width="375"><figcaption><p>background tasks manager located in the header bar of fylr</p></figcaption></figure>

#### Tasks Table

The **Tasks Table** lists all existing background tasks.

For each task, users can:

* **View Task Log:** Inspect execution details and results
* **Edit Task:** Modify configuration, schedule, or parameters

***

### Creating a New Task

Create a **new task** by using the <img src="../.gitbook/assets/Screenshot 2025-08-20 at 15.28.24.png" alt="" data-size="line">-Icon and selecting the module

#### Select a Module

Each module executes a type of background job. The selected module determines which parameters will be available during configuration.

Available modules:

* `delete_objects` : Delete objects
* `metadata`: Apply metadata mappings on search results &#x20;
* `search` : Execute an advanced search (send summaries via email)
* `set_unset_tags` — Set or unset tags

#### Task Configuration

Description: A brief description of the tasks purpose (can be edited later)

Define the schedule:

* **Manual time** (default: now)
* **Scheduled time** (future execution, repeated schedules possible)

Email Notifications: Send an email notification when the task completes

### Task Parameters

#### Common Parameters

* **Search Configuration**: Define the target records for the task using a commong [search.md](../search.md "mention")

Depending on the module used different parameters will be available.

{% hint style="info" %}
System right **"Administration > Access Task Manager"** is required to use access background tasks.

The user needs appropriate permissions to the datamodel to successfully apply modules.
{% endhint %}

***

### Monitoring and Logs

Once a task is created and executed, its progress and results can be monitored through the **Task Log**.

Task Log may be accessed from the tasks table or from the task editor.&#x20;

The log includes:

* information (start, finish)
* Status (success, failed, in progress)
* Output messages or error details
