# performance tuning

## Understanding the knobs

These are the configurable parameters in `fylr.yml` that affect performance:

```
fylr+:

  elastic+:
    parallel: 4
    objectsPerJob: 100
    maxMem: 25mb

  services+:
    execserver+:
      # One pool of slots for every service (since fylr 6.35). A slot is a
      # unit of admission, not a core: a job holds one while it runs, however
      # many threads its program uses. Each service is classified light or
      # heavy by its measured runtime, and heavy jobs never take the last
      # fastReserve slots, so short interactive work always finds one.
      # These are the shipped defaults (fylr.default.yml):
      slots: 0             # pool size, 0 = GOMAXPROCS (cores, or the container's CPU limit)
      fastReserve: -1      # slots only light jobs may take, -1 = a quarter of the pool, 0 = none
      heavyThreshold: 10s  # a service slower than this counts as heavy
      unknownShare: 0.5    # pool share the services without samples yet may use together
      drainTimeoutSec: 20  # graceful shutdown: running jobs may finish this long
      stallTimeoutSec: 600 # a command without progress for this long is aborted, 0 = off
      services+:
        ffmpeg:
          maxSlots: 2      # the most jobs of the service that run at once
          threads: 0       # the thread count of each of its jobs, 0 = every CPU
```

* `elastic.parallel` — 4 parallel fylr jobs feed the indexer with changed and new data. fylr compiles the documents for the indexer; depending on the data model and data this can be more CPU-consuming than the indexing itself.
* `execserver` concurrency is **auto-balanced**: you no longer size a pool per service. All services draw from one pool of `slots`, and the balancer keeps short interactive jobs (metadata, plugins, IIIF) responsive by reserving `fastReserve` slots that long conversions (ffmpeg, LibreOffice, ImageMagick) cannot take. The balancer learns each service's runtime and persists that profile across restarts, provided a `tempDir` is configured. To hold one service back, give it a `maxSlots`.

### Slots and threads

A **slot** decides whether a job may start, not how many CPUs it uses. The execserver starts a job when it has a free slot for it, and the job holds that one slot until it ends. `slots: 0` makes as many slots as the machine has CPUs, so by default as many jobs run at once as there are CPUs.

How many CPUs a running job uses is up to its program. ImageMagick, LibreOffice and the other tools use what they use; a video encode runs FFmpeg with the **`threads`** of its service. The operating system shares the CPUs between all programs that run.

So the keys answer different questions:

| Key | Question |
| --- | --- |
| `slots` | How many jobs run at once, all services together? |
| `fastReserve` | How many of them are kept for short jobs? |
| `maxSlots` (per service) | How many jobs of this service run at once? |
| `threads` (per service) | How many threads does each of its jobs run? |

{% hint style="info" %}
**Upgrading from before 6.35.** The `fylr.execserver.parallel` / `fylr.execserver.parallelHigh` worker counts no longer size anything (only `parallel: 0`, which switches file processing off on a node, keeps its meaning), and neither do the `waitgroups` block and the per-service `waitgroup` keys. Otherwise they are ignored: `fylr config check` reports `parallelHigh`, `waitgroups` and `waitgroup` as deprecated, and a `parallel` other than `0` gets a warning in the server log at startup. What used to be a dedicated waitgroup is a `maxSlots` on the service. [Updating the execserver to 6.35](../installation/updating-the-execserver-to-6.35.md) walks through the whole change.
{% endhint %}

### Other things you can change:

* Run the execserver jobs (conversion, metadata-readout etc.) on different hardware
* Run the execserver jobs on multiple hardware servers, optionally deciding which hardware does which kind of jobs
* Run the indexer on different / multiple hardware servers

## Under which circumstance would you change what?

### I want to hold one service back

Give the service a `maxSlots`: the most of its jobs that run at once. Its other jobs wait, and everything else keeps the rest of the pool:

```
fylr+:
  services+:
    execserver+:
      services+:
        ffmpeg:  { maxSlots: 1 }
        soffice: { maxSlots: 2 }
```

There is no way to size a pool per service any more; the `waitgroups` block of earlier versions is reported as deprecated and ignored.

### User experience in the frontend is slowed down by one type of asset processing

Long conversions already yield the reserved fast slots to interactive work. They still compete with it for CPU time: a video encode runs on every CPU as shipped. To cap a specific tool harder, give its service a `maxSlots` (as above), or give video encodes fewer threads:

```
fylr+:
  services+:
    execserver+:
      services+:
        # each encode on every CPU but two
        ffmpeg: { threads: -2 }
```

### Videos take long to encode

Video encodes run on the `ffmpeg` service. As shipped, two run at a time, each with one FFmpeg thread per CPU:

```
fylr+:
  services+:
    execserver+:
      services+:
        ffmpeg: { maxSlots: 2, threads: 0 }
```

The thread count is fixed: it does not depend on what else runs. Two encodes together ask for twice the CPUs, and the operating system shares them. While both run, each gets about half; when one ends, the other gets all of them. One upload produces its 360p, 720p and 1080p versions as separate encodes, so they run two at a time.

* **One encode at a time, on every CPU.** Each video is done as fast as the machine allows, and the next one waits. This suits many long videos, for example hours of 4K:

  ```
  ffmpeg: { maxSlots: 1, threads: 0 }
  ```
* **Two at a time, half the CPUs each:**

  ```
  ffmpeg: { maxSlots: 2, threads: 50% }
  ```

`threads` takes `0` (every CPU: `GOMAXPROCS`, that is the cores, the container's CPU limit, or the `GOMAXPROCS` environment variable when it is set), `N`, `-N` (every CPU but N), `N%` (that share of the CPUs) and `-N%` (every CPU but that share). The result is at least one.

An encode holds one slot like any other job, so `slots` and `fastReserve` do not change its thread count, and other jobs keep running next to it. `maxSlots` counts every job of the `ffmpeg` service: audio conversions, the frames of a video pages.zip and trims run there too, and with `maxSlots: 1` they wait for a running encode. Video thumbnails run on the `convert` service and do not wait.

The thread count of an encode is in the receipt of the version's `FILE_PRODUCE` event: the shipped video recipes run `fylr convert -v`, which writes `FFmpeg threads: N` to stderr. Run by hand, `fylr convert --threads=N` takes the same values; the execserver passes `threads` to it as `FYLR_CONVERT_THREADS`. Without either, the encode runs on every CPU.

{% hint style="info" %}
**`FYLR_CONVERT_VIDEO_MP4_THREADS` is no longer read, and `fylr convert --video-mp4-threads` is gone.** fylr warns at startup and in `fylr config check` where the variable is still set. Remove it and set `threads` on the `ffmpeg` service instead; on the command line, use `--threads`.
{% endhint %}

### Asset processing is too slow

Give the execserver more room — raise `slots` (on a small container, above its CPU limit, so short jobs overlap their transfers), add cores, or run execserver jobs on separate or multiple hardware servers:

* Example: [see execserver on another linux](../installation/linux-docker-compose/execserver-on-another-linux.md) (one, but easily customizable to multiple)
* optionally decide which hardware does which kind of jobs — Example: [outsource only video processing with ffmpeg to another fylr](../installation/linux-docker-compose/ffmpeg-on-a-separate-fylr.md)

## Reading the timing headers

Every API response carries `X-Fylr-Timer-…` headers with the time each section of the request took — preparation, the database, the search cluster, rendering. From **6.35.0** each section is measured on its own (before, every nested section reported the whole response time), and `X-Fylr-Timer-Elastic-Took` carries the time the search cluster itself reports for a query. Next to the wall time of the call it tells an expensive query apart from time lost on the connection or in a queue: a large `Elastic-Took` is the query, a large elastic wall time with a small `Elastic-Took` is the path to the cluster.
