# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The Oracle User Management driver includes several predefined GCVs. You can also add your own if you discover you need additional ones as you implement policies in the driver.

To access the driver’s GCVs in Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.

   1. Select the Configuration tab.
   2. Expand the Global Config Values section.

To add a GCV to the driver set:

1. On the Driver Dashboard, click the upper right corner of the driver set to display the Action menu.
2. Select Driver Set Properties.
3. On the Driver Set Configuration tab, expand the Global Config Values section.
4. Save the values.

To access the driver’s GCVs in Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select Properties > Global Configuration Values.

   or

   To add a GCV to the driver set, right-click the driver set icon ![](../graphics/driver_set_icon_n.png), then click Properties > GCVs.

The GCVs are divided into the following categories:

* [Password Synchronization](global-configuration-values.html#brv3kjy)
* [(Conditional) Default Configuration](global-configuration-values.html#b16xine8)
* [Entitlements](global-configuration-values.html#b14xgpuw)
* [Account Tracking](global-configuration-values.html#b14xgpux)
* [Managed System Information](global-configuration-values.html#b14xgpuy)

*IMPORTANT:*The HR driver synchronizes employee information; therefore, Account Tracking and Password Synchronization GCVs do not apply to this driver.

## A.2.1 Password Synchronization

These GCVs enable password synchronization between the Identity Vault and the Oracle EBS system.

In Designer, you must click the ![](../graphics/designer_edit_pass_sync_n.png) icon next to a GCV to edit it. This displays the Password Synchronization Options dialog box for a better view of the relationship between the different GCVs.

In Identity Console, to edit the Password management options, follow the steps given below:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.
3. Select the Configuration tab.
4. Expand the Global Config Values section.
5. Select the Password Synchronization tab.

For more information about how to use the Password Management GCVs, see "[Configuring Password Flow](../../../identity-manager-48/password_management/data/configuring-password-flow.html#configuring-password-flow)" in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

*Oracle EBS User's Default password:*
Specify the default password for the Oracle EBS users. The minimum length of the password should be more than 5 characters. If the user password is empty or contains less than 5 characters, the default password is set.

*Application accepts passwords from Identity Manager:*
If True, allows passwords to flow from the Identity Manager data store to the Oracle EBS system.

*Identity Manager accepts passwords from application:*
If True, allows passwords to flow from the Oracle EBS system to the Identity Manager.

*Publish passwords to NDS password:*
Use the password from the Oracle EBS system to set the non-reversible NDS password in the Identity Vault.

*Publish passwords to Distribution Password:*
Use the password from the Oracle EBS system to set the NMAS Distribution Password used for Identity Manager password synchronization.

*Require password policy validation before publishing passwords:*
If True, applies NMAS password policies during publish password operations. The password is not written to the data store if it does not comply.

*Reset user’s external system password to the Identity Manager password on failure:*
If True, on a publish Distribution Password failure, attempt to reset the password in the Oracle EBS system by using the Distribution Password from the Identity Manager data store.

*Notify the user of password synchronization failure via e-mail:*
If True, notify the user by e-mail of any password synchronization failures.

## A.2.2 (Conditional) Default Configuration

*Set Oracle EBS HR As Authoritative Data Source:*
Select True if you don’t want to synchronize add and delete operations on the Subscriber channel. All other operations including modify are synchronized. By default, False is selected.

## A.2.3 Entitlements

There are multiple sections in the Entitlements tab. Depending on which packages you installed, different options are enabled or displayed.

* [Entitlements Options for User Management and TCA Drivers](global-configuration-values.html#brv3ws0)
* [Data Collection Options for User Management and TCA Drivers](global-configuration-values.html#brnumyf)
* [Role Mapping Options for User Management and TCA Drivers](global-configuration-values.html#brnupu2)
* [Resource Mapping Options for User Management and TCA Drivers](global-configuration-values.html#brnv29g)
* [Entitlements Options for the HR Driver](global-configuration-values.html#b16xkhbe)
* [Data Collection Options for the HR Driver](global-configuration-values.html#b16xkq8j)
* [Role Mapping Options for the HR Driver](global-configuration-values.html#b16xkq8m)
* [Resource Mapping Options for the HR Driver](global-configuration-values.html#b16xkq8r)
* [Entitlement Extensions](global-configuration-values.html#brnvxvn)

### Entitlements Options for User Management and TCA Drivers

*(User Management and TCA drivers) Use User Account Entitlement:*
Select True to enable the driver to manage user accounts based on the driver’s defined entitlements. Select False to disable management of user accounts based on the entitlements.

* *Enable Login Disabled Attribute Sync:*
  Select Yes if the changes made to the LoginDisabled attribute in the Identity Vault should be synchronized even if the User Account entitlement (Account) is enabled.
* *Account Action on Entitlement Revoke?:*
  Select the action to take when a user account entitlement is revoked. The options are Disable User or Do Nothing. By default, Disable User is selected.

*Use Role Entitlement:*
Enables the Role entitlement that is included with the driver. Select True to enable this entitlement.

*Use Responsibility Entitlement:*
Enables the Responsibility entitlement that is included with the driver. Select True to enable this entitlement.

*Advanced Settings:*
Select Show to display the entitlement options that allow or deny additional functionality like data collection and others. These settings should rarely be changed.

### Data Collection Options for User Management and TCA Drivers

Data collection enables the Identity Report Module to gather information to generate reports. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable data collection:*
Select Yes to enable data collection for the driver through the Data Collection Service by the Managed System Gateway driver. If you are not going to run reports on data collected by this driver, select No.

*Allow data collection from user accounts:*
If Yes, it allows data collection by the Data Collection Service for the user accounts.

*Allow data collection from roles:*
If Yes, it allows data collection by the Data Collection Service for roles.

*Allow data collection from resources:*
If Yes, it allows data collection by the Data Collection Service for responsibilities.

### Role Mapping Options for User Management and TCA Drivers

The Identity Manager Catalog Administrator allows you to map business roles with IT roles. For more information, see the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_admin/data/bookinfo.html#bookinfo).

*Enable role mapping:*
If Yes, the driver is visible to Catalog Administrator.

*Allow mapping of user accounts:*
If Yes, it allows mapping of user accounts in Catalog Administrator. An account is required before a role or responsibility can be granted to it through Catalog Administrator.

*Allow mapping of roles:*
If Yes, it allows mapping of groups in Catalog Administrator.

*Allow mapping of responsibilities:*
If Yes, it allows mapping of responsibilities in Catalog Administrator.

### Resource Mapping Options for User Management and TCA Drivers

Identity Applications allow you to map resources to users. For more information, see the [NetIQ Identity Manager - User’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_user/data/netiq-identity-manager-user-guide.html#netiq-identity-manager-user-guide).

*Enables resource mapping:*
If Yes, the driver is visible to Identity Applications.

*Allow mapping of user accounts:*
If Yes, it allows mapping of user accounts in Identity Applications. An account is required before a role or responsibility can be granted to it.

*Allow mapping of roles:*
If Yes, it allows mapping of roles in Identity Applications.

*Allow mapping of responsibilities:*
If Yes, it allows mapping of responsibilities in Identity Applications.

### Entitlements Options for the HR Driver

*Use Employee Entitlements:*
Select True to enable the HR driver to manage employees based on the driver’s defined entitlements. Select False to disable employees based on the entitlements.

* *Action on Employee while Entitlement Revoke?:*
  Select the action to take when an entitlement is revoked for an employee. The options are Delete User or Do Nothing. By default, Delete User is selected.

*Format for Employee entitlement:*
Specifies the parameter format that the entitlement agent uses when granting this entitlement. The options are Identity Manager 4 or Legacy.

### Data Collection Options for the HR Driver

Data collection enables Identity Reporting to gather information to generate reports. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable data collection:*
Select Yes to enable data collection for the driver through Data Collection Service by the Managed System Gateway driver. If you are not going to run reports on data collected by this driver, select No.

*Allow data collection from employees:*
If Yes, it allows data collection by Data Collection Service for employees.

### Role Mapping Options for the HR Driver

Identity Applications allow you to map business roles with IT roles. For more information, see the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_admin/data/bookinfo.html#bookinfo).

*Enable role mapping:*
If Yes, the driver is visible to Identity Applications.

*Allow mapping of employees:*
If Yes, it allows mapping of employees in Identity Applications.

### Resource Mapping Options for the HR Driver

Identity Applications allow you to map resources to employees. For more information, see the [NetIQ Identity Manager - User’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_user/data/netiq-identity-manager-user-guide.html#netiq-identity-manager-user-guide).

*Enables resource mapping:*
If Yes, the driver is visible to Identity Applications.

*Allow mapping of employees:*
If Yes, it allows mapping of employees in Identity Applications.

### Entitlement Extensions

*User account extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

*Role extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

*Resource extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

## A.2.4 Account Tracking

Account tracking is part of Identity Reporting. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable account tracking:*
Set this to True to enable account tracking policies. Set it to False if you do not want to execute account tracking policies.

*Realm:*
Specify the name of the realm, security domain, or namespace in which the account name is unique. You must set the Realm to the Oracle EBS Domain Name.

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

## A.2.5 Managed System Information

These settings help Identity Reporting function to generate reports. There are different sections in the Managed System Information tab.

* [General Information](global-configuration-values.html#brnwucf)
* [System Ownership](global-configuration-values.html#brnwwph)
* [System Classification](global-configuration-values.html#brnwxtq)
* [Connection and Miscellaneous Information](global-configuration-values.html#brnx41r)

### General Information

*Name:*
Specify a descriptive name for the managed system.

*Description:*
Specify a brief description of the managed system.

*Location:*
Specify the physical location of the managed system.

*Vendor:*
Specify Oracle as the vendor of the managed system.

*Version:*
Specify the version of the managed system.

### System Ownership

*Business Owner:*
Browse to and select the business owner in the Identity Vault for the Oracle EBS system. You must select a user object, not a role, group, or container.

*Application Owner:*
Browse to and select the application owner in the Identity Vault for the Oracle EBS system. You must select a user object, not a role, group, or container.

### System Classification

*Classification:*
Select the classification of the Oracle EBS system. This information is displayed in the reports. The options are:

* Mission-Critical
* Vital
* Not-Critical
* Other

  If you select Other, you must specify a custom classification for the Oracle EBS system.

*Environment:*
Select the type of environment the Oracle EBS system provides. The options are:

* Development
* Test
* Staging
* Production
* Other

  If you select Other, you must specify a custom classification for the Oracle EBS system

### Connection and Miscellaneous Information

*Connection and miscellaneous information:*
This set of options is always set to hide, so that you don’t make changes to these options. These options are system options that are necessary for reporting to work.
