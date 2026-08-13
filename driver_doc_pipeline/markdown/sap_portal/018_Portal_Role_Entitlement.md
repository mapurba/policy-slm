# 5.3 Portal Role Entitlement

The portal role entitlement adds users to the SAP Portal roles, and it is disabled by default if you selected to use entitlements during the creation of the driver. This entitlement contains parameters, which means it can be granted multiple times. The parameters for the entitlement are the roles returned by the entitlement query to the SAP Portal. When the entitlement is granted with an SAP Portal Role as the parameter, the SAP User is added to the Portal Role.

For example, assume there is an RBPM role that contains two UMERole entitlements, one with a parameter of User Admins and the second with a parameter of HR Admin. When the RBPM role is granted and the entitlements are granted, the user is added to the User Admins and the HR Admin roles in the SAP Portal.

This entitlement is disabled by default. The best practice is to assign Portal users to Portal groups, which in turn contains the appropriate Portal Roles. However, if you want to assign Portal roles directly to the Portal users, this entitlement allows you to do that.

To manually enable this entitlement:

1. Verify that an entitlement agent that contains your list of criteria to grant or revoke Portal role assignments in SAP exists. For more information, see [Entitlement Agents](entitlement-agents-for-identity-manager-sap-portal-driver.html).
2. If you have an existing driver continue with [Step 3](understanding-portal-role-entitlement-for-identity-manager-sap-portal-driver.html#bj6d7g4); otherwise, during the creation of a driver, select True for the Use Portal Role Entitlement option.

   This sets the entitlement GCVs to True.
3. Access the GCVs page for the driver.
4. Select True for the User Portal Role Entitlement option.
5. Click OK to save the changes.

The entitlement is now enabled. When a user is granted a role through one of the entitlement agents, the associated Portal role assignments are automatically made for the user by the SAP Portal driver.
