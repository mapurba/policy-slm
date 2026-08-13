# 7.0 Troubleshooting

Viewing driver processes is necessary to analyze unexpected behavior. To view the driver processing events, use DSTrace. You should only use it during testing and troubleshooting the driver. Running DSTrace while the drivers are in production increases the utilization on the Identity Manager server and can cause events to process very slowly.

The driver supports the following six trace levels:

| Level | Description |
| 0 | Minimal tracing such as JMS Driver version, Build Stamp, and XDS Library |
| 1 | Information on connection |
| 2 | Information on messages |
| 3 | Verbose information on the messages that are sent or received, and the GUIDs |
| 4 | Information on JNDI session, context, and connection |
| 5 | Information on the methods and its signatures |

For information about configuring the driver to use DSTrace, see "[Viewing Identity Manager Processes](../../../identity-manager-48/driver_admin/data/b1rc1vm.html#b1rc1vm)" in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).
