# 4.2 Creating the Driver Object in Designer

You create the PeopleSoft driver by installing the driver packages and then modifying the configuration to suit your environment. After you create and configure the driver, you need to deploy it to the Identity Vault and start it.

*NOTE:*To create drivers, you now need to use the new package management features provided in Designer.

* [Importing the Current Driver Packages](create-driver-object-designer.html#bl582ar)
* [Installing the Driver Packages](create-driver-object-designer.html#brtiuc0)
* [Configuring the Driver](create-driver-object-designer.html#bfveihb)

## 4.2.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver object, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer. You can upgrade any package that is installed if there is a newer version of the package available.It is recommended to have the latest packages in the Package Catalog before creating a new driver object. For more information on upgrading packages, see "[Upgrading Installed Packages](../../../identity-manager-48/designer_admin/data/packman.html#packmanupgrade)" in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).

To verify you have the most recent version of the driver packages in the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/package_import_a.png)

   You can download the new packages from the [Download site](https://download.microfocus.com/Download?buildid=xGC_suQ7uiM~).
6. Select any PeopleSoft driver packages

   or

   Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](create-driver-object-designer.html#brtiuc0).

## 4.2.2 Installing the Driver Packages

After you have imported the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select PeopleSoft Base, then click Next.
4. Select the optional features to install for the PeopleSoft driver, then click Next. All options are selected by default.

   *PeopleSoft Password Synchronization:*
   This package contains the policies that enable the PeopleSoft driver to synchronize passwords. If you want to synchronize passwords, verify that this option is selected. For more information, see the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

   *Managed System Information:*
   This package contains the policies that enable Identity Reporting. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).
5. (Conditional) If there are package dependencies for the packages you selected to install, you must install them to install the selected package. Click OK to install the package dependency listed.
6. (Conditional) If more than one type of package dependency must be installed, you are presented with these packages separately. Continue to click OK to install any additional package dependencies.
7. (Conditional) On the Install Common Settings page, fill in the following fields, then click Next:

   The Common Settings page is displayed only if the Common Settings package is installed as a dependency.

   *User Container:*
   Select the Identity Vault container where the PeopleSoft accounts will be added if they don’t already exist in the vault. This value becomes the default for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.

   *Group Container:*
   Select the Identity Vault container where the PeopleSoft accounts will be added if they don’t already exist in the vault. This value becomes the default for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.
8. On the Driver Information page, specify a name for the driver, then click Next.
9. On the Application Authentication page, fill in the following fields, then click Next:

   *Authentication ID:*
   Specify the authentication ID for the driver.

   *Connection Information:*
   Specify the connection information for the driver to connect to the PeopleSoft system.

   *Password:*
   Specify the password for the authentication ID.
10. Fill in the following fields for Remote Loader information:

    *Connect To Remote Loader:*
    Select Yes or No to determine if the driver will use the Remote Loader. For more information, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_windows/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

    If you select No, then click Next. If you select Yes, use the following information to complete the configuration of the Remote Loader, then click Next:

    *Host Name:*
    Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

    *Port:*
    Specify the port number for this driver. Each driver connects to the Remote Loader on a separate port. The default value is 8090.

    *KMO:*
    Specify the key name of the Key Material Object containing the keys and certificates used for SSL. It is only used when there is an SSL connection between the Remote Loader and the Identity Manager engine.

    *Other Parameters:*
    Specify other parameters required for the driver in the connection string.These parameters must be in the key-value pair. For example, paraName1=paraValue1.

    *Remote Loader Password:*
    Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

    *Driver Password:*
    Specify a password for the driver to authenticate to the Identity Manager server. It must be the same password that is specified as the Driver Object password on the Remote Loader.
11. (Conditional) On the Install PeopleSoft Managed System Information page, fill in the following fields to define your PeopleSoft system, then click Next:

    The Install PeopleSoft Managed System Information page is displayed only if you selected to install the Managed System packages.

    *Name:*
    Specify a descriptive name for this PeopleSoft system. The name is displayed in reports.

    *Description:*
    Specify a brief description for this PeopleSoft system. The description is displayed in reports.

    *Location:*
    Specify the physical location of this PeopleSoft system. The location is displayed in reports.

    *Vendor:*
    Specify the vendor of PeopleSoft system. This information is displayed in reports.

    *Version:*
    Specify the version of this PeopleSoft system. The version is displayed in the reports.
12. (Conditional) On the Install PeopleSoft Managed System Information page, fill in the following fields to define the classification of the PeopleSoft system, then click Next:

    The Install PeopleSoft Managed System Information page is displayed only if you selected to install the Data Collection and Account Tracking packages.

    *Classification:*
    Select the classification of the PeopleSoft system. This information is displayed in the reports. Your options are:

    * Mission-Critical
    * Vital
    * Not-Critical
    * Other

      If you select Other, you must specify a custom classification for the PeopleSoft system.

    *Environment:*
    Select the type of environment the PeopleSoft system provides. The options are:

    * Development
    * Test
    * Staging
    * Production
    * Other

      If you select Other, you must specify a custom classification for the PeopleSoft system.
13. (Conditional) On the Install PeopleSoft Managed System Information page, fill in the following fields to define the ownership of the PeopleSoft system, then click Next:

    The Install PeopleSoft Managed System Information page is displayed only if you selected to install the Data Collection and Account Tracking packages.

    *Business Owner:*
    Select a user object in the Identity Vault that is the business owner of the PeopleSoft system. This can only be a user object, not a role, group, or container.

    *Application Owner:*
    Select a user object in the Identity Vault that is the application owner of the PeopleSoft system. This can only be a user object, not a role, group, or container.
14. (Conditional) On the Install PeopleSoft Password Synchronization page, fill in the following fields, then click Next:

    The Install PeopleSoft Password Synchronization page is displayed only if you selected to install the Password Synchronization packages.

    *Identity Manager accepts passwords from application:*
    Select True to allow passwords to flow from the connected system to the Identity Vault.

    *Publish passwords to NDS password:*
    Select True to use the password from the connected system to set the non-reversible NDS password in the Identity Vault.

    *Publish passwords to Distribution Password:*
    Select True to use the password from the connected system to set the NMAS Distribution Password used for Identity Manager password synchronization.

    *Require password policy validation before publishing passwords:*
    Select True to apply the NMAS password policies during publish password operations. The password is not written to the Identity Vault if it does not comply.

    *Notify the user of password synchronization failure via e-mail:*
    Select True to notify the user by e-mail of any password synchronization failures.
15. Review the summary of tasks that will be completed to create the driver, then click Finish.
16. After you have installed the driver, you must change the configuration for your environment. Proceed to [Configuring the Driver](create-driver-object-designer.html#bfveihb).

## 4.2.3 Configuring the Driver

After importing the packages, you need to configure the driver before it can run. You should complete the following tasks to configure the driver:

* *Ensure that the driver can authenticate to PeopleSoft:*
  Make sure that you have established a PeopleSoft administrative account for the driver (see [Creating a PeopleSoft Account](create-driver-account.html)) and that the correct authentication information, including the User ID and password, is defined for the driver parameters (see [Authentication ID:](driver-properties-configuration.html#bs8f029)).
* *Configure the driver parameters:*
  There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to configure the driver parameters located on the Driver Configuration page. For information about the driver parameters, see [Driver Parameters](driver-properties-configuration.html#b4m4h9a).
* *Configure the driver policies and filter:*
  Modify the driver policies and filter to implement your business policies. For instructions, see [Modifying Driver Policies](modify-driver-policies.html).
* *Configure password synchronization:*
  The basic driver configuration supports password synchronization through Universal Password. If you don’t want this setup, see [Configuring Password Flow](../../../identity-manager-48/password_management/data/configuring-password-flow.html#configuring-password-flow) in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

After completing the configuration tasks, continue with the next section, [Deploying, Starting and Activating the Driver](t4d0rxs1iuyr.html).
