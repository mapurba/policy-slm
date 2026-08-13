# A.1 Global Configuration Values (GCVs)

There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, you must review the Driver Parameters and the Global Configuration Values, in the Driver Configuration page. These settings must be configured properly for the driver to start and function correctly. You can configure the driver with entitlements enabled or disabled.

GCVs are the values that can be used by the driver to control its functionality. GCVs are defined in the driver or in the driver set. Driver set GCVs can be used by all drivers in the driver set.

The SCIM driver includes predefined GCVs. You can also add your own GCVs as required for the additional policy implementation in the driver. The configured SCIM driver’s GCV is:

* Validate Resource with Required Attributes: This field validates resources and the required attributes that are available in the schema. Select as false.
* Enable JSON To XDS Conversion Logs: By default this value is set to False. When it is set to True, it enables the JSON To XDS Conversion logs only in the remote loader. For more information, see [Hidden JSON Content in Output Transformation Policy Channels](t4d38vmw681a.html).

  *WARNING:*Enabling this field shows the JSON XDS logs containing sensitive data in the trace. This configuration is intended for debugging purposes in a test environment only. Do not enable this setting in the product environment.
* Connecting to SAP Cloud: Set this to true if you are connecting to SAP Cloud. Defaults to false.
* Connected Application’s Name: Enter the name of the connected application. This name appears in the entitlements.
* SCIM 2.0 URL: Auto-populates the SCIM 2.0 URL value as provided while creating the driver object.

For more information on GCVs, see [When and How to Use Global Configuration Values](../../../identity-manager-48/driver_admin/data/bh15mpk.html#bh15mpk) in "[NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle)".

## A.1.1 Configuring Entitlements

You can configure the driver with entitlements enabled or disabled. To configure entitlements, perform the following steps:

1. In the modeler window, right-click the driver icon or the driver line, then select Properties.
2. Click GCVs > Entitlements and review the following settings:

   ![](../graphics/scim_entitlements_a.png)

   *NOTE:*These settings are only displayed if you have installed the SCIM Entitlements package. The entitlements are supported based on the connected application’s capabilities.

   * *Enable User Account Entitlement:*
     This field enables the driver to manage user account permissions using the User Account entitlement. Ensure that the value of this parameter is set to true. By default, the value is set to False. Specify the values as shown in the following table to set User Account Entitlements.

     | Field | Description/Value |
     | Sync Login Disabled attribute | This field is used to control the Login Disabled attribute for a particular user:  Select:  + Yes, to sync the changes made to the Login Disabled attribute in the Identity Manager, to SAP Cloud. + No, to restricts syncing the changes of Login Disabled attribute in the Identity Manager to SAP Cloud. |
     | Action on Account Revocation | Select the action to be performed in SAP Cloud when the user account entitlement is revoked.  The available options are:  + Disable Account + Delete Account |
   * *Enable Group Entitlement:*
     This option enables the driver to manage group memberships using the Group entitlement. Ensure that the value of this parameter is set to true. By default, the value is set to false.

     *IMPORTANT:*If the values for Enable User Account Entitlement and Enable Group Entitlement parameter is set to False, the user and group membership synchronization will be managed using the non-entitlement configuration method.
3. Click Apply.
4. Click OK when finished.
