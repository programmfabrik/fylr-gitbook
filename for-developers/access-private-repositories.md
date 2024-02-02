---
description: >-
  Partners and customers may gain this access for their plugin development and
  security review. This page shows how to then actually access the repositories.
---

# Access private Repositories

## 1. Give us a key of yours

We need a public SSH key that is not already used with github.\
\
Github does not accept keys that are already used with github. So you may have to create an additional key. Here an example on how to do this, tested under Linux:

```
ssh-keygen -f ~/.ssh/mykey

cat ~/.ssh/mykey.pub
```

The last command then outputs the line that you need to send to us. Encrypted communication is not needed for that, as this is intended as the publicly known part of the key. Hence the .`pub` in the filename.

## 2. Use the key to clone and update the repository

After we confirmed to have granted access to your key, you may then clone some of our private repositories like this:&#x20;

(Example: webfrontend repository. Name contains easydb for historical reasons)

```
GIT_SSH_COMMAND='ssh -i ~/.ssh/mykey' git clone git@github.com:programmfabrik/easydb-webfrontend.git
```

To be able to pull updates in the future, configure git to continue to use the same key for this clone:

```
cd easydb-webfrontend

git config core.sshCommand "ssh -i ~/.ssh/mykey"
```

