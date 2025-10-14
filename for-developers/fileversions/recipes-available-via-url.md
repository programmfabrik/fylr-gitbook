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
* wma\


### Recipe Options

| key    | value                                |
| ------ | ------------------------------------ |
| format | \[string]                            |
| start  | timestamp to start snippet \[string] |
| end    | timestamp to end snippet \[string]   |

Timestamp in seconds, you may use dot notation to target in milliseconds.

Example:  `{ format:"mp3", start:"0.305", end:"20.571" }`

### Usage

Usage of the audio snippet generation endpoint:

{% hint style="info" %}
also see the technical documentation under&#x20;

* `{fylr base url}/inspect/apidocs/eas/download/`
* `{fylr base url}/inspect/apidocs/recipes/`
{% endhint %}

#### Full Request Example

`GET /api/v1/eas/download/{fileId}/{hash}/{version}&access_token={access_token}&recipe=audioconverter:snippet&recipe_params={params}`&#x20;

* `/inspect/files/{fileID}`  lists the required fields
* for `version` use a named rendition, like `original.mp3` &#x20;
* alternatively, download the record in the frontend and copy the according download URL in the browsers dev tools
* use `&recipe=audioconverter:snippet`  to use the recipe
* and pass the `recipe_params` as URL encoded JSON (depending on request context this might not be required)\
