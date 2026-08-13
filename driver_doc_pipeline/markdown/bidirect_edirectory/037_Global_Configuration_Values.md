# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The Bidirectional eDirectory driver includes several GCVs that are created from information supplied during importing the driver configuration file (see [Section 4.0, Creating a New Driver Object](creating-a-new-driver-object.html)) and one that is not.

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

The Global Configuration Values are divided into following categories:

* [eDirectory Base Container](global-configuration-values.html#bw8pv4t)
* [Default Configuration](global-configuration-values.html#bry2spn)
* [Password Synchronization](global-configuration-values.html#bry2uzm)
* [Account Tracking](global-configuration-values.html#brneb9i)
* [Entitlements](global-configuration-values.html#brv3kfj)
* [Managed System Information](global-configuration-values.html#brnebcn)

## A.2.1 eDirectory Base Container

The eDirectory Base Container specifies the connected eDirectory container in LDAP format where objects are synchronized. If you are using a Flat Placement rule, this is the container where the objects are placed. If you are using a Mirrored Placement rule, this is the base container. For example, ou=people,o=com.

## A.2.2 Default Configuration

The following GCVs define control the default configuration of the Bidirectional eDirectory driver:

*Subscriber Channel Placement type:*
Controls how the objects are placed in the base container of the connected eDirectory server. The options are:

* *Mirrored:*
  Mirrors the structure between the Identity Vault and the connected eDirectory server. It places objects hierarchically within the base container.

  This option in the driver configuration synchronizes User, Group, Organization, Country, and Organizational Unit objects.
* *Flat:*
  All of the objects are placed within the base container.

  This option synchronizes User, Group, Organization, and Organizational Unit objects.

*Publisher Channel Placement Type:*
Controls how the objects are placed in the Identity Vault. The options are:

* *Mirrored:*
  Mirrors the structure between the Identity Vault and the connected eDirectory server. It places objects hierarchically within the base container.

  This option in the driver configuration synchronizes User, Group, Organization, Country, and Organizational Unit objects.
* *Flat:*
  All of the objects are placed within the base container.

  This option synchronizes User, Group, Organization, and Organizational Unit objects.

## A.2.3 Password Synchronization

The following GCVs control password synchronization for the Bidirectional eDirectory driver. For more information, see the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

In Designer, you must click the ![](../graphics/designer_edit_pass_sync_n.png) icon next to a GCV to edit it. This displays the Password Synchronization Options dialog box for a better view of the relationship between the different GCVs.

In Identity Console, to edit the Password management options go to Configuration > Global Configuration Values, and then edit it in your Password synchronization policy tab.

*Connected System Name or Driver Name:*
Specify the name of the driver. The e-mail notification template uses this value to identify the source of the notification message.

*Application accepts passwords from Identity Manager:*
If this option is set to True, it allows passwords to flow from the Identity Manager data store to the connected eDirectory server.

*Identity Manager accepts passwords from application:*
If this option is set to True, it allows passwords to flow from the connected system to Identity Manager.

*Publish passwords to NDS password:*
Use the password from the connected system to set the non-reversible NDS password in eDirectory.

*Publish passwords to Distribution Password:*
Use the password from the connected system to set the NMAS Distribution Password used for Identity Manager password synchronization.

*Require password policy validation before publishing passwords:*
If this option is set to True, it applies NMAS password policies during publish password operations. The password is not written to the data store if it does not comply.

*Reset user’s external system password to the Identity Manager password on failure:*
If this option is set to True, and the Distribution Password fails to distribute, attempt to reset the password in the connected system by using the Distribution Password from the Identity Manager data store.

*Notify the user of password synchronization failure via e-mail:*
If this option is set to True, notify the user by e-mail of any password synchronization failures.

## A.2.4 Account Tracking

Account tracking is part of Identity Reporting. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable account tracking:*
Set this to True to enable account tracking policies. Set it to False if you do not want to execute account tracking policies.

*Realm:*
Specify the name of the realm, security domain, or namespace in which the account name is unique.

*Object Class:*
Add the object class to track. Class names must be in the application namespace.

*Identifiers:*
Add the account identifier attributes. Attribute names must be in the application namespace.

*Status attribute:*
Name of the attribute in the application namespace to represent the account status.

*Status active value:*
Value of the status attribute that represents an active state.

*Status inactive value:*
Value of the status attribute that represents an inactive state.

*Subscription default status:*
Select the default status the policies assume when an object is subscribed to the application and the status attribute is not set in the Identity Vault.

*Publication default status:*
Select the default status the policies assume when an object is published to the Identity Vault and the status attribute is not set in the application.

## A.2.5 Entitlements

There are multiple sections in the Entitlements tab. Depending on which packages you installed, different options are enabled or displayed.

* [Entitlements](global-configuration-values.html#brv3ws0)
* [Data Collection](global-configuration-values.html#brnumyf)
* [Role Mapping](global-configuration-values.html#brnupu2)
* [Resource Mapping](global-configuration-values.html#brnv29g)
* [Parameter Format](global-configuration-values.html#b10rtgx9)
* [Entitlement Extensions](global-configuration-values.html#brnvxvn)

### Entitlements

For more information about entitlements, see [Entitlements](standard-driver-features.html#b10rs3g9).

*Use Entitlements to control eDirectory Accounts:*
Select True to enable the driver to manage user accounts based on the driver’s defined entitlements. Select False to disable management of user accounts based on the entitlements.

*Enable Login Disabled attribute sync:*
Select True if the changes made to the LoginDisabled attribute in the Identity Vault should be synced even if the User Account entitlement (Account) is enabled.

*Account action on Entitlement Revoke:*
Select the action to take when a user account entitlement is revoked. The options are Disable User, Do Nothing, or Delete User. By default, Disable User is selected.

*Use Group Entitlement:*
Select True to enable the driver to manage user groups based on the driver’s defined entitlements.

Select False to disable management of group membership based on the entitlements.

*Advanced Settings:*
Select show to display the entitlement options that allow or deny additional functionality like data collection and others. These settings should rarely be changed.

### Data Collection

Data collection enables the Identity Report Module to gather information to generate reports. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable data collection:*
Select Yes to enable data collection for the driver through Data Collection Service by the Managed System Gateway driver. If you are not going to run reports on data collected by this driver, select No.

*Allow data collection from user accounts:*
Select Yes to allow data collection by Data Collection Service through the Managed System Gateway driver for the user accounts.

*Allow data collection from groups:*
Select Yes to allow data collection by Data Collection Service through the Managed System Gateway driver for groups.

### Role Mapping

Identity Applications allows you to map business roles with IT roles.

*Enable role mapping:*
Select Yes to make this driver visible to Identity Applications.

*Allow mapping of user accounts:*
Select Yes if you want to allow mapping of user accounts in Identity Applications. An account is required before a role, profile, or license can be granted through Identity Applications.

*Allow mapping of groups:*
Select Yes if you want to allow mapping of groups in Identity Applications.

### Resource Mapping

Identity Applications allow you to map resources to users. For more information, see the [NetIQ Identity Manager - User’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_user/data/netiq-identity-manager-user-guide.html#netiq-identity-manager-user-guide).

*Enables resource mapping:*
Select Yes to make this driver visible to Identity Applications.

*Allow mapping of user accounts:*
Select Yes if you want to allow mapping of user accounts in Identity Applications. An account is required before a role, profile, or license can be granted.

*Allow mapping of groups:*
Select Yes if you want to allow mapping of groups in Identity Applications.

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

## A.2.6 Managed System Information

These settings help Identity Reporting to generate reports. There are different sections in the Managed System Information tab.

* [General Information](global-configuration-values.html#brnwucf)
* [System Ownership](global-configuration-values.html#brnwwph)
* [System Classification](global-configuration-values.html#brnwxtq)
* [Connection and Miscellaneous Information](global-configuration-values.html#brnx41r)

### General Information

*Name:*
Specify a descriptive name for this connected eDirectory system. This name is displayed in the reports.

*Description:*
Specify a brief description of this connected eDirectory system. This description is displayed in the reports.

*Location:*
Specify the physical location of this connected eDirectory system. This location is displayed in the reports.

*Vendor:*
Select NetIQ as the vendor of the connected eDirectory system. This information is displayed in the reports.

*Version:*
Specify the version of this connected eDirectory system. This version information is displayed in the reports.

### System Ownership

*Business Owner:*
Browse to and select the business owner in the Identity Vault for this connected eDirectory system. You must select a user object, not a role, group, or container.

*Application Owner:*
Browse to and select the application owner in the Identity Vault for this connected eDirectory system. You must select a user object, not a role, group, or container.

### System Classification

*Classification:*
Select the classification of the connected eDirectory system. This information is displayed in the reports. The options are:

* Mission-Critical
* Vital
* Not-Critical
* Other

  If you select Other, you must specify a custom classification for the connected eDirectory system.

*Environment:*
Select the type of environment the connected eDirectory system provides. The options are:

* Development
* Test
* Staging
* Production
* Other

  If you select Other, you must specify a custom classification for the connected eDirectory system.

### Connection and Miscellaneous Information

*Connection and miscellaneous information:*
This options is always set to hide, so that you don’t make changes to these options. These options are system options that are necessary for reporting to work. If you make any changes, reporting stops working.
