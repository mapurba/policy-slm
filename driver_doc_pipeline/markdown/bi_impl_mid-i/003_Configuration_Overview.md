# 1.2 Configuration Overview

This section discusses driver configuration details specific to the IBM i driver. For basic configuration information, see the Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/). For detailed information about configuring the IBM i driver, see [Section 6.0, Configuring the IBM i Driver](b3r8t50.html).

## 1.2.1 Data Flow

Filters and policies control the data flow of users and groups to and from the connected system and the Identity Vault. The Data Flow option, specified during driver import, determines how these filters and policies behave.

* *Bidirectional:*
  Sets classes and attributes to be synchronized on both the Subscriber and Publisher channels.
* *Application to Identity Vault:*
  Sets classes and attributes to be synchronized on the Publisher channel only.
* *Identity Vault to Application:*
  Sets classes and attributes to be synchronized on the Subscriber channel only.

## 1.2.2 Filter and Schema Mapping

Attributes of i5/OS profiles that correspond to attributes of eDirectory™ User and Group objects are mapped by the default driver filter and the schema mapping policy. The IBM i driver provides a file (i5os.sch) that you can use to add auxiliary classes to eDirectory User and Group objects to support many more IBM i user and group attributes.

The Metadirectory engine uses filters to control which objects and attributes are shared. The default filter configuration for the IBM i driver allows objects and attributes to be shared as described in [Table 1-2](b3wx9up.html#b4r8562) and [Table 1-3](b3wx9up.html#b4r8dxo).

The eDirectory class User corresponds to the IBM i class UserProfile.

*Table 1-2* Default eDirectory User to i5/OS UserProfile Mapping

| eDirectory User Attribute | i5/OS UserProfile Attribute |
| CN | USRPRF |
| Description | TEXT |
| company | CMPNY |
| Facsimile Telephone Number | FAXTELNBR |
| Full Name | FULNAM |
| Given Name | FSTNAM |
| Home Directory | HOMEDIR |
| Login Disabled | STATUS |
| Postal Address | ADDR1 |
| preferredName | PREFNAM |
| Telephone Number | TELNBR1 |
| UID | UID |
| departmentNumber | DEPT |
| Initials | INITIALS |
| Title | TITLE |
| Password Expiration Interval | PWDEXPITV |
| Surname | LSTNAM |
| Generational Qualifier | GENQUAL |
| Group Membership | GroupMembership |
| nspmDistributionPassword | PASSWORD |

The eDirectory class Group corresponds to the IBM i class GroupProfile.

*Table 1-3* Default eDirectory Group to IBM i GroupProfile Mapping

| eDirectory Group Attribute | IBM i GroupProfile Attribute |
| CN | USRPRF |
| Description | TEXT |
| Member | Members |
| GID | GID |

*NOTE:*GroupMembership and Members are virtual attributes used to populate the IBM i GRPPRF and SUPGRPPRF user profile fields when the driver is configured to synchronize group membership.

## 1.2.3 Policies

The Metadirectory engine uses policies to control the flow of information into and out of the Identity Vault. The following table describes the policy functions for the IBM i driver in the default configuration:

*Table 1-4* Default i5/OS Driver Policy Functions

| Policy | Description |
| Mapping | Maps the Identity Vault User and Group objects and selected attributes to an IBM i user or group. |
| Publisher Event | None is provided. |
| Publisher Matching | Restricts privileged accounts and defines matching criteria for placement in the Identity Vault. |
| Publisher Create | Defines creation rules for users and groups before provisioning into the Identity Vault. |
| Publisher Placement | Defines where new users and groups are placed in the Identity Vault. |
| Publisher Command | Defines password publishing policies. |
| Subscriber Matching | Defines rules for matching users and groups in the connected system. |
| Subscriber Create | Defines required creation criteria. |
| Subscriber Command | Transforms IBM i attributes and defines password subscribing policies. |
| Subscriber Output | Sends e-mail notifications for password failures and converts information formats from the Identity Vault to the connected system. |
| Subscriber Event | Restricts events to a specified container. |
