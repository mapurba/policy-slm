# A.2 Global Configuration Values

Global Configuration Values (GCVs) can be used by the driver to control its functionality. GCVs are defined in the driver or in the driver set. Driver set GCVs can be used by all drivers residing in the driver set.

The Workday driver includes predefined GCVs. You can also add your own GCVs as required for the additional policy implementation in the driver. For information on most of the GCVs, see [Creating the Driver Object](t4avmq79xc47.html).

However, the following GCV’s should be configured after installing the driver:

* User Config: This GCV helps to configure settings for a user in the Publisher channel. For more information, see [Step 10](t4avmq79xc47.html#user_config_gcv) in the section [Creating the Driver Object](t4avmq79xc47.html).
* Business Process: As a part of Workday Business Process, you can specify the container details where the information for delta and future objects will be created in the Identity Vault. For more information, see [Configuring Business Process](t4f47egfqot3.html).
* *Retry Event Config:*
  You can specify certain attributes in this field for which events get logged on the Workday portal and the driver might retry to configure them after activating the user. Mention the required list of attributes separated by comma in this field. The following attributes will be listed by default:

  + wd-HomePrimaryPhone
  + wd-WorkPrimaryPhone
  + Internet EMail Address
  + homeEmailAddress

  NOTE:

  + If any secondary phone attributes are configured as part of the driver, you can add them to this retry event config list.
  + Ensure to extend the Schema to include DirXML-WDSyncAttr attribute in IDV for configuring the retry events. For more information, see [Section C.0, IDV Schema Extension](t4avmq7j9nt4.html).
* To get a reference to the container in IDV where new objects will be created, you must specify the following GCVs:

  + Relation Config
  + JobFamily Config
  + Location Config
  + Photo Config
  + Job Profile Config
  + Organizations Config

  To configure these GCVs, see [Step 11](t4avmq79xc47.html#object_gcvs) in the section [Creating the Driver Object](t4avmq79xc47.html).
* Entitlement: You can now enable entitlements for User-Based Security Groups and Organizational Roles. To enable entitlements, double click the connector line and navigate to GCVs > Entitlement tab. For more information, see [Customizing Entitlements](t4finm19niw9.html).

For more information on GCVs, see [When and How to Use Global Configuration Values](../../../identity-manager-49/driver_admin/data/bh15mpk.html#bh15mpk) in [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-49/driver_admin/data/bktitle.html#bktitle).
