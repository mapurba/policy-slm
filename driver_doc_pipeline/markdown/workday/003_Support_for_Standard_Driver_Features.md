# 1.2 Support for Standard Driver Features

The following sections provide information about how the Workday driver supports these standard driver features:

## 1.2.1 Local Platforms

A local installation is an installation of the driver on the Metadirectory server. You can install the Workday driver on the operating systems supported for the Metadirectory server.

For information about the operating systems supported for the Metadirectory server, see [NetIQ Identity Manager Overview and Planning Guide](../../../identity-manager-49/idm_overview_planning/data/netiq-identity-manager-overview-and-planning.html#netiq-identity-manager-overview-and-planning) in the [NetIQ Identity Manager Overview and Planning Guide](../../../identity-manager-49/idm_overview_planning/data/netiq-identity-manager-overview-and-planning.html#netiq-identity-manager-overview-and-planning).

![](../graphics/workday-local-3.png)

## 1.2.2 Remote Platforms

The Workday driver can use the Remote Loader service to run on a server other than the Metadirectory server. You can install the Workday driver on the operating systems supported for the Remote Loader.

For information about the supported operating systems, see [NetIQ Identity Manager Install and Upgrade Guide for Linux](../../../identity-manager-49/setup_linux/data/front.html#front).

![](../graphics/workday-remote-loader-3.png)

## 1.2.3 Supported Operations

The Workday driver supports the following operations on the Subscriber channel:

* Update user ID.

  When a user is renamed in IDV, the driver updates the user ID back in the Workday.
* Update user attributes such as email id, phone number, Custom IDs in Identity Vault.

  When a user is updated in IDV, the updated user information can be synchronized with Workday.

  *NOTE:*The delete operation for email ID and primary phone number (work and home) is not supported in the Identity Vault.
* Add and Modify operations of photo object in IDV.
* Managing permissions through user-based security groups and organizational roles.

*NOTE:*Workday driver does not support the following:

* Creating and deleting users in Workday
* Password synchronization

The following operations are supported on the Publisher channel:

* Users Object:

  + Add users (Employee and Contingent Worker Both)
  + Modify users

    When a user is updated in Workday, the updated user information is synchronized with the IDV.
  + Delete users

    Users cannot be deleted in Workday, hence there will be no delete event from workday.
  + Position or Relation object: Each job /position is treated as relation irrespective of primary position or non-primary position. The primary position information is also stored as part of the user object.
  + Location Object: Driver synchronizes locations and creates a separate object in IDV.
  + Job Family Object: Driver synchronizes job family and creates a separate object in IDV.
  + Job Profile Object: Driver synchronizes job profile and creates a separate object in IDV.
  + Organization Object: Driver synchronizes organizations and creates a separate object in IDV. Organization is configurable and can have different values such as Cost Center, Company, and HR Company etc.
  + Worker Photo Object: Driver synchronizes worker’s photo from Workday.
