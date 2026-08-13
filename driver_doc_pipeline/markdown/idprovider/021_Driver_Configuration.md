# A.1 Driver Configuration

In Identity Console:

1. Click the Identity Manager Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![Driver icon](../graphics/driver_icon_n.png "Driver icon") or line, then select click Properties > Driver Configuration.

The Driver Configuration options are divided into the following sections:

* [Driver Module](id-provider-driver-configuration.html#b4jzjxt)
* [Driver Object Password](id-provider-driver-configuration.html#b4jzp0o)
* [Authentication](id-provider-driver-configuration.html#b4jzr84)
* [Startup Option](id-provider-driver-configuration.html#b4m4gci)
* [Driver Parameters](id-provider-driver-configuration.html#b4m4h9a)
* [ECMAScript](id-provider-driver-configuration.html#bffyqez)
* [Global Configurations](id-provider-driver-configuration.html#brndxwr)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The name of the Java class is: com.novell.idm.dirxml.driver.idprovider.IDProviderShim

*Connect to the Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two suboptions:

* *Remote Loader Client Configuration for Documentation:*
  Includes information on the Remote Loader client configuration when Designer generates documentation for the ID Provider driver.
* *Driver Object Password:*
  Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

## A.1.2 Driver Object Password

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The authentication section stores the information required to authenticate to the connected system.

*Authentication ID:*
Specify a user application ID. This ID is used to pass Identity Vault subscription information to the application. For example, Administrator.

*Authentication Context:*
Specify the IP address or name of the server the application shim should communicate with.

*Remote Loader Connection Parameters:*
Used only if the driver is connecting to the application through the Remote Loader. The parameter to enter is hostname=xxx.xxx.xxx.xxx port=xxxx kmo=certificatename, when the hostname is the IP address of the application server running the Remote Loader server and the port is the port the remote loader is listening on. The default port for the Remote Loader is 8090.

The kmo entry is optional. It is only used when there is an SSL connection between the Remote Loader and the Identity Manager engine.

Example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Application Password:*
Specify the password for the user object listed in the Authentication ID field.

*Remote Loader Password:*
Used only if the driver is connecting to the application through the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the connected system.

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer.

## A.1.4 Startup Option

The startup options allow you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

*Do not automatically synchronize the driver:*
This option only applies if the driver is deployed and was previously disabled. If this is not selected, the driver re-synchronizes the next time it is started.

## A.1.5 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment. The driver parameters are divided into categories:

* [ID Policy Repository](id-provider-driver-configuration.html#bs0rre7)
* [Client Options](id-provider-driver-configuration.html#bs0rshm)
* [Server Options](id-provider-driver-configuration.html#bs0rxjs)

### ID Policy Repository

*LDAP server:*
The IP address or DNS name of the LDAP server that contains the ID policies.

*LDAP port:*
The TCP port of the LDAP server. The default port is 389 for a non-SSL connection and 636 for an SSL connection.

*Use SSL:*
Select True to use an SSL/TLS connection to the LDAP server.

*Always trust:*
If this options is set to True, the ID Provider driver trusts all LDAP servers even if their certificates are untrusted.

*Policy Container DN:*
Specify the DN of the policy container in your Identity Vault.

### Client Options

*Client name:*
The name the driver uses when it acts as an ID client and requests an ID from the provider. This is useful for tracing, and if access control is enabled on any of the ID policies. If access control is enabled, the ID client names that obtain an ID from the policy are specified. If the client name associated with the request is not in the list, the provider does not issue an ID.

*ID Generation Map:*
Specify a comma-separated list of attribute=policy pairs. For example: workforceID=wfid,uniqueID=uid.

This example configures the driver to request IDs from the wfid policy and store them in the workforceID attribute whenever a new object is created or when someone tries to change this attribute. IDs from the uid policy are used for the uniqueID attribute. The driver only issues IDs from an attribute if that attribute and the object class holding the attribute are in the Subscriber channel and the Publisher channel of the filter and are set to synchronize.

*NOTE:*Attribute names must be in the Identity Manager namespace (not LDAP) and must be case-exact.

### Server Options

*Start RMI?:*
Controls whether the ID Provider starts an RMI service or not. An RMI service is needed if you request IDs from other clients than the driver for example, from DirXML Script policies or style sheets. If all IDs are managed through this driver’s filter and ID Generation Map settings, no RMI service is needed.

*RMI server:*
The IP address of the RMI server. Leave this field blank for the server to bind to all available addresses.

*RMI port:*
The TCP port of the RMI service. The default port for RMI is 1099. If that port is in use, change to a different port that is lower than 1024. If the port is in conflict, you see errors in the trace when the driver starts. The configuration assumes a port of 1099 to avoid common port conflicts.

*RMI Service port:*
The TCP port for the RMI ID Provider service. The server uses an ephemeral port if the value of this parameter is zero.

*RMI ID Provider Service IP:*
The IP address of the server where the ID Provider service is available. This parameter is useful in NAT environments where ID Provider service has to be on a specific network interface. The IP address of the server where the client can access the ID Provider Service. In a NAT environment, this is the public IP address through which the clients can connect to the Identity Vault server.

*Use legacy ID Server schema:*
Enables a backward-compatibility mode when migrating an existing ID server configuration to run with the new ID Provider shim. True allows you to use legacy ID policies which do not use the schema that ships with the ID Provider driver.

*Trace level:*
Select On to enable the ID Provider trace level, not the driver trace level.

## A.1.6 ECMAScript

Enables you to add ECMAScript resource files. The resources extend the driver’s functionality when Identity Manager starts the driver.

## A.1.7 Global Configurations

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
