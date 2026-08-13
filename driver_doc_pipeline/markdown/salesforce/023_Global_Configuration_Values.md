# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The Salesforce.com driver includes several predefined GCVs. You can also add your own if you discover you need additional ones as you implement policies in the driver.

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

* [Driver Configuration](global-configuration-values.html#bs9xam7)
* [Password Synchronization](global-configuration-values.html#psyncgcv)
* [Entitlements](global-configuration-values.html#ent_gcvsf)
* [Password Generation](global-configuration-values.html#b1545t8t)
* [Account Tracking](global-configuration-values.html#attrgcvsf)
* [Managed System Information](global-configuration-values.html#msg_gcvsf)

## A.2.1 Driver Configuration

The following GCVs control the configuration of the Salesforce.com driver.

*Salesforce.com Default Profile ID:*
This option is used for creating new users when no actual value has been provided in the current transaction.

The ProfileID is a 15 character code that uniquely identifies a user profile tied to your Salesforce account.

To find ProfileID for any given profile in Salesforce, go to Setup > Manage Users > Profiles, click the appropriate profile and select the URL. A standard Salesforce 15 character code displays in the URL. Copy the 15 character code and use it as your Salesforce.com Default Profile ID.

*Default Time Zone:*
Specifies the default time zone for users created in the salesforce.com if time zone is not specified during the initial add event.

In order to add additional locations, edit this GCV option and add additional enumeration values. The value part of the field that this GCV represents is named by using region and key city, according to ISO standards.

*Default E-Mail Encoding:*
This option specifies the e-mail encoding information of the users created in the salesforce.com if e-mail encoding is not provided during the initial add event. In order to add additional e-mail encodings, check with salesforce.com to know the correct value for this field, then edit the option to add additional enumeration values.

*Default Locale:*
This option specifies the default locale information of the users created in the salesforce.com if it is not provided during the initial add event.

In order to add additional locales, edit this option and add additional enumeration values. The value part of the field that this GCV represents is built according to the language, and country if necessary, using two-letter ISO codes.

For example, en\_US. It is built from the 2 letter language code described in the ISO 639-1, followed by an underscore sign, followed by the 2 letter country code described in the ISO 3166-1.

*Default Language:*
Specify the default language of the users created in the salesforce.com if it is not provided during the initial add event.

In order to add additional languages, edit the option and add additional enumeration values. The value part of the field that this GCV represents is built according to the language, and country if necessary, using two-letter ISO codes.

For example, en\_US, built from the 2 letter language code described in the ISO 639-1, followed by an underscore sign, followed by the 2 letter country code described in the ISO 3166-1.

## A.2.2 Password Synchronization

Use the following GCVs to configure the driver to synchronize passwords to the Identity Vault. For more information, see [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

*Connected system name:*
Specify the name of the connected system. This name is used for password sync failure notifications.

*Notify the user of password synchronization failure via e-mail:*
Select this option if you want to notify the salesforce.com user through e-mail.

*Application accepts passwords from Identity Manager:*
Select whether the application accepts passwords from Identity Manager. Selecting this option to True allows the passwords to flow from the Identity Manager data store to connected system.

*Publisher channel password options (not supported by this driver):*
Leave the setting unchanged. The Salesforce.com driver doesn't support password synchronization on the Publisher channel, this option should remain set to false.

## A.2.3 Entitlements

There are multiple sections in the Entitlements tab. Depending on which packages you installed, different options are enabled or displayed.

* [Entitlements Configuration](global-configuration-values.html#brv3ws0)
* [Data Collection](global-configuration-values.html#brnumyf)
* [Role Mapping](global-configuration-values.html#brnupu2)
* [Parameter Format](global-configuration-values.html#b14xjbn1)
* [Resource Mapping](global-configuration-values.html#brnv29g)
* [Entitlement Extensions](global-configuration-values.html#brnvxvn)

### Entitlements Configuration

*Use Entitlements to Control Salesforce Accounts?:*
Select True to enable the driver to manage user accounts based on the driver’s defined entitlements. Select False to disable management of user accounts based on the entitlements.

* *On Revoke?:*
  Select the action to take when a user account entitlement is revoked. There is only one option, Disable User, which is selected by default.

*Use Group Entitlement:*
Enables the Group entitlement that is included with the driver. Select True to enable this entitlement.

*Use Role Entitlement:*
Enables the Role entitlement that is included with the driver. Select True to enable this entitlement.

*Use Permission Set Entitlement:*
Enables the permission set entitlement that is included with the driver. Select True to enable this entitlement.

*Advanced Settings:*
Select Show to display the entitlement options that allow or deny additional functionality like data collection and others. These settings should rarely be changed.

### Data Collection

Data collection enables the Identity Report Module to gather information to generate reports. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable data collection:*
If Yes, it enables the data collection for the driver through Data Collection Service by the Managed System Gateway driver. If you are not going to run reports on data collected by this driver, select No.

*Allow data collection from user accounts:*
If Yes, it allows data collection by Data Collection Service for the user accounts.

*Allow data collection from groups:*
If Yes, it allows data collection by Data Collection Service for the groups.

*Allow data collection from roles:*
If Yes, it allows data collection by Data Collection Service for roles.

*Allow data collection from permission sets:*
If Yes, it allows data collection by Data Collection Service for permission sets.

### Role Mapping

Identity Applications allow you to map business roles with IT roles. For more information, see the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_admin/data/bookinfo.html#bookinfo)

*Enable role mapping:*
If Yes, the driver is visible to Identity Applications.

*Allow mapping of user accounts:*
If Yes, it allows mapping of user accounts in Identity Applications. An account is required before a role or responsibility can be granted to it through Identity Applications.

*Allow mapping of groups:*
If Yes, it allows mapping of groups in Identity Applications.

*Allow mapping of roles:*
If Yes, it allows mapping of groups in Identity Applications.

*Allow mapping of permission sets:*
If Yes, it allows mapping of permission sets in Identity Applications.

### Parameter Format

*Format for Account entitlement:*
Specifies the parameter format that the entitlement agent uses when granting this entitlement. The options are Identity Manager 4 or Legacy.

*Format for Role entitlement:*
Specifies the parameter format that the entitlement agent uses when granting this entitlement. The options are Identity Manager 4 or Legacy.

*Format for Permission Set Entitlement:*
Specifies the parameter format that the entitlement agent uses when granting this entitlement. The options are Identity Manager 4 or Legacy.

*Format for Responsibility entitlement:*
Specifies the parameter format that the entitlement agent uses when granting this entitlement. The options are Identity Manager 4 or Legacy.

### Resource Mapping

Identity Applications allow you to map resources to users. For more information, see the [NetIQ Identity Manager - User’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_user/data/netiq-identity-manager-user-guide.html#netiq-identity-manager-user-guide).

*Enables resource mapping:*
If Yes, the driver is visible to Identity Applications.

*Allow mapping of user accounts:*
If Yes, it allows mapping of user accounts in Identity Applications. An account is required before a role or responsibility can be granted to it.

*Allow mapping of groups:*
If Yes, it allows mapping of groups in Identity Applications.

*Allow mapping of roles:*
If Yes, it allows mapping of roles in Identity Applications.

*Allow mapping of permission sets:*
If Yes, it allows mapping of permission sets in Identity Applications.

### Entitlement Extensions

*User account extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

*Group Extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

*Role Extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

*Permission Set Extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

## A.2.4 Password Generation

*Synchronize Identity Vault Password:*
Set this option to Yes to establish common password synchronization. Change it to No to ignore the Identity Vault password.

*Enable Password Generation Triggers:*
Set this option to Yes to generate password for new accounts.

*New Account:*
If On, the driver generates password for new accounts.

*Account Enable:*
If On, the driver generates a new password every time the account is enabled.

*Account Disable:*
If On, the driver generates a new password every time the account is disabled.

*Password Generation Method:*
If the universal password synchronization or distribution password is not set for a user account, you need to set an initial password for the user. Specify whether to use an attribute of a user account for setting up an initial password or to use a randomly generated password. If the user account is going to use SAML for authentication, select Random for this option. Otherwise, select Attribute Value.

## A.2.5 Account Tracking

Account tracking is part of Identity Reporting. For more information, see the [NetIQ Identity Reporting: User’s Guide to Running Reports](../../../identity-manager-48/report_descriptions/data/bookinfo.html#bookinfo).

*Enable account tracking:*
Set this to True to enable account tracking policies. Set it to False if you do not want to execute account tracking policies.

*Realm:*
Specify the name of the realm, security domain, or namespace in which the account name is unique. You must set the Realm to the Salesforce.com Domain Name.

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

## A.2.6 Managed System Information

These settings help Identity Reporting to generate reports. There are different sections in the Managed System Information tab.

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
Specify Salesforce.com as the vendor of the managed system.

*Version:*
Specify the version of the managed system.

### System Ownership

*Business Owner:*
Browse to and select the business owner in the Identity Vault for the connected application. You must select a user object, not a role, group, or container.

*Application Owner:*
Browse to and select the application owner in the Identity Vault for the connected application. You must select a user object, not a role, group, or container.

### System Classification

*Classification:*
Select the classification of the connected application. This information is displayed in the reports. The options are:

* Mission-Critical
* Vital
* Not-Critical
* Other

  If you select Other, you must specify a custom classification for the connected application.

*Environment:*
Select the type of environment the connected application provides. The options are:

* Development
* Test
* Staging
* Production
* Other

  If you select Other, you must specify a custom classification for the connected application.

### Connection and Miscellaneous Information

*Connection and miscellaneous information:*
This set of options is always set to hide, so that you don’t make changes to these options. These options are system options that are necessary for reporting to work.
