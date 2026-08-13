# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The SAP Portal driver includes several predefined GCVs. You can also add your own if you need additional ones as you implement policies in the driver.

To access the driver’s GCVs in Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.

   1. Select the Configuration tab.
   2. Expand the Global Config Values section.

To access the driver’s GCVs in Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select Properties > Global Configuration Values.

   or

   To add a GCV to the driver set, right-clickthe driver set icon ![](../graphics/driver_set_icon_n.png), then click Properties > GCVs.

The Global Configuration Values are divided into categories:

* [Entitlements](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#using-entitlement-gcvs-with-identity-manager-sap-portal-driver)
* [Account Tracking](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#using-account-tracking-gcvs-with-identity-manager-sap-portal-driver)
* [Process Logging](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#using-process-logging-gcvs-with-identity-manager-sap-portal-driver)
* [Managed System Information](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#using-managed-system-gcvs-with-identity-manager-sap-portal-driver)
* [SAP Portal Driver](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#gvcs-defined-for-identity-manager-sap-portal-driver)

## A.2.1 Entitlements

There are multiple sections in the Entitlements tab. Depending on which packages you installed, different options are enabled and displayed. This section documents all of the options.

* [Entitlements Options](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#using-entitlement-gcv-settings-with-identity-manager-sap-portal-driver)
* [Data Collection](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#using-data-collection-gcv-settings-with-identity-manager-sap-portal-driver)
* [Role Mapping](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#using-role-mapping-gcv-settings-with-identity-manager-sap-portal-driver)
* [Resource Mapping](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#using-resource-mapping-gcv-settings-with-identity-manager-sap-portal-driver)
* [Parameter Format](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#parameter-format-of-entitlements-for-identity-manager-sap-portal-driver)
* [Entitlement Extensions](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#entitlement-extension-of-identity-manager-sap-portal-driver)

### Entitlements Options

Entitlements act like an ON/OFF switch to control account access. For more information about entitlements, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

*Show entitlements configuration:*
Select show to display the configuration options for the entitlements.

*Use User Account Entitlement:*
Entitlements act like an on/off switch to control access. When the driver is enabled for entitlements, accounts are created and removed or disabled only when the account entitlement is granted to or revoked from users.

Select True to enable the user account entitlement. You must have an entitlement agent configured in your environment.

*Action when account entitlement revoked:*
Specifies which action is taken in the SAP system when a User Account Entitlement is revoked. The options are to disable the account or to delete the account.

*Use Portal Role Entitlement:*
Enables the Portal Role entitlement that is included with the driver. Select True to enable this entitlement.

*Use Portal Group Entitlement:*
Enables the Portal Group entitlement that is included with the driver. Select True to enable this entitlement.

*Advanced settings:*
Select show to display all of the advanced settings. The advanced settings enable additional functionality in the driver such as data collection or enabling the driver to work with Catalog Administrator. If you change these settings from the default, you risk disabling the additional functionality.

### Data Collection

Data collection enables Identity Reporting to gather information to generate reports. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable data collection:*
Select Yes to enable data collection for the driver through Data Collection Service by the Managed System Gateway driver. If you are not going to run reports on data collected by this driver, select No.

*Allow data collection from user accounts:*
Select Yes to allow data collection by Data Collection Service through the Managed System Gateway driver for the user accounts.

*Allow data collection from groups:*
Select Yes to allow data collection by Data Collection Service through the Managed System Gateway driver for groups.

*Allow data collection from roles:*
Select Yes to allow data collection by Data Collection Service through the Managed System Gateway driver for roles.

### Role Mapping

Identity Applications allow you to map business roles with IT roles. For more information, see the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_admin/data/bookinfo.html#bookinfo).

*Enable role mapping:*
If Yes, this driver is visible to Identity Applications.

*Allow mapping of user accounts:*
If Yes, allows mapping of user accounts in Identity Applications. An account is required before a role, profile, or license can be granted through Identity Applications.

*Allow mapping of groups:*
If Yes, allows mapping of groups in Identity Applications.

*Allow mapping of roles:*
If Yes, allows mapping of roles in Identity Applications.

### Resource Mapping

Identity Applications allow you to map resources to users. For more information, see the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_admin/data/bookinfo.html#bookinfo).

*Enables resource mapping:*
If Yes, this driver is visible to Identity Applications.

*Allow mapping of user accounts:*
If Yes, allows mapping of user accounts in Identity Applications. An account is required before a role, profile, or license can be granted.

*Allow mapping of groups:*
If Yes, allow mapping of groups in Identity Applications.

*Allow mapping of roles:*
If Yes, allows mapping of roles in Identity Applications.

### Parameter Format

*Format for User Account entitlement:*
Specifies the parameter format that the entitlement agent must use when granting this entitlement. The options are Identity Manager 4 or Legacy.

*Format for Role entitlement:*
Specifies the parameter format that the entitlement agent must use when granting this entitlement. The options are Identity Manager 4 or Legacy.

*Format for Group entitlement:*
Specifies the parameter format that the entitlement agent must use when granting this entitlement. The options are Identity Manager 4 or Legacy.

### Entitlement Extensions

*User account extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguraiton resource object.

*Group extensions:*
The content of this field is added below the entitlement element in the EntitlementConfiguration resource object.

*Role extensions:*
The content of this field is added below the entitlement element in the EntitlementConfiguration resource object.

## A.2.2 Account Tracking

Account tracking is part of the Identity Reporting Module. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Show Account Tracking Configuration:*
Select show to display the account tracking settings. If you changes these settings from the default, you risk disabling the account tracking feature.

*Enable Account Tracking:*
If True, it enables account tracking policies. Set it to False if you do not want to execute account tracking policies.

*Realm:*
Specifies the name of the realm, security domain, or namespace in which the account name is unique.

*Object Class:*
Adds the object class to track. Class names must be in the application namespace.

*Identifiers:*
Adds the account identifier attributes. Attribute names must be in the application namespace.

*Status attribute:*
Is the name of the attribute in the application namespace to represent the account status.

*Status active value:*
Is the value of the status attribute that represents an active state.

*Status inactive value:*
Is the value of the status attribute that represents an inactive state.

*Subscription default status:*
Specifies the default status that the policies assume when an object is subscribed to the application and the status attribute is not set in the Identity Vault.

*Publication default status:*
Specifies the default status that the policies assume when an object is published to the Identity Vault and the status attribute is not set in the application.

## A.2.3 Process Logging

These GCVS enable the policies for creating a daily, rolling log file of SAP Business Operations.

*Show Process Logging Options:*
Select show to display the options to configure a rolling log file of the SAP Business Operations.

*Enable process logging:*
If true, it enables process logging, then fill in the following fields:

* *Daily log file:*
  Select true to creating the daily log file with the format of <YYYYmmDD>-<driver-name>-<drv.proclog.logfile>.
* *Log file name:*
  Specify the process log file name.
* *Log file directory:*
  Specify the directory where the log file is created.

## A.2.4 Managed System Information

These settings help Identity Reporting to generate reports. There are different sections in the Managed System Information tab.

* [General Information](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#managed-system-general-information-gcv-setting-for-identity-manager-sap-portal-driver)
* [System Owner](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#managed-system-system-owner-gcv-setting-for-identity-manager-sap-portal-driver)
* [System Classification](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#managed-system-system-classification-gcv-setting-for-identity-manager-sap-portal-driver)
* [Connection and Miscellaneous Information](using-global-configuration-values-with-identity-manager-sap-portal-driver.html#managed-system-connection-and-miscellaneous-info-gcv-setting-for-identity-manager-sap-portal-driver)

### General Information

*Name:*
Specifies a descriptive name for this SAP system. This name is displayed in the reports.

*Description:*
Specifies a brief description of this SAP system. This description is displayed in the reports.

*Location:*
Specifies the physical location of this SAP system. This location is displayed in the reports.

*Vendor:*
Specifies SAP as the vendor of the SAP system. This information is displayed in the reports.

*Version:*
Specifies the version of this SAP system. This version information is displayed in the reports.

### System Owner

*Business Owner:*
Specifies the business owner in the Identity Vault for this SAP system. Ensure that you select a user object. You must not select a role, group, or container.

*Application Owner:*
Specifies the application owner in the Identity Vault for this SAP system. Ensure that you select a user object. You must not select a role, group, or container.

### System Classification

*Classification:*
Select the classification of the SAP system. This information is displayed in the reports. The options are:

* Mission-Critical
* Vital
* Not-Critical
* Other

  If you select Other, you must specify a custom classification for the SAP system.

*Environment:*
Select the type of environment the SAP system provides. The options are:

* Development
* Test
* Staging
* Production
* Other

  If you select Other, you must specify a custom classification for the SAP system.

### Connection and Miscellaneous Information

*Connection and miscellaneous information:*
This options is always set to hide, so that you don’t make changes to these options. These options are system options that are necessary for reporting to work. If you make any changes, reporting stops working.

## A.2.5 SAP Portal Driver

At this time, there are no defined GCVs specified for the SAP Portal driver.
