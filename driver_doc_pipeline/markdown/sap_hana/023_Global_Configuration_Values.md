# A.2 Global Configuration Values

Global Configuration Values (GCVs) can be used by the driver to control its functionality. GCVs are defined in the driver or in the driver set. Driver set GCVs can be used by all drivers residing in the driver set.

The SAP HANA driver includes predefined GCVs. You can also add your own GCVs as required for the additional policy implementation in the driver. For information on most of the GCVs, see [Creating the Driver Object](t4avmq79xc47.html).

However, the following GCV’s should be configured after installing the driver:

* Common Password Setting:

  + Set default password if not available: Set this value to True if the default password is not available for the server.

* SAP HANA Group and Role:

  + Group - Publisher Settings

    - Group Placement Container - Specify the tree path where the data has to sync for group placement container.

  + Role - Publisher Settings

    - Role Placement Container - Specify the tree path where the publisher settings data has to sync for roles.

* Entitlements:

  + Entitlements Configuration:

    - Enable User Account Entitlements: Set this value to True if you need to enable the user account entitlements, else set to False.
    - Enable User Group Entitlement: Set this value to True if you need to enable the user group entitlements, else set to False.
    - Enable Role Entitlement: Set this value to True if you need to enable the role entitlements, else set to False.

  + Advanced Settings:

    - Advanced Settings: By default this value is Hide. Set this value to Show if you need to define advanced setting parameters for Data Collection or Role Mapping or Resource Mapping or Entitlement Extensions. When Advanced Settings is set true below listed GCV values are displayed.

      * Data Collection

        + Enable Data Collection: When this value is set to Yes, the below listed GCV values are displayed. Else set it to No.

          - Allow Data Collection from User Account: Set this value to Yes if data collection is required from user accounts. Else set it to No.
          - Allow Data Collection from User Groups: Set this value to Yes if data collection is required from user groups. Else set it to No.
          - Allow Data Collection from Role: Set this value to Yes if data collection is required from roles. Else set it to No.
      * Role Mapping: When this value is set to Yes, the below listed GCV values are displayed. Else set it to No.

        + Allow mapping of User Account: Set this value to Yes if role mapping is required for user accounts. Else set it to No.
        + Allow mapping of User Groups: Set this value to Yes if role mapping is required for user groups. Else set it to No.
        + Allow mapping of Role: Set this value to Yes if mapping is required for roles. Else set it to No.
      * Entitlement Extensions:

        + User Account Extensions: Specify the assignment extensions for user accounts.
        + User Groups Extensions: Specify the assignment extensions for user groups.
        + Role Extensions: Specify the assignment extensions for roles.

* Password Synchronization

  Password Management

  + Application accepts password from Identity Manager: (Managed from the Password Sync page) - By default the value is set to True. The SAP HANA application accepts the password from Identity Manager.
  + Reset user’s external system password to the Identity Manager Password on failure: (Managed from the Password Sync page) - By default the value is set to True. If there is any failure during password synchronization, the Identity Manager password is synced to the external system (SAP HANA) user.
  + Notify the User Password Synchronization failure via e-mail: (Managed from the Password Sync page) - By default the value is set to True. This enables in notifying the user through an e-mail, if there is any failure in synchronizing the password.

For more information on GCVs, see [When and How to Use Global Configuration Values](../../../identity-manager-48/driver_admin/data/bh15mpk.html#bh15mpk) in [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).
