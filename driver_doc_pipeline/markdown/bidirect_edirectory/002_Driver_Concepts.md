# 1.1 Driver Concepts

* [Key Terms](driver-concepts.html#b2ihag3)
* [Data Flow](driver-concepts.html#bwctkbg)
* [How the Bidirectional eDirectory Driver Works](driver-concepts.html#abaaeg6)

## 1.1.1 Key Terms

*Identity Manager:*
NetIQ Identity Manager is a service that synchronizes data among servers in a set of connected systems by using a robust set of configurable policies. Identity Manager uses the Identity Vault to store shared information, and uses the Identity Manager engine for policy-based management of the information as it changes in the vault or connected system. Identity Manager runs on the server where the Identity Vault and the Identity Manager engine are located.

*Connected System:*
Any system that can share data with Identity Manager through a driver.

*Identity Vault:*
A hub, with applications and directories publishing their changes to it. The Identity Vault then sends changes to the applications and directories that have subscribed for them. This results in two main flows of data: the Publisher channel and the Subscriber channel.

*Identity Manager Engine:*
The core server that implements the event management and policies of Identity Manager. The engine runs on the Java Virtual Machine in eDirectory.

*Driver:*
A set of policies, filters, and objects that act as the connector between an Identity Vault and the driver shim.

This software enables an application to publish events from an application to the directory, enables an application to subscribe to events from the directory, and synchronizes data between the directory and applications.

*Driver Object:*
A collection of channels, policies, rules, and filters that connect an application to an Identity Vault that is running Identity Manager.

Each driver performs different tasks. Policies, rules, and filters tell the driver how to manipulate the data to perform those tasks.

The Driver object displays information about the driverĂ˘Â€Â™s configuration, policies, and filters. This object enables you to manage the driver and provide eDirectory management of the driver shim parameters.

*Driver Shim:*
The driver shim handles communication between eDirectory and Identity Manager engine. A driver shim can be implemented either in Java class or as a native Windows DLL file.

The driver shim filename for the Bidirectional eDirectory driver is EdirDriverShim.jar.

*Remote Loader:*
Enables a driver shim to execute outside of the Identity Manager engine (perhaps remotely on a different machine). The Remote Loader is typically used when the Identity Manager server does not meet the requirements of the driver shim.

The Remote Loader executes the driver shim and passes information between the shim and the Identity Manager engine. When you use a Remote Loader, you install the driver shim on the server where the Remote Loader is running, not on the server where the Identity Manager engine is running. You can choose to use SSL to encrypt the connection between the Identity Manager engine and the Remote Loader. For more information, see [Understanding Identity Manager Communication](../../../identity-manager-48/security/data/ports-used-by-identity-manager-components.html#ports-used-by-identity-manager-components) in the [NetIQ Identity Manager Security Guide](../../../identity-manager-48/security/data/identity-manager-security-guide.html#identity-manager-security-guide).

*NOTE:*The Bidirectional eDirectory driver does not support the Remote Loader.

*TAO:*
A TAO (Timing Analysis Output) file is an ASCII text file with the .TAO extension. The file contains the results of a timing analysis. In the current context, the TAO file refers to the event cache file used by Identity Manager.

*LDAP:*
The Lightweight Directory Access Protocol. An Internet protocol for accessing distributed directory services that act in accordance with X.500 data and service models.

*SSL:*
Secure Sockets Layer. A protocol for managing the security of the messages transmitted on the Internet. SSL uses a program layer located between the Internet's Hypertext Transfer Protocol (HTTP) and Transport Control Protocol (TCP) layers. SSL uses the public-and-private key encryption system from RSA, which also includes the use of a digital certificate.

*TLS:*
Transport Layer Security. A protocol that ensures privacy between communicating applications and their users on the Internet. When a server and client communicate, TLS ensures that there is no tampering with any message. TLS is the successor of the Secure Sockets Layer (SSL).

*Keystore:*
A keystore contains private keys and certificates with their corresponding public keys required by a server for client authentication.

## 1.1.2 Data Flow

The Identity Manager Bidirectional eDirectory driver synchronizes data between the Identity Vault and eDirectory. The driver can run anywhere that an Identity Manager server is running. The driver uses the Lightweight Directory Access Protocol to bidirectionally synchronize changes between an Identity Vault and the connected system (eDirectory).

The driver uses the change-log publication method to recognize data changes and communicates them to an Identity Vault. The Subscriber channel sends the Identity Vault changes to the connected system (eDirectory) through LDAP/LDAPS.

## 1.1.3 How the Bidirectional eDirectory Driver Works

The Bidirectional eDirectory driver requires a change-log module to be present in the eDirectory server. The change-log module cannot coexist with the Identity Manager engine.

The change-log module provides change notification for the driver's Publisher channel. The data flow between the Bidirectional eDirectory driver and the Identity Vault is controlled by filters and policies that are in place for the Bidirectional eDirectory driver.

If you need to connect to an Identity Manager server, you must use the traditional eDirectory driver.

*Figure 1-1* Bidirectional eDirectory Driver Functionality

![](../graphics/design_implementation_a.png)

* *Driver:*
  The bidirectional driver has Subscriber and Publisher channels:

  + *Subscriber Channel:*
    The Subscriber channel watches for additions and modifications to Identity Vault objects and issues LDAP commands that make changes to the connected system (eDirectory).
  + *Publisher Channel:*
    The Publisher channel reads information from the change-log and submits that information to an Identity Vault via Identity Manager engine. By default, the Publisher channel checks the log every 10 seconds. The Identity Manager engine applies policies, takes the appropriate actions, and posts the events to the Identity Vault.
  + *Filters:*
    Identity Manager uses filters to control which objects and attributes are shared. The default filter configuration for the Bidirectional eDirectory driver allows objects and attributes to be shared.
  + *Policies:*
    Policies are used to control data synchronization between the driver and the Identity Vault.
* *Change-log Module:*
  The change-log module has the following components:

  + *Change Cache:*
    The event logger logs eDirectory events into a change cache, which is a TAO file that has the same structure as the Identity Manager engine. A unique change cache is associated with a registered driver instance. Every successful new driver registration creates a new change cache that is associated with that driver. The TAO files have a proprietary format and are designed to reduce the disk usage for storing the change information. The change cache files are local to the eDirectory server on which they are created, because they refer to several server-specific details in the logged events.
  + *Event Logger:*
    The event logger is an Identity Manager dxevent module with a limited functionality. It registers event handlers for the eDirectory events. The event handler uses the filter information that is passed to the change-log when an eDirectory driver is registered. The filters determine events that the driver can consume from the change-log. The event handler filters events based on the driver filter. All filtered events are logged by the event logger.
  + *Change-log Extension Handler:*
    The change-log module provides LDAP extensions for changes to the eDirectory driver. The LDAP extension handler exposes the extension for registering an eDirectory driver instance and for initiating and stopping a change publication to the eDirectory driver. The driver registration information is stored in the driver data configuration file, which resides in the DIB directory of eDirectory. The event logger module provides changes to the change-log. The changes are stored in the TAO file format of the Identity Manager engine.

    The LDAP extension handler is a limited version of the dxldap module, whose only job is to expose extensions for the change-log. Other Identity Manager extensions are not present in the change-log module.

    There are four change-log operations: InitRequest, GetChangesRequest, SendChangesResponse, and EndRequest. The clientID is the GUID of the eDirectory driver in the Identity Vault. The GUID is used to uniquely identify the registered eDirectory driver instances.
