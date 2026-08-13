# 3.1 Creating the Driver Object in Designer

To create the eDirectory driver object, install the driver packages and then modify the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start it.

To connect two trees, you need to complete the following procedures for the drivers that are installed in each Identity Vault.

* [Importing the Current Driver Packages](creating-the-driver-object-in-designer.html#importing-the-current-driver-objects)
* [Installing the Driver Packages](creating-the-driver-object-in-designer.html#installing-the-driver-packages)
* [Configuring the Driver](creating-the-driver-object-in-designer.html#configuring-the-driver)
* [Deploying the Driver Object](creating-the-driver-object-in-designer.html#deploying-the-driver-object)
* [Starting the Driver](creating-the-driver-object-in-designer.html#starting-the-driver)

*NOTE:*You should not create driver objects by using the new Identity Manager 4.0 and later configuration files through Identity Console. This method of creating driver objects is no longer supported. To create drivers, you now need to use the new package management features provided in Designer.

## 3.1.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer. You can upgrade any package that is installed if there is a newer version of the package available.It is recommended to have the latest packages in the Package Catalog before creating a new driver object.

Before creating a driver object in Designer, it is recommended to have all the required packages already imported in the Package Catalog of Designer. Designer prompts you for importing the required packages when it creates the driver object.

To verify you have the most recent version of the driver packages imported into the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/package_import_a.png)
6. Select any eDirectory driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](creating-the-driver-object-in-designer.html#installing-the-driver-packages).

## 3.1.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select eDirectory Base, then click Next.
4. Select the optional features to install for the eDirectory driver. All options are selected by default. The options are:

   *Default Configuration:*
   These packages contain the default configuration information for the eDirectory driver. Always leave this option selected.

   *Entitlements:*
   These packages contain the policies and entitlements required to enable the driver for account creation and management with entitlements. For more information, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

   *Password Synchronization:*
   These packages contain the policies required to enable password synchronization. Leave this option selected if you want to synchronize passwords between the Identity Vaults.

   *Data Collection:*
   These packages contain the policies that enable the driver to collect data for reports. If you are using the Identity Reporting Module, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

   *Account Tracking:*
   This group of packages contain the policies that enable account tracking information for reports. If you are using the Identity Reporting Module, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).
5. After selecting the optional packages, click Next.
6. (Conditional) If there are package dependencies for the packages you selected to install, you must install these dependencies to install the selected packages. Click OK to install the Password Synchronization Notification package dependency.
7. (Conditional) Click OK to install the Common Settings package, if you have not installed any other packages into the selected driver set.
8. Click OK to install the Advanced Java Class package if you have not installed any other packages into the selected driver set.
9. (Conditional) Fill in the following fields on the Common Settings page:

   The Common Settings page is displayed only if the Common Settings package is installed as a dependency.

   *User Container:*
   Select the Identity Vault container where the users are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.

   *Group Container:*
   Select the Identity Vault container where the groups are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.
10. Click Next.
11. On the Driver Information page, specify a name for the driver, then click Next.
12. Fill in the following field to configure the driver:

    *Remote Tree Address and Port:*
    Specify the hostname or IP address, and port of the server in the remote Identity Vault.
13. Click Next.
14. Fill in the following fields on the eDirectory Default Configuration page:

    *eDirectory Publisher Placement type:*
    Select how the objects are placed in the remote Identity Vault and the local Identity Vault. The options are:

    * *Mirrored:*
      Mirrors the structure between the remote Identity Vault and the local Identity Vault.

      If you choose this option, use the same option for configuring both eDirectory trees you are synchronizing.

      This option in the driver configuration synchronizes User, Group, Organization, Country, and Organizational Unit objects. It also mirrors the structure of a subtree in the other tree.
    * *Flat:*
      All of the objects are placed into a single container.

      This option synchronizes User and Group objects and places all users in one container and all groups in another container.

      This option is typically used in conjunction with the Department option (or a similar configuration) in the other tree.

      This option doesn’t create the containers that hold the users and groups. You must create those manually.
    * *Department:*
      Users are placed in containers named after the department.

      This option synchronizes User and Group objects and places all users and groups in a container based on the Department field in your management console.

      This configuration is typically used in conjunction with the Flat option (or a similar configuration) in the other tree.

      This option doesn’t create the containers for each department. You must create those manually. They must be the same as the container specified during import.

    *Remote Tree Base User Container:*
    Specify the source container of the user objects in the remote Identity Vault.

    *Remote Tree Base Groups Container:*
    Specify the source container of the group objects in the remote Identity Vault.
15. Click Next.
16. (Conditional) Fill in the following fields on the eDirectory Managed System Information page. This page is displayed only if you selected to install the Data Collection and Account Tracking groups of packages.

    *Name:*
    Specify a descriptive name for this Identity Vault. The name is displayed in the reports.

    *Description:*
    Specify a brief description of the this Identity Vault. The description is displayed in the reports.

    *Location:*
    Specify the physical location of this Identity Vault. The location is displayed in the reports.

    *Vendor:*
    Select NetIQ as the vendor of this system. The vendor information is displayed in the reports.

    *Version:*
    Specify the version of this Identity Vault. The version is displayed in the reports.
17. Click Next.
18. (Conditional) Fill in the following fields to define the ownership of this Identity Vault. This page is displayed only if you selected to install the Data Collection and Account Tracking groups of packages.

    *Business Owner:*
    Select a user object in the Identity Vault that is the business owner of this Identity Vault. This can only be a user object, not a role, group, or container.

    *Application Owner:*
    Select a user object in the Identity Vault that is the application owner for this Identity Vault. This can only be a user object, not a role, group, or container.
19. Click Next.
20. (Conditional) Fill in the following fields to define the classification of the Identity Vault. This page is only displayed if you selected to install the Data Collection and Account Tracking groups of packages.

    *Classification:*
    Select the classification of the Identity Vault. This information is displayed in the reports. The options are:

    * Mission-Critical
    * Vital
    * Not-Critical
    * Other

      If you select Other, you must specify a custom classification for the Identity Vault.

    *Environment:*
    Select the type of environment the Identity Vault provides. The options are:

    * Development
    * Test
    * Staging
    * Production
    * Other

      If you select Other, you must specify a custom classification for the Identity Vault.
21. Click Next.
22. Review the summary of tasks that will be completed to create the driver, then click Finish.
23. After the driver packages are installed, there is additional configuration required for the eDirectory driver. Continue to [Configuring the Driver](creating-the-driver-object-in-designer.html#configuring-the-driver) to configure the driver.

## 3.1.3 Configuring the Driver

After installing the driver packages, the eDirectory driver will run. However, the basic configuration might not meet the requirements for your environment. You should complete the following tasks to configure the driver:

* *Secure the driver connection:*
  eDirectory drivers communicate via SSL using digital certificates for authentication. You need to set up this secure connection. See [Section 5.0, Securing Driver Communication](securing-driver-communication.html).
* *Configure the driver filter:*
  Modify the driver filter to include the object classes and attributes you want synchronized between the two eDirectory trees. For information about the classes and attributes include in the filter for the basic configuration, see [Section B.0, Synchronized Attributes](synchronized-attributes.html).
* *Configure policies:*
  Modify the policies as needed. Policies should generally be placed only on the Publisher channel, not on the Subscriber channel. The Matching and Placement policies cannot operate correctly on the Subscriber channel because the Subscriber channel is acting primarily as a source of events for the Publisher channel of the other tree.

  You might consider placing an Event Transform or Create Policy on the Subscriber channel to prevent sending unnecessary data across the channel.
* *Configure password synchronization:*
  The basic driver configuration is set up to support bidirectional password synchronization through Universal Password. If you don’t want this setup, see [Section 6.0, Synchronizing Passwords](synchronizing-passwords.html).

After completing the configuration tasks, continue with the next section, [Deploying the Driver Object](creating-the-driver-object-in-designer.html#deploying-the-driver-object).

## 3.1.4 Deploying the Driver Object

After a driver is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](creating-the-driver-object-in-designer.html#bfvehvl); otherwise, specify the following information:

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

   The driver requires rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat [Step 8.a](creating-the-driver-object-in-designer.html#bfvehvr) and [Step 8.b](creating-the-driver-object-in-designer.html#bfvehvs) for each object you want to exclude.
   4. Click OK.
9. Click OK.

## 3.1.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Start Driver.

For information about management tasks with the driver, see [Section 7.0, Managing the Driver](managing-the-driver.html).
