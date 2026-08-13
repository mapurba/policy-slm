# 4.2 Configuration and Performance Guidelines

Many factors affect the performance of the Identity Manager Fan-Out Driver. Performance is most critical for Authentication Services, such as Check Password and Get Context.

There are many relationships within the driver, and one or more of the factors described in the following sections can affect all of these relationships. Use the following as guidelines in planning and troubleshooting your Fan-Out Driver installation.

Acceptable Authentication Services performance is achievable using two or three low-end servers for Core Drivers. However, if your present network experiences problems, such as slow logins related to eDirectory, Fan-Out Driver operations will experience similar response problems.

For fault tolerance, your configuration should include Core Drivers running on several servers.

For fault tolerance, each Core Driver should use a different LDAP host server.

For optimal performance, each Core Driver and its LDAP host server should run on the same server.

Topics in this section include

* [eDirectory](babdhgie.html#br3ne7c)
* [Object Services and the Event Subsystem](babdhgie.html#br3ne7d)
* [Event Journal Services](babdhgie.html#chdgbgca)
* [Authentication Services](babdhgie.html#br3ne7e)
* [Platform Systems](babdhgie.html#br3ne7f)
* [Platform Services / Authentication Services Relationship](babdhgie.html#br3ne7g)

## 4.2.1 eDirectory

Tuning eDirectory on your network is beyond the scope of this document. Much documentation on this subject is available elsewhere, including NetIQ Technical Information Documents (TIDs), which are available at the [NetIQ Support Web site](http://support.netiq.com). The health and performance of eDirectory is critical to the ability of the driver to respond to Authentication Services requests and to deliver provisioning events in a timely manner. Therefore, the health and performance of eDirectory should be your starting point in doing any performance planning and troubleshooting with the driver.

Factors in driver performance relative to eDirectory include

* The size of the eDirectory tree
* Communication links between the LDAP host servers used by Core Drivers and servers holding replicas of the ASAM System container and other objects referenced by the driver
* LAN traffic
* Size of partitions containing relevant objects
* Performance of CPU and disks in servers holding relevant replicas
* Amount of memory in servers holding relevant replicas

The driver interfaces with eDirectory through LDAP. For LDAP tuning guidance, see the NetIQ eDirectory Administration Guide.

## 4.2.2 Object Services and the Event Subsystem

The Object Services component of the Core Driver is primarily responsible for maintaining the Census and other objects in the ASAM System container. Object Services receives provisioning events from the Event Subsystem, updates the Census as required, and passes the provisioning events to Event Journal Services. It is important for Identity Provisioning that the Core Driver be running at all times, but it is mostly a background process that does not require a great deal of processing power and is, for the most part, not a time-critical process.

Object Services performs Trawls to initially build and to verify the Census by performing a series of requests based on the Census Search objects defined in your configuration. For each Organizational Unit represented in the configuration, Object Services issues a single request to eDirectory to return all the objects contained in the given Organizational Unit.

Focus your Search objects to the specific directory locations of your users and groups rather than specifying a top level container object. This provides better feedback information during a Trawl and reduces the likelihood of an LDAP time-out because of slow servers or slow network links.

The Event Subsystem uses Identity Manager to provide events to Object Services. The Event Subsystem requires minimal processing power, but it does require replicas for all objects that are monitored. Network connectivity and eDirectory synchronization are the primary performance factors for the Event Subsystem.

For optimal performance, a writable partition of all replicas containing objects contained in the Census should reside on the same server as the LDAP host server used by a Core Driver. However, be aware that operations that lock the directory on the local server, such as running NDSRepair, sometimes delay requests or cause them to fail.

## 4.2.3 Event Journal Services

Event Journal Services waits for Platform Receivers to connect, then provides pending events and a snapshot of User and Group objects for processing. Network connectivity to the platforms, and proximity of the Core Driver to servers holding replicas of managed User and Group objects are the primary performance factors for Event Journal Services.

Platforms with very large numbers of managed users and groups should be connected to Event Journal Services with connections of adequate bandwidth to ensure that Full Sync Mode and Check Mode processing will complete within an acceptable time.

To reduce the number of concurrent connections that must be serviced by a Core Driver host, avoid using Persistent Mode on Platform Receivers.

## 4.2.4 Authentication Services

Authentication Services is responsible for processing requests made by Platform Services.

For optimal performance, LDAP host servers used by Core Drivers should hold a writable replica that contains the User objects represented in the Census, and other objects that might be referenced often by Authentication Services.

## 4.2.5 Platform Systems

Platform Services sends requests to the Core Driver. The systems on which Platform Services reside can be anything from a desktop workstation to a high-end mainframe system. The inherent performance of these systems is based on a number of factors, including

* System load
* The power of the system
* Network traffic
* Connectivity and bandwidth to the Core Drivers
* The number of Core Drivers defined in the configuration

Consider each of these as you configure each platform and as you select the location of the Core Drivers.

## 4.2.6 Platform Services / Authentication Services Relationship

The performance of the Platform Services / Authentication Services transaction is the most important performance relationship in the driver. The communication relies on the TCP/IP stack of the platform and Authentication Services server. TCP/IP configuration on the platform, the Authentication Services server, and the routers in between is the most important factor in the performance of servicing Authentication Services requests. Guidelines for configuring TCP/IP are beyond the scope of this section. Refer to appropriate NetIQ and platform operating system documentation and TIDs for further information.

Platform system planners should be aware of a mandatory three-second delay in reporting a bad password on a password check request. This delay is in eDirectory itself. It cannot be configured by the driver.
