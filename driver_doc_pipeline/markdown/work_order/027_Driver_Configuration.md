# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon or line, then select click Properties > Driver Configuration.

The Driver Configuration options are divided into the following sections:

* [Driver Module](driver-configuration.html#bs8i6bn)
* [Driver Object Password (Identity Console Only)](driver-configuration.html#b4jzp0o)
* [Authentication](driver-configuration.html#b4jzr84)
* [Startup Options](driver-configuration.html#bs8h5mh)
* [Driver Parameters](driver-configuration.html#b4m4h9a)
* [ECMAScript](driver-configuration.html#bffyqez)
* [Global Configuration](driver-configuration.html#brv2k2v)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The java class name is:

com.novell.nds.dirxml.driver.workorder.WorkOrderDriverShim

*Native:*
This option is not used with the WorkOrder driver.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two suboptions:

* Remote Loader Client Configuration for Documentation: Includes information on the Remote Loader client configuration when Designer generates documentation for the driver.
* Driver Object Password: Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

## A.1.2 Driver Object Password (Identity Console Only)

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The authentication section stores the information required to authenticate to the connected system.

*Authentication ID:*
Specify a user application ID. This ID is used to pass Identity Vault subscription information to the application.

Example: Administrator

*Authentication Context:*
Specify the IP address or name of the server the application shim should communicate with.

*Remote Loader Connection Parameters:*
Used only if the driver is connecting to the application through the Remote Loader. The parameter to enter is hostname=xxx.xxx.xxx.xxx port=xxxx kmo=certificatename, when the host name is the IP address of the application server running the Remote Loader server and the port is the port the Remote Loader is listening on. The default port for the Remote Loader is 8090.

The kmo entry is optional. It is only used when there is an SSL connection between the Remote Loader and the Identity Manager engine.

Example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Application Password:*
Specify the password for the user object listed in the Authentication ID field.

*Remote Loader Password:*
Used only if the driver is connecting to the application through the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the connected system.

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited.

Click Unlimited to set the file size to unlimited in Designer.

## A.1.4 Startup Options

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

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment. For example, you might find the polling interval to be shorter than you need. Making the interval longer could improve network performance while still maintaining your performance expectations for work order processing.

*Driver Name:*
The actual name you want to use for the driver.

*WorkOrders Container:*
The name of the container where WorkOrder objects and WorkToDo objects are to be stored.

*Poll Interval:*
How often the Publisher channel polls the WorkOrder container for work orders to be configured. The default is one minute. You can use this setting, not use this setting, or use it with the Poll Time setting. If you don’t want to use this setting, leave the field empty.

*Poll Time:*
Time of day the Publisher channel checks the WorkOrder container for work orders to be configured. By default, this setting is disabled (No poll time) so that only the Poll Interval setting is used. However, you can use this setting instead of the Poll Interval setting, or you can use it with the Poll Interval setting.

The poll times are available in half-hour increments. If you need a more granular poll time (for example, 1:15 PM rather than 1:00 PM or 1:30 PM), click the Edit XML button, locate the <definition display-name="Poll Time" id="112" name="polling-time" type="enum"> entry, and change the type from enum to string. Click OK to save the change, then enter the desired time in the Poll Time field. Use the HH:MM AM/PM format (for example, 1:15 PM).

*Publisher Heartbeat every Poll Interval:*
Specifies if the Publisher should emit heartbeat documents. The driver emits heartbeat documents to indicate to the Identity Manager engine that the driver is still functioning.

If you don’t use the Poll Interval setting, this setting is automatically disabled.

## A.1.6 ECMAScript

Enables you to add ECMAScript resource files. The resources extend the driver’s functionality when Identity Manager starts the driver.

## A.1.7 Global Configuration

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
