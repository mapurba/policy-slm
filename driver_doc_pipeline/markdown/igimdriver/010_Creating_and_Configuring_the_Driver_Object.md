# 2.5 Creating and Configuring the Driver Object

This section helps you create and configure the IGIM driver. You perform these tasks in your project in Designer.

* [Importing the Current Driver Packages](creating-and-configuring-the-netiq-idm-igim-driver.html#importing-latest-driver-packages-for-netiq-idm-igim-driver)
* [Creating the Driver Object](creating-and-configuring-the-netiq-idm-igim-driver.html#creating-the-netiq-idm-igim-driver)
* [Configuring the Driver Settings](creating-and-configuring-the-netiq-idm-igim-driver.html#configuring-the-netiq-igim-driver-settings)

## 2.5.1 Importing the Current Driver Packages

NetIQ regularly provides updates to the Identity Manager drivers. You must have the latest content for the IGIM driver. For more information about the packages, see [Planning to Install and Configure the Driver](planning-to-install-and-configure-netiq-igim-driver.html).

1. Open Designer.
2. Select Help > Check for Package Updates.
3. Select the updated packages for the driver that you want to update. Or, click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
4. Click OK to import the selected packages, then click OK in the successfully imported packages message.
5. When the update completes, restart Designer for the changes to take effect.

## 2.5.2 Creating the Driver Object

This section helps you configure the IGIM driver and establish its basic settings.

*NOTE:*The IGIM driver requires NOVLCOMSET, the driver set package for common settings. Ensure that you import this packages before configuring the driver. For more information about the required packages, see [Planning to Install and Configure the Driver](planning-to-install-and-configure-netiq-igim-driver.html).

1. In the Modeler view of Designer, select Developer.
2. (Conditional) If you have more than one driver set in the Identity Vault, select the driver set in the Modeler view to which you want to add the driver.
3. In the Palette view, expand Service.
4. Drag Identity Gateway Integration Module to the Modeler view.

   This action opens the Driver Configuration Wizard.
5. For Select Driver Base Configuration, select Identity Gateway Integration Module Base, then click Next.
6. For Optional Features, select the following item:

   * Identity Gateway Integration Module Default
7. Click Next.
8. For Driver Name, specify a value. For example, Identity Gateway Integration Module Driver.
9. Click Next.
10. (Conditional) On the Driver Parameters page, specify the following details, and then click Next:

    * *Preferred Server:*
      Specify the selection mode for the preferred server.The default setting is Auto. This setting automatically selects a preferred server from the list of servers associated with the driver set. To select a specific server, change the setting to Manual.
    * *Default Page Size:*
      Specify the page size of the cached event pages. The default value is 100.
    * *Flush Strategy:*
      Specify the method to remove the already read events. The options are Auto and Manual. The default setting is Auto. If you want the driver to purge the read events automatically, leave the setting as default. If the reading client must explicitly purge the older events, change the setting to Manual.
    * *Hostname:*
      Specify the network interface on which the driver accepts connections for the REST server. To listen on all interfaces, leave the field empty.
    * *Port:*
      Specify the port number on which the driver accepts connections for the REST server.

    * *Connection Protocol:*
      Specify the connection protocol to use. It is recommended to use a secured (https) connection. When you select https, the following parameters are displayed:

      + *Driver configuration mode:*
        Specify the configuration mode for the driver. Select Local to configure the driver to run with the Identity Manager engine. To configure the driver to run with the Remote Loader, select Remote.
      + *KMO (for secure connection):*
        If you select Local in Driver configuration mode, specify the key name of the Key Material Object (KMO) that contains the keys and certificate that the REST server uses for an SSL connection with the Identity Manager Identity with Changes collector. The default value is SSL CertificateDNS.
      + *Keystore file:*
        If you select Remote in Driver configuration mode, specify the name and path of the keystore file containing the trusted certificates that the REST server uses when the remote server is configured for server authentication.
      + *Keystore Password:*
        Specify the password for the private key for authenticating to the remote server.
    * *Heartbeat Interval (in minutes):*
      Allows the driver to send a periodic status message on the Publisher channel when there has been no Publisher channel traffic for the given number of minutes. The default value is 1 minute.
11. (Conditional) Select Yes or No to determine if the driver will use the Remote Loader. If you select No, skip to [Step 12](creating-and-configuring-the-netiq-idm-igim-driver.html#last-step). If you select Yes, use the following information to complete the Remote Loader configuration, then click Next:

    * *Host Name:*
      Specify the hostname or IP address of the server where the driver’s Remote Loader service is running.
    * *Port:*
      Specify the port number where the Remote Loader is installed and running. The default port number is 8090.
    * *KMO:*
      Specify the key name of the Key Material Object (KMO) that contains the keys and certificate the Remote Loader uses for an SSL connection. This parameter is only used when you use SSL for connections between the Remote Loader and the Identity Manager engine.
    * *Other Parameters:*
      Specify any other parameters required to connect to the Remote Loader. Any parameters specified must use a key-value pair format, as follows: paraName1=paraValue1 paraName2=paraValue2.
    * *Remote Password:*
      Specify the Remote Loader’s password as defined on the Remote Loader. The Identity Manager server (or Remote Loader) requires this password to authenticate to the Remote Loader.
    * *Driver Password:*
      Specify the driver object password that is defined in the Remote Loader service. The Remote Loader requires this password to authenticate to the Identity Manager server.
12. Review the summary of tasks that will be completed to create the driver, then click Finish.

After you have installed the driver, you can change the configuration for your environment.

If you do not need to configure the driver, continue with [Deploying the Driver Object](deploying-the-netiq-idm-igim-driver.html).

## 2.5.3 Configuring the Driver Settings

There are many settings that can help you customize and optimize the driver. The settings are defined in Driver Parameters located on the Driver Configuration page. These settings must be configured properly for the driver to start and function correctly.

To access the Driver Properties page:

1. Open your project.
2. In the Modeler view, right-click the driver icon ![IGIM-driver-icon](../graphics/driver_icon_n.png "IGIM-driver-icon") or the driver line, then select Properties.
3. Make the changes you want, then continue with [Deploying the Driver Object](deploying-the-netiq-idm-igim-driver.html).
