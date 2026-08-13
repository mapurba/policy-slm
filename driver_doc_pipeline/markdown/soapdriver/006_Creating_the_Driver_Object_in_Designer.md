# 3.1 Creating the Driver Object in Designer

You create the SOAP driver object by installing the driver packages and then modifying the configuration to suit your environment. After you create and configure the driver, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](create-driver-object-designer.html#bl582ar)
* [Installing the Driver Packages](create-driver-object-designer.html#brtiuc0)
* [Configuring the Driver Object](create-driver-object-designer.html#bfveihb)
* [Deploying the Driver Object](create-driver-object-designer.html#bfvehvc)
* [Starting the Driver](create-driver-object-designer.html#bfvehvw)

*NOTE:*To create driver objects, you now need to use the new package management features provided in Designer.

## 3.1.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer and can be updated after they are initially installed. You must have the most current version of the packages in the Package Catalog before you can create a new driver object.

To verify that you have the most recent version of the driver packages in the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/package_import_a.png)
6. Select any SOAP driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](create-driver-object-designer.html#brtiuc0).

## 3.1.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select SOAP Base, then click Next.
4. Select the type of SOAP driver packages to install, then click Next.

   The options are:

   * DSML 2.0
   * SPML 1.0
   * SPML 2.0
   * Other
5. Select the optional features to install for the SOAP driver, then click Next.

   The options are:

   *SOAP Password Synchronization:*
   This packages contains the policies that enable the SOAP driver to synchronize passwords. If you want to synchronize passwords, verify that this option is selected. For more information, see the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

   *Managed System Information:*
   This package contains the policies that enable Identity Reporting. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).
6. (Conditional) If there are package dependencies for the packages you selected to install, you must install them to install the selected package. Click OK to install the package dependency listed.
7. (Conditional) If more than one type of package dependency must be installed, you are presented with these packages separately. Continue to click OK to install any additional package dependencies.
8. On the Driver Information page, specify a name for the driver, then click Next.
9. On the Install SOAP Base page, fill in the following fields for the Subscriber options, then click Next:

   *URL of the SOAP server or Web Service:*
   Specify the URL of the SOAP server or Web service.

   *Authentication ID:*
   Specify the ID used to authenticate to the SOAP server or Web service.

   *Authentication Password:*
   Specify the password for the authentication ID.

   *Truststore file:*
   Specify the path and the name of the keystore file that contains the trusted certificates for the remote server to provide server authentication. For example, c:\security\truststore. Leave this field blank when server authentication is not used.

   *Set mutual authentication parameters:*
   Select Show if you want to set mutual authentication information.

   * *Keystore file:*
     Specify the path and the name of the keystore file that contains the trusted certificates for the remote server to provide mutual authentication. For example, C:\security\keystore. Leave this field blank when mutual authentication is not used.
   * *Keystore password:*
     Specify the password for the keystore file. Leave this field blank when mutual authentication is not used.

   *Proxy host and port:*
   Specify the host address and the host post when a proxy host and port are used. For example: 192.10.1.3:18180. Choose an unused port number on your server. Otherwise, leave this field blank.
10. On the Install SOAP Base page, fill in the following fields for the Publisher options, then click Next:

    *Listening IP address and port:*
    Specify the IP address of the server where this driver is installed and the port that this driver listens on. You can specify 127.0.0.1 if there is only one network card installed in the server. Choose an unused port number on your server. For example: 127.0.0.1:18180. The driver listens on this address for incoming requests, processes the requests, and returns a result.

    *Authentication ID:*
    Specify the authentication ID to validate incoming requests if Basic Authorization (on the HTTP header) is used.

    *Authentication Password:*
    Specify the password for the authentication ID.

    *KMO name:*
    When this server is configured to accept HTTPS connections, this is the KMO name in eDirectory. The KMO name is the name before the - in the RDN. Leave this field blank when a keystore file is issued or when HTTPS connections are not used.

    *Keystore file:*
    When this server is configured to accept HTTPS connections, this is the path and the name of the keystore file. For example; C:\security\keystore. Leave this field blank when a KMO name is used or when HTTPS connections are not used.

    *Keystore password:*
    When this server is configured to accept HTTPS connections, this is the keystore file password. Leave this field blank when a KMO name is used or when HTTPS connections are not used.

    *Server key alias:*
    When this server is configured to accept HTTPS connections, this is the key alias. Leave this field blank when a KMO name is used or when HTTPS connections are not used.

    *Server key password:*
    When this server is configured to accept HTTPS connections, this is the key alias password (not the keystore password). Leave this field blank when a KMO name is used or when HTTPS connections are not used.

    *Require mutual authentication:*
    When using SSL, it is common to do only server authentication. However, if you want to force both client and server to present certificates during the handshake process, select Required.

    *Heartbeat interval in minutes:*
    Specify the heartbeat interval in minutes. Leave this field blank to turn off the heartbeat.
11. Fill in the following fields for the Remote Loader information, then click Next:

    *Connect To Remote Loader:*
    Select Yes or No to determine if the driver will use the Remote Loader. For more information, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front).

    If you select No, skip to [Step 12](create-driver-object-designer.html#brd1lmr). If you select Yes, use the following information to complete the configuration of the Remote Loader:

    *Host Name:*
    Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

    *Port:*
    Specify the port number for this driver. Each driver connects to the Remote Loader on a separate port. The default value is 8090.

    *Remote Loader Password:*
    Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

    *Driver Password:*
    Specify a password for the driver to authenticate to the Identity Manager server. It must be the same password that is specified as the Driver Object Password on the Remote Loader.
12. (Conditional) This page is displayed only if you selected to install the Managed Systems Information packages. On the Install SOAP Managed System Information page, fill in the following fields to define your SOAP system, then click Next:

    *Name:*
    Specify a descriptive name for this SOAP system. The name is displayed in reports.

    *Description:*
    Specify a brief description for this SOAP system. The description is displayed in reports.

    *Location:*
    Specify the physical location of this SOAP system. The location is displayed in reports.

    *Vendor:*
    Leave Microsoft as the vendor of SOAP. This information is displayed in reports.

    *Version:*
    Specify the version of this SOAP system. The version is displayed in the reports.
13. (Conditional) This page is displayed only if you selected to install the Managed Systems packages. On the Install SOAP Managed System Information page, fill in the following fields to define the ownership of the SOAP system, then click Next:

    *Business Owner:*
    Select a user object in the Identity Vault that is the business owner of the SOAP system. This can only be a user object, not a role, group, or container.

    *Application Owner:*
    Select a user object in the Identity Vault that is the application owner of the SOAP system. This can only be a user object, not a role, group, or container.
14. (Conditional) This page is displayed only if you selected to install the Managed System packages. On the Install SOAP Managed System Information page, fill in the following fields to define the classification of the SOAP system, then click Next:

    *Classification:*
    Select the classification of the SOAP system. This information is displayed in the reports. You options are:

    * Mission-Critical
    * Vital
    * Not-Critical
    * Other

      If you select Other, you must specify a custom classification for the SOAP system.

    *Environment:*
    Select the type of environment the SOAP system provides. The options are:

    * Development
    * Test
    * Staging
    * Production
    * Other

      If you select Other, you must specify a custom classification for the SOAP system.
15. Review the summary of tasks that will be completed to create the driver, then click Finish.
16. After you have installed the driver, you must change the configuration for your environment. Proceed to [Configuring the Driver Object](create-driver-object-designer.html#bfveihb).

## 3.1.3 Configuring the Driver Object

After the driver packages are installed, you need to configure the driver before it can run. You should complete the following tasks to configure the driver:

* *Configure the driver parameters:*
  There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to review the [Driver Parameters](driver-configuration.html#b4m4h9a) located on the Driver Configuration page. The Driver Parameters let you configure the publication method and other parameters associated with the Publisher channel.
* *Customize the driver policies and filter:*
  The driver policies and filter control data flow between the Identity Vault and the application. You should ensure that the policies and filters reflect your business needs. For instructions, see [Section 5.0, Customizing the Driver](customize-driver.html).
* *Set Up a Secure HTTPS Connection:*
  The connection between the driver and the SPML or DSML server can be configured to use a secure HTTPS connection rather than an HTTP connection. For instructions, see [Section 6.0, Securing Communication](secure-communication.html).

After completing the configuration tasks, continue with [Deploying the Driver Object](create-driver-object-designer.html#bfvehvc).

## 3.1.4 Deploying the Driver Object

After the driver object is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 4](create-driver-object-designer.html#bfvehvl); otherwise, specify the following information, then click OK:

   *Host:*
   Specify the IP address or DNS name of the server hosting the Identity Vault.

   *Username:*
   Specify the DN of the user object used to authenticate to the Identity Vault.

   *Password:*
   Specify the user’s password.
4. Read the deployment summary, then click Deploy.
5. Read the message, then click OK.
6. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user. Whatever rights that the driver needs to have on the server, the DriversUser object must have the same security rights.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.

      For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see “Establishing a Security Equivalent User” in the [Identity Manager 4.0.2 Security Guide](https://www.netiq.com/documentation/idm402/idm_security/?page=/documentation/idm402/idm_security/data/front.html).
7. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude, then click OK.
   2. Repeat [Step 7.a](create-driver-object-designer.html#bfvehvr) for each object you want to exclude, then click OK.
8. Click OK.
9. Continue with the next section, [Starting the Driver](create-driver-object-designer.html#bfvehvw).

## 3.1.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs. You can use Identity Console or dxcmd commands to start the driver.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Live > Start Driver.
