# 3.1 Creating the Driver Object in Designer

You create each driver by installing the driver packages and then modifying the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](creating-the-driver-object-in-designer.html#bl582ar)
* [Installing the Driver Packages](creating-the-driver-object-in-designer.html#brn9cu1)
* [Configuring the Driver Object](creating-the-driver-object-in-designer.html#bfveihb)
* [Deploying the Driver Object](creating-the-driver-object-in-designer.html#bfvehvc)
* [Starting the Driver](creating-the-driver-object-in-designer.html#bfvehvw)

## 3.1.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer. You can upgrade any package that is installed if there is a newer version of the package available. It is recommended to have the latest packages in the Package Catalog before creating a new driver object. For more information on upgrading packages, see "[Upgrading Installed Packages](../../../identity-manager-48/designer_admin/data/packman.html#packmanupgrade)" in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).

To verify that you have the most recent version of the driver packages in the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/package_import_a.png)
6. Select any Oracle EBS driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](creating-the-driver-object-in-designer.html#brn9cu1).

## 3.1.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.

   You need to do this for each driver you want to create.
3. Depending on the driver you want to create, select one of the following and then click Next:

   * Oracle EBS User Management Base
   * Oracle EBS HR Base
   * Oracle EBS TCA Base

   *IMPORTANT:*Run the following steps for each driver you want to create.
4. Select the optional features to install for the driver, then click Next.

   All options are selected by default depending on the driver you choose to install. The options are:

   *Default Configuration:*
   These packages contain the default configuration information for the Oracle EBS driver. Always leave this option selected.

   *Password Synchronization:*
   These packages contain the policies required to enable password synchronization. Leave this option selected if you want to synchronize passwords between the Identity Vault and the Oracle EBS system.

   *Entitlements:*
   These packages contain the policies and entitlements required to enable the driver for account creation and management with entitlements. For more information, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

   *Data Collection:*
   These packages contain the policies that enable the driver to collect data for reports. If you are using Identity Reporting, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

   *Account Tracking:*
   These packages contain the policies that enables account tracking information for reports. If you are using Identity Reporting, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).
5. (Conditional) If there are package dependencies for the packages you selected to install, you must install these dependencies to install the selected packages. Click OK to install the Password Synchronization Notification package dependency.
6. (Conditional) Click OK to install the Common Settings package, if you have not installed any other packages into the selected driver set.
7. Click OK to install the Advanced Java Class package if you have not installed any other packages into the selected driver set.
8. (Conditional) Fill in the following fields on the Common Settings page, then click Next:

   The Common Settings page is displayed only if the Common Settings package is installed as a dependency.

   *User Container:*
   Select the Identity Vault container where the users are added if they don’t already existing in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.
9. On the Driver Information page, specify a name for the driver, then click Next.
10. Select Web Service Type. You can choose one of the following web services:

    * SOAP: Choose to use the SOAP APIs
    * REST: Choose to use the REST APIs

      + Authentication Type: Select the authentication type. By default Basic is selected.
      + Http Connection Timeout: Specify the time in minutes for the driver to wait for a REST response.

      *NOTE:*REST web service type is available from Oracle EBS Driver 4.1.2 onwards.

    Once done, click Next.
11. Fill in the following fields to configure the driver, then click Next:

    *Web Service Endpoint URL of the Oracle EBS:*
    Specify the URL of the Web service.

    *EBS Username:*
    Specify a name for the EBS user. This user should have appropriate privileges to access the SOAP/REST endpoint.

    *EBS Password:*
    Specify a password for the EBS user.
12. On the Install Oracle EBS Base page, fill in the following fields for the Subscriber options, then click Next:

    *Subscriber Channel Enabled:*
    By default, the Subscriber channel is enabled. This means that the events are synchronized from Identity Manager to the Oracle EBS system. Fill the following fields for the Subscriber options:

    * *Use SSL:*
      Specify Yes to use SSL to secure communication between the driver and the Oracle EBS server. For more information, see [Section 5.0, Securing Communication](securing-communication.html).

      To use SSL, fill in the following parameters:

      *Truststore File:*
      Specify the name and path of the keystore file containing the trusted certificates used when the remote server is configured to provide server authentication. For example, c:\security\truststore. Leave this field empty when server authentication is not used.

      *Set Mutual Authentication Parameters:*
      Specify Yes to use mutual authentication between the driver and the Oracle EBS server and specify the following information:

      + *Keystore File:*
        Specify the path and the name of the keystore file that contains the trusted certificates for the remote server to provide mutual authentication. For example, C:\security\keystore. Leave this field blank when mutual authentication is not used.
      + *Keystore Password:*
        Specify the password for the keystore file. Leave this field blank when mutual authentication is not used.

    *Use Proxy:*
    Specify Yes if you want to use a proxy connection between the driver and the Oracle EBS server.

    To use a proxy connection, fill in the following parameters:

    * *Proxy Host and Port:*
      Specify the host address and the host port when a proxy host and port are used. For example: 192.10.1.3:18180.

      Or, if a proxy host and port are not used, leave this field empty.
    * *Proxy Username:*
      Specify a name for the proxy connection.
    * *Proxy Password:*
      Specify a password for the proxy connection.
    * *HTTP Errors to Retry:*
      The HTTP error codes that return a retry status. The list of integers is separated by spaces. The error codes are: 307 404 408 503 504.
13. On the Install Oracle EBS Base page, fill in the following fields for the Publisher options, then click Next:

    *Publisher Channel Enabled:*
    By default, the Publisher channel is enabled. The events are synchronized from the Oracle EBS system to the Identity Manager. Fill the following fields for the Publisher options:

    * *Listening IP Address and Port:*
      Specify the IP address of the server where this driver is installed and the port that this driver listens on. You can specify 127.0.0.1 if there is only one network card installed in the server. Choose an unused port number on your server. For example: 127.0.0.1:18180. The driver listens on this address for incoming requests, processes the requests, and returns a result.
    * *Authentication ID:*
      Specify the authentication ID to validate incoming requests if Basic Authorization (on the HTTP header) is used.
    * *Authentication Password:*
      Specify the password for the authentication ID.

      *NOTE:*The Authentication Password prompts when the Publisher channel is disabled.

    *Use SSL:*
    By default, the SSL connection is used for secure communication between the driver and the Oracle EBS server. Change this option to No if you don’t want to use SSL.

    When SSL is used, you need to fill the following parameters:

    * *Select Certificate Store Mode:*
      Select KMO if you are using eDirectory KMO for secure connection. Select Keystore to use the Java Keystore.
    * *KMO Name:*
      If you select KMO, when this server is configured to accept HTTPS connections, this is the KMO name in eDirectory. The KMO name is the name before the - in the RDN. Leave this field blank when a keystore file is issued or when HTTPS connections are not used.
    * *Keystore File:*
      If you select Keystore, when this server is configured to accept HTTPS connections, this is the path and the name of the keystore file. For example; C:\security\keystore. Leave this field blank when a KMO name is used or when HTTPS connections are not used.
    * *Keystore Password:*
      When this server is configured to accept HTTPS connections, this is the keystore file password. Leave this field blank when a KMO name is used or when HTTPS connections are not used.
    * *Server Key Alias:*
      When this server is configured to accept HTTPS connections, this is the key alias. Leave this field blank when a KMO name is used or when HTTPS connections are not used.
    * *Server Key Password:*
      When this server is configured to accept HTTPS connections, this is the key alias password (not the keystore password). Leave this field blank when a KMO name is used or when HTTPS connections are not used.

    *Require Mutual Authentication:*
    When using SSL, it is common to do only server authentication. However, if you want to force both client and server to present certificates during the handshake process, select Required.

    *Polling Interval in Seconds:*
    Specify the number of seconds that the Publisher channel waits after running the polling script and sending Oracle EBS events to the Identity Manager engine. The default value is 60 seconds.

    *Heartbeat Interval in Minutes:*
    Specifies how often, in minutes, the driver shim contacts the Identity Manager engine when there has not been any traffic during the interval time. Specify 0 to disable the heartbeat. The default value is 1 minute.
14. Fill in the following fields for the Remote Loader information, then click Next:

    *Connect To Remote Loader:*
    Select Yes or No to determine if the driver will use the Remote Loader. For more information, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_windows/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

    If you select No, skip to [Step 17](creating-the-driver-object-in-designer.html#brnbqsk). If you select Yes, use the following information to complete the configuration of the Remote Loader:

    *Host Name:*
    Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

    *Port:*
    Specify the port number for this driver. Each driver connects to the Remote Loader on a separate port. The default value is 8090.

    *KMO:*
    Specify the Key Name (for example, kmo=remotecert) of the Key Material Object (KMO) containing the keys and certificate to be used for SSL.

    If you used spaces in the certificate name, you need to enclose the KMO object nickname in single quotation marks.

    *Remote Loader Password:*
    Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

    *Driver Password:*
    Specify a password for the driver to authenticate to the Identity Manager server. It must be the same password that is specified as the Driver Object Password on the Remote Loader.
15. (Conditional) On the Install Oracle EBS Managed System Information page, fill in the following fields to define the ownership of the Oracle EBS system, then click Next:

    *General Information*

    * Name: Specify a descriptive name for the managed system.
    * Description: Specify a brief description of the managed system.
    * Location: Specify the physical location of the managed system.
    * *Vendor:*
      Specify Oracle as the vendor of the managed system.
    * Version: Specify the version of the managed system.

    *System Ownership*

    * Business Owner: Select a user object in the Identity Vault that is the business owner of the Oracle EBS system. This can only be a user object, not a role, group, or container.
    * Application Owner: Select a user object in the Identity Vault that is the application owner of the Oracle EBS system. This can only be a user object, not a role, group, or container.

      This page is only displayed if you selected to install the Data Collection packages and the Account Tracking packages.

    *System Classification*

    * Classification: Select the classification of the Oracle EBS system. This information is displayed in the reports. The options are as follows:

      + Mission-Critical
      + Vital
      + Not-Critical
      + Other

        If you select Other, you must specify a custom classification for the Oracle EBS system

    * Environment: Select the type of environment the Oracle EBS system provides. The options are as follows:

      + Development
      + Test
      + Staging
      + Production
      + Other

        If you select Other, you must specify a custom environment for the Oracle EBS system.
16. (Conditional) On the Install Oracle EBS Account Tracking page, fill in the following fields for Account Tracking, then click Next:

    *Realm:*
    Specify the name of the realm, security domain, or namespace in which the account name is unique. You must set the Realm to the Oracle EBS Domain Name.
17. Review the summary of tasks that will be completed to create the driver, then click Finish.
18. Continue with [Configuring the Driver Object](creating-the-driver-object-in-designer.html#bfveihb).

## 3.1.3 Configuring the Driver Object

After importing the driver configuration file, you need to configure the driver object before it can run. Complete the following tasks to configure the driver:

* *Set Up a Secure HTTPS Connection:*
  You can configure the connection between the driver and Oracle EBS to use a secure HTTPS connection rather than an HTTP connection. For instructions, see [Section 5.0, Securing Communication](securing-communication.html).
* *Configure the driver parameters:*
  There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to configure the driver parameters located on the Driver Configuration page. For information about the driver parameters, see [Driver Parameters](driver-configuration.html#b4m4h9a).
* *Customize the driver policies and filter:*
  Modify the driver policies and filter to implement your business policies.

Continue with [Deploying the Driver Object](creating-the-driver-object-in-designer.html#bfvehvc).

## 3.1.4 Deploying the Driver Object

After the driver object is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 4](creating-the-driver-object-in-designer.html#bfvehvl), otherwise, specify the following information, then click OK:

   *Host:*
   Specify the IP address or DNS name of the server hosting the Identity Vault.

   *Username:*
   Specify the DN of the user object used to authenticate to the Identity Vault.

   *Password:*
   Specify the user’s password.
4. Read the deployment summary, then click Deploy.
5. Read the message, then click OK.
6. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.
7. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude, then click OK.
   2. Repeat [Step 7.a](creating-the-driver-object-in-designer.html#bfvehvr) for each object you want to exclude, then click OK.
8. Click OK.

## 3.1.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Start Driver.
3. Continue with [Activating the Driver](activating-the-driver.html).
