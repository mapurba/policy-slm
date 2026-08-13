# 5.2 User Account Entitlement

The user account entitlement is a simple (no parameters) entitlement used to control user account creation on the Subscriber channel. After the user account entitlement is enabled, the user account is provisioned when the entitlement is granted.

This entitlement also has Subscriber policies that define actions to take when the entitlement is revoked. When an entitlement is revoked, there are two actions that can be taken:

* *Disable:*
  When the entitlement is revoked, the user account is locked in the connected SAP Portal.
* *Delete:*
  A request is sent to delete the account.

To enable this entitlement:

1. Verify that an entitlement agent that contains your list of criteria to grant or revoke a user’s access to resources in SAP exists. For more information, see [Entitlement Agents](entitlement-agents-for-identity-manager-sap-portal-driver.html).
2. If you have an existing driver, continue with [Step 3](understanding-user-account-entitlement-for-identity-manager-sap-portal-driver.html#bj68p04); otherwise, during the creation of a driver, select True for the Use User Account Entitlement option.

   This sets the entitlement GCVs to True.
3. Access the GCVs page for the driver.
4. Select show for the Show entitlements configuration option.
5. Enable the user account entitlement by selecting true.
6. Select what to do when the user account entitlement is revoked by indicating whether you want the account disabled, deleted, or nothing done to the account.
7. Click OK to save the changes.

The entitlement is now enabled. However, a new user account is not provisioned until the entitlement is granted.
