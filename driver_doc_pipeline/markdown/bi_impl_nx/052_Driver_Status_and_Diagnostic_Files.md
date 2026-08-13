# A.1 Driver Status and Diagnostic Files

There are several log files that you can view to examine driver operation.

* [The System Log](b3xzdtn.html#b3xzhok)
* [The Trace File](b3xzdtn.html#b3xzpa5)
* [The Script Output File](b3xzdtn.html#b3ye15d)
* [DSTRACE](b3xzdtn.html#b3ye3ty)
* [The Status Log](b3xzdtn.html#b3yeaix)
* [The PAM Trace File](b3xzdtn.html#b3yecj2)

## A.1.1 The System Log

The system log is used by the driver shim to record urgent, informational, and debug messages. Examining these should be foremost in your troubleshooting efforts. For detailed message documentation, see [Section B.0, System and Error Messages](b3r8v2p.html).

The location for the system log varies from system to system and is generally configured through /etc/syslog.conf. The amount of information that is logged by the driver can also be configured through this system log configuration file. The following is a sample fragment from /etc/syslog.conf:

```
# sample /etc/syslog.conf
#
*.err;kern.notice;auth.notice                   /dev/sysmsg
*.err;kern.debug;daemon.notice;mail.crit        /var/adm/messages

*.alert;kern.err;daemon.err                     operator
*.alert                                         root
```

The options in the first column determine which messages are logged. The options in the second column specify the destination file or user to send the log output to. For example, specifying \*.err logs all messages with a priority of err or above. For more information about syslog priorities, view your system documentation using the man syslog command.

Messages from the Linux and UNIX driver shim and messages from the scripts are logged with various priorities as shown in [Table A-1](b3xzdtn.html#b465vhf). The information that is recorded depends on your syslog configuration.

*Table A-1* Message Priorities

| Message Topic | Priority |
| Script being called | DEBUG |
| Successful Linux or UNIX command execution | INFO |
| Publication events | INFO |
| Failures | ERR |

## A.1.2 The Trace File

The default trace file exists on the connected Linux and UNIX system at /usr/local/nxdrv/logs/trace.log. A large amount of debug information can be written to this file. Use the trace level setting in /etc/nxdrv.conf to control what is written to the file. For details about /etc/nxdrv.conf, see [The Driver Shim Configuration File](b4baik6.html).

*Table A-2* Driver Shim Trace Levels

| Trace Level | Description |
| 0 | No debugging. |
| 1–3 | Identity Manager messages. Higher trace levels provide more detail. |
| 4 | Previous level plus Remote Loader, driver, driver shim, and driver connection messages. |
| 5–7 | Previous level plus change log and loopback messages. Higher trace levels provide more detail. |
| 8 | Previous level plus driver status log, driver parameters, driver command line, driver security, driver Web server, driver schema, driver encryption, driver PAM, driver SOAP API, and driver include/exclude file messages. |
| 9 | Previous level plus low-level networking and operating system messages. |
| 10 | Previous level plus maximum low-level program details (all options). |

The following is an example /etc/nxdrv.conf line to set the trace level:

```
-trace 9
```

To view the trace file:

1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
2. Authenticate by using any user name and the password that you specified as the Remote Loader password.
3. Click Trace.

## A.1.3 The Script Output File

By default, script output is written to /usr/local/nxdrv/logs/script-trace.log on the connected system. This file captures the standard error output from all scripts executed by the driver shim. The location of the script output file is set in the globals.sh script.

## A.1.4 DSTRACE

You can view Identity Manager information using the DSTRACE facility on the Metadirectory server. Use iManager to set the tracing level. For example, trace level 2 shows Identity Vault events in XML documents, and trace level 5 shows the results of policy execution. Because a high volume of trace output is produced, we recommend that you capture the trace output to a file. For details about using DSTRACE, see the NetIQ® Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## A.1.5 The Status Log

The status log is a condensed summary of the events that have been recorded on the Subscriber and Publisher channels. This file exists on the connected system at /usr/local/nxdrv/logs/dirxml.log. You can also view the status log in iManager on the Driver Overview page. You can change the log level to specify what types of events to log. For details about using the status log, see the NetIQ Identity Manager 4.8 Administration Guide.

To view the status log:

1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
2. Authenticate by using any user name and the password that you specified as the Remote Loader password.
3. Click Status.

## A.1.6 The PAM Trace File

To log PAM trace messages to /usr/local/nxdrv/logs/pam\_nxdrv.log, specify the debug=\* command line option for the driver PAM module in your PAM configuration file. This file is implementation dependent. For details, see your system’s PAM documentation. For details about the driver PAM module command line options, see [Table C-4, Linux and UNIX Driver PAM Module Command Line Options](b3yj5z9.html#b4igolf).
