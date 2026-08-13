# 3.1 Creating the Driver Object in Designer

Create the GroupWise driver by installing the driver packages and then modifying the configuration to suit your environment. After you create and configure the driver, you need to deploy it to the Identity Vault and start it.

* [Importing the Driver Packages](create-driver-object-designer.html#bl582ar)
* [Installing the Driver Packages](create-driver-object-designer.html#brn9cu1)
* [Configuring the Driver Object](create-driver-object-designer.html#bfveihb)
* [Deploying the Driver](create-driver-object-designer.html#bfvehvc)
* [Associating Identity Vault with GroupWise System](create-driver-object-designer.html#b1d27cy6)
* [Starting the Driver](create-driver-object-designer.html#bfvehvw)

## 3.1.1 Importing the Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer.You can upgrade any package that is installed if there is a newer version of the package available. NetIQ recommends that you have the latest packages in the Package Catalog before creating a new driver object.

You can update driver packages at any time. They are stored in the Package Catalog. Packages are initially imported into the Package Catalog when you create a project, import a project, or convert a project. It is important to verify you have the latest packages imported into the Package Catalog before you install the driver.

To verify that Package Catalog has the most recent version of the driver packages, perform the following steps:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.

   Ensure that you have the latest version of the Common Settings packages in the Package Catalog.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. Continue with [Installing the Driver Packages](create-driver-object-designer.html#brn9cu1).

## 3.1.2 Installing the Driver Packages

Install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.

   or

   Drag and drop the GroupWise driver from the palette into the Modeler space.
3. Select GroupWise REST Base, then click Next.
4. Select the optional features to install the GroupWise driver. All options are selected by default. The options are:

   *Default Configuration:*
   These packages contain the default configuration information for the GroupWise driver. This is a mandatory package. Always leave this option selected.

   *Password Synchronization:*
   These packages contain the policies required to synchronize passwords to GroupWise.

   *Entitlements:*
   These packages contain the policies and entitlements required to enable the driver for account creation and management with entitlements.

   *Data Collection:*
   These packages contain the policies that enable the driver to collect data for reports. If you are using the Identity Reporting, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

   *Account Tracking:*
   These packages contain the policies that enable account tracking information for reports. If you are using the Identity Reporting Module, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).
5. Click Next.
6. (Conditional) Click OK to install the Password Synchronization Notification package dependency.
7. (Conditional) If there are package dependencies for the packages you selected to install, you must install these dependencies to install the selected packages. Click OK to install the Advanced Java Class and Common Settings packages, if you have not installed any other packages into the selected driver set.
8. (Conditional) If not already configured, fill in the following fields on the Common Settings page, then click Next:

   *User Container:*
   Select the Identity Vault container where the users are added if they don’t already existing in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.

   *Group Container:*
   Select the Identity Vault container the groups are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.
9. Click Next.
10. On the Install GroupWise REST Base page, specify the name of the driver, then click Next.
11. On the Install GroupWise REST Base page, fill in the following fields, then click Next:

    *Authentication ID:*
    Specify the user ID used to authenticate to the GroupWise system. By default, it is the GroupWise Administrator user.

    *Connection Information:*
    Specify the IP address and the decimal port number (for example, IP Address:port) to connect to GroupWise. By default, it runs on port 9710 (Administration Service port). The Administration Service running on the GroupWise primary domain is used as the connection address in the driver configuration.

    *NOTE:*If you specify GroupWise server host name instead of IP address, ensure that Set Bind Exclusive setting is changed to false in the Message Transfer Agent of the GroupWise server. To do this, log in to Administration Service, change the setting and then restart the Administration Service.

    *Password:*
    Specify the admin user password to authenticate to GroupWise.

    *Always accept server certificate:*
    By default, this is set to No. Specify the values for the following parameters to use the keystore:

    * *Keystore path for SSL certificates:*
      Specify the full path to the keystore file containing the SSL certificates.
    * *Keystore Password:*
      Specify the password for accessing the keystore file containing the SSL certificates.

    For more information about setting up SSL connections, See [Section 6.0, Securing Driver Communication](secure-driver-communication.html).

    Select Yes if you want the driver to accept the GroupWise server's certificate for establishing SSL connection with the Identity Manager server. This avoids the need for manually maintaining a keystore.
12. On the Install GroupWise REST Base page, fill in the following field, then click Next:

    *Default Sync Destination GroupWise Post Office:*
    Specify the GroupWise post office name in dot format. The newly added Identity Vault objects are created in this GroupWise post office. For example: GWDomain.PostOffice. In earlier GroupWise drivers, the GroupWise post office name was specified in slash format.
13. Fill in the following fields for Remote Loader information:

    *Connect To Remote Loader:*
    Select Yes or No to determine if the driver will use the Remote Loader.

    If you select No, skip to [Step 17](create-driver-object-designer.html#brymnia). If you select Yes, provide the following information to complete the configuration of the Remote Loader, then click Next:

    *Host Name:*
    Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

    *Port:*
    Specify the port number where the Remote Loader is installed and is running for this driver. The default value is 8090.

    *KMO:*
    Specify the Key Name of the Key Material Object (KMO) that contains the keys and certificates the Remote Loader uses for an SSL connection. This parameter is only used when you use SSL for connections between the Remote Loader and the Identity Manager engine.

    *Other parameters:*
    Specify any other parameters required to connect to the Remote Loader. Any parameters specified must use a key-value pair format, as follows:

    ```
    paraName1=paraValue1 paraName2=paraValue2
    ```

    *Remote Loader Password:*
    Specify the Remote Loader’s password as defined in the Remote Loader. The Identity Manager server (or Remote Loader shim) requires this password to authenticate to the Remote Loader.

    *Driver Password:*
    Specify the driver object password that is defined in the Remote Loader service. The Remote Loader requires this password to authenticate to the Identity Manager server.
14. (Conditional) Provide the following fields on the Managed System Information page, then click Next:

    *Name:*
    Specify a descriptive name for this GroupWise system. The name is displayed in the reports.

    *Description:*
    Specify a brief description of this GroupWise system. The description is displayed in the reports.

    *Location:*
    Specify the physical location of this GroupWise system. The location is displayed in the reports.

    *Vendor:*
    Select NetIQ Corporation as the vendor of this system. The vendor information is displayed in the reports.

    *Version:*
    Specify the version of this GroupWise system. The version is displayed in the reports.

    *NOTE:*This page is only displayed if you installed the Managed System package.
15. (Conditional) Fill in the following fields on the Managed System Information page, then click Next:

    This page is displayed only if you selected to install the Data Collection and Account Tracking groups of packages.

    *Business Owner:*
    Select a user object in the Identity Vault that is the business owner of this GroupWise system. This can only be a user object, not a role, group, or container.

    *Application Owner:*
    Select a user object in the Identity Vault that is the application owner for this GroupWise system. This can only be a user object, not a role, group, or container.

    *NOTE:*This page is only displayed if you installed the Managed System package.
16. (Conditional) Fill in the following fields on the Managed System Information page, then click Next:

    This page is displayed only if you selected to install the Data Collection and Account Tracking groups of packages.

    *Classification:*
    Specify the classification for this GroupWise system in your environment. For example, Mission-Critical. If you select Other, you must specify a custom classification for the GroupWise system.This information is displayed in the reports.

    *Environment:*
    Specify the type of environment the GroupWise system provides. For example, Development, Test, or Production. If you select Other, you must specify a custom classification for the GroupWise system. This information is displayed in the reports.

    *Authentication IP Address:*
    Specify the IP address used to authenticate to the GroupWise system.

    *Authentication Port:*
    Specify the port used to authenticate to the GroupWise system.

    *Authentication ID:*
    Specify the user ID used to authenticate to the GroupWise system.

    *NOTE:*This page is only displayed if you installed the Managed System package.
17. (Conditional) Provide the following field on the Account Tracking Information page, then click Next:

    *Realm:*
    Specify the name of the realm, security domain, or namespace in which the account name is unique.

    *NOTE:*This page is only displayed if you installed the Account Tracking package.
18. Review the summary of tasks that will be completed to create the driver, then click Finish.

The driver is now created. To modify the configuration settings, proceed to the section [Configuring the Driver Object](create-driver-object-designer.html#bfveihb).

## 3.1.3 Configuring the Driver Object

After installing the driver packages, you can configure the driver to suit your environment. There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to review the [Driver Parameters](driver-configuration.html#b4m4h9a) located on the Driver Configuration page.

After completing the configuration tasks, continue with the next section, [Deploying the Driver](create-driver-object-designer.html#bfvehvc).

## 3.1.4 Deploying the Driver

After a driver object is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](create-driver-object-designer.html#bfvehvl); otherwise, specify the following information:

   *Host:*
   Specify the IP address or DNS name of the server hosting the Identity Vault.

   *Username:*
   Specify the DN of the user object used to authenticate to the Identity Vault.

   *Password:*
   Specify the user’s password.
4. Click OK.
5. Review the deployment summary, then click Deploy.
6. Read the successful message, then click OK.
7. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.

      For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see “Establishing a Security Equivalent User” in the [Identity Manager 4.0.2 Security Guide](https://www.netiq.com/documentation/idm402/idm_security/?page=/documentation/idm402/idm_security/data/front.html).
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat [Step 8.a](create-driver-object-designer.html#bfvehvr) and [Step 8.b](create-driver-object-designer.html#bfvehvs) for each object you want to exclude.
   4. Click OK.
9. Click OK.
10. Continue with the next section, [Associating Identity Vault with GroupWise System](create-driver-object-designer.html#b1d27cy6).

## 3.1.5 Associating Identity Vault with GroupWise System

You must associate Identity Vault with the GroupWise system.

1. In the GroupWise Administration console, click System > LDAP Servers, then click New Directory.

   ![](../graphics/groupwise_console_a.png)
2. In the General tab, fill in the following fields, then click Test Connection to verify that you have provided accurate information about Identity Manager server:

   1. *Name:*
      Specify the name of your Identity Vault (eDirectory tree).
   2. *Description:*
      Provide a description for eDirectory.
   3. *Type:*
      Select the directory type. In this case, it is eDirectory.
   4. *Address:*
      Enter the IP address of your eDirectory server (Your eDirectory server must be set to allow clear text in order to use port 389).
   5. *SSL Certificate:*
      This is an optional field. Use it if you want the GroupWise server to communicate with a backend server in SSL mode.
   6. *LDAP User:*
      Specify the admin user name.
   7. *LDAP User Password:*
      Specify the password for the admin user.
   8. *Test Connection:*
      Click this button to verify that you have provided accurate information about Identity Manager server.
   9. *Base DN:*
      Specify the container where the objects reside in Identity Vault. For example, o=data.
   10. *Sync Domain:*
       The GroupWise domains are populated in the drop-down list. Select the value that matches the domain name that you specified for the Default Sync Destination GroupWise Post Office parameter in [Step 12](create-driver-object-designer.html#b198c1zv).
   11. *Enable Synchronization:*
       Uncheck this option.
3. Click OK to complete the configuration.
4. Click Close to return to the main Administration console window.

## 3.1.6 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it will not do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Live > Start Driver.
