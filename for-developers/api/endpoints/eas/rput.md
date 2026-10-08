# /rput

The **eas/rput** endpoint is used to asynchronously upload files. Use **/eas/put** to synchronously upload files. A file can only be inserted if a filename is provided, either by setting it as query parameter or in the `Content-Disposition` header set by the web server of the URL.

### `POST /eas/rput`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/rput" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### Sources that throttle

A public source may refuse an anonymous client (Wikimedia answers `403` to Go's default `User-Agent`) or rate-limit one that fetches many files (`429 Too Many Requests`). From **6.35.0** the download identifies fylr the same way the reachability check does, and an answer that means *ask again later* — `429`, `502`, `503`, `504` — is told apart from a final one (`403`, `404`): the check inside the request asks again up to twice, and the download in the file worker hands the job back to the queue for the delay the source names in `Retry-After`, leaving the file `pending` instead of `failed`. A job that is turned away this way for an hour is given up on.
