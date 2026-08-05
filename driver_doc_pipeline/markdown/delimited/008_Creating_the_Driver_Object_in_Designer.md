# 3.2 Creating the Driver Object in Designer

To create a Delimited Text driver object, install the driver packages and then modify the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](create-driver-object-designer.html#brcyw6o)
* [Installing the Driver Packages](create-driver-object-designer.html#delimted-install-driver-packages)
* [Modifying the Driver Settings](create-driver-object-designer.html#modify-driver-settings)
* [Deploying the Driver Object](create-driver-object-designer.html#deploy-driver-object)

## 3.2.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer. You can upgrade any package that is installed if there is a newer version of the package available. It is recommended to have the latest packages in the Package Catalog before creating a new driver object. Designer prompts you for importing the required packages when it creates the driver object. For more information on upgrading packages, see "[Upgrading Installed Packages](../../../identity-manager-48/designer_admin/data/packman.html#packmanupgrade)" in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).

To verify you have the latest packages in the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK if there are no package updates

   or

   Click OK to import the package updates.
4. In the Outline view, right-click the Package Catalog.
5. Click Import Package.
6. Select the Delimited Text packages.

   or

   Click Select All to import all of the packages displayed, then click OK.

   By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
7. Click OK to import the selected packages, then click OK in the successfully imported packages message.
8. After the current packages are imported, continue with [Installing the Driver Packages](create-driver-object-designer.html#delimted-install-driver-packages).

## 3.2.2 Installing the Driver Packages

To install the driver packages:

1. Start Designer and open your project.
2. In the Modeler, right-click the driver set where you want to create your new driver, then select New > Driver.
3. Select Delimited Text Base from the list of base packages, then click Next.
4. Select the optional features to install for the Delimited Text driver.

   All options are selected by default. The options are:

   * *Delimited Text Entitlements:*
     This package contains policies for quick onboarding of custom entitlements and dynamic resource creation. This package also contains GCVs to control the resource mapping. Select this package if you want to enable the entitlement onboarding feature for this driver. For more information, see "[Synchronizing Permission Changes from the Connected Systems](../../../identity-manager-48/driver_admin/data/b1n9nq3m.html#b1n9nq3m)" in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).

     *NOTE:*If you are enabling quick onboarding of custom entitlements functionality, ensure that you upgrade the Managed System Gateway driver version to 4.0.0.6.
   * *Delimited Text Password Synchronization:*
     This package contains GCVs and sample policies for synchronizing passwords.
   * *Delimited Text Managed System Information:*
     This package contains the policies that enable the driver to collect data for reports.

   Note that if the Delimited Text Managed System Information and Password Synchronization packages are not imported into the Package Catalog, only the package ID is displayed for those packages in the list of optional features.
5. Click Next.
6. (Optional) If you want the driver to synchronize passwords, select the Delimited Text Password Synchronization package, then click Next.
7. (Conditional) If not already configured, fill in the following fields on the Common Settings page, then click Next:

   * *User Container:*
     Select the Identity Vault container where users are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set.
   * *Group Container:*
     Select the Identity Vault container where groups are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set.

   *NOTE:*The Common Settings page is only displayed if the Common Settings package is a dependency.
8. (Conditional) If not already configured, fill in the following fields on the Common Settings Advanced Edition page, then click Next:

   * *User Application Provisioning Services URL:*
     Specify the User Application Identity Manager Provisioning URL.
   * *User Application Provisioning Services Administrator:*
     Specify the DN of the User Application Administrator user. This user should have the rights for creating and assigning resources. For more information, see "[Setting Up Administrative User Accounts](../../../identity-manager-48/driver_admin/data/t42erzeaaktr.html#b1845rl6)" in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

   *NOTE:*This page is only displayed if you installed the Common Settings Advanced Edition package.
9. On the Install Delimited Text Base page, specify a name for the driver, then click Next.
10. Fill in the following fields, then click Next:

    * *Input File Path:*
      Specify the path for the input file.
    * *Output File Path:*
      Specify the path for the output file.
11. (Conditional) If you want to use the Remote Loader with this driver, fill in the following fields to configure the driver to connect through the Remote Loader, then click Next. Otherwise, click No, then click Next.

    * *Connect to Remote Loader:*
      By default, the driver is configured to connect through the Remote Loader. If you want to run the driver locally, select no, then click Next. Otherwise, fill in the remaining fields to configure the driver to connect through the Remote Loader.
    * *Host Name:*
      Specify the host name or IP address of the server where the driver’s Remote Loader service is running.
    * *Port:*
      Specify the port number where the Remote Loader is installed and is running for this driver. The default port number is 8090.
    * *Remote Password:*
      Specify the Remote Loader’s password, as defined on the Remote Loader. The Identity Manager server or the Remote Loader shim requires this password to authenticate to the Remote Loader
    * *Driver Password:*
      Specify the driver object password that is defined in the Remote Loader service. The Remote Loader requires this password to authenticate to the Identity Manager server.
12. On the Driver Parameters page, fill in the following fields, then click Next:

    * *Field Delimiter:*
      Specify the character to use to delimit field values in the input and output files. It must be one character. You can also use the tab as the delimiter field value. Tab is represented as {tab}. The default is a comma.
    * *Field Names:*
      Specify a comma-separated list of attribute names that can be referred to in the Schema Mapping rule. The fields of the records included in your input CSV files must correspond to the order and positioning of the names in this list.
13. (Conditional) On the Install Delimited Text Managed System Information page, fill in the following fields to define your Delimited Text system, then click Next:

    *NOTE:*This page is only displayed if you installed the Managed System Information package.

    * *Name:*
      Specify a descriptive name for this Delimited Text system.
    * *Description:*
      Specify a brief description for this Delimited Text system.
    * *Location:*
      Specify the physical location of this Delimited Text system.
    * *Vendor:*
      Leave the setting unchanged.
    * *Version:*
      Specify the version of this Delimited Text system.
14. (Conditional) On the Install Delimited Text Managed System Information page, fill in the following fields to define your Delimited Text system, then click Next:

    *NOTE:*This page is only displayed if you selected to install the Managed System Information package.

    * *Business Owner:*
      Select a user object in the Identity Vault that is the business owner of the Delimited Text system. This can only be a user object, not a role, group, or container.
    * *Application Owner:*
      Select a user object in the Identity Vault that is the application owner of the Delimited Text system. This can only be a user object, not a role, group, or container.
15. (Conditional) On the Install Delimited Text Managed System Information page, fill in the following fields to define your Delimited Text system, then click Next:

    * *Classification:*
      Select the classification of the Delimited Text system. This information is displayed in the reports. Your options are:

      + Mission-Critical
      + Vital
      + Not-Critical
      + Other

        If you select Other, you must specify a custom classification for the Delimited Text driver system.
    * *Environment:*
      Select the type of environment the Delimited Text system provides. The options are:

      + Development
      + Test
      + Staging
      + Production
      + Other

        If you select Other, you must specify a custom classification for the Delimited Text driver system.
16. Review the settings and click Finish to create the driver.
17. Modify the driver settings. Proceed to [Modifying the Driver Settings](create-driver-object-designer.html#modify-driver-settings).

## 3.2.3 Modifying the Driver Settings

There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to review the [Driver Parameters](driver-configuration.html#b94psi3) located on the Driver Configuration page. These settings let you control the format and content of the input and output files.

The driver configuration settings are explained in [Section A.0, Driver Properties](driver-properties.html).

If you do not have the Driver Properties page displayed in Designer:

1. Open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Properties.
3. Click OK when finished.
4. Deploy the driver to the Identity Vault. Proceed to [Deploying the Driver Object](create-driver-object-designer.html#deploy-driver-object).

## 3.2.4 Deploying the Driver Object

To deploy the driver into the Identity Vault,

1. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Live > Deploy.
2. If you are authenticated to the Identity Vault, skip to [Step 3](create-driver-object-designer.html#bfvehvl), otherwise, specify the following information, then click OK.:

   * *Host:*
     Specify the IP address or DNS name of the server hosting the Identity Vault.
   * *Username:*
     Specify the DN of the user object used to authenticate to the Identity Vault.
   * *Password:*
     Specify the user’s password.
3. Read through the deployment summary, then click Deploy.
4. Read the successful message, then click OK.
5. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault and to the input and output directories on the server. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser, for example, and assign security equivalence to that user. For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see “Establishing a Security Equivalent User” in the [Identity Manager Security Guide](https://www.netiq.com/documentation/idm45/idm_security/?page=/documentation/idm45/idm_security/data/front.html).

   For receiving events from the Identity Vault, ensure that the driver’s Security Equals DN has the following rights in the Identity Vault:

   * *Entry:*
     Browse rights.
   * *Attributes:*
     Read rights.

   1. Click Add, browse to and select the object with the correct rights.
   2. Click OK twice.
6. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, browse to and select the user object you want to exclude, then click OK.
   2. Repeat [Step 6.a](create-driver-object-designer.html#bfvehvr) for each object you want to exclude, then click OK.
7. Click OK.

After you have customized the driver for your environment, you must deploy it to the Identity Vault. Proceed to [Deploying the Driver Object](create-driver-object-designer.html#deploy-driver-object).
