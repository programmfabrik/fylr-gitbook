# /api/v1/plugin

Read information about installed plugins, and download the bundled plugin assets (JavaScript, CSS, HTML templates, translations).

### `GET /plugin` — List installed plugins.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/bundle.js` — Concatenated plugin JavaScript bundle.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/bundle.js" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/bundle.css` — Concatenated plugin CSS bundle.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/bundle.css" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/bundle.html` — Concatenated plugin HTML templates.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/bundle.html" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/bundle/l10n/{lang}.json` — Concatenated plugin translations for a language.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/bundle/l10n/{lang}.json" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/static/{plugin}/{path}` — Download a bundled static asset of a plugin.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/static/{plugin}/{path}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/extension/{plugin}/{path}` — Call a plugin-defined backend extension endpoint.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/extension/{plugin}/{path}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
