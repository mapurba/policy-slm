# 3.1 Creating the Driver in Designer

To create a JMS driver object, install the driver packages and then modify the configuration to suit your environment. After you create and configure the driver, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](creating-the-driver-in-designer.html#bl582ar)
* [Installing the Driver Packages](creating-the-driver-in-designer.html#brtiuc0)
* [Configuring the Driver](creating-the-driver-in-designer.html#bfveihb)
* [Deploying the Driver](creating-the-driver-in-designer.html#bfvehvc)
* [Starting the Driver](creating-the-driver-in-designer.html#bfvehvw)

*NOTE:*To create drivers, you now need to use the new package management features provided in Designer.

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
6. Select any JMS driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](creating-the-driver-in-designer.html#brtiuc0).

## 3.1.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select JMS Base, then click Next.
4. Select the corresponding package for one of the supported JMS vendors.

   The options are:

   * JMS JBoss
   * JMS SonicMQ
   * JMS WebSphere
   * JMS TIBCO
   * Other

   You can select only one package at a time. If you selected Other, then click Next. Otherwise, specify the Broker URL for the JMS vendor you selected, then click Next. The URL usually consists of a protocol (http), an IP address (255.255.255.255), and a port number (8080). For example: jnp://172.17.2.16:1099.
5. On the Driver Information page, specify a name for the driver, then click Next.
6. Fill in the following fields for Remote Loader information:

   *Connect To Remote Loader:*
   Select Yes or No to determine if the driver will use the Remote Loader. For more information, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_windows/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

   If you select No, skip to [Step 7](creating-the-driver-in-designer.html#brtiudh). If you select Yes, use the following information to complete the configuration of the Remote Loader, then click Next:

   *Host Name:*
   Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

   *Port:*
   Specify the port number for this driver. Each driver connects to the Remote Loader on a separate port. The default value is 8090.

   *Remote Loader Password:*
   Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

   *Driver Password:*
   Specify a password for the driver to authenticate to the Identity Manager server. It must be the same password that is specified as the Driver Object Password on the Remote Loader.
7. Review the summary of tasks that will be completed to create the driver, then click Finish.
8. After you have installed the driver, you must change the configuration for your environment. Proceed to [Configuring the Driver](creating-the-driver-in-designer.html#bfveihb).

## 3.1.3 Configuring the Driver

After installing the driver packages, the driver will start. However, the basic configuration probably does not meet the requirements for your environment. You should complete the following tasks to configure the driver:

* *Configure the driver parameters:*
  There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to review the [Driver Parameters](driver-configuration.html#b4m4h9a) located on the Driver Configuration page.
* *Configure the driver filter:*
  Modify the driver filter to include the object classes and attributes you want synchronized between the Identity Vault and the JMS vendor.
* *Configure policies:*
  Modify the policies on the Subscriber and Publisher channels. For information about using policies, see the [NetIQ Identity Manager - Using Designer to Create Policies](../../../identity-manager-48/policy_designer/data/using-designer-to-create-policies.html#using-designer-to-create-policies).

After completing the configuration tasks, continue with the next section, [Deploying the Driver](creating-the-driver-in-designer.html#bfvehvc).

## 3.1.4 Deploying the Driver

After a driver is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](creating-the-driver-in-designer.html#bfvehvl); otherwise, specify the following information:

   *Host:*
   Specify the IP address or DNS name of the server hosting the Identity Vault.

   *Username:*
   Specify the DN of the user object used to authenticate to the Identity Vault.

   *Password:*
   Specify the user’s password.
4. Click OK.
5. Read the deployment summary, then click Deploy.
6. Read the message, then click OK.
7. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault and to the input and output directories on the server. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.

      For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see “Establishing a Security Equivalent User” in the [Identity Manager 4.5 Security Guide](https://www.netiq.com/documentation/idm402/idm_security/?page=/documentation/idm402/idm_security/data/front.html).
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat [Step 8.a](creating-the-driver-in-designer.html#bfvehvr) and [Step 8.b](creating-the-driver-in-designer.html#bfvehvs) for each object you want to exclude.
   4. Click OK.
9. Click OK.

## 3.1.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Start Driver.

For information about management tasks with the driver, see [Section 6.0, Managing the Driver](managing-the-driver.html).
