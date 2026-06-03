# /api/eas/put

The **eas/put** endpoint is used to synchronously upload files.

Differs from easydb 5: easydb 5 `eas/put` accepts a single file per
request ("one request must not contain more than one file upload form
field"); **fylr** accepts multiple files in one request (the
`references` / `filenames` parameters are arrays). Also, easydb 5
reports a missing user as `400` ("not authenticated"); **fylr**
rejects it with `401` (`UserRequired`).

### `POST /eas/put`
{% swagger src="../fylr-openapi.yml" path="/eas/put" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `PUT /eas/put`
{% swagger src="../fylr-openapi.yml" path="/eas/put" method="put" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
