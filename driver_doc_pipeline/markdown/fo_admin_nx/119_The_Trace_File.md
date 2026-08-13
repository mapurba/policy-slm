# A.4 The Trace File

The default trace file exists on the connected Linux and UNIX system at /usr/local/ASAM/debug.log. A large amount of debug information can be written to this file. Use the trace level setting in /usr/local/ASAM/data/fanout.conf to control what is written to the file. For details about /usr/local/ASAM/data/fanout.conf, see [The Driver Shim Configuration File](b4baik6.html).

*Table A-4* Driver Shim Trace Levels

| Trace Level | Description |
| 0 | No debugging. |
| 1–3 | Identity Manager messages. Higher trace levels provide more detail. |
| 4 | Previous level plus Remote Loader, driver, driver shim, and driver connection messages. |
| 5–7 | Previous level plus change log and loopback messages. |
| 8 | Previous level plus driver status log, driver parameters, driver command line, driver security, driver Web server, driver schema, driver encryption, driver PAM, driver SOAP API, and driver include/exclude file messages. |
| 9 | Previous level plus low-level networking and operating system messages. |
| 10 | Previous level plus maximum low-level program details (all options). |

The following is an example /usr/local/ASAM/data/fanout.conf line to set the trace level:

```
-trace 9
```

To view the trace file:

1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
2. Authenticate by using any user name and the password that you specified as the Remote Loader password.
3. Click Trace.
