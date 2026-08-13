# 1.2 Driver Features

* [Local Platforms](driver-features.html#local-platforms)
* [Remote Platforms](driver-features.html#remote-platforms)
* [Entitlements](driver-features.html#entitlements)
* [Password Synchronization](driver-features.html#password-synchronization)
* [Synchronizing Data](driver-features.html#synchronizing-data)

## 1.2.1 Local Platforms

The eDirectory driver runs in any Identity Manager installation. See "[Implementation Checklist](../../../identity-manager-48/setup_linux/data/t4ah8ymr4q7y.html#t4ah8ymr4q7y)" in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or "[Planning Your Installation](../../../identity-manager-48/setup_windows/data/planning-an-identity-manager-installation.html#planning-an-identity-manager-installation)" in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

## 1.2.2 Remote Platforms

The eDirectory driver supports remote connections without the Remote Loader. The driver does not use the Remote Loader because the driver in one tree communicates directly with the driver in the other tree.

## 1.2.3 Entitlements

The basic driver configuration supports entitlements. When entitlements are enabled, the driver does the following actions by default:

* Adds User object accounts
* Removes User object accounts
* Adds members of the distribution list
* Removes members of the distribution list

The driver support entitlements you create if supporting policies are provided for implementing them. For more information about entitlements, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

*IMPORTANT:*In the driver filter, select the Application option in Merge Authority for the loginDisabled attribute in the eDirectory driver that does not have an entitlement.

## 1.2.4 Password Synchronization

The eDirectory driver supports password synchronization via Universal Password. If desired, you can also use the older form of password synchronization (Public/Private key pair or NDS password). For more information, see [Section 6.0, Synchronizing Passwords](synchronizing-passwords.html).

## 1.2.5 Synchronizing Data

The eDirectory driver synchronizes data between two Identity Vaults or trees. The driver can run anywhere that a Identity Manager server is running.
