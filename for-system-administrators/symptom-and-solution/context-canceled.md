# context canceled

## Symptoms

* fylr (execserver part of fylr) may output / log something like this message:

```
ERR exec #0: signal: killed [context canceled] Env=execserver
```

* From 6.35 the text before the bracket can also be a line from the command's stderr (its last error line); the bracket at the end is what tells the cases apart.
* Also, the execserver job probably does not achieve what it is supposed to (as it was aborted). May result in missing preview, missing extracted metadata etc..

## Cause

`[context canceled]` means the execserver stopped the command because the job was withdrawn from outside while it ran — not because of a timeout of its own.

**From 6.35** the job travels over the broker connection between the fylr and the execserver, and is withdrawn when

* the fylr cancels it: the request waiting for the job ended (its client, or a proxy in front of fylr with a shorter timeout, closed the connection — custom download versions, plugin callbacks), or the fylr server is stopping. The execserver logs `broker: job canceled by client` right before;
* the broker connection drops: every job running over it is cancelled. The execserver logs `broker: client disconnected`.

A limit of the execserver itself shows a different bracket:

| Bracket | Meaning | Setting |
| --- | --- | --- |
| `[context deadline exceeded]` | the job ran longer than its timeout | the recipe exec's `timeout`; for plugin callbacks `fylr.execserver.pluginJobTimeoutSec` (default 2400) |
| `[stalled: no progress for …]` | the command showed no progress for the stall timeout | `fylr.services.execserver.stallTimeoutSec` (default 600, `0` = off), the recipe exec's `stallTimeout` |
| `[out of memory: …]` | the command exceeded the memory a single job may hold, or all commands together exceeded the machine's budget | derived from the machine's memory |
| `[execserver draining]` | the execserver shut down before the job finished; fylr retries the job, it did not fail | `fylr.services.execserver.drainTimeoutSec` |

See [Execution limits](../../for-developers/execserver.md#execution-limits) for how each limit works.

**Up to 6.34.x** the job was an HTTP request from fylr to the execserver, and `[context canceled]` meant that request was closed while the job ran: by fylr (restart, a client that went away), or by a proxy or load balancer between fylr and the execserver whose timeout was shorter than the job.

## Solutions

* Find out who withdrew the job: look at the execserver log right before the message, and at `/inspect/system/topology/` for the state of the connections between the fylr servers and the execservers.
* If a proxy in front of fylr (or, up to 6.34.x, between fylr and the execserver) closes long requests, raise its timeout.
* If the message says `[context deadline exceeded]` instead, increase the timeout. For plugin callbacks this is `fylr.yml`, default:

```yaml
fylr+:
  execserver+:
    pluginJobTimeoutSec: 2400
```

For a produced version it is the recipe exec's `timeout`. From 6.35 a recipe exec without one has no wall-clock limit — the stall timeout supervises it instead — and metadata extraction is stopped after one hour; up to 6.34.x `pluginJobTimeoutSec` also applied to every recipe exec without a timeout of its own.

* Reduce load on the hardware so that processing per asset is faster. All the reasons for load on your hardware are out of the scope of this fylr documentation, but to e.g. reduce the number of parallel video conversions to 1, cap the `ffmpeg` service (from 6.35; earlier versions used a `waitgroups` block):

```yaml
fylr+:
  services+:
    execserver+:
      services+:
        ffmpeg:
          maxSlots: 1
```

* Change the used "recipe"(=list of steps on how to process certain asset file types). About recipes see e.g. [https://docs.fylr.io/releases/2023/v6.8.0](https://docs.fylr.io/releases/2023/v6.8.0) and search for the word recipe.

