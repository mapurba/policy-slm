# A.1 Driver Configuration

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select click Properties > Driver Configuration.

In Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.

The following sections describe driver configuration in details:

* [Driver Module](identity-manager-sap-portal-driver-configuration.html#identity-manager-sap-portal-driver-module)
* [Driver Object Password](identity-manager-sap-portal-driver-configuration.html#identity-manager-sap-portal-driver-password)
* [Authentication](identity-manager-sap-portal-driver-configuration.html#identity-manager-sap-portal-driver-authentication)
* [Startup Options](identity-manager-sap-portal-driver-configuration.html#identity-manager-sap-portal-driver-startup-options)
* [Driver Parameters](identity-manager-sap-portal-driver-configuration.html#identity-manager-sap-portal-driver-parameters)
* [ECMAScript](identity-manager-sap-portal-driver-configuration.html#using-ecmascript-with-identity-manager-sap-portal-driver)
* [Global Configurations](identity-manager-sap-portal-driver-configuration.html#using-global-configuration-objects-with-identity-manager-sap-portal-driver)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The name of the Java class is: com.novell.nds.dirxml.driver.sap.portal.SAPPortalShim

*Native:*
This option is not used with the SAP Portal driver.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two suboptions:

* *Driver Object Password:*
  Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.
* *Include in documentation:*
  Includes information on the Remote Loader client configuration when Designer generates documentation for the SAP Portal driver.

## A.1.2 Driver Object Password

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The authentication options store the information required to authenticate to the connected system.

*Authentication ID:*
This field is not used for the SAP Portal driver. The authentication field is in the Subscriber settings documented in the [URL of remote SPML Provisioning Service Point:](identity-manager-sap-portal-driver-configuration.html#bsa1jis).

*Authentication Context:*
This field is not used for the SAP Portal driver.

*Remote Loader Connection Parameters:*
Used only if the driver is connecting to the application through the Remote Loader. The parameter to enter is hostname=xxx.xxx.xxx.xxx port=xxxx kmo=certificatename, when the host name is the IP address of the application server running the Remote Loader server and the port is the port the Remote Loader is listening on. The default port for the Remote Loader is 8090.

The kmo entry is optional. It is only used when there is an SSL connection between the Remote Loader and the Identity Manager engine.

Example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If this option is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer.

*Application Password:*
Specify the password for the user object listed in the Authentication ID field.

*Remote Loader Password:*
Used only if the driver is connecting to the application through the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the connected system.

## A.1.4 Startup Options

The Startup options allow you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

*Do not automatically synchronize the driver:*
This option only applies if the driver is deployed and was previously disabled. If this option is not selected, the driver re-synchronizes the next time it is started.

## A.1.5 Driver Parameters

The driver parameters let you tune driver behavior to align with your network environment.

The parameters are presented by category:

### Driver Settings

*XML element handling specific for Identity Manager (<nds>, <input>, <output>):*
Enables the Identity Manager engine to handle XML elements.

* *Remove/add elements:*
  Enables the driver shim to remove and add the required XML elements of <nds>, <input>, and <output>. These required elements are removed from the XML documents sent to the application and the elements are added to the XML documents received from the application before presenting the document to the Identity Manager engine.
* *Pass elements through:*
  Turns off XML element handling.

*Custom Java Extensions:*
Enables custom Java extensions to extend the driver shim’s functionality. Select Show to enable the custom Java extensions. Select Hide if you don’t have any custom Java extensions.

### Subscriber Settings

*Portal Authentication Information:*
Fill in the following fields for the SAP Portal authentication information:

* *URL of remote SPML Provisioning Service Point:*
  Specify the URL for the remote [SPML](identity-manager-sap-portal-driver-terminology.html#bjfkqvu) Provisioning Service Point (PSP). A PSP is a software component that listens for, processes, and returns the results for well-formed [SPML](identity-manager-sap-portal-driver-terminology.html#bjfkqvu) requests.

  For example: http://my.sap.com:50000/spml/spmlservice
* *Authentication ID:*
  Specify the authentication ID for the remote [SPML](identity-manager-sap-portal-driver-terminology.html#bjfkqvu) Provisioning Service Point.
* *Authentication Password:*
  Specify the password for the authentication ID.

*Show Advanced Options:*
Select Show to display the advanced configuration options for the SAP Portal driver.

*Truststore file:*
When the remote server is configured to provide server authentication, this is the path and the name of the keystore file which contains trusted certificates.

For example: c:\security\trustore

Leave this field blank when server authentication is not used.

*Set mutual authentication parameters:*
Select Show if you want to set mutual authentication information.

* *Keystore file:*
  Specify the path and name of the keystore file, if the remote server is configured to provide mutual authentication. For example: c:\security\keystore. Leave this field blank when mutual authentication is not used.
* *Keystore password:*
  Specify the keystore file password, if the remote server is configured to provide mutual authentication. Leave this field blank when mutual authentication is not used.

*Proxy host and port:*
When a proxy host and port are used, specify the host address and the host port. Choose an unused port number on your server. Otherwise, leave this field blank.

For example: 192.10.1.3:8180

*Handle HTTP session cookies:*
Some HTTP applications set cookies and expect them to be present on future requests. Select Handle Cookies if you want the driver to keep track of session cookies. Cookies are only kept until the driver is stopped.

*Process empty subscriber documents:*
Select whether or not the Subscriber channel should send empty documents to the target application. Documents could be empty if policies or style sheets strip the XML without vetoing the command. Select Ignore to block empty documents from being sent to the target application.

*HTTP errors to retry:*
List the HTTP error codes that should return a retry status. Must be a list of integers separated by spaces.

*Customize HTTP Request-Header Fields:*
Select Show if you want to set mutual authentication information. Use the following fields to define the custom HTTP request-header:

* *Authorization:*
  Select Use to add the Authentication ID and the password from the Authentication section into this request-header field.

  + *Key:*
    Specify Authorization as the keyword for the HTTP request-header field.
  + *Value:*
    Specify the value to associate with the keyword in an HTTP request-header field.
* *Context Type:*
  Select Use to add the media type to the HTTP request-header field to comply with RFC 2376.

  + *Key:*
    Specify Content-Type to set an HTTP request-header field.
  + *Value:*
    Specify text/xml; charset=uf-8 as the value of the keyword in the HTTP request-header field.
* *SOAPAction:*
  Select Use to enable the SOAPAction HTTP request header field to indicate the intent of the SOAP HTTP request.

  + *Key:*
    Specify SOAPAction to set an HTTP request-header field.
  + *Value:*
    Specify #batchRequest as the value of the HTTP request-header.

*Optional Request-Header:*
When required, specify an additional request-header that is unique to your situation.

### Publisher Settings

*Heartbeat interval in minutes:*
Specify the heartbeat interval in minutes. Leave this field blank to turn off the heartbeat.

## A.1.6 ECMAScript

Displays an ordered list of ECMAScript resource files. The files contain extension functions for the driver that Identity Manager loads when the driver starts. You can add additional files, remove existing files, or change the order the files are executed.

## A.1.7 Global Configurations

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
