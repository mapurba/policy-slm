# 1.0 Overview

The Identity Manager driver for Linux and UNIX Settings automates the management of Linux and UNIX operational attributes, such as login shell, UID, GID, and home directory, in the Identity Vault.

This enables you to provision systems using other drivers, such as the Linux and UNIX driver or the Fan-Out driver. This also enables you to use account redirection via LDAP, Name Service Switch, or PAM modules.

You can also use the driver to automate enabling users for Linux User Management (LUM) and NetIQÂ® Samba. LUM simplifies user management in a networked environment with many Linux workstations and servers by storing all necessary properties in the Identity Vault rather than locally on each machine. NetIQ Samba provides Windows\* access (CIFS and HTTP-WebDAV) to files stored on the OES server.

Without the Linux and UNIX Settings driver, you must use iManager to set up each user individually. The driver uses Identity Manager events and performs the same functions as the LUM and NetIQ Samba iManager plug-ins, but without the manual activity. For the detailed steps taken by the driver to set up users, see [LUM Automation](b3fz6ex.html) and [Samba Automation](b3fz6nm.html).

You must modify the Linux Workstation objects, selecting the LUM-enabled groups for the workstations to be members of, in order for users to be able to log in to OES or NetIQ Samba.
