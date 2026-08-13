# A.1 Driver Status and Diagnostic Files

There are several log files that you can view to examine driver operation.

* [The Job Log](b3xzdtn.html#b3xzhok)
* [The Trace File](b3xzdtn.html#b3xzpa5)
* [CL Program Output](b3xzdtn.html#b3ye15d)
* [DSTRACE](b3xzdtn.html#b3ye3ty)
* [The Status Log](b3xzdtn.html#b3yeaix)

## A.1.1 The Job Log

The job log is used by the driver shim to provide urgent, informational, and debug messages. These messages come from the driver shim and from CL programs called by the driver shim to process events. Examining these should be foremost in your troubleshooting efforts.

Use the DSPJOBLOG command or IBM i Navigator to view the job log.

For detailed message documentation, see [Section B.0, System and Error Messages](b3r8v2p.html).

## A.1.2 The Trace File

The default trace file exists on the connected i5/OS system in the driver IFS path at logs/trace.log. A large amount of debug information can be written to this file. Use the trace level setting in the driver shim configuration file to control what is written to the file. For details, see [The Driver Shim Configuration File](b4baik6.html).

*Table A-1* Driver Shim Trace Levels

| Trace Level | Description |
| 0 | No debugging. |
| 1–3 | Identity Manager messages. Higher trace levels provide more detail. |
| 4 | Previous level plus CL program, Remote Loader, driver, driver shim, and driver connection messages. |
| 5–7 | Previous level plus change log and loopback messages. Higher trace levels provide more detail. |
| 8 | Previous level plus driver status log, driver parameters, driver command line, driver security, driver Web server, driver schema, driver encryption, and driver include/exclude file messages. |
| 9 | Previous level plus low-level networking and operating system messages. |
| 10 | Previous level plus maximum low-level program details (all options). |

The following is an example configuration file line to set the trace level:

```
-trace 9
```

## A.1.3 CL Program Output

Output from the CL programs is written to the job log. Use the DSPJOBLOG command or i5/OS Navigator to view the job log.

If the trace level is set to at least 4, CL program output is also written to the trace file. For details about the trace file and trace levels, see [The Trace File](b3xzdtn.html#b3xzpa5).

## A.1.4 DSTRACE

You can view Identity Manager information using the DSTRACE facility on the Metadirectory server. Use iManager to set the tracing level. For example, trace level 2 shows Identity Vault events in XML documents, and trace level 5 shows the results of policy execution. Because a high volume of trace output is produced, we recommend that you capture the trace output to a file. For details about using DSTRACE, see the NetIQ® Identity Manager Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## A.1.5 The Status Log

The status log is a condensed summary of the events that have been recorded on the Subscriber and Publisher channels. This file exists on the connected system in the driver IFS path at logs/dirxml.log. You can also view the status log in iManager on the Driver Overview page. You can change the log level to specify what types of events to log. For details about using the status log, see the NetIQ Identity Manager Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
