# O.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon or line, then select click Properties > Driver Configuration.

The following sections describe driver configuration in details:

* [Driver Module](how-to-configure-jdbc-driver.html#b4jzjxt)
* [Authentication](how-to-configure-jdbc-driver.html#b1hdlhxt)
* [Startup Option](how-to-configure-jdbc-driver.html#b4m4gci)
* [Driver Parameters](how-to-configure-jdbc-driver.html#b4m4h9a)
* [ECMAScript](how-to-configure-jdbc-driver.html#brv2j9u)
* [Global Configuration](how-to-configure-jdbc-driver.html#brv2k2v)

## O.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Use this option to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally. Select this option to run the driver locally.

The Java class name is: com.netiq.idm.driver.fanoutshim.FanoutDriverShim.

*Native:*
This option is not used with the REST driver.

*Connect to Remote Loader:*
This option is not used for JDBC Fan-out driver. Used when the driver is connecting remotely to the connected system.

*Name:*
Displays the Java class name.

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Fan-out Agent, you must enter a password on this page. This password is used by the Fan-out Agent to authenticate itself to the driver shim.

## O.1.2 Authentication

The authentication section describes the parameters required for authentication to the connected database.

*Authentication ID:*
Specify a user application ID. This ID is used to pass Identity Vault subscription information to the application. For example, Administrator.

*Connection Information (Designer only):*
Specify the IP address or name of the server the application shim should communicate with.

*IMPORTANT:*The Remote Loader options are not applicable for the JDBC Fan-out drivers. The Fan-out drivers use the Fan-out Agent component to create multiple database instances.

*Driver Cache Limit (kilobytes):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. select Unlimited option to set the file size to unlimited in Designer.

*Application Password:*
Use the Set Password option to set the application authentication password.

*Remote loader password:*
Use this option to update the remote loader password. This option is not used for the JDBC Fan-out driver.

## O.1.3 Startup Option

The Startup Option section allows you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

## O.1.4 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment.

The parameters are presented by category:

* [Driver Settings](how-to-configure-jdbc-driver.html#bs4c7yk)
* [Normal JDBC Driver Settings](how-to-configure-jdbc-driver.html#b1i8d8uk)
* [Subscriber Settings](how-to-configure-jdbc-driver.html#b1i8dayd)
* [Publisher Settings](how-to-configure-jdbc-driver.html#b1i8daye)

### Driver Settings

*Fanout transport related parameters:*
Select Show to view the transport related parameters for Fan-out drivers.

*Show Subscriber Event Queue parameters:*
Select Show to view the subscriber event parameters. The options are:

* SEND: The queue for sending the subscriber events to the Fan-out Agent.
* RECV: The subscriber event receiving queue for receiving the subscriber events from Fan-out Agent.
* DELAYED RECV: The subscriber delayed event receiving queue is used for receiving the delayed subscriber events from FanOut Agent.

*Show Configuration Queue Parameters:*
Select Show to view the configuration queue parameters. The options are SEND and RECV.

*Show Query-in Queue Parameters:*
Select Show to view the query-in queue parameters. The options are SEND and RECV.

*Show Query-out Queue Parameters:*
Select Show to view the query-out queue parameters. The options are SEND and RECV.

*Show Other Parameters:*
Select Show to view the additional parameters.

* Configuration batch size: Specify the batch size for the Driver configuration document. The value is from 1 - 99999.

*Show Fanout Parameters:*
Select Show to view the fan-out connection related information such as Fan-out Agent password, configuration information, Fan-out Agent shim password.

* Fanout Shim Password: Specify the password for the fan-out driver shim. After successful authentication, the FanOut Agent loads/creates the driver instances of the specified shim class name.
* Fanout Agent Password: Specify the password of Fan-out Agent you are connecting to. The Fan-out Agent establishes connection only after a valid authentication.
* Encryption Key: Specify the key to encrypt/decrypt the sensitive data before sending to the message queue(s).
* AMQ Keystore Key: Specify the full path to the keystore file.
* AMQ Keystore Password: Specify the keystore password.
* AMQ Truststore Path for SSL Certs: Specify the full path to the truststore file.
* AMQ Truststore Password: Specify the truststore.
* Fanout Shim classname: Specify shim classname that the Fan-out Agent loads when you start the any fan-out driver.
* Matching Attributes: Matching attributes that Fan-out Agent uses to match objects in delayed add events. Attribute names must be as per the schema of the connected system. NetIq recommends that these attributes must be schema-mapped equivalent of the attributes that are used in the object matching policy.

### Normal JDBC Driver Settings

For the normal JDBC driver setting, see [Driver Parameters](configure-jdbc-driver-specific-parameters.html).

### Subscriber Settings

*Disable Subscriber:*
Select no (default) to allow flow of events from Identity Manager engine to the connected database.

*Show primary key parameters:*
Select Show if you want to configure the primary key parameters.

* *Generation/retrieval method (table-global):*
  Select the desired option to generate/retrieve the primary key values. This setting is global for all tables and views. The options are as follows:

  + subscription event (default)
  + subscriber-generated
  + auto-generated / identity column
* *Retrieval timing (table-global):*
  Select the desired option to retrieve the primary key value. This setting is global for all tables and views. The options are:

  + before row insertion (default)
  + after row insertion
* *Method and timing (table-global):*
  Specify how and when the primary key values are generated or retrieved on a per table or view basis. This parameter overrides global method and timing settings. Use semicolon, comma, or space as the delimiter for multiple values. For example: usr("?=indirect.proc\_idu()"); grp("indirect.proc\_idg(idg)").

*Disable statement-level locking:*
Select the appropriate option to disable statement locking. This option determines if explicit locking or database resources are disabled on the Subscriber channel. The value is set to no (default) by default.

*Check update counts:*
Select yes (default) to enable the Subscriber channel to check for any updates after any of the insert, update, or delete statements are executed against the tables. This option ensures that the statements are resulting in updating the database. The value is set to yes (default) by default.

### Publisher Settings

*Disable the Publisher Channel:*
Select yes (default) to ignore the flow of events from the connected database to Identity Manager engine. The Fan-out driver implementation do not support the Publisher channel. By default, this option is disabled for the Fan-out driver configuration.

*Heartbeat interval (in minutes):*
Specify the interval in minutes that the Publisher remain inactive before sending a heartbeat document.

## O.1.5 ECMAScript

Displays an ordered list of ECMAScript resource files. The files contain extension functions for the driver that Identity Manager loads when the driver starts. You can add additional files, remove existing files, or change the order the files are executed.

## O.1.6 Global Configuration

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
