# 2.4 Participating Systems

You can install the components of the Identity Manager 4.8 driver for Linux and UNIX to a single system, but the components are typically installed on two systems. The driver is installed on a Metadirectory server. The driver shim is installed on the connected Linux or UNIX system. In addition, you can install the driver PAM module on NIS or NIS+ clients to publish password change information from them.

The connected system runs a lightweight process, called the driver shim or embedded Remote Loader, that communicates with the driver on the Metadirectory server over an encrypted TCP/IP network link.

The Metadirectory server and the connected system can be the same system if the system is running a version of Linux or UNIX supported as a connected system. This can be useful for testing and prototyping. Even if the Metadirectory server and the connected system are the same system, the driver is still run as a Remote Loader driver.
