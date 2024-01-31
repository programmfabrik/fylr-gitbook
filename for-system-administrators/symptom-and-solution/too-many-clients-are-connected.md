# too many clients are connected



## Symptoms

* Log messages around the central topic of `too many clients are connected`&#x20;
* Even panic and tracebacks may appear in the logs / output of fylr, like: (shortened here)

```
ERR Recover from panic, rolling back error="could not start read transaction: [...]
/usr/local/go/src/runtime/debug/stack.go:24 +0x5e
runtime/debug.PrintStack()
[...]
/usr/local/go/src/net/http/server.go:3086 +0x5cb
```

## Cause

There are already more connections from fylr to the postgreSQL database service than the configured limit in postgreSQL.

## Solutions

### Change limit in fylr

In fylr yaml configuration: fylr.db.maxIdleConns

* if you use this, fylr will try to stay below the new limit and the errors may go away if you match the limit of your postgreSQL Installation.
* We do not recommend this, as it may slow fylr down.

### Change limit in postgreSQL

* if you increase this limit, the error might go away or appear less frequent. But postgreSQL may consume more memory.
* We recommend this method unless your server cannot provide enough memory. Hopefully, the limit is just too low for your server, so just try to increase it and monitor whether problems arrive.
* in [docker-compose.yml](../../\_assets/docker-compose.yml#L35) add a line like `-c max_connections=200`  . 200 is just an example. The line shall be below the [line](../../\_assets/docker-compose.yml#L35) with  `command`  for the postgresql service. The default seems to be 100.
