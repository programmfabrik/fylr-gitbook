---
description: >-
  Where fylr's connections to an S3 storage location come from, what limits
  apply, and how to count them
---

# too many S3 connections

## Symptoms

* The S3 provider reports that a connection limit for your account or source IP is being reached.
* Under load — bulk imports, mass rendition production, large exports — uploads, renditions or downloads fail sporadically.
* Log messages about connection resets, timeouts or `context canceled` against the S3 endpoint.

## Where the connections come from

Connections to an S3 storage location are **not** all opened by the fylr process. Depending on your setup up to three different hosts talk to the S3 endpoint:

| Traffic                                                                          | Opened by                            | Goes to                       |
| -------------------------------------------------------------------------------- | ------------------------------------ | ----------------------------- |
| fylr's own reads and writes: file janitor, copies between locations, exports, and every upload arriving at fylr | the **fylr** process                 | S3 endpoint                   |
| Fetching the source file of a rendition job (`%_source.url%`)                      | the **execserver** host              | S3 endpoint (presigned GET)   |
| Storing a produced rendition (`%_target.url%`)                                     | the **execserver**                   | fylr's backend — **not** S3; fylr writes it to S3 |
| Downloads, if the location has `allow_redirect: true`                              | the **end user's browser**           | S3 endpoint (presigned GET)   |

Two consequences:

* If the execserver runs on a separate machine, counting on the fylr host alone under-reports. Count on both.
* With `allow_redirect: true`, download traffic reaches S3 from many client IPs and never touches fylr's own connection budget at all. It still counts towards a limit that applies to the whole account.

## Which limits apply

fylr uses the AWS SDK for Go v2 with its default HTTP transport for every S3 storage location. Per fylr process and per storage location:

| Setting                              | Value  |
| ------------------------------------ | ------ |
| Maximum connections per host         | 2048   |
| Idle connections kept in the pool    | 10     |
| Idle connection timeout              | 90 s   |

The important one is the second: **only about ten connections are pooled.** Above roughly ten concurrent S3 requests, every further request opens a fresh connection and closes it once the request is done. Under sustained load this produces a lot of connection churn, and each closed connection then sits in `TIME_WAIT` for 60 seconds on Linux.

{% hint style="info" %}
If your provider's limit counts **sockets** rather than **established connections**, the number they see can be several times the actual concurrency, because most of those sockets are in `TIME_WAIT` and no longer carrying data. Clarify which one is counted before you ask for a higher limit — see the state breakdown below.
{% endhint %}

There is no fylr configuration option to cap or widen the S3 connection pool. `fylr.debug.http` tunes fylr's general purpose outbound HTTP client, not the S3 client of a storage location. The `fylr.execserver.parallel` worker count is deprecated and no longer limits file work; the file dispatcher derives its admission from the capacity of the connected execservers and the CPU count.

## Counting the connections

Run these on the fylr host, and on the execserver host if it is a separate machine. All of them resolve the endpoint name to its current IP addresses and match the peer address against them, so they stay correct when the endpoint is DNS round-robin.

A point in time count of established connections:

```bash
S3HOST=s3.example.com; ss -Htn state established | grep -cE "$(getent ahostsv4 $S3HOST | awk '{print $1}' | sort -u | paste -sd'|' -)"
```

A live sampler that also tracks the peak — run this during a bulk import to find out what your instance actually needs:

```bash
S3HOST=s3.example.com; peak=0; while :; do RE=$(getent ahostsv4 "$S3HOST" | awk '{print $1}' | sort -u | paste -sd'|' -); est=$(ss -Htn state established | grep -cE "$RE"); all=$(ss -Htan | grep -cE "$RE"); (( est > peak )) && peak=$est; printf '%s established=%-5s all_sockets=%-5s peak=%s\n' "$(date +%T)" "$est" "$all" "$peak"; sleep 1; done
```

A breakdown by TCP state. This is the one that shows whether a reported number is real concurrency or mostly `TIME_WAIT`:

```bash
S3HOST=s3.example.com; ss -Htan | grep -E "$(getent ahostsv4 $S3HOST | awk '{print $1}' | sort -u | paste -sd'|' -)" | awk '{print $1}' | sort | uniq -c | sort -rn
```

### If fylr runs in Docker

With the default bridge networking the connections live in the container's network namespace, so `ss` on the host does not see them. Enter the namespace instead of using `docker exec` — the fylr image does not ship `ss`:

```bash
nsenter -t "$(docker inspect -f '{{.State.Pid}}' fylr)" -n ss -Htan state established
```

On Kubernetes the same works from the node, using the PID of the container process.

## Reducing the number

* **Run fewer file workers.** Set `fylr.execserver.parallel: 0` on nodes that should not do file work, and reduce the number of entries in `fylr.execserver.addresses`. Fewer concurrent rendition jobs means fewer simultaneous fetches from S3.
* **Check `allow_redirect`.** With `allow_redirect: true` downloads go from the browser straight to S3. That takes them off fylr's connection budget, which helps against a per source IP limit but not against an account wide one. With `false`, all download traffic is served by fylr and counts against fylr's own connections to S3.
* **Ask what is being counted.** A limit expressed in sockets and a limit expressed in established connections are very different numbers for the same workload.
