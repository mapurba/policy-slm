# 2.2 Installing the Remote Loader and Driver Files

The files for the Entity Data Model driver need to be on the same server where you install the Remote Loader.

* [Installing the Remote Loader](b1fixbz2.html#b1fn0uui)
* [Adding the Entity Data Model Driver File to the Identity Vault](b1fixbz2.html#b1g2bimz)
* [Adding the Entity Data Model Driver Files to the Remote Loader Server](b1fixbz2.html#b1fixilv)

## 2.2.1 Installing the Remote Loader

The Remote Loader loads drivers and communicates with the Identity Manager engine on behalf of drivers installed on remote servers. To ensure appropriate communication between the Entity Data Model driver and Identity Manager, NetIQ recommends that you install the Remote Loader on the Entity Data Model server.

For more information about installation, see [“Installing and Managing the Remote Loader”](https://www.netiq.com/documentation/identity-manager-46/setup/data/part04e.html) in the [NetIQ Identity Manager Setup Guide](https://www.netiq.com/documentation/identity-manager-46/setup/data/front.html).

## 2.2.2 Adding the Entity Data Model Driver File to the Identity Vault

By default, the driver files are installed on the Identity Manager server at the same time as the Identity Manager engine. The installation program extends the Identity Vault’s schema and installs the driver shim and the driver configuration file. It does not create the driver in the Identity Vault or upgrade an existing driver’s configuration.

## 2.2.3 Adding the Entity Data Model Driver Files to the Remote Loader Server

This section provides information for adding the files for the Entity Data Model driver to the Remote Loader server.

1. Log in to the server where you installed the Remote Loader.

   NetIQ recommends that you install the Remote Loader on the Entity Data Model server.
2. Copy the arshim.jar file from the Identity Vault server to the lib directory for the Remote Loader, located by default in the opt/novell/eDirectory/lib/dirxml/classes directory.
3. In the lib directory, install the third-party JDBC driver that supports the Entity Data Model database.
4. In the /etc/opt/novell/dirxml/rdxml Entity Data Model driver directory, create a text file that defines the classpath for the Entity Data Model driver. For example:

   ```
   -description "AR Driver"
   -commandport 8000
   -connection "port=8090"
   -trace 3
   -tracefile "/opt/netiq/ar.log"
   -tracefilemax 100M
   -class "com.novell.nds.dirxml.driver.arshim.AccessReviewDriverShim"
   ```

   For more information about classpaths, see [“Installing and Managing the Remote Loader”](https://www.netiq.com/documentation/identity-manager-46/setup/data/part04e.html) in the [NetIQ Identity Manager Setup Guide](https://www.netiq.com/documentation/identity-manager-46/setup/data/front.html).
5. Note the port number associated with the Remote Loader instance. You need this value when configuring the driver in Designer.
