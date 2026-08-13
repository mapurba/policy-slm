# 13.0 Troubleshooting Platform Services

NetIQ® Identity Manager Fan-Out Driver components record messages to their Audit Log, Operational Log, and their host system log. Examining these should be foremost in your troubleshooting efforts.

The Audit and Operational logs of Core Driver components are maintained in their logs directory.

The Linux/UNIX Platform Services Process and Platform Receiver write log messages to the Linux/UNIX SYSLOG facility.

By its very nature, the Identity Manager Fan-Out Driver is highly dependent upon the proper operation of your network and eDirectory™. If you are having problems with the driver, ensure that the various driver components are able to communicate with one another and that eDirectory is functioning properly.

For information pertaining to Identity Manager Fan-Out Driver performance issues, see [Section 4.0, Core Driver Planning](babheghf.html).

*IMPORTANT:*Make sure you upgrade the driver, including all of your platforms, when new versions or support packs become available.
