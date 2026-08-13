# B.0 Trace Levels

The driver supports the following trace levels:

*Table B-1* Supported Trace Levels

| Level | Description |
| 0 | No debugging |
| 1-3 | Identity Manager messages. Higher trace levels provide more detail. |
| 4 | Previous level plus Remote Loader, driver, driver shim, and driver connection messages, driver parameters, driver security, driver schema, request and response XML. |

For information about setting driver trace levels, see "[Viewing Identity Manager Processes](../../../identity-manager-48/driver_admin/data/b1rc1vm.html#b1rc1vm)" in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).

#### Oracle EBS Trace and Logging

You can enable trace and logging in the Oracle User Management, HR, or TCA modules. For example, to enable trace in the User Management module,

1. Log in to the Oracle EBS system with an administrator role.
2. Go to System Administrator > Security:User > Define window.
3. Click Help > Diagnostics > Trace, then select one of the following options:

   * No TraceRegular TraceTrace with BindsTrace with WaitsTrace with Binds and Waits
   * PL/SQL Profiling

To disable the trace, click No Trace.

To enable logging in the User Management module,

1. Log in to the Oracle EBS system with an administrator role.
2. Go to System Administrator > Security:User > Define window.
3. Click Help > Diagnostics > Logging > Preferences.

   A screen like this appears:

   ![](../graphics/oracle_umlogscreen_a.png)
