# fylr Supervisor

The fylr Supervisor runs and manages a fleet of fylr instances on one machine. It starts each instance as a child process, provisions its PostgreSQL database and OpenSearch indices, and routes public traffic to it by host name through a built-in reverse proxy with on-demand TLS (ACME or manually uploaded certificates).

Beyond running instances, the Supervisor centralizes what would otherwise be configured per instance:

* **Licenses** — stored once, assigned as a fleet default or per instance.
* **Storage backends** — named S3 buckets or shared directories, assigned to instances as storage locations.
* **Managed base config** — selected base-config values pushed into instances and locked in their editors.
* **Rate limits** — per-instance and per-client-IP request limits enforced by the router.
* **Backups & restores** — a central backup store; backups pull a remote fylr in, restores push a stored backup into an existing or new instance.
* **Deployments** — upload a release or branch build and run it as a throwaway instance.

Idle instances hibernate after a configurable period and wake on the next request for their host. A web UI and a JSON management API (see [API documentation](api-documentation.md)) expose all of this; everything the UI does goes through the same API.

{% hint style="info" %}
The Supervisor is under active development; details of the API and behavior described here may still change.
{% endhint %}
