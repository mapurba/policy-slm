# 2.5 Configuring Entitlements

In Designer, after creating the driver object, double click the connector line and navigate to GCVs > Entitlement tab. Specify the following parameters to configure entitlements:

* Enable User Account Entitlement: Select the value as true to enable the entitlements feature for User Accounts.
* Enable User Group Entitlement: Select the value as true to enable the entitlements feature for User Groups.
* Enable Role Entitlement: Select the value as true to enable the entitlements feature for Roles.

*NOTE:*After configuring the SAP HANA driver for entitlements, you can deploy the driver. Post deployment, perform the procedures as explained in the following sections.

## 2.5.1 Fetching Entitlements from SAP HANA Cloud Database

You must ensure to perform a “CodeMap refresh” to fetch all the users, user groups and assignable roles from SAP HANA. The code map refresh, helps to facilitate the grant or revoke permissions through Identity Manager. For the procedure to refresh the code map, see [Entitlement Query Settings](https://www.netiq.com/documentation/identity-manager-48/help_idm_identityapps_admin/data/t44v3h6rz1j7.html) section in the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](https://www.netiq.com/documentation/identity-manager-47/identity_apps_admin/data/bookinfo.html#bookinfo). SAP HANA driver is supported by following entitlements.

* Users: Assigning Permissions to users.
* User Group: Adding and removing members to the user group is supported using entitlements.
* Roles operations: Assigning and revoking privileges to roles is supported using entitlements.
