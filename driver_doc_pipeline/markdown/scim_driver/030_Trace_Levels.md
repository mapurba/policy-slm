# B.0 Trace Levels

The driver supports the following trace levels:

*Table B-1* Supported Trace Levels

| Level | Description |
| 0 | Driver status messages. All warnings and failure status is captured. |
| 1 | Driver status and Driver initialization messages. The success, warnings and failure status are captured. |
| 2 | Previous levels plus all other error details. |
| 3 and 4 | Previous levels plus XDS to JSON parser processing details. |
| 5 | Previous level plus all configured debug messages. |
| 6 | Previous levels plus HTTPS request documents. |
| 7 | Previous levels plus HTTPS response documents. |

For information about setting driver trace levels, see "[Viewing Identity Manager Processes](../../../identity-manager-48/driver_admin/data/b1rc1vm.html#b1rc1vm)" in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).
