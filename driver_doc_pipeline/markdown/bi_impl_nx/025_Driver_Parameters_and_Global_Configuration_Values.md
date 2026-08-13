# 5.1 Driver Parameters and Global Configuration Values

You can control the operation of the Linux and UNIX driver by modifying the properties described in the following sections.

*IMPORTANT:*Changing these values requires a restart of the driver.

* [Driver Configuration Page](b3xub84.html#b4d9ehs)
* [Global Configuration Values Page](b3xub84.html#b4d9yhs)

To change import-only properties, you must re-import the driver configuration file LinuxUnix-IDM3\_5\_0-V2.xml over the existing driver. For details, see [Creating the Driver in Designer](b1bybgrg.html).

To edit the properties shown on the Driver Configuration page and the Global Configuration Values page:

1. In iManager, select Identity Manager Overview from the Identity Manager task list on the left side of the window.
2. Navigate to your Driver Set by searching the tree or by entering its name.
3. Click the driver to open its overview.
4. Click the driver icon.
5. Select Driver Configuration or Global Config Values as appropriate.
6. Edit the property values as desired, then click OK.

## 5.1.1 Driver Configuration Page

*Table 5-1* Driver Configuration Page

| Property Name | Values or Format |
| Driver Module | Connect to Remote Loader must be selected. |
| [Driver Object Password](b3xub84.html#b3xvqhp) | Text Value |
| Authentication ID | Not used by the Linux and UNIX driver. |
| Authentication Context | Not used by the Linux and UNIX driver. |
| [Remote Loader Connection Parameters](b3xub84.html#b3xvoig) | Host name or IP address and port number of the driver shim on the connected system, and the RDN of the object with server certificate |
| Driver Cache Limit | The recommended value is 0 (zero). |
| Application Password | Not used by the Linux and UNIX driver. |
| [Remote Loader Password](b3xub84.html#b3xvr2u) | Text Value |
| Startup Option | * Auto start * Manual |
| [Database Type](b3xub84.html#b3xvat3) | * Files * NIS * NIS+ |
| [Automatic Loopback Detection](b3xub84.html#b46686t) | * Yes * No |
| [Remove Home Directories](b3xub84.html#b3xvidk) | * Yes * No |
| [Create Home Directories](b3xub84.html#b3xvkfe) | * Yes * No |
| [Allow Duplicate UIDs](b3xub84.html#b3xvkff) | * Yes * No |
| [Allow Duplicate GIDs](b3xub84.html#b456017) | * Yes * No |
| [Polling Interval](b3xub84.html#b3xv8y7) | Number of seconds |
| [Heartbeat Interval](b3xub84.html#b46697t) | Number of seconds |
| [Publisher Disabled](b3xub84.html#b4668g7) | * Yes * No |

### Driver Object Password

The Driver object password is used by the driver shim (embedded Remote Loader) to authenticate itself to the Metadirectory engine. This must be the same password that is specified as the Driver object password on the connected system driver shim.

### Remote Loader Connection Parameters

The Remote Loader Connection Parameters option specifies information that the driver uses for Secure Sockets Layer (SSL) communication with the connected system.

*Table 5-2* Remote Loader Connection Parameters

| Parameter | Description |
| host=hostName | Connected system host name or IP address. |
| port=portNumber | Connected system TCP port number. The default is 8090. |
| kmo=objectRDN | The RDN of the object with the server certificate signed by the tree’s certificate authority. Enclose the RDN in double quotes (") if the name contains spaces. |

The following is an example Remote Loader connection parameter string:

```
hostname=192.168.17.41 port=8090 kmo="SSL CertificateDNS"
```

### Remote Loader Password

The Remote Loader password is used to control access to the driver shim (embedded Remote Loader). This must be the same password that is specified as the Remote Loader password on the connected system driver shim.

### Database Type

Database Type specifies the type of account management database that you use for your network-wide information storage.

* *Files:*
  Local file-based storage (/etc/passwd)
* *NIS:*
  Map-based storage
* *NIS+:*
  Hierarchical domain-based storage.

### Automatic Loopback Detection

Specifies whether the driver shim discards events that would cause loopback conditions. This function supplements the loopback detection provided by the Metadirectory engine.

### Remove Home Directories

Specifies whether the driver automatically removes home directories from the file system when users are deleted.

This option has no effect on AIX systems.

### Create Home Directories

Specifies whether the driver automatically creates home directories in the file system when users are created.

This option has no effect on AIX systems. On AIX, the add-user.sh script uses the native AIX mkuser command. By default, this command creates a home directory. This setting is governed by /usr/lib/security/mkuser.default and /etc/security/login.cfg.

### Allow Duplicate UIDs

Specifies whether the driver allows duplicate UIDs on the connected Linux or UNIX system.

AIX does not allow duplicate UIDs. Select No for AIX connected systems.

### Allow Duplicate GIDs

Specifies whether the driver allows duplicate GIDs on the connected Linux or UNIX system.

AIX does not allow duplicate GIDs. Select No for AIX connected systems.

### Polling Interval

Specifies the number of seconds that the Publisher shim waits after running the polling script and sending events from the change log to the Metadirectory engine. The default interval is 60 seconds.

### Publisher Disabled

Specifies whether the Publisher shim is active.

Select Yes if you are using Identity Vault to Application (one-way) data flow. This saves processing time.

### Heartbeat Interval

Specifies how often, in seconds, the driver shim contacts the Metadirectory engine to verify connectivity. Specify 0 to disable the heartbeat.

## 5.1.2 Global Configuration Values Page

*Table 5-3* Global Configuration Values

| Property Name | Values or Format |
| [Connected System or Driver Name](b3xub84.html#b455xz1) | Text Value |
| [Synchronize Group Membership](b3xub84.html#b3xvi0q) | * Yes * No |
| [Exclude Privileged Users and Groups](b3xub84.html#b3xvfia) | * Yes * No |
| [Require POSIX Attributes When Subscribing](b3xub84.html#b3xvgs1) | * Yes * No |
| [Use First Name + Last Name for gecos](b3xub84.html#b3xvkfg) | * Yes * No |
| [Lower Case CNs](b3xub84.html#b49oi3c) | * Yes * No |
| [The Linux or UNIX Connected System Accepts Passwords from the Identity Vault](b3xub84.html#b3xvua6) | * Yes * No |
| [The Identity Vault Accepts Passwords from the Linux or UNIX Connected System](b3xub84.html#b3xvuna) | * Yes * No |
| [The Identity Vault Accepts Administrative Password Resets from the Linux or UNIX Connected System](b3xub84.html#b3xvvsi) | * Yes * No |
| [Publish Passwords to NDS Password](b3xub84.html#b3xvvsj) | * Yes * No |
| [Publish Passwords to Distribution Password](b3xub84.html#b3xvvsk) | * Yes * No |
| [Require Password Policy Validation before Publishing Passwords](b3xub84.html#b3xvvsl) | * Yes * No |
| [Reset User’s External System Password to the Identity Manager Password on Failure](b3xub84.html#b3xvvsm) | * Yes * No |
| [Notify the User of Password Synchronization Failure via E-Mail](b3xub84.html#b3xvvsn) | * Yes * No |
| [User Base Container](b3xub84.html#b455w4s) | Identity Vault Container object |
| [Group Base Container](b3xub84.html#b3xvcn0) | Identity Vault Container object |

To view and edit Password Management GCVs, select Show for Show Password Management Policy.

To view and edit User and Group Placement GCVs, select Show for Show User and Group Placements.

### Connected System or Driver Name

Specifies the name of the driver. This value is used by the e-mail notification templates.

### Synchronize Group Membership

This option does not apply if the POSIX Management Mode is set to Manage Local. When it does apply, it has the following effect:

* It specifies whether the driver synchronizes the Group Membership attribute of a corresponding Group object in the Identity Vault (if one exists with that GID).
* The driver always synchronizes a user’s GID number (primary group identification) to the RFC 2307 gidNumber attribute of the corresponding User object in the Identity Vault.

### Exclude Privileged Users and Groups

Specifies whether the driver excludes events for users and groups with a uidNumber or gidNumber less than 100.

### Require POSIX Attributes When Subscribing

This option does not apply if the POSIX Management Mode is set to Manage Local. When it does apply, it specifies whether the driver requires users and groups from the Identity Vault to have RFC 2307 information, such as uidNumber, gidNumber, and homeDirectory, before it provisions them to the connected Linux or UNIX system.

### Use First Name + Last Name for gecos

Specifies whether the driver creates the user gecos field from the First Name and Last Name attributes of the User object in the Identity Vault for subscribed events.

### Lower Case CNs

Specifies whether the driver uses lowercase for the CN of User and Group objects it receives in events from the Metadirectory engine.

Linux and UNIX user and group names are usually lowercase.

### The Linux or UNIX Connected System Accepts Passwords from the Identity Vault

Specifies whether the driver allows passwords to flow from the Identity Vault to the connected Linux or UNIX system.

### The Identity Vault Accepts Passwords from the Linux or UNIX Connected System

Specifies whether the driver allows passwords to flow from the connected Linux or UNIX system to the Identity Vault.

### The Identity Vault Accepts Administrative Password Resets from the Linux or UNIX Connected System

Specifies whether the driver allows passwords to be reset from the connected Linux or UNIX system in the Identity Vault. The root user can use the passwd command to set another user’s password.

### Publish Passwords to NDS Password

Specifies whether the driver uses passwords from the connected Linux or UNIX system to set non-reversible NDS® passwords in the Identity Vault.

### Publish Passwords to Distribution Password

Specifies whether the driver uses passwords from the connected Linux or UNIX system to set NMAS™ Distribution Passwords, which are used for Identity Manager password synchronization.

### Require Password Policy Validation before Publishing Passwords

Specifies whether the driver applies NMAS password policies to published passwords. If so, a password is not written to the Identity Vault if it does not conform.

### Reset User’s External System Password to the Identity Manager Password on Failure

Specifies whether, on a publish Distribution Password failure, the driver attempts to reset the password on the connected Linux or UNIX system using the Distribution Password from the Identity Vault.

### Notify the User of Password Synchronization Failure via E-Mail

Specifies whether the driver sends an e-mail to a user if the password cannot be synchronized.

### User Base Container

Specifies the base container object in the Identity Vault for user synchronization. This container is used in the Subscriber channel Event Transformation policy to limit the Identity Vault objects being synchronized. This container is used in the Publisher channel Placement policy as the destination for adding objects to the Identity Vault. Use a value similar to the following:

```
users.myorg
```

### Group Base Container

Specifies the base container object in the Identity Vault for group synchronization. This container is used in the Subscriber channel Event Transformation policy to limit the Identity Vault objects being synchronized. This container is used in the Publisher channel Placement policy as the destination when adding objects to the Identity Vault. Use a value similar to the following:

```
groups.myorg
```
