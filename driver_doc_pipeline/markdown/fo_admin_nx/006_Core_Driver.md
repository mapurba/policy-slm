# 2.1 Core Driver

The Core Driver can be further broken down into two main parts:

* The Driver Shim
* The objects that represent Core Driver properties and functionality in the Identity Vault (eDirectory)

The Shim is the installed driver software that provides authentication services, such as password verification, to target platforms. It provides identity provisioning events, such as add, modify, and delete, for users and groups, to target platforms. It also uses its Event Subsystem to retrieve events from Identity Manager. Finally, the Core Driver includes an embedded remote loader that replaces the functionality of the standard remote loader used by Identity Manager.

The objects used in the Identity Vault to store Core Driver properties and functionality include:

* The driver object, which stores configuration information about the Core Driver.
* The ASAM System container object, which stores configuration and user management information for users connecting to other systems via the Fan-Out Driver.

A writable replica of the partition holding the ASAM System container must reside on the LDAP host server used by a Core Driver. A User object, configured during installation, is used by the driver to perform an LDAP Bind for access to eDirectory.

*Figure 2-2* Core Driver

![](../graphics/coredriver.png)

In summary, the Core Driver provides these functions:

* eDirectory access to platforms for Authentication Services, such as password verification.
* Provisioning events to Platform Services for the maintenance of local user accounts and groups.
* The Web interface that you use to configure and manage the driver
* Management of the objects inside the ASAM System container
* An audit trail of significant occurrences

You can run multiple Core Drivers to provide redundancy for Authentication Services and Identity Provisioning functions.

One Core Driver is designated as the primary Core Driver. Other Core Drivers are secondary Core Drivers. Only the primary Core Driver listens for events from eDirectory. The primary Core Driver also serves the Web interface and provides environmental information during the installation process for other Core Drivers.

## 2.1.1 Core Driver Component Details

The software architecture of the Core Driver includes eight main components. Five of the components are collectively referred to as the Provisioning Manager:

### Provisioning Manager Components

Descriptions of each component in Provisioning Manager follows.

#### Object Services

Object Services maintains the objects within the ASAM System container. Some of these objects store configuration information for the various driver components. Others represent users and groups of users that can be defined on target platforms. The object that contains these users and groups is called the Census.

Object Services on the primary Core Driver is notified by the Event Subsystem of events, such as add, modify, or delete, pertaining to users and groups of users in eDirectory. These events are used to maintain the Census.

To initially build and periodically ensure the integrity of the Census, Object Services examines specified portions of eDirectory for users and groups. This process is called a Trawl. You can use the Web interface to set the Trawl schedule. Only the primary Core Driver performs Trawls.

Census Search objects that you define using the Web interface describe which objects in eDirectory are included in the Census. Platform Set search objects that you define using the Web interface describe which users and groups are managed for a given set of platforms.

For more information about Object Services and the Census, see [Census Container](br12c66.html#babjjgaa). For more information about associating users and groups with sets of platforms, see [Platform Set Objects](br12c66.html#babffida).

#### Event Journal Services

Event Journal Services receives provisioning events from Object Services and makes them available to sets of platforms according to the rules you specify. Event Journal Services ensures that provisioning events for a platform are delivered, even if the platform is not always available.

Platforms can periodically connect to Event Journal Services to receive provisioning events, or they can maintain a persistent connection and receive events as they occur.

By defining multiple Core Drivers to provide events to platforms, you can provide for improved availability.

#### Audit Services

Audit Services maintains the Audit Log and Operational Logs for a Core Driver.

#### Certificate Services

Certificate Services mints the certificates used by Secure Sockets Layer (SSL) to authenticate and secure connections between the components.

#### Web Services

Web Services provides the secure Web interface for monitoring and administering the Identity Manager Fan-Out Driver. The Web interface is provided through an iManager plug-in.

### Authentication Services

Authentication Services provides Platform Services with the time-critical interface to eDirectory. This interface is used for such functions as checking the passwords of users logging in to the platform. This interface is also used by the AS Client API.

By defining multiple Core Drivers to provide Authentication Services to platforms, you can provide for improved performance and availability.

Authentication Services supports platform communications using SSL and DES encryption.

### Event Subsystem

The Event Subsystem uses Identity Manager to subscribe to eDirectory events and provides them to Object Services. Objects of interest must be replicated on the Core Driver server.

### Embedded Remote Loader

Identity Manager includes a software component known as the Remote Loader. It is used to interface with drivers on the various systems that can be connected to Identity Manager.

The Core Driver bypasses this component, using its own Embedded Remote Loader. The resulting tighter integration provides eDirectory, Identity Manager, and the Fan-Out Core Driver with greater individual resources and fault tolerance while maintaining a simple configuration
