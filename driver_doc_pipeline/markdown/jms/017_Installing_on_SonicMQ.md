# 4.3 Installing on SonicMQ

As part of installing SonicMQ for the driver, you should complete the following tasks consecutively. These instructions are for Linux, but you can follow the same procedure for other platforms.

* [Locating Prerequisite Jar Files](installing-on-sonicmq.html#b5kflt9)
* [Running Scripts to Configure the Messaging System](installing-on-sonicmq.html#b5khti1)

## 4.3.1 Locating Prerequisite Jar Files

1. On your messaging server, locate the following jar files:

   * mfcontext.jar
   * sonic\_ASPI.jar
   * sonic\_Channel.jar
   * sonic\_Client.jar
   * sonic\_Crypto.jar
   * sonic\_Selector.jar
   * sonic\_SF.jar
   * sonic\_SSL.jar
   * sonic\_XA.jar
   * sonic\_XMessage.jar
2. Copy the jar files to the Identity Manager server.

   The following table identifies where to place jar files on an Identity Management server, by platform.

   | Platform | Directory Path |
   | Windows | Local installation: novell\NDS\lib  Remote installation: novell\RemoteLoader\lib |
   | Linux/UNIX | Local installation: /usr/lib/dirxml/classes (pre-eDirectory 8.8) or opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8)  Remote installation: /usr/lib/dirxml/classes (pre-eDirectory 8.8) or /opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8) |
3. If necessary, restart your eDirectory server.
4. Continue with [Running Scripts to Configure the Messaging System](installing-on-sonicmq.html#b5khti1).

## 4.3.2 Running Scripts to Configure the Messaging System

Use the following instructions to locate and run the scripts to configure your message system.

1. Locate where you installed the installation script (idm\_jms\_install.cli) during the JMS driver installation. The following table indicates the default directories where scripts are installed, by platform.

   | Platform | Directory Path |
   | Windows | C:\Novell\IdentityManager\NDS\DirXMLUtilities\jms\sonic |
   | Linux\UNIX | install-dir/lib/dirxml/rules/jms/sonic |
2. Copy the script to your messaging server.
3. Follow the instructions provided in the script.
