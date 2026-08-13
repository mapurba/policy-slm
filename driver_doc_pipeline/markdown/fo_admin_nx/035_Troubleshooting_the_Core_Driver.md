# 7.0 Troubleshooting the Core Driver

NetIQ® Identity Manager Fan-Out Driver components record messages to their Audit Log, Operational Log, and their host system log. Examining these should be foremost in your troubleshooting efforts.

The Audit and Operational logs of Core Driver components are maintained in their logs directory.

By its very nature, the Fan-Out Driver is highly dependent upon the proper operation of your network and NetIQ eDirectory™. If you are having problems with the driver, ensure that the various driver components are able to communicate with one another, and that eDirectory is functioning properly.

For information pertaining to performance issues, see [Configuration and Performance Guidelines](babdhgie.html).

*IMPORTANT:*Make sure that you upgrade the Identity Manager Fan-Out Driver, including all of your platforms, when new versions or support packs become available.
