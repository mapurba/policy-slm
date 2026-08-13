# 5.1 Driver Parameters and Global Configuration Values

You can control the operation of the driver by modifying the properties described in the following sections.

*IMPORTANT:*Changing these values requires a restart of the driver.

* [Driver Configuration Page](b3xub84.html#b4d9ehs)
* [Global Configuration Values Page](b3xub84.html#b4d9yhs)

Driver properties and Global Configuration Values are first created during the deployment of Designer Top Secret Driver packages. Driver properties and Global Configuration Values are first created during the deployment of Designer Top Secret Driver packages. For details, see [Creating the Driver in Designer](b1byr9qs.html).

To edit the properties shown on the Driver Configuration page and the Global Configuration Values page:

1. In iManager, select Identity Manager Overview from the Identity Manager task list on the left side of the window.
2. Navigate to your driver set by searching the tree or by entering its name.
3. Click the driver to open its overview.
4. Click the driver icon.
5. Select Driver Configuration or Global Config Values as appropriate.
6. Edit the property values as desired, then click OK.

## 5.1.1 Driver Configuration Page

*Table 5-1* Driver Configuration Page

| Property Name | Values or Format |
| Driver Module | Connect to Remote Loader must be selected |
| [Driver Object Password](b3xub84.html#b3xvqhp) | Text value |
| Authentication ID | Not used |
| Authentication Context | Not used |
| [Remote Loader Connection Parameters](b3xub84.html#b3xvoig) | Host name or IP address and port number of the driver shim on the connected system, and the RDN of the object with the server certificate |
| Driver Cache Limit | The recommended value is 0 (zero) |
| Application Password | Not used |
| [Remote Loader Password](b3xub84.html#b3xvr2u) | Text value |
| Startup Option | * Auto start * Manual |
| [Automatic Loopback Detection](b3xub84.html#b46686t) | * Yes * No |
| [Create Home Directories](b3xub84.html#b3xvkfe) | * Yes * No |
| [User Catalog Alias](b3xub84.html#b6abcjm) | Catalog data set name |
| [Group Catalog Alias](b3xub84.html#b6abckh) | Catalog data set name |
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

### Automatic Loopback Detection

Specifies whether the driver shim discards events that would cause loopback conditions. This function supplements the loopback detection provided by the Metadirectory engine.

### Create Home Directories

Specifies whether the driver automatically creates home directories in the hierarchical file system when users are created.

### User Catalog Alias

Specifies the data set name of the catalog used for new users created by the driver.

If you specify a value for User Catalog Alias, the REXX exec to add a new user issues the following command:

```
DEFINE ALIAS(NAME('user') RELATE('UserCatalogAlias'))
```

### Group Catalog Alias

Specifies the data set name of the catalog used for new groups created by the driver.

If you specify a value for Group Catalog Alias, the REXX exec to add a new group issues the following command:

```
DEFINE ALIAS(NAME('group') RELATE('GroupCatalogAlias'))
```

### Polling Interval

Specifies the number of seconds that the Publisher shim waits after running the polling exec and sending events from the change log to the Metadirectory engine. The default interval is 60 seconds.

### Publisher Disabled

Specifies whether the Publisher shim is active.

Select Yes if you are using Identity Vault to Application (one-way) data flow. This saves processing time.

### Heartbeat Interval

Specifies how often, in seconds, the driver shim contacts the Metadirectory engine to verify connectivity. Specify 0 to disable the heartbeat.

## 5.1.2 Global Configuration Values Page

*Table 5-3* Global Configuration Values

| Property Name | Values or Format |
| [Connected System or Driver Name](b3xub84.html#b455xz1) | Text value |
| [Create Users With](b3xub84.html#b3xvi0q) | Text value |
| [User Default Department](b3xub84.html#b3xvfia) | Text value |
| [User Default Group](b3xub84.html#b6abi74) | Text value |
| [User Default TSO Account Number](b3xub84.html#b6abi75) | Text value |
| [User Default TSO Proc](b3xub84.html#b6abi76) | Text value |
| [User Default TSO Unit](b3xub84.html#b6abi77) | Text value |
| [UID Assignment](b3xub84.html#b6abid9) | * Assign by Top Secret * Assign by Identity Vault |
| [UID Range](b3xub84.html#b6abkiq) | Numeric range |
| [GID Range](b3xub84.html#b6abjro) | Numeric range |
| [Default Home Directory](b3xub84.html#b6abn0h) | Text value |
| [Default Program](b3xub84.html#b6abofr) | Text value |
| [The Top Secret Connected System Accepts Passwords from the Identity Vault](b3xub84.html#b3xvua6) | * Yes * No |
| [The Identity Vault Accepts Passwords from the Top Secret Connected System](b3xub84.html#b3xvuna) | * Yes * No |
| [The Identity Vault Accepts Administrative Password Resets from the Top Secret Connected System](b3xub84.html#b3xvvsi) | * Yes * No |
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

### Create Users With

Specifies the ACID of a user to be used as a model for creating new users.

### User Default Department

Specifies the default department for new users.

### User Default Group

Specifies the default group for new users.

### User Default TSO Account Number

Specifies the default account number for new users.

### User Default TSO Proc

Specifies the default cataloged procedure name for new users. For example, IKJACCNT.

### User Default TSO Unit

Specifies the default unit name for new users. For example, SYSALLDA.

### UID Assignment

Specifies how UID and GID numbers are assigned to new users and groups. Select Assign by Top Secret or Assign by Identity Vault.

### UID Range

Specifies a range of numbers used when Top Secret assigns UID numbers for new users. The REXX exec to add a new user uses this value with the RANGE keyword on the TSS command. Use a pair of values separated by a comma, similar to the following:

```
10000,200000
```

### GID Range

Specifies a range of numbers used when Top Secret assigns GID numbers for new groups. The REXX exec to add a new group uses this value with the RANGE keyword on the TSS command. Use a pair of values separated by a comma, similar to the following:

```
10000,200000
```

### Default Home Directory

Specifies the default OMVS home directory path for new users. Include the ending slash (/) in the directory path. The user’s ACID is appended to the value that you specify. Use a value similar to the following:

```
/home/
```

In this example, the home directory that is assigned by the driver for a user whose ACID is IBMUSER is /home/IBMUSER.

### Default Program

Specifies the default OMVS program (login shell). Use a value similar to the following:

```
/bin/sh
```

### The Top Secret Connected System Accepts Passwords from the Identity Vault

Specifies whether the driver allows passwords to flow from the Identity Vault to the connected system.

### The Identity Vault Accepts Passwords from the Top Secret Connected System

Specifies whether the driver allows passwords to flow from the connected system to the Identity Vault.

### The Identity Vault Accepts Administrative Password Resets from the Top Secret Connected System

Specifies whether the driver allows passwords to be reset from the connected system in the Identity Vault. An administrative user can use the TSS REPLACE command to set another user’s password.

### Publish Passwords to NDS Password

Specifies whether the driver uses passwords from the connected system to set NDS® passwords in the Identity Vault. NDS passwords in the Identity Vault are not bidirectional and cannot be synchronized to another system.

### Publish Passwords to Distribution Password

Specifies whether the driver uses passwords from the connected system to set NMAS™ Distribution Passwords, which are used for Identity Manager password synchronization.

### Require Password Policy Validation before Publishing Passwords

Specifies whether the driver applies NMAS password policies to published passwords. If so, a password is not written to the Identity Vault if it does not conform.

### Reset User’s External System Password to the Identity Manager Password on Failure

Specifies whether, on a publish Distribution Password failure, the driver attempts to reset the password on the connected system using the Distribution Password from the Identity Vault.

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
