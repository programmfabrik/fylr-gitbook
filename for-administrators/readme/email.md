---
description: >-
  In this section the email server can be configured, so FYLR can for example
  send emails when a collection was shared or a workflow was triggered.
---

# Email

## General

### From

Please use an email address which the SMTP server accepts as sender.

### Signature

Include a signature in all emails. Optional.

### Administrator Email

One or more addresses. A warning about a soon expiring license is sent there.

## Configuration

### Server Address

SMTP address including port, like smtp.gmail.com:587

### HELO Domain

The domain name that FYLR uses to introduce himself as, towards the SMTP server. (HELO or EHLO message in the smtp protocol.) This can be used by the SMTP server to check DNS and reject FYLR, so pick one that is acceppted by the chosen SMTP server.

### Server TLS

Use encryption when connecting to the SMTP server? STARTTLS is a variant where the first connection is unencrypted but during the communication, encryption is then soon started. Choose what the SMTP server supports.

### Skip certificates check

If you trust the SMTP server anyway (like it is in your Local Area Network and you already have measures against imposters/man-in-the-middle attacks), you can configure here to not check its certificate.

### PLAIN AUTHENTICATION

One of three alternatives, choose one. If in doubt, check PLAIN first. It is secure if you use encryption.

#### Identity

Part of the official protocol but rarely used. Typically, just use Username and Password.

#### Username

Username string to send to the SMTP server to authenticate, if at all needed.

#### Password

Password string to send to the SMTP server to authenticate, if at all needed. To remove the password from the base configuration, use "-" and save.

### LOGIN AUTHENTICATION

One of three alternatives, choose one. If in doubt, check PLAIN first.

#### Username

Username string to send to the SMTP server to authenticate, if at all needed.

#### Password

Password string to send to the SMTP server to authenticate, if at all needed. To remove the password from the base configuration, use "-" and save.

### CRAM-MD5 AUTHENTICATION

One of three alternatives, choose one. If in doubt, check PLAIN first.

#### Username

Username string to send to the SMTP server to authenticate, if at all needed.

#### Password

Password string to send to the SMTP server to authenticate, if at all needed. To remove the password from the base configuration, use "-" and save.
