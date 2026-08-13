# A.1 Driver Configuration

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select click Properties > Driver Configuration.

In Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.

The following sections describe driver configuration in details:

* [Driver Module](driver-configuration.html#b4jzjxt)
* [Driver Object Password](driver-configuration.html#b4jzp0o)
* [Authentication](driver-configuration.html#b4jzr84)
* [Startup Option](driver-configuration.html#b4m4gci)
* [Driver Parameters](driver-configuration.html#b4m4h9a)
* [Global Configurations](driver-configuration.html#brndxwr)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

* The name of the Java class for the User Management driver is: com.novell.nds.dirxml.driver.ebs.user.EBSUserDriver
* The name of the Java class is for the HR driver is: com.novell.nds.dirxml.driver.ebs.hr.EBSHRDriver
* The name of the Java class for the TCA driver is: com.novell.nds.dirxml.driver.ebs.tca.EBSTCADriver

*Native:*
This option is not used with the Oracle drivers.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the Oracle EBS system. Designer includes two suboptions:

* *Remote Loader Client Configuration for Documentation:*
  Includes information on the Remote Loader client configuration when Designer generates documentation for the Oracle User driver.
* *Driver Object Password:*
  Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

## A.1.2 Driver Object Password

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The authentication section stores the information required to authenticate to the Oracle EBS system.

*Authentication ID:*
Specify an Oracle account that the driver can use to authenticate to the Oracle system.

For example:

For all drivers (User Management, HR, or TCA), assign System Administrator responsibility to the user.

*Authentication Context:*
Specify the IP address or name of the Oracle EBS server the driver should communicate with. For example, http://myoracleserver.com:8000/webservices/SOAProvider/plsql/idm\_driver\_s/.

*NOTE:*To test the connection with Oracle EBS server, use the following command:

curl -v -u "$USERNAME:$PASSWORD" -H "$CONTENTTYPE" -H "$SOAPACTION" -d "$POSTDATA" "$SOAPURL"

*Remote Loader Connection Parameters:*
Used only if the driver is connecting to the application through the Remote Loader.

In Identity Console, enter hostname=xxx.xxx.xxx.xxx port=xxxx secureprotocol=TLS version enforceSuiteB=true/false kmo=certificatename.

* hostname specifies the IP address of the Remote Loader server.
* port specifies the TCP/IP port on which the Remote Loader listens for connections from the remote interface shim. The default port for the Remote Loader is 8090.
* secureprotocol specifies the version of the TLS protocol that the Remote Loader uses to connect to the Identity Manager engine. Identity Manager supports TLSv1, TLS v1\_1, and TLSv1\_2 versions only.
* enforceSuiteB specifies whether the Remote Loader uses Suite B for communicating with the Identity Manager engine. To use Suite B, specify enforceSuiteB=true. The communication supports only TLS version 1.2 version. Communication is not established if the connection has non-Suite B authentication algorithms.
* The kmo entry is optional. Use it only when an SSL connection exists between the Remote Loader and the Identity Manager engine.

  For example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Application Password:*
Specify the password for the user object listed in the Authentication ID field.

*Remote Loader Password:*
Used only if the driver is connecting to the application through the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the Oracle EBS system.

*Driver Cache Limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer.

## A.1.4 Startup Option

The Startup Option allows you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

*Do not automatically synchronize the driver:*
This option only applies if the driver is deployed and was previously disabled. If this is not selected, the driver re-synchronizes the next time it is started.

## A.1.5 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment.

The parameters are presented by category:

* [Subscriber Options](driver-configuration.html#bs4ccga)
* [Publisher Options](driver-configuration.html#bs4cgqb)

### Subscriber Options

*Subscriber Channel Enabled:*
By default, the Subscriber channel is enabled. This means that the events are synchronized from the Identity Manager to the Oracle EBS system. Fill the following fields for the Subscriber options:

*Use SSL:*
By default, the SSL connection is enabled to secure communication between the driver and the Oracle EBS server. Specify No to not use SSL. For more information, see [Section 5.0, Securing Communication](securing-communication.html).

If you use SSL, fill in the following parameters:

*Truststore File:*
Specifies the name and path of the keystore file containing the trusted certificates used when the remote server is configured to provide server authentication. For example, c:\security\truststore. Leave this field empty when server authentication is not used.

*Set Mutual Authentication Parameters:*
Specify Yes to set mutual authentication information. Specify No to not use mutual authentication.

* *Keystore File:*
  Specify the path and the name of the keystore file that contains the trusted certificates for the remote server to provide mutual authentication. For example, C:\security\keystore. Leave this field blank when mutual authentication is not used.
* *Keystore Password:*
  Specify the password for the keystore file. Leave this field blank when mutual authentication is not used.

*Use Proxy:*
Specify Yes if you want to use the proxy connection. Specify No to not use proxy.

* *Proxy Host and Port:*
  Specify the host address and the host port when a proxy host and port are used. For example: xxx.xx.x.x:xxxxx.

  Or, if a proxy host and port are not used, leave this field empty.
* *Proxy Username:*
  Specify a name for the proxy connection.
* *Proxy Password:*
  Specify a password for the proxy connection.

*HTTP Errors to Retry:*
The HTTP error codes that return a retry status. The list of integers is separated by spaces. The error codes are: 307 404 408 503 504.

### Publisher Options

*Publisher Channel Enabled:*
By default, the Publisher channel is enabled. The events are synchronized from the Oracle EBS system to Identity Manager. Fill the following fields for the Publisher options:

*Listening IP Address and Port:*
Specifies the IP address of the server where the Oracle EBS driver is installed and the port number that this driver listens on.

Choose an unused port number on your server. For example: 192.168.10.1:18180. The driver listens on this address for incoming requests, processes the requests, and returns a result. Leave this field blank when the Publisher channel is not active.

*Authentication ID:*
Specify the Authentication ID that the driver will use to validate the Publisher events from the Oracle EBS system. It is communicated to the Oracle EBS system when the driver is started. The driver uses it to determine which events it should ignore. For example, it ignores events from the unauthorized connected systems.

*Authentication Password:*
Specify the authentication password that the driver will use to validate the Publisher events from the Oracle EBS system. It is communicated to the Oracle EBS system when the driver is started.

If you need to clear the password, select Remove existing password, then click Apply.

*Server Key Alias:*
When this server is configured to accept HTTPS connections, this is the key alias. Leave this field blank when a KMO name is used or when HTTPS connections are not used.

*Server Key Password:*
When this server is configured to accept HTTPS connections, this is the key alias password (not the keystore password). Leave this field blank when a KMO name is used or when HTTPS connections are not used.

*Use SSL:*
By default, the SSL connection is used for secure communication between the Oracle drivers and the Oracle EBS server. Specify No to not use SSL. For more information, see [Section 5.0, Securing Communication](securing-communication.html).

When SSL is used, fill the following parameters:

*Select Certificate Store Mode:*
There are two options: KMO and Keystore. Select KMO if you are using eDirectory KMO for secure connection. Select Keystore to use the Java Keystore.

*KMO Name:*
If you select KMO for the secure connection, specify the KMO name to be used in eDirectory.

When the server is configured to accept HTTPS connections, this name becomes the KMO name in the Identity Vault. The KMO name is the name before the “-” (dash) in the RDN.

Leave this field empty when a keystore file is used or when HTTPS connections are not used.

*Keystore File:*
If Keystore option is used for the secure connection, this field specifies the keystore name and path to the keystore file. This file is used when the server is configured to accept HTTPS connections.

Leave this field empty when a KMO name is used or when HTTPS connections are not used.

*Keystore Password:*
Specifies the keystore file password used with the Keystore File field when this server is configured to accept HTTPS connections.

Leave this field empty when a KMO name is used or when HTTPS connections are not used.

*Server Key Alias:*
Specifies a Server key alias when this server is configured to accept HTTPS connections.

Leave this field empty when a KMO name is used or when HTTPS connections are not used.

*Server Key Password:*
When this server is configured to accept HTTPS connections, this is the key alias password (not the keystore password). Leave this field empty when a KMO name is used or when HTTPS connections are not used.

*Require Mutual Authentication:*
When using SSL, it is common to do only server authentication. However, if you want to force both client and server to present certificates during the handshake process, mutual authentication is required.

*Polling Interval in Seconds:*
Specifies how often the Publisher channel polls for unprocessed events. Leave this field blank to turn off the polling. The default value is 60 seconds.

*Heartbeat Interval in Minutes:*
Configures the driver shim to send a periodic status message on the Publisher channel when there has been no Publisher traffic for the given number of minutes. Leave this field empty to turn off the heartbeat. The default value is 1 minute.

## A.1.6 Global Configurations

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
