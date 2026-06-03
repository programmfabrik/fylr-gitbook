# /api/l10n

Static UI translations — the localisations the front-end and admin
pages need before a user is signed in. Returned as
`{<lang>: {key: text}}` — a single top-level entry keyed by the
requested language tag whose value is the flat translation map.

### `GET /l10n/static/{lang}.json` — Static UI translations for a language.
{% swagger src="./fylr-openapi.yml" path="/l10n/static/{lang}.json" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /l10n/user/{version}` — Datamodel translations for a version.
{% swagger src="./fylr-openapi.yml" path="/l10n/user/{version}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /l10n/user/HEAD` — Update HEAD datamodel translations.
{% swagger src="./fylr-openapi.yml" path="/l10n/user/HEAD" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
