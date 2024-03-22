---
description: Connect to remote easydb and fylr instance
---

# Connector Plugin

{% hint style="info" %}
Please note: this plugin is licensed as a separate module. If in doubt, please check your license agreement.
{% endhint %}

## About

The Connector Plugin (`easydb-connector-plugin`) is a frontend plugin which allows to connect to remote easydb and fylr instances. The plugin performs searches in remote instances and shows the results in the local frontend.

The plugin needs to be installed and enabled on the local and the remote instances.

## Adding the Plugin

First, make sure the plugin is added to your fylr and enabled by checking the [Plugin Manager](../../for-administrators/plugin-manager.md). If not, add the plugin. To license and get the plugin, please get in touch with Programmfabrik GmbH.

## Configuration

Open the [Base Configuration](../../for-administrators/readme/), go to "Plugins" and open "easydb-connector-plugin".

First, enable the Connector by enabling "Activated for users".

Under "easydb instances for Connector", add one or more connections to remote easydb5 and fylr instances.

For each remote instance, set the following configuration:

| Configuration                                    | Description           | Notes        |
| ------------------------------------------------ | --------------------- | ------------ |
| **Enable**                                       | Enable/disable this connection | |
| **Name**                                         | Name of this connection, is shown in the Connector Overview | |
| **URL**                                          | The Server URL of the remote instance | The URL is mandatory. |
| **Login**                                        | Connector user login | The login is mandatory. The user should have sufficient rights ([see below](#setting-up-fylr-for-connector-partners)) |
| **Password**                                     | Connector user password | The password is mandatory. |
| **OAuth2 Client ID**                             | Client ID of a remote fylr | This is mandatory, if the remote instance is a fylr. Can be ignored for remote easydb5 instances. |
| **OAuth2 Client Secret**                         | Client Secret (in clear text) of a remote fylr | This is mandatory, if the remote instance is a fylr and the remote instance is configured with a secret. If the fylr instance is public, or the remote instance is an easydb5, this can be igored. |
| **Allow HTTPS without certificate verification** | Enable this to skip certificate verification, if the remote instance uses HTTPS |  |
| **Timeout in seconds**                           | If there are connection problems to the remote instance, and the authentication takes too long, timeout after this duration. | `0`: no timeout, default: `10` |

## Setting up fylr for connector partners

To enable your connector partners to access your fylr, you must first determine which content they should have access to.

To do this, create a new user account in the "Users" area and assign the right "Allow connector connections from other instances via this user" in the "System Rights" tab, as well as the "Download" frontend function if you want to allow your connector partner to download.

{% hint style="info" %}
We recommend setting up a separate user account for each connector partner, as this allows you to share your content in a targeted manner.
{% endhint %}

Now define in the "Pools" (or "Objecttype") area, which content your connector partner should have access to by adding a new line in the "Permissions" tab and assigning the necessary read and download permissions for the previously created user. Repeat this for all pools and, if necessary, in the "Tags & workflows" area.

{% hint style="info" %}
Please note that you must assign at least the rights "View data records" and "Permitted masks" for the authorizations.
{% endhint %}

To ensure that the users of the connector partner can also use the expert search, grant all necessary rights to the connector user in the "Objecttypes" area.

Finally, send your URL, login and password, as well as the OAuth2 Client informatio to your connector partner.

## Security

When connecting to a connector partner, a user specially set up for this purpose is used. The login and password of this user is used to log in to the partner.

The token generated upon successful login can be used to execute any API requests with the user's rights. It is therefore essential that you do not grant this user too extensive rights, which may allow data to be changed or deleted or settings to be changed on the local fylr.

{% hint style="warning" %}
The rights of the connector user should only include **search** rights and **read** rights to the pools, object types and masks that are to be shared within the connector network. No further rights should be granted to this user!
{% endhint %}

In the Base Configuration, the login, password and a potential Client secret must be stored in plain text for each connector partner. Therefore, make sure to restrict access to the Base Configuration as much as possible, so that only the administrator has access to the stored user data.

Logging in to the connector partners is done via the server part of the plugin. The token used in the frontend for the search is requested once by the plugin. If the current user has rights to use the connector, a login is carried out for each connector using the login data from the Base Configuration and a check is also made to see whether the user has access rights to the connector.

