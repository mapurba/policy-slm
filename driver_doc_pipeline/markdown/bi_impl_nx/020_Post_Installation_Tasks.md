# 3.9 Post-Installation Tasks

1. If desired, set Startup Option on the Driver Configuration page to Auto start. This causes the driver to start when the Metadirectory engine starts.
2. Set the driver shim to start automatically when the connected system starts. For details, see your operating system documentation.
3. Activate the driver.

   Identity Manager and Identity Manager drivers must be activated within 90 days of installation or they shut down. At any time during the 90 days, or afterward, you can activate Identity Manager products.

   For details about activating NetIQ Identity Manager Products, see the Identity Manager 4.8 Installation Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

You can run the nxdrv-config command on the connected system at any time to change the driver shim configuration. You can configure the Remote Loader and driver passwords, SSL settings, the PAM or LAM module, and the schema. For details about using nxdrv-config, see [Using the nxdrv-config Command](b4339kg.html).
