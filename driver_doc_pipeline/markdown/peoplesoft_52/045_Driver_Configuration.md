# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon or line, then select click Properties > Driver Configuration.

The following sections describe driver configuration in details:

* [Driver Module](driver-properties-configuration.html#b4jzjxt)
* [Driver Object Password](driver-properties-configuration.html#b4jzp0o)
* [Authentication](driver-properties-configuration.html#bs8h5hj)
* [Startup Option](driver-properties-configuration.html#bs8h5mh)
* [Driver Parameters](driver-properties-configuration.html#b4m4h9a)
* [ECMAScript](driver-properties-configuration.html#brv2j9u)
* [Global Configuration](driver-properties-configuration.html#brv2k2v)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The java class name is:

com.novell.nds.dirxml.driver.psoftshim.PSOFTDriverShim

*Native:*
This option is not used with the PeopleSoft driver.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two suboptions:

* ![](../graphics/designer_logo_n.png) Remote Loader Client Configuration for Documentation: Includes information on the Remote Loader client configuration when Designer generates documentation for the driver.
* ![](../graphics/designer_logo_n.png) Driver Object Password: Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

## A.1.2 Driver Object Password

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The Authentication section stores the information required to authenticate to the connected system.

*Authentication ID:*
Specify a user application ID. This ID is used to pass Identity Vault subscription information to the application.

Example: PSAdmin

*Connection Information:*
Specify the IP address or name of the PeopleSoft server the driver should communicate with.

The connection string uses the following format:

<hostname or IP address>:<Port Number>

Example: //PSServer:9000

To enable failover and load balancing, you can supply multiple server connection strings separated by a comma.

*Application Password:*
Specify the password for the user object listed in the Authentication ID field.

*Remote Loader Authentication Parameters:*
Used only if the driver is connecting to the application through the Remote Loader. The parameter to enter is hostname=xxx.xxx.xxx.xxx port=xxxx kmo=certificatename, where the hostname is the IP address of the application server running the Remote Loader server and the port is the port the Remote Loader is listening on. The default port for the Remote Loader is 8090.

The kmo entry is optional. It is only used when there is an SSL connection between the Remote Loader and the Identity Manager engine.

Example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Remote Loader Password:*
Used only if the driver is connecting to the application through the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the connected system.

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited.

Click Unlimited to set the file size to unlimited in Designer.

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

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment.

The parameters are presented by category:

* [Driver Options](driver-properties-configuration.html#bs5eipr)
* [Subscriber Options](driver-properties-configuration.html#bs5eupr)
* [Publisher Options](driver-properties-configuration.html#bs5ew60)

### Driver Options

*Schema CI Name:*
Allows you to list the Data Schema Component interfaces that the driver synchronizes. Use the Plus icon to add an item, the Minus icon to delete an item, and the Pen icon to edit an item. The default is DIRXML\_SCHEMA01.

*Data Record ID Field:*
Specify the name of the data record definition that uniquely identifies a PeopleSoft object. The default is Assoc\_ID.

*Use Case-Sensitive Search:*
Controls whether the driver uses case-sensitive matching criteria while evaluating search attribute matches. The default is No Case-Sensitive Matching.

*Domain Connection Password:*
Controls enabling and disabling of domain connection password functionality. When this option is set to Enable on the PeopleSoft server, an unencrypted domain connection password is provided. By default, this option is set to Disable.

### Subscriber Options

*Allow Subscriber channel add events:*
Subscriber Add events are implemented by invoking the Component Interface Create method (if present). If you want the driver to allow Subscriber channel Add events, select Allow Subscriber add. The default is Disallow Subscriber add.

* *Data Record ID Field Default Value:*
  Specify a default value for the Schema CI key field. This parameter is used only for Subscriber channel Add events. The default is New.

*Allow Subscriber channel delete events:*
Subscriber Delete events are implemented by invoking the Component Interface Delete method (if present). If you want the driver to allow Subscriber channel Delete events, select Allow Subscriber delete. The default is Disallow Subscriber delete.

### Publisher Options

*Transaction CI Name:*
Specify the name of the PeopleSoft CI object that defines the set of fields required for the driver Transaction interface. The set of fields in the specified transaction CI must contain the same fields and keys that are identified in the default transaction CI in order for the driver to work. The default is DIRXML\_TRANS01.

*Driver Subset Identifier:*
Specify the value of the DIRXML\_DRIVER field in the transaction CI that identifies a subset of published transactions. This value is used for polling the transaction CI to retrieve relevant transactions from the PeopleSoft application.

*Publisher Polling Option:*
The PeopleSoft driver supports two options for Publisher Transaction record polling. To choose an interval of seconds between polls, select Utilize Interval Polling. To use a crontab format, select Utilize crontab Format Polling.

If you select Utilize Interval Polling, fill in the Queue Poll Interval by specifying the number of seconds between checks for available transactions to process. The default is 5.

If you select Utilize crontab Format Polling, fill in the Enter Queue Poll crontab Format String by specifying the polling interval in crontab format. The default value of \* \* \* \* \* generates a poll every minute.

* *Queue Poll Interval (seconds):*
  Specify the number of seconds between checks for available transactions to process.

*Publisher heartbeat interval:*
Specify how many minutes of inactivity can elapse before this channel sends a heartbeat document. In practice, more than the number of minutes specified can elapse. That is, this parameter defines a lower bound.

## A.1.6 ECMAScript

Displays an ordered list of ECMAScript resource files. The files contain extension functions for the driver that Identity Manager loads when the driver starts. You can add additional files, remove existing files, or change the order the files are executed.

## A.1.7 Global Configuration

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
