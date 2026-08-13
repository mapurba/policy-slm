# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The GroupWise driver includes many GCVs. You can also add your own if you discover you need additional ones as you implement policies in the driver.

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

The global configuration values are organized as follows:

* [Driver Configuration](global-configuration-values.html#bryop82)
* [Entitlements](global-configuration-values.html#brypl3s)
* [Account Tracking](global-configuration-values.html#brneb9i)
* [Password Synchronization](global-configuration-values.html#b1cxlhgw)
* [Managed System Information](global-configuration-values.html#bryptxv)

## A.2.1 Driver Configuration

*GroupWise Domain Database Version:*
GroupWise REST is the version of the GroupWise domain database to which this driver should connect.

*Default Sync Destination: GroupWise Post Office:*
Specify the GroupWise post office name in dotted form. The newly added Identity Vault objects are created in this GroupWise post office. For example: GWDomain.PostOffice.

*Synchronize Groups:*
This option allows the driver to synchronize eDirectory groups to GroupWise distribution lists. True enables the synchronization. False disables the synchronization.

*Cleanup Group Membership:*
This option is available only if Synchronize Groups is set to True. Removes the user from the Group Membership attribute when the user is removed from the GroupWise distribution lists.

*Synchronize eDir OrgUnit To GroupWise External Post Office:*
This option allows the driver to synchronize eDirectory organizational units to GroupWise external post offices. To enable synchronization, select True and specify a non-GroupWise domain name that exists within the GroupWise system in the Create External Post Offices in this Non-GroupWise Domain setting.

To disable synchronization, click False.

*Create External Post Offices in this Non-GroupWise Domain:*
Specify a non-GroupWise domain name that exists within the GroupWise system. This domain hosts the external post offices created by the GroupWise driver when synchronizing eDirectory Organizational Units to GroupWise post offices.

*Create Nicknames:*
Allows the driver to create GroupWise nicknames when GroupWise accounts are renamed or moved to another post office. True creates nicknames when the accounts are renamed or moved. False does not create nicknames when the accounts are renamed or moved.

*Delete All Nicknames:*
Allows the driver to delete GroupWise nicknames when GroupWise accounts are renamed or moved to another post office. False does not delete nicknames when the accounts are renamed or moved. Select True to delete them.

*Reassign Resource Ownership:*
The driver reassigns ownership of resources when GroupWise accounts are disabled or expired.

True assigns the resources to the default User ID you specify in the next parameter. This setting does not apply when a GroupWise account is deleted because the resources must be reassigned. False is the default.

*Default Resource Owner User ID:*
Specify the prefix of the default user to become the new owner of resources that are reassigned. The default is IS\_admin.

You must specify this name even when the Reassign Resource Ownership option is False. When a GroupWise account is deleted, its resources are assigned to this account. If the default User ID does not have a GroupWise account in the post office of the deleted account, an account is created.

*IMPORTANT:*The driver does not start if a default user prefix is not specified.

*Create Accounts During Migration:*
Allows the driver to create new GroupWise accounts for users without a current account during a migration from eDirectory. True allows the accounts to be created. False does not create the accounts.

Migration causes Identity Manager to examine every object specified. When an object does not have a driver association, the Create policy is applied. If the object meets the Create rule criteria, the object is passed to the driver as an Add event. When you specify True, the driver creates a GroupWise account. When False is specified, the Add event is ignored and the driver issues a warning that this option is set to False. The default value is False.

Migration sets the driver association on all users with GroupWise accounts. See [Associating Identity Vault with GroupWise System](create-driver-object-designer.html#b1d27cy6) for more information.

*Publisher Heartbeat interval:*
Specify the Publisher channel heartbeat interval in minutes. Enter 0 to disable the heartbeat.

*Disassociate User in GroupWise on Deletion in ID Vault:*
When a user is deleted in the Identity Vault, the corresponding user account is disassociated in the GroupWise server. The default value is False.

*GroupWise Web Service (SOAP) URL:*
Specify the URL for the GroupWise Web Service (SOAP) API. Identity Manager engine can verify the synced password to GroupWise server in the Identity Vault using password synchronization status capability.

Example: http://<ipaddress>:7191/soap

## A.2.2 Entitlements

There are multiple sections in the Entitlements tab. Depending on which packages you installed, different options are enabled and displayed. This section documents all of the options.

* [Entitlements Options](global-configuration-values.html#bryple6)
* [Data Collection](global-configuration-values.html#brnumyf)
* [Role Mapping](global-configuration-values.html#brnupu2)
* [Resource Mapping](global-configuration-values.html#brnv29g)
* [Parameter Format](global-configuration-values.html#b1d478nz)
* [Entitlement Extensions](global-configuration-values.html#b1d479vl)

### Entitlements Options

*Use Driver GWAccount Entitlement:*
Select True to allow the driver to manage GroupWise accounts based on the GroupWise account entitlement. Select False to not use the GroupWise account entitlement.

If you select False, the following options are not displayed.

*Enable Login Disabled attribute sync:*
Select True if the changes made to the LoginDisabled attribute in the Identity Vault should synchronize even if the User Account entitlement (Account) is enabled.

*Parameter Format:*
Specify the parameter format the entitlement agent must use. You can pass the entitlement parameters in the legacy format or as a Jason string arranged in a {"name":"value"} format.

*Action On GroupWise Account Entitlement Add:*
Select the action you want the driver to take on the associated GroupWise account (mailbox), when a user is created in the Identity Vault with a GroupWise account entitlement. The options are:

* Enable the GroupWise account
* Disable the GroupWise account

*Action On GroupWise Account Entitlement Remove:*
Select the action you want the driver to take on the associated GroupWise account (mailbox), when a user’s GroupWise account entitlement is removed. The options are:

* Disable the GroupWise account
* Delete the GroupWise account
* Expire the GroupWise account
* Disable and expire the GroupWise account

*Use Group Entitlement:*
Select whether the driver manages group membership for users with the gwGroup entitlement. By default, this is set to True. This allows the driver to manage GroupWise group membership based on the gwGroup entitlement. Select False if you do not want the driver to manage group membership for users based on the gwGroup entitlement.

*Parameter Format:*
Specify the parameter format the entitlement agent must use. You can pass the entitlement parameters in the legacy format or as a Jason string arranged in a {"name":"value"} format.

*Advanced Settings:*
Select show to display the entitlement options that allow or deny additional functionality like data collection and others. These settings should rarely be changed.

### Data Collection

Data collection enables the Identity Report Module to gather information to generate reports. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable data collection:*
Select Yes to enable data collection for the driver through the Data Collection Service by the Managed System Gateway driver. If you are not going to run reports on data collected by this driver, select No.

*Allow data collection from user accounts:*
Select Yes to allow data collection by the Data Collection Service through the Managed System Gateway driver for the user accounts.

*Allow data collection for Groups:*
Select Yes to allow data collection by the Data Collection Service through the Managed System Gateway driver for groups.

### Role Mapping

NetIQ Identity Applications allow you to map business roles with IT roles.

*Enable role mapping:*
Select Yes to make this driver visible to Identity Applications.

*Allow mapping of user accounts:*
Select Yes if you want to allow mapping of user accounts in Identity Applications. An account is required before a role, profile, or license can be granted through Identity Applications.

*Allow mapping of groups:*
Select Yes if you want to allow mapping of groups in Identity Applications.

### Resource Mapping

Identity Applications allow you to map resources to users.

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

*Groupwise account extensions:*
The content of this field is added below the entitlement element in the EntitlementConfiguration resource object.

*Group extensions:*
The content of this field is added below the entitlement element in the EntitlementConfiguration resource object.

## A.2.3 Account Tracking

Account tracking is part of the Identity Reporting Module. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

*Enable account tracking:*
Set this to True to enable account tracking policies. Set it to False if you do not want to execute account tracking policies.

*Realm:*
Specify the name of the realm, security domain, or namespace in which the account name is unique.

*Object Class:*
Add the object class to track. Class names must be in the application namespace.

*Identifiers:*
Add the account identifier attributes. Attribute names must be in the application namespace.

*NOTE:*A new identifier, LDAPDN, has been added to the Identifiers list. You must add it manually because the package upgrade doesn't add it to the Account Tracking GCV.

*Status attribute:*
Name of the attribute in the application namespace to represent the account status.

*Status active value:*
Value of the status attribute that represents an active state.

*Status inactive value:*
Value of the status attribute that represents an inactive state.

## A.2.4 Password Synchronization

The following GCVs control the follow of passwords between GroupWise and the Identity Vault. For more information about how to use the Password Management GCVs, see [Configuring Password Flow](../../../identity-manager-48/password_management/data/configuring-password-flow.html#configuring-password-flow) in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

*Set the initial/default GroupWise password on account creation:*
If True, the GroupWise initial/default password is set when an account is created. The initial password value is specified in the Create policy. If False, the initial password is not set.

GroupWise has two passwords, the initial password and the regular password. The initial password is stored in clear text and can be seen by an admin. The regular password is encrypted and cannot be viewed. When it is set, the regular password is used by GroupWise instead of the initial password. When a GroupWise user changes his or her password, it is stored as the regular password. For security, the initial password is never set to a password sent from eDirectory.

## A.2.5 Managed System Information

These settings help the Identity Reporting Module function to generate reports. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

### General Information

*ID:*
Specify a unique ID for the GroupWise system. This ID is displayed in the reports.

*Name:*
Specifies a descriptive name for this GroupWise system. The name is displayed in the reports.

*Description:*
Specifies a brief description of this GroupWise system. The description is displayed in the reports.

*Location:*
Specify the physical location of the GroupWise system. This information is displayed in the reports.

*Vendor:*
Select NetIQ as the vendor of this system. The vendor information is displayed in the reports.

*Version:*
Specify the version of this GroupWise system. The version is displayed in the reports.

### System Ownership

*Business Owner:*
Select a user object in the Identity Vault that is the business owner of this GroupWise system. This can only be a user object, not a role, group, or container.

*Application Owner:*
Select a user object in the Identity Vault that is the application owner for this GroupWise system. This can only be a user object, not a role, group, or container.

### System Classification

*Classification:*
Specify the classification for this GroupWise system in your environment. For example, Mission-Critical. This information is displayed in the reports.

*Environment:*
Specify the type of environment the GroupWise system provides. For example, development, test, or production. This information is displayed in the reports.

### Connection And Miscellaneous Information

*Connection and miscellaneous information:*
Select show to display the following settings:

*ID:*
Specify a unique ID for the GroupWise system. This ID is displayed in the reports.

*Type:*
Specifies the type of the managed system.

*Authentication IP Address:*
Specify the IP address used to authenticate to the GroupWise system.

*Authentication Port:*
Specify the port used to authenticate to GroupWise system.

*Authentication ID:*
Specify the user ID used to authenticate to GroupWise ystem.
