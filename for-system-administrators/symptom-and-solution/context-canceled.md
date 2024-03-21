# context canceled

## Symptoms

* fylr (execserver part of fylr) may output / log something like this message:

```
ERR exec #0: signal: killed [context canceled] Env=execserver
```

* Also, the execserver job probably does not achieve what it is supposed to (as it was aborted). May result in missing preview, missing extracted metadata etc..

## Cause

Processing of an asset file used more time than the configured timeout (or, less likely, tried to use more memory than the configured limit).

## Solutions

* Increase the timeout in `fylr.yml`. Default:

```yaml
fylr+:
  execserver+:
    pluginJobTimeoutSec: 2400
```

* Reduce load on the hardware so that processing per asset is faster. All the reasons for load on your hardware are out of the scope of this fylr documentation, but to e.g. reduce the number of parallel video processing to 1 see the code block below.
  * Default is waitgroup `slow` instead of waitgroup `video`. Waitgroup `slow` defaults to `2` processes.

```yaml
fylr+:
  services+:
    execserver+:
      waitgroups+:
        video:
          processes: 1
      services+:
        ffmpeg:
          waitgroup: video
```

* Change the used "recipe"(=list of steps on how to process certain asset file types). About recipes see e.g. [https://docs.fylr.io/releases/2023/v6.8.0](https://docs.fylr.io/releases/2023/v6.8.0) and search for the word recipe.

