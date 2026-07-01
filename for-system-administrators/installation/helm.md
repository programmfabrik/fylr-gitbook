# Kubernetes

How to install fylr in a kubernetes cluster

Instructions: See our [helm chart](https://github.com/programmfabrik/fylr-helm/blob/main/charts/fylr/README.md).

* Uses helm charts and Linux containers.
* Needs helm and a kubernetes cluster.
* 3rd party tools for preview thumbnails are pre-packaged.

Through your firewalls you probably sooner or later need access to:

* https://docker.fylr.io (fylr core)
* https://artifacts.opensearch.org (indexer plugin)
* https://github.io and https://github.com (fylr plugins)
* https://auth.docker.io (indexer and PostgreSQL)
* https://registry-1.docker.io (indexer and PostgreSQL)
* https://index.docker.io (indexer and PostgreSQL)
* https://cloudfront.net (indexer and PostgreSQL)
* https://production.cloudflare.docker.com (indexer and PostgreSQL)

\
... and of course the **package sources** of the Linux distribution used on your server; for security updates, tools and operating system upgrades.
