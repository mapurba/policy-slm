# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The PeopleSoft driver includes several predefined GCVs. You can also add your own if you discover you need additional ones as you implement policies in the driver.

To access the driver’s GCVs in Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver icon, then click the upper right corner of the driver icon to display the driver’s properties page.

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

The global configuration values are organized as follows:

* [Password Synchronization](global-configuration-values.html#brv3kjy)
* [Managed System Information](global-configuration-values.html#brnebcn)

## A.2.1 Password Synchronization

These GCVs enable password synchronization between the Identity Vault and the PeopleSoft system.

In Designer, you must click the ![](../graphics/designer_edit_pass_sync_n.png) icon next to a GCV to edit it. This displays the Password Synchronization Options dialog box for a better view of the relationship between the different GCVs.

In Identity Console, to edit the Password management option, follow the steps given below:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.
3. Select the Configuration tab.
4. Expand the Global Config Values section.
5. Select the Password Synchronization tab.

For more information about how to use the Password Management GCVs, see [Configuring Password Flow](../../../identity-manager-48/password_management/data/configuring-password-flow.html#configuring-password-flow) in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

*Connected System Name:*
Specifies the name of the PeopleSoft system or the driver name. This value is used by the e-mail notification template to identify the source of the notification message.

*Application accepts passwords from Identity Manager:*
If True, allows passwords to flow from the Identity Manager data store to the connected system.

*Identity Manager accepts passwords from application:*
If True, allows passwords to flow from the connected system to Identity Manager.

*Publish passwords to NDS password:*
If True, uses the password from the connected system to set the non-reversible NDS password in eDirectory.

*Publish passwords to Distribution Password:*
If True, uses the password from the connected system to set the NMAS Distribution Password used for Identity Manager password synchronization.

*Require password policy validation before publishing passwords:*
If True, applies NMAS password policies during publish password operations. The password is not written to the data store if it does not comply.

*Reset user’s external system password to the Identity Manager password on failure:*
If True, on a publish Distribution Password failure, attempts to reset the password in the connected system by using the Distribution Password from the Identity Manager data store.

*Notify the user of password synchronization failure via e-mail:*
If True, notifies the user by e-mail of any password synchronization failures.

## A.2.2 Managed System Information

These settings help Identity Reporting to generate reports.

*ID:*
Specifies an ID that uniquely identifies the managed system.

*Name:*
Specifies a descriptive name for this PeopleSoft system. This name is displayed in the reports.

*Description:*
Specifies a brief description of this PeopleSoft system. This description is displayed in the reports.

*Type:*
Specifies the type for the PeopleSoft system.

*Classification:*
Specifies the classification of the PeopleSoft system. This information is displayed in the reports.

*Vendor:*
Specifies Oracle as the vendor of the PeopleSoft system. This information is displayed in the reports.

*Version:*
Specifies the version of this PeopleSoft system. This version information is displayed in the reports.

*Business Owner:*
Specifies the business owner in the Identity Vault for this PeopleSoft system. Ensure that a user object is selected. You must not select a role, group, or container.

*Application Owner:*
Specifies the application owner in the Identity Vault for this PeopleSoft system. Ensure that a user object is selected. You must not select a role, group, or container.

*Location:*
Specifies the physical location of this PeopleSoft system. This location is displayed in the reports.

* Mission-Critical
* Vital
* Not-Critical
* Other

  If you select Other, you must specify a custom classification for the PeopleSoft system.

*Environment:*
Specifies the type of environment the PeopleSoft system provides. The options are:

* Development
* Test
* Staging
* Production
* Other

  If you select Other, you must specify a custom classification for the PeopleSoft system.

*Authentication IP Address:*
Specifies the IP address used to authenticate to the PeopleSoft system.

*Authentication Port:*
Specifies the port used to authenticate to the PeopleSoft system.

*Authentication ID:*
Specifies the user ID used to authenticate to the PeopleSoft system.
