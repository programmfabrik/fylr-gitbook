# Recipes available via URL

## Audio Snippets

Used to extract snippets from audio files

Extensions supported:

* aac
* aiff
* dts
* flac
* m4a
* mp2
* mp3
* oga
* ogg
* opus
* ra
* wav
* wma<br>

### Recipe Options

| key    | value                                |
| ------ | ------------------------------------ |
| format | \[string]                            |
| start  | timestamp to start snippet \[string] |
| end    | timestamp to end snippet \[string]   |

Timestamp in seconds, you may use dot notation to target in milliseconds.

Example: `{ format:"mp3", start:"0.305", end:"20.571" }`

### Usage

Usage of the audio snippet generation endpoint:

{% hint style="info" %}
also see the technical documentation under

* `{fylr base url}/inspect/apidocs/eas/download/`
* `{fylr base url}/inspect/apidocs/recipes/`
{% endhint %}

#### Full Request Examples

**api/v1/objects/**

{% code overflow="wrap" %}
```
GET /api/v1/objects/uuid/{uuid}/file/id/{file}?recipe=audioconverter:snippet&recipe_params={params}
```
{% endcode %}

{% hint style="info" %}
* Find the a base URL to append a recipe to at the file field share menu in the detail view of a object
* To access the copyable deep links set the correct permissions for the deep link user[export-and-deep-links.md](../../for-administrators/readme/export-and-deep-links.md "mention")
{% endhint %}

{% hint style="warning" %}
**Permissions when calling this without a login (deep link):** an unauthenticated request to `/api/v1/objects/…` does **not** run as *Anonymous* — it runs as the system user **`system:deep_link`**. Rights granted to the *Anonymous users* group therefore do **not** apply here.

For the snippet URL to work without login, grant the **`deep_link` user** (on the relevant objecttype) the same rights the use case needs, e.g.:

* view records (with the *standard* mask), and
* **asset show + download** for the version you are addressing (e.g. `audio.original`).

`file/id/{file}` and `file/standard/{n}` both work; `file/standard/{n}` avoids needing the file id.
{% endhint %}



**api/v1/eas/download/**

{% code overflow="wrap" %}
```
GET /api/v1/eas/download/{fileId}/{hash}/{version}&access_token={access_token}&recipe=audioconverter:snippet&recipe_params={params}
```
{% endcode %}



* `/inspect/files/{fileID}` lists the required fields
* for `version` use a named rendition, like `original.mp3`
* alternatively, download the record in the frontend and copy the according download URL in the browsers dev tools
* use `&recipe=audioconverter:snippet` to use the recipe
* and pass the `recipe_params` as URL encoded JSON (depending on request context this might not be required)

<br>
