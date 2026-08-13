# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The SOAP driver includes several predefined GCVs. You can also add your own if you discover you need additional ones as you implement policies in the driver.

To access the driver’s GCVs in Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Locate the driver icon, then click the driver icon to display the driver’s properties page.
4. Click Global Config Values drop down to display the GCV page.

To access the driver’s GCVs in Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select Properties > Global Configuration Values.

   or

   To add a GCV to the driver set, right-clickthe driver set icon ![](../graphics/driver_set_icon_n.png), then click Properties > GCVs.

The global configuration values are organized as follows:

* [Password Synchronization](global-configuration-values.html#brv3kjy)

## A.2.1 Password Synchronization

These GCVs enable password synchronization between the Identity Vault and the connected system.

In Designer, you must click the ![](../graphics/designer_edit_pass_sync_n.png) icon next to a GCV to edit it. This displays the Password Synchronization Options dialog box for a better view of the relationship between the different GCVs.

In Identity Console, to edit the Password management options go to Configuration > Global Configuration Values, and then change it in your Password synchronization policy tab.

For more information about how to use the Password Management GCVs, see "[Configuring Password Flow](../../../identity-manager-48/password_management/data/configuring-password-flow.html#configuring-password-flow)" in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

*Connected System or Driver Name:*
Specify the name of the SOAP system or the driver name. This valued is used by the e-mail notification template to identity the source of the notification message.

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
If True, on a publish Distribution Password failure, attempts to reset the password in the connected system by using the Distribution Password from the Identity Manager data store.

*Notify the user of password synchronization failure via e-mail:*
If True, notifies the user by e-mail of any password synchronization failures.
