# 4.1 Creating the Driver Object in Designer

To create the Entitlements Service driver, install the driver packages and then modify the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](create-driver-object-designer.html#bl582ar)
* [Installing the Driver Packages](create-driver-object-designer.html#brn9cu1)
* [Configuring the Driver Settings](create-driver-object-designer.html#bfx15dc)
* [Deploying the Driver Object](create-driver-object-designer.html#bfx15dg)
* [Starting the Driver](create-driver-object-designer.html#bfx15e0)

*NOTE:*To create drivers, you need to use the new package management features provided in Designer. This method of creating driver objects is not supported in Identity Console.

## 4.1.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer. You can upgrade any package that is installed if there is a newer version of the package available. Before creating a driver object in Designer, it is recommended to have all the required packages already imported in the Package Catalog of Designer. Designer prompts you for importing the required packages when it creates the driver object. For more information on upgrading packages, see "[Upgrading Installed Packages](../../../identity-manager-49/designer_admin/data/packman.html#packmanupgrade)"in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-49/designer_admin/data/bookinfo.html#bookinfo).

To verify you have the most recent version of the driver packages in the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/package_import_a.png)
6. Select any Role-Based Entitlement driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](create-driver-object-designer.html#brn9cu1).

## 4.1.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select Role-Based Entitlements (RBE) Base, then click Next.
4. On the Role-Based Entitlements page, specify a name for the driver, then click Next.
5. Review the summary of tasks that will be completed to create the driver, then click Finish.
6. After the driver packages are installed, if you want to change the configuration of the Role-Based Entitlement driver, continue to [Configuring the Driver Settings](create-driver-object-designer.html#bfx15dc).

   or

   If you do not need to change the configuration, continue with [Deploying the Driver Object](create-driver-object-designer.html#bfx15dg).

## 4.1.3 Configuring the Driver Settings

After you import the driver configuration file, the Role-Based Entitlements Service driver will run. However, there are many configuration settings that you can use to customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). The settings are described in [Section A.0, Driver Properties](driver-properties.html).

If you do not have the Driver Properties page displayed in Designer:

1. Open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Properties.
3. Make the changes you want, then click OK.
4. Continue with [Deploying the Driver Object](create-driver-object-designer.html#bfx15dg).

## 4.1.4 Deploying the Driver Object

After the driver object is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](create-driver-object-designer.html#bfx15dp); otherwise, specify the follow information:

   * *Host:*
     Specify the IP address or DNS name of the server hosting the Identity Vault.
   * *Username:*
     Specify the DN of the user object used to authenticate to the Identity Vault.
   * *Password:*
     Specify the user’s password.
4. Click OK.
5. Read the deployment summary, then click Deploy.
6. Read the successful message, then click OK.
7. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault and to the input and output directories on the server. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.

      For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see "[Establishing a Security Equivalent User](../../../identity-manager-49/security/data/establishing-security-equivalent-user-in-identity-manager.html#establishing-security-equivalent-user-in-identity-manager)" in the [NetIQ Identity Manager Security Guide](../../../identity-manager-49/security/data/identity-manager-security-guide.html#identity-manager-security-guide).
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat [Step 8.a](create-driver-object-designer.html#bfx15dv) and [Step 8.b](create-driver-object-designer.html#bfx15dw) for each object you want to exclude.
   4. Click OK.
9. Click OK.

## 4.1.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Start Driver.

For information about management tasks for the driver, see [Section 8.0, Managing the Driver](manage-driver.html).
