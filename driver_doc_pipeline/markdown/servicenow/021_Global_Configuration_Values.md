# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The ServiceNow driver includes several predefined GCVs. You can also add your own GCVs, on a need basis, while you implement policies in the driver.

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
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select Properties > GCVs.

   or

   To add a GCV to the driver set, right-click the driver set icon ![](../graphics/driver_set_icon_n.png), then click Properties > GCVs.

## A.2.1 Password Synchronization

Use the following GCVs to configure the driver to synchronize passwords to ServiceNow.

*Application accepts passwords from Identity Manager:*
This option is used to determine whether the application accepts passwords from Identity Manager. Selecting True allows the passwords to flow from the Identity Manager data store to connected system.

*Notify the user of password synchronization failure via e-mail:*
Select this option if you want to notify the user through e-mail.

## A.2.2 Entitlements

There are multiple sections in the Entitlements tab. Depending on which packages you installed, different options are enabled or displayed.

* [Entitlements Configuration](global-configuration-values.html#b1huzebd)
* [Role Mapping](global-configuration-values.html#b1huzt5m)
* [Parameter Format](global-configuration-values.html#b14xjbn1)
* [Resource Mapping](global-configuration-values.html#b1huzvnn)
* [Entitlement Extensions](global-configuration-values.html#b1huzxuf)

### Entitlements Configuration

*Use Entitlements to control ServiceNow accounts:*
Select True to enable the driver to manage user accounts based on the driver’s defined entitlements. Select False to disable management of user accounts based on the entitlements.

*Enable Login Disabled Attribute Sync:*
Select True if the changes made to the LoginDisabled attribute in the Identity Vault should be synchronized even if the User Account entitlement (Account) is enabled.

*When Account Entitlement Revoked:*
Select an appropriate action when a user account entitlement is revoked. The options are Disable User or Delete User. By default, Disable User is selected.

*Use Group Entitlement:*
Select True to enable the driver to manage group membership based on the driver’s defined entitlements.

*Use Role Entitlement:*
Select True to enable the driver to manage user roles based on the driver’s defined entitlements.

*Use Department Entitlement:*
Select True to enable the driver to manage department based on the driver’s defined entitlements.

*Advanced Settings:*
Select Show to display the entitlement options that allow or deny additional functionality like role mapping, resource mapping and others. These settings should rarely be changed.

*Parameter Format:*
Specify the parameter format the entitlement agent must use when granting this entitlement.

### Role Mapping

Identity Applications allows you to map business roles with IT roles.

*Enable role mapping:*
Select Yes to make this driver visible to Identity Applications.

*Allow mapping of user accounts:*
Select Yes if you want to allow mapping of user accounts in Identity Applications.

*Allow mapping of groups:*
Select Yes if you want to allow mapping of groups in Identity Applications.

*Allow mapping of roles:*
Select Yes if you want to allow mapping of roles in Identity Applications.

*Allow mapping of departments:*
Select Yes if you want to allow mapping of departments in Identity Applications.

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

*Enable resource mapping:*
Select Yes to make this driver visible to Identity Applications.

*Allow mapping of user accounts:*
Select Yes if you want to allow mapping of user accounts in Identity Applications.

*Allow mapping of groups:*
Select Yes if you want to allow mapping of groups in Identity Applications.

*Allow mapping of roles:*
Select Yes if you want to allow mapping of roles in Identity Applications.

*Allow mapping of departments:*
Select Yes if you want to allow mapping of departments in Identity Applications.

### Entitlement Extensions

Identity Applications allow you to map resources to users. For more information, see the NetIQ Identity Manager - User’s Guide to the Identity Applications [NetIQ Identity Manager - User’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_user/data/netiq-identity-manager-user-guide.html#netiq-identity-manager-user-guide).

*User account extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

*Group extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

*Role extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.

*Department extensions:*
The content of this field is added below the entitlement elements in the EntitlementConfiguration resource object.
