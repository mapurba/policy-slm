# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler, then right-click the driver line and click Properties > Driver Configuration.

The Driver Configuration options are divided into the following sections:

* [Driver Module](driver-configuration.html#driver-module)
* [Driver Object Password](driver-configuration.html#driver-object-password)
* [Authentication](driver-configuration.html#authentication)
* [Startup Option](driver-configuration.html#startup-option)
* [Driver Parameters](driver-configuration.html#driver-parameters)
* [ECMAScript](driver-configuration.html#ecmascript)
* [Global Configurations](driver-configuration.html#global-configurations)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

*Native:*
This option is not used with the eDirectory driver.

*Connect to Remote Loader:*
The Remote Loader is not used with the eDirectory driver. However, Designer includes two suboptions, one (Driver Object Password) of which is required to set up authentication between two eDirectory drivers. If you use a driver object password, you need to select the Connect to Remote Loader option, set the password, click Apply to save the password, then select the Java option again.

* *Remote Loader Client Configuration for Documentation:*
  This option is not used with the eDirectory driver.
* *Driver Object Password:*
  Specifies a password for the eDirectory driver. This password must match the [Application Password:](driver-configuration.html#bsdltk7) set for the destination eDirectory driver.

## A.1.2 Driver Object Password

The driver object password is used to enable the eDirectory driver’s Subscriber channel to authenticate to the Publisher channel of the destination eDirectory driver. This authentication, although it is optional, provides an extra layer of security between the two drivers.

In Designer, this setting is located under the [Connect to Remote Loader:](driver-configuration.html#bsdlqlm) option.

For additional information about setting up authentication between the two drivers, see [Section 5.0, Securing Driver Communication](securing-driver-communication.html).

*Driver Object Password:*
Specifies a password for the eDirectory driver. This password must match the [Application Password:](driver-configuration.html#bsdltk7) set for the destination eDirectory driver.

## A.1.3 Authentication

The Authentication section stores the information required to authenticate to the connected system. For the eDirectory driver, it stores the information required to authenticate to the connected eDirectory driver and tree.

*Authentication information for server:*
Displays or specifies the server that the driver is associated with.

*Authentication ID:*
This ID is used by the driver to authenticate to the destination eDirectory driver. The ID is automatically generated and stored in this field when you run the NDS-to-NDS Driver Certificates Wizard. Authentication ID is used for establishing the secure connection. Format of the data in the Authentication ID field is the name of the local KMO object to use for the connection. This KMO object should be present in the local directory tree. For example, if eDirectory driver is configured between Server1 and Server2:

* Authentication ID on server1 is : eDirectory(Server1)
* Authentication ID on Server2 is : eDirectory(Server2)

  Both KMOs eDirectory(Server1) and eDirectory(Server2) should be signed by the same certificate authority (CA).

For information, see [Section 5.0, Securing Driver Communication](securing-driver-communication.html).

*Authentication Context:*
Specify the hostname or IP address of the destination server as well as the decimal port number (for example, 187.168.1.1:8196).

You can specify a separate port for Subscriber and Publisher channels by specifying a second port number following a second colon. If a second port number is specified, the Publisher channel uses the second port number rather than using the same port number as the Subscriber channel (for example, 255.255.255.255:2000:2001).

If your server has multiple IP addresses, you can specify the IP address you want the Publisher channel to use. This requires specifying the remote IP address, the Subscriber channel port, the local IP address, and the Publisher channel port. For example. 137.65.134.81:2000:137.65.134.83:2000 specifies that the Subscriber channel communicates with the remote tree on 137.65.134.81, port 2000, and that the Publisher channel listens on 137:65.134.83, port 2000.

If you see java.net.ConnectException: Connection Refused, no port connection is available in the other eDirectory tree. This error might be caused by one of the following:

* The driver in the other eDirectory tree is not running.
* The driver is running but is configured to use a different port.

*Remote Loader Connection Parameters:*
The eDirectory driver does not support the use of the Remote Loader. These options do not apply.

*Application Password:*
The application password, when used in conjuction with the driver object password, enables the eDirectory driver’s Subscriber channel to authenticate to the Publisher channel of the destination eDirectory driver. This authentication, although it is optional, provides an extra layer of security between the two drivers.

This password be the same as the driver object password for the destination eDirectory driver.

For more information, see [Section 5.0, Securing Driver Communication](securing-driver-communication.html).

*Remote Loader Password:*
The eDirectory driver does not support the use of the Remote Loader. These options do not apply.

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer.

## A.1.4 Startup Option

The Startup Option section enables you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

*Do not automatically synchronize the driver:*
This option applies only if the driver is deployed and was previously disabled. If this is not selected, the driver re-synchronizes the next time it is started.

## A.1.5 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment.

The parameters are divided into the following categories:

* [Driver Settings](driver-configuration.html#bsdm0xp)
* [Subscriber Settings](driver-configuration.html#bsdm15u)
* [Publisher Settings](driver-configuration.html#bsdm2v6)

### Driver Settings

*SSL type:*
Specifies whether to use a Key Material Object (KMO) for SSL or use a Java keystore file to secure the eDirectory driver communication. If you select keystore, provide the following mandatory parameters:

* *Name of the keystore file:*
  Specify the name of the Java keystore file. If the file path is not specified, the file must be available in the eDirectory DIB file directory.
* *Keystore password:*
  Specify the password to access the Java keystore file that contains the SSL certificates.
* *Reenter Keystore password:*
  Specify the password again.
* *Remove existing password:*
  Enable this option if you do not want to specify the keystore password. If you select this option, the Keystore password option is automatically disabled.
* *Name of certificate (key alias):*
  Specify the name of the key and certificate used when creating the keystore. The Java keytool program refers to this parameter as the alias.
* *Certificate password (key password):*
  Specify the password for the key created in the keystore.
* *Reenter Certificate password (key password):*
  Specify the key password again.
* *Remove existing password:*
  Enable this option if you do not want to specify the key password. If you select this option, the Certificate password option is automatically disabled.
* *Advanced options:*
  Select Show to display the advanced options.
* *Subscriber acts as server for SSL handshake:*
  Ideally, the SSL handshake protocol has the subscriber acting as the client side of the SSL handshake. Select Yes to reverse the protocol and set the subscriber as the server side of the SSL handshake.
* *Disable mutual authentication - only used if acting as server:*
  Select Yes to disable the SSL mutual authentication. This option is applicable only if you set subscriber as the server side of the SSL handshake.

*Secure Protocol:*
Specifies the version of the TLS protocol that is used to establish a connection between eDirectory drivers. Identity Manager supports TLSv1, TLSv1\_1, and TLSv1\_2.

### Subscriber Settings

*Address or host name of remote publisher:*
Specifies the IP address or DNS name of the server hosting the remote eDirectory driver that the local subscriber connects to.

*TCP port of remote publisher:*
If the remote publisher options specify a TCP port, this must be set to specify and the value from the remote Publisher channel entered into the Port number field. (These two fields must match what is set in the remote Publisher channel's options, which have corresponding fields).

*Port number:*
Specifies the port number that the remote publisher is configured to run on. Displays only if you select specify in the TCP port of remote publisher field.

*Advanced options:*
Displays additional fields when you select show.

*Socket local bind:*
The local bind fields specify which IP address the Subscriber channel’s socket will be bound to. This is generally only useful if the server has more than one IP address and it is important to bind to a particular address because of firewall settings.

*Local bind address for subscriber socket:*
The local bind fields specify which IP address the Subscriber channel's socket will be bound to. This is generally only useful if the server has more than one IP address and it is important to bind to a particular address because of firewall settings.

*Receive timeout in minutes:*
In order to detect a lost TCP/IP connection, the eDir-to-eDir driver periodically sends small packets. This value determines how long after entering a receive-wait condition the Subscriber channel waits until sending a keep-alive packet to determine if the TCP/IP connection has been lost. Generally, do not change this value except under instruction from NetIQ.

The default value for the Subscriber channel is one minute.

### Publisher Settings

*Publisher heartbeat interval:*
Specifies how often you want the driver to send a status message along the Publisher channel when there has not been any traffic during the interval time.

*Local bind address for publisher socket:*
Specifies which IP address the Subscriber channel's socket will be bound to. This is generally only useful if the server has more than one IP address and it is important to bind to a particular address because of firewall settings. This setting applies to the local publisher's “server” socket on which the local publisher listens for connections from the remote Subscriber channel.

*Receive timeout in minutes:*
In order to detect a lost TCP/IP connection, the eDirectory driver periodically sends small packets. This value determines how long after entering a receive-wait condition the Publisher channel waits until sending a keep-alive packet to determine if the TCP/IP connection has been lost. Generally, do not change this value except under instruction from NetIQ.

The default value for the Publisher channel is ten minutes.

## A.1.6 ECMAScript

Enables you to add ECMAScript resource files. The resources extend the driver’s functionality when Identity Manager starts the driver.

## A.1.7 Global Configurations

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
