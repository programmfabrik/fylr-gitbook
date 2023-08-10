---
description: fylr messages, fylr output, docker logs
---

# Log messages that can be ignored

```
WRN Invalid token: "" BackendID=SyzRaj Env=api RunID=ANibqg path=/api/v1/user/session query=access_token=ory_at_CCS... status=400
```

... and ...

```
WRN Accepting token failed error
```

... are probably just old browser sessions with a now invalid authentication.\


### More ignorable messages without explanation:

```
could not obtain lock on row in relation
```

```
WRN Unknown endpoint method GET /api/v1/plugin/mapbox-gl.js.map BackendID=SyzRaj Env=api RunID=YOYZCz path=/api/v1/plugin/mapbox-gl.js.map query= status=400
```

```
WRN Error occurred in NewIntrospectionRequest error=request_unauthorized Env=api
```

```
WRN Copying html for plugin error=": unable to load: 404 Not Found" BackendID=SyzRaj Env=api RunID=kYTPGF
```

```
WRN Copying html for plugin error=": unable to load: 404 Not Found" BackendID=SyzRaj Env=api RunID=kYTPGF
```

```
DBG Console stream socket message error="websocket: close 1006 (abnormal closure): unexpected EOF" BackendID=SyzRaj Env=api RunID=aZRkCt
```
