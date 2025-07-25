# manipulating attributes

## Replacing strings in attributes

Our attribute syntax can replace strings. This syntax is part of our attribute matching (fylr 6.20 and newer):

```
%(key||search||replacement)s
```

Where `search` is the regexp matching what is then replaced with `replacement`.

The regular expressions syntax rules: https://pkg.go.dev/regexp#Regexp.ReplaceAllString.

Example: `%(email||^.*=||)s`, in context:

When a user logs in with attribute email equal to `urn:campus:1:mail=ben@example.com` and attribute mapping Target:Email `%(email||^.*=||)s` then his email address in fylr will be just `ben@example.com`, because the search part matches all up to the equal sign and the replacement is empty.

## Multi-Value-Attributes

If there are multiple values for e.g. department, a 4th parameter can now be used to concatenate multiple values into one.

```
%(key||search||replacement||;)s
```

Example: `%(dpmt||^.*=||||;)s`, in context:

When a user logs in with these two attributes  `urn:campus:1:dpmt=marketing` and `urn:campus:2:dpmt=sales` , the attribute mapping is done like above and in fylr the department will be

`marketing;sales`
