# 1.4 Key Driver Features

The following sections provide information about the standard driver features supported by the Oracle EBS drivers:

* [Driver Packages](key-driver-features.html#alvqsdq)
* [Supported Operations](key-driver-features.html#alvqsqp)

## 1.4.1 Password Synchronization

The Subscriber channel sets the password. Passwords are not synchronized on the Publisher channel. This means that passwords are synchronized from the Identity Vault to the Oracle EBS system, but not from the Oracle EBS system to the Identity Vault. This feature is not needed for the HR driver.

## 1.4.2 Entitlements

The Oracle EBS drivers driver implements entitlements. You can use entitlements to grant or revoke rights to an account in the driver. You should enable entitlements for the drivers only if you plan to use the User Application or Role-Based Entitlements with the drivers. For more information about entitlements, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).

*NOTE:*The HR driver only supports the employee entitlement.

## 1.4.3 Object Synchronization

The Oracle EBS drivers synchronize users on the Subscriber and Publisher channels.

## 1.4.4 Driver Packages

The Identity Manager content is delivered in packages. The packages create a driver with a set of policies suitable for synchronizing data with the Identity Vault. The following packages provide basic functionality for configuring the Oracle EBS drivers:

#### Common Packages

* NOVLEBSATRK
* NOVLEBSAENT
* NOVLEBSENT
* NOVLEBSMSI
* NOVLPWDSYNC
* NOVLEBSPWD

#### Packages for the User Management Driver

* NOVLORAUBASE
* NOVLORAUDCFG

#### Packages for the HR Driver

* NOVLORAHBASE
* NOVLORAHDCFG
* NOVLORAHENT
* NOVLORAHATRK

#### Packages for the TCA Driver

* NOVLORATBASE
* NOVLORATDCFG

## 1.4.5 Supported Operations

The Oracle EBS drivers support Add, Modify, Delete, Rename, Move, Future Add or Delete, Migrate, and Password Synchronization operations on the user objects on the Subscriber channels. All of them except Password Synchronization are supported on the Publisher channel.
