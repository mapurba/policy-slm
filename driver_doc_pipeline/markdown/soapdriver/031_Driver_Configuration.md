# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon or line, then select click Properties > Driver Configuration.

The Driver Configuration options are divided into the following sections:

* [Driver Module](driver-configuration.html#b4jzjxt)
* [Authentication](driver-configuration.html#b4jzr84)
* [Startup Option](driver-configuration.html#b4m4gci)
* [Driver Parameters](driver-configuration.html#b4m4h9a)
* [ECMAScript](driver-configuration.html#brv2j9u)
* [Global Configuration](driver-configuration.html#brv2k2v)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The Java class name is: com.novell.nds.dirxml.driver.soap.SOAPDriver

*Native:*
This option is not used with the SOAP driver.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two suboptions:

* Remote Loader Client Configuration for Documentation: Includes information on the Remote Loader client configuration when Designer generates documentation for the driver.
* Driver Object Password: Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.2 Authentication

The authentication section stores the information required to authenticate to the connected system.

*Authentication ID:*
This option is not used with the SOAP driver. The SOAP driver requires separate authentication settings for both the [Subscriber Options](driver-configuration.html#bs4ccga) and the [Publisher Options](driver-configuration.html#bs4cgqb).

*Authentication Context:*
This option is not used with the SOAP driver.

*Remote Loader Connection Parameter:*
Used only if the driver is connecting to the application through the Remote Loader.

In Identity Console, enter hostname=xxx.xxx.xxx.xxx port=xxxx secureprotocol=TLS version enforceSuiteB=true/false kmo=certificatename.

* hostname specifies the IP address of the Remote Loader server.
* port specifies the TCP/IP port on which the Remote Loader listens for connections from the remote interface shim. The default port for the Remote Loader is 8090.
* secureprotocol specifies the version of the TLS protocol that the Remote Loader uses to connect to the Identity Manager engine. Identity Manager supports TLSv1, TLS v1\_1, and TLSv1\_2 versions only.
* enforceSuiteB specifies whether the Remote Loader uses Suite B for communicating with the Identity Manager engine. To use Suite B, specify enforceSuiteB=true. The communication supports only TLS version 1.2 version. Communication is not established if the connection has non-Suite B authentication algorithms.
* The kmo entry is optional. Use it only when an SSL connection exists between the Remote Loader and the Identity Manager engine.

  For example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Application Password:*
This option is not used with the SOAP driver.

*Remote Loader Password:*
Used only if the driver is connecting to the application through the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the connected system.

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer.

## A.1.3 Startup Option

The Startup Option section allows you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

*Do not automatically synchronize the driver:*
This option applies only if the driver is deployed and was previously disabled. If this option is not selected, the driver re-synchronizes the next time it is started.

## A.1.4 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment.

The parameters are presented by category:

* [Driver Options](driver-configuration.html#bs4c7yk)
* [Subscriber Options](driver-configuration.html#bs4ccga)
* [Publisher Options](driver-configuration.html#bs4cgqb)

### Driver Options

*<nds>, <input>, <output> Element Handling:*
Specify Remove/add elements if you want the driver shim to remove and add the required <nds>, <input>, and <output> XML elements.

*query-ex operation supported:*
Select Yes if you want the driver shim to report support for the query-ex operation to the engine. Select Yes only if you are adding explicit support in your driver policy and transforms for the query-ex feature and if it can be supported by your target application or Web service. Most SOAP driver implementations should be set to No.

*Custom Java Extensions:*
Select Show if you have developed custom Java classes to extend the driver shim’s functionality. Otherwise, select Hide.

* *Document Handling:*
  Select Implemented if you have developed a custom Java class to process data as XML documents.
* *Byte array handling:*
  Select Implemented if you have developed a custom Java class to process data as a byte array.
* *Subscriber Transport Layer Replacement:*
  Select Implemented if you have developed a custom Java class to replace the default HTTP transport layer for the Subscriber channel.
* *Publisher Transport Layer Replacement:*
  Select Implemented if you have developed a custom Java class to replace the default HTTP transport layer for the Publisher channel.
* *Schema:*
  Select Implemented if you have developed a custom Java class to provide the application schema to the driver.

For more information, see [Section B.0, Using Java Extensions](using-java-extensions.html).

### Subscriber Options

*URL of the SOAP server or Web Service:*
Specify the URL of the remote server and the port number that the server listens on.

The URL should begin with http:// unless you have configured SSL settings, in which case it should begin with https:// and use a DNS hostname rather than an IP address.

*Authentication ID:*
If the remote server requires an authentication ID, specify the ID in the field. Otherwise, leave the field empty.

*Authentication Password:*
Specify the authentication password for the remote server if you specified an [Authentication ID:](driver-configuration.html#bs4cd8e). Otherwise, leave the field empty.

If you need to clear the password, select Remove existing password, then click Apply.

*Truststore File:*
Specify the name and path of the keystore file containing the trusted certificates used when the remote server is configured to provide server authentication. For example, c:\security\truststore. Leave this field empty when server authentication is not used.

*Set mutual authentication parameters:*
Specify Show to set mutual authentication information. Specify Hide to not use mutual authentication.

* *Keystore file:*
  Specify the path and the name of the keystore file that contains the trusted certificates for the remote server to provide mutual authentication. For example, C:\security\keystore. Leave this field blank when mutual authentication is not used.
* *Keystore password:*
  Specify the password for the keystore file. Leave this field blank when mutual authentication is not used.

*Proxy host and port:*
Specify the host address and the host port when a proxy host and port are used. For example: 192.10.1.3:18180.

Or, if a proxy host and port are not used, leave this field empty.

*Handle HTTP session cookies:*
Some HTTP applications set cookies and expect them to be present on future requests. Select Handle Cookies if you want the driver to keep track of session cookies.

Cookies are only kept until the driver is stopped.

*Process empty subscriber documents:*
Indicates whether or not the Subscriber channel should send the empty documents to the target application. Documents could be empty if the policy or the style sheets strip the XML without vetoing the command.

*HTTP errors to retry:*
Specify the HTTP errors that must return a retry status. Error codes must be a list of integers separated by spaces. For example, 307 404 408 503 504.

*Response Time out:*
Specify the time in milliseconds for getting a response from the remote SOAP server after which the request returns an error.

*Customize HTTP Request Header Fields:*
Select Show to enable customized header fields or select Hide to disable the feature. Each of the following fields is conditional, depending on if you select Use or Ignore.

* *Authorization:*
  If you select Use, specify the key and value in the appropriate fields. This header is automatically used if you enter an authentication ID and password in the Subscriber Settings.
* *Context Type:*
  If you select Use, specify the key and value in the appropriate fields.
* *SOAPAction:*
  If you select Use, specify the key and value in the appropriate fields.
* *Optional Request Header:*
  If you select Use, specify the key and value in the appropriate fields. You can specify up to three optional request headers.

### Publisher Options

*Listening IP address and port:*
Specify the IP address of the server where the SOAP driver is installed and the port number that this driver listens on.

If you imported a sample configuration file, this field contains the IP address and port that you specified in the wizard.

*Authentication ID:*
Specify the Authentication ID of the remote server to validate incoming requests. If the remote server does not send an Authentication ID, leave this field empty.

If you imported a sample configuration file, this field contains the IP address and port that you specified in the wizard.

*Authentication Password:*
Specify the authentication password of the remote server to validate incoming requests if you entered an Authentication ID above. Otherwise, leave these fields empty.

If you need to clear the password, select Remove existing password, then click Apply.

*KMO name:*
Specify the KMO name to be used in eDirectory.

When the server is configured to accept HTTPS connections, this name becomes the KMO name in eDirectory. The KMO name is the name before the “-” (dash) in the RDN.

Leave this field empty when a keystore file is used or when HTTPS connections are not used.

*Keystore file:*
Specify the keystore name and path to the keystore file. This file is used when the server is configured to accept HTTPS connections.

Leave this field empty when a KMO name is used or when HTTPS connections are not used.

*Keystore password:*
Specify the keystore file password used with the [Keystore file:](driver-configuration.html#bs4cfp1)keystore file specified above when this server is configured to accept HTTPS connections.

Leave this field empty when a KMO name is used or when HTTPS connections are not used.

*Server key alias:*
Specify a Server key alias when this server is configured to accept HTTPS connections.

Leave this field empty when a KMO name is used or when HTTPS connections are not used.

*Server key password:*
When this server is configured to accept HTTPS connections, this is the key alias password (not the keystore password). Leave this field empty when a KMO name is used or when HTTPS connections are not used.

*Require mutual authentication:*
When using SSL, it is common to do only server authentication. However, if you want to force both client and server to present certificates during the handshake process, you should require mutual authentication.

*Heartbeat interval in seconds:*
Specify the heartbeat interval in seconds.

Leave this field empty to turn off the heartbeat.

*NOTE:*A SOAP client calling the Web service in the Publisher channel must specify a URL ending with a slash. For example, http://1.1.1.1:9095/. Without a context path (the slash), the driver does not process the request received.

## A.1.5 ECMAScript

Displays an ordered list of ECMAScript resource files. The files contain extension functions for the driver that Identity Manager loads when the driver starts. You can add additional files, remove existing files, or change the order the files are executed.

## A.1.6 Global Configuration

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
