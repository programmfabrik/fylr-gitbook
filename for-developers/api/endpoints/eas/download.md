# /download

The download endpoint is used to deliver binary file data. It delivers data for original files as well as renditions. These URL to the files should be taken from the responses of `/api/db` or `/api/search`.

### `GET /eas/download/{fileId}/{hash}/{version}`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `HEAD /eas/download/{fileId}/{hash}/{version}`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}" method="head" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /eas/download/{fileId}/{hash}/{version}/{zippath}`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}/{zippath}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `HEAD /eas/download/{fileId}/{hash}/{version}/{zippath}`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}/{zippath}" method="head" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
