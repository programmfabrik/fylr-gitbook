---
description: the chat pane — filling fields, searching, and acting through tools
---

# The AI assistant

The assistant is a pane at the right edge of the window, opened with the **AI assistant** handle. It pushes the content aside rather than covering it — a record opened full screen stops at the pane — and it stays where it is while you navigate: opening a record from the assistant's results does not throw the conversation away.

What it does depends on what is in front of you.

## In the editor: filling fields

1. **Mark the target fields.** In the editor, every text field has a star next to its name. The marked fields are what the assistant may fill; the chat shows them, and marking is the user's decision, not an administrator's.
2. **Ask.** "Describe the car in one sentence", "translate the title into the other languages", "shorten this".
3. **Look at the answer.** The assistant answers with a value per marked field, a multilingual field with one value per language, shown as a card.
4. **Apply.** The values go into the editor exactly as a template or a metadata mapping would — nothing is saved. The **Save** button is still yours, and languages the answer did not touch keep their value.

The conversation belongs to the record: the turns of the same record are remembered, so "ok, now the other languages too" works, and opening another record starts a new conversation.

Whether the files of the record go along is a checkbox, and which model is used is not the user's choice: the pool's or objecttype's `ai_config` lists the permitted models, and the first of them is used.

### The pool policy

`ai_config` on a pool or objecttype, inherited down the pool tree:

<table data-header-hidden><thead><tr><th width="200"></th><th></th></tr></thead><tbody>
<tr><td><code>enabled</code></td><td>Whether the assistant may be used for these records at all.</td></tr>
<tr><td><code>models</code></td><td>The permitted models, <code>&lt;provider&gt;/&lt;model&gt;</code>. The first is the default, and the rest are what a failed call falls through to — see <a href="configuration.md#a-model-may-be-a-chain">A model may be a chain</a>.</td></tr>
<tr><td><code>max_files</code></td><td>How many files may go along with one request.</td></tr>
<tr><td><code>assets</code></td><td>Per file class (<code>image</code>, <code>video</code>, …): whether files of that class may be sent, which versions (<code>preview</code>, <code>small</code>), whether the original is allowed, and a size cap.</td></tr>
</tbody></table>

A user only ever sends a file they are allowed to see: the rendition is picked under their rights, not the assistant's.

## Outside the editor: searching and acting

With no record open, the assistant is a search — and, when tools are enabled, an agent.

* The request goes to the **search assistant** model first, which turns it into a retrieval query: a descriptive phrase in the data languages for the vector side, single words for the word side. The pane shows what it searched for.
* It searches **where you are**: in the search app, the objecttypes of that search; in the lists, every objecttype, with the hits grouped under their objecttype.
* The hits come back as the ordinary record cards. A click opens the record; **Show in search** hands the whole result set to the search app.
* A request that names a number — *"find me five pictures"* — is answered with that many, best first, rather than with the one that survives the cut.
* If the request needs more than finding — collecting, sharing, opening — the assistant calls [tools](#tools).

The prompt is cleared when the question goes off, and the empty box offers what usually comes next as a greyed-out suggestion; space or → takes it.

## Tools

A tool is something the assistant may do in fylr. fylr hands out the catalogue, the assistant asks for a tool, and **fylr runs it in the user's own session**: their rights, their masks, their audit trail. The model never touches the API.

| Tool | | |
| --- | --- | --- |
| `search_objects` | reads | Finds records: the hybrid search behind one call. |
| `get_objects` | reads | Reads records by id — their texts and the ids of their files. |
| `find_user` | reads | Looks a user up by email or login. |
| `create_collection` | **changes** | Creates a collection under the user's own top level. |
| `add_to_collection` | **changes** | Puts records into a collection. |
| `share_collection` | **changes** | Shares a collection with a user, with a notification mail. |
| `open_object` | the window | Opens a record in the editor. |
| `show_collection` | the window | Selects a collection and shows what is in it. |

A tool that changes something is never run on the model's say-so: the pane shows the call and waits for the user to confirm it. fylr checks the rights regardless — the confirmation is there so nobody is surprised, not as the security boundary.

The last two are run by the browser, not by the server: they move the window rather than the data. That is also why the assistant can only claim to have done what a tool reported back — "I opened the record" is a tool result, not a phrase the model is free to produce.

That makes a request like *"collect all images of a Porsche in a collection"* one conversation: the assistant searches, shows what it found, asks whether to create the collection, asks whether to add the records, and reports. *"Share it with someone@example.com"* is the next turn.

{% hint style="info" %}
The tools are a catalogue on the server, not knowledge in the browser. The same catalogue is what other agents can be given later; the frontend is only the first caller.
{% endhint %}
