# 4.2 The Driver Shim Configuration File

The driver shim configuration file controls operation of the driver shim. The location and name of the file is dependent on the operating system:

* Windows: wsdrv.conf in the conf directory in your installation directory.
* Linux or UNIX: /etc/usdrv.conf

A default configuration file is created at installation time.

You can specify the configuration options listed in [Table 4-5](b8mqqe6.html#b8mqrjx), one per line. You can also specify these options on the driver shim command line. For details about driver shim command line options, see [Driver Shim Command Line Options](b8nrawu.html).

*Table 4-5* Driver Shim Configuration File Statements

| Option (Short and Long Forms) | Description |
| -conn connString  -connection connString | A string with connection options. Enclose the string in double quotes ("). If you specify more than one option, separate the options with spaces.  port=driverShimPort  ca=Certificate Authority Key File |
| -hp httpPort  -httpport httpPort | Specifies the HTTP services port number. The default HTTP services port number is 8091.  You can connect to this port to view log files. For details, see [Driver Status and Diagnostic Files](b8nnry9.html). |
| -path driverPath | Specifies the path for driver files. The default path is /usr/local/nxdrv. |
| -t traceLevel  -trace traceLevel | Sets the level of debug tracing. 0 is no tracing, and 10 is all tracing. For details, see [Driver Status and Diagnostic Files](b8nnry9.html).  The output file location is specified by the tracefile option. |
| -tf fileName  -tracefile fileName | Sets the trace file location.  Windows default file: C:\Progra~1\Novell\WSDriver\logs\trace.log  Linux/UNIX default file: /opt/novell/usdrv/logs/trace.log. |
| -tfm size  -tracefilemax size | Specifies the limit to the size of the trace file for this instance. Specify the value in kilobytes, megabytes, or gigabytes, using the abbreviation for the byte type. The minimum value is 100K. For example:  * -tracefilemax 1000K * -tracefilemax 100M * -tracefilemax 10G  *NOTE:*  * When you add this option to the configuration file, the application uses the specified name for the tracefile and includes up to 9 “roll-over” files. Each file size is 1/10th of the total size specified. The roll-over files are named using the base of the main trace filename plus \_n, where n is 1 through 9. * If the trace file data is larger than the specified maximum when the Driver Shim is started, the trace file data remains larger than the specified maximum until roll-over is completed through all 10 files. |

#### Example Configuration File

```
-tracefile /opt/novell/usdrv/logs/trace.log
-trace 0
-tracefilemax 100M
-connection "ca=/opt/novell/usdrv/keys/ca.pem port=8090"
-httpport 8091
-path /opt/novell/usdrv/
```
