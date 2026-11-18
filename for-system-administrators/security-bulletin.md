---
description: Security fixes in fylr and the components it ships, with fylr's severity estimate, the publication date and the release that carries each, and widely reported vulnerabilities that do not affect fylr
---

# Security Bulletin

This page lists the security fixes of recent fylr releases: updates of the components fylr ships, fixes in fylr's own code and hardening. Each fix names the first release that carries it, and every later release carries it too. Widely reported vulnerabilities that do not affect fylr are listed at the end.

Run the newest fylr release. An installation with the docker images gets the fixed packages by updating fylr. An installation without them updates the same packages through its own package sources.

Questions about an advisory go to [support@programmfabrik.de](mailto:support@programmfabrik.de).

## Severity for fylr

The severity is fylr's own estimate of what a vulnerability means for a fylr installation, independent of the advisory's CVSS score or the vendor's rating.

| Severity | Meaning |
| --- | --- |
| High | Anyone who reaches the installation, or any user with normal rights, can use it, uploading a file included, and gains code execution, access to files or to other users' data, or a way past authentication. |
| Medium | It can be used only under conditions, such as an account with special rights, a configuration that is not the default or a plugin that is not installed by default, or its impact is limited, such as a denial of service. |
| Low | fylr ships the vulnerable code, but it cannot be used in fylr's setup, or its impact is negligible. |
| Not affected | fylr does not ship the vulnerable code, or nothing in fylr reaches it. |

"Published" is the day the advisory was published, "Fixed in" the fylr release that carries the fix and its release date.

## Components fylr ships

### Chromium

Chromium 156.0.8078.79 from Debian in the fylr image fixes these advisories. Only the PDF Creator plugin uses Chromium.

<details>

<summary>72 Chromium advisories: 43 medium, 29 low</summary>

| Advisory | Description | Severity for fylr | Published | Fixed in |
| --- | --- | --- | --- | --- |
| CVE-2026-76024 | Use after free in MediaStream in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-76027 | Information loss in CacheStorage in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-76029 | Improper input validation in Network in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-118304 | Use after free in SVG in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118306 | Use after free in FileSystem in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118307 | Use after free in Paint in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118308 | Use after free in SVG in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118311 | Use after free in Media in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118313 | Out of bounds write in Video in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118315 | Type confusion in SVG in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118316 | Use after free in V8 in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118317 | Use after free in HTML in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118318 | Buffer overflow in V8 in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118319 | Integer overflow in Skia in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118320 | Race condition in V8 in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118322 | Uninitialized resource in ANGLE in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118328 | Out of bounds read in WebRTC in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118331 | Use after free in FileAPI in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118333 | Buffer overflow in Video in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118334 | Use after free in ImageCapture in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118336 | Race condition in Headless in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118337 | Use after free in Forms in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118339 | Use after free in Animation in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118341 | Use after free in Modularization in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118342 | Use after free in Editing in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118344 | Use after free in Layout in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118345 | Buffer overflow in PDFium in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118347 | Use after free in FileSystem in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118348 | Integer overflow in Skia in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118351 | Use after free in Skia in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118352 | Use after free in Cache in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118355 | Use after free in Command in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118356 | Use after free in WTF in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118357 | Use after free in FileSystem in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118358 | Use after free in WebAudio in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118359 | Use after free in V8 in Google Chrome prior to 156.0.8078.73 | Medium | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-119260 | Use after free in Frames in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119262 | Out of bounds write in V8 in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119263 | Use after free in GarbageCollection in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119264 | Use after free in Dawn in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119267 | Use after free in DOM in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119268 | Use after free in Editing in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119269 | Incorrect authorization in Blink in Google Chrome prior to 156.0.8078.79 | Medium | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-76025 | Incorrect authorization in FileSystem in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-76026 | Origin validation error in Autofill in Google Chrome prior to 156.0.8078.79 (one-time codes in cross-site frames) | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-76028 | Incorrect authorization in FileSystem in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-76030 | Incorrect authorization in FileSystem in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-76031 | Incorrect authorization in Input in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-111943 | eMudhra CA key compromise: eight emSign intermediates with recoverable private keys, distrusted in trust stores | Low | 2026-10-21 | 6.36.0 (unreleased) |
| CVE-2026-118309 | Incorrect reference resolution in UI in Google Chrome on Android prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118310 | Use after free in Views in Google Chrome on Windows prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118312 | Observable discrepancy in Paint in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118314 | Incorrect reference resolution in UI in Google Chrome on Android prior to 156.0.8078.73 (co-installed app) | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118321 | Use after free in Core in Google Chrome on Android prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118327 | Incorrect authorization in Media in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118329 | Uninitialized resource in ANGLE in Google Chrome on Mac prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118330 | Use after free in Browser in Google Chrome on Windows prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118332 | Use after free in Compositing in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118335 | Out of bounds write in Metrics in Google Chrome on Mac prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118338 | Observable discrepancy in Animation in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118340 | Integer overflow in Skia in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118343 | Use after free in ReadingList in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118346 | Out of bounds read in Compositing in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118349 | Use after free in Payments in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118353 | Missing authorization in Paint in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-118354 | Uninitialized resource in Skia in Google Chrome prior to 156.0.8078.73 | Low | 2026-10-27 | 6.36.0 (unreleased) |
| CVE-2026-119261 | Buffer overflow in Skia in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119265 | Incorrect reference resolution in Quota in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119266 | Incorrect reference resolution in Quota in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119270 | Incorrect reference resolution in CacheStorage in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119271 | Uninitialized resource in Skia in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |
| CVE-2026-119272 | Incorrect authorization in FileSystem in Google Chrome prior to 156.0.8078.79 | Low | 2026-10-30 | 6.36.0 (unreleased) |

</details>

### expat

expat 2.10.0 from Debian in the fylr image.

| Advisory | Description | Severity for fylr | Published | Fixed in |
| --- | --- | --- | --- | --- |
| CVE-2026-113351 | libexpat 2.7.2 through 2.9.0 Denial of Service via XML_ParserReset | Low | 2026-10-20 | 6.36.0 (unreleased) |
| CVE-2026-115506 | libexpat: billion laughs protection detects entity amplification too late | Low | 2026-10-22 | 6.36.0 (unreleased) |
| CVE-2026-117610 | libexpat through 2.9.0 contains a NULL pointer dereference vulnerability in externalEntityInitProcessor2() in lib/xmlparse.c | Low | 2026-10-28 | 6.36.0 (unreleased) |
| CVE-2026-118370 | libexpat through 2.9.0 Integer Overflow in storeAtts via attIndex and nPrefixes | Low | 2026-10-28 | 6.36.0 (unreleased) |

### poppler

poppler 26.07.0-4 from Debian in the fylr image.

| Advisory | Description | Severity for fylr | Published | Fixed in |
| --- | --- | --- | --- | --- |
| CVE-2026-93311 | Integer overflow in Poppler 26.07.0 SampledFunction::SampledFunction (poppler/Function.cc) through the BitsPerSample argument | Low | 2026-09-18 | 6.36.0 (unreleased) |

### gRPC for Go

The Go module google.golang.org/grpc 1.83.1 in the fylr binary. fylr starts no gRPC server; the module comes with the client library for Azure Blob Storage.

| Advisory | Description | Severity for fylr | Published | Fixed in |
| --- | --- | --- | --- | --- |
| CVE-2026-84304, GHSA-vp52-pcj8-j9qc, GO-2026-6348 | Heap memory exhaustion via fragmented HTTP/2 DATA frames in google.golang.org/grpc | Low | 2026-09-15 | 6.35.0 (2026-10-13) |
| GHSA-hrxh-6v49-42gf, GO-2026-6061 | Vulnerabilities in the xDS RBAC authorization engine and the HTTP/2 transport server of google.golang.org/grpc | Low | 2026-07-27 | 6.35.0 (2026-10-13) |

## fylr's own code

A bug in fylr's own code is published with the release that fixes it, without details, so that installations which have not updated yet are not put at risk. The [release notes](../releases/README.md) of each release list the commits.

| Description | Severity for fylr | Fixed in |
| --- | --- | --- |
| Security bugs in fylr's own code | High | 6.36.0 (unreleased) |
| Security bugs in fylr's own code | High | 6.35.0 (2026-10-13) |
| Security bugs in fylr's own code. 6.35.0 carries these fixes too. | High | 6.34.7 (2026-09-26) |

## Hardening

| Release | Change |
| --- | --- |
| 6.36.0 (unreleased) | With `fylr.services.execserver.sandbox.enabled: true` on Linux, the execserver confines every command it runs with Landlock: a command writes only in its own job directory and cannot read `fylr.yml` or the files of other jobs. The sandbox is off by default, see `sandbox` in [fylr.example.yml](configuration/fylr.example.yml.md). |
| 6.35.1 (2026-10-27) | fylr runs with an OpenSearch user whose rights cover only the instance's own indices, so several instances can share one OpenSearch without reaching each other's indices. |
| 6.35.0 (2026-10-13) | Every response carries security policy headers, `X-Frame-Options: SAMEORIGIN` by default, and tells browsers not to guess its content type. Credentialed CORS answers only configured origins. See [Security headers and CORS](configuration/http-and-https.md#security-headers-and-cors). |
| 6.34.0 (2026-07-15) | An access or refresh token issued to the web app is tied to the browser it was issued in. |

## Not affected

| Advisory | Description | Why fylr is not affected | Published |
| --- | --- | --- | --- |
| CVE-2026-109618, CVE-2026-109619 | "PHP2Shell": remote code execution in PHP core | fylr ships no PHP. Its web server is part of the fylr binary, which is written in Go. | 2026-10-21 |
| CVE-2026-123158 | OpenSSH "sshole": password authentication bypass in sshd on musl Linux without PAM | fylr ships no SSH server, and the fylr images are Debian with glibc. | 2026-11-05 |
| CVE-2026-122006, GHSA-f3w6-w445-fwh9 | Rails Active Storage: file read and write through an upload processed by ImageMagick | fylr ships no Ruby on Rails. | 2026-11-04 |
| CVE-2024-27834 | Apple WebKit: pointer authentication bypass | A flaw in WebKit on the user's own device. fylr ships no WebKit. | 2024-05-14 |
| CVE-2026-111943, CVE-2026-111944, CVE-2026-113812, CVE-2026-115557 | eMudhra CA key compromise: eight intermediates with published private keys | The fylr binary of 6.35.3, built with Go 1.27.3, the trust store of the fylr image, Node.js and Python distrust the eight intermediates. The Chromium of the PDF Creator plugin distrusts them from 6.36.0, see Chromium above. | 2026-10-21 |
| CVE-2026-59162, GHSA-fx5j-qcqg-grpf, GO-2026-6452 | Panic via a negative shared-string index in github.com/xuri/excelize | fylr only writes XLSX files with this module and never reads one. 6.35.0 ships the fixed excelize 2.11.0 all the same. | 2026-09-16 |
| CVE-2026-98432 | Linux kernel: use after free in IPv4 TCP connection setup | A flaw in the Linux kernel of the host. The fylr images contain no kernel; a kernel update of the host fixes it. | 2026-10-15 |
| none | Linux kernel: 948 local privilege escalation flaws reported by OpenAI ("A thousand fewer paths to root") | Flaws in the Linux kernel of the host, which need a local user. The fylr images contain no kernel; a kernel update of the host fixes them. | 2026-11-05 |
