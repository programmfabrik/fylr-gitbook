#!/bin/bash

# Tests _assets/maintain and the release records in _assets/releases on a host
# with docker and the compose plugin. Run as root; .github/workflows/
# maintain-test.yml runs it when one of them changes.
#
# R checks every release record: its format, and that the registry has the
# images it names.
# B drives the update with its own release records and the small fylr-server
# image: a first update, the next release, the cases that are refused.
# A installs fylr as the Linux installation page says, with the release records
# of this checkout, and runs what the cron jobs run.

set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
pass=0; fail=0
ok(){ echo "ok    $*"; pass=$((pass+1)); }
no(){ echo "FAIL  $*"; fail=$((fail+1)); }
check(){ # check <description> <command...>: the command succeeds
    local d=$1; shift
    if "$@" >/dev/null 2>&1; then ok "$d"; else no "$d"; fi
}
checknot(){ # checknot <description> <command...>: the command fails
    local d=$1; shift
    if "$@" >/dev/null 2>&1; then no "$d"; else ok "$d"; fi
}
same(){ # same <description> <got> <want>
    if [ -n "$2" ] && [ "$2" = "$3" ]; then ok "$1"; else no "$1 (got '$2', want '$3')"; fi
}
section(){ echo; echo "=== $*"; }
run(){ # run <maintain args>: output in $OUT, status in $RC
    OUT=$("$MAINTAIN" "$@" 2>&1); RC=$?
    [ -n "$OUT" ] && echo "$OUT" | sed 's/^/      | /' | cut -c1-240
}
says(){ # says <description> <text>: the last run printed the text
    if grep -qF -- "$2" <<<"$OUT"; then ok "$1"; else no "$1 (no '$2' in the output)"; fi
}

echo "docker $(docker version --format '{{.Server.Version}}'), $(docker compose version), bash $BASH_VERSION"
docker info --format 'storage driver {{.Driver}}, {{.DriverStatus}}' | cut -c1-160
df -h / | tail -1

FS=docker.fylr.io/fylr/fylr-server
# fylr-server 6.35.2 and 6.35.3, as their releases pushed them
OLD=$FS@sha256:e8c85584ecf3a5d0498d016e834263256134cbd4b6dad53c53c0a4efe2dc0bf2
NEW=$FS@sha256:cb298ba3dd0e31b2fe6ef6b9511862d541eb88425fb35824b0d1124b45620a8f
GONE=$FS@sha256:0000000000000000000000000000000000000000000000000000000000000000

record(){ # record <tag> <version> <serial> <required> <current> <image>...
    local tag=$1
    {
        echo "fylr-release 1"; echo "tag $1"; echo "version $2"; echo "serial $3"
        echo "maintain-required $4"; echo "maintain-current $5"
        shift 5; for i; do echo "image $i"; done
    } > "$B/www/$tag"
}
image_of(){ docker inspect --format '{{.Image}}' "$1" 2>/dev/null; }      # image id a container runs
id_of(){ docker image inspect --format '{{.Id}}' "$1" 2>/dev/null; }      # image id of a reference
container_of(){ docker inspect --format '{{.Id}}' "$1" 2>/dev/null; }

########################################################################
section "R: the release records in _assets/releases"

ACCEPT="application/vnd.docker.distribution.manifest.v2+json, application/vnd.oci.image.manifest.v1+json, application/vnd.docker.distribution.manifest.list.v2+json, application/vnd.oci.image.index.v1+json"
for f in "$REPO"/_assets/releases/*; do
    tag=$(basename "$f")
    if [ "$(head -1 "$f")" != "fylr-release 1" ] || [ "$(sed -n 's/^tag //p' "$f")" != "$tag" ] || ! grep -q '^serial [0-9][0-9]*$' "$f"; then
        no "$tag: not a release record of its tag"
        continue
    fi
    images=$(sed -n 's/^image //p' "$f")
    bad=""
    [ -n "$images" ] || bad=" names no image;"
    for image in $images; do
        if ! [[ "$image" =~ ^docker\.fylr\.io/(fylr/[a-z-]+)@(sha256:[0-9a-f]{64})$ ]]; then
            bad="$bad $image is not an image of docker.fylr.io/fylr by digest;"
            continue
        fi
        code=$(curl -s -o /dev/null -w '%{http_code}' -m 30 -H "Accept: $ACCEPT" "https://docker.fylr.io/v2/${BASH_REMATCH[1]}/manifests/${BASH_REMATCH[2]}")
        [ "$code" = 200 ] || bad="$bad the registry answers $code for $image;"
    done
    if [ -z "$bad" ]; then ok "$tag: $(sed -n 's/^version //p' "$f"), the registry has its images"; else no "$tag:$bad"; fi
done

########################################################################
section "B: updates with own release records, fylr-server image"

B=/srv/fylr-b; mkdir -p $B/www
MAINTAIN=$B/maintain
install -m 755 "$REPO/_assets/maintain" $MAINTAIN
cat > /etc/default/fylr <<EOF
BASEDIR=$B
MYLOG=$B/maintain.log
RELEASES_URL=http://127.0.0.1:8099
EOF
cat > $B/docker-compose.yml <<EOF
services:
  fylr:
    image: $FS:latest
    container_name: fylr-b
    entrypoint: ["sleep", "infinity"]
EOF
( cd $B/www && exec python3 -m http.server 8099 --bind 127.0.0.1 >/dev/null 2>&1 ) &
SERVER=$!
sleep 1
echo "compose lists the images as: $(cd $B && docker compose config --images | tr '\n' ' ')"

section "B1: a fresh host and no release record"
run update
same     "update fails" "$RC" 1
says     "it says that the tag has no release record" "there is no release record for the tag 'latest'"
checknot "compose did not pull the image by its tag" docker image inspect $FS:latest
checknot "no container was started" docker inspect fylr-b

section "B2: the record names 6.35.2, the registry's latest is 6.35.3"
record latest v6.35.2 100 1 1 $OLD
run update
same  "update succeeds" "$RC" 0
check "the container runs" test "$(docker inspect --format '{{.State.Running}}' fylr-b)" = true
same  "the container runs the image of the record" "$(image_of fylr-b)" "$(id_of $OLD)"
same  "the tag on the host is that image" "$(id_of $FS:latest)" "$(id_of $OLD)"
C=$(container_of fylr-b)

section "B3: update again with the same record"
run update
same "update succeeds" "$RC" 0
same "the container was not recreated" "$(container_of fylr-b)" "$C"

section "B4: the next release"
OLDID=$(id_of $OLD)
record latest v6.35.3 200 1 1 $NEW
run update
same     "update succeeds" "$RC" 0
same     "the container runs the new image" "$(image_of fylr-b)" "$(id_of $NEW)"
checknot "the old image is gone by its digest" docker image inspect $OLD
checknot "the old image is gone by its id" docker image inspect "$OLDID"
C=$(container_of fylr-b)

section "B5: an older record is served again"
record latest v6.35.2 100 1 1 $OLD
run update
same "update fails" "$RC" 1
says "it says the record is older" "is older than the release installed here"
same "the container still runs the new image" "$(image_of fylr-b)" "$(id_of $NEW)"
same "the container was not recreated" "$(container_of fylr-b)" "$C"

section "B6: going back on purpose"
OUT=$(MAINTAIN_ALLOW_DOWNGRADE=1 $MAINTAIN update 2>&1); RC=$?
[ -n "$OUT" ] && echo "$OUT" | sed 's/^/      | /' | cut -c1-240
same "update succeeds" "$RC" 0
same "the container runs 6.35.2 again" "$(image_of fylr-b)" "$(id_of $OLD)"
C=$(container_of fylr-b)

section "B7: the record names an image the registry does not have"
record latest v6.35.9 300 1 1 $GONE
run update
same  "update fails" "$RC" 1
says  "it says it cannot pull" "cannot pull $GONE"
same  "the container still runs its image" "$(image_of fylr-b)" "$(id_of $OLD)"
same  "the container was not recreated" "$(container_of fylr-b)" "$C"
check "the container still runs" test "$(docker inspect --format '{{.State.Running}}' fylr-b)" = true

section "B8: the record names an image in another registry"
record latest v6.35.9 310 1 1 "ghcr.io/example/fylr-server@sha256:${NEW##*:}"
run update
same "update fails" "$RC" 1
says "it says the record names no image" "names no image for $FS"
same "the container was not recreated" "$(container_of fylr-b)" "$C"

section "B9: a release needs a newer script"
record latest v6.36.0 400 2 2 $NEW
run update
same "update fails" "$RC" 1
says "it says it is deprecated" "is DEPRECATED and can no longer update fylr"
same "the container was not recreated" "$(container_of fylr-b)" "$C"
run recreate-fylr
says "another command says it too" "is DEPRECATED and can no longer update fylr"
record latest v6.35.3 500 1 2 $NEW
run update
same "with a record it can read, update succeeds" "$RC" 0
says "it says a newer script exists" "a newer maintain script (version 2) is available"
same "the container runs 6.35.3" "$(image_of fylr-b)" "$(id_of $NEW)"
run recreate-fylr
if grep -q DEPRECATED <<<"$OUT"; then no "the deprecation is gone"; else ok "the deprecation is gone"; fi

section "B10: pull and update-fylr"
run pull
same "pull succeeds" "$RC" 0
C=$(container_of fylr-b)
run update-fylr
same "update-fylr succeeds" "$RC" 0
check "update-fylr recreated the container" test "$(container_of fylr-b)" != "$C"
same  "on the image of the record" "$(image_of fylr-b)" "$(id_of $NEW)"

section "B11: a tag without release records"
sed -i "s#image: $FS:latest#image: $FS:v6.35.1#" $B/docker-compose.yml
run update
same     "update fails" "$RC" 1
says     "it names the tag" "there is no release record for the tag 'v6.35.1'"
checknot "the image was not pulled by its tag" docker image inspect $FS:v6.35.1
echo 'UNVERIFIED_TAGS="v6.35.1"' >> /etc/default/fylr
run update
same  "named in UNVERIFIED_TAGS, update succeeds" "$RC" 0
same  "the container runs the image of the tag" "$(image_of fylr-b)" "$(id_of $FS:v6.35.1)"

echo; echo "images after part B:"; docker images --digests --format '      {{.Repository}}:{{.Tag}} {{.Digest}} {{.ID}}' | cut -c1-150
echo "state file:"; sed 's/^/      /' $B/.maintain-state | cut -c1-170
( cd $B && docker compose down >/dev/null 2>&1 )
kill $SERVER 2>/dev/null
docker image prune -af >/dev/null 2>&1

########################################################################
section "A: an installation as the Linux installation page says, records of this checkout"

# The records of this checkout, not the ones on main: right after a push the
# raw files of main can be minutes behind.
( cd "$REPO/_assets/releases" && exec python3 -m http.server 8099 --bind 127.0.0.1 >/dev/null 2>&1 ) &
SERVER=$!
echo 'RELEASES_URL=http://127.0.0.1:8099' > /etc/default/fylr
echo "vm.max_map_count=262144" >> /etc/sysctl.d/99-memory_for_indexer.conf
sysctl -q -p /etc/sysctl.d/99-memory_for_indexer.conf
mkdir -p /srv/fylr; cd /srv/fylr
mkdir -p config/fylr postgres assets backups sqlbackups indexer migration
chown 1000 assets backups indexer migration
chown  999 postgres sqlbackups
cp "$REPO/_assets/fylr.yml" config/fylr/fylr.yml
cp "$REPO/_assets/docker-compose.yml" docker-compose.yml
install -m 755 "$REPO/_assets/maintain" maintain
MAINTAIN=/srv/fylr/maintain

# http://localhost without a certificate, as "No HTTPS" on the HTTP and HTTPS page
python3 - config/fylr/fylr.yml <<'PY'
import sys
p = sys.argv[1]; s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)
rep('externalURL: "https://EXAMPLE.COM"', 'externalURL: "http://localhost"')
rep('''      addr: ":443"
      tls:
        forwardHttpAddr: ":80"
        letsEncrypt:
          email: you@EXAMPLE.COM
          useStagingCA: false
''', '''      addr: ":80"
      tls:
''')
rep('''        signingSecret: "EXAMPLE8901234567890123456789023"
''', '''        signingSecret: "EXAMPLE8901234567890123456789023"
        allowHttpRedirects: true
        clients+:
          fylr-web-frontend+:
            redirectURIs:
              - http://localhost/oauth2/callback
''')
open(p, "w").write(s)
PY

F=docker.fylr.io/fylr/fylr
WANT=$(sed -n "s#^image \($F@sha256:[0-9a-f]*\)\$#\1#p" "$REPO/_assets/releases/latest")
echo "the record of latest names $WANT ($(sed -n 's/^version //p' "$REPO/_assets/releases/latest"))"

section "A1: the images, pulled by maintain before the first start"
run pull
same  "pull succeeds" "$RC" 0
same  "the fylr image on the host is the one of the record" "$(id_of $F:latest)" "$(id_of "$WANT")"

section "A2: the first start, in the order of the installation page"
docker compose up -d postgresql opensearch 2>&1 | tail -2 | sed 's/^/      | /'
for i in $(seq 1 72); do
    docker exec opensearch curl -fsS http://localhost:9200/_cluster/health >/dev/null 2>&1 && break
    sleep 5
done
check "opensearch answers" docker exec opensearch curl -fsS http://localhost:9200/_cluster/health
docker compose up -d fylr 2>&1 | tail -2 | sed 's/^/      | /'
same  "fylr runs the image of the record" "$(image_of fylr)" "$(id_of "$WANT")"

section "A3: fylr answers"
version=""
for i in $(seq 1 120); do
    version=$(curl -fsS -m 5 http://localhost/api/v1/settings 2>/dev/null | python3 -c 'import json,sys; print(json.load(sys.stdin).get("version", ""))' 2>/dev/null)
    [ -n "$version" ] && break
    [ "$(docker inspect --format '{{.State.Running}}' fylr 2>/dev/null)" = true ] || break
    sleep 5
done
same "GET /api/v1/settings answers with the version of the record" "$version" "$(sed -n 's/^version //p' "$REPO/_assets/releases/latest")"
echo "      fylr container: $(docker inspect --format '{{.State.Status}}, exit code {{.State.ExitCode}}' fylr 2>&1)"

section "A4: the nightly cron job: backup and update"
C=$(container_of fylr)
run backup
same  "backup succeeds" "$RC" 0
check "a dump is in sqlbackups" bash -c 'ls /srv/fylr/sqlbackups/fylr.*.pgdump'
run update
same  "update succeeds" "$RC" 0
same  "fylr was not recreated" "$(container_of fylr)" "$C"
check "fylr still answers" curl -fsS -m 10 http://localhost/api/v1/settings

section "A5: the weekly cleanup"
run cleanup
same  "fylr still runs the image of the record" "$(image_of fylr)" "$(id_of "$WANT")"
check "the image is still there by its tag" docker image inspect $F:latest
check "fylr still answers" curl -fsS -m 10 http://localhost/api/v1/settings

if [ $fail -gt 0 ]; then
    echo; echo "--- maintain log"; tail -40 /var/log/fylr-maintain.log 2>/dev/null | cut -c1-200
    echo "--- containers"; docker ps -a --format '      {{.Names}} {{.Image}} {{.Status}}'
    echo "--- fylr, errors and the last lines"
    journalctl CONTAINER_NAME=fylr --no-pager 2>/dev/null | grep -E " (ERR|FTL|PNC) |panic|FYLR started" | head -25 | cut -c1-260
    journalctl CONTAINER_NAME=fylr -n 12 --no-pager 2>/dev/null | cut -c1-220
fi

kill $SERVER 2>/dev/null
echo; echo "$pass passed, $fail failed"
[ $fail -eq 0 ]
