# 3.2 Installing the Windows Scripting Driver

Topics in this section include

* [Installing the Driver Shim](b8mow8v.html#b8mowoy)
* [Running the Driver](b8mow8v.html#b8mp00j)
* [Running the Script Service for PowerShell (default mode)](b8mow8v.html#brh2if1)
* [Running Multiple Instances of the Driver (optional)](b8mow8v.html#brh2jbf)

## 3.2.1 Installing the Driver Shim

1. Obtain one of the following files from your installation media:

   * win\_x86\_64\_scriptdriver\_install.exe (64-bit)
   * win\_x86\_scriptdriver\_install.exe (32-bit)

   Run this file on your Windows system.
2. Click Next to continue the installation.
3. Accept the default installation folder or specify your own. Click Next to continue.
4. Review your settings and click Next to continue.
5. After the driver files are copied, you are prompted to retrieve an SSL certificate. NetIQ eDirectory must be running to retrieve the certificate. The certificate allows SSL encryption between the Identity Manager engine and the driver shim. Enabling SSL is optional but is recommended for better security. To retrieve the certificate, click Yes and follow the prompts in the console window:

   1. Specify the DNS name or IP address of your eDirectory server.
   2. Specify the LDAP secure port, default 636.
   3. Enter Y to accept the certificate.
6. You are prompted to enter Driver and Remote Loader passwords. These passwords are used to verify that an authorized driver shim is communicating with the Identity Manager engine. Although you don’t need to enter the passwords immediately, they must be set at some point before running the driver. Click Yes to the prompt and follow the prompts in the console window:

   1. Enter and confirm the Remote Loader password.
   2. Enter and confirm the Driver password.
7. The installation of the driver shim is finished, with the option of starting the Driver Shim Service. Proceed to the next section to complete the installation of the driver.

## 3.2.2 Running the Driver

Start the driver engine component in NetIQ iManager.

The driver shim is a Windows service. Use the Windows Services application to start and stop the NetIQ Identity Manager Windows Script Driver service (see [Section 6.0, Using the Scripting Driver](b8nnhcs.html)).

## 3.2.3 Running the Script Service for PowerShell (default mode)

The Script Service preloads Windows PowerShell and keeps it in memory to provide faster performance. Requests to the Script Service are securely submitted by a small program called the Script Client.

### Using the Script Service

To install and use the Script Service:

1. If necessary, add the .NET Framework 3.5 Feature using the Add Roles and Features operation in the Server Manager application.
2. Run Win\Microsoft WSE 3.0 Runtime.msi to install the Web Service Enhancements module.
3. It may be necessary to open TCP port 8081 in your firewall--this port is used only for communication between the Script Client and Script Service executables. The port can be customized in scriptservice.conf, as explained below.
4. In the Services application, set NetIQ IDM Windows Script Driver - Script Service to start automatically.

### Configuring the Script Service

To configure the Script Service

1. Create a file named scriptservice.conf in the WSDriver\conf directory.
2. Open the file and add the desired configuration lines, using the following keywords:

   | Keyword | Description | Syntax |
   | -address | Change the default address and port for Script Service.  Default: localhost:8081 | -address <DNS name or IP address>[:port] |
   | -nosecurity | Do not enforce security. This command is required if the Use Windows EFS driver parameter is disabled. | ``` -nosecurity ``` |
   | -command | Execute a script command on startup. May be specified multiple times. | ``` -command <command> ``` |

### Using PowerShell Directly

If you no longer wish to use the Script Service, follow these steps:

1. Open the Driver Configuration in iManager. In the Driver Parameters, change Script Command to powershell.exe.
2. Either stop or disable the Script Service.
3. Restart the driver.

## 3.2.4 Running Multiple Instances of the Driver (optional)

Running multiple instances of the Scripting Driver on the same system may be desirable, but require some additional steps taken. The instructions in this section assume that you have already installed the Scripting Driver on the system.

### Adding a Windows Scripting Driver Instance

To add an instance:

1. Copy existing files:

   After stopping your original driver, create a new directory, and copy all original driver files to the new directory, using the same directory structure.

   For example, copy files and directories from C:\Program Files\Novell\WSDriver to C:\Program Files\Novell\WSDriver2.
2. Edit wsdrv.conf:

   1. Open the file conf\wsdrv.conf in your new directory structure. Replace all file paths with the path to the new instance directory.

      For example, paths might appear for the -path, -tracefile and -connection options.
   2. Change the port numbers (connection and HTTP) to be different from the original driver's port numbers.

      For example, if the original driver uses default ports 8090 and 8091, the new instance could use 9090 and 9091. Note that these ports need to be opened in a firewall.
3. Create a new service:

   Using the Command Prompt, run wsdriver.exe from the new instance directory with the following options:

   ```
     wsdriver -installService -instance {number} -path {path}
   ```

   The instance number could be 2 for the second instance, 3 for a third, and so on. The path should be the path to the new instance directory, using quote marks. Here's an example:

   ```
     wsdriver -installService -instance 2 -path "C:\Program
        Files\Novell\WSDriver2"
   ```

   This command will create a service named Novell IDM Windows Script Driver - 2.

   *NOTE:*If you would like to run a driver instance directly (not as a service), use the -instance option:

   ```
     wsdriver -instance 2
   ```

   This option is not needed for the original instance.
4. Create a new driver object:

   1. Using iManager or Designer, create a new Driver Object to connect to the new instance. Alternatively, export the original driver's configuration and import it as a new driver.
   2. After creating the Driver, open its configuration. Change the port number in Remote Loader Connection Parameters to the new instance's connection port.
5. Start the services and drivers:

   Start the server for the original and new instances, and start the Drivers in iManager or Designer. The instances will run independently.

### Removing a Windows Scripting Driver Instance

To remove an instance:

1. Stop the Service.
2. Uninstall the Service.

   From the Command Prompt, run:

   ```
     wsdriver -removeService -instance {number}
   ```

   For example:

   ```
     wsdriver -removeService -instance 2
   ```
3. Delete the files.

   Delete the new directory, and all sub-directories, created for the instance.

*NOTE:*To remove the original instance, use the uninstall feature.

### Adding a Linux or Unix Scripting Driver Instance

To add an instance:

1. Copy existing files:

   After stopping your original driver, copy the file structure from /opt/novell/usdrv to your alternate instance location. For example:

   cp -r /opt/novell/usdrv /opt/novell/usdrv-instance2
2. Create a new, separate configuration file from /etc/usdrv.conf:

   1. Open the new configuration file, /etc/usdrv-instance2.conf, and specify the alternate path location for your new instance.

      For example, paths might appear for the -path, -tracefile and -connection options.
   2. Change the port numbers (connection and HTTP) to be different from the original driver's port numbers.

      For example, if the original driver uses default ports 8090 and 8091, the new instance could use 9090 and 9091. Note that these ports need to be opened in a firewall.
3. Create a new, separate, startup script from the original /etc/init.d/usdrvd and change the new startup script to specify the alternate paths as well.
4. Create a new driver object:

   1. Using iManager or Designer, create a new Driver Object to connect to the new instance. Alternatively, export the original driver's configuration and import it as a new driver.
   2. After creating the Driver, open its configuration. Change the port number in Remote Loader Connection Parameters to the new instance's connection port.
5. Start the services and drivers:

   Start the server for the original and new instances, and start the Drivers in iManager or Designer. The instances will run independently.
