---
description: Arrange docker and a reverse proxy to avoid conflicts with multiple fylrs
---

# multiple fylrs in one Linux

Our default recommended fylr Installation has one fylr directly listening to port 443/80 for http(s). If you want multiple fylrs you need to direct web traffic to the correct one. We present one example here with Apache webserver used as reverse proxy.

{% hint style="info" %}
This increases the risk to run into resource and performance issues (except for small fylr instances with few traffic on a big server).&#x20;
{% endhint %}

To somewhat reduce performance issues, only one indexer and only one PostgreSQL is used for all fylrs in this example.



## Prerequisites

* install [docker](https://docs.docker.com/engine/install/#server)
*   install [certbot](https://certbot.eff.org/)\
    e.g. for Debian 12:\
    `apt install -y snapd`

    log out and back in again, to ensure snap’s paths are updated correctly\
    `snap install snapd`\
    `apt-get remove certbot`\
    `snap install --classic certbot`\
    `type -a certbot || ln -s /snap/bin/certbot /usr/local/bin/`
* install Apache 2\
  e.g. for Debian 12: `apt-get install -y apache2 ; a2enmod ssl rewrite proxy_http`



## Prepare Linux for fylr

We assume `bash` and Debian 12 in our examples.

```
mkdir /srv/fylr ; cd /srv/fylr
echo "vm.max_map_count=262144" >> /etc/sysctl.d/99-memory_for_indexer.conf
sysctl -p /etc/sysctl.d/99-memory_for_indexer.conf
mkdir -p postgres indexer sqlbackups
chown  999 postgres sqlbackups
chown 1000 indexer
swapoff -a; free -h
```

## Download all and configure common services

Use this example `docker-compose.yml` as a starting point:

```
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/multi/docker-compose.yml -o docker-compose.yml
```

Replace all strings that have `EXAMPLE` in it. E.g. with vim: `vim docker-compose.yml`

Download all software and start the indexer and SQL database service:

```
docker compose pull
docker compose up -d postgresql opensearch
```

## For each fylr instance

Choose unique names and ports and put them into bash variables. Use the same as you used in `docker-compose.yml`.

```
DIR=fylr-EXAMPLE1     # directory name below /srv/fylr/
SERVICE=fylr-EXAMPLE1 # name in docker-compose.yml
DOMAIN=EXAMPLE1.COM
PORT=81
DB=EXAMPLE1
DBUSER=EXAMPLE1
```

#### Configure the reverse proxy:

```
cd /etc/apache2/sites-enabled
cat >>../sites-available/$DOMAIN.conf<<EOF
<VirtualHost *:80>
    ServerName $DOMAIN
    ServerAdmin administratoren@programmfabrik.de
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:$PORT/ upgrade=websocket
    ProxyPassReverse / http://127.0.0.1:$PORT/ upgrade=websocket
</VirtualHost>
EOF
ln -s ../sites-available/$DOMAIN.conf .
apache2ctl -t && systemctl restart apache2
certbot --apache --agree-tos -d $DOMAIN # -m emailadress
```

... certbot in the last command will configure the https part of the reverse proxy in Apache.

#### Configure fylr:

```
cd /srv/fylr
mkdir -p $DIR/config/fylr $DIR/assets $DIR/migration $DIR/backups
chown 1000 $DIR/assets $DIR/backups $DIR/migration
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/multi/fylr.yml -o $DIR/config/fylr/fylr.yml
vi $DIR/config/fylr/fylr.yml  # replace string with EXAMPLE
```

Replace all strings in `fylr.yml` that have `EXAMPLE` in it. E.g. with vim: \
`vim $DIR/config/fylr/fylr.yml`

#### Create SQL database:

```
PSQL="docker compose exec postgresql psql -U fylr"
$PSQL -c 'CREATE DATABASE "'$DB'";'

$PSQL -c "CREATE USER $DBUSER WITH LOGIN ENCRYPTED PASSWORD '$DBUSER';"

$PSQL -c 'GRANT ALL PRIVILEGES ON DATABASE '$DB' TO '$DBUSER';'

$PSQL -c 'ALTER DATABASE '$DB' OWNER TO '$DBUSER';'
```

#### Start this fylr instance:

```
docker compose up -d $SERVICE
```

## Remarks

A maintain script and cron job, as in the [default recommended installation](./), are not provided by us, as we do not have sufficient experience with this multi-fylr-setup. This should also tell you to be cautious and use the recommended installation instead, when possible.
