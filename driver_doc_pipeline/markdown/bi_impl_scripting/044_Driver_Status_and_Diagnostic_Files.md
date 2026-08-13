# A.1 Driver Status and Diagnostic Files

There are several log files that you can view to examine driver operation.

* [The System Log (Linux/UNIX only)](b8nnry9.html#b8nnsga)
* [The Trace File](b8nnry9.html#b8nnyqr)
* [The Script Output File](b8nnry9.html#b8no0ug)
* [DSTRACE](b8nnry9.html#b8no13k)
* [The Status Log](b8nnry9.html#b8no1bi)

## A.1.1 The System Log (Linux/UNIX only)

The system log is used by the Scripting driver shim to record urgent, informational, and debug messages. Examining these should be foremost in your troubleshooting efforts. For detailed message documentation, see [Section B.0, System and Error Messages](b8noakn.html).

The location for the system log varies from system to system and is generally configured through /etc/syslog.conf. The amount of information that is logged by the driver can also be configured through this system log configuration file. The following is a sample fragment from /etc/syslog.conf:

```
# sample /etc/syslog.conf
#
*.err;kern.notice;auth.notice                      /dev/sysmsg
*.err;kern.debug;daemon.notice;mail.crit          /var/adm/messages

*.alert;kern.err;daemon.err                        operator
*.alert                                            root
```

The options in the first column determine which messages are logged. The options in the second column specify the destination file or user to send the log output to. For example, specifying \*.err logs all messages with a priority of err or above. For more information about syslog priorities, view your system documentation using the man syslog command. Messages from the driver shim and messages from the scripts are logged with various priorities as shown in [Table A-1](b8nnry9.html#b8nnxoa). The information that is recorded depends on your syslog configuration.

*Table A-1* Message Priorities

| Message Topic | Priority |
| Script being called | DEBUG |
| Successful Linux or UNIX command execution | INFO |
| Publication events | INFO |
| Failures | ERR |

## A.1.2 The Trace File

The default trace file exists on the connected system as trace.log in the logs directory under the installation folder. A large amount of debug information can be written to this file. Use the trace level setting in your driver shim configuration file to control what is written to the file. For details about the driver shim configuration file, see [The Driver Shim Configuration File](b8mqqe6.html).

*Table A-2* Driver Shim Trace Levels

| Trace Level | Description |
| 0 | No debugging |
| 1–3 | Identity Manager messages. Higher trace levels provide more detail. |
| 4 | Previous level plus Remote Loader, driver, driver shim, and driver connection messages. |
| 5–7 | Previous level plus change log and loopback messages. Higher trace levels provide more detail. |
| 8 | Previous level plus driver status log, driver parameters, driver command line, driver security, driver Web server, driver schema, driver encryption, driver PAM, driver SOAP API, and driver include/exclude file messages. |
| 9 | Previous level plus low-level networking and operating system messages. |
| 10 | Previous level plus maximum low-level program details (all options). |

The following is an example configuration line to set the trace level:

```
-trace 9
```

To view the trace file:

1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
2. Authenticate by using any username and the password that you specified as the Remote Loader password.
3. Click Trace.

## A.1.3 The Script Output File

By default, script output is written to script-trace.log in the logs directory under the driver installation directory on the connected system. This file captures the output from all scripts executed by the driver shim. The location of the script output file is set in the driver parameters.

## A.1.4 DSTRACE

You can view Identity Manager information using the DSTRACE facility on the Metadirectory server. Use iManager to set the tracing level. For example, trace level 2 shows Identity Vault events in XML documents, and trace level 5 shows the results of policy execution. Because a high volume of trace output is produced, we recommend that you capture the trace output to a file. For details about using DSTRACE, see the Identity Manager Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## A.1.5 The Status Log

The status log is a condensed summary of the events that have been recorded on the Subscriber and Publisher channels. This file exists on the connected system as dirxml.log in the logs directory under the driver installation directory. You can also view the status log in iManager on the Driver Overview page. You can change the log level to specify what types of events to log. For details about using the status log, see the Identity Manager Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

To view the status log:

1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
2. Authenticate by using any username and the password that you specified as the Remote Loader password.
3. Click Status.
