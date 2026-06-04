# /api/v1/settings

Unauthenticated endpoint reporting brief information about the running fylr
instance: `version`, `instance` name, build details, Elastic `index_names`
and license-derived `capabilities`. The current system status is returned in
the `x-fylr-status` response header, which makes this path usable as a
liveness/status probe.

### `GET /settings` — Get all settings
{% swagger src="./fylr-openapi.yml" path="/settings" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
