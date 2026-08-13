# 1.4 Support for Standard Driver Features

The following sections provide information about how the SAP Portal driver supports standard driver features:

* [Local Platforms](identity-manager-sap-portal-driver-support-for-standard-driver-features.html#identity-manager-sap-portal-driver-support-for-local-platforms)
* [Remote Platforms](identity-manager-sap-portal-driver-support-for-standard-driver-features.html#identity-manager-sap-portal-driver-support-for-remote-platforms)
* [Entitlements](identity-manager-sap-portal-driver-support-for-standard-driver-features.html#identity-manager-sap-portal-driver-support-for-entitlements)
* [Password Synchronization](identity-manager-sap-portal-driver-support-for-standard-driver-features.html#identity-manager-sap-portal-driver-support-for-password-sync)
* [Account Tracking](identity-manager-sap-portal-driver-support-for-standard-driver-features.html#identity-manager-sap-portal-driver-support-for-account-tracking)
* [Identity Applications](identity-manager-sap-portal-driver-support-for-standard-driver-features.html#identity-manager-sap-portal-driver-support-for-mapping-business-roles-with-it-roles)

## 1.4.1 Local Platforms

A local installation is an installation of the driver on the same server as the Identity Manager engine and the Identity Vault.

The SAP Portal driver can be installed on the same operating systems that are supported by the Identity Manager engine. For information, see the [NetIQ Identity Manager Technical Information website](https://www.netiq.com/products/identity-manager/advanced/technical-information/).

## 1.4.2 Remote Platforms

You can install the Remote Loader if you don’t want to install the Identity Manager engine and the Identity Vault (eDirectory) on the same server.

The SAP Portal driver can be installed on the same operating systems supported by the Remote Loader. For information, see the [NetIQ Identity Manager Technical Information website](https://www.netiq.com/products/identity-manager/advanced/technical-information/).

## 1.4.3 Entitlements

Entitlements are a way to set up a list of criteria to grant or revoke access to resources for users, roles, and groups. The SAP Portal drivers contains three preconfigured entitlements. For more information, see [Section 5.0, Implementing the Preconfigured Entitlements](implementing-preconfigured-entitlements-in-identity-manager-sap-portal-driver.html).

## 1.4.4 Password Synchronization

The SAP Portal driver can synchronize passwords from the Identity Vault into the SAP NetWeaver server. The password synchronization is one way. For more information, see the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

## 1.4.5 Account Tracking

Account Tracking allows you to manage all of the identities each user account has in each system connected to the Identity Vault. Account Tracking is a feature included with the Identity Reporting Module. For more information, see the [Administrator Guide to NetIQ Identity Reporting](../../../identity-manager-48/report_setup/data/bookinfo.html#bookinfo).

## 1.4.6 Identity Applications

The SAP Portal driver can be configured to work with the Identity Manager’s Identity Applications component that allows you to map business roles to IT roles. For more information, see [Identity Applications Administration](../../../identity-manager-48/identity_apps_admin/data/t42bq2rlpx68.html#t42bq2rlpx68) in the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](../../../identity-manager-48/identity_apps_admin/data/bookinfo.html#bookinfo).
