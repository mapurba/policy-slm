# Glossary

Account Redirection

The process of ensuring that users and groups are the same across all platforms by redirecting account information requests to a User or Group object in eDirectory™.

AS Client API

The Authentication Services application programming interface (API). The AS Client API can be used by applications to perform functions, such as user ID/password verification, password changes, and obtaining information from eDirectory.

ASAM Directory

The file system directory that contains the binaries, configuration information, and other related files used by Identity Manager Fan-Out Driver components.

ASAM Master User Object

The User object that Core Driver components use for LDAP Bind operations.

ASAM System Container Object

The container object in eDirectory that holds component configuration and user and group management objects.

Audit Log

The log of occurrences of interest for auditing purposes. The Audit Log is maintained by the Audit Services component of each Core Driver.

Audit Services

The Core Driver component that performs logging.

Authentication Services

The set of services that provides access to information from eDirectory for authentication purposes. The principal components of Authentication Services are the Core Driver Authentication Services component, the Platform Services Process, the AS Client API, and the System Intercept.

Census

The collection of Enterprise User and Enterprise Group objects that represent users and groups from eDirectory that can be associated with a Platform Set. Object Services maintains the Census using provisioning events. Object Services on the primary Core Driver initially builds and periodically verifies the Census through the use of Trawls.

Census Search Object

An eDirectory object used to specify users and groups to be included in the Census.

Certificate

A digital object used to authenticate and secure SSL communications.

Certificate Services

The Core Driver component that issues certificates for other components.

Context

The location of an object within the eDirectory tree.

Core Driver

The components that provide Identity Provisioning and Authentication Services to platforms, and provide for the management of the Identity Manager Fan-Out Driver.

DES

Data Encryption Standard, approved by the U.S. government.

Enterprise Group (eGroup)

An object that represents a group of users that can be defined on a platform. Enterprise Group objects reside in the Census container.

Enterprise User (eUser)

An object that represents a user that can be defined on a platform. It is used by Authentication Services to locate the corresponding User object in eDirectory. Enterprise User objects reside in the Census container.

Entropy Daemon

A process that collects and provides cryptographically strong random data.

Event Driven Objects

A container in the ASAM System container that holds objects affected by provisioning events.

Event Journal Services

The Core Driver component that manages event information and provides provisioning events to Platform Receivers.

Event Subsystem

The Core Driver component that receives provisioning events from eDirectory and provides them to Object Services.

Identity Provisioning

The automatic provisioning of account related information from eDirectory to a target platform. The principal components of Identity Provisioning are the Event Subsystem, Object Services, Event Journal Services, Platform Receivers, and Receiver scripts.

Name Service Switch

A library for Linux and UNIX operating systems that implements a set of system functions used by programs to retrieve user and group account information. The Fan-Out Driver provides a Name Service Switch that allows a Linux or UNIX system to redirect account information from eDirectory.

Naming Exception

A conflict detected by Object Services between multiple User or Group objects having the same common name.

Object Services

The Core Driver component that maintains the Census.

Operational Log

A log of occurrences pertaining to the processing of a component. Audit Services maintains the Operational Log for the Core Driver.

PAM

Pluggable Authentication Module. PAM is a standard framework for UNIX defined by OSF RFC 86.0 that provides for authentication of users by facilities external to the original UNIX operating system.

Password Redirection

The process of ensuring that users' passwords are the same across all platforms by redirecting authentication requests to a User object in eDirectory.

Password Replication

The process of ensuring that users' passwords are the same across all platforms by replicating password information between the platforms and eDirectory.

Platform

A system that uses the Core Driver for Identity Provisioning, Authentication Services, or both.

Platform Configuration File

The file that contains configuration information for Platform Services. It identifies users to include or exclude from processing, and contains information used to locate the Core Driver servers.

Platform Object

The object in the ASAM System container that contains information about a platform.

Platform Receiver

The Platform Services component that obtains provisioning events from Event Journal Services and runs Receiver scripts to process them as appropriate for the platform.

Platform Services

The Identity Manager Fan-Out Driver components that run on a platform. These include the System Intercept, the Platform Services Process, the AS Client API, the Platform Receiver, and Receiver scripts.

Platform Services Cache Daemon

The process that runs on a platform and communicates with the Core Driver for Posix account information. Along with the Name Service Switch, the Platform Service Cache Daemon provides complete account redirection.

Platform Services Process

The process that runs on a platform and communicates with the Core Driver for Authentication Services. The Platform Services Process provides Core Driver server connection management, load balancing, and failover capability.

Platform Set

A group of platforms that share a common set of users and groups.

Platform Set Search Object

An eDirectory object used to specify users and groups to be included in a Platform Set.

Primary Core Driver

The Core Driver that serves the Web interface, provides environmental information during the installation of other Core Drivers, performs Census Trawls, and listens for events from eDirectory.

Provisioning Event

An event, such as an add, modify, or delete, originating from eDirectory, that pertains to a user account or group. The Event Subsystem subscribes to events from eDirectory and passes them to Object Services. Object Services records provisioning events in eUser and eGroup objects. Event Journal Services passes the events to Platform Receivers. Platform Receivers run Receiver scripts to process provisioning events as appropriate for the platform.

Provisioning Manager

The Core Driver component that comprises Object Services, Audit Services, Certificate Services, Event Journal Services, and Web Services. Platforms access the Provisioning Manager to obtain a security certificate and to obtain provisioning events.

Receiver Script

A script invoked by the Platform Receiver to process provisioning events. A fully functional set of base scripts, written in the customary scripting language for the platform, is provided. You can extend these scripts as appropriate for your needs.

Secondary Core Driver

Any Core Driver other than the primary Core Driver.

Secure Sockets Layer (SSL)

The communications protocol used for communication between components. SSL is a standard security protocol that provides communications privacy. The protocol allows client/server applications to communicate in a way that is designed to prevent eavesdropping, tampering, and message forgery.

System Intercept

A vendor-provided control point into the system that is used to interface with Authentication Services for a platform.

System Log

The operating system log of information that is of system-wide interest.

Trawl

The process used by Object Services to collect information from eDirectory to initially build and periodically ensure the validity of the Census.

Universal Time

By international agreement, the world-wide standard for systematic time keeping. Universal Time is based on the mean solar time at zero degrees longitude. Formerly known as GMT, Universal Time is abbreviated as Z or as UT.

User and Group Subtree

The high level container object that you specify during installation of the Core Driver that holds users and groups that can be included in the Census. The ASAM Master User is granted Supervisor rights to this container.

Web Application

The Web-based application that is used to administer and monitor the Identity Manager Fan-Out Driver. The application is accessed as a plug-in to the iManager interface.

Web Services

The Core Driver component that provides the Web interface.
