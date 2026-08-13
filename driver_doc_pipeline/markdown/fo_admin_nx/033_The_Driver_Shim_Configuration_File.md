# 6.6 The Driver Shim Configuration File

The driver shim configuration file /usr/local/ASAM/data/fanout.conf controls operation of the driver shim. You can specify the configuration options listed in [Table 6-2](b4baik6.html#b4572iu), one per line. You can also specify these options on the command line. For details about driver shim command line values, see [Driver Shim Command Line Options](b3yj43k.html).

*Table 6-2* Driver Shim Configuration File Statements

| Option (Short and Long Forms) | Description |
| -conn <connString>  -connection <connString> | A string with connection options. Enclose the string in double quotes ("). If you specify more than one option, separate the options with spaces.   * port=<driverShimPort> * ca=<Certificate Authority Key File> |
| -path <driverPath> | Specifies the path for driver files. The default path is /usr/local/ASAM. |
| -netinterface <ipaddress> | Specifies the ip address through which the driver listens for client requests. |
| -sp <RLpassword>,<DOpassword>,  -setpassword <RLpassword>,<DOpassword>, | Sets the Remote Loader and Driver object passwords. |
| -t <traceLevel>  -trace <traceLevel> | Sets the level of debug tracing. 0 is no tracing, and 10 is all tracing. For details, see [The Trace File](brm7yxe.html).  The output file location is specified by the tracefile option. |
| -tf <fileName>  -trace <traceLevel> | Sets the tracefile location.  The default is /usr/local/ASAM/logs/trace.log. |
| -tfm size  -tracefilemax size | Specifies the limit to the size of the trace file for this instance. Specify the value in kilobytes, megabytes, or gigabytes, using the abbreviation for the byte type. The minimum value is 100K. For example:  * -tracefilemax 1000K * -tracefilemax 100M * -tracefilemax 10G  *NOTE:*  * When you add this option to the configuration file, the application uses the specified name for the tracefile and includes up to 9 “roll-over” files. Each file size is 1/10th of the total size specified. The roll-over files are named using the base of the main trace filename plus \_n, where n is 1 through 9. * If the trace file data is larger than the specified maximum when the Driver Shim is started, the trace file data remains larger than the specified maximum until roll-over is completed through all 10 files. |
| -ndl  -nodirxmllog | Disables writing to the driver status log file.  Disables writing to dirxml.log. |

#### Example Driver Shim Configuration File

```
  -tracefile /usr/local/ASAM/debug.log
  -trace 0
  -tracefilemax 100M
  -connection "ca=/usr/local/ASAM/keys/ca.pem port=8090"
  -path /usr/local/ASAM/
```
