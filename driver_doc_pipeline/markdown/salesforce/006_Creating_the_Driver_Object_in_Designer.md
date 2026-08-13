# 3.1 Creating the Driver Object in Designer

You create a Salesforce.com driver object by installing the driver packages and then modifying the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](create-driver-object-designer.html#bl582ar)
* [Installing the Driver Packages](create-driver-object-designer.html#bfvehvb)
* [Configuring the Driver Object](create-driver-object-designer.html#bfveihb)
* [Deploying the Driver Object](create-driver-object-designer.html#bfvehvc)
* [Starting the Driver](create-driver-object-designer.html#bfvehvw)

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
6. Select any Salesforce driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](create-driver-object-designer.html#bfvehvb).

## 3.1.2 Installing the Driver Packages

1. In Designer, open your project.
2. From the Palette, drag-and-drop the Salesforce.com driver to the desired driver set in the Modeler.

   The Salesforce.com driver is under the Enterprise category in the Palette.
3. Select Salesforce Base, then click Next.
4. Select the optional features to install for the Salesforce.com driver, then click Next.

   The options are:

   All options are selected by default. The options are:

   *Default Configuration:*
   These packages contain the default configuration information for the Salesforce.com driver. Always leave this option selected.

   *Password Generation and Synchronization:*
   This package contains the policies that allow the Salesforce.com driver to synchronize passwords to the Identity Vault. By default, it is not selected. For more information, see the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

   *Entitlements Support:*
   These packages contain the policies and entitlements required to enable the driver for account creation and management with entitlements. For more information, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

   *Data Collection:*
   These packages contain the policies that enable the driver to collect data for reports. If you are using Identity Reporting, verify that this option is selected. For more information, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

   *Account Tracking:*
   These packages contain the policies that enables account tracking information for reports. If you are using Identity Reporting, verify that this option is selected. For more information, see the [NetIQ Identity Reporting: User’s Guide to Running Reports](../../../identity-manager-48/report_descriptions/data/bookinfo.html#bookinfo).
5. (Conditional) If there are package dependencies for the packages you selected to install, you must install them to install the selected package. Click OK to install the package dependencies listed.
6. (Conditional) Fill in the following fields on the Common Settings page, then click Next:

   The Common Settings page is displayed only if the Common Settings package is not installed already.

   *User Container:*
   Select the Identity Vault container where the users are added if they don’t already existing in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.
7. On the Install Salesforce Base page, specify a name for the driver that is unique within the driver set, then click Next.
8. On the new Install Salesforce.com Base page, fill in the following fields, then click Next:

   *Salesforce.com Login URL:*
   Specify the login URL of Salesforce.com.

   *Salesforce.com Login ID:*
   Specify the e-mail address used to login to Salesforce.com.

   Ensure that you create a unique administrator user to be solely used by the Salesforce.com driver for authentication and specify that user in this parameter. If you specify the same user with which you login and administer Salesforce.com, the driver ignores changes on the Publisher channel (loopback detection).

   *Salesforce.com Login Password:*
   Specify the authentication password to login to Salesforce.com.

   *Salesforce.com Security Token:*
   Specify the security token for login account at Salesforce.com.
9. Fill in the following fields for the Remote Loader information, then click Next:

   *Connect To Remote Loader:*
   Select Yes or No to determine if the driver will use the Remote Loader. For more information, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_windows/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

   If you select No, skip to [Step 12](create-driver-object-designer.html#brd1vuu). If you select Yes, use the following information to complete the configuration of the Remote Loader, then click Next:

   *Host Name:*
   Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

   *Port:*
   Specify the port number for this driver. Each driver connects to the Remote Loader on a separate port. The default value is 8090.

   *Remote Loader Password:*
   Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

   *Driver Password:*
   Specify a password for the driver to authenticate to the Identity Manager server. It must be the same password that is specified as the Driver Object Password on the Remote Loader.
10. (Conditional) On the Install Salesforce Account Tracking page, fill in the following fields for Account Tracking, then click Next:

    *Realm:*
    Specify the name of the realm, security domain, or namespace in which the account name is unique. You must set the Realm to the Salesforce.com Domain Name.
11. (Conditional) On the Install Salesforce Managed System Information page, fill in the following fields to define the ownership of Salesforce.com, then click Next:

    *General Information*

    * Name: Specify a descriptive name for the managed system.
    * Description: Specify a brief description of the managed system.
    * Location: Specify the physical location of the managed system.
    * *Vendor:*
      Specify Salesforce.com as the vendor of the managed system.
    * Version: Specify the version of the managed system.

    *System Ownership*

    * Business Owner: Select a user object in the Identity Vault that is the business owner of Salesforce.com. This can only be a user object, not a role, group, or container.
    * Application Owner: Select a user object in the Identity Vault that is the application owner of Salesforce.com. This can only be a user object, not a role, group, or container.

      This page is only displayed if you selected to install the Data Collection packages and the Account Tracking packages.

    *System Classification*

    * Classification: Select the classification of the Salesforce.com. This information is displayed in the reports. The options are as follows:

      + Mission-Critical
      + Vital
      + Not-Critical
      + Other

        If you select Other, you must specify a custom classification for the Salesforce.com.

    * Environment: Select the type of environment the Salesforce.com provides. The options are as follows:

      + Development
      + Test
      + Staging
      + Production
      + Other

        If you select Other, you must specify a custom environment for the Salesforce.com.
12. Review the summary of tasks that will be completed to create the driver, then click Finish.
13. After you have installed the driver, you can change the configuration for your environment. Proceed to [Configuring the Driver Object](create-driver-object-designer.html#bfveihb).

    or

    If you do not need to configure the driver, continue with [Deploying the Driver Object](create-driver-object-designer.html#bfvehvc).

## 3.1.3 Configuring the Driver Object

There are many settings that can help you customize and optimize the driver. You should complete the following tasks to configure the driver:

* *Configure the driver parameters:*
  There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to review the [Driver Parameters](driver-configuration.html#b4m4h9a) located on the Driver Configuration page. The Driver Parameters let you configure the Salesforce login information and security credentials, and other parameters associated with the Publisher channel.
* *Customize the driver policies and filter:*
  The driver policies and filter control data flow between the Identity Vault and the application. You should ensure that the policies and filters reflect your business needs. For instructions, see [Section 4.0, Schema Mapping](schema-mapping.html).

If you do not have the Driver Properties page displayed in Designer:

1. Open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Properties.
3. Make any desired changes, then click OK to save the changes.
4. After the driver is create in Designer, it must be deployed to the Identity Vault. Proceed to [Deploying the Driver Object](create-driver-object-designer.html#bfvehvc) to deploy the driver.

## 3.1.4 Deploying the Driver Object

After the driver object is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](create-driver-object-designer.html#bfvehvl); otherwise, specify the following information:

   * *Host:*
     Specify the IP address or DNS name of the server hosting the Identity Vault.
   * *Username:*
     Specify the DN of the user object used to authenticate to the Identity Vault.
   * *Password:*
     Specify the user’s password.
4. Click OK.
5. Read through the deployment summary, then click Deploy.
6. Read the successful message, then click OK.
7. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.

      For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see [Establishing a Security Equivalent User](../../../identity-manager-48/security/data/establishing-security-equivalent-user-in-identity-manager.html#establishing-security-equivalent-user-in-identity-manager) in the [NetIQ Identity Manager Security Guide](../../../identity-manager-48/security/data/identity-manager-security-guide.html#identity-manager-security-guide).
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat [Step 8.a](create-driver-object-designer.html#bfvehvr) and [Step 8.b](create-driver-object-designer.html#bfvehvs) for each object you want to exclude.
   4. Click OK.
9. Click OK.

## 3.1.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Start Driver.

   The driver cannot initialize completely unless it successfully connects to the .NET Remote Loader and loads the Salesforce.com driver shim.

For information about management tasks for the driver, see [Section 7.0, Managing the Driver](manage-driver.html).
