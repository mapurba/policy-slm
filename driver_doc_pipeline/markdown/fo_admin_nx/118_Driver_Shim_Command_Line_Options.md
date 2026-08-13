# A.3 Driver Shim Command Line Options

The following options can be specified on the driver shim command line. You can also specify driver shim configuration file statements as command line options. For details about the driver shim configuration file, see [The Driver Shim Configuration File](b4baik6.html).

## A.3.1 Options Used to Set Up Driver Shim SSL Certificates

The following command line options are used to set up the driver shim SSL certificates:

*Table A-2* Driver Shim Command Line Options for Setting Up SSL Certificates

| Option (Short and Long Forms) | Description |
| -s  -secure | Secures the driver by creating SSL certificates, then exits. |
| -p  -password | Specifies the Remote Loader password. |

## A.3.2 Other Options

*Table A-3* Other Driver Shim Command Line Options

| Option (Short and Long Forms) | Description |
| -c <congFile>  -config <configFile> | Instructs the driver shim to read options from the specified configuration file.  Options are read from ddname DRVCONF by default. |
| -?  -help | Displays the command line options, then exits. |
| -v  -version | Displays the driver shim version and build date, then exits. |
