# D.2 Message Destination

Audit Services maintains the Operational Logs and Audit Logs for the Core Driver in the logs directory. You can use the Web interface to view these logs.

Other log messages are handled depending on the system as follows.

## D.2.1 Linux and UNIX

System messages written by the Core Driver, and all messages written by the Linux/UNIX Platform Services Process and Platform Receiver, are written using the SYSLOG facility specified by the SYSLOGFACILITY statement of their respective configuration files.

The severity code of each message is used to determine the priority as follows.

*Table D-2* Linux/UNIX Message Destination by Severity Code

| Severity | Priority |
| Debugging | LOG\_DEBUG |
| Informational | LOG\_INFO |
| Warning | LOG\_WARNING |
| Error | LOG\_ERR |

## D.2.2 Windows

System messages written by the Core Driver are written to the Windows Application Log.
