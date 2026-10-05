# performance tuning

## Understanding the knobs

These are the configurable parameters in `fylr.yml` that affect performance:

```
fylr+:

  elastic:
    parallel: 4
    objectsPerJob: 100
    maxMem: 100mb

  services:
    execserver:
      # One pool of slots for every service (since fylr 6.35). A slot is a
      # unit of admission, not a core: a job holds one, a command that leased
      # a temporary CPU allocation holds more. Each service is classified light
      # or heavy by its measured runtime, and heavy jobs never take the last
      # fastReserve slots, so short interactive work always finds one.
      # These are the shipped defaults (fylr.default.yml):
      slots: 0             # pool size, 0 = GOMAXPROCS (cores, or the container's CPU limit)
      fastReserve: -1      # slots only light jobs may take, -1 = a quarter of the pool, 0 = none
      heavyThreshold: 10s  # a service slower than this counts as heavy
      unknownShare: 0.5    # pool share a service may use before it has samples
      drainTimeoutSec: 20  # graceful shutdown: running jobs may finish this long
      stallTimeoutSec: 600 # a command without progress for this long is aborted, 0 = off
      services+:
        ffmpeg:
          maxSlots: 2      # the most slots one service holds at once
```

* `elastic.parallel` — 4 parallel fylr jobs feed the indexer with changed and new data. fylr compiles the documents for the indexer; depending on the data model and data this can be more CPU-consuming than the indexing itself.
* `execserver` concurrency is **auto-balanced**: you no longer size a pool per service. All services draw from one pool of `slots`, and the balancer keeps short interactive jobs (metadata, plugins, IIIF) responsive by reserving `fastReserve` slots that long conversions (ffmpeg, LibreOffice, ImageMagick) cannot take. The balancer learns each service's runtime and persists that profile across restarts, provided a `tempDir` is configured. To hold one service back, give it a `maxSlots`.

{% hint style="info" %}
**Upgrading from before 6.35.** The `execserver.parallel` / `execserver.parallelHigh` keys are gone (only `parallel: 0`, which switches file processing off on a node, keeps its meaning), and so are the `waitgroups` block and the per-service `waitgroup` keys: `fylr config check` reports them as deprecated, and they are ignored. What used to be a dedicated waitgroup is a `maxSlots` on the service. [Updating the execserver to 6.35](../installation/updating-the-execserver-to-6.35.md) walks through the whole change.
{% endhint %}

### Other things you can change:

* Run the execserver jobs (conversion, metadata-readout etc.) on different hardware
* Run the execserver jobs on multiple hardware servers, optionally deciding which hardware does which kind of jobs
* Run the indexer on different / multiple hardware servers

## Under which circumstance would you change what?

### I want to hold one service back

Give the service a `maxSlots`: the most slots it holds at once, jobs and temporary CPU allocations together. A video encode that would otherwise borrow every spare CPU stays within its budget, and everything else keeps the rest of the pool:

```
fylr+:
  services+:
    execserver+:
      services+:
        ffmpeg:  { maxSlots: 2 }
        soffice: { maxSlots: 2 }
```

There is no way to size a pool per service any more; the `waitgroups` block of earlier versions is reported as deprecated and ignored.

### User experience in the frontend is slowed down by one type of asset processing

Long conversions already yield the reserved fast slots to interactive work. To cap a specific tool harder, give its service a `maxSlots` (as above), or reduce the CPU cores it uses:

```
fylr+:
  services+:
    execserver+:
      env:
        # threads used by ffmpeg for mp4 video format
        - FYLR_CONVERT_VIDEO_MP4_THREADS=1
```

### Asset processing is too slow

Give the execserver more room — raise `slots` (on a small container, above its CPU limit, so short jobs overlap their transfers), add cores, or run execserver jobs on separate or multiple hardware servers:

* Example: [see execserver on another linux](../installation/linux-docker-compose/execserver-on-another-linux.md) (one, but easily customizable to multiple)
* optionally decide which hardware does which kind of jobs — Example: [outsource only video processing with ffmpeg to another fylr](../installation/linux-docker-compose/ffmpeg-on-a-separate-fylr.md)

## Reading the timing headers

Every API response carries `X-Fylr-Timer-…` headers with the time each section of the request took — preparation, the database, the search cluster, rendering. From **6.35.0** each section is measured on its own (before, every nested section reported the whole response time), and `X-Fylr-Timer-Elastic-Took` carries the time the search cluster itself reports for a query. Next to the wall time of the call it tells an expensive query apart from time lost on the connection or in a queue: a large `Elastic-Took` is the query, a large elastic wall time with a small `Elastic-Took` is the path to the cluster.
