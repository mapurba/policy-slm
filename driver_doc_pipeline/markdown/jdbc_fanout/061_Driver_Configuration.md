# B.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver, then click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon or line, then select click Properties > Driver Configuration.

The following sections describe driver configuration in details:

## B.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Use this option to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally. Select this option to run the driver locally.

The Java class name is: com.netiq.idm.driver.fanoutshim.FanoutDriverShim.

*Native:*
This option is not used with the JDBC Fanout driver.

*Connect to Remote Loader:*
This option is not valid for this driver.

*Name:*
Displays the java class name.

*IMPORTANT:*Although Driver Object Password option is editable, this parameter is not applicable for the Fanout driver.

## B.1.2 Authentication

The authentication section describes the parameters required for authentication to the connected Active MQ.

*Connection Information (Designer only):*
Specify the IP address or name of the server the application shim should communicate with. Use the syntax: protocol://host:port. For example, tcp://192.99.162.46:61616

*Driver Cache Limit (kilobytes):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. select Unlimited option to set the file size to unlimited in Designer.

*IMPORTANT:*Although Application Authentication ID and Set Password options are editable, these parameters are not applicable for the Fanout driver.

The Remote Loader options do not apply to the Fanout driver. This driver uses the Fanout agent component to create multiple JDBC Fanout driver instances.

## B.1.3 Startup Option

The Startup Option section allows you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

## B.1.4 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment.

The parameters are presented by category:

### Driver Settings

*Fanout transport related parameters:*
Select Show to view the transport related parameters for Fanout driver.

*Show Subscriber Event Queue parameters:*
Select Show to view the Subscriber event parameters. The options are:

* *SEND:*
  The driver uses this queue for sending the Subscriber events to the Fanout agent.
* *RECV:*
  The driver uses this queue for receiving the Subscriber events from the Fanout agent.
* *DELAYED RECV:*
  This driver uses this queue for receiving the delayed Subscriber events from the Fanout agent.

*Show Configuration Queue Parameters:*
Select Show to view the configuration queue parameters. The options are SEND and RECV.

*Show Query-in Queue Parameters:*
Select Show to view the query-in queue parameters. The options are SEND and RECV.

*Show Query-out Queue Parameters:*
Select Show to view the query-out queue parameters. The options are SEND and RECV.

The Fanout agent creates queues for each connection instance. It uses these queues to send events to individual connection instances. These queues act as event caches (at Fanout agent level) for the connection instances.

*Show Other Parameters:*
Select Show to view the additional parameters.

* *Configuration batch size:*
  Specifies the batch size for the driver configuration document. The value ranges from 1 - 99999.
* *Show Fanout Parameters:*
  Select Show to view the Fanout connection related information such as Fanout agent password, configuration information, Fanout agent shim password.

* *Fanout Shim Password:*
  Specifies the password for the Fanout driver shim. After successful authentication, the Fanout agent loads/creates the driver instances of the specified shim class name.
* *Fanout Agent Password:*
  Specifies the password for the Fanout agent you are connecting to. The Fanout agent establishes connection only after a valid authentication.
* *Encryption Key:*
  Specifies the key to encrypt/decrypt the sensitive data before sending to the message queue(s).
* *AMQ Keystore Key:*
  Specifies the full path to the keystore file.
* *AMQ Keystore Password:*
  Specifies the keystore password.
* *AMQ Truststore Path for SSL Certs:*
  Specifies the full path to the truststore file.
* *AMQ Truststore Password:*
  Specifies the truststore password.
* *Secure Protocol Version:*
  Specifies the version of the TLS protocol that the driver uses to connect to the Identity Manager engine. Identity Manager supports TLSv1, TLSv1\_1, and TLSv1\_2.

  *NOTE:*This parameter is included in Fanout driver 1.1.
* *Enforce Suite B:*
  Specifies whether the driver uses Suite B for establishing communication with ActiveMQ. When Suite B is enabled, the communication is authenticated with Suite B cryptographic algorithms. This communication is supported only on TLS 1.2 protocol.

  *NOTE:*This parameter is included in Fanout driver 1.1.
* *Fanout Shim classname:*
  Specifies the driver shim classname that the Fanout agent loads when you start the a Fanout driver.
* *Matching Attributes:*
  Used by the Fanout agent to match the objects in the delayed add events. This parameter must be schema-mapped equivalent of the attributes that are used in the object matching policy. If you are using different attributes, specify the attribute names according to the connected system schema.

### Normal JDBC Driver Settings

For the normal JDBC driver setting, see [Driver Parameters](../../jdbc/data/how-to-configure-jdbc-driver.html#b4m4h9a) from the [JDBC Driver Guide](https://www.netiq.com/documentation/idm45drivers/jdbc/data/bookinfo.html).

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
Select the appropriate option to disable statement locking. This option determines if explicit locking or database resources are disabled on the Subscriber channel. The default value is set to no.

*Check update counts:*
Select yes to enable the Subscriber channel to check for any updates after any of the insert, update, or delete statements are executed against the tables. This option ensures that the statements are resulting in updating the database. The default value is set to yes.

*Query TimeOut (in minutes):*
Specify the time in minutes that the driver waits for a response from the Fanout agent when the driver issues a query to the agent. The default value is 1 minute.

## B.1.5 ECMA Script

Displays an ordered list of ECMAScript resource files. The files contain extension functions for the driver that Identity Manager loads when the driver starts. You can add additional files, remove existing files, or change the order the files are executed.

## B.1.6 Global Configuration

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
