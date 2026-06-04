# /rput

The **eas/rput** endpoint is used to asynchronously upload files. Use **/eas/put** to synchronously upload files. A file can only be inserted if a filename is provided, either by setting it as query parameter or in the `Content-Disposition` header set by the web server of the URL.

### `POST /eas/rput`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/rput" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
