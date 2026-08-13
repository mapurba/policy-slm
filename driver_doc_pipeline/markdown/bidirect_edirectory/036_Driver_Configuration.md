# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler, then right-click the driver line and click Properties > Driver Configuration.

The Driver Configuration options are divided into the following sections:

* [Driver Module](driver-configuration.html#b957pzn)
* [Driver Object Password](driver-configuration.html#b957q01)
* [Authentication](driver-configuration.html#b957q0c)
* [Startup Option](driver-configuration.html#b957q0t)
* [Driver Parameters](driver-configuration.html#b957q17)
* [ECMAScript](driver-configuration.html#b957q21)
* [Global Configurations](driver-configuration.html#brndxwr)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally. By default, the Java class name is com.novell.nds.dirxml.driver.edir.EDIRDriverShim. The class path is case-sensitive.

*Native:*
This option is not used with the Bidirectional eDirectory driver.

*Connect to Remote Loader:*
The Remote Loader is not used with the Bidirectional eDirectory driver.

## A.1.2 Driver Object Password

This option is not used with the Bidirectional eDirectory driver.

## A.1.3 Authentication

The Authentication section stores the information required to authenticate to the connected system. For the Bidirectional eDirectory driver, it stores the information required to authenticate to the eDirectory server that the driver is associated with.

*Authentication ID:*
Specify the DN of the LDAP account that the driver will use to authenticate to connected eDirectory. For information, see [Section 6.0, Configuring SSL Connections](configuring-ssl-connections.html).

*Connection Context:*
Specify the hostname or IP address of the eDirectory server as well as the decimal port number (for example, 187.168.1.1:389).

Port 389 uses the TLS protocol for a clear text connection, and port 636 uses the SSL protocol. For more information, see [Section 6.0, Configuring SSL Connections](configuring-ssl-connections.html).

*Remote Loader Connection Parameters:*
The Bidirectional eDirectory driver does not support the use of the Remote Loader for a local driver. These options do not apply.

*Driver Cache Limit (KB):*
Specify the maximum event cache file size (in KB). If the value is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer.

*Application Password:*
Specify the password for the user object listed in the Authentication ID option.

For more information, see [Section 6.0, Configuring SSL Connections](configuring-ssl-connections.html).

*Remote Loader Password:*
This option is not used with the Bidirectional eDirectory driver.

## A.1.4 Startup Option

The Startup Option section enables you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

If the driver is Disabled and then changed to Auto start or Manual, you can select the Do Not Automatically Synchronize the Driver check box. This prevents the driver from synchronizing objects automatically when it loads. To synchronize objects manually, use the Synchronize button on the Driver Overview page.

## A.1.5 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment.

The parameters are divided into the following categories:

* [Driver Settings](driver-configuration.html#bsdm0xp)
* [Subscriber Settings](driver-configuration.html#bsdm15u)
* [Publisher Settings](driver-configuration.html#bsdm2v6)

### Driver Settings

*Use SSL:*
Select Yes to use SSL to secure communication between the Bidirectional eDirectory driver and the eDirectory server. If you use SSL, fill in the following parameters:

* *Always Accept Server Certificate:*
  Select Yes if you want the driver to accept the LDAP server's certificate for establishing SSL connection with the eDirectory server. To use the keystore, select this option to No. For more information on setting up SSL connections, see [Section 6.0, Configuring SSL Connections](configuring-ssl-connections.html).
* *Keystore Path for SSL Certificates:*
  Specify the full path to the keystore file containing the SSL certificates.
* *Use Mutual Authentication:*
  Select Yes if you want the driver to use SSL mutual authentication (both client and server), or select No for server authentication only. If you select Yes, you must have the appropriate certificates configured in your keystore.
* *Key Alias:*
  Specify the alias of the key.
* *Keystore Password:*
  Specify the password for accessing the keystore file containing the SSL certificates.
* *Reenter Keystore Password:*
  Specify the password again.
* *Remove Existing Password:*
  Enable this option if you do not want to specify the keystore password. If you select this option, the Keystore Password option is automatically disabled.

*Password Sync Type:*
Specifies which password sync type to use. By default, this option is set to Sync UP password. To sync NDS password, select Sync NDS password option and enable the public/private key pair in the driver filter for both Publisher and Subscriber channels.

*User Container:*
Specifies the container where the users are added if they don’t already exist in the Identity Vault. This value becomes the default value for all drivers in the driver set. It is in slash format, such as netiq/users, where ou=users.o=netiq.

### Subscriber Settings

*Show Default Configuration:*
This option applies to the connected eDirectory server. Select Show to display the following option:

* *eDirectory Port Number:*
  Specify the port number of the connected eDirectory server. This port number is used for creating home directories. The default value is 524. For more information, see [Creating Home Directories](creating-home-directories.html).

  The Identity Vault hosting the bi-directional eDirectory driver should be able to communicate using port 524, with the server specified for the Connection Context. However, if the volume containing the home directory resides on a different server, NCP communication using the same port is possible between the Identity Vault and this server.

### Publisher Settings

*Show Default Configuration:*
This option applies to the connected eDirectory server. Select Show to display the following options:

* *eDirectory Base Container:*
  Specifies the connected eDirectory container in LDAP format where objects are synchronized. If you are using a flat Placement rule, this is the container where the objects are placed. If you are using a mirrored Placement rule, this is the base container. For example, ou=people,o=com.
* *Polling Interval in Seconds:*
  Specifies the number of seconds that the Publisher channel waits after running the polling script and sending eDirectory events from the change-log to the Identity Manager engine.
* *Heartbeat Interval in Minutes:*
  Specifies how often, in minutes, the driver shim contacts the Identity Manager engine when there has not been any traffic during the interval time. Specify 0 to disable the heartbeat.
* *Keep Alive Interval in Minutes:*
  Specifies how often, in minutes, the driver shim re-initializes an idle change-log connection in order to keep the connection alive between the bidirectional eDirectory shim and the change-log. The default value is 30 minutes. The minimum duration is 1 minute. Setting the interval as 0 or lesser will disable this option.

  *NOTE:*It is highly recommended to specify the interval to more than 5 minutes. After the set interval duration, the shim will re-initialize the connection and re-register with the change-log module. Lesser interval results in more re-initialization and re-registration activity and consequently additional cpu cycles.
* *Allow Loop-back Detection:*
  When this option is set to True, the driver avoids event loopback. However, the passwords still loopback into the Publisher channel since passwords are always modified by the server object. When the option is set to False, the Subscriber channel events might loop into the Publisher channel.

  The default behavior of the Publisher channel is to avoid sending changes that the Subscriber channel makes. The Publisher channel detects Subscriber channel changes by looking at the creatorsName or modifiersName attribute to see whether the authenticated entry that made the change is the same entry that the driver uses to authenticate to the eDirectory server. If the entry is the same, the Publisher channel assumes that this change was made by the driver’s Subscriber channel and does not synchronize the change.

*Show Change-log Plug-in Configuration:*
This setting applies to the configuration of the change-log plug-in. Select Show to display the following options:

* *Maximum Days without Reconnect:*
  Specify the number of days after which driver change cache and registration information is deleted if the driver does not connect. The default value is 30.
* *Ignore Processing Errors:*
  Specify if the change-log should ignore any error codes that it receives during SendChangesResponse operation. If the value is set to true, the errors are ignored and the next event is processed. By default, the value is set to false, which means the same event might be resent.
* *Allow Password on Clear-text Connection:*
  By default, the value is false, which means that the password is sent over a secure channel. You can change the value to true to send the password in clear text, but this is not a recommended setting.
* *Change-log Trace Level*
  : Specify the change-log trace level. There are three trace levels: ERROR, INFO, and DEBUG. Detailed messages are logged if you select INFO. DEBUG logs debugging data along with detailed messages. The default trace level is ERROR.

  To view the change-log trace on the remote eDirectory server, enable the DVRS and DXML flags of the DSTrace utility.
* *Change-log Prefered Maximum Batch-size:*
  Specify the maximum number of events that the change-log module sends in a batch between a range of 1 to 500.

## A.1.6 ECMAScript

The ECMAScript section enables you to add ECMAScript resource files. The resources extend the driver’s functionality when Identity Manager starts the driver.

## A.1.7 Global Configurations

The Global Configurations section displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
