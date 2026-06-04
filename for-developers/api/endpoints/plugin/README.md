# /api/v1/plugin

Read information about installed plugins, and download the bundled
plugin assets (JavaScript, CSS, HTML templates, translations).

### `GET /plugin` — List installed plugins.
{% swagger src="../fylr-openapi.yml" path="/plugin" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /plugin/bundle.js` — Concatenated plugin JavaScript bundle.
{% swagger src="../fylr-openapi.yml" path="/plugin/bundle.js" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /plugin/bundle.css` — Concatenated plugin CSS bundle.
{% swagger src="../fylr-openapi.yml" path="/plugin/bundle.css" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /plugin/bundle.html` — Concatenated plugin HTML templates.
{% swagger src="../fylr-openapi.yml" path="/plugin/bundle.html" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /plugin/bundle/l10n/{lang}.json` — Concatenated plugin translations for a language.
{% swagger src="../fylr-openapi.yml" path="/plugin/bundle/l10n/{lang}.json" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /plugin/static/{plugin}/{path}` — Download a bundled static asset of a plugin.
{% swagger src="../fylr-openapi.yml" path="/plugin/static/{plugin}/{path}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /plugin/extension/{plugin}/{path}` — Call a plugin-defined backend extension endpoint.
{% swagger src="../fylr-openapi.yml" path="/plugin/extension/{plugin}/{path}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
