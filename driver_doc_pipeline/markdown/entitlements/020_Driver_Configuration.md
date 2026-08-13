# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![List of Entitlement Policies](../graphics/driver_icon_n.png "List of Entitlement Policies") or line, then select click Properties > Driver Configuration.

The Driver Configuration options are divided into the following sections:

* [Driver Module](driver-configuration.html#b94psgk)
* [Driver Object Password (Identity Console Only)](driver-configuration.html#b94psgy)
* [Authentication](driver-configuration.html#b94psh9)
* [Startup Option](driver-configuration.html#b94pshp)
* [Driver Parameters](driver-configuration.html#b94psi3)
* [ECMAScript](driver-configuration.html#b94sjyt)
* [Global Configurations](driver-configuration.html#brndxwr)

## A.1.1 Driver Module

The Driver Module section lets you change the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java\* class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The name of the Java class is:

com.novell.nds.dirxml.driver.entitlement.EntitlementServiceDriver

*Native:*
Used to specify the name of the .dll file that is instantiated for the application shim component of the driver. If this option is selected, the driver is running locally.

*Connect to Remote Loader:*
This setting does not apply to the Entitlements Service driver. You cannot use the driver with the Remote Loader.

## A.1.2 Driver Object Password (Identity Console Only)

*Driver Object Password:*
This setting does not apply to the Entitlements Service driver.

## A.1.3 Authentication

The Authentication section stores the information required to authenticate to the connected system and to the Remote Loader. The Entitlements Service driver functions only against the Identity Vault and cannot use the Remote Loader. Therefore, the authentication settings do not apply.

The only setting that applies to the Entitlements Service driver is the cache setting.

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited.

Click Unlimited to set the file size to unlimited in Designer.

## A.1.4 Startup Option

The Startup Option section enables you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

*Do not automatically synchronize the driver:*
This option applies only if the driver is deployed and was previously disabled. If this is not selected, the driver re-synchronizes the next time it is started.

## A.1.5 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters.

*Driver parameters for server:*
Displays or specifies the server name or IP address of the server whose driver parameters you want to modify.

*Edit XML:*
Opens an editor so that you can edit the driver’s configuration file.

*Subscriber Options > Result Threshold:*
Specifies the maximum number of results that the driver logs for each object to which an entitlement is granted or revoked. For example, if a user is granted four entitlements, the default threshold of 10 results per entitlement causes a maximum of 40 results to be logged on the User object.

## A.1.6 ECMAScript

Enables you to add ECMAScript resource files. The resources extend the driver’s functionality when Identity Manager starts the driver.

## A.1.7 Global Configurations

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
