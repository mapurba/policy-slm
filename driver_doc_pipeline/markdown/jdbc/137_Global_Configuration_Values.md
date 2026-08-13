# O.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The REST driver includes several predefined GCVs. You can also add your own if you discover you need additional ones as you implement policies in the driver.

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

   To add a GCV to the driver set, right-clickthe driver set icon ![](../graphics/driver_set_icon_n.png), then click Properties > GCVs.

The global configuration values are organized as follows:

## O.2.1 Global Configuration Values

The following global configuration values are used for database options and base configuration options.

*JDBC connection URL format used:*
Specify the connection URL format used for the JDBC driver to connect to the databases. Use '<HOST>','<PORT> and '<DB>' tokens to specify the location of host's IP address, port and database/SID in the connection URL.

*NOTE:*The tokens are case-sensitive and angle-brackets are mandatory since they are used as delimiters.

If you use the same fan-out driver to connect oracle pluggable database and oracle traditional database, the url template of the databases should be separated using a comma. For example: jdbc:oracle:thin:@<HOST>:<PORT>/<DB>, jdbc:oracle:thin:@<HOST>:<PORT>:<DB>

*Synchronization model:*
Select the synchronization model. The synchronization options are: Direct and Indirect. Direct synchronization uses views to synchronize directly to existing tables of arbitrary structure. Indirect synchronization synchronizes to intermediate staging tables with a particular structure.

*UserName Column:*
Specify the exact column name of the usr table that store the usernames.

## O.2.2 Managed System Information

These settings help Identity Reporting to generate reports. There are different sections in the Managed System Information tab.

* [General Information](how-to-set-gcv-for-jdbc-driver.html#brnwucf)
* [System Ownership](how-to-set-gcv-for-jdbc-driver.html#brnwwph)
* [System Classification](how-to-set-gcv-for-jdbc-driver.html#brnwxtq)
* [Connection and Miscellaneous Information](how-to-set-gcv-for-jdbc-driver.html#brnx41r)
* [JDBC FanOut Instances Information](how-to-set-gcv-for-jdbc-driver.html#b1ibimgt)

### General Information

*Name:*
Specify a descriptive name for the managed system.

*Description:*
Specify a brief description of the managed system.

*Location:*
Specify the physical location of the managed system.

*Vendor:*
Specify Microsoft as the vendor of the managed system.

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

### JDBC FanOut Instances Information

These settings help to configure the Managed System Service related details of each JDBC FanOut instance. To create a new instance, click the plus sign and fill in the following information:

* *JDBC FanOut Instance Name:*
  Specify the descriptive name of the new logical instance of the managed system.
* *Show other configuration values:*
  Select Show to display additional information related to the FanOut instance. For more information, see [Managed System Information](how-to-set-gcv-for-jdbc-driver.html#brnebcn).
* *Connection and miscellaneous information:*
  Select Show to display the system options. The options are:

  + Instance ID
  + Authentication IP Address
  + Authentication Port
  + Authentication ID
  + Database Schema
  + Type

  *NOTE:*The connection information options are auto-generated and always set to hide.

## O.2.3 Entitlements

There are multiple sections in the Entitlements tab. Depending on which packages you installed, different options are enabled or displayed.

* [Entitlements](how-to-set-gcv-for-jdbc-driver.html#b1if56i1)
* [Data Collection](how-to-set-gcv-for-jdbc-driver.html#brnumyf)
* [Role Mapping](how-to-set-gcv-for-jdbc-driver.html#brnupu2)
* [Resource Mapping](how-to-set-gcv-for-jdbc-driver.html#brnv29g)
* [Parameter Format](how-to-set-gcv-for-jdbc-driver.html#b1if5m2e)
* [Entitlements Extensions](how-to-set-gcv-for-jdbc-driver.html#b1if5oh3)

### Entitlements

*Account Entitlement Value:*
Specify the entitlement value to assign for user account during the account creation. Identity Applications display this value to the user during account provisioning.

*Use Entitlements to Control DB Accounts:*
Select True to enable the driver to manage database accounts based on the driver’s defined entitlements. Select False to disable management of database accounts based on the entitlements.

*Use Group Entitlement:*
Select True to enable the driver to manage group membership based on the driver’s defined entitlements.

*Allow Login Disabled in Subscriber Channel:*
Select True to enable the driver to control the flow of Login Disabled attribute in the Subscriber Channel and only on a regular attribute change.

*Advanced Settings:*
Entitlement options that allow or deny additional functionality like data collection, role mapping, resource mapping, parameter format, and entitlement extensions. Leave these settings as default.

### Data Collection

Data collection enables Identity Report to gather information to generate reports. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable data collection:*
Select Yes to enable data collection for the driver through Data Collection Service by the Managed System Gateway driver. If you are not going to run reports on data collected by this driver, select No.

*Allow data collection from user accounts:*
Select Yes to allow data collection by Data Collection Service for the user accounts.

*Allow data collection from groups:*
Select Yes to allow data collection by Data Collection Service for groups.

### Role Mapping

The Identity Manager Identity Applications allows you to map business roles with IT roles. For more information, see [Identity Applications Administration](../../../identity-manager-48/identity_apps_admin/data/t42bq2rlpx68.html#t42bq2rlpx68) in the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_admin/data/bookinfo.html#bookinfo).

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
Specify the parameter format the entitlement agent must use when granting the user account entitlement. The options are Identity Manager 4 and Legacy.

*Format for Group entitlement:*
Specify the parameter format the entitlement agent must use when granting the group entitlement. The options are Identity Manager 4 and Legacy.

### Entitlements Extensions

*User account extension:*
Specify the user account extension. The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object

*Group extensions:*
Specify the group extensions. The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object

## O.2.4 Account Tracking

The following controls the Account tracking is part of Identity Reporting. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable Account Tracking:*
Set this to True to enable account tracking policies for the JDBC Fan-out driver. Set it to False if you do not want to execute account tracking policies.

* Object class
* Realm
* Identifiers for Account
* Status Attribute
* Status active value
* Status inactive value
* Subscription default status
* Publication default status

## O.2.5 Password Synchronization

The following GCVs control password synchronization for the Office 365 driver. For more information, see the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

*Application Accepts Passwords from Identity Manager:*
If this option is set to True, the driver allows passwords to flow from the Identity Manager data store to the connected Office 365 server.

*Identity Manager Accepts Passwords from the Application:*
If this option is set to True, it allows passwords to flow from the connected system to Identity Manager.

*Publish Passwords to NDS Password:*
Use the password from the connected system to set the non-reversible NDS password in the Identity Vault.

*Publish Passwords to Distribution Password:*
Use the password from the connected system to set the NMAS Distribution Password used for Identity Manager password synchronization.

*Require passwords policy validation before publishing passwords:*
Select True to apply NMAS password policies when publishing passwords. Password is not written to the data store if it does not comply.

*Reset user’s external system password to the Identity Manager password on failure:*
If this option is set to True, and the Distribution Password fails to distribute, attempt to reset the password in the connected system by using the Distribution Password from the Identity Manager data store.

*Notify the user of password synchronization failure via e-mail:*
If this option is set to True, notify the user by e-mail of any password synchronization failures.

*Connected System or Driver Name:*
Specifies the name of the connected system, application or Identity Manager driver. This value is used by the e-mail notification templates to identify the source of notification messages.

In Designer, you must click the ![](../graphics/designer_edit_pass_sync_n.png) icon next to a GCV to edit it. This displays the Password Synchronization Options dialog box for a better view of the relationship between the different GCVs.

In Identity Console, to edit the Password management option, follow the steps given below:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.
3. Select the Configuration tab.
4. Expand the Global Config Values section.
5. Select the Password Synchronization tab.

## O.2.6 JDBC Fanout Common

*Allow ‘Group add’ in Fanout mode:*
Select to Disable to prevent the group add/creation events in the Subscriber channel. Group add events are broadcasted to each of the instances configured by the driver. If disabled, group add operations will be vetoed.

*Synchronize the first or the last replica value:*
Select the appropriate option to synchronize the first or last replica value of multi-valued attributes mapped to single-valued columns. The options are: First and Last.
