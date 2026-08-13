# 1.0 Overview

The Identity Manager 4.8 driver for IBM i (i5/OS and OS/400) synchronizes data between the Identity Vault and a connected IBM i system. The driver runs on a target IBM i system. The Identity Vault runs on any platform supported by Identity Manager and communicates with the driver on the connected system over a secure network link.

The driver uses embedded Remote Loader technology to communicate with the Identity Vault, bidirectionally synchronizing changes between the Identity Vault and the connected system. The embedded Remote Loader component, also called the driver shim, runs as a native process on the connected IBM i system. There is no requirement to install Java\* on the connected system.

The driver commits changes to the connected system using customizable Control Language (CL) programs that issue native system commands. The publication method uses exits supplied by IBM for notification of changes and a change log to save changes for subsequent publishing.

The IBM i driver uses a scriptable framework, designed so that you can easily add support for existing and future applications.

The Identity Manager driver for IBM i continues the flexibility of previous versions while adding the bidirectional support and Identity Manager policy options available with traditional Identity Manager drivers. New features include:

* Bidirectional synchronization of data without requiring Java or a separate Remote Loader
* Customizable schema to integrate all aspects of IBM i account administration
* Customizable CL programs to handle all data to be synchronized
* Low memory and processor requirements on the Metadirectory server
* No LDAP or Fan-Out core driver configuration

The following sections present a basic overview of the IBM i driver:

* [Driver Architecture](b3wvpsh.html)
* [Configuration Overview](b3wx9up.html)
