# manipulating attributes

## Replacing strings in attributes

Our attribute syntax can replace strings. This syntax is part of our attribute matching (fylr 6.20 and newer):

```
%(key||search||replacement)s
```

Where `search` is the regexp matching what is then replaced with `replacement`.

The regular expressions syntax rules: [https://pkg.go.dev/regexp#Regexp.ReplaceAllString](https://pkg.go.dev/regexp#Regexp.ReplaceAllString).

Example: `%(email||^.*=||)s`, in context:

When a user logs in with attribute email equal to `urn:campus:1:mail=ben@example.com` and attribute mapping Target:Email `%(email||^.*=||)s` then his email address in fylr will be just `ben@example.com`, because the search part matches all up to the equal sign and the replacement is empty.

<figure><img src="../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

## Multi-Value-Attributes

If there are multiple values for e.g. department, a 4th parameter can now be used to concatenate multiple values into one.

```
%(key||search||replacement||;)s
```

Example: `%(dpmt||^.*=||||;)s`, in context:

When a user logs in with these two attributes `urn:campus:1:dpmt=marketing` and `urn:campus:2:dpmt=sales` , the attribute mapping is done like above and in fylr the department will be

`marketing;sales`

## pick first attribute

If an attribute is replaced like this `%(mail|email)s`, fylr now uses the first entry which is not empty as replacement.

## Using JavaScript

You can edit incoming data from SAML via JavaScript in the following field:<br>

<figure><img src="../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

Each user is processed separately and is stored in the JavaScript object `entry` with string arrays as values. Changes configured in this field are done before the IDP data is mapped to the fylr user.

### Complex example

Requirements for the JavaScript in this example scenario:

* If the user has an attribute `officialEmail`, use that as the user's email address in fylr.
* Otherwise use the attribute `email` (private email address) in fylr, but only if the user is an employee, never if it is a student.
* Employees but not students have `urn:employee` somewhere in their `entitlement` attribute.

JavaScript that solves these requirements:

```
// check entitlement attribute: does it contain the string that shows that this is an employee?
entry.isEmployee=["false"]
if ('entitlement' in entry) {
  for (const item of entry.entitlement) {
    if (item.includes('urn:employee')) {
      entry.isEmployee=["true"]
    }
  }
}

// use officialEmail if present, use other email only if employee
if ('officialEmail' in entry) {
  entry.validMail=entry.officialEmail
} else if (entry.isEmployee[0].includes("true")) {
  // for employees: other mail address may be used
  entry.validMail=entry.mail
} else {
  // for others (students): by law, other mail address MUST NOT be used
  entry.validMail=[]
}
```

* tested in fylr
*   requires the following User Mapping in fylr:&#x20;

    <figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

### Debugging JavaScript

* JavaScript is runin "Strict Mode".
* Thus attributes cannot be overwritten.
* After a SAML account tried to login, look into https://yourfylr.example.co&#x6D;**/inspect/system/console/** (login as fylr account "root"). Example output there after successful first login:

```log
2026-06-23 16:37:09 +00:00 DBG starting log for "saml". Debug: true [...]
2026-06-23 16:37:09 +00:00 DBG DN:
  id: [1dda9fb491dc01bd24d2423ba2f2bae561f56ddf2376b29a11c80281d21201f9]
  entitlement: [urn:foo urn:bar urn:bas urn:employee]
  lastName: [jackson]
  SessionIndex: [id-8aaa346bd3ea6283933d11eee9780cfc7bd7c5db]
  login: [jackson]
  mail: [jackson@example.com]
  officialEmail: [office234@example.com]
  firstName: [jady]
2026-06-23 16:37:09 +00:00 DBG using session info (after JS): [...]
2026-06-23 16:37:09 +00:00 DBG DN:
  SessionIndex: [id-8aaa346bd3ea6283933d11eee9780cfc7bd7c5db]
  mail: [jackson@example.com]
  entitlement: [urn:foo urn:bar urn:bas urn:employee]
  firstName: [jady]
  id: [1dda9fb491dc01bd24d2423ba2f2bae561f56ddf2376b29a11c80281d21201f9]
  isEmployee: [true]
  lastName: [jackson]
  login: [jackson]
  myref: [case3]
  officialEmail: [office234@example.com]
  validMail: [office234@example.com]
[...]
2026-06-23 16:37:09 +00:00 DBG user mapping map[string]string{"email":"%(validMail)s", "login":"%(login)s", "reference":"%(myref)s"} BackendID=xAcRTO Env=webapi Hostname=test-saml-fylr-5b4489dcc4-thrrs RunID=LnLzcf login=saml server=0
2026-06-23 16:37:09 +00:00 DBG user reference "case3" [....]
2026-06-23 16:37:09 +00:00 DBG user email "office234@example.com" [...]
2026-06-23 16:37:09 +00:00 DBG user login "jackson" [...]
2026-06-23 16:37:09 +00:00 DBG search user in database by reference "case3" [...]
2026-06-23 16:37:09 +00:00 DBG mapped user
{"_basetype":"user","user":{"_version":0,"login":"jackson","reference":"case3","type":"sso",[...]
2026-06-23 16:37:09 +00:00 DBG user new in fylr [...]
2026-06-23 16:37:09 +00:00 DBG User logged in "jackson", updating record in database [...]
```

* The first indented block is before JavaScript.
* The first indented block is after JavaScript.
* The rest of the lines is the result of the login and mapping process. This was the first time a user with `myref`=`case3` has logged in. `myref` is mapped to `Reference` and Referenz (same a s Reference) is used for `User Update` .
* The value of the attribute `officialEmail` was used in fylr.
