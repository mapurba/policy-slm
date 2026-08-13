# 4.1 Creating the Driver Object in Designer

To create the Bidirectional eDirectory driver object, install the driver packages and then modify the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start it.

To synchronize data between the eDirectory connected system and the Identity Vault, you need to complete the following procedures for the drivers that are installed in each Identity Vault:

* [Importing the Current Driver Packages](creating-the-driver-object-in-designer.html#bl582ar)
* [Installing the Driver Packages](creating-the-driver-object-in-designer.html#brn9cu1)
* [Configuring the Driver Object](creating-the-driver-object-in-designer.html#bfveihb)

*NOTE:*You should not create driver objects using the new Identity Manager 4.0 and later configuration files through Identity Console. This method of creating driver objects is no longer supported. To create drivers, you now need to use the new package management features provided in Designer.

## 4.1.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer. You can upgrade any package that is installed if there is a newer version of the package available. Before creating a driver object in Designer, it is recommended to have the latest packages in the Package Catalog. Designer prompts you for importing the required packages when it creates the driver object. For more information on upgrading packages, see "[Upgrading Installed Packages](../../../identity-manager-48/designer_admin/data/packman.html#packmanupgrade)" in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).

To verify that you have the most recent version of the driver packages imported into the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   Click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.

   ![](../graphics/package_import_a.png)

   In the Select Package window, browse to the installation folder and select Bidirectional eDirectory driver packages. These packages are added to the list of packages for this driver.
6. Click Select All to import all of the packages displayed.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, restart Designer.

   Continue with [Installing the Driver Packages](creating-the-driver-object-in-designer.html#brn9cu1).

## 4.1.2 Installing the Driver Packages

After you import the current driver packages into the Package Catalog, you can install the driver packages to create a new driver.

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then click New > Driver.
3. Select eDir2eDir Base, then click Next.
4. Select the optional packages to install for the Bidirectional eDirectory driver. All options are selected by default. The options are:

   *Default Configuration:*
   These packages contain the default configuration information for the Bidirectional eDirectory driver. Always leave this option selected.

   *Entitlements:*
   These packages contain the policies and entitlements required to enable the driver for account creation and management with entitlements. For more information, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

   *Password Synchronization:*
   These packages contain the policies required to enable password synchronization. Leave this option selected if you want to synchronize passwords between the Identity Vault and the eDirectory server.

   *Data Collection:*
   These packages contain the policies that enable the driver to collect data for reports. If you are using Identity Reporting, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

   *Account Tracking:*
   These packages contain the policies that enable account tracking information for reports. If you are using Identity Reporting, verify that this option is selected. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).
5. After selecting the optional packages, click Next.
6. If there is a package dependency, install the dependent package. For example, Password Synchronization Notification Packages.
7. (Conditional) Click OK to install the Common Settings package and the edir2eDir Default Configuration package, if you have not installed any other packages into the selected driver set.
8. (Conditional) Fill in the following fields on the Common Settings page, then click Next:

   The Common Settings page is displayed only if the Common Settings package is installed as a dependency.

   *User Container:*
   Select the container where the users are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set. It is in slash format, such as netiq/users, where ou=users.o=netiq.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.

   *Group Container:*
   Select the container where the groups are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   If you want a unique location for this driver, set the value for all drivers on this page. After the driver is created, change the value on the driver’s Global Configuration Values page.
9. On the Driver Information page, specify a name for the driver, then click Next.
10. On the Application Authentication page, fill in the following fields, then click Next:

    *Authentication ID:*
    Specify the DN of the LDAP account in full LDAP DN format that the driver will use to authenticate to connected eDirectory.

    For information, see [Section 6.0, Configuring SSL Connections](configuring-ssl-connections.html).

    *Connection Information:*
    Specify the hostname or IP address of the eDirectory server as well as the decimal port number (for example, 187.168.1.1:389).

    Port 389 uses the TLS protocol for clear text transfer and port 636 uses the SSL protocol. For more information, see [Section 6.0, Configuring SSL Connections](configuring-ssl-connections.html).

    *Password:*
    Specify the password for the LDAP account that the driver will use to authenticate to connected eDirectory.

    *Use SSL:*
    Select Yes to use SSL to secure communication between the Bidirectional eDirectory driver and the eDirectory server. If you use SSL, fill in the following parameters:

    * *Always Accept Server Certificate:*
      Select Yes for the driver to accept the LDAP server's certificate for establishing the SSL connection with the eDirectory server. To use the keystore, select this option to No. For more information on setting up SSL connections, see [Section 6.0, Configuring SSL Connections](configuring-ssl-connections.html).
    * *Keystore Path for SSL Certs:*
      Specify the full path to the keystore file containing the SSL certificates.
    * *Use Mutual Authentication:*
      Select Yes if you want the driver to use SSL mutual authentication (both client and server), or select No for server authentication only. If you select Yes, you must have the appropriate certificates configured in your keystore.
    * *Key Alias:*
      Specify the alias of the key.
    * *Keystore Password:*
      Specify the keystore password for accessing the keystore file containing the SSL certificates.

    *eDirectory Base Container:*
    Specify the connected eDirectory container in LDAP format where objects are synchronized. If you are using a flat Placement rule, this is the container where the objects are placed. If you are using a mirrored Placement rule, this is the base container. For example, ou=people,o=com.

    *NOTE:*If you are using Identity Tracking with the driver, NetIQ recommends that you have a unique organization name (O) between the remote eDirectory tree and the Identity Vault. If it is not done and the trees are not mirrored, events might be reported for an unrelated object in the connected system (eDirectory tree) with the same DN.
11. On the Remote Loader page, do not fill any fields. Click Next.

    *NOTE:*The Bidirectional eDirectory driver does not support the Remote Loader. This option does not apply.
12. (Conditional) Fill in the following fields to define your connected eDirectory system, then click Next:

    This page is displayed only if you selected to install the Data Collection and Account Tracking packages.

    *Name:*
    Specify a descriptive name for this connected eDirectory system. The name is displayed in the reports.

    *Description:*
    Specify a brief description of the connected eDirectory system. The description is displayed in the reports.

    *Location:*
    Specify the physical location of the connected eDirectory system. The location is displayed in the reports.

    *Vendor:*
    Select NetIQ as the vendor of the connected eDirectory system. The vendor information is displayed in the reports.

    *Version:*
    Specify the version of the connected eDirectory system. The version is displayed in the reports.
13. (Conditional) Fill in the following fields to define the ownership of the connected eDirectory system, then click Next:

    This page is displayed only if you selected to install the Data Collection and Account Tracking packages.

    *Business Owner:*
    Select a user object in the Identity Vault that is the business owner of the connected eDirectory system. This can only be a user object, not a role, group, or container.

    *Application Owner:*
    Select a user object in the Identity Vault that is the application owner of the connected eDirectory system. This can only be a user object, not a role, group, or container.
14. (Conditional) Fill in the following fields to define the classification of the connected eDirectory system, then click Next:

    This page is displayed only if you selected to install the Data Collection and Account Tracking packages.

    *Classification:*
    Select the classification of the connected eDirectory system. This information is displayed in the reports. The options are:

    * Mission-Critical
    * Vital
    * Not-Critical
    * Other

      If you select Other, you must specify a custom classification for the Identity Vault.

    *Environment:*
    Select the type of environment the connected eDirectory system provides. The options are:

    * Development
    * Test
    * Staging
    * Production
    * Other

      If you select Other, you must specify a custom classification for the connected eDirectory system.
15. Fill in the following fields on the bidirectional eDirectory Default Configuration page, then click Next:

    *Publisher Placement type:*
    Select the desired form of placement for the Publisher channel. This option determines the Publisher Channel Placement policies. The options are:

    * *Mirrored:*
      Mirrors the structure between the Identity Vault and eDirectory.

      This option in the driver configuration synchronizes User, Group, Organization, Country, and Organizational Unit objects.
    * *Flat:*
      All of the objects are placed into a single (base) container.

      This option synchronizes User, Group, Organization, and Organizational Unit objects.

    *Subscriber Channel Placement Type:*
    Select the desired form of placement for the Subscriber channel. This option determines the Subscriber Channel Placement policies. The options are:

    * *Mirrored:*
      Mirrors the structure between the Identity Vault and the connected eDirectory server. It places objects hierarchically within the base container.

      This option in the driver configuration synchronizes User, Group, Organization, Country, and Organizational Unit objects.
    * *Flat:*
      All of the objects are placed within the base container.

      This option synchronizes User, Group, Organization, and Organizational Unit objects.
16. On the Password Sync Settings page, specify a password for the user, then click Next.

    This option in the driver configuration assumes a default password if you don’t specify the password for the user.
17. (Conditional) On the Account Tracking page, specify the name of the realm which uniquely identifies the location of the users in the connected eDirectory.
18. Review the summary of tasks, then click Finish.
19. After the driver packages are installed, there is additional configuration required for the Bidirectional eDirectory driver. Continue to [Configuring the Driver Object](creating-the-driver-object-in-designer.html#bfveihb) to configure the driver.

## 4.1.3 Configuring the Driver Object

The Bidirectional eDirectory driver is operational after the driver packages are installed. However, the basic configuration might not meet the requirements for your environment. You should complete the following tasks to configure the driver object:

* *Secure the driver connection:*
  The Bidirectional eDirectory driver communicates through LDAP protocols via SSL, using digital certificates for authentication. You need to set up this secure connection. See [Section 6.0, Configuring SSL Connections](configuring-ssl-connections.html).
* *Configure the driver filter:*
  Modify the driver filter to include the object classes and attributes you want synchronized between the eDirectory connected system and the Identity Vault. For information about the classes and attributes included in the filter for the basic configuration, see [Section B.0, Synchronized Attributes](synchronized-attributes.html).
* *Configure policies:*
  Modify the policies as needed for your driver.
* *Configure password synchronization:*
  The basic driver configuration is set up to support bidirectional password synchronization through Universal Password and NDS password. By default, Universal Password is configured. For more information, see [Section 7.0, Synchronizing Passwords](synchronizing-passwords.html).

After completing the configuration tasks, continue with the next section, [Deploying, Starting and Activating the Driver](t4d0rxs1iuyr.html).
