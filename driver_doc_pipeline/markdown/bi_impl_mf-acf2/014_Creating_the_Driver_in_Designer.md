# 3.5 Creating the Driver in Designer

The ACF2 Driver supports Designer 4 Package features, which allows you to create a driver by selecting which packages to install. After you create and configure the driver, you need to deploy it to the Identity Vault and start it.

Topics include

* [Importing the Current Driver Packages](b3xdkfa.html#b135fu1h)
* [Installing the Driver Packages](b3xdkfa.html#b135fu1i)
* [Configuring the Driver](b3xdkfa.html#b135fu1j)
* [Deploying the Driver](b3xdkfa.html#b135fu1k)
* [Starting the Driver](b3xdkfa.html#b135fu1l)
* [Creating the Driver in iManager](b3xdkfa.html#b1byc4e4)

## 3.5.1 Importing the Current Driver Packages

Driver packages can be updated at any time and are stored in the Package Catalog. Packages are initially imported into the Package Catalog when you create a project, import a project, or convert a project. It is important to verify you have the latest packages imported into the Package Catalog before you install the driver.

To verify you have the latest packages imported into the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK if there are no package updates.

   or

   Click OK to import the package updates.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/bi_acf2_import_package.png)
6. Select the ACF2 packages.

   or

   Click Select All to import all of the packages displayed, then click OK.

   *NOTE:*By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue to the next section, [Installing the Driver Packages](b3xdkfa.html#b135fu1i).

## 3.5.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then select New > Driver.
3. Select ACF2 Base from the list of base packages, then click Next.
4. Select the optional features to install for the ACF2 driver. The options are:

   *NOTE:*Publications referenced in the following option descriptions can be accessed at the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

   *Default Configuration:*
   This package contains the default configuration information for the ACF2 driver. Always leave this option selected.

   *Entitlements:*
   This package contains configuration information for synchronizing ACF2 accounts and policies that enable account creation and auditing for the ACF2 driver. To enable account creation and auditing, verify that this option is selected. For more information, see the Identity Manager 4.8 Entitlements Guide.

   *Password Synchronization:*
   This package contains the policies that enable the ACF2 driver to synchronize passwords. To synchronize passwords, verify that this option is selected. For more information, see the Identity Manager 4.8 Password Management Guide.

   *Data Collection:*
   This package contains the policies that enable the driver to collect data for reports. If you are using the Identity Reporting Module, verify that this option is selected. For more information, see the Identity Reporting Module Guide.

   *Account Tracking:*
   This package contains the policies that enable you to track accounts for reports. If you are using the Identity Reporting Module, verify that this option is selected. For more information, see the Identity Reporting Module Guide.
5. After selecting the optional packages, click Next.
6. (Conditional) If the packages you selected to install have package dependencies, you must install them to install the selected package. Click OK to install the package dependencies listed.
7. (Conditional) If more than one type of package dependency must be installed, you are presented with these packages separately. Continue to click OK to install any additional package dependencies.
8. (Conditional) The Common Settings page is only displayed if the Common Settings package is installed as a dependency. On the Install Common Settings page, fill in the following fields:

   *User Container:*
   Select the Identity Vault container where ACF2 users will be added if they don’t already exist in the vault. This value becomes the default for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.

   *Group Container:*
   Since the ACF2 driver does not synchronize Group objects, this setting can be ignored.
9. (Conditional) If not already configured, fill in the following fields on the Common Settings Advanced Edition page, then click Next:

   User Application Provisioning Services URL: specify the User Application Identity Manager Provisioning URL.

   User Application Provisioning Services Administrator: Specify the DN of the User Application Administrator user. This user should have the rights for creating and assigning resources. For more information, see “Setting Up Administrative Accounts” in the NetIQ Identity Manager 4.8 Common Driver Administration Guide.
10. On the Install ACF2 page, fill in the following field:

    *Driver Name:*
    Specify a name for the driver that is unique within the driver set.
11. (Conditional) On the Driver Parameters page, review the default Subscriber and Publisher Options. Edit, if necessary, and click Next.
12. On the Install ACF2 Base page, fill in the following fields to connect to the Remote Loader and click Next:

    Connect to Remote Loader: By default, the driver is configured to connect using the Remote Loader. You must select Yes for this option.

    Host Name: Specify the port number where the Remote Loader is installed and is running for this driver. The default port number is 8090.

    Port: Specify the Remote Loader’s password as defined on the Remote Loader. The Metadirectory server (or Remote Loader shim) requires this password to authenticate to the Remote Loader.

    Remote Password: Specify the Remote Loader’s password as defined on the Remote Loader. The Metadirectory server (or Remote Loader shim) requires this password to authenticate to the Remote Loader.

    Driver Password: Specify the driver object password that is defined in the Remote Loader service. The Remote Loader requires this password to authenticate to the Metadirectory server.
13. (Conditional) On the Account Tracking page, review the default values. Edit, if necessary, and click Next.
14. (Conditional) On the Entitlements Name to CSV File Mappings page, click the Add Name to File Mapping icon to populate the page with the entitlement configuration options. Identity Manager uses the CSV file to map ACF2 entitlements into corresponding resources in the Identity Manager catalog.

    *NOTE:*This page is displayed only if you installed the Entitlements package.

    The information that you specify in this page is used for creating the permission catalog. Fill in the following fields, then click Next:

    Entitlement Name: Specify a descriptive name for the entitlement to map it to the CSV file that contains the ACF2 entitlement details.

    Entitlement Name is the name of the entitlement. This parameter corresponds to the Entitlement Assignment Attribute in ACF2. For example, you could define an entitlement called ParkingPass.

    Entitlement Assignment Attribute: Specify a descriptive name for the assignment attribute for an entitlement.

    Entitlement Assignment Attribute holds the entitlement values in ACF2. For example, you could have an attribute called Parking.

    You must add this parameter to Field Names in the Driver Parameters page or modify it in driver settings after creating the driver.

    CSV File: Specify the location of the CSV file. This file must be located on the same server as the driver. This file contains the values for the application entitlements.

    Multi-valued?: Set the value of this parameter to True if you want to assign resources and entitlements multiple times with different values to the same user. Otherwise, set it to False.
15. (Conditional) On the Entitlements page, review the default values. Edit, if necessary, and click Next.
16. (Conditional) On the General Information page, fill in the following fields to define your ACF2 system, then click Next:

    Name: Specify a descriptive name for this ACF2 system. The name is displayed in reports.

    Description: Specify a brief description for this ACF2 system. The description is displayed in reports.

    Location: Specify the physical location for this ACF2 system. The location is displayed in reports.

    Vendor: Leave CA as the vendor of ACF2. This information is displayed in reports.

    Version: Specify the version of this ACF2 system. The version is displayed in reports.

    *NOTE:*This page is only displayed if you installed the Managed System package.
17. (Conditional) This page is displayed only if you selected to install the Managed System Information packages. On the Install ACF2 Managed System Information page, fill in the following fields, then click Next.

    Classification: Select the classification of the ACF2 system. This information is displayed in the reports. Options include:

    * Mission-Critical
    * Vital
    * Not-Critical
    * Other

    If you select Other, you must specify a custom classification for the ACF2 system.

    Environment: Select the type of environment the ACF2 system provides. Options include:

    * Development
    * Test
    * Staging
    * Production
    * Other

    If you select Other, you must specify a custom classification for the ACF2 system.
18. (Conditional) On the System Ownership page, fill in the following fields to define the ownership of the ACF2 system, then click Next:

    Business Owner: Select a user object in the Identity Vault that is the business owner of the ACF2 system. This can only be a user object, not a role, group, or container.

    *Application Owner:*
    Select a user object in the Identity Vault that is the application owner of the ACF2 system. This can only be a user object, not a role, group, or container.
19. Review the summary of tasks that will be completed to create the driver, then click Finish.

The driver is created. You can modify the configuration settings by continuing with the next section, [Configuring the Driver](b3xdkfa.html#b135fu1j). If you don’t need to configure the driver, skip ahead to [Deploying the Driver](b3xdkfa.html#b135fu1k).

## 3.5.3 Configuring the Driver

There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to review the Driver Parameters located on the Driver Configuration page and the Global Configuration Values. These settings must be configured properly for the driver to start and function correctly.

To access the Driver Properties page:

1. Open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon.png) or the driver line, then select Properties.
3. Modify the driver settings as necessary.

   *IMPORTANT:*In addition to the driver settings, you should review the set of default policies and rules provided by the basic driver configuration. Although these policies and rules are suitable for synchronizing with ACF2\*, your synchronization requirements for the driver might differ from the default policies. If this is the case, you need to change them to carry out the policies you want. The default policies and rules are discussed in [Configuration Overview](b3wx9up.html).
4. Continue with the next section, [Deploying the Driver](b3xdkfa.html#b135fu1k).

## 3.5.4 Deploying the Driver

After a driver is created in Designer, it must be deployed into the Identity Vault:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon.png) or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](b3xdkfa.html#b135vhlt); otherwise, specify the following information:

   *Host:*
   Specify the IP address or DNS name of the server hosting the Identity Vault.

   *Username:*
   Specify the DN of the user object used to authenticate to the Identity Vault.

   *Password:*
   Specify the user’s password.
4. Click OK.
5. Read through the deployment summary, then click Deploy.
6. Read the successful message, then click OK.
7. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user. Whatever rights that the driver needs to have on the server, the DriversUser object must have the same security rights:

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization:

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat Step [Step 8.a](b3xdkfa.html#b135vkq3) and Step [Step 8.b](b3xdkfa.html#b135vkq4) for each object you want to exclude.
   4. Click OK.
9. Click OK.

## 3.5.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon.png) or the driver line, then select Live > Start Driver.

## 3.5.6 Creating the Driver in iManager

Drivers are created with packages, and iManager does not support packages. In order to create or modify drivers, you must use Designer. See [Creating the Driver in Designer](b3xdkfa.html).
