---
description: also known as On Premise Installation
---

# if we install on your server

We offer to install fylr (or troubleshoot) on _your_ server in case the following criteria are met\
(and if a business agreement was made).\
\
If these criteria below are _not_ possible, we still have at least two alternative approaches: _You_ can install on your server; or we install on _our_ servers (which then needs a hosting contract with us).<br>

* Pre-installed **Debian** or **Ubuntu**. \
  A version which is recent enough to be in active maintenance by the distribution. \
  Without Desktop, with SSH server, without firewall software.\
  \
  fylr can run on many more operating systems, but we do not have sufficient experience with all of them to do the installation ourselves.\
  \
  **RedHat** may be possible as a pioneer project, but we only have limited experience there as of yet.<br>
* We need HTTPS (Port 443) and SSH access **to your server**.\
  Our approach is:\
  <mark style="color:$success;">**SSH is encrypted, secure and state of the art, even as a permanently open port.**</mark>
* The account has to have full administrative rights, either directly as `root` or via `sudo` or `su`.
* Access can be granted by password or - preferred - by our public ssh key: \
  `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINHZyevoIWd21NeOejA3AtXsiY5fOhDFXjhnMFmRBOMi`&#x20;
* The SSH access has to be without manual tokens, PINs, TANs, telephone calls, etc.. We have multiple employees sharing tasks and also with separate areas of knowledge and responsibility, so one hardware token will not work and individual accounts would be too numerous. To fit the tasks for you into our work, we cannot predict when we will need access and too often it is outside of business hours to rely on calling you first to open the connection. A permanently open SSH port with just one account for our company solves all of this. We will make sure that the minimal number of people and data is accessed.
* **Optional**: The access may be restricted to our IP address. We are using the static IP address `138.199.160.200` as the source IP address during access. This can be the second factor besides the ssh key (or password) to be sure it is _us_ who is connecting. Thus providing "Multi Factor Authentication" / "Two Factor Authentication".
* **Optional**: The SSH port can be configured by the customer. The default is 22.
* **Optional**: The access can be secured via a customer operated SSH proxy (also known as Jumphost). This only includes SSH protocol software, not virtual desktops.
* **Optional**: Additionally, a customer operated OpenVPN server can be used. We can evaluate other software, if it is compatible with OpenConnect or if it can be done with OpenFortiVPN. All these have encryption, which is made redundant by SSH's encryption, and they increase complexity and fragility and are thus not recommended.
* **Optional**: We can offer you to connect to our SSH server and use that connection to tunnel to you - sometimes called a "reverse SSH tunnel". This tends to be unstable and is thus not recommended.<br>
* **From your server to the internet** we need access to download our software and required software such as docker, Opensearch, PostgreSQL, plugins, etc..\
  We strongly **recommend** to give your fylr server general internet access instead of just specific sites. This will never be a desktop computer where someone sits in front of and clicks on malicious links or attachments. \
  If you need a whitelist of allowed sources, it will include the following, but docker could anytime change these or add more required sites ...\
  https://docker.fylr.io (fylr core),\
  https://download.docker.com,\
  https://artifacts.opensearch.org and https://artifacts.elastic.co (indexer plugin),\
  https://raw.githubusercontent.com (tools and configuration templates), \
  https://github.io and https://github.com (fylr plugins),\
  &#x20;   for indexer and PostgreSQL:\
  https://auth.docker.io,  \
  https://registry-1.docker.io,  \
  https://index.docker.io,  \
  https://cloudfront.net,  \
  https://production.cloudflare.docker.com\
  \
  ... and of course the **package sources** of the Linux distribution used on your server; for security updates, tools and operating system upgrades.\
  \
  **Optional**: Use of a proxy for these is possible, but will take longer to configure. Not tested for download of fylr plugins yet.

We recommend that we test SSH access a few working days prior to the installation, whereby we also check the prerequisites of the server.

The installation takes several minutes or a few hours in case of complications.<br>

## if we shall maintain fylr on your server

Also known as a maintenance contract.

* We need permanent SSH access to your server, to do maintenance tasks and to monitor your server. Our monitoring software connects every few minutes, so it is essentially a permanent connection.
* The SSH access has to be fully automated, with no manual tokens, PINs, TANs, telephone calls, etc. so that our monitoring software can run on its own.
