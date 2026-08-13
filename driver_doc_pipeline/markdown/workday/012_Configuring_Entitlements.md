# 2.8 Configuring Entitlements

In Designer, after creating the driver object, double click the connector line and navigate to GCVs > Entitlement tab. Specify the following parameters to configure entitlements:

* Enable User-Based Security Group Entitlement: Select the value as true to enable the entitlements feature for User-Based Security Group.
* Enable Assignable Role Entitlement: Select the value as true to enable the entitlements feature for Assignable Roles.

*NOTE:*After configuring the Workday driver for entitlements, you can deploy the driver. Post deployment, perform the procedures as explained in the following sections.

## 2.8.1 Fetching Entitlements from Workday Portal

You must ensure to perform a “CodeMap refresh” to fetch all the user-based security groups and assignable roles from Workday. The code map refresh, helps to facilitate the grant or revoke permissions through Identity Manager. For the procedure to refresh the code map, see [Entitlement Query Settings](https://www.netiq.com/documentation/identity-manager-48/help_idm_identityapps_admin/data/t44v3h6rz1j7.html) section in the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](https://www.netiq.com/documentation/identity-manager-47/identity_apps_admin/data/bookinfo.html#bookinfo).

## 2.8.2 Assigning Permissions to a User

You can assign the required permissions to a new user, or change an already assigned permission from an existing user to a new user. In Identity Manager, this changing of the assignment is a two step process as follows:

1. First, you must revoke the currently assigned resource permission, and submit the request.
2. Then, grant the permission to another user and submit the request again.

For more information to perform the above steps, see [About the Resource Editor](https://www.netiq.com/documentation/identity-manager-49/identity_apps_design/data/resource-editor.html) section in the [NetIQ Identity Manager - Administrator’s Guide to Designing the Identity Applications](https://www.netiq.com/documentation/identity-manager-49/identity_apps_design/data/netiq-identity-apps-design-guide.html).
