# A.1 Driver Status and Diagnostic Files

There are several log files that you can view to examine driver operation.

* [The System Log](b3xzdtn.html#b3xzhok)
* [The Trace File](b3xzdtn.html#b3xzpa5)
* [The REXX Exec Output File](b3xzdtn.html#b3ye15d)
* [DSTRACE](b3xzdtn.html#b3ye3ty)
* [The Status Log](b3xzdtn.html#b3yeaix)
* [The Operational Log](b3xzdtn.html#b6aqg60)
* [Change Log Started Task Message Log](b3xzdtn.html#b6m584r)

## A.1.1 The System Log

SYSLOG is used by the driver shim to record urgent, informational, and debug messages. Examining these should be foremost in your troubleshooting efforts. For detailed message documentation, see [Section B.0, System and Error Messages](b3r8v2p.html).

## A.1.2 The Trace File

The default trace file exists on the connected system at /opt/novell/tsdrv/logs/trace.log. A large amount of debug information can be written to this file. Use the trace level setting in the driver shim configuration file to control what is written to the file. For details about the driver shim configuration file, see [The Driver Shim Configuration File](b4baik6.html).

*Table A-1* Driver Shim Trace Levels

| Trace Level | Description |
| 0 | No debugging. |
| 1–3 | Identity Manager messages. Higher trace levels provide more detail. |
| 4 | Previous level plus Remote Loader, driver, driver shim, and driver connection messages. |
| 5–7 | Previous level plus change log and loopback messages. Higher trace levels provide more detail. |
| 8 | Previous level plus driver status log, driver parameters, driver security, driver Web server, driver schema, driver encryption, and driver include/exclude file messages. |
| 9 | Previous level plus low-level networking and operating system messages. |
| 10 | Previous level plus maximum low-level program details (all options). |

The following is an example the driver shim configuration file line to set the trace level:

```
-trace 9
```

To view the trace file:

1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
2. Authenticate by using any user name and the password that you specified as the Remote Loader password.
3. Click Trace.

## A.1.3 The REXX Exec Output File

Output from the REXX execs is written to DDNAME SYSTSPRT of the driver shim started task. This file captures the standard error output from all execs executed by the driver shim.

## A.1.4 DSTRACE

You can view Identity Manager information using the DSTRACE facility on the Metadirectory server. Use iManager to set the tracing level. For example, trace level 2 shows Identity Vault events in XML documents, and trace level 5 shows the results of policy execution. Because a high volume of trace output is produced, we recommend that you capture the trace output to a file. For details about using DSTRACE, see the NetIQ® Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## A.1.5 The Status Log

The status log is a condensed summary of the events that have been recorded on the Subscriber and Publisher channels. This file exists on the connected system at /opt/novell/tsdrv/logs/dirxml.log. You can also view the status log in iManager on the Driver Overview page. You can change the log level to specify what types of events to log. For details about using the status log, see the NetIQ Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

To view the status log:

1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
2. Authenticate by using any user name and the password that you specified as the Remote Loader password.
3. Click Status.

## A.1.6 The Operational Log

The operational log contains both important and informational messages that indicate the operational status of the driver shim. These messages indicate items that are not urgent enough to warrant operator response, but useful for tracking the progress of the driver. The location of the operational log is specified by the DRVLOG DD statement in the driver shim started task JCL.

## A.1.7 Change Log Started Task Message Log

The change log started task writes important and informational messages to DDNAME SYSPRINT.
