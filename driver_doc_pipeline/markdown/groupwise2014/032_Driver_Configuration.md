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
* [Driver Object Password](driver-configuration.html#b4jzp0o)
* [Authentication](driver-configuration.html#b4jzr84)
* [Startup Option](driver-configuration.html#b4m4gci)
* [Driver Parameters](driver-configuration.html#b4m4h9a)
* [ECMAScript](driver-configuration.html#bryoobc)
* [Global Configurations](driver-configuration.html#bryooej)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The name of the driver’s Java class is com.novell.gw.dirxml.driver.rest.shim.GWdriverShim

*Native:*
This option is not used with the GroupWise driver.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two suboptions:

* *Remote Loader Client Configuration for Documentation:*
  Includes information on the Remote Loader client configuration when Designer generates documentation for the driver.
* *Driver Object Password:*
  Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

## A.1.2 Driver Object Password

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The authentication section stores the information required to authenticate to the connected system.

*Authentication ID:*
Specifies the user ID used to authenticate to the GroupWise system. By default, this is the GroupWise Administrator user.

*Connection Information:*
Specifies the IP address and the decimal port number (for example, IP Address:port) to connect to GroupWise. By default, it runs on port 9710 (Administration Service port). The Administration Service running on the GroupWise primary domain is used as the connection address in the driver configuration.

*Remote Loader Connection Parameters:*
Used when the driver is connecting remotely to the connected system. The parameter to enter is hostname=xxx.xxx.xxx.xxx port=xxxx kmo=certificatename, when the host name is the IP address of the Remote Loader server and the port is the port the Remote Loader is listening on. The default port for the Remote Loader is 8090.

The kmo entry is optional. It is only used when there is an SSL connection between the Remote Loader and the Identity Manager engine.

*Application Password:*
Specifies the admin user password to authenticate to GroupWise system.

*Remote Loader Password:*
Used only if the driver is using the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the connected system.

*Cache limit (KB):*
Specifies the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer.

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

The parameters are:

*GroupWise Domain Database Version:*
GroupWise REST is the version of the GroupWise domain database to which this driver should connect.

*Create Nicknames:*
Select True if you want the driver to create GroupWise nicknames when GroupWise accounts are renamed or moved to another post office.

*Reassign Resource Ownership:*
Select True if you want the driver to reassign ownership of resources when the GroupWise accounts are disabled or expired.

*Default Resource Owner User ID:*
Specifies the default user who becomes the new owner of resources that are reassigned.

*Cleanup Group Membership:*
Cleans up Identity Vault Group memberships when removing a user from all GroupWise Distribution Lists. Select True or False.

*Always accept server certificate:*
By default, this is set to No. To use the keystore, specify the values for the following parameters:

* *Keystore path for SSL certificates:*
  Specify the full path to the keystore file containing the SSL certificates.
* *Keystore Password:*
  Specify the password for accessing the keystore file containing the SSL certificates.
* *Reenter Keystore password:*
  Specify the password again to confirm it.

Select Yes if you want the driver to accept the GroupWise server's certificate for establishing SSL connection with the Identity Manager server. This avoids the need for manually maintaining a keystore. For more information on setting up SSL connections, See [Section 6.0, Securing Driver Communication](secure-driver-communication.html).

*Publisher Heartbeat Interval:*
Specifies the Publisher channel heartbeat interval in minutes. Specify 0 to disable the heartbeat.

## A.1.6 ECMAScript

Displays an ordered list of ECMAScript resource files. The files contain extension functions for the driver that Identity Manager loads when the driver starts. You can add additional files, remove existing files, or change the order the files are executed.

## A.1.7 Global Configurations

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
