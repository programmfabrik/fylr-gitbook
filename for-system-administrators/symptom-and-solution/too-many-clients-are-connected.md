# too many clients are connected

## Symptoms

* Log messages around the central topic of `too many clients are connected`
* Even panic and tracebacks may appear in the logs / output of fylr, like: (shortened here)

```
ERR Recover from panic, rolling back error="could not start read transaction: [...]
/usr/local/go/src/runtime/debug/stack.go:24 +0x5e
runtime/debug.PrintStack()
[...]
/usr/local/go/src/net/http/server.go:3086 +0x5cb
```

## Cause

There are already more connections from fylr to the PostgreSQL database service than the configured limit in PostgreSQL.

## Solution

We recommend to set the limits in fylr and postgres to the same number.

An example can bee seen here: [https://github.com/programmfabrik/fylr-gitbook/commit/ede6fc41a74e1c6963b376b92c45c626eb1f6126](https://github.com/programmfabrik/fylr-gitbook/commit/ede6fc41a74e1c6963b376b92c45c626eb1f6126)

You may also need to find the correct limit for your situation.

### Change limit in fylr

In fylr yaml configuration: `fylr.db.maxOpenConns`&#x20;

* If you use this, fylr will try to stay below the new limit and the errors may go away.
* If you use a limit far below what your hardware can handle, you may slow fylr down.

### Change limit in PostgreSQL

* If you increase this limit, the error might go away or appear less frequent.&#x20;
* But PostgreSQL may consume more memory.
* In [docker-compose.yml](../../\_assets/docker-compose.yml#L35) add a line like `-c max_connections=200` . 200 is just an example. The line shall be below the [line](../../\_assets/docker-compose.yml#L35) with `command` for the postgresql service. The default seems to be 100.
