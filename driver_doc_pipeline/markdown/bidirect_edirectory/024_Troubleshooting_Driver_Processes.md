# 9.1 Troubleshooting Driver Processes

Viewing driver processes is necessary to analyze unexpected behavior. To view the driver processing events, use DSTrace. You should only use it during testing and troubleshooting the driver. Running DSTrace while the drivers are in production increases the utilization on the Identity Manager server and can cause events to process very slowly. For more information, see "[Viewing Identity Manager Processes](../../../identity-manager-48/driver_admin/data/b1rc1vm.html#b1rc1vm)" in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

For more information about generating trace levels, see [Change-log Trace Level](driver-configuration.html#bwcsgfd).

The following articles provide more information about the Identity Manager trace:

* [Capturing and Reading NetIQ Identity Manager Traces](http://www.novell.com/communities/node/5681/capturing-and-reading-novell-identity-manager-traces)
* [Comprehending NetIQ Identity Manager Traces - Part 1](http://www.novell.com/communities/node/9677/comprehending-idm-traces-part-1)
* [Comprehending NetIQ Identity Manager Traces - Part 2](http://www.novell.com/communities/node/11166/comprehending-idm-traces-part-2)
