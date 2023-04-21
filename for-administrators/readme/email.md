---
description: In this section the email server can be configured. fylr can be made to send out ...(TODO: example) to its users.
---

# Email

## General

### From
Please use an email address which the SMTP server accepts.

### Signature
Optional.

### Administrator Email
TODO: is it just for showing this to the users? Or is fylr sending alerts to these addresses?


## Configuration

### Server Address
SMTP address including port, like smtp.gmail.com:587

### HELO Domain
The domain name that fylr uses to introduce himself as, towards the SMTP server. (HELO or EHLO message in the smtp protocol.)  This can be used by the SMTP server to check DNS and reject fylr, so pick one that is acceppted by the chosen SMTP server.

### Server TLS
Use encryption when connecting to the SMTP server? STARTTLS is a variant where the first conenction is unencrypted but during the communication, encryption is then soon started. Choose what the SMTP server supports.

### Skip certificates check
If you trust the SMTP server anyway (like it is in your Local Area Network and you already have measures against imposters/man-in-the-middle attacks), you can configure here to not check its certificate.

### PLAIN AUTHENTICATION
One of three alternatives, choose one. If in doubt, check PLAIN first. It is secure if you use encryption.

#### Identity
Part of the official protocol but rarely used. Typically, just use Username and Password.

#### Username
Username string to send to the SMTP server to authenticate, if at all needed.

#### Password
Password string to send to the SMTP server to authenticate, if at all needed.

### LOGIN AUTHENTICATION
One of three alternatives, choose one. If in doubt, check PLAIN first.

#### Username
Username string to send to the SMTP server to authenticate, if at all needed.

#### Password
Password string to send to the SMTP server to authenticate, if at all needed.

### CRAM-MD5 AUTHENTICATION
One of three alternatives, choose one. If in doubt, check PLAIN first.

#### Username
Username string to send to the SMTP server to authenticate, if at all needed.

#### Password
Password string to send to the SMTP server to authenticate, if at all needed.
