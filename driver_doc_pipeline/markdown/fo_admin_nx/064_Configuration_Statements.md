# 10.3 Configuration Statements

This section describes the following platform configuration file statements:

* [ADMINPASSWORD Statement](beiffigc.html#babcdbdj)
* [ADMINUSER Statement](beiffigc.html#babjhjbe)
* [AM.GROUP.INCLUDE Statement / AM.GROUP.EXCLUDE Statement](beiffigc.html#chddjjje)
* [AM.USER.INCLUDE Statement / AM.USER.EXCLUDE Statement](beiffigc.html#chdiefij)
* [AS.USER.INCLUDE Statement / AS.USER.EXCLUDE Statement](beiffigc.html#chdgehfb)
* [ASAMDIR Statement](beiffigc.html#brg3ydu)
* [AUTHENTICATION Statement](beiffigc.html#brg3ydt)
* [CODEPAGE Statement](beiffigc.html#brg3ye5)
* [DEBUGLOGFILE Statement](beiffigc.html#brhj9dt)
* [DEBUGTOSTDOUT Statement](beiffigc.html#brhj9du)
* [DIRECTTOAUTHENTICATION Statement](beiffigc.html#chdecfdc)
* [ENTROPY Statement](beiffigc.html#chdjaiic)
* [IGNORESTANDARDEXCLUDES Statement](beiffigc.html#chdeccja)
* [LOCALE Statement](beiffigc.html#brg3ydz)
* [PASSWORDPROMPT Statement](beiffigc.html#chdieagh)
* [PASSWORDPROMPTCURRENT Statement](beiffigc.html#brsiz4c)
* [PASSWORDPROMPTCHANGE Statement](beiffigc.html#brsj16r)
* [PASSWORDPROMPTCHANGEAGAIN Statement](beiffigc.html#brsj16s)
* [PLATFORMNAME Statement](beiffigc.html#bs4q0ii)
* [PASSWORDSOURCE Statement](beiffigc.html#b15d7cqm)
* [POLLINT Statement](beiffigc.html#brg3ye0)
* [POLLRAND Statement](beiffigc.html#bhf0ja6)
* [PROVISIONING Statement](beiffigc.html#bhf0ezv)
* [RUNMODE Statement](beiffigc.html#chdihjdd)
* [SYSLOGFACILITY Statement](beiffigc.html#brg3yea)
* [TRACEFILE Statement](beiffigc.html#brhj9dv)
* [TRACETOSTDOUT Statement](beiffigc.html#brhj9dw)
* [UPDATEPASSWORD Statement](beiffigc.html#chdfcbba)
* [CRYPTTYPE Statement](beiffigc.html#bucg2ea)
* [UPDATESAMBA Statement](beiffigc.html#chdbhfia)
* [USEFILEIPC Statement](beiffigc.html#bbrsqhu)
* [EXCLUDEUNMANAGED Statement](beiffigc.html#bi12f0d)

## 10.3.1 ADMINPASSWORD Statement

The ADMINPASSWORD statement specifies the password of the administrative user specified by the ADMINUSER statement. If there is no ADMINPASSWORD statement, you are prompted to enter the password when obtaining a platform security certificate.

Syntax:

```
ADMINPASSWORD Pswd
```

Pswd specifies the password of the administrative user.

Example:

```
ADMINPASSWORD 18emf25dhf
```

## 10.3.2 ADMINUSER Statement

The ADMINUSER statement specifies the fully distinguished name of an eDirectory user with Read and Create object rights to the ASAM System container. If there is no ADMINUSER statement, you are prompted to enter a user object name when obtaining a platform security certificate.

Syntax:

```
ADMINUSER Fdn
```

Fdn specifies the fully distinguished name of an eDirectory user with Read and Create object rights to the ASAM System container.

Example:

```
ADMINUSER .Admin.DigitalAirlines
```

## 10.3.3 AM.GROUP.INCLUDE Statement / AM.GROUP.EXCLUDE Statement

AM.GROUP.INCLUDE and AM.GROUP.EXCLUDE provide a list of specific groups or group masks to be included or excluded from Identity Provisioning. This can be useful for installation verification and early implementation and for special groups that should be managed locally. Multiple AM.GROUP.INCLUDE and AM.GROUP.EXCLUDE statements can be coded, and they can be mixed together. There is no limit to the number of groups that can be included or excluded.

Syntax:

```
AM.GROUP.INCLUDE GroupMask[ GroupMask, GroupMask ...]
```

```
AM.GROUP.EXCLUDE GroupMask[ GroupMask, GroupMask ...]
```

GroupMask can be a single complete group name, or it can include masking characters to represent more than one group. If more than one GroupMask matches a given group, the most specific GroupMask is used. GroupMask is case-insensitive. For more information, see [Mask Characters and Examples](beibhfbg.html#chdfbaee).

Unless AM.GROUP.EXCLUDE \* is coded, AM.GROUP.INCLUDE \* is always assumed. Certain special groups are always excluded unless the IGNORESTANDARDEXCLUDES statement is specified. For details, see [IGNORESTANDARDEXCLUDES Statement](beiffigc.html#chdeccja).

Do not code both an AM.GROUP.INCLUDE statement and an AM.GROUP.EXCLUDE statement.

For more information, see [Using Include and Exclude Configuration Statements](beibhfbg.html).

Example:

```
AM.GROUP.EXCLUDE sales, mkt*
```

## 10.3.4 AM.USER.INCLUDE Statement / AM.USER.EXCLUDE Statement

AM.USER.INCLUDE and AM.USER.EXCLUDE provide a list of specific user IDs or user ID masks to be included or excluded from Identity Provisioning. This can be useful for installation verification and early implementation and for special user IDs that should be managed locally. Multiple AM.USER.INCLUDE and AM.USER.EXCLUDE statements can be coded, and they can be mixed together. There is no limit to the number of users that can be included or excluded.

Syntax:

```
AM.USER.INCLUDE UserMask[ UserMask, UserMask ...]
```

```
AM.USER.EXCLUDE UserMask[ UserMask, UserMask ...]
```

UserMask can be a single complete user ID, or it can include masking characters to represent more than one user ID. If more than one UserMask matches a given user ID, the most specific UserMask is used. UserMask is case-insensitive. For more information, see [Mask Characters and Examples](beibhfbg.html#chdfbaee).

Unless AM.USER.EXCLUDE \* is coded, AM.USER.INCLUDE \* is always assumed. Certain special users are always excluded unless the INGORESTANDARDEXCLUDES statement is specified. For details, see [IGNORESTANDARDEXCLUDES Statement](beiffigc.html#chdeccja).

Do not code both an AM.USER.INCLUDE \* statement and an AM.USER.EXCLUDE \* statement.

Identity Manager Fan-Out Driver Linux/UNIX platforms always manage root locally.

For more information, see [Using Include and Exclude Configuration Statements](beibhfbg.html).

Example:

```
AM.USER.EXCLUDE act*, billing%, sys*, sales48
```

## 10.3.5 AS.USER.INCLUDE Statement / AS.USER.EXCLUDE Statement

AS.USER.INCLUDE and AS.USER.EXCLUDE provide a list of specific user IDs or user ID masks to be included or excluded from Authentication Services. This can be useful for installation verification and early implementation and for special user IDs that should be authenticated locally. Multiple AS.USER.INCLUDE and AS.USER.EXCLUDE statements can be coded, and they can be mixed together. There is no limit to the number of users that can be included or excluded, although a large list can cause a performance impact because it must be searched for every user login. These statements apply to system authentications only and are not used by the AS Client API routines (although there is an API call to test whether a user ID is excluded).

Syntax:

```
AS.USER.INCLUDE UserMask[ UserMask, UserMask ...]
```

```
AS.USER.EXCLUDE UserMask[ UserMask, UserMask ...]
```

UserMask can be a single complete user ID, or it can include masking characters to represent more than one user ID. If more than one UserMask matches a given user ID, the most specific UserMask is used. UserMask is case-insensitive. For more information, see [Mask Characters and Examples](beibhfbg.html#chdfbaee).

Unless AS.USER.EXCLUDE \* is coded, AS.USER.INCLUDE \* is always assumed. Certain special users are always excluded unless the INGORESTANDARDEXCLUDES statement is specified. For details, see [IGNORESTANDARDEXCLUDES Statement](beiffigc.html#chdeccja).

Do not code both an AS.USER.INCLUDE \* statement and an AS.USER.EXCLUDE \* statement.

For more information, see [Using Include and Exclude Configuration Statements](beibhfbg.html).

Example:

```
AS.USER.EXCLUDE act*, billing%, sys*, sales48
```

## 10.3.6 ASAMDIR Statement

The ASAMDIR statement specifies the file path where the Identity Manager Fan-Out Driver is installed. Fan-Out Driver components use ASAMDIR to find files needed for execution.

Syntax:

```
ASAMDIR FilePath
```

FilePath specifies the location in file system where the component is installed. If there is no ASAMDIR statement, FilePath defaults as follows:

* *z/OS:*
  /usr/local/ASAM in HFS
* *IBM i:*
  /usr/local/ASAM
* *Linux and UNIX:*
  /usr/local/ASAM
* *Windows:*
  c:\novell\asam

Example:

```
ASAMDIR c:\novell\asam
```

## 10.3.7 AUTHENTICATION Statement

The AUTHENTICATION statement specifies the network address and port of one Core Driver used for Authentication Services. In order to use Authentication Services, you must have at least one AUTHENTICATION statement in your configuration file.

A maximum of 100 AUTHENTICATION statements can be coded.

Syntax:

```
AUTHENTICATION Address [PORT PortNumber] [PREF PrefGroup]
```

Address specifies the DNS name or IP address of a Core Driver used for Authentication Services.

PortNumber specifies the TCP port number that is to be used to communicate with this Core Driver. PORT is optional. PortNumber defaults to 3451.

*IMPORTANT:*If you specify a port number other than the default, you must also use the Web interface to specify the same port number for the Core Driver configuration object.

PrefGroup specifies the Preference Group Number that determines the way a Core Driver is selected. It is optional, and the default is for all Core Drivers listed to be in Preference Group 1. Core Drivers within a Preference Group are selected equally for load balancing. Core Drivers with the lowest Preference Group Number are always tried first, followed by the Core Drivers with the next Preference Group Number, and so on, until a Core Driver can be contacted. Preference Group Number must be coded as a positive integer.

Examples:

```
AUTHENTICATION cdriver1.digitalairlines.com
AUTHENTICATION cdriver2.digitalairlines.com
AUTHENTICATION cdriver5.digitalairlines.com PORT 5009 PREF 2
```

## 10.3.8 CODEPAGE Statement

The CODEPAGE statement specifies a code page to be used by the Platform Receiver. Data received and sent by the Platform Receiver is encoded in UTF-8.

Syntax:

```
CODEPAGE   CodepageID
```

CodepageID specifies the code page to be used by the Platform Receiver for converting values from and to UTF-8. For information about the available choices for CodepageID, see the man page for iconv on your system.

If no CODEPAGE statement is present, UTF-8 values are used without conversion.

Example:

```
CODEPAGE iso88591
```

## 10.3.9 DEBUGLOGFILE Statement

The DEBUGLOGFILE statement specifies a destination file for debugging data written when the -d command line parameter is present for a component.

Syntax:

```
DEBUGLOGFILE FilePath
```

FilePath specifies the location in file system where the debugging output is to be written.

Example:

```
DEBUGLOGFILE /usr/local/ASAM/debug.txt
```

## 10.3.10 DEBUGTOSTDOUT Statement

The DEBUGTOSTDOUT statement specifies that debugging data is to be written to the standard output channel stdout when the -d command line parameter is present for a component.

Syntax:

```
DEBUGTOSTDOUT
```

Example:

```
DEBUGTOSTDOUT
```

## 10.3.11 DIRECTTOAUTHENTICATION Statement

The DIRECTTOAUTHENTICATION statement causes Authentication Services to connect directly to a Core Driver for Authentication Services without using the Platform Services Process. Use the DIRECTTOAUTHENTICATION statement on platforms where the volume of traffic with Core Drivers is so low that running the Platform Services Process is not justified.

Platforms using the DIRECTTOAUTHENTICATION statement do not perform Core Driver load balancing, although failover support is available if you specify multiple AUTHENTICATION statements.

Syntax:

```
DIRECTTOAUTHENTICATION
```

Example:

```
DIRECTTOAUTHENTICATION
```

## 10.3.12 ENTROPY Statement

The ENTROPY statement specifies the file where components obtain entropy for SSL.

Syntax:

```
ENTROPY   FilePath
```

FilePath specifies the file that contains entropy.

If no ENTROPY statement is coded, the default is to use the /dev/random device for entropy. If there is no /dev/random device, the default entropy file is /etc/entropy.

If your platform has a /dev/random device, you do not need to code an ENTROPY statement.

Example:

```
ENTROPY /etc/entropy
```

## 10.3.13 IGNORESTANDARDEXCLUDES Statement

The IGNORESTANDARDEXCLUDES statement specifies that the standard list of users and groups excluded from Identity Provisioning and Authentication Services processing is not used. If this statement is not present, the standard list of excludes is used. For the standard list of excluded users and groups, see [Standard Exclude List](babchigb.html).

Syntax:

```
IGNORESTANDARDEXCLUDES
```

Example:

```
IGNORESTANDARDEXCLUDES
```

## 10.3.14 LOCALE Statement

The LOCALE statement identifies the language to be used by the component.

Syntax:

```
LOCALE Id
```

Id specifies the two-character ISO 639 language identifier.

Example:

```
LOCAL en
```

## 10.3.15 PASSWORDPROMPT Statement

The PASSWORDPROMPT statement specifies the prompt issued by the PAM module to request the user's password for authentication.

Syntax:

```
PASSWORDPROMPT Text
```

If there is no PASSWORDPROMPT statement, Text defaults to

```
"NDS Password: "
```

Example:

```
PASSWORDPROMPT "Password: "
```

## 10.3.16 PASSWORDPROMPTCURRENT Statement

The PASSWORDPROMPTCURRENT statement specifies the prompt issued by the PAM module to request the user's current password for password changes.

Syntax:

```
PASSWORDPROMPTCURRENT Text
```

If there is no PASSWORDPROMPTCURRENT statement, Text defaults to

```
"Current NDS Password: "
```

Example:

```
PASSWORDPROMPTCURRENT "Enter Current Password: "
```

## 10.3.17 PASSWORDPROMPTCHANGE Statement

The PASSWORDPROMPTCHANGE statement specifies the prompt issued by the PAM module to request the user's new password for password changes.

Syntax:

```
PASSWORDPROMPTCHANGE Text
```

If there is no PASSWORDPROMPTCHANGE statement, Text defaults to

```
"New NDS Password: "
```

Example:

```
PASSWORDPROMPTCHANGE "New Password: "
```

## 10.3.18 PASSWORDPROMPTCHANGEAGAIN Statement

The PASSWORDPROMPTCHANGEAGAIN statement specifies the prompt issued by the PAM module to verify the user's new password for password changes.

Syntax:

```
PASSWORDPROMPTCHANGEAGAIN Text
```

If there is no PASSWORDPROMPTCHANGEAGAIN statement, Text defaults to

```
"Re-enter New NDS Password: "
```

Example:

```
PASSWORDPROMPTCHANGEAGAIN "Verify New Password: "
```

## 10.3.19 PLATFORMNAME Statement

The PLATFORMNAME statement specifies the common name of the Platform object. If there is no PLATFORMNAME statement, you are prompted to enter the name when obtaining a platform security certificate.

Syntax:

```
PLATFORMNAME Cn
```

Cn specifies the common name of the Platform configuration object that was specified in the Web interface when platform was defined.

Example:

```
PLATFORMNAME WestCentral
```

## 10.3.20 PASSWORDSOURCE Statement

The PASSWORDSOURCE statement allows you to specify where encrypted passwords should be stored. For example, on older UNIX systems, encrypted password information is stored in /etc/passwd. On most modern UNIX systems, this information is stored in /etc/shadow. On non-trusted HP-UX, the PASSWORDSOURCE statement should be used to specify whether the HP-UX system is using /etc/passwd or /etc/shadow for encrypted password information. By default, the installer package will determine which source to use; however, if you are running HP-UX in Trusted Computing Base (TCB) mode, where there is no /etc/shadow file, then you should omit the PASSWORDSOURCE statement and let Platform Services use standard HP API hooks to manage the encrypted password storage.

Syntax:

```
PASSWORDSOURCE fully-qualified-path-to-file
```

An important example of the PASSWORDSOURCE statement’s use is on HP-UX, when shadow passwords are enabled. The default location to look for encrypted passwords on non-trusted-mode HP-UX is /etc/passwd. When shadow passwords are enabled on HP-UX, PASSWORDSOURCE should be set as follows:

```
PASSWORDSOURCE /etc/shadow
```

## 10.3.21 POLLINT Statement

The POLLINT statement specifies the interval in number of seconds between polling cycles. It can be used to spread the amount of traffic and load placed on the Core Driver during event processing. The default for the polling interval is 300 seconds (5 minutes), which, in some circumstances, may be too frequent.

Syntax:

```
POLLINT seconds
```

Example:

```
POLLINT 600
```

In the above example, POLLINT will set the polling interval to 600 seconds (10 minutes).

## 10.3.22 POLLRAND Statement

The POLLRAND statement specifies the minimum and maximum polling interval in seconds from which to choose a random interval between polling cycles. It can be used to spread the amount of traffic and load placed on the Core Driver during event processing. The default for the polling interval is 300 seconds (5 minutes), which, in some circumstances, may be too frequent.

Syntax:

```
POLLRAND minsec maxsec
```

Example:

```
POLLRAND 300 1200
```

In the above example, POLLRAND will set the platform receiver (asamrcvr) to select a random integer between 300 and 1200 to represent the interval in number of seconds before the next polling cycle begins.

## 10.3.23 PROVISIONING Statement

The PROVISIONING statement specifies the network address and port of one Provisioning Manager Core Driver. A PROVISIONING statement must appear in the configuration file for the Platform Receiver and when obtaining a security certificate.

You can code more than one PROVISIONING statement. The first PROVISIONING statement in the file identifies the Provisioning Manager that is tried first. If a connection with the Provisioning Manager identified by the first PROVISIONING statement fails, the Provisioning Managers identified by any other PROVISIONING statements are tried, in the order the PROVISIONING statements appear in the configuration file, until a connection is successful or there are no more PROVISIONING statements.

Syntax:

```
PROVISIONING Address [PORT PortNumber]
```

Address specifies the DNS name or IP address of a Provisioning Manager.

PortNumber specifies the TCP port number that is to be used to communicate with the Provisioning Manager. PORT is optional. The default port number for the Provisioning Manager is 3451.

*IMPORTANT:*If you specify a port number other than the default, you must also use the Web interface to specify the same port number for the Core Driver configuration object.

Example:

```
PROVISIONING cdriver1.digitalairlines.com
PROVISIONING cdriver4.digitalairlines.com
```

## 10.3.24 RUNMODE Statement

The RUNMODE statement specifies the mode of operation the Platform Receiver uses. Command line parameters that specify a mode of operation override the mode specified on the RUNMODE statement.

Syntax:

```
RUNMODE Mode
```

Mode specifies the mode of operation for the Platform Receiver. Possible values follow.

*Table 10-1* Values For Specified Mode

| Value | Description |
| PERSISTENT | The Platform Receiver uses Persistent Mode. |
| POLLING | The Platform Receiver uses Polling Mode. |
| SCHEDULED | The Platform Receiver uses Scheduled Mode. |

If no RUNMODE statement or mode-related command line parameter is present, the Platform Receiver uses persistent Mode.

For more information about Platform Receiver modes of operation, see [Modes of Operation](babdcabj.html#babfijbb).

Example:

```
RUNMODE polling
```

## 10.3.25 SYSLOGFACILITY Statement

The SYSLOGFACILITY statement specifies the SYSLOG facility name to use for message logging on Linux/UNIX systems.

Syntax:

```
SYSLOGFACILITY   FacilityName
```

FacilityName specifies the SYSLOG facility to use for logging messages. The possible values for a specific Linux/UNIX system are mapped by the syslog.h file of that particular system.

If no SYSLOGFACILITY statement is coded, the default value is LOG\_DAEMON.

Example:

```
SYSLOGFACILITY LOG_DAEMON
```

## 10.3.26 TRACEFILE Statement

The TRACEFILE statement specifies that debugging output is generated and the file path where it is written. If the TRACEFILE statement is present in the platform configuration file, full debugging output is generated even if the -d command line parameter is not present.

To obtain debugging output from the system intercepts when you use the DIRECTTOAUTHENTICATION statement, you must use either the TRACEFILE or the TRACETOSTDOUT statement.

Syntax:

```
TRACEFILE FilePath
```

FilePath specifies the location in the file system where debugging output is written.

Example:

```
TRACEFILE c:\novell\asam\debug.txt
```

## 10.3.27 TRACETOSTDOUT Statement

The TRACETOSTDOUT statement specifies that debugging output is generated and that it is written to the standard output channel stdout. If the TRACETOSTDOUT statement is present in the platform configuration file, full debugging output is generated even if the -d command line parameter is not present.

To obtain debugging output from the system intercepts when you use the DIRECTTOAUTHENTICATION statement, you must use either the TRACEFILE or the TRACETOSTDOUT statement.

Syntax:

```
TRACETOSTDOUT
```

Example:

```
TRACETOSTDOUT
```

## 10.3.28 UPDATEPASSWORD Statement

The UPDATEPASSWORD statement specifies that the driver updates the local security system upon a successful check password or change password operation, or when password replication information is received from the Core Driver. This allows a user to log in using the last password that worked on the system if the driver, eDirectory, or the network is not available, and the local security system is appropriately configured.

If there is no UPDATEPASSWORD statement present in the platform configuration file, the driver does not store passwords in the local security system.

Syntax:

```
UPDATEPASSWORD
```

Example:

```
UPDATEPASSWORD
```

## 10.3.29 CRYPTTYPE Statement

The CRYPTTYPE statement specifies the format to use for storing passwords if the Fan-Out driver is configured to update local passwords. Therefore, the CRYPTTYPE statement works only if the platform configuration file (asamplat.conf) also contains the UPDATEPASSWORD statement.

When the Fan-Out driver is configured to update local Linux or UNIX passwords, the driver can automatically choose from the available password storage formats of the target operating system. The CRYPTTYPE statement allows you to override this choice with a specific format you prefer.

The Fan-Out driver supports many different operating systems which, in turn, support many different formats for locally stored passwords.

Syntax:

```
CRYPTTYPE format [rounds]
```

Possible values for format are DES, MD5, BLOWFISH, SHA256, SHA512 and SUN\_MD5.

Since its version 9 (12/02) release, Solaris has supported DES, MD5, BLOWFISH and SUN\_MD5. Linux support is based on the version of glibc. Most recent Linux distributions support DES, MD5, SHA256 and SHA512. Blowfish is not in the mainline of glibc, but has been added in some Linux distributions, including SUSE® Linux.

*NOTE:*Some formats supported by the Fan-Out driver may not be appropriate for your operating system. For example, inappropriate CRYPTTYPE formats in asamplat.conf cause the driver to failover to DES on Solaris and MD5 on Linux.

The value for rounds only applies to BLOWFISH, SHA256 or SHA512. This second argument can be used to indicate the number of rounds, or repetitions, of transformation to be used. For BLOWFISH, possible values for rounds are 04, 05, 06, 07, 08, 09, 10, 11 or 12. For SHA256 and SHA512 any number within the range of 1000-999999999 is a possible value for rounds. You may also omit the rounds parameter.

Example (MD5 format):

```
CRYPTTYPE MD5
```

Example (BLOWFISH format):

```
CRYPTTYPE BLOWFISH 09
```

Example (SHA512 format):

```
CRYPTTYPE SHA512 7000
```

### Default Format Scenarios

The Fan-Out driver is designed to use default format types when the following conditions exist:

* If an unacceptable rounds argument is specified for BLOWFISH on Linux, glibc uses MD5 instead.
* If an unacceptable rounds argument is specified for SHA256 or SHA512 on Linux, glibc substitutes 1000 for the unacceptable value.
* If an unacceptable rounds argument is specified for BLOWFISH on Solaris, Solaris substitutes 11 for the unacceptable value.
* If no CRYPTTYPE statement is used in asamplat.conf on Solaris or Linux, the driver will attempt to use the native operating system configuration files to decide upon an encryption mechanism:

  + On Solaris /etc/security/policy.conf is consulted.
  + On Linux /etc/login.defs and /etc/default/passwd are consulted. If both exist, configuration information in /etc/login.defs is given preference over configuration information in /etc/default/passwd.
* If no encryption configuration information can be found in the native configuration files, DES is used on Solaris and MD5 is used on Linux.

## 10.3.30 UPDATESAMBA Statement

The UPDATESAMBA statement specifies that the driver updates the Samba password file upon a successful check password or change password operation, or when password replication information is received from the Core Driver.

If there is no UPDATESAMBA statement present in the platform configuration file, the driver does not store passwords in the Samba password file.

Syntax:

```
UPDATESAMBA FilePath
```

FilePath specifies the location of the smbpasswd program in file system.

Example:

```
UPDATESAMBA /usr/local/samba/bin/smbpasswd
```

## 10.3.31 USEFILEIPC Statement

The USEFILEIPC statement specifies that data from the Platform Receiver should be made accessible by the Platform Receiver scripts by using file Input/Output rather than environment variables.

While environment variables are a convenient method for communicating data between the Platform Receiver and the scripts, they have size limitations, based on the operationg system parameter ARG\_MAX, that make it impossible to process events when they become too large. For example, a group that contains many users could exceed this size limit. The value of ARG\_MAX varies on different operating systems.

Syntax:

```
USEFILEIPC
```

Example:

```
USEFILEIPC
```

## 10.3.32 EXCLUDEUNMANAGED Statement

The EXCLUDEUNMANAGED statement specifies that the Platform Receiver should query the Fan-Out Driver Census (in the Identity Vault) if it cannot reconcile a user’s membership in a group account on a local system with a corresponding group account managed in Identity Manager.

Not all group accounts on a local system need to be replicated and tracked centrally from the Identity Vault. For example, Linux and UNIX often place users in certain default groups that are of no consequence to security and therefore not added to the Identity Vault.

The Fan-Out driver does not make this distinction between groups managed by Identity Manager and groups relevant only to the local system. If the Platform Receiver detects that a user is member to a local group that does not also exist in the Identity Vault, it reverses the membership in its charge to maintain parity with Identity Manager.

The EXCLUDEUNMANAGED statement bypasses this default behavior. When it is specified, the Platform Receiver will first query the Census to see if the group account in question also exists in the Identity Vault. If the group is not found in the Census, it is excluded automatically and the local unmanaged group membership can be preserved.

Syntax:

```
EXCLUDEUNMANAGED
```

Example:

```
EXCLUDEUNMANAGED
```
