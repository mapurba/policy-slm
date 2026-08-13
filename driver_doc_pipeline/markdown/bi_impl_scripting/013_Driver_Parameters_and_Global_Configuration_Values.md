# 4.1 Driver Parameters and Global Configuration Values

You can control the operation of the Scripting driver by modifying the properties described in the following sections. Topics in this section include

* [Properties That Can Be Set Only During Driver Import](b8mp4y6.html#b8mp5ou)
* [Driver Configuration Page](b8mp4y6.html#b8mpjjq)
* [Global Configuration Values Page](b8mp4y6.html#b8mqhhb)

*IMPORTANT:*Changing these values requires a restart of the driver.

To edit the properties shown on the Driver Configuration page and the Global Configuration Values page:

1. In iManager, select Identity Manager Overview from the Identity Manager task list on the left side of the window.
2. Navigate to your driver set by searching the tree or by entering its name.
3. Click the driver to open its overview.
4. Click the driver icon.
5. Select Driver Configuration or Global Config Values as appropriate.
6. Edit the property values as desired, then click OK.

## 4.1.1 Properties That Can Be Set Only During Driver Import

Properties that you can set only during driver import are used to generate policies and other configuration details.

To change import-only properties, you must re-import the Scripting.xml driver configuration file over the existing driver.

*Table 4-1* Driver Import-Only Parameters

| Property Name | Values or Format |
| Data Flow | Bidirectional  Application to Identity Vault  Identity Vault to Application |
| Enable Entitlements | Yes  No |
| Use SSL | No |

### Data Flow

* *Bidirectional:*
  Identities are synchronized from both the Identity Vault and the connected system (application). After all pending events are processed, the Identity Vault and connected system mirror each other.
* *Application to Identity Vault:*
  Identities are synchronized from the connected system (application) to the Identity Vault, but not vice versa. For example, an identity created in the Identity Vault is not created on the connected system unless explicitly migrated.
* *Identity Vault to Application:*
  Identities are synchronized from the Identity Vault to the connected system (application), but not vice versa. For example, changes made to a connected system’s identity are not synchronized to the Identity Vault.

### Enable Entitlements

Specifies whether the driver uses either Approval Flow or Role-Based Entitlements with the Entitlements Service driver.

Enable entitlements for the driver only if you plan to use the User Application or Role-Based Entitlements with the driver.

You can use Role-Based Entitlements to integrate the Scripting driver with the Identity Manager User Application.

### Use SSL

Specifies whether the driver uses Secure Sockets Layer (SSL) to encrypt the connection between the Identity Vault and the application.

We strongly recommend that you use SSL. If you do not use SSL, identity data (including passwords) is sent across the network in clear text.

## 4.1.2 Driver Configuration Page

*Table 4-2* Driver Configuration Page

| Property Name | Values or Format |
| Driver Module | Connect to Remote Loader must be selected. |
| Driver Object Password | Text Value |
| Authentication ID | Not used by the Scripting driver. |
| Authentication Context | Not used by the Scripting driver. |
| Remote Loader Connection | Parameters Host name or IP address and port number of the driver shim on the connected system, and the RDN of the object with server certificate. |
| Driver Cache Limit | The recommended value is 0 (zero). |
| Application Password | Not used by the Scripting driver. |
| Remote Loader Password | Text Value |
| Startup Option | Auto start  Manual |
| Automatic Loopback Detection | Yes  No |
| Script Command | Text Value |
| Script Trace File | Filename |
| Subscriber Script | Filename |
| Polling Script | Filename |
| Heartbeat Script | Filename |
| Polling Interval | Number of seconds |
| Heartbeat Interval | Number of seconds |

### Driver Object Password

The Driver object password is used by the driver shim (embedded Remote Loader) to authenticate itself to the Metadirectory engine. This must be the same password that is specified as the Driver object password on the connected system driver shim.

### Remote Loader Connection Parameters

*Table 4-3* Remote Loader Connection Parameters

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

### Script Command

Specifies the command line the driver uses when executing scripts. The driver provides default values for Shell scripts, Perl, Python, VBScript and PowerShell. Normally this value does not need to be changed.

### Script Trace File

Specifies a file to which script trace output will be written. The path is relative to the Scripting driver installation directory.

### Subscriber Script

Specifies the script file that the driver runs for Subscriber events. The driver provides default values for Shell scripts, Python, Perl, VBScript and PowerShell, so this value does not normally need to be changed.

### Polling Script

Specifies the script file that the Publisher shim runs to poll for external events. The driver provides default values for Shell scripts, Perl, Python, VBScript and PowerShell, so this value does not normally need to be changed.

### Heartbeat Script

Specifies the script file that the Publisher shim runs to check the external account management system’s status. The driver provides default values for Shell scripts, Perl, Python, VBScript and PowerShell, so this value does not normally need to be changed.

### Polling Interval

Specifies the number of seconds that the Publisher shim waits after running the polling script and sending events from the change log to the Metadirectory engine. The default interval is 60 seconds, and the minimum interval is 1 second.

### Heartbeat Interval

Specifies how often, in seconds, the driver shim contacts the Metadirectory engine to verify connectivity. Specify 0 to disable the heartbeat.

## 4.1.3 Global Configuration Values Page

*Table 4-4* Global Configuration Values

| Property Name | Values or Format |
| Connected System or Driver Name | Text Value |
| Auto Associate Objects | Yes  No |
| Application Supports Query | Yes  No |
| Auto Resolve Association Reference | Yes  No |
| Auto Associate Subscriber Value | Text Value |
| Auto Associated Publisher Value | Text Value |
| Strip Old Values | Text Value |
| The Scripting Connected System Accepts Passwords from the Identity Vault | True  False |
| The Identity Vault Accepts Passwords from the Scripting Connected System | True  False |
| The Identity Vault Accepts Administrative Password Resets from the Scripting Connected System | True  False |
| Publish Passwords to NDS Password | True  False |
| Publish Passwords to Distribution Password | True  False |
| Require Password Policy Validation before Publishing Passwords | True  False |
| Reset User’s External System Password to the Identity Manager Password on Failure | True  False |
| Notify the User of Password Synchronization Failure via E-Mail | True  False |
| User Base Container | Identity Vault Container object |
| Group Base Container | Identity Vault Container object |

To view and edit Password Management GCVs, select Show for Show Password Management Policy.

To view and edit User and Group Placement GCVs, select Show for Show User and Group Placements.

### Connected System or Driver Name

Specifies the name of the driver. This value is used by the e-mail notification templates.

### Auto Associate Objects

Automatically assign associations to objects. Use this option to automatically generate associations on both the Subscriber and Publisher channels.

### Application Supports Query

Does your application support the ability to query information? If the driver cannot query data from your target application, objects cannot be matched and information cannot be merged. If you are only interested in event notification to your target scripts and not data synchronization, you can select No.

### Auto Resolve Association References

Automatically resolve association references from one object to another.

### Auto Associate Subscriber Value

When generating associations, select which value should be used for the object’s association. If you choose SourceName, the object's naming attribute will be used as the association. This value might be easier to read and use by a script. If you choose GUID, the object's Global Unique Identifier will be used. This value is guaranteed to be unique, even when it's renamed or moved.

### Auto Associate Publisher Value

When generating associations, select which value should be used for the object’s association. If you choose SourceName, the object’s naming attribute will be used as the association. This value might be easier to read and use by a script. If you choose GUID, the object's Global Unique Identifier will be used. This value is guaranteed to be unique, even when it is renamed or moved.

### Strip Old Values

By default, the engine will remove attribute values whose timestamps are older than that of their current state. Choose Strip to keep the default and strip these values when events are processed on the subscriber channel. Choose Keep to allow the attribute values to be processed by the subscriber channel. This is useful if your application requires that an action be taken on every event.

### The Scripting Connected System Accepts Passwords from the Identity Vault

Specifies whether the driver allows passwords to flow from the Identity Vault to the connected system.

### The Identity Vault Accepts Passwords from the Scripting Connected System

Specifies whether the driver allows passwords to flow from the connected system to the Identity Vault.

### The Identity Vault Accepts Administrative Password Resets from the Scripting Connected System

Specifies whether the driver allows passwords to be reset from the connected system in the Identity Vault.

### Publish Passwords to NDS Password

Specifies whether the driver uses passwords from the connected system to set nonreversible NDS® passwords in the Identity Vault.

### Publish Passwords to Distribution Password

Specifies whether the driver uses passwords from the connected system to set NMAS™ Distribution passwords, which are used for Identity Manager password synchronization.

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
