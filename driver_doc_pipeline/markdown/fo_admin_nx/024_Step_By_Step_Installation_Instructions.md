# 5.2 Step-By-Step Installation Instructions

This section presents the various step-by-step tasks that can be combined to cover all Core Driver installation scenarios. The tasks are grouped first into four basic categories:

* [Installing the Driver Shim on Linux](bfg23nl.html#bfiju30)
* [Installing the Driver Shim on Windows Systems](bfg23nl.html#bfgy4bx)
* [Setting Up the Core Driver in iManager](bfg23nl.html#bfgy4by)
* [Other Tasks Following Installation](bfg23nl.html#bfgygtf)

*NOTE:*Be aware of the following:

* Some of the configuration tasks discussed briefly in this section are covered again in more detail in [Section 6.0, Configuring and Administering the Core Driver](chdcejie.html)

## 5.2.1 Installing the Driver Shim on Linux

Core Driver installation on Linux and UNIX begins with one of the following tasks, depending on your scenario:

* [Installing a New Core Driver Shim on Linux](bfg23nl.html#bfiju31)
* [Upgrading a Core Driver Shim on Linux](bfg23nl.html#bfiju3c)

### Installing a New Core Driver Shim on Linux

To install a new Driver Shim on Linux:

1. From your installation media, locate and execute the appropriate self-extracting installer:

   ```
     sh linux_x86_64_coredriver.bin
   ```

   *NOTE:*If eDirectory has EBA enabled, you will need to run export DISABLE\_EBA=true before running this installer.
2. Accept the license, select your installation directory and proceed to install the product files.
3. The installer will next assist you in configuring the Driver Shim. You will be prompted for the Remote Loader password, which is used to encrypt driver network communications. Enter a password and remember it, as you will use it when configuring the driver in iManager.
4. You will then be prompted for a Driver Object password. This is used to access the driver object in eDirectory. This password will also be used when configuring the driver in iManager.
5. The next entry you are asked for is the eDirectory server/port, so the installer can retrieve an SSL certificate from eDirectory using your SSL-configured LDAP server. Enter the DNS name or IP address of the LDAP server that the Core Driver Shim will use to communicate with. Typically, this will be localhost on port 636.
6. When prompted for an eDirectory admin name/password, enter the eDirectory administrator’s ID in LDAP dot format (example: admin.acme), followed by the password.

   *NOTE:*The installer must get a successful directory connection in order to proceed. Consult your eDirectory LDAP documentation for troubleshooting.
7. When prompted for an ASAM System Container Context, specify the distinguished name (DN) of the container in which the organizational unit ASAM System should be created. The driver will store configuration and synchronization information in this container. Enter the DN in LDAP dot format. Example: idm.acme.

   *NOTE:*If you are adding a secondary driver, or upgrading a driver, the installer may detect your existing Fan-Out installation and prompt you to accept the discovered location.
8. You are next prompted for information about the Core Driver, beginning with a descriptive name and the network port it will use (default 3451).
9. For the Core Driver network address, select a DNS name or IP address for the Core Driver. If your system has multiple addresses, use one which other systems (platforms) can use to communicate with the driver.

   The installer will then create the eDirectory objects and indexes needed to completed the configuration.
10. Immediately after installation, you may need to change the port setting for the Core Driver’s built-in remote loader. This is especially likely if you are also using the standard remote loader that comes with Identity Manager, since both versions of the remote loader use 8090 as their default port setting.

    The port setting for the Core Driver’s built-in remote loader resides in the fanout.conf file, which is located in /usr/local/ASAM/data/.

    Edit the following line in fanout.conf to reflect the desired port:

    ```
    -connection "ca=/usr/local/ASAM/keys/ca.pem port=8090"
    ```
11. If this installation is a secondary driver, migrate the Certificate Authority from the primary system. For details, see [Migrating Certificate Authority](bfg23nl.html#bi167q5).

*NOTE:*If you have a firewall, be sure to add the Driver's network port (default 3451) to its open ports list.

At the completion of this installation task, go next to [Setting Up the Core Driver in iManager](bfg23nl.html#bfgy4by).

### Upgrading a Core Driver Shim on Linux

If you already have an instance of the Core Driver Shim installed on your Linux system, you may use the same installer to upgrade the installation files.

To upgrade a Driver Shim on Linux:

1. Stop the Core Driver object in iManager.
2. From your installation media, locate and execute the appropriate self-extracting installer:

   ```
     sh linux_x86_64_coredriver.bin
   ```
3. Accept the license, and enter Y to upgrade the existing installation.
4. If you are currently running a Core Driver shim version prior to 4.8.1.0, are upgrading to version 4.8.1.0 or later, and use systemd for managing services, you may wish to convert your previous startup method from the older init to systemd.

   1. Disable your current init startup routine:

      chkconfig asamcdrvd off
   2. Install new systemd startup configuration:

      cp /usr/local/ASAM/data/SystemdStartupScripts/asamcdrv.service /etc/systemd/system/
   3. Refresh systemd and enable service:

      systemctl daemon-reload

      systemctl enable asamcdrv

## 5.2.2 Installing the Driver Shim on Windows Systems

Core Driver installation on Windows begins with one of the following tasks, depending on your scenario:

* [Installing the Core Driver Shim on Windows Systems](bfg23nl.html#bfgyl26)
* [Upgrading a Local Core Driver Shim on Windows Systems](bfg23nl.html#bfgymus)
* [Upgrading a Remote Core Driver Shim on Windows Systems](bfg23nl.html#bfgyn4d)

### Installing the Core Driver Shim on Windows Systems

To install a Driver Shim on a Windows System:

1. From your installation media, run the following command:

   ```
     fan-out\IDMCoreDrivers\Win\win_x86_coredriver.exe
   ```

   This x86 (32-bit) executable is compatible with both x86 and x64 versions of Windows.
2. Accept the license, select your installation directory and proceed to install the product files.
3. The installer will next assist you in configuring the Driver Shim. You will be prompted for the Remote Loader password, which is used to encrypt driver network communications. Enter a password and remember it, as you will use it when configuring the driver in iManager.
4. You will then be prompted for a Driver Object password. This is used to access the driver object in eDirectory. This password will also be used when configuring the driver in iManager.
5. The next entry you are asked for is the eDirectory server/port, so the installer can retrieve an SSL certificate from eDirectory using LDAP. Enter the DNS name or IP address of an eDirectory server, and the LDAP secure port (default 636). In the console window that appears, enter y to accept the certificate.

   *NOTE:*If you are running both eDirectory and Active Directory on the Windows server, you may need to change the LDAP ports of either eDirectory or Active Directory so that they do not interfere with each other. See your product documentation for more information.
6. When prompted for an eDirectory admin name/password, enter the eDirectory administrator’s ID in LDAP dot format (example: admin.acme), followed by the password.

   *NOTE:*The installer must get a successful directory connection in order to proceed. Consult your eDirectory LDAP documentation for troubleshooting.
7. When prompted for an ASAM System Container Context, specify the distinguished name (DN) of the container in which the organizational unit ASAM System should be created. The driver will store synchronization information in this container. This is usually the top-level organization in the tree. Example: acme.
8. You are next prompted for information about the Core Driver, beginning with a descriptive name and the network port it will use (default 3451).
9. For the Core Driver network address, select a DNS name or IP address for the Core Driver. If your system has multiple addresses, use one which other systems (platforms) can use to communicate with the driver.

   The installer will then create the eDirectory objects and indexes needed to completed the configuration.
10. Immediately after installation, you may need to change the port setting for the Core Driver’s built-in remote loader. This is especially likely if you are also using the standard remote loader that comes with Identity Manager, since both versions of the remote loader use 8090 as their default port setting.

    The port setting for the Core Driver’s built-in remote loader resides in the fanout.conf file, which is located in C:\Novell\ASAM\data\.

    Edit the following line in fanout.conf to reflect the desired port:

    ```
    -connection "ca=/usr/local/ASAM/keys/ca.pem port=8090"
    ```

*NOTE:*If you have a firewall, be sure to add the Driver's network port (default 3451) to its open ports list.

At the completion of this installation task, go next to [Setting Up the Core Driver in iManager](bfg23nl.html#bfgy4by).

### Upgrading a Local Core Driver Shim on Windows Systems

You can upgrade a driver running in Local mode on your Windows eDirectory server. The upgraded Driver will run as a Remote Driver, with both the Driver objects and Driver Shim on the same system.

To upgrade a Driver Shim that is running in Local mode in Windows:

1. Stop the Core Driver object in iManager.
2. From your installation media, run the following command:

   ```
     fan-out\IDMCoreDrivers\Win\win_x86_coredriver.exe
   ```

   This x86 (32-bit) executable is compatible with both x86 and x64 versions of Windows.
3. Accept the license, select the same installation directory as your previous installation (usually C:\Novell\ASAM) and proceed to install the product files.
4. The installer will next assist you in configuring the Driver Shim. You will be prompted for the Remote Loader password, which is used to encrypt driver network communications. Enter a password and remember it, as you will use it when configuring the driver in iManager.
5. You will then be prompted for a Driver Object password. This password will also be used when configuring the driver in iManager.
6. The next entry you are asked for is the eDirectory server/port, so the installer can retrieve an SSL certificate from eDirectory using LDAP. Enter the DNS name or IP address of an eDirectory server, and the LDAP secure port (default 636). In the console window that appears, enter y to accept the certificate.

   *NOTE:*If you are running both eDirectory and Active Directory on the Windows server, you may need to change the LDAP ports of either eDirectory or Active Directory so that they do not interfere with each other. See your product documentation for more information.
7. When prompted for an eDirectory admin name/password, enter the eDirectory administrator’s ID in LDAP dot format (example: admin.acme), followed by the password.

   *NOTE:*The installer must get a successful directory connection in order to proceed. Consult your eDirectory LDAP documentation for troubleshooting.
8. When prompted for an ASAM System Container Context, specify the distinguished name (DN) of the container in which the organizational unit ASAM System resides. This is usually the top-level organization in the tree. Enter the DN in LDAP dot format. Example: idm.acme.
9. When prompted whether to create a new Driver or upgrade an existing one, click No to upgrade an existing Driver.
10. When a list of drivers displays, select the Driver associated with the system you are upgrading.

    The installer will then generate an updated configuration file and install indexes needed to completed the configuration. (You may receive a warning message regarding indexes since they will already exist.)
11. Immediately after installation, you may need to change the port setting for the Core Driver’s built-in remote loader. This is especially likely if you are also using the standard remote loader that comes with Identity Manager, since both versions of the remote loader use 8090 as their default port setting.

    The port setting for the Core Driver’s built-in remote loader resides in the fanout.conf file, which is located in C:\Novell\ASAM\data\.

    Edit the following line in fanout.conf to reflect the desired port:

    ```
    -connection "ca=/usr/local/ASAM/keys/ca.pem port=8090"
    ```

*NOTE:*If you have a firewall, be sure to add the Driver's network port (default 3451) to its open ports list.

At the completion of this installation task, go next to [Setting Up the Core Driver in iManager](bfg23nl.html#bfgy4by), which includes the task for upgrading a Core Driver configuration

### Upgrading a Remote Core Driver Shim on Windows Systems

If you’re running a Fan-Out Driver in Remote mode, you can upgrade the Driver Shim on the Windows system running the Connected System portion of the Driver.

To upgrade a Driver Shim that is running in Remote mode in Windows:

1. Stop the Core Driver object and the Remote Loader instance for the current driver in iManager.
2. Still in iManager, open the Identity Manager Remote Loader Console, select the Fan-Out Driver instance and click Edit. Make a note of the Connection Port, Trace Level and Trace File fields.
3. Because you no longer need the standard NetIQ Remote Loader, you may disable or remove it as follows, depending on whether you have other Remote Drivers:

   * If you’re running other Remote Drivers on the system, simply remove the Fan-Out Driver instance by selecting it in the Remote Loader Console and clicking Remove.
   * If you aren't running other Remote Drivers on the system, open Control Panel and run | Add or Remove Programs (Programs and Features on Windows Server 2008) to remove the NetIQ Identity Manager Connected System program.
4. From your installation media, run the following command:

   ```
     fan-out\IDMCoreDrivers\Win\win_x86_coredriver.exe
   ```

   This x86 (32-bit) executable is compatible with both x86 and x64 versions of Windows.
5. Accept the license, select the same installation directory as your previous installation (usually C:\Novell\ASAM) and proceed to install the product files.
6. The installer will next assist you in configuring the Driver Shim. You will be prompted for the Remote Loader password, which is used to encrypt driver network communications. Enter a password and remember it, as you will use it when configuring the driver in iManager.
7. You will then be prompted for a Driver Object password. This password will also be used when configuring the driver in iManager.
8. The next entry you are asked for is the eDirectory server/port, so the installer can retrieve an SSL certificate from eDirectory using LDAP. Enter the DNS name or IP address of an eDirectory server, and the LDAP secure port (default 636). In the console window that appears, enter y to accept the certificate.

   *NOTE:*If you are running both eDirectory and Active Directory on the Windows server, you may need to change the LDAP ports of either eDirectory or Active Directory so that they do not interfere with each other. See your product documentation for more information.
9. When prompted for an eDirectory admin name/password, enter the eDirectory administrator’s ID in LDAP dot format (example: admin.acme), followed by the password.

   *NOTE:*The installer must get a successful directory connection in order to proceed. Consult your eDirectory LDAP documentation for troubleshooting.
10. When prompted for an ASAM System Container Context, specify the distinguished name (DN) of the container in which the organizational unit ASAM System resides. This is usually the top-level organization in the tree. Enter the DN in LDAP dot format. Example: idm.acme.
11. When prompted whether to create a new Driver or upgrade an existing one, click No to upgrade an existing Driver.
12. When a list of drivers displays, select the Driver associated with the system you are upgrading.

    The installer will then generate an updated configuration file and install indexes needed to completed the configuration. (You may receive a warning message regarding indexes since they will already exist.)
13. Immediately after installation, you may need to change the port setting for the Core Driver’s built-in remote loader. This is especially likely if you are also using the standard remote loader that comes with Identity Manager, since both versions of the remote loader use 8090 as their default port setting.

    The port setting for the Core Driver’s built-in remote loader resides in the fanout.conf file, which is located in C:\Novell\ASAM\data\.

    Edit the following line in fanout.conf to reflect the desired port:

    ```
    -connection "ca=/usr/local/ASAM/keys/ca.pem port=8090"
    ```

*NOTE:*If you have a firewall, be sure to add the Driver's network port (default 3451) to its open ports list.

At the completion of this installation task, go next to [Setting Up the Core Driver in iManager](bfg23nl.html#bfgy4by), which includes the task for upgrading a Core Driver configuration.

## 5.2.3 Setting Up the Core Driver in iManager

You will use the Fan-Out Driver’s Web application to complete the Core Driver installation. This application resides in recent versions of iManager as a standard plug-in. If your version of iManager does not include the plug-in, you can install it from the software that comes with the Core Driver.

*NOTE:*In addition to iManager, you can use Designer, an application interface that comes with Identity Manager, for setting up and modeling large deployments of the Fan-Out Driver. A Fan-Out Driver application plug-in is included as part of the Designer installation. For more information on using Designer, see [Applications For Configuration](chdijbdi.html).

After you have installed or upgraded a Driver Shim, the installation process continues in iManager with the following tasks, depending on your scenario:

* [Importing a Configuration for a Newly Installed Core Driver](bfg23nl.html#bfgz7zl)
* [Upgrading a Core Driver Configuration](bfg23nl.html#bfgz8fu)

If your version of iManager does not include the plug-in or if you are not familiar with iManager, you can refer to two additional topics at the end of this section before starting:

* [Installing the iManager Plug-In (If not Preinstalled)](bfg23nl.html#bfgz253)
* [Using the iManager Interface](bfg23nl.html#bfgz79y)

### Importing a Configuration for a Newly Installed Core Driver

Use iManager to configure a Core Driver in the Identity Vault (eDirectory). To import a Core Driver configuration:

1. Login to iManager for your tree and select the Import Configuration task under Identity Manager Utilities on the left.
2. Keep the Driver Set selection and, if this is a new Driver Set, select the server in eDirectory where the Driver will run.
3. From the Configurations menu, select Fan-Out-IDM3\_6\_0-V1.xml. If this file is not available, select Import a configuration from the client and select the file rules\Fan-Out-IDM3\_6\_0-V1.xml under the directory where the Driver Shim is installed (C:\Novell\ASAM by default).
4. Enter the following configuration fields. The installer will have filled in some of these fields:

   * Driver Name: Enter a descriptive name.
   * Activation Group: Choose the selection that corresponds to the activation you purchased. The Driver will operate in evaluation mode for 90 days if you don’t have an activation.
   * LDAP Host and Port: Enter the DNS name or IP address and TCP port of your LDAP host.
   * Remote Host Name and Port: Enter the DNS name or IP address and TCP port used by the system where the Driver Shim runs.
   * ASAM Master User/Password: Enter an LDAP account that will be used to manage Driver information.
   * Driver Object Password/Remote Loader Password: Enter the passwords you entered when installing the Driver Shim.
5. Click Define Security Equivalences and add your ASAM Master User.
6. Click Exclude Administrative Roles and add the admin user, the ASAM Master User and other high-privilege users to the Excluded Users list.
7. Click Finish to complete the import.

### Upgrading a Core Driver Configuration

If you upgrade a Core Driver Shim, you also need to upgrade its configuration in iManager. To upgrade a configuration:

1. Login to iManager for your tree and select the Import Configuration task under Identity Manager Utilities on the left.
2. Select the Driver Set that contains the Driver to be upgraded.
3. Click Next to keep the Driver Set selection.
4. From the Configurations menu, select Fan-Out-IDM3\_6\_0-V1.xml. If this file is not available, select Import a configuration from the client and select the file rules\Fan-Out-IDM3\_6\_0-V1.xml under the directory where the Driver Shim is installed (C:\Novell\ASAM by default).
5. On the next page, to the right of the Driver Name field, select the driver you wish to upgrade from the Existing Drivers drop-down box.
6. Enter the following configuration fields, consistent with your current installation. The installer will have filled in some of these fields:

   * Activation Group: Choose the selection that corresponds to the activation you purchased. The Driver will operate in evaluation mode for 90 days if you don’t have an activation.
   * LDAP Host and Port: Enter the DNS name or IP address and secure TCP port of your LDAP host.
   * Remote Host Name and Port: Enter the DNS name or IP address and TCP port used by the system where the Driver Shim runs.
   * ASAM Master User/Password: Enter an LDAP account that will be used to manage Driver information.
   * Driver Object Password/Remote Loader Password: Enter the passwords you entered when installing the Driver Shim.
7. On the next page, select Update everything about that driver and policy libraries and click Next.
8. Click Finish to complete the import.
9. If necessary, apply any manual customizations.

*NOTE:*You must install the new version of the iManager Plug-in before using the Driver. See [Installing the iManager Plug-In (If not Preinstalled)](bfg23nl.html#bfgz253).

### Installing the iManager Plug-In (If not Preinstalled)

If your installation of iManager does not display the Fan-Out Driver Configuration role (Roles and Tasks menu on the left), you can install the iManager plug-in manually.

To install the iManager plug-in:

1. Login to iManager as an administrative user.
2. Click the Configure icon at the top.
3. Click Available NetIQ Plug-in Modules under Plug-in Installation on the left menu.
4. Click Add above the list of plug-ins.
5. Select fan-out\iManagerPlugIn\FanOutWeb.npm from your installation media and click OK.
6. Check the box next to NetIQ Identity Manager - Fan-Out Driver Plug-in and click Install above the list of plug-ins.
7. Restart the Tomcat or Tomcat5 service on your iManager system, and exit and log back into iManager.
8. If the Fan-Out Driver Configuration role has not appeared, continue with the following steps.
9. Click the Configure icon at the top.
10. Click RBS Configuration under Role Based Services on the left menu.
11. Click the number under the Not-Installed column in the table.
12. Check the box next to FanOutWeb and click Install above the list.
13. Click the Roles and Tasks icon at the top.

With the plug-in now installed, you can proceed to your next task.

*NOTE:*For additional information about using iManager with the Fan-Out Driver application plug-in, see [Applications For Configuration](chdijbdi.html).

### Using the iManager Interface

To use the iManager interface for setting up a Core Driver:

1. In iManager, select the Configure iManager Plug-In task under Fan-Out Driver Configuration.
2. Enter the DNS name or IP address and port of the system running the Driver Shim and click Apply.
3. You may now use any of the items under Fan-Out Driver Configuration and Fan-Out Driver Utilities in iManager.

## 5.2.4 Other Tasks Following Installation

After the initial installation or upgrade of a Core Driver, other tasks that you may need to perform from time to time include the following:

* [Migrating Certificate Authority](bfg23nl.html#bi167q5)
* [Starting the Core Driver](bfg23nl.html#bfgzjwn)
* [Stopping the Core Driver](bfg23nl.html#bfgzjwr)
* [Configuring the Core Driver Shim to Auto-Start](bfg23nl.html#b12f3265)
* [Reconfiguring the Driver Shim](bfg23nl.html#bfgzjwv)
* [Installing Secondary Drivers](bfg23nl.html#bfikvwi)
* [Installing a New Primary Driver](bfg23nl.html#bfh02k4)

### Migrating Certificate Authority

If you have migrated your primary Core Driver from one system to another, or have added a new secondary Core Driver, you will need to physically copy the Certificate Authority files from your previous host system to your new host system. These files are:

```
  ASAM/data/CoreDriver/certs/ca_cert.pem
  ASAM/data/CoreDriver/certs/ca_key.pem
  ASAM/data/CoreDriver/certs/ca.pem
```

If you do not perform this migration, your new primary Core Driver system will generate a new Certificate Authority when it first starts up. This will invalidate any platform certificates that may have been signed using the previous Certificate Authority.

### Starting the Core Driver

Both the Identity Manager Driver object and Driver Shim service must be running for the Core Driver to operate. To start the Core Driver:

1. In iManager, select the Identity Manager Overview task under Identity Manager.
2. Select the Driver Set where the Driver is installed.
3. Click the status indicator (stop line) in the upper right corner of the driver icon, then click Start Driver.
4. On the Driver Shim system, start the Fan-Out Driver as follows:

   * If the system is running Linux/UNIX, using init, enter the following command:

     ```
     /etc/init.d/asamcdrvd start
     ```
   * If the system is running Linux/UNIX, using systemd, enter the following command:

     ```
     systemctl start asamcdrv
     ```
   * If the system is running Windows, open Control Panel and run Administrative Tools > Services. Start the NetIQ IDM Fan-Out Driver service.

### Stopping the Core Driver

To stop the Core Driver:

1. On the Driver Shim system, stop the Fan-Out Driver as follows:

   * If the system is running Linux/UNIX, using init, enter the following command:

     ```
     /etc/init.d/asamcdrvd stop
     ```
   * If the system is running Linux/UNIX, using systemd, enter the following command:

     ```
     systemctl stop asamcdrv
     ```
   * If the system is running Windows, open Control Panel and run Administrative Tools > Services. Stop the NetIQ IDM Fan-Out Driver service.
2. In iManager, stop the Driver in the Driver Set Overview.

### Configuring the Core Driver Shim to Auto-Start

If you want the Core Driver Shim (asamcdrv) to automatically start at system startup, you will need to configure the operating system startup routines.

Using chkconfig

For systems using init, the asamcdrvd startup script for Linux automatically integrates with the Linux chkconfig utility. To set asamcdrvd to auto-start, enter the following command:

```
chkconfig asamcdrvd on
```

Using systemctl

For systems using systemd, the asamcdrv.service configuration will automatically be installed and set to start automatically.

### Reconfiguring the Driver Shim

The Driver Shim can be reconfigured in a number of areas, as itemized below.

*NOTE:*Always be sure to stop the Driver Shim before starting any of these reconfiguration tasks as described in [Stopping the Core Driver](bfg23nl.html#bfgzjwr).

* To re-run the installer’s configuration wizard in Windows, open Control Panel and run Add or Remove Programs (Programs and Features on Windows Server 2008). Click the Change button under NetIQ IDM Fan-Out Core Driver. Then select Modify or Repair from the dialog box that opens.

  You can use the installer to create a new installation, create a new driver or upgrade an existing driver. Note that the installer doesn't remember previously configured fields, so you'll have to enter the fields like you did on the first-time install.
* To change the Remote Loader and/or Driver Object passwords:

  + If the system is running Linux, enter the following command and select menu item 1:

    ```
    /usr/local/ASAM/setup/fandrv-config
    ```
  + If the system is running Windows, execute the following command from the installation directory (C:\Novell\ASAM by default):

    ```
    bin\CoreDriver\asamcdrv.exe -sp
    ```
* To retrieve a new SSL certificate from eDirectory:

  + If the system is running Linux, enter the following command and select menu item 2:

    ```
    /usr/local/ASAM/setup/fandrv-config
    ```
  + If the system is running Windows, execute the following command from the installation directory (C:\Novell\ASAM by default):

    ```
    bin\CoreDriver\asamcdrv.exe -s
    ```
* To install or remove the Driver Shim service in Windows, execute the following command from the installation directory (C:\Novell\ASAM by default) using either the installService or removeService parameter:

  ```
  bin\CoreDriver\asamcdrv.exe -parameter
  ```

### Installing Secondary Drivers

For scalability, you can install secondary drivers to handle platform synchronization and password requests. A system can run only one Driver Shim. See [Performance Tuning](bfmn9rs.html) for more information on specifying secondary drivers.

To install a secondary driver.

1. On the secondary Driver Shim’s system, follow steps 1-7 under one of the following tasks, depending on your operating environment:

   *NOTE:*In step 7, be sure to specify the container that holds the ASAM System Container.

   * [Installing a New Core Driver Shim on Linux](bfg23nl.html#bfiju31)
   * [Installing the Driver Shim on Windows Systems](bfg23nl.html#bfgy4bx)
2. You will be prompted to create a new Driver or upgrade a Driver. Click Yes to create a new Driver.
3. Specify a distinct name for the Driver as well as its port.
4. Select the Driver’s network address.
5. When you are prompted whether to make the new Driver primary, click No to keep the Driver secondary.
6. Once the Driver Shim is installed, import a new Driver following the steps in [Importing a Configuration for a Newly Installed Core Driver](bfg23nl.html#bfgz7zl). Be sure to use the XML configuration file generated for the secondary Driver.
7. Migrate the Certificate Authority from the primary system. For details, see [Migrating Certificate Authority](bfg23nl.html#bi167q5).

You can now run the secondary Driver as you would the primary Driver.

### Installing a New Primary Driver

Depending on your configuration needs, you may decide to install a Driver Shim for a new primary driver.

*NOTE:*If the Core Driver you wish to make primary is already installed, you can use the Configure Core Drivers menu task in iManager to do this.

1. Stop all Identity Manager Driver objects and Driver Shims. See [Stopping the Core Driver](bfg23nl.html#bfgzjwr).
2. Follow all the steps in the task, [Installing Secondary Drivers](bfg23nl.html#bfikvwi), with the following exception:

   In step 5, click Yes to make the driver primary.
3. Start all Identity Manager Driver objects and Driver Shims. See [Starting the Core Driver](bfg23nl.html#bfgzjwn).
