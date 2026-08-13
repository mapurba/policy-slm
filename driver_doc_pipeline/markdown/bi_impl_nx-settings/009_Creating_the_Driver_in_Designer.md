# 3.4 Creating the Driver in Designer

The Linux and Unix Settings Driver supports Designer 4 Package features, which allows you to create a driver by selecting which packages to install. After you create and configure the driver, you need to deploy it to the Identity Vault and start it.

Topics in this section include

* [Importing the Current Driver Packages](b1byr9qs.html#b1bxqdg4)
* [Installing the Driver Packages](b1byr9qs.html#b1bxqp8a)
* [Configuring the Driver](b1byr9qs.html#b1bxrh8d)
* [Deploying the Driver](b1byr9qs.html#b1bxrmiy)
* [Starting the Driver](b1byr9qs.html#b1byalib)
* [Creating the Driver in iManager](b1byr9qs.html#b1byat6m)

## 3.4.1 Importing the Current Driver Packages

Driver packages can be updated at any time and are stored in the Package Catalog. Packages are initially imported into the Package Catalog when you create a project, import a project, or convert a project. It is important to verify you have the latest packages imported into the Package Catalog before you install the driver.

To verify you have the latest packages imported into the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK if there are no package updates

   or

   Click OK to import the package updates.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   *Figure 3-1*  Import Package

   ![](../graphics/racf_import_package.png)
6. Select the Linux and Unix Settings Packages

   or

   Click Select All to import all of the packages displayed, then click OK.

   *NOTE:*By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue to the next section, [Installing the Driver Packages](b1byr9qs.html#b1bxqp8a).

## 3.4.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then select New > Driver.
3. Select Linux and Unix Settings Base from the list of base packages, then click Next.
4. Select the optional features to install for the Linux and Unix Settings driver. The options are:

   Linux and Unix Settings Posix: This option contains the policies needed for Posix Account and Group attributes. This option is mandatory.

   Optional Configuration: Linux and Unix Settings Posix: This option provides policies necessary for OES, LUM and Samba auto-assigned attributes.

   Entitlements: This package contains the policies needed for implementing Entitlements.
5. After selecting the optional packages, click Next.
6. (Conditional) If the packages you selected to install have package dependencies, you must also install them to install the selected package. Click OK to install the listed package dependencies.
7. (Conditional) If more than one type of package dependency must be installed, you are presented with these packages separately. Continue to click OK to install any additional package dependencies.
8. (Conditional) The Common Settings page is displayed only if the Common Settings package is installed as a dependency. On the Install Common Settings page, fill in the following fields:

   User Container: Select the Identity Vault container where Linux and Unix Settings users will be added if they don’t already exist in the vault. This value becomes the default for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.

   Group Container: Since the Linux and Unix Settings driver does not synchronize Group objects, this setting can be ignored.
9. (Conditional) If not already configured, fill in the following fields on the Common Settings Advanced Edition page, then click Next:

   User Application Provisioning Services URL: specify the User Application Identity Manager Provisioning URL.

   User Application Provisioning Services Administrator: Specify the DN of the User Application Administrator user. This user should have the rights for creating and assigning resources. For more information, see “Setting Up Administrative Accounts” in the NetIQ Identity Manager 4.8 Common Driver Administration Guide.
10. On the Install Linux and Unix Settings page, fill in the following field:

    Driver Name: Specify a name for the driver that is unique within the driver set.
11. (Conditional) On the Driver Parameters page, review the default Subscriber and Publisher Options. Edit, if necessary, and click Next:
12. (Conditional) On the Entitlements Name to CSV File Mappings page, click the Add Name to File Mapping icon to populate the page with the entitlement configuration options. Identity Manager uses the CSV file to map Linux and Unix Settings entitlements into corresponding resources in the Identity Manager catalog.

    *NOTE:*This page is displayed only if you installed the Entitlements package.

    The information that you specify in this page is used for creating the permission catalog. Fill in the following fields, then click Next:

    Entitlement Name: Specify a descriptive name for the entitlement to map it to the CSV file that contains the Linux and Unix Settings entitlement details.

    Entitlement Name is the name of the entitlement. This parameter corresponds to the Entitlement Assignment Attribute in Linux and Unix Settings. For example, you could define an entitlement called ParkingPass.

    Entitlement Assignment Attribute: Specify a descriptive name for the assignment attribute for an entitlement.

    Entitlement Assignment Attribute holds the entitlement values in Linux and Unix Settings. For example, you could have an attribute called Parking.

    You must add this parameter to Field Names in the Driver Parameters page or modify it in driver settings after creating the driver.

    CSV File: Specify the location of the CSV file. This file must be located on the same server as the driver. This file contains the values for the application entitlements.

    Multi-valued?: Set the value of this parameter to True if you want to assign resources and entitlements multiple times with different values to the same user. Otherwise, set it to False.
13. Review the summary of tasks that will be completed to create the driver, then click Finish.

The driver is created. You can modify the configuration settings by continuing with the next section, [Configuring the Driver](b1byr9qs.html#b1bxrh8d). If you don’t need to configure the driver, skip ahead to [Deploying the Driver](b1byr9qs.html#b1bxrmiy).

## 3.4.3 Configuring the Driver

There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to review the Driver Parameters located on the Driver Configuration page and the Global Configuration Values. These settings must be configured properly for the driver to start and function correctly.

To access the Driver Properties page:

1. Open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon.png) or the driver line, then select Properties.
3. Modify the driver settings as necessary.
4. Continue with the next section, [Deploying the Driver](b1byr9qs.html#b1bxrmiy).

## 3.4.4 Deploying the Driver

After a driver is created in Designer, it must be deployed into the Identity Vault:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon.png) or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](b1byr9qs.html#b1bxrmj4); otherwise, specify the following information:

   Host: Specify the IP address or DNS name of the server hosting the Identity Vault.

   Username: Specify the DN of the user object used to authenticate to the Identity Vault.

   Password: Specify the user’s password.
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
   3. Repeat [Step 8.a](b1byr9qs.html#b1byali8) and [Step 8.b](b1byr9qs.html#b1byali9) for each object you want to exclude.
   4. Click OK.
9. Click OK.

## 3.4.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon.png) or the driver line, then select Live > Start Driver.

## 3.4.6 Creating the Driver in iManager

Drivers are created with packages, and iManager does not support packages. In order to create or modify drivers, you must use Designer. See [Creating the Driver in Designer](b1byr9qs.html).
