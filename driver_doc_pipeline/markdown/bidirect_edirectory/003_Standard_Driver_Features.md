# 1.2 Standard Driver Features

The following sections provide information about how the Bidirectional eDirectory driver supports standard driver features:

* [Local Platforms](standard-driver-features.html#b92nb34)
* [Entitlements](standard-driver-features.html#b10rs3g9)
* [Password Synchronization](standard-driver-features.html#b96ayf1)
* [Driver Packages](standard-driver-features.html#bw52ty6)

## 1.2.1 Local Platforms

The Bidirectional eDirectory driver runs in any Identity Manager installation. See, [Considerations for Installing Drivers with the Identity Manager Engine](../../../identity-manager-48/idm_overview_planning/data/identity-manager-server-guidelines.html#guidelines-for-installing-drivers-with-identity-manager-engine) in the [NetIQ Identity Manager Overview and Planning Guide](../../../identity-manager-48/idm_overview_planning/data/netiq-identity-manager-overview-and-planning.html#netiq-identity-manager-overview-and-planning) .

## 1.2.2 Entitlements

Entitlements standardize a method of recording this information on objects in the Identity Vault. The Bidirectional eDirectory driver implements entitlements. You can use entitlements to grant or revoke rights to an account in the driver. The driver is unaware of the User Application or Role-Based Entitlements. It depends on the User Application server or the Entitlements driver to grant or revoke the entitlement for a user based upon its own rules.

You should enable entitlements for the driver only if you plan to use the User Application or Role-Based Entitlements with the driver. For more information about entitlements, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

## 1.2.3 Password Synchronization

The Bidirectional eDirectory driver supports password synchronization via Universal Password. You can also use the older form of password synchronization (a public/private key pair or NDS password). For more information, see [Section 7.0, Synchronizing Passwords](synchronizing-passwords.html).

## 1.2.4 Driver Packages

The Identity Manager content is now delivered in packages. The packages are included with Identity Manager 4.0 and later. For more information about Identity Manager packages, see "[Configuring Packages](../../../identity-manager-48/designer_admin/data/configpackages.html#configpackages)" in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo) .

There are multiple packages for the Bidirectional eDirectory driver. The packages create a driver with a set of policies suitable for synchronizing data with the Identity Vault.
