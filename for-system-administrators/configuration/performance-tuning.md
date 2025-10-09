# performance tuning

## Understanding the knobs

These are the configurable parameters, which affect performance in `fylr.yml`:

```
fylr+:

  elastic:
    parallel: 4
    objectsPerJob: 100
    maxMem: 100mb

  execserver:
    parallel: 18
    parallelHigh: 10

  services:
    execserver:
      waitgroups:
        # video / office conversion
        slow:
          processes: 2
        # convert / image
        medium:
          processes: 6
        # plugins / metadata etc.
        fast:
          processes: 10

      services:
        # this service allows to execute arbitrary binaries
        exec:
          waitgroup: fast
        # plugin support
        node:
          waitgroup: fast
        python3:
          waitgroup: fast
        xslt:
          waitgroup: fast
        # file conversion support
        convert:
          waitgroup: medium
        ffmpeg:
          waitgroup: slow
        inkscape:
          waitgroup: slow
        soffice:
          waitgroup: slow
        pdf2pages:
          waitgroup: slow
        iiif:
          waitgroup: fast
        dot:
          waitgroup: fast
        metadata:
          waitgroup: fast
```

* 4 parallel fylr jobs instruct the indexer to add changed and new data to the index. fylr has to compile the documents for the indexer. This is a complex task and depending on the data model and data, this can be more CPU-consuming than what the indexer is doing.
* 10 workers check whether further conversions can be started, for standard preview versions&#x20;
* 18 workers check whether further processing can be started: Like reading metadata from new assets and everything else&#x20;
* 2 simultaneous processing of video/office preview images are allowed. \
  These are jobs done with ffmpeg, inkscape, soffice(LibreOffice) and pdf2pages. \
  (Waitgroup "slow")
* 6 simultaneous processing of image previews are allowed \
  These are jobs done with ImageMagick convert. \
  (Waitgroup "medium")
* 10 simultaneous metadata readouts are allowed. (Processing of plugins is in this category, too).\
  These are jobs done with e.g. iiif, dot, node, python3, xsltmetadata.&#x20;

These example values are the defaults in fylr v6.12.



### Other things you can change:

* Run the execserver jobs (conversion, metadata-readout etc.) on a different hardware
* Run the execserver jobs (conversion, metadata-readout etc.) on multiple hardware servers
  * optionally: decide which hardware does which kind of jobs
* Run the indexer on a different hardware
* Run the indexer on multiple hardware servers



## Under which circumstance would you change what?



### User experience in Frontend is slowed down by one type of asset processing

*   Reduce the number allowed jobs of that type. E. g. only allow one video conversion at a time:

    ```
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

### User experience in Frontend is slowed down by asset processing in general

* Reduce the number of allowed concurrent jobs
* Run the execserver jobs (conversion, metadata-readout etc.) on a different hardware than the rest of fylr

### Asset processing is too slow

* Increase the number of allowed concurrent jobs.

Maybe you then have to increase the hardware resources, too:

* Mor CPU cores
* Run the execserver jobs (conversion, metadata-readout etc.) on multiple hardware servers\
  Example: [see execserver on another linux](../installation/linux-docker-compose/execserver-on-another-linux.md) (only one, but easily customizable to multiple)
  * optionally: decide which hardware does which kind of jobs\
    Example: see [outsource only video processing with ffmpeg to another fylr](../installation/linux-docker-compose/ffmpeg-on-a-separate-fylr.md)

