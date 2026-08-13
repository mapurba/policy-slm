# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon or line, then select click Properties > Driver Configuration.

The following sections describe driver configuration in details:

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The Java class name is:

com.novell.nds.dirxml.driver.salesforce.SFDriverShim

*Native:*
This option is not used with the Salesforce.com driver.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two suboptions:

* *Driver Object Password:*
  Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.
* *Remote Loader Client Configuration for Documentation:*
  Includes information on the Remote Loader client configuration when Designer generates documentation for the driver.

## A.1.2 Driver Object Password

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The authentication section stores the information required to authenticate to the connected system.

*Authentication ID:*
This option is not used with the Salesforce.com driver.

*Authentication Context:*
This option is not used with the Salesforce.com driver.

*Remote Loader Connection Parameters:*
Used only if the driver is connecting to the application through the Remote Loader. The parameter to enter is hostname=xxx.xxx.xxx.xxx port=xxxx kmo=certificatename, when the host name is the IP address of the application server running the Remote Loader server and the port is the port the Remote Loader is listening on. The default port for the Remote Loader is 8090.

The kmo entry is optional. It is only used when there is an SSL connection between the Remote Loader and the Identity Manager engine.

Example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer.

*Application Password:*
This option is not used with the Salesforce.com driver.

*Remote Loader Password:*
Used only if the driver is connecting to the application through the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the connected system.

## A.1.4 Startup Option

The Startup Option section allows you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

*Do not automatically synchronize the driver:*
This option only applies if the driver is deployed and was previously disabled. If this is not selected, the driver re-synchronizes the next time it is started.

## A.1.5 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment. The parameters are divided into the following categories:

### Driver Settings

*Salesforce.com Login URL:*
Specify the URL of the Salesforce.com Login Server based on your choice of Salesforce.com WSDL.

The default URL is https://www.salesforce.com/services/Soap/u/21.0.

*NOTE:*The minimum SOAP API version supported by Salesforce.com is 21.0.

*Salesforce.com Login ID:*
Specify the Login ID of the Salesforce.com administrator.

Ensure that you create a unique administrator user to be solely used by the Salesforce.com driver for authentication and specify that user in this parameter. If you specify the same user with which you login and administer Salesforce.com, the driver ignores changes on the Publisher channel (loopback detection).

*Salesforce.com Login Password:*
Specify the password for the Salesforce.com administrator.

If you need to clear the password, select Remove existing password, then click Apply.

*Salesforce.com Security Token:*
Specify the security token for your login account at Salesforce.com.

*Proxy host and port:*
When an HTTP proxy is used, specify the host address and the host port. For example: 192.10.1.3:18180.

*Set Proxy Authentication parameters:*
Select Show to display the proxy authentication parameters.

* *Proxy User ID:*
  Specify the username of the proxy user for authentication. Leave the field blank for anonymous authentication.
* *Proxy User Password:*
  Specify the password of the proxy user, if proxy user authentication is used.

*Truststore File:*
Specify the name and path of the keystore file containing the trusted certificates used when the remote server is configured to provide server authentication. For example: c:\security\truststore. Leave this field empty when server authentication is not used.

*NOTE:*A Salesforce.com client calling the Web service in the Publisher channel must specify a URL ending with a slash. For example, http://1.1.1.1:9095/. Without a context path (the slash), the driver does not process the request received.

### Publisher Settings

*Publisher Channel Enabled:*
Select Enable to enable the Publisher connection. The following options are displayed to configure the Publisher channel.

* *Poll Interval (seconds):*
  Specify how often the Publisher channel polls for the unprocessed IDs. The default value is 60 seconds.
* *Publisher Heartbeat Interval:*
  Specifies how often, in minutes, the driver shim contacts the Identity Manager engine when there has not been any traffic during the interval time. The default value is 1 minute. Specify 0 to disable the heartbeat.
