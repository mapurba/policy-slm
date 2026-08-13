# 4.4 Installing on TIBCO EMS

As part of installing TIBCO for the driver, you should complete the following tasks consecutively. These instructions are for Linux and Windows.

* [Locating Prerequisite Client Jar Files](installing-on-tibco-ems.html#b95q5bk)
* [Running Scripts to Configure the Messaging System](installing-on-tibco-ems.html#b95q5bs)

## 4.4.1 Locating Prerequisite Client Jar Files

1. On your messaging server, locate the following jar files:

   * tibjms.jar
   * tibcrypt.jar
2. The following table identifies where to place jar files on a TIBCO server, by platform:

   | Platform | Directory Path |
   | Windows | C:tibco\ems\clients\java |
   | Linux | /opt/tibco/ems/clients/java |
3. Copy the jar files to the Identity Manager server.

   The following table identifies where to place jar files on an Identity Management server, by platform:

   | Platform | Directory Path |
   | Windows | Local installation: novell\NDS\lib  Remote installation: novell\RemoteLoader\lib |
   | Linux/UNIX | Local installation: /usr/lib/dirxml/classes (pre-eDirectory 8.8) or opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8)  Remote installation: /usr/lib/dirxml/classes (pre-eDirectory 8.8) or /opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8) |
4. If necessary, restart your eDirectory server.
5. Continue with [Running Scripts to Configure the Messaging System](installing-on-tibco-ems.html#b95q5bs).

## 4.4.2 Running Scripts to Configure the Messaging System

Use the following instructions to locate and run the scripts to configure your message system:

1. Locate where you installed the installation script (idm\_jms\_install.tib) during the driver installation. The following table indicates the default directories where scripts are installed, by platform:

   | Platform | Directory Path |
   | Windows | C:\Novell\IdentityManager\NDS\DirXMLUtilities\jms\tibco\_ems |
   | Linux\UNIX | install-dir/lib/dirxml/rules/jms/tibco\_ems |
2. Copy the idm\_jms\_install.tib and idm\_jms\_uninstall.tib scripts to your messaging server. The following table indicates the location where you should copy the scripts to on your messaging server, by platform.

   | Platform | Directory Path |
   | Windows | C:\tibco\ems\bin |
   | Linux/UNIX | /opt/tibco/ems/bin |
3. Update the IP address and port number of the connection factory in the idm\_jms\_install.tib script.
4. Change directories on the messaging server to run the tibjmsadmin utility. The following table indicates where the tibjmsadmin utility is installed, by platform.

   | Platform | Directory Path |
   | Windows | C:\tibco\ems\bin |
   | Linux/UNIX | /opt/tibco/ems/bin |
5. To run the installation script, enter the following at the command line prompt:

   >tibjmsadmin -script idm\_jms\_install.tib
