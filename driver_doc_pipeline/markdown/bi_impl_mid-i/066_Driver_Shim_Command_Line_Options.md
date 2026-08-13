# C.2 Driver Shim Command Line Options

The following options can be specified on the driver shim command line.

*Table C-1* Driver Shim Command Line Options

| Option | Description |
| CONFIG | Instructs the driver shim to read options from the specified configuration file.  Options are read from /etc/i5osdrv.conf by default. |
| CONNECTION | Specifies connection options.   * port=<driverShimPort> * ca=<Certificate Authority Key File> |
| TRACE | Sets the level of debug tracing. 0 is no tracing, and 10 is all tracing. For details, see [The Trace File](b3xzdtn.html#b3xzpa5).  The output file location is specified by the TRACEFILE option. |
| TRACEFILE | Sets the trace file location.  The default is logs/trace.log in the driver IFS path. |
| OPTION(\*SECURE) | Secures the driver by creating SSL certificates, then exits. |
| OPTION(\*SETPASS) | Sets the Remote Loader and Driver object passwords. |
| OPTION(\*VERSION) | Displays driver shim version information. |

The following is an example driver shim command line:

```
I5OSDRV/I5OSDRV CONFIG('/etc/i5osdrv.conf')
   CONNECTION('port=8090 ca=/usr/local/i5osdrv/keys/ca.pem')
   TRACEFILE('/tmp/trace.out')
   HTTPPORT(8888)
   TRACE(10)
```
