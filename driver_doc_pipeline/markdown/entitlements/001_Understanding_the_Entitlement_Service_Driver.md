# 1.0 Understanding the Entitlement Service Driver

The following overview assumes that you understand entitlements (as explained in the "[How Entitlements Work](../../../identity-manager-49/entitlements/data/identity-manager-entitlement-process.html#identity-manager-entitlement-process)" in the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-49/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements)) and have created the entitlements you want to manage through the Entitlements Service driver.

The Entitlements Service driver is one of three entitlement agents that you can use to grant entitlements, or permission slips, to users. The other two entitlement agents are the role-based provisioning component (see "[Role-Based Entitlements:](../../../identity-manager-49/entitlements/data/identity-manager-entitlement-process.html#bfnqsnt)" in the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-49/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements)) and workflow-based provisioning component in the User Application (see "[User Application Workflow-Based Provisioning:](../../../identity-manager-49/entitlements/data/identity-manager-entitlement-process.html#bfnquq0)" in the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-49/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements)).

*IMPORTANT:*NetIQ recommends you to use User Application as the Roles-Based Entitlement granting authority instead of using the Entitlements Service driver. The Entitlement Service driver is not intended to be a roles service and is supported only as an entitlement granting authority.

Entitlements Service Driver supports legacy entitlement. It does not support the Identity Manager 4.0 entitlement format.

The following sections provide information to help you understand the Entitlements Service driver:

* [How the Entitlements Service Driver Works](how-entitlement-driver-works.html)
* [Role-Based Entitlements Versus Other Entitlements](role-based-entitlements-vs-other-entitlements.html)
* [Using Multiple Entitlements Service Drivers](use-multiple-entitlement-drivers.html)
