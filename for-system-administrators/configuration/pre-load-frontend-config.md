---
description: >-
  When initializing an instance, set in fylr.yml values for the frontend
  configuration.
---

# pre-load frontend config

* Some configuration is done in fylr.yml.
* Some configuration is done in the web-frontend of fylr.
* If you want to avoid configuration in the frontend, for example when installing many similar instances, you can set initial values for the frontend configuration in fylr.yml.
* As soon as the SQL Database is used for the first time (during the first start of a fylr instance, or after a purge), those initial values in fylr.yml are copied to the database. But as soon as they are in the database, they are only read and written in the database and ignored in `fylr.yml`. So make sure your desired values are in `fylr.yml` _before_ the first use of the SQL database. In other words: if you want to change these settings _after_ the first start of fylr, then you _have_ to use the web-frontend.

## How to configure a few initial values for the frontend

1. Get the desired configuration for the initial values. As there are hundreds of settings and many variants and scenarios, these are not documented explicitly. Instead, we suggest to...&#x20;
   1. Configure your desired values in another running fylr instance, in the frontend.
   2.  Download that configuration: (it will be in JSON format)

       <figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption><p>Cogwheel menu at the bottom of the Base Configuration</p></figcaption></figure>


   3.  Extract from the downloaded JSON file the desired settings. In this example, we want to make sure the Service `Email Notifications` is started. The relevant JSON is:&#x20;

       ```
       {
           "system": {
               "config": {
       [...]
                   "notification_scheduler": {
                       "active": true,
                       "active:info": {
                           "is_default": false
                       }
                   },
       [...]
       ```
   4.  Convert the JSON syntax into YAML syntax: (you can omit the block around `is_default`)

       ```
       system:
         config:
           notification_scheduler:
             active: true
       ```
2.  Put the YAML configuration into `fylr.yml` for the to-be-initialized fylr instance:

    ```
    fylr+:
      db:
        init:
          config:
            system:
              config:
                notification_scheduler:
                  active: true
    ```
3. only then start this fylr instance

## How to configure many initial values for the frontend

When you want to for example change the produce configuration for preview versions, there are thousands of JSON lines. Instead of converting them all to YAML, use the JSON file directly. The first few steps are the same as in the previous paragraph:

1. Configure your desired values in another running fylr instance, in the frontend.
2. Download that configuration: (it will be in JSON format)

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption><p>Cogwheel menu at the bottom of the Base Configuration</p></figcaption></figure>

3. Optionally change the JSON configuration file to your requirements.
4. Put the downloaded JSON file as (in this example) `config.json` into the same directory as the `fylr.yml` file.
5.  Configure your to-be-initialized fylr instance to use the `config.json` file, in `fylr.yml`:

    ```
    fylr+:
      db:
        init:
          configFile: config.json
          config:
          # this has to be empty or else configFile is not loaded
          locations:
            assets:
              kind: file
    [... etc. ...]
    ```
6. Make sure you have no configuration-"leaves" in the `config:`-"branch" as shown in the example above. In other words: `config` has to be empty or else it will replace `configFile`.
7. Only then start the new fylr instance.

{% hint style="info" %}
`config.json` will only be used if this SQL Database was never used before by fylr.
{% endhint %}
