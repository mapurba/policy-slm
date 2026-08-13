# 1.3 Key Features

This section discuses the following key features of the driver:

* [Local Platforms](key-features.html#b1d4wt77)
* [Remote Platforms](key-features.html#b1d4wt78)
* [Entitlements](key-features.html#b1d4yakl)
* [Password Synchronization](key-features.html#b1d4wrnn)
* [Data Synchronization](key-features.html#b1d4wrno)
* [Driver Shim](key-features.html#abbcqgv)
* [Driver Packages](key-features.html#b1d4ygp2)

## 1.3.1 Local Platforms

A local installation is an installation of the driver on the Identity Manager server. You can install the GroupWise driver on all operating systems supported for the Identity Manager server.

## 1.3.2 Remote Platforms

The GroupWise driver can use the Remote Loader service to run on a server other than the Identity Manager server. The Remote Loader enables the driver to communicate with the Identity Manager server.

## 1.3.3 Entitlements

The GroupWise driver supports the following entitlements by default:

* *UserAccount:*
  This entitlement grants or revokes a GroupWise account for a specified user. When this entitlement is granted, the driver provides an enabled logon account. When this entitlement is revoked, the driver either disables or deletes the logon account, depending on the driver configuration.
* *Group:*
  This entitlement grants or revokes membership to a group in GroupWise. When the entitlement is revoked, Identity Manager removes the user from the group.

If you upgrade a lower version of the GroupWise driver to the latest GroupWise driver, the upgraded driver performs the following actions by using the entitlements:

* Adds user object accounts
* Removes, disables, or expires user object accounts
* Adds members to a group
* Removes members from a group
* Adds members to a distribution list
* Removes members from a distribution list

## 1.3.4 Password Synchronization

The Subscriber channel sets the password. Passwords are not synchronized on the Publisher channel. The passwords are synchronized from the Identity Vault to GroupWise system, but not from GroupWise system to the Identity Vault.

## 1.3.5 Data Synchronization

The GroupWise driver synchronizes users, groups, and organizational unit.

If you upgrade a lower version of the GroupWise driver to the latest GroupWise driver, the upgraded driver synchronizes users, groups, distribution lists, external entities, organizational unit, and post offices.

## 1.3.6 Driver Shim

The driver uses a Java based driver shim to communicate between the Identity Manager engine and GroupWise REST APIs. The driver shim converts the XML-based Identity Manager command and event language (XDS) to the protocols and REST API calls required to interact with GroupWise.

The shim for GroupWise is com.novell.gw.dirxml.driver.rest.shim.GWdriverShim. For information about installing the driver shim, see [Installing the Driver Shim](install-driver-shim.html).

## 1.3.7 Driver Packages

The GroupWise driver packages are available on the Package Update site. When the driver is created with packages in Designer, a set of policies and rules are created suitable for synchronizing with GroupWise.

For creating a new driver, use the following packages:

* GroupWise REST Account Tracking version 3.0.0
* GroupWise REST Audit Entitlements version 3.0.0
* GroupWise REST Base version 3.2.0
* GroupWise REST Default Configuration version 3.2.0
* GroupWise REST Entitlements version 3.1.0
* GroupWise REST Managed System Information version 3.0.0
* GroupWise REST Password Synchronization version 3.2.0

For upgrading to the latest GroupWise driver, use the following packages:

* GroupWise Account Tracking version 2.5.1
* GroupWise Audit Entitlements version 2.5.0
* GroupWise Base version 2.6.0
* GroupWise Entitlements version 2.5.1
* GroupWise Managed System Information version 2.5.0
* GroupWise Password Synchronization version 2.6.0

*IMPORTANT:*Use these packages only if you are upgrading your existing driver to the latest GroupWise driver. They are not meant for connecting to GroupWise 2012 or lower versions of GroupWise. Download these packages from the [Package Update site](http://cdn.novell.com/cached/designer/packages/idm/customupdatesite2_0_0/).

To configure your driver to connect to GroupWise 2012 or lower versions, use packages with versions less than 2.5 from the [Package Update site](http://cdn.novell.com/cached/designer/packages/idm/updatesite2_0_0/).
