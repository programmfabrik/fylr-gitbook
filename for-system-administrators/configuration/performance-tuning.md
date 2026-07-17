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
      # Concurrency is auto-balanced (since fylr 6.35): every service shares one
      # CPU pool sized to the host, and each is classified light or heavy by its
      # measured runtime. Heavy jobs (long conversions) never occupy the last
      # `fastReserve` slots, so short interactive work always finds a slot.
      # All keys are optional — the defaults below apply when unset:
      #   cpus: 0             # pool size, 0 = number of CPUs
      #   fastReserve: 0      # slots kept for light jobs, 0 = max(1, cpus / 4)
      #   heavyThreshold: 10s # a service slower than this counts as heavy
      #   unknownShare: 0.5   # pool share a service may use before it has samples
      #   drainTimeoutSec: 20 # graceful shutdown: running jobs may finish this long
```

* `elastic.parallel` — 4 parallel fylr jobs feed the indexer with changed and new data. fylr compiles the documents for the indexer; depending on the data model and data this can be more CPU-consuming than the indexing itself.
* `execserver` concurrency is **auto-balanced**: you no longer size a pool per service. All services draw from one CPU pool, and the balancer keeps short interactive jobs (metadata, plugins, IIIF) responsive by reserving `fastReserve` slots that long conversions (ffmpeg, LibreOffice, ImageMagick) cannot take. The balancer learns each service's runtime and persists that profile across restarts.

{% hint style="info" %}
**Upgrading from before 6.35.** The `execserver.parallel` / `execserver.parallelHigh` keys and the default per-service `waitgroup` assignments are gone. An existing explicit `waitgroups` block still works and turns auto-balancing off (see below); a config that keeps it now needs a `waitgroup:` on every service, because the default mapping no longer exists.
{% endhint %}

### Other things you can change:

* Run the execserver jobs (conversion, metadata-readout etc.) on different hardware
* Run the execserver jobs on multiple hardware servers, optionally deciding which hardware does which kind of jobs
* Run the indexer on different / multiple hardware servers

## Under which circumstance would you change what?

### I want manual control over concurrency (opt out of auto-balancing)

Configure an explicit `waitgroups` block with a `waitgroup:` on every service. This restores manually sized pools exactly as before 6.35:

```
fylr+:
  services+:
    execserver+:
      waitgroups:
        slow:                 # video / office conversion
          processes: 2
        medium:               # convert / image
          processes: 6
        fast:                 # plugins / metadata etc.
          processes: 10
      services+:
        ffmpeg:    { waitgroup: slow }
        soffice:   { waitgroup: slow }
        inkscape:  { waitgroup: slow }
        pdf2pages: { waitgroup: slow }
        convert:   { waitgroup: medium }
        exec:      { waitgroup: fast }
        node:      { waitgroup: fast }
        python3:   { waitgroup: fast }
        xslt:      { waitgroup: fast }
        iiif:      { waitgroup: fast }
        metadata:  { waitgroup: fast }
```

### User experience in the frontend is slowed down by one type of asset processing

With auto-balancing, long conversions already yield the reserved fast slots to interactive work. To cap a specific tool harder, opt it into an explicit waitgroup (as above), or reduce the CPU cores it uses:

```
fylr+:
  services+:
    execserver+:
      env:
        # threads used by ffmpeg for mp4 video format
        - FYLR_CONVERT_VIDEO_MP4_THREADS=1
```

### Asset processing is too slow

Give the execserver more CPU — raise `cpus`, add cores, or run execserver jobs on separate or multiple hardware servers:

* Example: [see execserver on another linux](../installation/linux-docker-compose/execserver-on-another-linux.md) (one, but easily customizable to multiple)
* optionally decide which hardware does which kind of jobs — Example: [outsource only video processing with ffmpeg to another fylr](../installation/linux-docker-compose/ffmpeg-on-a-separate-fylr.md)
