# 1.2 Support for Standard Driver Features

The following sections provide information about how the SAP HANA driver supports these standard driver features:

* [Local Platforms](t4avmq76rihg.html#t4avmq76rq79)
* [Remote Platforms](t4avmq76rihg.html#t4avmq76rxx2)
* [Supported Operations](t4avmq76rihg.html#t4avmq76s5mv)
* [Support for Password Synchronization](t4avmq76rihg.html#t4p23gp40usr)
* [Supported Pagination techniques:](t4avmq76rihg.html#t4p23hzyll5r)

## 1.2.1 Local Platforms

A local installation is an installation of the driver on the Metadirectory server. You can install the SAP HANA driver on the operating systems supported for the Metadirectory server.

For information about the operating systems supported for the Metadirectory server, see [Considerations for Installing Drivers with the Identity Manager Engine](../../../identity-manager-48/idm_overview_planning/data/identity-manager-server-guidelines.html#guidelines-for-installing-drivers-with-identity-manager-engine) in the [NetIQ Identity Manager Overview and Planning Guide](../../../identity-manager-48/idm_overview_planning/data/netiq-identity-manager-overview-and-planning.html#netiq-identity-manager-overview-and-planning).

## 1.2.2 Remote Platforms

The SAP HANA driver can use the Remote Loader service to run on a server other than the Metadirectory server. You can install the SAP HANA driver on the operating systems supported for the Remote Loader.

For information about the supported operating systems, see [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front).

## 1.2.3 Supported Operations

The SAP HANA driver supports the following operations on the Publisher and Subscriber channel:

* Publisher Channel

  + Users: Publisher Channel supports add, modify, delete and query operations for users.
  + User Group: Publisher Channel supports add, modify, delete and query operations for users groups.
  + Roles Operations: Publisher Channel supports add, modify, delete and query operations for roles.

* Subscriber Channel

  + Users: Subscriber Channel supports add, modify, delete, migrate and query operations for users.
  + User Group: Subscriber Channel supports query operations, adding and removing members using Entitlements.
  + Roles Operations: Subscriber Channel supports query operations, assigning and revoking operations using Entitlements.

## 1.2.4 Support for Password Synchronization

The SAP HANA driver supports password synchronization only in subscriber channel. The password set for the user must meet the password policy criteria defined in SAP HANA. For more information see, [Password Policy Configuration Options](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/61662e3032ad4f8dbdb5063a21a7d706.html)

## 1.2.5 Supported Pagination techniques:

SAP HANA driver follows pagination technique that uses an Offset Pagination. It updates paging parameter with page size.
