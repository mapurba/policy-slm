# 1.2 Configuration Overview

This section discusses driver configuration details specific to the Identity Manager driver for RACF. For basic configuration information, see the Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/). For detailed information about configuring the driver, see [Section 5.0, Configuring the RACF Driver](b3r8t50.html).

Topics include

* [Data Flow](b3wx9up.html#b3wxdf3)
* [OMVS Information Management](b3wx9up.html#b685bxb)
* [TSO Information Management](b3wx9up.html#b3wxh6t)
* [Filter and Schema Mapping](b3wx9up.html#b3wyla3)
* [RACF Password Phrases](b3wx9up.html#bmn6zec)
* [Policies](b3wx9up.html#b3wyopl)

## 1.2.1 Data Flow

Filters and policies control the data flow of users and groups to and from the connected system and the Identity Vault. The Data Flow option, specified during driver import, determines how these filters and policies behave:

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

* *ACCT:*
  The default account number
* *PROC:*
  The default logon procedure
* *UNIT:*
  The default unit name

## 1.2.4 Filter and Schema Mapping

The Metadirectory engine uses filters to control which objects and attributes are shared. The default filter configuration for the driver allows objects and attributes to be shared as described in the following table:

*Table 1-2* Default Filter and Schema Mapping

| eDirectory Class | eDirectory Attribute | RACF Class | RACF Attribute |
| User | CN | User | DirXML-RACF-userid |
| User | Group Membership | User | DirXML-RACF-groups |
| User | Login Disabled | User | DirXML-RACF-revoked |
| User | Login Expiration Time | User | DirXML-RACF-revokedate |
| User | Password Expiration Interval | User | DirXML-RACF-password-interval |
| User | Password Expiration Time | User | DirXML-RACF-expired |
| Group | CN | Group | DirXML-RACF-group |

## 1.2.5 RACF Password Phrases

In z/OS 1.10, RACF supports password phrases, which may be case-sensitive and up to 100 characters in length. This is a departure from the previous requirements for RACF passwords, in which you were allowed a maximum of 8 non-case-sensitive characters. You can allow the driver to capture and synchronize RACF password phrases by selecting this option.

## 1.2.6 Policies

The Metadirectory engine uses policies—each with its own set of specific rules—to control the flow of information into and out of the Identity Vault. This section describes each policy and its rules.

### Subscriber Policies

This section describes policies categorized under the Subscriber channel.

#### Event Transformation Policies

The driver includes one policy in this category: NOVLRACFDCFG-sub-et. Its purpose is to:

* Veto events that fall outside of the configured container scope for Users and Groups
* Veto move and rename events, which are not natively supported by RACF

#### Matching Policies

One policy exists in this category: NOVLRACFDCFG-sub-mp. The purpose of this policy is to query the RACF database for objects matching the CN attribute value of the User or Group event being processed.

#### Creation Policies

There is one default policy, NOVLRACFDCFG-sub-cp, which provides the following:

* Require RACF password and NAME fields
* Set default Group and Owner fields

Additional package NOVLRACFOMVS-sub-cp may be added to provide:

* Default OMVS segment fields
* UID and/or GID assignments
* Configures default OMVS segment fields

Additional package NOVLRACFTSO-sub-cp may be added to provide:

* Default TSO segment fields

#### Command Transformation Policies

Four policies exist under this category. The first policy, Command Transformation, performs several tasks, depending on how the driver was imported:

* Updates the RACF NAME field, when the Given Name or Surname attributes change
* Transforms the Login Expiration Time into a a RACF revoke date format
* Transforms the Password Expiration Interval into a RACF password interval
* Transforms the Identity Vault password into a RACF pass phrase

The next three policies transform the Distribution Password into a RACF modify-password event and optionally veto the password sync if the driver is configured to do so on the Subscriber.

#### Output Transformation Policies

Three policies exist under this category:

* The first policy assigns default RACF CONNECT attributes when a Group Membership (CONNECT) is being added in RACF.
* The second policy sends an e-mail notice to any user that fails during password synchronization.
* The third policy generates a pseudo-attribute called RACFCMD. This attribute is the actual RACF command that will be executed on the RACF system.

  *IMPORTANT:*Proper execution of the default REXX scripts requires the RACFCMD pseudo-attribute. Therefore, it is imperative that this policy is not removed or modified.

### Publisher Policies

This section describes policies categorized under the Publisher channel.

#### Input Transformation Policies

Four policies exist under this category. They are designed to convert events that originated on RACF into XDS format, suitable to be processed by the Identity Vault.

*NOTE:*These policies are necessary for proper XML conversion, therefore it is imperative that these policies are not removed. Modifications to these policies require a fundamental understanding of the RACF change log format, the Java Parser and XSLT.

The first policy, TSO (RACF) Input Transform, recognizes various RACF change log document formats, including password changes, pass phrase changes and command images. This policy is an XSLT style sheet, which uses a Java parser to convert the change log format to XDS format.

The next policy, RACF Back Patch Transform, may perform queries against RACF to gather information about an event for which all necessary information is not currently available.

The next policy, Final TSO Input Transform, is the last transformation policy in the chain to handle RACF change log events. It transforms the original change log event into a Publisher status document.

The last of the input transformation policies, Password(Pub)-Sub Email Notifications, generates email notifications to users whose passwords did not synchronize properly with RACF.

#### Matching Policies

One policy exists under this category: Matching Rule. The purpose of this policy is to query the Identity Vault for User or Group objects whose CN attributes match the name of the RACF User or Group being processed.

#### Creation Policies

One policy exists under this category: Create Rule. This policy sets the required eDirectory attribute for User objects, Surname, equal to the CN value.

#### Placement Policies

One policy exists under this category: Placement Rule. This policy places User objects into the configured User container and Group objects into the configured Group container.

#### Command Transformation Policies

Four policies exists under this category. All related to user passwords, the rules in these polices:

* Strip passwords from events, if configured to do so
* Transform password events into Distribution Passwords the Login Expiration Time into a RACF revoke date format
* Add meta information to password events, to trap conditions where the sync may fail
