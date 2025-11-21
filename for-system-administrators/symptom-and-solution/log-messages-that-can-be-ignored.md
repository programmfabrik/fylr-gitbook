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

... are probably just old browser sessions with a now invalid authentication.

<br>

### During migration

```
level=warning msg="Request failed after 29ms: Status not OK but \"400 Bad Request\" [400] fylr error: \"Duplicate file reference provided: www.easydb.example.com:eas:12345:original with file id 67890\" [EasDuplicateReference]"
```

... This happens if the same asset is linked in several versions in one object. In this case, the asset should not be uploaded multiple times. Instead, the same asset ID is used again in all versions. This is only logged because it is recognized as an error in a central location (API error with status code 400), but it is then evaluated by fylr restore and not treated as an actual error.



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
