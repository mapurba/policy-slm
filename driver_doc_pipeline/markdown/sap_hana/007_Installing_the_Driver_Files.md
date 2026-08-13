# 2.3 Installing the Driver Files

The SAP HANA driver is a Java-based driver and can be run on the Identity Manager engine or on a Remote Loader server. It works only with Java Remote Loader.

* [Installing the Driver Files as a Root User](t4azuzp4pnau.html#t4dsciq3uvqu)
* [Installing the Driver Files as a Non-Root User](t4azuzp4pnau.html#t4dscj2smtnz)
* [Configuring Remote Loader for the Driver Instance](t4azuzp4pnau.html#t4azv02eedmk)

## 2.3.1 Installing the Driver Files as a Root User

You must install the driver files manually. The SAP HANA driver files are installed on the Identity Manager server at the same time as the Identity Manger engine. The installation program extends the Identity Vault’s schema and installs the driver shim and the driver configuration file, but does not create the driver in the Identity Vault or upgrade an existing driver’s configuration. For information about creating the driver, see [Creating the Driver Object](t4avmq79xc47.html).

To install the dependent jar files, perform the following actions on your platform as applicable:

1. Login as root on the server where you want apply the driver jar file.
2. Navigate to the extracted IDM\_SAPHanaDriver\_1.0.0.zip directory and perform one of the following actions for your platform:

   * For Linux:

     Install the new netiq-DXMLSAPHana-1.0.0.0000-1.noarch.rpm in your driver installation directory by running the following command in a terminal window. If you are installing the binary, run the below command:

     ```

                       rpm -ivh (binaries-path)/netiq-DXMLSAPHana-1.0.0.0000-1.noarch.rpm
     ```

   * For Windows:

     Copy the saphanashim.jar file to your driver installation folder. For example, <InstallLocation\_Drive>\NetIQ\IdentityManager\NDS (local installation) or <InstallLocation\_Drive>\Novell\RemoteLoader\64bit (remote installation).

*NOTE:*It is mandatory,

* For Windows: Identity Manager engine must contain the ngdbc-2.16.11.jar (available in [Maven Repository](https://repo1.maven.org/maven2/com/sap/cloud/db/jdbc/ngdbc/2.16.11/)) in <InstallLocation\_Drive>\NetIQ\IdentityManager\NDS\lib and Windows RL path <InstallLocation\_Driver>\NetIQ\IDM\RemoteLoader\64bit\lib
* For Linux: Identity Manager engine must contain the ngdbc-2.16.11.jar (available in [Maven Repository](https://repo1.maven.org/maven2/com/sap/cloud/db/jdbc/ngdbc/2.16.11/)) in /opt/novell/eDirectory/lib/dirxml/classes.

## 2.3.2 Installing the Driver Files as a Non-Root User

1. Verify that the /rpmdirectory exists and contains the \_db.\* file.
2. The\_db.\* file is created during a non-root installation of the Identity Manager engine. The absence of this file indicates that the Identity Manager is not installed properly. In such a case, reinstall the Identity Manager to correctly place the file in the mentioned directory.
3. To set the root directory to the location of non-root in Identity Manager, enter the following command in the command prompt:

   ROOTDIR=<non-root eDirectory location>

   This will set the environmental variables to the directory where Identity Manager is installed as a non-root user.
4. For example, to install the SAP HANA driver rpm, use this command:

   rpm --dbpath $ROOTDIR/rpm -ivh --relocate=/usr=$ROOTDIR/opt/novell/eDirectory --relocate=/etc=$ROOTDIR/etc --relocate=/opt/novell/eDirectory=$ROOTDIR/opt/novell/eDirectory --relocate=/opt/novell/dirxml=$ROOTDIR/opt/novell/dirxml --relocate=/var=$ROOTDIR/var --badreloc --nodeps --replacefiles /home/user/netiq-DXMLSAPHana-1.0.0.0000-1.noarch.rpm

   *NOTE:*In the above command /opt/novell/eDirectory is the location where non-root Identity Manager is installed, and /home/user/ is the home directory of the non-root user.

You must configure the driver to use an SSL connection between the Remote Loader and the Identity Manager server. For more information, see [Creating a Secure Connection to the Identity Manager Engine](../../../identity-manager-48/driver_admin/data/b18xta1v.html#t461ov2hxlp7) in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

For more information on configuring the Remote Loader, see [Configuring Remote Loader for the Driver Instance](t4azuzp4pnau.html#t4azv02eedmk).

## 2.3.3 Configuring Remote Loader for the Driver Instance

For more information about specifying values for these parameters, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/driver_admin/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

Below is an example of a Linux configuration file with some sample values.

```
-description "SAP HANA Driver"
-commandport 8000
-connection "port=8090"
-trace 3
-tracefile "/opt/netiq/SAP HANAdriver.log" (or "C:\novell\remoteloader\64bit\SAP HANADriver-Trace.log" on Windows)
-tracefilemax 100M
-class "com.netiq.dirxml.driver.saphana.SAPHanaDriverShim"
```

Once the driver instance is running, you can use the command line on Linux or Remote Loader Console on Windows to instruct the Remote Loader to perform a function. For example, turn the trace on or off on Windows or stop the driver instance.
