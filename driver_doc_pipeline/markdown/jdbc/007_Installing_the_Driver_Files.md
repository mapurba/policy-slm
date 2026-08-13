# 2.0 Installing the Driver Files

By default, the JDBC driver files are installed on the Identity Manager server at the same time as the Identity Manager engine. The installation program extends the Identity Vault’s schema and installs the driver shim and a driver configuration file. It does not create the driver object in the Identity Vault (see [Section 5.0, Creating a New Driver Object](create-new-driver-object-for-jdbc-driver.html)) or upgrade an existing driver’s configuration (see [Section 7.0, Upgrading an Existing Driver](upgrade-an-existing-driver.html)).

The JDBC driver can either be located on the same server as the JDBC database or any other server. The following sections explain what to do if the JDBC driver files are not on the JDBC database server and how to install the third-party JDBC jar files that the driver uses to communicate with the database:

For information about uninstalling the driver, see [Section A.0, Uninstalling the Driver](uninstall-the-jdbc-driver.html).

* [Installing the Driver Files](how-to-install-jdbc-driver-files-for-identity-manager.html)
* [Installing JDBC Driver Jar Files](how-to-install-jdbc-driver-jar-files-for-identity-manager.html)
