# 3.1 Creating the Driver Object in Designer

You can run the driver as a native Java module or as an Identity Manager driver on any supported platform.

To create an ID Provider driver object, install the driver packages and then modify the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](check-id-provider-driver-object-in-designer.html#bl582ar)
* [Installing the Driver Packages](check-id-provider-driver-object-in-designer.html#brn9cu1)
* [Configuring the Driver Settings](check-id-provider-driver-object-in-designer.html#bfx15dc)
* [Deploying the Driver Object](check-id-provider-driver-object-in-designer.html#bfx15dg)
* [Starting the Driver](check-id-provider-driver-object-in-designer.html#bfx15e0)

## 3.1.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements (not available in Beta), filters, and Schema Mapping policies. These packages are only available in Designer. You can upgrade any package that is installed if there is a newer version of the package available. It is recommended to have the latest packages in the Package Catalog before creating a new driver object. For more information on upgrading packages, see "[Upgrade Settings:](../../../identity-manager-48/designer_admin/data/packmancontent.html#b11r7up8)" in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).

To verify you have the most recent version of the driver packages in the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/package_import_a.png)
6. Select any ID Provider driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](check-id-provider-driver-object-in-designer.html#brn9cu1).

## 3.1.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select ID Provider Base, then click Next.
4. On the ID Provider page, specify a name for the driver, then click Next.
5. On the ID Provider page, fill in the following fields, then click Next:

   *LDAP server:*
   Specify the IP address or DNS name of the LDAP server that contains the ID policies.

   *Policy Container DN:*
   Specify the LDAP DN of the policy container.
6. On the ID Provider page, fill in the following fields, then click Next:

   *Authentication ID:*
   Specify the LDAP DN of a user with read/write access to the ID Policy container and its child objects.

   *Authentication Password:*
   Specify the password of the user named in the Authentication ID field.
7. Fill in the following fields for Remote Loader information:

   *Connect To Remote Loader:*
   Select Yes or No to determine if the driver will use the Remote Loader. For more information, see the [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_windows/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

   If you select No, skip to [Step 8](check-id-provider-driver-object-in-designer.html#brnbqsk). If you select Yes, use the following information to complete the configuration of the Remote Loader, then click Next:

   *Host Name:*
   Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

   *Port:*
   Specify the port number for this driver. Each driver connects to the Remote Loader on a separate port. The default value is 8090.

   *Remote Loader Password:*
   Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

   *Driver Password:*
   Specify a password for the driver to authenticate to the Identity Manager server. It must be the same password that is specified as the Driver Object Password on the Remote Loader.
8. Review the summary of tasks that will be completed to create the driver, then click Finish.
9. After the driver packages are installed, if you want to change the configuration of the Role-Based Entitlement driver, continue to [Configuring the Driver Settings](check-id-provider-driver-object-in-designer.html#bfx15dc).

   or

   If you do not want to change the configuration of the driver, continue to [Deploying the Driver Object](check-id-provider-driver-object-in-designer.html#bfx15dg).

## 3.1.3 Configuring the Driver Settings

After you import the driver configuration file, the ID Provider driver will run. However, there are many configuration settings that you can use to customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). The settings are described in [Section A.0, Driver Properties](id-provider-driver-properties.html).

If you do not have the Driver Properties page displayed in Designer:

1. Open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Properties.
3. Make the changes you want, then continue to [Starting the Driver](check-id-provider-driver-object-in-designer.html#bfx15e0).

   If you want to make additional changes to the driver, the following sections contain information about the driver parameters.

* [ID Policy Repository](check-id-provider-driver-object-in-designer.html#bs0pzo8)
* [Client Options](check-id-provider-driver-object-in-designer.html#bs0q00k)
* [Server Options](check-id-provider-driver-object-in-designer.html#bs0q08c)

### ID Policy Repository

The ID policy repository parameters contain information about the location and how to access any ID policies.

| Parameter | Default Value | Description |
| LDAP Server | 127.0.0.1 | The IP address or DNS name of the LDAP server holding the ID policies |
| LDAP Port | 636 | The TCP port that the LDAP server listens on.  The value is usually 389 for non-SSL connections and 636 for SSL connections. |
| Use SSL | True | Specify whether or not you want to use SSL. |
| Always trust | True | Specify whether or not you want to trust all servers. If this option is set to True, the ID provider trusts all LDAP servers even if the server certificate is untrusted. |
| Policy Container DN | LDAP DN for the policy container under the driver object. For example cn=id-policies,cn=id-provider,cn=driverset1,dc=idm,dc=services,dc=system. | Specify or browse to the DN of the policy container in your tree. The policy container can only be created under the ID Provider driver. |

### Client Options

The client options are for the ID Provider clients. For more information, see [Section 5.0, Configuring ID Clients](configure-id-provider-client.html).

| Parameter | Default Value | Description |
| Client name | ID-Provider Driver | This is the name the driver uses when it acts as an ID client and requests and ID from the provider. This is useful for tracing and if access control is enabled on any of the ID policies.  If access control is enabled, a list of ID client names can be specified that are allowed to obtain an ID from the policy. If the client name associated with the request is not in that list, the provider does not issue an ID. |
| ID Generation Map | workforceID=wfid | Provide a comma-separated list of attribute=policy pairs.  For example, workforceID=wfid,uniqueID=uid. This example configures the driver to request IDs from the wfid policy and stores them in the workforceID attribute whenever a new object is created or whenever someone tries to change this attribute.  Similarly, IDs from the UID policy are used from the uid attribute. The driver only issues IDs for any attribute if that attribute and the object class holding the attribute are in both the Subscriber, Publisher, Filter, and are set to synchronize.  Attribute names must be in the Identity Namespace (not LDAP) and must be case-exact. |

### Server Options

These options allow you to set up clients other than the ID Provider driver by using Java Remote Method Invocation (RMI). It also allows you to set ID Provider trace level.

| Parameter | Default Value | Description |
| Start RMI | True | Controls whether the ID provider starts an RMI service or not. You only need a running RMI service if you request IDs from other clients than the driver (for example, DirXMLScript policies.) If all IDs are managed through this driver’s filter and ID Generation Map settings, then no RMI service is needed. |
| RMI server | 172.17.2.117 | Specify the IP address the RMI server binds to. Leave this field empty if you want the server to bind to all IP addresses. |
| RMI port | 1199 | Specify the TCP port the RMI service listens on. The defined standard port for RMI is 1099. If that port is already in use (you see errors in the trace when you start the driver), use a different port higher than 1023. This configuration assumes a port of 1199 to avoid common port conflicts. |
| Use legacy ID-server schema? | False | Enables the backward compatibility mode when migrating an existing ID-Server configuration to run with the new ID Provider driver. Setting this to True allows you to keep using legacy ID policies, which do not use the new schema that ships with the ID Provider. |
| Trace level | ALL | This is not the driver trace level, but the ID Provider trace level. The levels are:  * *OFF:*   Tracing is turned off. * *FATAL:*   Displays only fatal messages. * *ERROR:*   Displays only error messages. * *WARN:*   Displays only warning messages. * *INFO:*   Displays only informational messages. * *DEBUG:*   Displays only debug messages. * *ALL:*   Displays all messages. |

## 3.1.4 Deploying the Driver Object

After a driver is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 4](check-id-provider-driver-object-in-designer.html#bfx15dp); otherwise, specify the follow information, then click OK:

   * *Host:*
     Specify the IP address or DNS name of the server hosting the Identity Vault.
   * *Username:*
     Specify the DN of the user object used to authenticate to the Identity Vault.
   * *Password:*
     Specify the user’s password.
4. Read the deployment summary, then click Deploy.
5. Read the successful message, then click OK.
6. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault and to the input and output directories on the server. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user. Whatever rights that the driver needs to have on the server, the DriversUser object must have the same security rights.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.

      For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see [Establishing a Security Equivalent User](../../../identity-manager-48/security/data/establishing-security-equivalent-user-in-identity-manager.html#establishing-security-equivalent-user-in-identity-manager) in the [NetIQ Identity Manager Security Guide](../../../identity-manager-48/security/data/identity-manager-security-guide.html#identity-manager-security-guide).
7. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude, then click OK.
   2. Repeat [Step 7.a](check-id-provider-driver-object-in-designer.html#bfx15dv) for each object you want to exclude, then click OK.
8. Click OK.

## 3.1.5 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or the driver line, then select Live > Start Driver.

For information about management tasks for the driver, see [Section 6.0, Managing the ID Provider Driver](manage-id-provider-driver.html).
