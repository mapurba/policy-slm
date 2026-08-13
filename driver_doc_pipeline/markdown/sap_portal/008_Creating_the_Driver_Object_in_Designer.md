# 3.1 Creating the Driver Object in Designer

The following sections provide steps for using Designer to create and configure a new SAP Portal driver.

* [Importing the Current Driver Packages](creating-new-identity-manager-sap-portal-driver-in-designer.html#importing-packages-for-identity-manager-sap-portal-driver)
* [Installing the Driver Packages](creating-new-identity-manager-sap-portal-driver-in-designer.html#installing-packages-for-identity-manager-sap-portal-driver)
* [Using Designer to Adjust the Driver Settings](creating-new-identity-manager-sap-portal-driver-in-designer.html#configuring-identity-manager-sap-portal-driver)
* [Using Designer to Deploy the Driver Object](creating-new-identity-manager-sap-portal-driver-in-designer.html#deploying-identity-manager-sap-portal-driver)
* [Using Designer to Start the Driver](creating-new-identity-manager-sap-portal-driver-in-designer.html#starting-identity-manager-sap-portal-driver)

*NOTE:*To create drivers, you now need to use the new package management features provided in Designer.

## 3.1.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer and can be updated often. You must have the most current version of the packages imported into the Package Catalog before you can create a new driver object.

To verify you have the most recent version of the driver packages imported into the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/package_import_a.png)
6. Select any SAP Portal driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the message indicating that the package imported.
8. After the current packages are imported, continue with [Installing the Driver Packages](creating-new-identity-manager-sap-portal-driver-in-designer.html#installing-packages-for-identity-manager-sap-portal-driver).

## 3.1.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select SAP Portal Base, then click Next.
4. Select the optional features to install for the SAP Portal driver. All options are selected by default. The options are:

   *Entitlements:*
   These packages contain the policies and entitlements required to enable the driver for account creation and management with entitlements.

   *Process File Logging:*
   These packages contain the policies for creating a daily, rolling log file of SAP Business Operations.

   *Data Collection:*
   These packages contain the policies that enable the driver to collect data for reports. If you are using the Identity Reporting Module, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

   *Account Tracking:*
   This group of packages contain the policies that enables account tracking information for reports. If you are using the Identity Reporting Module, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

   Account Tracking feature was introduced with NetIQ Compliance Management Platform. The Compliance Management Platform helps you mitigate risk, simplify business governance, and ensures compliance throughout the enterprise. The platform enables you to provision users based on how you do business, secure both Web and Client applications by granting access to users based upon provisioning policy, and monitor and validate user and system activity in real time with automated, policy-based corrective actions for non-compliant activities. For more information, see [NetIQ Compliance Management Platform product page](http://www.novell.com/products/compliancemanagementplatform/).
5. After selecting the packages that you want, click Next.
6. (Conditional) If there are package dependencies for the packages you selected to install, you must install these dependencies to install the selected packages. Click OK to install the package dependencies.
7. (Conditional) Fill in the following fields on the Common Settings page, then click Next:

   The Common Settings page is displayed only if the Common Settings package is installed as a dependency.

   *User Container:*
   Select the Identity Vault container where the users are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.

   *Group Container:*
   Select the Identity Vault container where the groups are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.
8. On the Driver Information page, specify a name for the driver, then click Next.
9. Fill in the following fields to configure the driver, then click Next:

   *URL of the remote SPML Provisioning Service Point:*
   Specify the URL of the remote SAP Portal SPML Provisioning Service Point.

   For example: http://my.sap.com:50000/spml/spmlservice

   *Authentication ID:*
   Specify the authentication ID for the remote SAP Portal SPML Provisioning Service Point. For more information, see [Creating an Administrative User Account for the Driver](creating-admin-user-account-for-identity-manager-sap-portal-driver.html).

   *Authentication Password:*
   Specify the password for the Authentication ID, then reenter the password for verification.
10. Fill in the following fields for Remote Loader information:

    *Connect To Remote Loader:*
    Select Yes or No to determine if the driver will use the Remote Loader. For more information, see "[Configuring the Remote Loader and Drivers](../../../identity-manager-48/driver_admin/data/b18xta1v.html#b18xta1v)" in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

    If you select No, skip to [Step 11](creating-new-identity-manager-sap-portal-driver-in-designer.html#brtiud2). If you select Yes, use the following information to complete the configuration of the Remote Loader:

    *Host Name:*
    Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

    *Port:*
    Specify the port number for this driver. Each driver connects to the Remote Loader on a separate port. The default value is 8090.

    *Remote Loader Password:*
    Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

    *Driver Password:*
    Specify a password for the driver to authenticate to the Identity Manager server. It must be the same password that is specified as the driver object password on the Remote Loader.
11. (Conditional) Fill in the following fields on the Process Logging page to create the daily, rolling log file of SAP Business Operations, then click Next:

    *Show Process Logging Options:*
    Select show to display the options to configure the rolling log file of SAP Business Operations.

    *Enable process logging:*
    Select true to enable process logging, then fill in the following fields:

    * *Daily log file:*
      Select true to create the daily log file with the format of <YYYYmmDD>-<driver-name>-<drv.proclog.logfile>.
    * *Log file name:*
      Specify the process log filename.
    * *Log file directory:*
      Specify the directory where the log file is created.
12. (Conditional) Fill in the following fields on the Managed System Information page, then click Next:

    This page is displayed only if you selected to install the Data Collection and Account Tracking packages.

    *Name:*
    Specify a descriptive name for this SAP Portal system. The name is displayed in the reports.

    *Description:*
    Specify a brief description of this SAP Portal system. The description is displayed in the reports.

    *Location:*
    Specify the physical location of this SAP Portal system. The location is displayed in the reports.

    *Vendor:*
    Select SAP as the vendor of this system. The vendor information is displayed in the reports.

    *Version:*
    Specify the version of this SAP Portal system. The version is displayed in the reports.
13. (Conditional) Fill in the following fields to define the classification of the SAP Portal System, then click Next:

    This page is displayed only if you selected to install the Dat Collection and Account Tracking packages.

    *Classification:*
    Select the classification of the SAP Portal system. This information is displayed in the reports. The options are:

    * Mission-Critical
    * Vital
    * Not-Critical
    * Other

      If you select Other, you must specify a custom classification for the SAP system.

    *Environment:*
    Select the type of environment the SAP Portal system provides. The options are:

    * Development
    * Test
    * Staging
    * Production
    * Other

      If you select Other, you must specify a custom classification for the SAP system.
14. Review the summary of tasks that will be completed to create the driver, then click Finish.
15. If this basic driver configuration fits your needs, continue with [Using Designer to Deploy the Driver Object](creating-new-identity-manager-sap-portal-driver-in-designer.html#deploying-identity-manager-sap-portal-driver).

    or

    If you need to customize the driver settings, continue with [Using Designer to Adjust the Driver Settings](creating-new-identity-manager-sap-portal-driver-in-designer.html#configuring-identity-manager-sap-portal-driver).

## 3.1.3 Using Designer to Adjust the Driver Settings

If you need to do additional configuration for the driver, you must access the properties page of the driver. If you do not have the Driver Properties page displayed:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Properties.

   This opens the properties page for the driver. Use the information in [Section A.0, Driver Properties](identity-manager-sap-portal-driver-properties.html) to adjust the configuration.
3. After you have customized the driver for you environment, you must deploy the driver to the Identity Vault. Proceed to [Using Designer to Deploy the Driver Object](creating-new-identity-manager-sap-portal-driver-in-designer.html#deploying-identity-manager-sap-portal-driver).

## 3.1.4 Using Designer to Deploy the Driver Object

After the driver object is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](creating-new-identity-manager-sap-portal-driver-in-designer.html#bfuwdvx); otherwise, specify the following information to authenticate:

   *Host:*
   Specify the IP address or DNS name of the server hosting the Identity Vault.

   *Username:*
   Specify the DN of the user object used to authenticate to the Identity Vault.

   *Password:*
   Specify the user’s password.
4. Click OK.
5. Read through the deployment summary, then click Deploy.
6. Read the message indicating the success, then click OK.
7. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.

      For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see [Establishing a Security Equivalent User](../../../identity-manager-48/security/data/establishing-security-equivalent-user-in-identity-manager.html#establishing-security-equivalent-user-in-identity-manager) in the [NetIQ Identity Manager Security Guide](../../../identity-manager-48/security/data/identity-manager-security-guide.html#identity-manager-security-guide).
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude, then click OK.
   2. Repeat [Step 8.a](creating-new-identity-manager-sap-portal-driver-in-designer.html#bfuwk84) for each object you want to exclude.
   3. Click OK.
9. Click OK.
10. Continue with [Using Designer to Start the Driver](creating-new-identity-manager-sap-portal-driver-in-designer.html#starting-identity-manager-sap-portal-driver).

## 3.1.5 Using Designer to Start the Driver

When a driver is created, it is stopped by default. You must start the driver before events are processed.

To start the driver after the driver is deployed:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Start Driver.

For information about management tasks with the driver, see [Section 8.0, Managing the Driver](managing-identity-manager-sap-portal-driver.html).
