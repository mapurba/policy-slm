# A.1 Driver Configuration

In Identity Console:

1. Login to Identity Console, select IDM Administration under Identity Manager if not defaulted already.
2. The Identity Manager Overview page appears.
3. Click Driver Sets tab, the configured drivers appear.

   *NOTE:*If the driver set is not listed on the Driver Sets tab, use the Search In field to search for and display the driver set.
4. Click the driver tile. By default Connection Parameters tab appears.Â To configure the selected driver, goto Configuration tab and click Driver > Parameters under Driver Settings, Subscriber Settings and Publisher Settings.
5. Define the driver parameters as required.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon or line, then select click Properties > Driver Configuration.

The Driver Configuration options are divided into the following sections:

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The Java class name is: com.netiq.dirxml.driver.saphana.SAPHanaDriverShim

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two sub options:

* *Remote Loader Client Configuration for Documentation:*
  Includes information on the Remote Loader client configuration when Designer generates documentation for the driver.

## A.1.2 Driver Object Password

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The authentication section stores the information required to authenticate to the connected system.

*Authentication ID:*
This option is not used with the SAP HANA driver.

*Authentication Context:*
This option is not used with the SAP HANA driver.

*Remote Loader Connection Parameters:*
Used only if the driver is connecting to the application through the Remote Loader. The parameter to enter is hostname=xxx.xxx.xxx.xxx port=xxxx kmo=certificatename, when the host name is the IP address of the application server running the Remote Loader server and the port is the port the Remote Loader is listening on. The default port for the Remote Loader is 8090.

The kmo entry is optional. It is only used when there is an SSL connection between the Remote Loader and the Metadirectory engine.

Example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer.

*Application Password:*
This option is not used with the SAP HANA driver.

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

* Driver Options
* Subscriber Options
* Publisher Options

To configure the above options, see [Step 6](t4avmq79xc47.html#driver_param) in the section [Creating the Driver Object](t4avmq79xc47.html).
