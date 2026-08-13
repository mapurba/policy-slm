# 1.0 Overview

The Identity Manager 4.8 driver for Linux and UNIX synchronizes data between the Identity Vault and a connected Linux or UNIX system. The driver runs on a target system, such as Linux, Solaris\*, AIX\*, or HP-UX\*. The Identity Vault runs on any platform supported by Identity Manager and communicates with the driver on the connected system over a secure network link.

The driver uses embedded Remote Loader technology to communicate with the Identity Vault, bidirectionally synchronizing changes between the Identity Vault and the connected system. The embedded Remote Loader component, also called the driver shim, runs as a native process on the connected Linux or UNIX system. There is no requirement to install Java\* on the connected system.

The driver commits changes to the connected system using customizable shell scripts that issue native system commands. The publication method uses a polling script that scans the system for changes, and a change log to save changes for subsequent publishing. Password changes are sent to the change log using the authentication module framework and are then published to the Identity Vault.

The Linux and UNIX driver uses a scriptable framework, designed so that you can easily add support for existing and future applications.

The Identity Manager 4.8 driver for Linux and UNIX combines the flexibility of the Fan-Out driver for Linux and UNIX systems as well as the bidirectional support and Identity Manager policy options available with the NIS driver. Key features of the driver include:

* Bidirectional synchronization of data without requiring Java or a separate Remote Loader
* Customizable schema to integrate all aspects of Linux and UNIX account administration
* Customizable shell scripts to handle all data to be synchronized
* Low memory and processor requirements on the Metadirectory server
* No LDAP or Fan-Out core driver configuration

The following sections present a basic overview of the Linux and UNIX driver:

* [Driver Architecture](b3wvpsh.html)
* [Configuration Overview](b3wx9up.html)
