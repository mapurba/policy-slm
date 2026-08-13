# 1.2 Configuration Overview

This section discusses driver configuration details specific to the Linux and UNIX driver. For basic configuration information, see the Identity Manager 4.8 Administration Guide. For detailed information about configuring the Linux and UNIX driver, see [Section 5.0, Configuring the Linux and UNIX Driver](b3r8t50.html).

## 1.2.1 Data Flow

Filters and policies control the data flow of users and groups to and from the connected system and the Identity Vault. The Data Flow option, specified during driver import, determines how these filters and policies behave.

* *Bidirectional:*
  Sets classes and attributes to be synchronized on both the Subscriber and Publisher channels.
* *Application to Identity Vault:*
  Sets classes and attributes to be synchronized on the Publisher channel only.
* *Identity Vault to Application:*
  Sets classes and attributes to be synchronized on the Subscriber channel only.

## 1.2.2 POSIX Information Management

The Linux and UNIX driver uses the RFC 2307 posixAccount and posixGroup attributes. You can use these classes to maintain the Linux and UNIX attributes between corresponding users and groups in the connected system and the Identity Vault.

The POSIX Information Management option, specified during driver import, provides management methods for RFC 2307 posixAccount and posixGroup attributes, such as uidNumber, gidNumber, homeDirectory, loginShell, and memberUid.

* *Manage Local:*
  The connected system maintains all the RFC 2307 information. RFC 2307 information is not created or stored in the Identity Vault. RFC 2307 schema extensions are not required. This option is useful for maintaining UID and GID information on multiple systems separately.
* *Manage from Identity Vault:*
  The Identity Vault provides and maintains all RFC 2307 information for users and groups. RFC 2307 information must be present in the Identity Vault before users and groups can be provisioned to the connected system.
* *Manage Bidirectional:*
  RFC 2307 information can be created and managed by both the Identity Vault and the connected system.

## 1.2.3 Filter and Schema Mapping

The Metadirectory engine uses filters to control which objects and attributes are shared. The default filter configuration for the Linux and UNIX driver allows objects and attributes to be shared as described in the following table:

*Table 1-1* Default Linux and UNIX Driver Filter and Schema Mapping

| eDirectory Class | eDirectory Attribute | Linux and UNIX Class | Linux and UNIX Attribute |
| User | CN | User | loginName |
| User | gecos | User | gecos |
| User | gidNumber | User | gidNumber |
| User | homeDirectory | User | homeDirectory |
| User | loginShell | User | loginShell |
| User | uidNumber | User | uidNumber |
| User | Group Membership | User | gidNumber |
| Group | CN | Group | groupName |
| Group | gidNumber | Group | gidNumber |
| Group | member | Group | memberUid |

## 1.2.4 Policies

The Metadirectory engine uses policies to control the flow of information into and out of the Identity Vault. The following table describes the policy functions for the Linux and UNIX driver in the default configuration:

*Table 1-2* Default Linux and UNIX Driver Policy Functions

| Policy | Description |
| Mapping | Maps the Identity Vault User and Group objects and selected attributes to a Linux or UNIX user or group. |
| Publisher Event | None is provided. |
| Publisher Matching | Restricts privileged accounts and defines matching criteria for placement in the Identity Vault. |
| Publisher Create | Defines creation rules for users and groups before provisioning into the Identity Vault. |
| Publisher Placement | Defines where new users and groups are placed in the Identity Vault. |
| Publisher Command | Defines password publishing policies. |
| Subscriber Matching | Defines rules for matching users and groups in the connected system. |
| Subscriber Create | Defines required creation criteria. |
| Subscriber Command | Transforms RFC 2307 attributes and defines password subscribing policies. |
| Subscriber Output | Sends e-mail notifications for password failures and converts information formats from the Identity Vault to the connected system. |
| Subscriber Event | Restricts events to a specified container. |
