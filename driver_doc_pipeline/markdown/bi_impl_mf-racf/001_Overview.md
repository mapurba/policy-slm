# 1.0 Overview

The NetIQ® Identity Manager 4.8 driver for RACF synchronizes data between Identity Manager and a RACF installation on a connected mainframe. Identity Manager, installed on any Identity Manager supported platform, communicates with the driver on the target z/OS system over a secure network link.

The driver gives you access to RACF user and group attributes in accordance with the z/OS RACF schema. The driver also allows you to issue arbitrary TSO commands on the z/OS system. Identity Manager gives you access to eDirectory™ objects and their attributes via its Identity Vault.

The driver uses embedded Remote Loader technology to communicate with Identity Manager, bidirectionally synchronizing changes between the Identity Vault and RACF. It implements this technology using its own embedded Remote Loader component as part of the main driver shim, which runs as a started task on the connected z/OS system.

The driver shim’s Subscriber function commits changes to RACF using customizable REXX execs that issue native TSO commands through the z/OS service routine IKJEFTSR. This flexible interface provides the option for implementing additional business logic through REXX programming.

The driver shim’s Publisher function uses standard security system exit routines to capture events of interest and submits them to the Identity Manager Metadirectory engine.

The Identity Manager 4.8 driver for RACF combines the flexibility of the Fan-Out driver and the bidirectional support and Identity Manager policy options available from traditional Identity Manager drivers. Key features of the driver include:

* Bidirectional synchronization of data
* Customizable schema to integrate all aspects of account administration
* Customizable REXX execs to handle all data to be synchronized
* Driver shim implemented as a traditional z/OS started task
* Operator command control for starting and stopping the driver shim, configuring Remote Loader options, and displaying status information
* Support for RACF passwords and password phrases

The following sections present a basic overview of the driver:

* [Driver Architecture](b3wvpsh.html)
* [Configuration Overview](b3wx9up.html)
