# 2.5 Installing the Driver Files

The Workday driver is a Java-based driver and can be run on the Identity Manager engine or on a Remote Loader server. It works only with native and Java Remote Loader.

* [Installing the Driver Files as a Root User](t4azuzp4pnau.html#t4dsciq3uvqu)
* [Installing the Driver Files as a Non-Root User](t4azuzp4pnau.html#t4dscj2smtnz)
* [Configuring Remote Loader for the Driver Instance](t4azuzp4pnau.html#t4azv02eedmk)

## 2.5.1 Installing the Driver Files as a Root User

You must install the driver files manually. The Workday driver files are installed on the Identity Manager server at the same time as the Identity Manger engine. The installation program extends the Identity Vault’s schema and installs the driver shim and the driver configuration file, but does not create the driver in the Identity Vault or upgrade an existing driver’s configuration. For information about creating the driver, see [Creating the Driver Object](t4avmq79xc47.html).

If you want to run the driver with Remote loader, verify that the WorkdayShim.jar file is present in the following directories for the Remote Loader:

* *Linux:*
  /opt/novell/eDirectory/lib/dirxml/classes
* *Windows:*
  C:\novell\remoteloader\lib

Else, copy the file from the Identity Vault server to the appropriate directory based on the operating system.

* Linux: Install the new novell-DXMLWday.rpm in your driver installation directory by running the following command in a terminal window:

  + If you are installing the binary, run the command: rpm -Ivh (binaries-path)/novell-DXMLWday.rpm
* Windows: Copy WorkdayShim.jar in the {IDM-Install-Folder\nds\lib} directory of the Identity Manager Engine. If you want to run the driver with Remote loader on Windows, verify that the WorkdayShim.jar file is present in the {remoteloader\lib} directory.

To install the dependent jar files, perform the following actions on your platform as applicable:

* Linux:

  + Copy the jar file WorkdayUtils.jar, from <IDM\_WorkDayDriver\_1300>/common folder and place it in /opt/novell/eDirectory/lib/dirxml/classes/ directory in the Identity Manager engine.
  + Copy the WorkdayUtils.jar, imgscalr-lib-4.2.jar, jcce-1.3.0.jar, and jcce-oauth-1.3.0.jar from <IDM\_WorkDayDriver\_1300>/common folder and place it in the driver installation folder. For example, /opt/novell/eDirectory/lib/dirxml/classes/ (for local or remote installation).
* Windows:

  + Copy the jar files WorkdayUtils.jar from <IDM\_WorkDayDriver\_1300>/common folder and place it in Identity Manager engine path \NetIQ\IdentityManager\NDS\lib.
  + Copy the imgscalr-lib-4.2.jar, jcce-1.3.0.jar and jcce-oauth-1.3.0.jar from <IDM\_WorkDayDriver\_1300>/common folder and place it in the driver installation folder. For example, \NetIQ\IdentityManager\NDS (local installation) or \Novell\RemoteLoader\64bit (remote installation).

## 2.5.2 Installing the Driver Files as a Non-Root User

1. Verify that the /rpmdirectory exists and contains the \_db.\* file.
2. The\_db.\* file is created during a non-root installation of the Identity Manager engine. The absence of this file indicates that the Identity Manager is not installed properly. In such a case, reinstall the Identity Manager to correctly place the file in the mentioned directory.
3. To set the root directory to the location of non-root in Identity Manager, enter the following command in the command prompt:

   ROOTDIR=<non-root eDirectory location>

   This will set the environmental variables to the directory where Identity Manager is installed as a non-root user.
4. For example, to install the Workday driver rpm, use this command:

   rpm --dbpath $ROOTDIR/rpm -Ivh --relocate=/usr=$ROOTDIR/opt/novell/eDirectory --relocate=/etc=$ROOTDIR/etc --relocate=/opt/novell/eDirectory=$ROOTDIR/opt/novell/eDirectory --relocate=/opt/novell/dirxml=$ROOTDIR/opt/novell/dirxml --relocate=/var=$ROOTDIR/var --badreloc --nodeps --replacefiles /home/user/novell-DXMLWday.rpm

   *NOTE:*In the above command /opt/novell/eDirectory is the location where non-root Identity Manager is installed, and /home/user/ is the home directory of the non-root user.
5. To install the dependent jar files, perform the following actions based on your platform:

   * Linux:

     + Copy the jar file WorkdayUtils.jar, from <IDM\_WorkDayDriver\_1300>/common folder and place it in /opt/novell/eDirectory/lib/dirxml/classes/ directory in the Identity Manager engine.
     + Copy the WorkdayUtils.jar, imgscalr-lib-4.2.jar, jcce-1.3.0.jar, and jcce-oauth-1.3.0.jar from <IDM\_WorkDayDriver\_1300>/common folder and place it in the driver installation folder. For example, /opt/novell/eDirectory/lib/dirxml/classes/ (for local or remote installation).
   * Windows:

     + Copy the jar files WorkdayUtils.jar from from <IDM\_WorkDayDriver\_1300>/common folder and place it in Identity Manager engine path \NetIQ\IdentityManager\NDS\lib.
     + Copy the imgscalr-lib-4.2.jar, jcce-1.3.0.jar and jcce-oauth-1.3.0.jar from <IDM\_WorkDayDriver\_1300>/common folder and place it in the driver installation folder. For example, \NetIQ\IdentityManager\NDS (local installation) or \Novell\RemoteLoader\64bit (remote installation).

You must configure the driver to use an SSL connection between the Remote Loader and the Identity Manager server. For more information, see [Creating a Secure Connection to the Identity Manager Engine](../../../identity-manager-49/driver_admin/data/b18xta1v.html#t461ov2hxlp7) in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-49/driver_admin/data/bktitle.html#bktitle).

For more information on configuring the Remote Loader, see [Configuring Remote Loader for the Driver Instance](t4azuzp4pnau.html#t4azv02eedmk).

## 2.5.3 Configuring Remote Loader for the Driver Instance

For more information about specifying values for these parameters, see [Configuring the Remote Loader and Drivers](../../../identity-manager-49/driver_admin/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-49/driver_admin/data/bktitle.html#bktitle).

Below is an example of a configuration file with some sample values.

```
-description "Workday Driver"
-commandport 8000
-connection "port=8090"
-trace 3
-tracefile "/opt/netiq/workdaydriver.log" (or "C:\novell\remoteloader\64bit\WorkdayDriver-Trace.log" on Windows)
-tracefilemax 100M
-class "com.netiq.dirxml.driver.workday.WDDriverShim"
```

Once the driver instance is running, you can use the command line on Linux or Remote Loader Console on Windows to instruct the Remote Loader to perform a function. For example, turn the trace on or off on Windows or stop the driver instance.
