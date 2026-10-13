# Collection Pin Code

* PIN an Collection schuetzt alle Rechte einer ACL ausser BAG\_READ
* PIN wird an Collection - User Beziehung gespeichert User kann seine PINs einsehen
* PIN wird pro Browser gespeichert (Cookie `fylr-browser-id`, Anfragen ohne Cookie teilen sich einen Eintrag) und schaltet die Collection nur für Anfragen aus dem Browser frei, in dem er eingegeben wurde
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

Pro Collection kann ein User einen PIN pro Browser haben; der GET zeigt nur den des anfragenden Browsers. Der POST ändert nur die PINs dieses Users:

* `_collection_pin_codes` weggelassen: nichts ändert sich.
* Collection in der Liste: ihr PIN für den anfragenden Browser wird gesetzt, ihre PINs für andere Browser bleiben erhalten. `pin_code: ""` löscht nur den PIN des anfragenden Browsers.
* Collection nicht in der Liste: ihre PINs für alle Browser werden gelöscht. `[]` löscht also alle PINs des Users.

### Unbekannte Collection ID

Einträge mit einer Collection ID, die es nicht gibt, werden ohne Fehler verworfen.

### Frontend Check:

Nach dem Speichern kann ein GET /api/collection durchgeführt werden und damit geschaut ob die PIN für die Collection OK ist oder nicht.

### GET /api/user

Der GET gibt pro Collection den PIN zurück, der für den anfragenden Browser gespeichert ist; wurde er nur in anderen Browsern eingegeben, kommt `pin_code: ""`. Wenn Collection gelöscht werden, fliegen sie auch aus der Liste hier raus.

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
* Ab 6.35.0: Eigentümer und Nutzer mit BAG\_ACL (direkt oder von der übergeordneten Mappe geerbt) müssen den PIN nicht eingeben (`_pin_ok: true`); der PIN einer Kind-Mappe wird gegen die Kind-Mappe geprüft, auch wenn die Rechte von der Mutter-Mappe kommen.
