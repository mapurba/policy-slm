# D.2 Driver Shim Command Line Options

The following options can be specified on the driver shim (usdrv on Linux and UNIX, wsdriver on Windows) command line. You can also specify driver shim command line options as driver shim configuration file statements. For details about the driver shim configuration file, see [The Driver Shim Configuration File](b8mqqe6.html).

## D.2.1 Options Used to Set Up Driver Shim SSL Certificates

The following command line options are used to set up the driver shim SSL certificates:

*Table D-1* Driver Shim Command Line Options for Setting Up SSL Certificates

| Option (Short and Long Forms) | Description |
| -s  -secure | Secures the driver by creating SSL certificates, then exits. |
| -p  -password | Specifies the Remote Loader password |

## D.2.2 Other Options

*Table D-2* Other Driver Shim Command Line Options

| Option (Short and Long Forms) | Description |
| -c <congFile>  -config <configFile> | Instructs the driver shim to read options from the specified configuration file. Options are read from conf/usdrv.conf (Linux/UNIX) or conf\wsdrv.conf (Windows) by default. |
| -sp [remoteLoaderPassword driverObjectPassword]  -setpassword [remoteLoaderPassword driverObjectPassword] | Sets the Remote Loader and driver object passwords to the passwords specified on the command line, then stops the driver shim. If the passwords are omitted, the driver shim prompts for the passwords. |
| -installService | Creates a Windows service for the driver shim called NetIQ Identity Manager Windows Script Driver (Windows only). |
| -removeService | Removes the Windows service NetIQ Identity Manager Windows Script Driver (Windows only). |
| -?  -help | Displays the command line options, then exits. |
| -v-version | Displays the driver shim version and build date, then exits. |
