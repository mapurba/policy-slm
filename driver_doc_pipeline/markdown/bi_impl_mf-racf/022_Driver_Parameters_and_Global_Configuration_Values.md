# 5.1 Driver Parameters and Global Configuration Values

You can control the operation of the driver by modifying the properties described in the following sections.

*IMPORTANT:*Changing these values requires a restart of the driver.

* [Setting Properties during Driver Import](b3xub84.html#b4d9cao)
* [Driver Configuration Page](b3xub84.html#b4d9ehs)
* [Global Configuration Values Page](b3xub84.html#b4d9yhs)

To change import-only properties, you must re import the driver configuration file RACF-IDM3\_6\_0-V5.xml over the existing driver, or add the required additional Designer packages. For details, see [Creating the Driver in Designer](b1bybgrg.html).

To edit the properties shown on the Driver Configuration page and the Global Configuration Values page:

1. In iManager, select Identity Manager Overview from the Identity Manager task list on the left side of the window.
2. Navigate to your driver set by searching the tree or by entering its name.
3. Click the driver to open its overview.
4. Click the driver icon.
5. Select Driver Configuration or Global Config Values as appropriate.
6. Edit the property values as desired, then click OK.

## 5.1.1 Setting Properties during Driver Import

Properties that you can set only during driver import are used to generate policies and other configuration details.

*Table 5-1* Driver Import-Only Parameters

| Property Name | Values or Format |
| [Data Flow](b3xub84.html#b3xusu3) | * Bidirectional * Application to Identity Vault * Identity Vault to Application |
| [Set Preconfigured TSO Data](b3xub84.html#b6bav43) | * Yes * No |
| [Set Preconfigured OMVS Data](b3xub84.html#b6barw8) | * Yes * No |
| [Enable Entitlements](b3xub84.html#b3xvdmx) | * Yes * No |
| [Use SSL](b3xub84.html#b3xvlwp) | * Yes * No |

### Data Flow

* *Bidirectional:*
  Identities are synchronized from both the Identity Vault and the connected system (application). After all pending events are processed, the Identity Vault and connected system mirror each other.
* *Application to Identity Vault:*
  Identities are synchronized from the connected system (application) to the Identity Vault, but not vice versa. For example, an identity created in the Identity Vault is not created on the connected system unless explicitly migrated.
* *Identity Vault to Application:*
  Identities are synchronized from the Identity Vault to the connected system (application), but not vice versa. For example, changes made to a RACF identity are not synchronized to the Identity Vault.

### Set Preconfigured TSO Data

* *Yes:*
  Enables prompts for the default TSO account number and default TSO procedure.
* *No:*
  Disables prompts for the default TSO account number and default TSO procedure.

### Set Preconfigured OMVS Data

* *Yes:*
  Enables prompts for the UID and GID number assignment source (RACF or Identity Vault), the default home directory path and the default program.
* *No:*
  Disables prompts for the UID and GID number assignment source (RACF or Identity Vault), the default home directory path and the default program.

### Enable Entitlements

Specifies whether the driver uses either Approval Flow or Roles-Based Entitlements with the Entitlements Service driver.

Enable entitlements for the driver only if you plan to use the User Application or Roles-Based Entitlements with the driver.

You can use Role-Based Entitlements to integrate the driver with the Identity Manager User Application. For more information about Roles-Based Entitlements, see the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

### Use SSL

Specifies whether the driver uses Secure Sockets Layer (SSL) to encrypt the connection between the Identity Vault and the application.

NetIQ strongly recommends that you use SSL. If you do not use SSL, your identity data, including passwords, is sent across the network in clear text.

## 5.1.2 Driver Configuration Page

*Table 5-2* Driver Configuration Page

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
| [Polling Interval](b3xub84.html#b3xv8y7) | Number of seconds |
| [Heartbeat Interval](b3xub84.html#b46697t) | Number of seconds |
| [Publisher Disabled](b3xub84.html#b4668g7) | * Yes * No |

### Driver Object Password

The Driver object password is used by the driver shim (embedded Remote Loader) to authenticate itself to the Metadirectory engine. This must be the same password that is specified as the Driver object password on the connected system driver shim.

### Remote Loader Connection Parameters

The Remote Loader Connection Parameters option specifies information that the driver uses for Secure Sockets Layer (SSL) communication with the connected system.

*Table 5-3* Remote Loader Connection Parameters

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

Specifies whether the driver shim discards events that would cause loopback conditions. This function supplements the loopback detection provided by the Metadirectory engine. The RACF driver provides its own loopback detection, so this option should always be set to No.

### Polling Interval

Specifies the number of seconds that the Publisher shim waits after running the polling exec and sending events from the change log to the Metadirectory engine. The default interval is 60 seconds.

### Publisher Disabled

Specifies whether the Publisher shim is active.

Select Yes if you are using Identity Vault to Application (one-way) data flow. This saves processing time.

### Heartbeat Interval

Specifies how often, in seconds, the driver shim contacts the Metadirectory engine to verify connectivity. Specify 0 to disable the heartbeat.

## 5.1.3 Global Configuration Values Page

*Table 5-4* Global Configuration Values

| Property Name | Values or Format |
| [Connected System or Driver Name](b3xub84.html#b455xz1) | Text value |
| [User Default Group](b3xub84.html#b6abi74) | Text value |
| [User Default Owner](b3xub84.html#b3xvfia) | Text value |
| [Default CONNECT Attributes](b3xub84.html#bqk4e6w) | Text value |
| [User Default TSO Account Number](b3xub84.html#b6abi75) | Text value |
| [User Default TSO Proc](b3xub84.html#b6abi76) | Text value |
| [UID Assignment](b3xub84.html#b6abid9) | * Assign by RACF * Assign by Identity Vault |
| [Default Home Directory](b3xub84.html#b6abn0h) | Text value |
| [Default Program](b3xub84.html#b6abofr) | Text value |
| [The RACF Connected System Accepts Passwords from the Identity Vault](b3xub84.html#b3xvua6) | * Yes * No |
| [The Identity Vault Accepts Passwords from the RACF Connected System](b3xub84.html#b3xvuna) | * Yes * No |
| [Publish Passwords to NDS Password](b3xub84.html#b3xvvsj) | * Yes * No |
| [Publish Passwords to Distribution Password](b3xub84.html#b3xvvsk) | * Yes * No |
| [Require Password Policy Validation before Publishing Passwords](b3xub84.html#b3xvvsl) | * Yes * No |
| [Reset User’s External System Password to the Identity Manager Password on Failure](b3xub84.html#b3xvvsm) | * Yes * No |
| [Synchronize RACF Pass Phrases to Identity Vault Passwords on the Publisher Channel](b3xub84.html#b3xvvsn) | * Yes * No |
| [Synchronize RACF Pass Phrases to Identity Vault Passwords on the Publisher Channel](b3xub84.html#b3xvvsn) | * Yes * No |
| [Synchronize Identity Vault Passwords to RACF Pass Phrases on the Subscriber Channel](b3xub84.html#bmineni) | * Yes * No |
| [Synchronize RACF Passwords to Identity Vault Passwords on the Publisher Channel](b3xub84.html#bminenj) | * Yes * No |
| [User Base Container](b3xub84.html#b455w4s) | Identity Vault Container object |
| [Group Base Container](b3xub84.html#b3xvcn0) | Identity Vault Container object |

To view and edit Password Management GCVs, select Show for Show Password Management Policy.

To view and edit User and Group Placement GCVs, select Show for Show User and Group Placements.

### Connected System or Driver Name

Specifies the name of the driver. This value is used by the e-mail notification templates.

### User Default Group

Specifies the default group for new users.

### User Default Owner

Specifies the default owner for new users.

### Default CONNECT Attributes

When a Group Membership (CONNECT) is added in RACF, additional operands can be specified as properties of the CONNECT. This field allows you to edit the default values. The default values are

```
  authority(use) uacc(read)
```

### User Default TSO Account Number

Specifies the default account number for new users.

### User Default TSO Proc

Specifies the default cataloged procedure name for new users. For example, IKJACCNT.

### UID Assignment

Specifies how UID and GID numbers are assigned to new users and groups. Select Assign by RACF or Assign by Identity Vault.

### Default Home Directory

Specifies the default OMVS home directory path for new users. Include the ending slash (/) in the directory path. The user’s user ID is appended to the value that you specify. Use a value similar to the following:

```
  /home/
```

In this example, the home directory that is assigned by the driver for a user whose user ID is IBMUSER is /home/IBMUSER.

### Default Program

Specifies the default OMVS program (login shell). Use a value similar to the following:

```
  /bin/sh
```

### The RACF Connected System Accepts Passwords from the Identity Vault

Specifies whether the driver allows passwords to flow from the Identity Vault to the connected system.

### The Identity Vault Accepts Passwords from the RACF Connected System

Specifies whether the driver allows passwords to flow from the connected system to the Identity Vault.

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

### Synchronize RACF Pass Phrases to Identity Vault Passwords on the Publisher Channel

Specifies whether the driver should publish and synchronize changes to the RACF pass phrase to the Identity Vault password.

### Synchronize Identity Vault Passwords to RACF Pass Phrases on the Subscriber Channel

Specifies whether password changes in the Identity Vault should be synchronized with the RACF pass phrase.

### Synchronize RACF Passwords to Identity Vault Passwords on the Publisher Channel

Specifies whether password changes in RACF should be synchronized with the Identity Vault password.

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
