# 1.0 Overview

The NetIQÂ® Identity Manager 4.8 driver for CA Top Secret synchronizes data between the Identity Vault and a connected system running Top Secret Security for z/OS. The driver runs on the targeted z/OS system. The Identity Vault runs on any Identity Manager supported platform and communicates with the driver on the target z/OS system over a secure network link.

The driver uses embedded Remote Loader technology to communicate with the Identity Vault, bidirectionally synchronizing changes between the Identity Vault and the connected system. The embedded Remote Loader component, also called the driver shim, runs as a started task on the connected z/OS system. There is no requirement to install Java\* on the connected system.

The Subscriber shim commits changes to the security system using customizable REXX execs that issue native TSO commands.

The Publisher shim uses standard security system exit routines to capture events of interest and submits them to the Metadirectory engine.

The driver uses a scriptable framework, designed so that you can easily add support for existing and future applications.

The Identity Manager 4.8 driver for Top Secret combines the flexibility of the Fan-Out driver and the bidirectional support and Identity Manager policy options available from traditional Identity Manager drivers. Key features of the driver include:

* Bidirectional synchronization of data without requiring Java or a separate Remote Loader
* Customizable schema to integrate all aspects of account administration
* Customizable REXX execs to handle all data to be synchronized
* Configuration on the z/OS system using traditional sequential files
* Driver shim implemented as a traditional z/OS started task
* Operator command control for starting and stopping the driver shim, configuring Remote Loader options, and displaying status information

The following sections present a basic overview of the driver:

* [Driver Architecture](b3wvpsh.html)
* [Configuration Overview](b3wx9up.html)
