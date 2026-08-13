# 5.1 Creating the Driver Object in Designer

You create the JDBC driver by installing the driver packages and then modifying the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwsf8)
* [Installing the Driver Packages](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwsfi)
* [Configuring the Driver Object](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwsgy)
* [Deploying the Driver Object](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwsh3)
* [Starting the Driver Object](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwshn)

*NOTE:*To create drivers, you need to use the new package management features provided in Designer.

## 5.1.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver object, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer. You can upgrade any package that is installed if there is a newer version of the package available. For more information on upgrading packages, see "[Upgrading Installed Packages](../../../identity-manager-48/designer_admin/data/packman.html#packmanupgrade)" in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).

Before creating a driver object in Designer, you need to verify that you have all the required packages already imported in the Package Catalog of Designer. Designer prompts you for importing the required packages when it creates the driver object.

You can create packages based on the schema for your environment, keeping in mind the data synchronization model (direct/indirect) and its dependent packages.

To verify you have the most recent version of the driver packages in the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/package_import_a.png)

   You can download the new packages from the [Designer Auto-update site](http://cdn.novell.com/cached/designer/packages/idm/updatesite1_0_0/).
6. Select any JDBC driver packages.

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwsfi).

## 5.1.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select an appropriate JDBC Base Database Package, such as Oracle Base, then click Next.
4. Select the optional features to install for the JDBC driver, then click Next.

   All options are selected by default. The options are:

   *Entitlements Support:*
   These packages contain the policies that provision the user accounts on the connected database. For more information, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

   *Data Collection:*
   These packages contain the policies that enable the driver to collect data for reports. If you are using Identity Reporting, ensure that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

   *Account Tracking:*
   These packages contain the policies that enable account tracking information for reports. If you are using Identity Reporting, ensure that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

   *Synchronization Mode:*
   These packages contain the GCVs and sample policies. If you choose the direct/indirect synchronization mode, ensure that you don’t change this setting on the driver creation and configuration pages.

   By default, the Show only Applicable packages versions option is selected.

   *IMPORTANT:*The JDBC packages provide examples of the core functions of the JDBC driver. These examples help you customize the driver for your environment. You can add new policies and settings to the driver to meet your business requirements. The final implementation can be packaged and deployed in Identity Manager.
5. (Conditional) If there are package dependencies for the packages you selected to install for this driver, you must install them to install the selected package. Click OK to install the package dependency listed.
6. (Conditional) If more than one type of package dependency must be installed, you are presented with separate configuration pages for each package. Continue to click OK to install any additional package dependencies.
7. (Conditional) The Common Settings page is displayed only if the Common Settings package is installed as a dependency. On the Install Common Settings page, specify the common settings for User and Group containers:

   *User Container:*
   Select the Identity Vault container where the user accounts will be added in the Identity Vault. This value becomes the default for all drivers in the driver set.

   *Group Container:*
   Select the Identity Vault container where the groups will be added in the Identity Vault. This value becomes the default for all drivers in the driver set.
8. Click Next.

   When all dependencies are installed, the components must be configured.
9. On the Driver Information page, specify a name for the driver that is unique within the driver set, then click Next.
10. On the Application Authentication page, fill in the following information for the connected database:

    *Version:*
    Specify the version of the connected database.

    *Synchronization Model:*
    Specify the mode of data synchronization based on the selected package.

    *Data Flow:*
    Specify whether the authoritative source of data is the database, Identity Manager, or bidirectional.

    *IMPORTANT:*Ensure that you don’t change the setting for Synchronization Model and Data Flow options that you selected earlier in the Package Configuration Wizard.

    *JDBC Implementation:*
    Specify the database connection details.

    *Connection Information:*
    Specify the database information for the driver to use to connect to the database, such as the IP address, port, and type of the database.

    If the database type is selected as SID, you need to enter the Oracle SID value. If the database type is selected as CDB, you need to enter the Oracle Service Name.

    *Authentication ID:*
    Specify the authentication ID for the connected database.

    *Password:*
    Specify the password for the driver to connect to the database.

    For more information, see [JDBC Driver Settings](modify-jdbc-driver-settings.html).
11. Click Next.
12. Fill in the following fields for Remote Loader information:

    *Connect To Remote Loader:*
    Select Yes or No to determine if the driver will use the Remote Loader. For more information, see “Configuring Identity Manager Drivers to Work with the Remote Loader” in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

    If you select No, skip to [Step 13](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwsg9). If you select Yes, use the following information to complete the configuration of the Remote Loader:

    *Host Name:*
    Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

    *Port (Connection):*
    Specify the port number for this driver object. Each driver object connects to the Remote Loader on a separate port. The default value is 8090.

    *Remote Loader Password:*
    Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

    *Driver Password:*
    Specify a password for the driver object to authenticate to the Identity Manager server. It must be the same password that is specified as the Driver Object password on the Remote Loader.
13. Click Next.
14. (Conditional) This page is displayed only if you selected to install the Data Collection and Account Tracking groups of packages. On the JDBC Managed System Information page, fill in the following fields to define your connected database application:

    *Name:*
    Specify a descriptive name for the connected database application. The name is displayed in reports.

    *Description:*
    Specify a brief description for the connected database application. The description is displayed in reports.

    *Location:*
    Specify the physical location of the connected database application. The location is displayed in reports.

    *Vendor:*
    Specify the vendor of the connected database application. This information is displayed in reports.

    *Version:*
    Specify the version of the connected database application. The version is displayed in reports.
15. Click Next.
16. (Conditional) This page is displayed only if you selected to install the Managed System packages and the Account Tracking packages. On the Install JDBC Managed System Information page, fill in the following fields to define the classification of the connected database application:

    *Classification:*
    Select the classification of the connected database application. This information is displayed in the reports. Your options are:

    * Mission-Critical
    * Vital
    * Not-Critical
    * Other

      If you select Other, you must specify a custom classification for the JDBC system.

    *Environment:*
    Select the type of environment the connected database application provides. The options are:

    * Development
    * Test
    * Staging
    * Production
    * Other

      If you select Other, you must specify a custom classification for the database application.
17. Click Next.
18. (Conditional) This page is displayed only if you selected to install the Data Collection and Account Tracking groups of packages. Fill in the following fields to define the ownership of the connected database application:

    *Business Owner:*
    Select a user object in the Identity Vault that is the business owner of the database application. This can only be a user object, not a role, group, or container.

    *Application Owner:*
    Select a user object in the Identity Vault that is the application owner of the database application. This can only be a user object, not a role, group, or container.
19. Click Next.
20. On the Entitlements Information page, specify a name for the Account Entitlement Value field, then click Next.
21. (Conditional) This page is displayed only if you selected to install the Account Tracking groups of packages. On the Account Tracking page, fill in the following fields:

    *Connected Database:*
    Specify the connected database application.

    *Synchronization Model:*
    Specify the mode of data synchronization.

    *NOTE:*Ensure that you don’t change the setting that you selected earlier in the Package Configuration Wizard. If you change it after installing the package in a driver object, make sure that you change the SyncModel in the Publication Mode GCV.

    *Object Class:*
    This field is populated based on your selection in the Synchronization Model. Specify the table or view in the connected database for which account tracking is enabled. By default, the value is usr.

    *Realm:*
    Specify the name of the realm that uniquely identifies the location of user accounts in the connected database. For example, mysql.indirect.usr, where MySQL is the database name with the indirect data synchronization model, and user is the table or view in the connected database for which account tracking is enabled.
22. Click Next.
23. Review the summary of tasks that will be completed to create the driver, then click Finish.
24. After you have installed the driver object, you must change the configuration for your environment. Proceed to [Configuring the Driver Object](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwsgy).

## 5.1.3 Configuring the Driver Object

After importing the packages and creating the driver object, you need to configure the driver to make it operational. There are many settings that can help you customize and optimize the driver. Although it is important for you to understand all of the settings, your first priority should be to configure the driver parameters located on the Driver Configuration page. For information about the driver parameters, see [Section 6.0, Configuring the JDBC Driver](configure-jdbc-driver.html). After completing the configuration tasks, continue with the next section, [Deploying the Driver Object](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwsh3).

*NOTE:*If the connected system is MS SQL Server database and if you have chosen a direct Synchronization Model option, ensure that you change the Key-Gen-Method option to Subscriber Generated in the Subscriber channel.

## 5.1.4 Deploying the Driver Object

After the driver object is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwshc); otherwise, specify the following information:

   *Host:*
   Specify the IP address or DNS name of the server hosting the Identity Vault.

   *Username:*
   Specify the DN of the user object used to authenticate to the Identity Vault.

   *Password:*
   Specify the user’s password.
4. Click OK.
5. Read the deployment summary, then click Deploy.
6. Read the successful message, then click OK.
7. Click Define Security Equivalence to assign rights to the driver object:

   The driver object requires rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user. For receiving events from the Identity Vault, ensure that driver object’s Security Equals DN has the following rights in the Identity Vault:

   *Entry Rights:*
   The rights to create entries in the Identity Vault.

   *Attributes Rights:*
   The rights to modify the attributes in the Identity Vault.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.

      For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see "[Establishing a Security Equivalent User](../../../identity-manager-48/security/data/establishing-security-equivalent-user-in-identity-manager.html#establishing-security-equivalent-user-in-identity-manager)" in the [NetIQ Identity Manager Security Guide](../../../identity-manager-48/security/data/identity-manager-security-guide.html#identity-manager-security-guide).
8. Click Exclude Administrative Roles to exclude users that should not be synchronized:

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat [Step 8.a](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwshi) and [Step 8.b](how-to-create-a-driver-object-using-designer-for-jdbc-driver.html#bxcwshj) for each object you want to exclude.
   4. Click OK.
9. Click OK.

## 5.1.5 Starting the Driver Object

When a driver is created, it is stopped by default. To make the driver work, you must start the driver. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs. You can use Identity Console or dxevent commands to start the driver.

To start the driver:

1. If you are using the Remote Loader with the driver, make sure the Remote Loader driver instance is running.
2. In Designer, open your project.
3. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Start Driver.
4. Continue with [Activating the Driver](how-to-activate-jdbc-driver.html).
