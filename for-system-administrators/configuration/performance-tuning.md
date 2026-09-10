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
      # Every service shares one pool of slots (since fylr 6.35), and each is
      # classified light or heavy by its measured runtime. Heavy jobs (long
      # conversions) never occupy the last `fastReserve` slots, so short
      # interactive work always finds a slot. These are the shipped defaults:
      slots: 0            # size of the pool, 0 = GOMAXPROCS, the CPUs available to fylr
      fastReserve: -1     # slots kept for light jobs, -1 = max(1, slots / 4), 0 = none
      heavyThreshold: 10s # a service slower than this counts as heavy
      unknownShare: 0.5   # pool share a service may use before it has samples
      drainTimeoutSec: 20 # graceful shutdown: running jobs may finish this long
      services:
        soffice:
          maxSlots: 1      # the most slots this service holds at once, 0 = no cap
```

* `elastic.parallel` — 4 parallel fylr jobs feed the indexer with changed and new data. fylr compiles the documents for the indexer; depending on the data model and data this can be more CPU-consuming than the indexing itself.
* `execserver` concurrency is one pool: you no longer size a pool per service. All services draw from it, and the balancer keeps short interactive jobs (metadata, plugins, IIIF) responsive by reserving `fastReserve` slots that long conversions (ffmpeg, LibreOffice, ImageMagick) cannot take. The balancer learns each service's runtime and persists that profile across restarts, provided a `tempDir` is configured. A slot is a unit of admission, not a core: a job holds one while it runs, a command that leased a temporary CPU allocation holds more, and on a small container `slots` may sit above the CPU limit so short jobs overlap their transfers.
* `maxSlots` on a service caps what it holds of the pool at once, jobs and temporary allocations together. It is the one per-service knob.

{% hint style="info" %}
**Upgrading from before 6.35.** The `execserver.parallel` / `execserver.parallelHigh` keys, the `waitgroups` block and the per-service `waitgroup` keys are gone: they are reported as deprecated at startup and ignored, and there is no manual mode. A service that ran in its own small waitgroup gets `maxSlots` instead. [Updating the execserver to 6.35](../installation/updating-the-execserver-to-6.35.md) walks through the whole change.
{% endhint %}

### Other things you can change:

* Run the execserver jobs (conversion, metadata-readout etc.) on different hardware
* Run the execserver jobs on multiple hardware servers, optionally deciding which hardware does which kind of jobs
* Run the indexer on different / multiple hardware servers

## Under which circumstance would you change what?

### One tool must not run in parallel, or must not take the pool

Give its service a `maxSlots`. It counts jobs and temporary CPU allocations together, so `1` is one job at a time that leases nothing, and `4` is four single-slot encodes or one four-thread encode:

```
fylr+:
  services+:
    execserver+:
      services+:
        soffice+:
          maxSlots: 1
        ffmpeg+:
          maxSlots: 4
```

### User experience in the frontend is slowed down by one type of asset processing

Long conversions already yield the reserved fast slots to interactive work. To cap a specific tool harder, give it a `maxSlots` (as above), or reduce the CPU cores it uses:

```
fylr+:
  services+:
    execserver+:
      env:
        # threads used by ffmpeg for mp4 video format
        - FYLR_CONVERT_VIDEO_MP4_THREADS=1
```

### Asset processing is too slow

Give the execserver more slots or more CPU. On a small container, raise `slots` above the CPU limit first: a slot is a unit of admission, and jobs that wait on their transfers overlap without needing a core each. Then add cores, or run execserver jobs on separate or multiple hardware servers:

* Example: [see execserver on another linux](../installation/linux-docker-compose/execserver-on-another-linux.md) (one, but easily customizable to multiple)
* optionally decide which hardware does which kind of jobs — Example: [outsource only video processing with ffmpeg to another fylr](../installation/linux-docker-compose/ffmpeg-on-a-separate-fylr.md)
