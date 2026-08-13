# 1.2 Configuration Overview

This section discusses driver configuration details specific to the Identity Manager Driver for Top Secret. For basic configuration information, see the Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/). For detailed information about configuring the driver, see [Section 5.0, Configuring the Top Secret Driver](b3r8t50.html).

Topics include

* [Data Flow](b3wx9up.html#b3wxdf3)
* [OMVS Information Management](b3wx9up.html#b685bxb)
* [TSO Information Management](b3wx9up.html#b3wxh6t)
* [Filter and Schema Mapping](b3wx9up.html#b3wyla3)
* [Policies](b3wx9up.html#b3wyopl)

## 1.2.1 Data Flow

Filters and policies control the data flow of users and groups to and from the connected system and the Identity Vault. The Data Flow option, specified during driver import, determines how these filters and policies behave.

* *Bidirectional:*
  Sets classes and attributes to be synchronized on both the Subscriber and Publisher channels.
* *Application to Identity Vault:*
  Sets classes and attributes to be synchronized on the Publisher channel only.
* *Identity Vault to Application:*
  Sets classes and attributes to be synchronized on the Subscriber channel only.

## 1.2.2 OMVS Information Management

The Set Preconfigured OMVS Data option, specified during driver import, determines whether the driver sets preconfigured OMVS (UNIX System Services) attributes for new users in the security system.

The attributes you can configure are:

* *OMVSPGM:*
  The default program (login shell)
* *UID Assignment:*
  Whether UID and GID numbers are assigned by the security system or by the Identity Vault
* *HOME:*
  The default home directory

## 1.2.3 TSO Information Management

The Set Preconfigured TSO Data option, specified during driver import, determines whether the driver sets preconfigured Time Sharing Option (TSO) information for new users in the security system.

The attributes you can configure are:

* *TSOLACCT:*
  The default account number
* *TSOLPROC:*
  The default logon procedure
* *TSOUNIT:*
  The default unit name

## 1.2.4 Filter and Schema Mapping

The Metadirectory engine uses filters to control which objects and attributes are shared. The default filter configuration for the driver allows objects and attributes to be shared as described in the following table:

*Table 1-1* Default Filter and Schema Mapping

| eDirectory Class | eDirectory Attribute | Top Secret Class | Top Secret Attribute |
| User | CN | USER | ACID |
| User | Group Membership | USER | GROUP |
| User | Login Disabled | USER | SUSPEND |
| User | Login Expiration Time | USER | UNTIL |
| User | Password Expiration Interval | USER | PASSINT |
| User | Surname | USER | NAME |
| Group | CN | GROUP | ACID |

## 1.2.5 Policies

The Metadirectory engine uses policies to control the flow of information into and out of the Identity Vault. The following table describes the policy functions for the driver in the default configuration:

*Table 1-2* Default Driver Policy Functions

| Policy | Description |
| Mapping | Maps the Identity Vault User and Group objects and selected attributes to a user or group in the security system. |
| Publisher Input | Parses security system commands to produce XDS events. |
| Publisher Event | None is provided. |
| Publisher Matching | Restricts privileged accounts and defines matching criteria for placement in the Identity Vault. |
| Publisher Create | Defines creation rules for users and groups before provisioning into the Identity Vault. |
| Publisher Placement | Defines where new users and groups are placed in the Identity Vault.  Converts object names to lowercase. |
| Publisher Command | Defines password publishing policies. |
| Subscriber Matching | Defines rules for matching users and groups in the connected system and restricts events from a configurable container. |
| Subscriber Create | Defines required creation criteria.  Converts object names to uppercase. |
| Subscriber Command | Defines password subscribing policies. |
| Subscriber Output | Sends e-mail notifications for password failures and converts information formats from the Identity Vault to the connected system. |
