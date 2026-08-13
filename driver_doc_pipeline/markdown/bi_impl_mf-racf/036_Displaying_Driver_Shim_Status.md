# 7.4 Displaying Driver Shim Status

To see status, version and statistic information for the driver shim, issue the following operator command:

```
  MODIFY RACFDRV,APPL=STATUS
```

You can use the LDXSERV TSO command to display information about the Publisher channel event subsystem. Enter the following TSO command:

```
  LDXSERV STATUS
```

To use the LDXSERV command, you must include the driver load library in your STEPLIB concatenation.
