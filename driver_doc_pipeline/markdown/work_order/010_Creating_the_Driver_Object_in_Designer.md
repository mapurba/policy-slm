# 4.2 Creating the Driver Object in Designer

You create the WorkOrder driver object by importing the driver’s basic configuration file and then modifying the configuration to suit your environment. After you’ve created and configured the driver, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](create-driver-object-designer.html#bl582ar)
* [Installing the Driver Packages](create-driver-object-designer.html#brtiuc0)
* [Configuring the Driver Settings](create-driver-object-designer.html#bfyh7j5)
* [Deploying the Driver Object](create-driver-object-designer.html#bfyh7j9)
* [Starting the Driver](create-driver-object-designer.html#bfyh7jt)

*NOTE:*You should not create driver objects by using the new Identity Manager 4.0 and later configuration files through Identity Console. This method of creating driver objects is no longer supported. To create drivers, you now need to use the new package management features provided in Designer.

## 4.2.1 Importing the Current Driver Packages

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
6. Select any WorkOrder driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](create-driver-object-designer.html#brtiuc0).

## 4.2.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver object.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select WorkOrder Base, then click Next.
4. On the Driver Information page, specify a name for the driver, then click Next.
5. On the Install WorkOrder Base page, specify the name of the container that holds the WorkOrder objects, then click Next.
6. Fill in the following fields for Remote Loader information:

   *Connect To Remote Loader:*
   Select Yes or No to determine if the driver will use the Remote Loader. For more information, see [Installing Java Remote Loader](../../../identity-manager-48/setup_linux/data/install-linux-java-remote-loader.html#install-linux-java-remote-loader) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Planning to Install the Remote Loader](../../../identity-manager-48/setup_windows/data/windows-install-remote-loader.html#windows-install-remote-loader) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

   If you select No, skip to [Step 7](create-driver-object-designer.html#brtiudh). If you select Yes, use the following information to complete the configuration of the Remote Loader, then click Next:

   *Host Name:*
   Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

   *Port:*
   Specify the port number for this driver. Each driver connects to the Remote Loader on a separate port. The default value is 8090.

   *Remote Loader Password:*
   Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

   *Driver Password:*
   Specify a password for the driver to authenticate to the Identity Manager server. It must be the same password that is specified as the Driver Object Password on the Remote Loader.
7. Review the summary of tasks that will be completed to create the driver, then click Finish.
8. After you have installed the driver, you must change the configuration for your environment. Proceed to [Configuring the Driver Settings](create-driver-object-designer.html#bfyh7j5).

## 4.2.3 Configuring the Driver Settings

After installing the driver packages, the WorkOrder driver will run. However, the basic configuration might not meet the requirements for your environment. For example, you might need to change whether the driver checks for new work orders in the WorkOrder container at a specific interval throughout the day or only at a specific time each day. The default setting is to poll the WorkOrder container every minute.

In addition to the polling setting, there are additional settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs).

The driver configuration settings are explained in [Section A.0, Driver Properties](driver-properties.html).

If you do not have the Driver Properties page displayed in Designer:

1. Open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Properties.

   Although it is important for you to understand all of the settings, your first priority should be to review the [Driver Parameters](driver-configuration.html#b4m4h9a) located on the Driver Configuration page. These settings let you control the method the driver uses to check for new work orders.
3. After you configure the driver, continue with [Deploying the Driver Object](create-driver-object-designer.html#bfyh7j9).

## 4.2.4 Deploying the Driver Object

After the driver object is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 4](create-driver-object-designer.html#bfyh7ji); otherwise, specify the following information to authenticate, then click OK:

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
   2. Repeat [Step 7.a](create-driver-object-designer.html#bfyh7jo) for each object you want to exclude.
   3. Click OK.
8. Click OK.

## 4.2.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it doesn’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Start Driver.

For information about management tasks with the driver, see [Section 8.0, Managing the Driver](manage-driver.html).
