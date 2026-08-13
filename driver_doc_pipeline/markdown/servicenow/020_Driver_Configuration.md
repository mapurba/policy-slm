# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon or line, then select click Properties > Driver Configuration.

The following sections describe driver configuration in details:

* [Driver Module](driver-configuration.html#b4jzjxt)
* [Driver Object Password](driver-configuration.html#b1hrfedj)
* [Authentication](driver-configuration.html#b4jzr84)
* [Startup Option](driver-configuration.html#b4m4gci)
* [Driver Parameters](driver-configuration.html#b4m4h9a)
* [ECMA Script](driver-configuration.html#b1huy0as)
* [Global Configuration](driver-configuration.html#brv2k2v)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Use this option to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally. Select this option to run the driver locally.

The Java class name is: com.novell.nds.dirxml.driver.ServiceNow.ServiceNowDriverShim

*Native:*
This option is not used with the ServiceNow driver.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two sub options:

* Remote Loader Client Configuration for Documentation: Includes information on the Remote Loader client configuration when Designer generates documentation for the driver.
* Driver Object Password: Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

*Name:*
Displays the java class name.

## A.1.2 Driver Object Password

Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The authentication section describes the parameters required for authentication to the connected system.

*Authentication ID:*
Specify a user application ID. This ID is used to pass Identity Vault subscription information to the application.

*Authentication Context:*
Specify the IP address or name of the server the application shim should communicate with.

*Remote Loader Connection Parameters:*
The syntax for the parameter is hostname=xxx.xxx.xxx.xxx port=xxxx kmo=certificatename, where the hostname is the IP address of the application server running the Remote Loader server and the port is the port the Remote Loader is listening on. The default port for the Remote Loader is 8090.

The kmo entry is optional. It is only used when there is an SSL connection between the Remote Loader and the Identity Manager engine.

Example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Driver Cache Limit (KB):*
Specify the maximum event cache file size. If the value is set to zero, the file size is unlimited.

*Application Password:*
Specify the password to connect to the application.

*Remote Loader Password:*
Specify the password to connect to the application through the remote loader. The password should match with the password specified during the configuration of the Remote Loader on the connected system.

## A.1.4 Startup Option

The Startup Option section allows you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

## A.1.5 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment.

The parameters are presented by category:

* [Driver Settings](driver-configuration.html#bs4c7yk)
* [Publisher Options](driver-configuration.html#bs4cgqb)

### Driver Settings

*ServiceNow Base URL:*
Specify the URL to connect to ServiceNow.

*ServiceNow Login ID:*
Specify the login ID to connect to ServiceNow.

ServiceNow Login Password: Specify the password for the login ID.

Select Remove existing password to clear the password.

*Always Accept Server Certificate:*
This option eliminates the need for manually maintaining a truststore. If you select No, you must have a truststore configured with the appropriate certificates.

*Truststore File Path:*
Specify the name and path of the truststore file containing the trusted certificates used when the remote server is configured to provide server authentication. For example, c:\security\truststore. Leave this field empty when server authentication is not used.

*Proxy Host and Port:*
When an HTTP proxy is used, specify the host address and the host port. For example, 192.10.1.3:18180. Otherwise, leave the field blank.

*Set Proxy Authentication Parameters:*
Select Show to display the proxy authentication parameters:

* *Proxy User ID:*
  Specify the user name for authentication. Leave the field blank for anonymous authentication.
* *Proxy User Password:*
  Specify the password for the user.

*Use Custom Application Schema:*
To use a custom schema with the driver, select Yes. By default, the value is set to No, which allows Identity Manager to load the default schema with the driver.

* *Custom Schema File Path:*
  To use a custom schema file, provide the local directory path where the entire schema file exists. For the driver to use the new schema, restart the driver.

### Publisher Options

*Publisher Heartbeat interval:*
Specify the heartbeat interval in seconds.

Leave this field empty to turn off the heartbeat.

## A.1.6 ECMA Script

The ECMAScript section enables you to add ECMAScript resource files. The resources extend the driver’s functionality when Identity Manager starts the driver.

## A.1.7 Global Configuration

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
