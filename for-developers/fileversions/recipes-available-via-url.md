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

| key    | value                               |
| ------ | ----------------------------------- |
| format | \[string]                           |
| start  | timestamp to start snippet\[string] |
| end    | timestamp to end snippet\[string]   |

You may use dot notation to target in milliseconds.

### Usage

Usage of the audio snippet generation endpoint:

{% hint style="info" %}
also see the technical documentation under&#x20;

* `{fylr base url}/inspect/apidocs/eas/download/`
* `{fylr base url}/inspect/apidocs/recipes/`
{% endhint %}

#### Example&#x20;

`GET /api/v1/eas/download/{fileId}/{hash}/{version}&access_token={access_token}&recipe=audioconverter:snippet&recipe_params={params}`&#x20;

* `/inspect/files/{fileID}`  lists the required fields.&#x20;
* for `version` use a named rendition, like `original.mp3`&#x20;
* alternatively, download the record in the frontend and copy the according download URL in the browsers dev tools
* recipe params:
  * URL encoded JSON, timestamp in seconds (might not be required, depending on request context)
  * use milliseconds by applying dot notation, e.g.: `{format:"mp3",start:"0.99",end:"20.5"}`\
