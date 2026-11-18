---
description: >-
  The third-party components fylr is built from, with the license each one is
  distributed under.
---

# Libraries fylr links

{% hint style="info" %}
Compiled from fylr **v6.36.0**, the newest release. Each release replaces these pages with its own.
{% endhint %}

The third-party components compiled into the fylr binary, the JavaScript the
web frontend ships, and the license each one is distributed under. The programs
a fylr installation *runs* are a separate question and have a list of their
own.

- **216** Go components in the shipped binaries
- **15** third-party components in the web frontend
- **13** distinct license texts
- **0** strong copyleft (GPL, AGPL)
- **1** weak copyleft (LGPL, MPL, EPL)
- **1** without a license file

This list describes **v6.36.0**.

Build tooling and test-only dependencies are not part of the shipped
artifacts and are therefore not listed. The complete license text of every
component is reproduced in `LEGAL.md`, which ships next to `LICENSE`
in every release archive and in the container image, and which the web
frontend shows under *About > Info*.

## What the graph is made of

| License                    | Components | Obligation       |
|----------------------------|------------|------------------|
| MIT                        | 103        | permissive       |
| Apache-2.0                 | 57         | permissive       |
| BSD-3-Clause               | 40         | permissive       |
| BSD-2-Clause               | 13         | permissive       |
| Apache-2.0 OR BSD-3-Clause | 5          | permissive       |
| ISC                        | 4          | permissive       |
| Unlicense                  | 2          | permissive       |
| CC0-1.0                    | 1          | permissive       |
| LicenseRef-MIT-Lucent      | 1          | permissive       |
| MPL-2.0                    | 1          | weak copyleft    |
| MPL-2.0 OR Apache-2.0      | 1          | permissive       |
| OFL-1.1 AND MIT            | 1          | permissive       |
| Unknown                    | 1          | no license found |
| Zlib                       | 1          | permissive       |

## The server components

216 in the shipped binaries. *Direct* means the module is in our own `require` block; *indirect* means it
arrives through another dependency.

| Module                                                                       | Version                               | Dependency | License                    |
|------------------------------------------------------------------------------|---------------------------------------|------------|----------------------------|
| Go standard library                                                          |                                       | —          | BSD-3-Clause               |
| cloud.google.com/go/auth                                                     | v0.19.0                               | indirect   | Apache-2.0                 |
| cloud.google.com/go/auth/oauth2adapt                                         | v0.2.8                                | indirect   | Apache-2.0                 |
| cloud.google.com/go/compute/metadata                                         | v0.9.0                                | indirect   | Apache-2.0                 |
| dario.cat/mergo                                                              | v1.0.2                                | indirect   | BSD-3-Clause               |
| github.com/AfterShip/email-verifier                                          | v1.4.1                                | direct     | MIT                        |
| github.com/Azure/azure-sdk-for-go/sdk/azcore                                 | v1.22.0                               | direct     | MIT                        |
| github.com/Azure/azure-sdk-for-go/sdk/azidentity                             | v1.13.1                               | indirect   | MIT                        |
| github.com/Azure/azure-sdk-for-go/sdk/internal                               | v1.12.0                               | indirect   | MIT                        |
| github.com/Azure/azure-sdk-for-go/sdk/storage/azblob                         | v1.8.0                                | direct     | MIT                        |
| github.com/Azure/go-ntlmssp                                                  | v0.1.1                                | indirect   | MIT                        |
| github.com/AzureAD/microsoft-authentication-library-for-go/apps              | v1.7.2                                | indirect   | MIT                        |
| github.com/Masterminds/goutils                                               | v1.1.1                                | indirect   | Apache-2.0                 |
| github.com/Masterminds/semver/v3                                             | v3.5.0                                | indirect   | MIT                        |
| github.com/Masterminds/sprig/v3                                              | v3.3.0                                | direct     | MIT                        |
| github.com/PuerkitoBio/goquery                                               | v1.13.0                               | direct     | BSD-3-Clause               |
| github.com/alecthomas/kong                                                   | v1.16.1                               | direct     | MIT                        |
| github.com/andybalholm/cascadia                                              | v1.3.4                                | indirect   | BSD-2-Clause               |
| github.com/antchfx/xmlquery                                                  | v1.5.1                                | direct     | MIT                        |
| github.com/antchfx/xpath                                                     | v1.3.6                                | indirect   | MIT                        |
| github.com/aws/aws-sdk-go-v2                                                 | v1.45.1                               | direct     | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream                        | v1.7.20                               | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/config                                          | v1.33.1                               | direct     | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/credentials                                     | v1.20.1                               | direct     | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/feature/ec2/imds                                | v1.19.1                               | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/feature/s3/transfermanager                      | v0.2.3                                | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/internal/configsources                          | v1.5.1                                | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/internal/endpoints/v2                           | v2.8.1                                | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/internal/sync/singleflight                      | v1.45.1                               | direct     | BSD-3-Clause               |
| github.com/aws/aws-sdk-go-v2/internal/v4a                                    | v1.5.1                                | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding                | v1.13.19                              | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/service/internal/checksum                       | v1.11.1                               | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/service/internal/presigned-url                  | v1.14.1                               | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/service/internal/s3shared                       | v1.20.1                               | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/service/s3                                      | v1.109.1                              | direct     | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/service/signin                                  | v1.7.1                                | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/service/sso                                     | v1.35.1                               | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/service/ssooidc                                 | v1.40.1                               | indirect   | Apache-2.0                 |
| github.com/aws/aws-sdk-go-v2/service/sts                                     | v1.47.1                               | indirect   | Apache-2.0                 |
| github.com/aws/smithy-go                                                     | v1.28.1                               | direct     | Apache-2.0                 |
| github.com/aws/smithy-go/internal/sync/singleflight                          | v1.28.1                               | direct     | BSD-3-Clause               |
| github.com/bahlo/generic-list-go                                             | v0.2.0                                | indirect   | BSD-3-Clause               |
| github.com/bbrks/go-blurhash                                                 | v1.2.0                                | direct     | MIT                        |
| github.com/beevik/etree                                                      | v1.7.1                                | direct     | BSD-2-Clause               |
| github.com/beorn7/perks/quantile                                             | v1.0.1                                | indirect   | MIT                        |
| github.com/blevesearch/segment                                               | v0.9.1                                | direct     | Apache-2.0                 |
| github.com/boombuler/barcode                                                 | v1.0.1-0.20190219062509-6c824513bacc  | indirect   | MIT                        |
| github.com/buger/jsonparser                                                  | v1.1.2                                | indirect   | MIT                        |
| github.com/caddyserver/certmagic                                             | v0.25.4                               | direct     | Apache-2.0                 |
| github.com/caddyserver/zerossl                                               | v0.1.5                                | indirect   | MIT                        |
| github.com/cespare/xxhash/v2                                                 | v2.3.0                                | indirect   | MIT                        |
| github.com/clipperhouse/displaywidth                                         | v0.11.0                               | indirect   | MIT                        |
| github.com/clipperhouse/uax29/v2/graphemes                                   | v2.7.0                                | indirect   | MIT                        |
| github.com/crewjam/httperr                                                   | v0.2.0                                | direct     | BSD-2-Clause               |
| github.com/crewjam/saml                                                      | v0.5.1                                | direct     | BSD-2-Clause               |
| github.com/davecgh/go-spew/spew                                              | v1.1.2-0.20180830191138-d8f796af33cc  | direct     | ISC                        |
| github.com/dlclark/regexp2                                                   | v1.12.0                               | direct     | MIT                        |
| github.com/dlclark/regexp2/v2                                                | v2.5.2                                | indirect   | MIT                        |
| github.com/dop251/goja                                                       | v0.0.0-20260826204918-8f1c0696a37b    | direct     | MIT                        |
| github.com/dop251/goja/ftoa                                                  | v0.0.0-20260826204918-8f1c0696a37b    | direct     | LicenseRef-MIT-Lucent      |
| github.com/dop251/goja/ftoa/internal/fast                                    | v0.0.0-20260826204918-8f1c0696a37b    | direct     | BSD-3-Clause               |
| github.com/dustin/go-humanize                                                | v1.0.1                                | direct     | MIT                        |
| github.com/ebitengine/purego                                                 | v0.10.2                               | indirect   | Apache-2.0                 |
| github.com/elastic/go-elasticsearch/v7                                       | v7.17.10                              | direct     | Apache-2.0                 |
| github.com/fatih/color                                                       | v1.19.0                               | indirect   | MIT                        |
| github.com/felixge/httpsnoop                                                 | v1.1.0                                | direct     | MIT                        |
| github.com/fxamacker/cbor/v2                                                 | v2.9.3                                | direct     | MIT                        |
| github.com/gabriel-vasile/mimetype                                           | v1.4.15                               | direct     | MIT                        |
| github.com/go-asn1-ber/asn1-ber                                              | v1.5.8                                | indirect   | MIT                        |
| github.com/go-ldap/ldap/v3                                                   | v3.4.14                               | direct     | MIT                        |
| github.com/go-logr/logr                                                      | v1.4.3                                | direct     | Apache-2.0                 |
| github.com/go-logr/stdr                                                      | v1.2.2                                | indirect   | Apache-2.0                 |
| github.com/go-ole/go-ole                                                     | v1.3.0                                | indirect   | MIT                        |
| github.com/go-sourcemap/sourcemap                                            | v2.1.4                                | indirect   | BSD-2-Clause               |
| github.com/go-viper/mapstructure/v2                                          | v2.5.0                                | indirect   | MIT                        |
| github.com/go-webauthn/webauthn                                              | v0.18.0                               | direct     | BSD-3-Clause               |
| github.com/go-webauthn/x/crypto/secp256k1                                    | v0.3.0                                | indirect   | ISC                        |
| github.com/go-webauthn/x/encoding/asn1                                       | v0.3.0                                | indirect   | BSD-3-Clause               |
| github.com/go-webauthn/x/revoke                                              | v0.3.0                                | indirect   | BSD-2-Clause               |
| github.com/go-xmlfmt/xmlfmt                                                  | v1.1.3                                | direct     | MIT                        |
| github.com/goccy/go-json                                                     | v0.10.6                               | indirect   | MIT                        |
| github.com/gofrs/uuid                                                        | v4.4.0                                | indirect   | MIT                        |
| github.com/golang-jwt/jwt/v4                                                 | v4.5.2                                | indirect   | MIT                        |
| github.com/golang-jwt/jwt/v5                                                 | v5.3.1                                | indirect   | MIT                        |
| github.com/golang/groupcache/lru                                             | v0.0.0-20241129210726-2c02b8208cf8    | indirect   | Apache-2.0                 |
| github.com/google/go-tpm                                                     | v0.9.8                                | indirect   | Apache-2.0                 |
| github.com/google/pprof/profile                                              | v0.0.0-20260802141513-ef3492d7dac3    | indirect   | Apache-2.0                 |
| github.com/google/s2a-go                                                     | v0.1.9                                | indirect   | Apache-2.0                 |
| github.com/google/uuid                                                       | v1.6.0                                | indirect   | BSD-3-Clause               |
| github.com/google/wire                                                       | v0.7.0                                | indirect   | Apache-2.0                 |
| github.com/googleapis/enterprise-certificate-proxy/client                    | v0.3.14                               | indirect   | Apache-2.0                 |
| github.com/googleapis/gax-go/v2                                              | v2.19.0                               | indirect   | BSD-3-Clause               |
| github.com/gorilla/css/scanner                                               | v1.0.1                                | indirect   | BSD-3-Clause               |
| github.com/gorilla/mux                                                       | v1.8.1                                | direct     | BSD-3-Clause               |
| github.com/gorilla/websocket                                                 | v1.5.3                                | direct     | BSD-2-Clause               |
| github.com/gosimple/slug                                                     | v1.15.0                               | direct     | MPL-2.0                    |
| github.com/gosimple/unidecode                                                | v1.0.1                                | indirect   | Apache-2.0                 |
| github.com/grantae/certinfo                                                  | v0.0.0-20170412194111-59d56a35515b    | direct     | MIT                        |
| github.com/hbollon/go-edlib                                                  | v1.7.0                                | indirect   | MIT                        |
| github.com/huandu/xstrings                                                   | v1.5.0                                | indirect   | MIT                        |
| github.com/inbucket/html2text                                                | v1.0.0                                | indirect   | MIT                        |
| github.com/jackc/pgpassfile                                                  | v1.0.0                                | indirect   | MIT                        |
| github.com/jackc/pgservicefile                                               | v0.0.0-20240606120523-5a60cdf6a761    | indirect   | MIT                        |
| github.com/jackc/pgx/v5                                                      | v5.11.0                               | direct     | MIT                        |
| github.com/jackc/puddle/v2                                                   | v2.2.2                                | indirect   | MIT                        |
| github.com/jbenet/go-context/io                                              | v0.0.0-20150711004518-d14ea06fba99    | direct     | MIT                        |
| github.com/jonboulle/clockwork                                               | v0.5.0                                | indirect   | Apache-2.0                 |
| github.com/josharian/intern                                                  | v1.0.0                                | indirect   | MIT                        |
| github.com/kardianos/service                                                 | v1.3.0                                | direct     | Zlib                       |
| github.com/kataras/tablewriter                                               | v0.0.0-20180708051242-e063d29b7c23    | indirect   | MIT                        |
| github.com/klauspost/cpuid/v2                                                | v2.3.0                                | indirect   | MIT                        |
| github.com/kylelemons/godebug                                                | v1.1.0                                | indirect   | Apache-2.0                 |
| github.com/landoop/tableprinter                                              | v0.0.0-20201125135848-89e81fc956e7    | direct     | Apache-2.0                 |
| github.com/libdns/libdns                                                     | v1.1.1                                | indirect   | MIT                        |
| github.com/logrusorgru/aurora                                                | v2.0.3                                | indirect   | Unlicense                  |
| github.com/lucasb-eyer/go-colorful                                           | v1.4.1                                | direct     | MIT                        |
| github.com/mailru/easyjson                                                   | v0.9.2                                | indirect   | MIT                        |
| github.com/mattermost/xml-roundtrip-validator                                | v0.1.0                                | direct     | Apache-2.0                 |
| github.com/mattn/go-colorable                                                | v0.1.14                               | indirect   | MIT                        |
| github.com/mattn/go-isatty                                                   | v0.0.24                               | indirect   | MIT                        |
| github.com/mattn/go-runewidth                                                | v0.0.23                               | indirect   | MIT                        |
| github.com/mattn/go-shellwords                                               | v1.0.14                               | direct     | MIT                        |
| github.com/mattn/go-sqlite3                                                  | v1.14.50                              | direct     | MIT                        |
| github.com/mholt/acmez/v3                                                    | v3.1.6                                | direct     | Apache-2.0                 |
| github.com/miekg/dns                                                         | v1.1.72                               | indirect   | BSD-3-Clause               |
| github.com/mitchellh/copystructure                                           | v1.2.0                                | indirect   | MIT                        |
| github.com/mitchellh/reflectwalk                                             | v1.0.2                                | indirect   | MIT                        |
| github.com/mmcloughlin/geohash                                               | v0.10.0                               | direct     | MIT                        |
| github.com/munnerz/goautoneg                                                 | v0.0.0-20191010083416-a7dc8b61c822    | indirect   | BSD-3-Clause               |
| github.com/ncruces/go-strftime                                               | v1.0.0                                | indirect   | MIT                        |
| github.com/nfnt/resize                                                       | v0.0.0-20180221191011-83c6a9932646    | direct     | ISC                        |
| github.com/olekukonko/cat                                                    | v0.0.0-20250911104152-50322a0618f6    | indirect   | MIT                        |
| github.com/olekukonko/errors                                                 | v1.3.0                                | indirect   | MIT                        |
| github.com/olekukonko/ll                                                     | v0.1.8                                | indirect   | MIT                        |
| github.com/olekukonko/tablewriter                                            | v1.1.4                                | direct     | MIT                        |
| github.com/olivere/elastic/v7/config                                         | v7.0.32                               | indirect   | MIT                        |
| github.com/olivere/elastic/v7/uritemplates                                   | v7.0.32                               | indirect   | MIT                        |
| github.com/pb33f/jsonpath/pkg/jsonpath                                       | v0.8.2                                | indirect   | Apache-2.0                 |
| github.com/pb33f/libopenapi                                                  | v0.38.7                               | direct     | MIT                        |
| github.com/pb33f/ordered-map/v2                                              | v2.3.1                                | indirect   | Apache-2.0                 |
| github.com/philhofer/fwd                                                     | v1.2.0                                | indirect   | MIT                        |
| github.com/pkg/browser                                                       | v0.0.0-20240102092130-5ac0b6a4141c    | indirect   | BSD-2-Clause               |
| github.com/pkg/errors                                                        | v0.9.1                                | direct     | BSD-2-Clause               |
| github.com/pquerna/otp                                                       | v1.5.0                                | direct     | Apache-2.0                 |
| github.com/programmfabrik/elastic/v7                                         | v7.0.31-0.20220107153946-70fc46807afe | direct     | MIT                        |
| github.com/programmfabrik/fylr-build-plugin/pluginseal                       | v1.9.0                                | direct     | Unlicense                  |
| github.com/programmfabrik/go-datasize                                        | v0.0.0-20230103131654-7145e216c8b9    | direct     | MIT                        |
| github.com/programmfabrik/go-email                                           | v0.0.0-20230712170028-d40481e23141    | direct     | MIT                        |
| github.com/programmfabrik/go-iso8601                                         | v0.0.0-20260908085253-529901e90db0    | direct     | MIT                        |
| github.com/programmfabrik/sqlpro                                             | v0.0.0-20261021190854-5b171ee6da1b    | direct     | MIT                        |
| github.com/prometheus/client_golang/internal/github.com/golang/gddo/httputil | v1.24.1                               | direct     | BSD-3-Clause               |
| github.com/prometheus/client_golang/prometheus                               | v1.24.1                               | direct     | Apache-2.0                 |
| github.com/prometheus/client_model/go                                        | v0.6.2                                | indirect   | Apache-2.0                 |
| github.com/prometheus/common                                                 | v0.70.1                               | indirect   | Apache-2.0                 |
| github.com/prometheus/procfs                                                 | v0.21.1                               | indirect   | Apache-2.0                 |
| github.com/remyoudompheng/bigfft                                             | v0.0.0-20230129092748-24d4a6f8daec    | indirect   | BSD-3-Clause               |
| github.com/richardlehane/mscfb                                               | v1.0.7                                | indirect   | Apache-2.0                 |
| github.com/richardlehane/msoleps/types                                       | v1.0.6                                | indirect   | Apache-2.0                 |
| github.com/robert-nix/ansihtml                                               | v1.0.1                                | direct     | MIT                        |
| github.com/rs/zerolog                                                        | v1.35.1                               | direct     | MIT                        |
| github.com/russellhaering/goxmldsig                                          | v1.6.1                                | direct     | Apache-2.0                 |
| github.com/saintfish/chardet                                                 | v0.0.0-20230101081208-5e3ef4b5456d    | direct     | MIT                        |
| github.com/shirou/gopsutil/v4                                                | v4.26.7                               | direct     | BSD-3-Clause               |
| github.com/shopspring/decimal                                                | v1.4.0                                | indirect   | MIT                        |
| github.com/skip2/go-qrcode                                                   | v0.0.0-20200617195104-da1b6568686e    | direct     | MIT                        |
| github.com/spf13/cast                                                        | v1.10.0                               | indirect   | MIT                        |
| github.com/ssor/bom                                                          | v0.0.0-20170718123548-6386211fdfcf    | indirect   | MIT                        |
| github.com/theplant/cldr                                                     | v0.0.0-20190423050709-9f76f7ce4ee8    | direct     | MIT                        |
| github.com/tidwall/gjson                                                     | v1.19.0                               | direct     | MIT                        |
| github.com/tidwall/match                                                     | v1.2.0                                | indirect   | MIT                        |
| github.com/tidwall/pretty                                                    | v1.2.1                                | indirect   | MIT                        |
| github.com/tidwall/sjson                                                     | v1.2.5                                | direct     | MIT                        |
| github.com/tiendc/go-deepcopy                                                | v1.7.2                                | indirect   | MIT                        |
| github.com/tinylib/msgp/msgp                                                 | v1.6.4                                | indirect   | MIT                        |
| github.com/tredoe/osutil/user/crypt                                          | v1.5.0                                | direct     | BSD-2-Clause               |
| github.com/twpayne/go-geom                                                   | v1.6.1                                | direct     | BSD-2-Clause               |
| github.com/vanng822/css                                                      | v1.0.1                                | indirect   | MIT                        |
| github.com/vanng822/go-premailer/premailer                                   | v1.35.0                               | direct     | MIT                        |
| github.com/x448/float16                                                      | v0.8.4                                | indirect   | MIT                        |
| github.com/xuri/efp                                                          | v0.0.1                                | indirect   | BSD-3-Clause               |
| github.com/xuri/excelize/v2                                                  | v2.11.0                               | direct     | BSD-3-Clause               |
| github.com/xuri/nfp                                                          | v0.0.2-0.20250530014748-2ddeb826f9a9  | indirect   | BSD-3-Clause               |
| github.com/yudai/pp                                                          | v2.0.1                                | indirect   | Unknown                    |
| github.com/yuin/goldmark                                                     | v1.8.5                                | direct     | MIT                        |
| github.com/yusufpapurcu/wmi                                                  | v1.2.4                                | indirect   | MIT                        |
| github.com/zeebo/blake3                                                      | v0.2.4                                | indirect   | CC0-1.0                    |
| go.opentelemetry.io/auto/sdk                                                 | v1.2.1                                | indirect   | Apache-2.0                 |
| go.opentelemetry.io/otel                                                     | v1.44.0                               | indirect   | Apache-2.0 OR BSD-3-Clause |
| go.opentelemetry.io/otel/metric                                              | v1.44.0                               | indirect   | Apache-2.0 OR BSD-3-Clause |
| go.opentelemetry.io/otel/sdk                                                 | v1.44.0                               | indirect   | Apache-2.0 OR BSD-3-Clause |
| go.opentelemetry.io/otel/sdk/metric                                          | v1.44.0                               | indirect   | Apache-2.0 OR BSD-3-Clause |
| go.opentelemetry.io/otel/trace                                               | v1.44.0                               | indirect   | Apache-2.0 OR BSD-3-Clause |
| go.uber.org/multierr                                                         | v1.11.0                               | indirect   | MIT                        |
| go.uber.org/zap                                                              | v1.28.0                               | direct     | MIT                        |
| go.uber.org/zap/exp/zapslog                                                  | v0.3.0                                | indirect   | MIT                        |
| go.yaml.in/yaml/v4                                                           | v4.0.0-rc.6                           | direct     | Apache-2.0                 |
| gocloud.dev                                                                  | v0.46.0                               | direct     | Apache-2.0                 |
| golang.org/x/crypto                                                          | v0.55.0                               | direct     | BSD-3-Clause               |
| golang.org/x/image                                                           | v0.45.0                               | direct     | BSD-3-Clause               |
| golang.org/x/mod                                                             | v0.40.0                               | direct     | BSD-3-Clause               |
| golang.org/x/net                                                             | v0.58.0                               | direct     | BSD-3-Clause               |
| golang.org/x/oauth2                                                          | v0.36.0                               | direct     | BSD-3-Clause               |
| golang.org/x/sync                                                            | v0.22.0                               | direct     | BSD-3-Clause               |
| golang.org/x/sys                                                             | v0.47.0                               | direct     | BSD-3-Clause               |
| golang.org/x/text                                                            | v0.41.0                               | direct     | BSD-3-Clause               |
| golang.org/x/tools/godoc/vfs                                                 | v0.1.0-deprecated                     | direct     | BSD-3-Clause               |
| golang.org/x/xerrors                                                         | v0.0.0-20240903120638-7835f813f4da    | indirect   | BSD-3-Clause               |
| google.golang.org/api                                                        | v0.272.0                              | indirect   | BSD-3-Clause               |
| google.golang.org/api/internal/third_party/uritemplates                      | v0.272.0                              | indirect   | BSD-3-Clause               |
| google.golang.org/genproto/googleapis/rpc                                    | v0.0.0-20260526163538-3dc84a4a5aaa    | indirect   | Apache-2.0                 |
| google.golang.org/grpc                                                       | v1.83.1                               | indirect   | Apache-2.0                 |
| google.golang.org/protobuf                                                   | v1.36.11                              | indirect   | BSD-3-Clause               |
| modernc.org/libc                                                             | v1.74.4                               | indirect   | BSD-3-Clause               |
| modernc.org/mathutil                                                         | v1.7.1                                | indirect   | BSD-3-Clause               |
| modernc.org/memory                                                           | v1.11.0                               | indirect   | BSD-3-Clause               |
| modernc.org/sqlite                                                           | v1.57.0                               | direct     | BSD-3-Clause               |

### Not in every build

These components are linked into some of the binaries only. `+cgo` is the
binary of the container images, the others are the downloads.

| Module                           | Builds                                                 |
|----------------------------------|--------------------------------------------------------|
| github.com/ebitengine/purego     | darwin/amd64, darwin/arm64                             |
| github.com/go-ole/go-ole         | windows/amd64                                          |
| github.com/mattn/go-sqlite3      | linux/amd64+cgo                                        |
| github.com/ncruces/go-strftime   | darwin/amd64, darwin/arm64, windows/amd64              |
| github.com/prometheus/procfs     | linux/amd64+cgo, linux/amd64                           |
| github.com/remyoudompheng/bigfft | darwin/amd64, darwin/arm64, linux/amd64, windows/amd64 |
| github.com/yusufpapurcu/wmi      | windows/amd64                                          |
| modernc.org/libc                 | darwin/amd64, darwin/arm64, linux/amd64, windows/amd64 |
| modernc.org/mathutil             | darwin/amd64, darwin/arm64, linux/amd64, windows/amd64 |
| modernc.org/memory               | darwin/amd64, darwin/arm64, linux/amd64, windows/amd64 |
| modernc.org/sqlite               | darwin/amd64, darwin/arm64, linux/amd64, windows/amd64 |

## The web frontend

15 components, as the build of the web frontend lists them: the npm packages
coffeescript-ui bundles into `cui.min.js` and the files in the frontend's
`thirdparty/` directory. The frontend's own `package.json` has no runtime
dependencies — everything in it is build tooling that never reaches the
browser.

| Component                         | Version | Description                                                                                                                                                                                                                                                                              | License               |
|-----------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| ace-builds                        | 1.44.0  | Ace (Ajax.org Cloud9 Editor)                                                                                                                                                                                                                                                             | BSD-3-Clause          |
| blurhash-js                       | —       | Decodes blurhash placeholders in the browser while the real image loads                                                                                                                                                                                                                  | MIT                   |
| bowser                            | —       | Browser detection                                                                                                                                                                                                                                                                        | MIT                   |
| chroma.js                         | 2.4.2   | Color conversions for the theming and color-picker widgets                                                                                                                                                                                                                               | BSD-3-Clause          |
| coordinate-parser                 | 1.0.7   | Geographical coordinate parser                                                                                                                                                                                                                                                           | Apache-2.0            |
| dompurify                         | 3.4.15  | DOMPurify is a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG. It runs as JavaScript and works in all modern browsers, as well as in Node.js (via jsdom). DOMPurify is written by security people who have vast background in web attacks and XSS. Fear not. | MPL-2.0 OR Apache-2.0 |
| email-addresses                   | 5.0.0   | An email address parser based on rfc5322                                                                                                                                                                                                                                                 | MIT                   |
| font-awesome                      | 4.7.0   | The icon set used across the frontend                                                                                                                                                                                                                                                    | OFL-1.1 AND MIT       |
| formatcoords                      | 1.1.3   | format decimal lat/lon coords into degrees/minutes/seconds formats (like DMS).                                                                                                                                                                                                           | ISC                   |
| leaflet                           | 1.9.4   | JavaScript library for mobile-friendly interactive maps                                                                                                                                                                                                                                  | BSD-2-Clause          |
| leaflet-defaulticon-compatibility | 0.1.2   | Retrieve all Leaflet Default Icon options from CSS, in particular all icon images URL's, to improve compatibility with bundlers and frameworks that modify URL's in CSS.                                                                                                                 | BSD-2-Clause          |
| load-google-maps-api              | 1.3.3   | A thin, Promise-returning helper for loading the Google Maps JavaScript API.                                                                                                                                                                                                             | MIT                   |
| marked                            | 18.0.5  | A markdown parser built for speed                                                                                                                                                                                                                                                        | MIT                   |
| moment                            | 2.30.1  | Parse, validate, manipulate, and display dates                                                                                                                                                                                                                                           | MIT                   |
| moment-timezone                   | 0.6.2   | Parse and display moments in any timezone.                                                                                                                                                                                                                                               | MIT                   |
