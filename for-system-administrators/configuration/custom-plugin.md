# How to load your own plugin into fylr

Assuming you installed fylr via docker-compose.

1. Connect a new folder via docker-compose.yml
{{{
volumes:
  -"./plugins:/fylr/files/plugins/custom"
}}}

2. Set the fylr UID on the local "plugins" folder:
{{{
chown 1000 plugins
}}}

3. Add a new plugin path to fylr.yml

