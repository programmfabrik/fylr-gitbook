# /api/eas/download

The download endpoint is used to deliver binary file data. It delivers data for original files as well as renditions. These URL to the files should be taken from the responses of `/api/db` or `/api/search`.

### `GET /eas/download/{fileId}/{hash}/{version}`
{% swagger src="../fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/download/{fileId}/{hash}/{version}`
{% swagger src="../fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas/download/{fileId}/{hash}/{version}/{zippath}`
{% swagger src="../fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}/{zippath}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `HEAD /eas/download/{fileId}/{hash}/{version}/{zippath}`
{% swagger src="../fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}/{zippath}" method="head" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
