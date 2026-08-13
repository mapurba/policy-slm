# 6.2 The Driver Shim Configuration File

The driver shim configuration file controls operation of the driver shim.

The default driver shim configuration file is in the IFS /etc directory. So that the exit programs can find the file, its name is the lowercased name of the driver library. For example, if you installed the driver shim into the I5OSDRV library, the configuration file is /etc/i5osdrv.conf.

You can specify the configuration options listed in [Table 6-5](b4baik6.html#b4572iu), one per line.

*Table 6-5* Driver Shim Configuration File Statements

| Option (Short and Long Forms) | Description |
| -conn <connString>  -connection <connString> | A string with connection options. Enclose the string in double quotes ("). If you specify more than one option, separate the options with spaces.   * port=<driverShimPort> * ca=<Certificate Authority Key File> |
| -i5oslibrary <libraryName> | Specifies the library name where the driver shim is installed. The default is I5OSDRV. |
| -path <driverPath> | Specifies the IFS path for driver files. The default path is /usr/local/i5osdrv. |
| -t <traceLevel>  -trace <traceLevel> | Sets the level of debug tracing. 0 is no tracing, and 10 is all tracing. For details, see [The Trace File](b3xzdtn.html#b3xzpa5).  The output file location is specified by the tracefile option. |
| -tf <fileName>  -tracefile <fileName> | Sets the trace file location.  The default is logs/trace.log in the driver IFS path. |
| -tfm size  -tracefilemax size | Specifies the limit to the size of the trace file for this instance. Specify the value in kilobytes, megabytes, or gigabytes, using the abbreviation for the byte type. The minimum value is 100K. For example:  * -tracefilemax 1000K * -tracefilemax 100M * -tracefilemax 10G  *NOTE:*  * When you add this option to the configuration file, the application uses the specified name for the tracefile and includes up to 9 “roll-over” files. Each file size is 1/10th of the total size specified. The roll-over files are named using the base of the main trace filename plus \_n, where n is 1 through 9. * If the trace file data is larger than the specified maximum when the Driver Shim is started, the trace file data remains larger than the specified maximum until roll-over is completed through all 10 files. |

#### Example Driver Shim Configuration File

```
-tracefile /usr/local/i5osdrv/logs/trace.log
-trace 0
-tracefilemax 100M
-connection "ca=/usr/local/i5osdrv/keys/ca.pem port=8090"
-path /usr/local/i5osdrv/
```
