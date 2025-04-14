# Collection Pin Code

* PIN an Collection schuetzt alle Rechte einer ACL ausser BAG\_READ
* PIN wird an Collection - User Beziehung gespeichert User kann seine PINs einsehen
* POST /api/collection wird um "pin\_code" erweitert

```json
{
  _has_pin: true|false,
  _pin_ok: true|false, // key weglassen, wenn _has_pin: false ist!
  collection: {
      _id: 4,
      pin_code: "henk"
  }
}
```

## POST /api/user

```
_collection_pin_codes: [
   {
       collection_id: 1234,
       pin_code: "henk"
   }
]
```

### Fehler beim POST:

Collection ID nicht vorhanden

### Frontend Check:

Nach dem Speichern kann ein GET /api/collection durchgeführt werden und damit geschaut ob die PIN für die Collection OK ist oder nicht.

### GET /api/user

Der GET gibt die aktuellen PIN Code zurück. Wenn Collection gelöscht werden, fliegen sie auch aus der Liste hier raus.

```json
_collection_pin_codes: [
   {
       collection_id: 1234,
       pin_code: "henk"
   },
  {
       collection_id: 124,
       pin_code: "henk2"
   }
]
```

## POST /api/search \[type==collection]

Muss `_has_pin` UND `_pin_ok` anzeigen, auch wenn "generate\_rights:false" ist.

Sonstiges:

* PIN code nicht eingegeben oder nicht korrekt für eine Collection die einen PIN hat erlaubt für den Nutzer erstmal nur BAG\_READ, wenn der Nutzer dieses über eine ACL bekommt. Alle anderen Rechte die über die ACL kommen werden erst dann aktiv wenn der PIN Code korrekt hinterlegt ist.
* \_has\_pin: true, \_pin\_ok: true
* collection.pin\_code is read/writable nur bei BAG\_ACL recht
