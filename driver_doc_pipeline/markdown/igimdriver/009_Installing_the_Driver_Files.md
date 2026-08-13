# 2.4 Installing the Driver Files

The IGIM driver is a Java-based driver and can be run on the Identity Manager engine or on a Remote Loader server. It works only with native and Java Remote Loader.

By default, the IGIM driver files are installed on the Identity Manager server at the same time as the Identity Manger engine. The installation program extends the Identity Vault’s schema and installs the driver shim and the driver configuration file. It does not create the driver in the Identity Vault or upgrade an existing driver’s configuration. For information about creating the driver, see [Creating the Driver Object](creating-and-configuring-the-netiq-idm-igim-driver.html#creating-the-netiq-idm-igim-driver).

If you want to run the driver with the Remote loader, verify that the IGDriverShim.jar file is present in the /opt/novell/eDirectory/lib/dirxml/classes or C:\novell\remoteloader\lib directory for the Remote Loader. Otherwise, copy the file from the Identity Vault server to the appropriate directory for your operating system. You must configure the driver to use an SSL connection between the Remote Loader and the Identity Manager server. For more information, see [Creating a Secure Connection to the Identity Manager Engine](../../../identity-manager-48/driver_admin/data/b18xta1v.html#t461ov2hxlp7) in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

Before using the Remote Loader, you must configure the Remote Loader and the driver. For more information, see [Configuring the Remote Loader for the Driver Instance](installing-the-netiq-idm-igim-driver-files.html#configuring-the-netiq-idm-igim-driver-with-remote-loader).

## 2.4.1 Configuring the Remote Loader for the Driver Instance

To configure the driver to work with the Remote Loader, specify the following configuration parameters from the command line, in a configuration file (UNIX or Linux), or in the Remote Loader Console (Windows):

* -description (optional)
* -commandport
* connection parameters:

  + port (mandatory)
  + address
  + fromaddress
  + handshaketimeout
  + rootfile
  + keystore
  + storepass
  + localaddress
  + hostname
  + kmo
  + secureprotocol
  + enforceSuiteB
  + useMutualAuth
* trace file parameters (optional):

  + -trace
  + -tracefile
  + -tracefilemax
* -javaparam
* -class or -module

For more information about specifying values for these parameters, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/driver_admin/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

NetIQ provides a sample configuration file config8000.txt to help you configure the Remote Loader and drivers for use with your application shim on Linux. By default, the sample file is located in the /opt/novell/dirxml/doc directory. You can save the file in the default path or choose a different location for the file. On Windows, specify the configuration details at the time of adding the driver instance to the Remote Loader in the Remote Loader Console.

Below is an example of a configuration file with some sample values.

```
-description "IGIM Driver"
-commandport 8000
-connection "port=8090"
-trace 3
-tracefile "/opt/netiq/igimdriver.log" (or "C:\novell\remoteloader\64bit\IGIMDriver-Trace.log" on Windows)
-tracefilemax 100M
-class "com.netiq.idm.driver.igdriver.IGDriverShim"
```

Once the driver instance is running, you can use the command line on Linux or Remote Loader Console on Windows to instruct the Remote Loader to perform a function. For example, turn the trace on or off on Windows or stop the driver instance.

### Configuring the Remote Loader for the Driver Instance on Linux

This section assumes that the IGDriverShim.jar file is present in the /opt/novell/eDirectory/lib/dirxml/classes directory for the Remote Loader.

1. Log in to the computer where you installed the Remote Loader.
2. In a text editor, create a new file or open the sample file config8000.txt from the /opt/novell/dirxml/doc directory.
3. Add the configuration parameters to the file.
4. Save the file.
5. Note the port number associated with the Remote Loader instance. You need this value when configuring the driver in Designer.
6. (Optional) For the Remote Loader to start the driver automatically when your system starts, save the file to the /etc/opt/novell/dirxml/rdxml directory.

### Configuring the Remote Loader for the Driver Instance on Windows

This section assumes that the IGDriverShim.jar file is present in the c:\novell\remoteloader\lib directory for the Remote Loader.

1. Log in to the computer where you installed the Remote Loader.
2. Run rlconsole.exe located by default in C:\novell\remoteloader\nnbit.
3. Click Add, then specify the Description, Driver, and other parameters in the page that displays. The Remote Loader uses these parameters to configure the driver instance and stores them in a .txt file.
4. Save the file in the default location or specify a different location for the file. For example, C:\novell\remoteloader\IGIMRemoteLoader-Config.txt.
5. Note the port number associated with the Remote Loader instance. You need this value when configuring the driver in Designer.
6. (Optional) For the Remote Loader to start the driver automatically when your system starts, verify that Establish a Remote Loader service for this driver instance is selected.

   To configure the driver as an application, deselect this setting. In this case, you need to start the driver manually.
7. Click OK.
