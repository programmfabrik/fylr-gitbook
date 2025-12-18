---
description: How to configure and use the ai-metadata plugin
---

# ai metadata plugin

{% hint style="info" %}
For the setup of this plugin **root** permissions are suggested.
{% endhint %}

### Plugin description

The **ai-metadata plugin** enables the integration of OpenAIs ChatGPT into a fylr instance by automatically filling object type fields. Custom prompts can be configured and mapped to fylr object types through metadata mappings. The generated output is written directly to objects during their creation.

### Datamodel requirements

To successfully use the ai-metadata plugin to describe your instances content, your Object Type needs to have

* **a file field**: the source image for ChatGPT to describe
* **text fields or lists**: (multilingual) text fields to map ChatGPTs output to

### Installation

{% hint style="info" %}
**This plugin is a paid feature.** The plugin is only available after a valid license has been purchased.

Please contact us to obtain the license.
{% endhint %}

Move to your fylr instances Plugin Manager to install the ai-metadata plugin by finding the <img src="../.gitbook/assets/Screenshot 2025-08-20 at 15.28.24.png" alt="" data-size="line">-Icons in the bottom of the plugin list and clicking the plus symbol.

While installing enabling the plugin is the default behavior. You can enable or disable the plugin anytime, active configuration will be preserved until enabled again.

<figure><img src="../.gitbook/assets/Screenshot 2025-08-20 at 15.27.19.png" alt="" width="343"><figcaption></figcaption></figure>

### Configuration

After installing and activating the plugin, select it in the plugin list.

Configure the plugin in the "General Tab" by adding an API Key

| Setting                        | Description                                                                                 |
| ------------------------------ | ------------------------------------------------------------------------------------------- |
| **ChatGPT API Key (Required)** | Enter your OpenAI API key. Without API Key, requests to OpenAI will be denied.              |
| **Erweitertes Protokoll**      | Optional. Debug option (detailed logging).                                                  |
| **Used image size**            | Controls the resolution of images sent to OpenAI. “Small” is sufficient for most use cases. |

### Creating the ChatGPT prompts

Inside the plugin managers config tab, create one or more **named prompts** by clicking <img src="../.gitbook/assets/Screenshot 2025-08-20 at 15.33.59.png" alt="" data-size="line">.

The available inputs are mandatory.

<table><thead><tr><th width="141.953125">Setting</th><th width="302.953125">Description</th><th>Options</th></tr></thead><tbody><tr><td>Name</td><td>Name your prompt. This name will be used later to refer to this particular prompt.</td><td>-</td></tr><tr><td>Question for Chat GPT</td><td>Your custom ChatGPT prompt</td><td>-</td></tr><tr><td>Type</td><td>Output type</td><td><ul><li><em>Single line text</em></li><li><em>Single line text (multilingual)</em></li><li><em>List text</em></li><li><em>List text (multilingual)</em></li></ul></td></tr></tbody></table>

#### Choosing the Output Type

{% hint style="info" %}
**The output type matters when mapping the prompt to the object type later**, make sure you select the option that fits your needs and matches your object types fields.

If it doesn't, edit your datamodel accordingly and continue afterwards.
{% endhint %}

* _Single line text_
  * maps to[#single-line--multi-line-text-simple-text-string](../for-administrators/tools/csv-importer/examples/all-data-types.md#single-line--multi-line-text-simple-text-string "mention")
* _Single line text (multilingual)_
  * maps to [#single-line-and-multiline-text-multilingual](../for-administrators/tools/csv-importer/examples/all-data-types.md#single-line-and-multiline-text-multilingual "mention")
* _List text_
  * maps to [#single-line--multi-line-text-simple-text-string](../for-administrators/tools/csv-importer/examples/all-data-types.md#single-line--multi-line-text-simple-text-string "mention") in a nested field.
* _List text (multilingual)_
  * maps to [#single-line-and-multiline-text-multilingual](../for-administrators/tools/csv-importer/examples/all-data-types.md#single-line-and-multiline-text-multilingual "mention") in a nested field.

#### Examples

<figure><img src="../.gitbook/assets/Screenshot 2025-08-20 at 16.14.58.png" alt="Example prompts created for the ai-metadata plugin. The prompts display the usage of the different output type options while showcasing prompts in various complexities."><figcaption><p>Example prompts created for the ai-metadata plugin. The prompts display the usage of the different output type options while showcasing prompts in various complexities.</p></figcaption></figure>

{% hint style="info" %}
**Multilingual fields:** Make sure to include the languages of your expected output in your prompt.
{% endhint %}

Each named list entry in the Plugin Managers configuration tab of the ai-metadata plugin becomes available in the **Metadata Mapping** section of fylr.

As a start, you can upload the displayed configuration and modify as needed.

{% file src="../.gitbook/assets/fylr-ai-metadata-plugin-example-config.json" %}

### Creating the Metadata Mapping

Navigate to "Metadata Mappings" in the configuration.

Create a new **IMPORT Mapping** by finding the <img src="../.gitbook/assets/Screenshot 2025-08-20 at 15.28.24.png" alt="" data-size="line">-Icons in the bottom of the available Mappings and clicking the plus symbol, selecting IMPORT.

<table><thead><tr><th width="149.2109375">Option</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Select an Object Type to apply the mapping to</td></tr><tr><td>Name</td><td>Provide a descriptive name for your mapping</td></tr></tbody></table>

If the plugin is enabled and a prompt is configured in the previous step, you should now see the section **“ChatGPT Metadata”** listing your created prompts.

Per default all Object Types are listed, in the below example, only the fields for the selected Object Type are shown because the object type limits the mapping to be used on OT "ChatGPT Object"

To map the available fields to the created prompts, drag and drop the individual fields onto your created mapping. Right click a mapping to remove.

<figure><img src="../.gitbook/assets/Screenshot 2025-08-21 at 09.44.42.png" alt="Example of a created Metadata Mapping in fylr. To map an object types fields to our created ChatGPT Prompts drag and drop the individual fields onto your created mapping."><figcaption><p>Example of a created Metadata Mapping in fylr using drag and drop.</p></figcaption></figure>

{% hint style="info" %}
Right-click on a mapping to remove it. Duplicate Mappings are allowed.
{% endhint %}

**Reload the frontend to make the mapping available for upload dialogs and record creation.**

### Usage while creating records

When creating a new record, select the metadata mapping that includes your prompt configuration.

The mapping can be used

* during **upload via the plus icon**

<figure><img src="../.gitbook/assets/Screenshot 2025-08-21 at 10.09.47.png" alt="Create New Records view in fylr app. Highlighted are our choosen Object Type and the metadata mapping using the ChatGPT prompts"><figcaption></figcaption></figure>

When clicking **Next**, you will see the Metadata Mapping being applied with a progress indicator.

<figure><img src="../.gitbook/assets/Screenshot 2025-08-21 at 10.10.21.png" alt="" width="305"><figcaption><p>Metadata mapping status progress</p></figcaption></figure>

In the next view, see the prompt results arranged into your fields. After saving, the records will be accessible just like any other record.

{% hint style="info" %}
**Upload collections** can be configured to apply a custom metadata mapping to be applied to all newly added records
{% endhint %}

If not satisfied with the results, after updating your prompts with closer alignment to your requirements, restart the import process or continue reading to apply the mapping with a background task.

***

## Usage with Background Tasks

To run the **ai-metadata plugin** in background tasks, follow these steps:

{% hint style="danger" %}
**Creating a new background task from a selection of records** to be mapped by the ai-metadata plugin is currently **not supported**.
{% endhint %}

### Create and Configure the Task

1. Open the **Background Tasks** section in the header bar of your fylr instance.

<figure><img src="../.gitbook/assets/Screenshot 2025-08-22 at 14.19.16.png" alt="background tasks manager located in the header bar of fylr" width="375"><figcaption><p>background tasks manager located in the header bar of fylr</p></figcaption></figure>

2. Create a **new task** by using the <img src="../.gitbook/assets/Screenshot 2025-08-20 at 15.28.24.png" alt="" data-size="line">-Icon and selecting the module **Metadata**
3. Define the schedule:

* **Manual time** (default: now)
* **Scheduled time** (future execution)

### Task Parameters

#### Configure the mapping

<figure><img src="../.gitbook/assets/Screenshot 2025-08-26 at 14.55.47.png" alt="" width="563"><figcaption><p>Example mapping configuration for using the ai-metadata plugin in a background task</p></figcaption></figure>

| Parameter            | Description                                                                         |
| -------------------- | ----------------------------------------------------------------------------------- |
| **Object Type**      | Apply only to the specified object type.                                            |
| **Metadata Mapping** | Select the metadata mapping to be applied.                                          |
| **Pool**             | Used when creating linked records with pool management during metadata mapping.     |
| **Mask**             | Define which mask to use for the task.                                              |
| **Field for Files**  | If multiple file fields exist, specify which one to use as source for yourn prompt. |

#### Creating a search result to apply the mapping to

For the task to have records to apply the mapping to, configure a search that finds the records you want to be filled by ChatGPT (selection of records / the entire search result).

{% hint style="warning" %}
If individual records are selected, only those will be mapped.

If an entire search result is selected using **"Select All", the same search will be reused** for the next scheduled run of the background task.
{% endhint %}

{% hint style="danger" %}
**Warning: An empty search will result in the background-task sending ALL records to ChatGPT.**
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-08-26 at 15.33.46.png" alt="Example configuration of a search query showing results to be mapped by the ai-metadata plugin using the bg-tasks." width="563"><figcaption><p>Example configuration of a search query showing results to be mapped by the ai-metadata plugin using the bg-tasks.</p></figcaption></figure>

If the found records have no values in their fields yet, the **Override Values** checkbox might not be required.

After the created tasks next scheduled job has finished (now or later, depending on the amount of records to be mapped), confirm the changes made in the tasks log and the record itself.
