# 2.2 Installing the Oracle EBS Driver Jar Files

You can install the Oracle EBS driver(s) shim in the following ways:

* On a local machine: Install the Oracle EBS driver files on the Identity Manager server and use a SOAP/REST endpoint to connect to the Oracle EBS system. For information on installing the Identity Manager server, see "[Planning Your Installation](../../../identity-manager-48/setup_linux/data/planning-an-identity-manager-installation.html#planning-an-identity-manager-installation)" in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or "[Planning Your Installation](../../../identity-manager-48/setup_windows/data/planning-an-identity-manager-installation.html#planning-an-identity-manager-installation)" in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).
* On a remote machine: Install the Remote Loader (required to run the driver on a non-Identity Manager server) and the Oracle EBS driver files on a non-Identity Manager server where you want to run the driver. For information on installing the Remote Loader, see "[Installing Identity Manager](../../../identity-manager-48/setup_linux/data/install-identity-manager-linux.html#install-identity-manager-linux)" in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Installing and Configuring Identity Manager Components](../../../identity-manager-48/setup_windows/data/installation-and-configuration-process-overview.html#installation-and-configuration-process-overview) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

To communicate with the Oracle EBS, the Oracle EBS driver requires that you copy the appropriate Oracle EBS driver jar files to the driver location.

1. Locate the appropriate Oracle EBS driver jar files.

   The Oracle EBS driver jar files are generally present on the system. Check for the following files in the /opt/novell/eDirectory/lib/dirxml/classes directory:

   * EBSHRShim.jar
   * EBSShim.jar
   * EBSTCAShim.jar
   * EBSUserShim.jar
2. Place the files in the appropriate location.

   The following tables show the default paths where the driver files are placed on an Identity Manager server or on a Remote Loader server.

   *Table 2-1* Locations for JAR Files: Identity Manager Server

   | Platform | Directory Path |
   | Linux | /opt/novell/eDirectory/lib/dirxml/classes |
   | Windows | C:\novell\NDS\lib |

   *Table 2-2* Locations for JAR Files: Remote Loader

   | Platform | Directory Path |
   | Linux | /opt/novell/eDirectory/lib/dirxml/classes |
   | Windows | C:\novell\RemoteLoader\lib |
