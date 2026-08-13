# 5.2 The Driver Shim Configuration File

The driver shim configuration file controls operation of the driver shim. You can specify the configuration options listed in [Table 5-4](b4baik6.html#b4572iu), one per line. You can also specify these options on the command line. For details about driver shim command line values, see [Driver Shim Command Line Options](b3yj43k.html).

The driver shim configuration file must be a sequential file or a member of a partitioned data set. The DRVCONF DD statement in the driver shim started task JCL identifies the driver shim configuration file. An example driver shim configuration file is provided in the driver samples library member DRVCONF.

*Table 5-4* Driver Shim Configuration File Statements

| Option (Short and Long Forms) | Description |
| -conn <connString>  -connection <connString> | A string with connection options. Enclose the string in double quotes ("). If you specify more than one option, separate the options with spaces.   * port=<driverShimPort> * ca=<Certificate Authority Key File> |
| -hp <httpPort>  -httpport <httpPort> | Specifies the HTTP services port number. The default HTTP services port number is 8091.  You can connect to this port to view log files. For details, see [The Trace File](b3xzdtn.html#b3xzpa5) and [The Status Log](b3xzdtn.html#b3yeaix). |
| -path <driverPath> | Specifies the path for driver files. The default path is /opt/novell/tsdrv. |
| -sp <RLpassword>,<DOpassword>,  -setpassword <RLpassword>,<DOpassword>, | Sets the Remote Loader and Driver object passwords. |
| -t <traceLevel>  -trace <traceLevel> | Sets the level of debug tracing. 0 is no tracing, and 10 is all tracing. For details, see [The Trace File](b3xzdtn.html#b3xzpa5).  The output file location is specified by the tracefile option. |
| -tf <fileName>  -tracefile <fileName> | Sets the trace file location.  The default is /opt/novell/tsdrv/logs/trace.log. |
| -tfm size  -tracefilemax size | Specifies the limit to the size of the trace file for this instance. Specify the value in kilobytes, megabytes, or gigabytes, using the abbreviation for the byte type. The minimum value is 100K. For example:  * -tracefilemax 1000K * -tracefilemax 100M * -tracefilemax 10G  *NOTE:*  * When you add this option to the configuration file, the application uses the specified name for the tracefile and includes up to 9 “roll-over” files. Each file size is 1/10th of the total size specified. The roll-over files are named using the base of the main trace filename plus \_n, where n is 1 through 9. * If the trace file data is larger than the specified maximum when the Driver Shim is started, the trace file data remains larger than the specified maximum until roll-over is completed through all 10 files. |

#### Example Driver Shim Configuration File

```
-tracefile /opt/novell/tsdrv/logs/trace.log
-tracefilemax 100M
-trace 3
-connection "ca=/opt/novell/tsdrv/keys/ca.pem"
-path /opt/novell/tsdrv/
```
