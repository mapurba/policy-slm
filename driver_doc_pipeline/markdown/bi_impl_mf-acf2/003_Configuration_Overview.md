# 1.2 Configuration Overview

This section discusses driver configuration details specific to the Identity Manager driver for ACF2. For basic configuration information, see the Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-48/). For detailed information about configuring the driver, see [Section 5.0, Configuring the ACF2 Driver](b3r8t50.html).

The following topics include each Designer ACF2 Package available for configuration:

* [ACF2 Base](b3wx9up.html#b3wxdf3)
* [ACF2 Default Configuration](b3wx9up.html#b685bxb)
* [ACF2 Entitlements](b3wx9up.html#bmn6zec)
* [ACF2 Password Synchronization](b3wx9up.html#b3wyopl)
* [ACF2 Account Tracking](b3wx9up.html#b12zb180)
* [ACF2 Managed System Information](b3wx9up.html#b12zb8hl)

## 1.2.1 ACF2 Base

The ACF2 Base provides the policies and settings necessary to provide a basic functioning ACF2 Driver.

The ACF2 Base Package includes the following Global Configuration Variables:

* *Remote Loader:*
  A boolean true/false value indicating whether or not to use the Remote Loader service. For this driver, this value should always be set to true.
* *Host Name:*
  The physical DNS hostname or IP address for the ACF2 system to connect to.
* *Port:*
  The TCP/IP port of the remote loader running on the ACF2 system (default 8090).
* *KMO:*
  The SSL KMO object to use for secure communication.
* *Remote Password:*
  The remote loader password.
* *Driver Password:*
  The driver object password.

The ACF2 Base Package provides the following Identity Manager policies:

* *NOVLACF2BASE-ot-AppendACF2CMD:*
  This output transform converts XDS documents from the Subscriber channel into ACF2 commands that will be executed by the ACF2 driver shim.
* *NOVLACF2BASE-it-ChangeLog:*
  This input transform converts ACF2 ChangeLog events into XDS that can be interpreted by the rest of the Publisher channel.

## 1.2.2 ACF2 Default Configuration

The ACF2 Default Configuration provides a set of configuration settings to begin synchronizing ACF2 Logonid records with Identity Vault users.

The ACF2 Default Configuration Package includes the following Global Configuration Variables (GCVs):

* *User Base Container:*
  A DN value that represents a container in the Identity Vault from which Subscriber events are restricted from and new and matched User objects are created under on the Publisher channel.
* *Subscriber Passphrase Synchronization:*
  A boolean true/false value indicating whether to synchronize Vault passwords with ACF2 passphrases.
* *Publisher Passphrase Synchronization:*
  A boolean true/false value indicating whether to synchronize ACF2 passphrases with Vault passwords.

The ACF2 Default Configuration Package provides the following Identity Manager policies:

* *NOVLACF2DCFG-pub-cp:*
  This Publisher Create Policy provides a default Surname using either the Full Name field or Association value from the add event.
* *NOVLACF2DCFG-pub-mp:*
  This Publisher Matching Policy attempts to match Users by the CN attribute within the User Base Container GCV.
* *NOVLACF2DCFG-pub-pp:*
  This Publisher Placement Policy sets the target DN for new users to be the concatenation of the User Base Container GCV and the lowercase value of the CN attribute.
* *NOVLACF2DCFG-sub-cp:*
  This Subscriber Create Policy requires the CN and Password and reformats the CN value to be uppercase.
* *NOVLACF2DCFG-sub-et:*
  This Subscriber Event Transform vetoes events not in the User Base Container and also renames and moves.
* *NOVLACF2DCFG-sub-mp:*
  This Subscriber Matching Policy queries ACF2 for Users that match the CN attribute.

The ACF2 Default Configuration Package provides the NOVLACF2DCFG-smp schema mapping policy and the NOVLACF2DCFG-filter filter policy. See [Default ACF2 Schema](b13qy5am.html) for details.

*Table 1-2* Default Schema Mapping and Filter

| eDirectory Class | eDirectory Attribute | ACF2 Record | ACF2 Field |
| User | CN | Logonid | LID |
| User | Login Disabled | Logonid | SUSPEND |
| User | nspmDistributionPassword | Logonid | PASSWORD |
| User | Full Name | Logonid | NAME |
| User | Telephone Number | Logonid | PHONE |

In addition, the remaining ACF2 fields are automatically mapped to corresponding attributes in the ACF2 Auxiliary Schema. For a complete list, see [Table C-5](bmn9uvw.html#bqkp2ae). Each additional auxiliary attribute in the filter is intentionally set to ignore on both channels by default, so they can be conveniently configured otherwise if necessary.

## 1.2.3 ACF2 Entitlements

The ACF2 Entitlements Package provides a basic entitlement for an ACF2 Logonid record. This package leverages the DirXML-EntitlementsRef attribute, set by the Role Based Entitlements Driver. When entitlements are granted or revoked, you can take the appropriate action in ACF2 by creating, suspending or deleting the Logonid record.

The ACF2 Entitlements Package provides the following Identity Manager policies:

* *NOVLACF2ENT-pub-et-DisallowDeletes:*
  When this Publisher Event Transformation detects a user is deleted from ACF2, it removes the user’s Vault association and vetoes the event.
* *NOVLACF2ENT-sub-cp-EntitlementsImpl:*
  This Subscriber Create Policy blocks account creation when an Entitlement is not granted.
* *NOVLACF2ENT-sub-ct-EntitlementsImpl:*
  When this Subscriber Command Transformation detects a removed entitlement, it results in a delete or suspension. It is based upon the on-account-remove GCV.
* *NOVLACF2ENT-sub-mp-EntitlementsImpl:*
  When this Subscriber Matching Policy detects an ACF2 User account managed by entitlements, it vetoes the matching existing account.

The ACF2 Entitlements Package also provides a filter that includes the User attribute DirXML-EntitlementsRef. This attribute, configured for notification on the Subscriber channel, is set outside the driver whenever a process grants or removes an entitlement for a User.

## 1.2.4 ACF2 Password Synchronization

The ACF2 Password Synchronization Package leverages the Common Password Synchronization policies to provide email notifications for failed password synchronization and configuration options for Universal Passwords.

The ACF2 Password Synchronization Package provides the following Identity Manager policies:

* *NOVLPWDSYNC-pub-ctp-AddPwdPayload:*
  Publish password payloads.
* *NOVLPWDSYNC-pub-ctp-CheckPwdGCV:*
  Publish password changes.
* *NOVLPWDSYNC-pub-ctp-DefaultPwd:*
  On User add, provide default password if none exists.
* *NOVLPWDSYNC-pub-ctp-PublishDistPwd:*
  Publish passwords to NMAS distribution password.
* *NOVLPWDSYNC-pub-ctp-PublishNDSPwd:*
  Publish passwords to NDS password.
* *NOVLPWDSYNC-sub-ctp-AddPwdPayload:*
  Payloads for subscribe to password changes.
* *NOVLPWDSYNC-sub-ctp-CheckPwdGCV:*
  Subscribe to password changes.
* *NOVLPWDSYNC-sub-ctp-DefaultPwd:*
  On User add, provide default password of Surname if no password exists.
* *NOVLPWDSYNC-sub-ctp-TransformDistPwd:*
  Transform NMAS attribute to password elements.
* *NOVLPWDSYNC-itp-EmailOnFailedPwdSub:*
  Email notifications for failed password subscriptions.
* *NOVLPWDSYNC-otp-EmailOnFailedPwdPub:*
  Email notifications for failed password publications.

The ACF2 Password Synchronization Package includes the following Global Configuration Variables (GCVs):

* *Connected System or Driver Name:*
  The name of the connected system, application or Identity Manager driver. This value is used by the e-mail notification templates.
* *Application accepts passwords from Identity Manager:*
  Option to allow passwords to flow from the Identity Manager vault to the connected system.
* *Identity Manager accepts passwords from application:*
  Option to allow passwords to flow from the connected system to the Identity Manager data store.
* *Publish passwords to NDS password:*
  Use the password from the connected system to set the non-reversible NDS password in eDirectory.
* *Publish passwords to Distribution Password:*
  Use the password from the connected system to set the NMAS Distribution Password used for Identity Manager password synchronization.
* *Require password policy validation before publishing passwords:*
  Option to apply the NMAS password policies during password operations on the Publisher channel. The password is not written to the data store if it does not comply.
* *Reset user’s external system password to the Identity Manager password on failure:*
  Attempt to reset the password in the connected system by using the Distribution Password from the Identity Vault when a publish Distribution Password failure occurs.
* *Notify the user of password synchronization failure via e-mail:*
  Notify the user of a password synchronization failure via email.

## 1.2.5 ACF2 Account Tracking

The ACF2 Account Tracking Package allows the driver to track the accounts and identities of each user in your system.

The ACF2 Account Tracking Package (with the prerequisite Data Collection Common and Account Tracking Common packages) provides the following Identity Manager policies:

* *NOVLATRKBASE-itp-Publish*
* *NOVLATRKBASE-itp-WriteAccounts*
* *NOVLATRKBASE-otp-Subscribe*
* *NOVLDATACOLL-itp-DataCollectionQuerySupport:*
  Convert selected attributes to a form most commonly used in the Identity Vault.
* *NOVLDATACOLL-smp-SkipSchemaMapping*

The ACF2 Account Tracking Package (with the prerequisite Data Collection Common and Account Tracking Common packages) includes the following Global Configuration Variables (GCVs):

* *Enable account tracking:*
  If true, account tracking policies are enabled. If false, account tracking policies are not executed.
* *Realm:*
  Name of realm. The realm must be set to the ACF2 DNS name (Example: acf2.yourcompany.org).
* *Object class:*
  Add the object class to track. Class names must be in the application namespace.
* *Identifiers:*
  Add the account identifier attributes. Attribute names must be in the application namespace.
* *Status attribute:*
  Name of the attribute in the application namespace to represent the account status.
* *Status active value:*
  Value of the status attribute that represents an active state.
* *Status inactive value:*
  Value of the status attribute that represents an inactive state.
* *Subscription default status:*
  Default status the policies will assume when an object is subscribed to the application and the status attribute is not set in the identity vault.
* *Publication default status:*
  Default status the policies will assume when an object is published to the identity vault and the status attribute is not set in the application.

## 1.2.6 ACF2 Managed System Information

The ACF2 Managed System Information Package provides settings that help the Identity Reporting Module generate reports.

The ACF2 Managed System Information Package includes the following Global Configuration Variables (GCVs):

* *General Information*

  + *Name:*
    Descriptive name for the ACF2 connected system. This name is displayed in the reports.
  + *Description:*
    Brief description of this connected ACF2 system. This description is displayed in the reports.
  + *Location:*
    The physical location of this connected ACF2 system. This location is displayed in the reports.
  + *Vendor:*
    The vendor of this connected ACF2 system (Computer Associates). This information is displayed in the reports.
  + *Version:*
    The version of this connected ACF2 system. This version information is displayed in the reports.
* *System Ownership*

  + *Business Owner*
  + *Application Owner*
* *System Classification*

  + *Classification*
  + *Environment*
* *Connection and miscellaneous Information:*
  This options is always set to hide so that you don’t make changes to these options. These options are system options that are necessary for reporting to work. If you make any changes, reporting stops working.
