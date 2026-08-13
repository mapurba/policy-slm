# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The eDirectory driver includes several GCVs that are created from information supplied during importing the driver configuration file (see [Section 3.0, Creating a New Driver Object](creating-a-new-driver-object.html)) and one that is not.

The driver also includes the GCVs that are used with password synchronization. In Designer, you must click the ![](../graphics/designer_edit_pass_sync_n.png) icon next to a password synchronization GCV to edit it. This displays the Password Synchronization Options dialog box that has a better view of the relationship between the different settings. In Identity Console, navigate to Configuration > Global Configuration Values and edit the password synchronization settings in your password synchronization policy tab.

You can add your own GCVs if you discover you need additional ones as you implement policies in the driver.

To access the driver’s GCVs in Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Locate the driver icon, then click the driver icon to display the driver’s properties page.
4. Click Global Config Values drop down to display the GCV page.

To access the driver’s GCVs in Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select Properties > Global Configuration Values.

   or

   To add a GCV to the driver set, right-click the driver set icon ![](../graphics/driver_set_icon_n.png), then click Properties > GCVs.

The Global Configuration Values are divided into categories:

* [Default Configuration](global-configuration-values.html#bry2spn)
* [Entitlements](global-configuration-values.html#brv3kfj)
* [Password Synchronization](global-configuration-values.html#bry2uzm)
* [Account Tracking](global-configuration-values.html#brneb9i)
* [Managed System Information](global-configuration-values.html#brnebcn)

## A.2.1 Default Configuration

The following GCVs define control the default configuration of the eDirectory driver:

*eDirectory Publisher Placement type:*
Controls how the objects are placed in the remote Identity Vault and the local Identity Vault. The options are:

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

## A.2.2 Entitlements

There are multiple sections in the Entitlements tab. Depending on which packages you installed, different options are enabled or displayed.

* [Entitlements](global-configuration-values.html#brv3ws0)
* [Data Collection](global-configuration-values.html#brnumyf)
* [Role Mapping](global-configuration-values.html#brnupu2)
* [Resource Mapping](global-configuration-values.html#brnv29g)
* [Parameter Format](global-configuration-values.html#b10rtgx9)
* [Entitlement Extensions](global-configuration-values.html#brnvxvn)

### Entitlements

For more information about entitlements, see [Entitlements](driver-features.html#entitlements).

*Use Entitlements to control eDirectory Accounts:*
Select True to enable the driver to manage user accounts based on the driver’s defined entitlements. Select False to disable management of user accounts based on the entitlements.

*Enable Login Disabled attribute sync:*
Select True if the changes made to the loginDisabled attribute in the Identity Vault should be synced even if the User Account entitlement (Account) is enabled.

*Account action on Entitlement Revoke:*
Select the action to take when a user account entitlement is revoked. The options are Disable User, Do Nothing, or Delete User. By default, Disable User is selected.

*Use Group Entitlement:*
Select True to enable the driver to manage user groups based on the driver’s defined entitlements.

Select False to disable management of group membership based on the entitlements.

*Advanced Settings:*
Select show to display the entitlement options that allow or deny additional functionality like data collection and others. These settings should rarely be changed.

*NOTE:*The eDirectory driver is installed and configured in two trees. You should only install the entitlement package in one of the trees.

### Data Collection

Data collection enables the Identity Report Module to gather information to generate reports. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable data collection:*
Select Yes to enable data collection for the driver through the Data Collection Service by the Managed System Gateway driver. If you are not going to run reports on data collected by this driver, select No.

*Allow data collection from user accounts:*
Select Yes to allow data collection by the Data Collection Service through the Managed System Gateway driver for the user accounts.

*Allow data collection from groups:*
Select Yes to allow data collection by the Data Collection Service through the Managed System Gateway driver for groups.

### Role Mapping

The Role Mapping Administrator allows you to map business roles with IT roles.

*Enable role mapping:*
Select Yes to make this driver visible to the Role Mapping Administrator.

*Allow mapping of user accounts:*
Select Yes if you want to allow mapping of user accounts in the Role Mapping Administrator. An account is required before a role, profile, or license can be granted through the Role Mapping Administrator.

*Allow mapping of groups:*
Select Yes if you want to allow mapping of groups in the Role Mapping Administrator.

### Resource Mapping

The Roles Based Provisioning Module allows you to map resources to users. For more information, see the [NetIQ Identity Manager - User’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_user/data/netiq-identity-manager-user-guide.html#netiq-identity-manager-user-guide).

*Enables resource mapping:*
Select Yes to make this driver visible to the Roles Based Provisioning Module.

*Allow mapping of user accounts:*
Select Yes if you want to allow mapping of user accounts in the Roles Based Provisioning Module. An account is required before a role, profile, or license can be granted.

*Allow mapping of groups:*
Select Yes if you want to allow mapping of groups in the Roles Based Provisioning Module.

### Parameter Format

*Format for Account entitlement:*
Select the parameter format the entitlement agent must use. The options are Identity Manager 4 or Legacy.

*Format for Group entitlement:*
Select the parameter format the entitlement agent must use. The options are Identity Manager 4 or Legacy.

### Entitlement Extensions

*User account extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

*Group extensions:*
The content of this field is added below the entitlement element in the EntitlementConfiguration resource object.

*Exchange mailbox extensions:*
The content of this field is added below the entitlement element in the EntitlementConfiguration resource object.

## A.2.3 Password Synchronization

The following GCVs control password synchronization for the eDirectory driver. For more information, see the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

In Designer, you must click the ![](../graphics/designer_edit_pass_sync_n.png) icon next to a GCV to edit it. This displays the Password Synchronization Options dialog box for a better view of the relationship between the different GCVs.

In Identity Console, to edit the Password management options go to Configuration > Global Configuration Values, and then edit it in your Password synchronization policy tab.

*Connected System Name or Driver Name:*
Specify the name of the driver. The e-mail notification template uses this value to identify the source of the notification message.

*Application accepts passwords from Identity Manager:*
If True, allows passwords to flow from the Identity Manager data store to the connected system.

*Identity Manager accepts passwords from application:*
If True, allows passwords to flow from the connected system to Identity Manager.

*Publish passwords to NDS password:*
Use the password from the connected system to set the non-reversible NDS password in eDirectory.

*Publish passwords to Distribution Password:*
Use the password from the connected system to set the NMAS Distribution Password used for Identity Manager password synchronization.

*Require password policy validation before publishing passwords:*
If True, applies NMAS password policies during publish password operations. The password is not written to the data store if it does not comply.

*Reset user’s external system password to the Identity Manager password on failure:*
If True, on a publish Distribution Password failure, attempt to reset the password in the connected system by using the Distribution Password from the Identity Manager data store.

*Notify the user of password synchronization failure via e-mail:*
If True, notify the user by e-mail of any password synchronization failures.

## A.2.4 Account Tracking

Account tracking is part of the Identity Reporting Module. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable account tracking:*
If this option is set to True, it enables account tracking policies. Set it to False if you do not want to execute account tracking policies.

*Realm:*
Specifies the name of the realm, security domain, or namespace in which the account name is unique.

*Object Class:*
Specifies the object class to track. Class names must be in the application namespace.

*Identifiers:*
Specifies the account identifier attributes. Attribute names must be in the application namespace.

*Status attribute:*
Specifies the name of the attribute in the application namespace to represent the account status.

*Status active value:*
Specifies the value of the status attribute that represents an active state.

*Status inactive value:*
Specifies the value of the status attribute that represents an inactive state.

*Subscription default status:*
Specifies the default status the policies assume when an object is subscribed to the application and the status attribute is not set in the Identity Vault.

*Publication default status:*
Specifies the default status the policies assume when an object is published to the Identity Vault and the status attribute is not set in the application.

## A.2.5 Managed System Information

These settings help the Identity Reporting Module function to generate reports. There are different sections in the Managed System Information tab.

* [General Information](global-configuration-values.html#brnwucf)
* [System Ownership](global-configuration-values.html#brnwwph)
* [System Classification](global-configuration-values.html#brnwxtq)
* [Connection and Miscellaneous Information](global-configuration-values.html#brnx41r)

### General Information

*Name:*
Specifies a descriptive name for this Identity Vault. This name is displayed in the reports.

*Description:*
Specifies a brief description of this Identity Vault. This description is displayed in the reports.

*Location:*
Specifies the physical location of this Identity Vault. This location is displayed in the reports.

*Vendor:*
Specifies NetIQ as the vendor of the Identity Vault. This information is displayed in the reports.

*Version:*
Specifies the version of this Identity Vault. This version information is displayed in the reports.

### System Ownership

*Business Owner:*
Browse to and select the business owner in the Identity Vault for this Identity Vault. You must select a user object, not a role, group, or container.

*Application Owner:*
Browse to and select the application owner in the Identity Vault for this Identity Vault. You must select a user object, not a role, group, or container.

### System Classification

*Classification:*
Specifies the classification of the Identity Vault. This information is displayed in the reports. The options are:

* Mission-Critical
* Vital
* Not-Critical
* Other

  If you select Other, you must specify a custom classification for the Identity Vault.

*Environment:*
Specifies the type of environment the Identity Vault provides. The options are:

* Development
* Test
* Staging
* Production
* Other

  If you select Other, you must specify a custom classification for the Identity Vault.

### Connection and Miscellaneous Information

*Connection and miscellaneous information:*
This options is always set to hide, so that you don’t make changes to these options. These options are system options that are necessary for reporting to work. If you make any changes, reporting stops working.
