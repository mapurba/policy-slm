# 6.6 Trace Levels

To see debugging output from the driver, add a DirXML-DriverTraceLevel attribute value from 1 to 7 on the driver set containing the driver instance. This attribute is commonly confused with the DirXML-XSL TraceLevel attribute. For more information on driver set trace levels, refer to "[Viewing Identity Manager Processes](../../../identity-manager-48/driver_admin/data/b1rc1vm.html#b1rc1vm)" in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

The driver supports the following seven trace levels:

*Table 6-63* Supported Trace Levels

| Level | Description |
| 1 | Minimal tracing |
| 2 | Database properties |
| 3 | Connection status, SQL statements, event log records |
| 4 | Verbose output |
| 5 | Database resource allocation/deallocation; state file contents |
| 6 | JDBC API (invoked methods, passed arguments, returned values, etc.) |
| 7 | Third-party driver |

Levels 6 and 7 are particularly useful for debugging third-party drivers.
