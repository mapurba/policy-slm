# 7.2 Obtaining Debugging Output

Identity Manager Fan-Out Driver components support the option to produce extensive debugging output. Although this output is intended primarily for use by NetIQ Technical Support, you might find it useful for your own troubleshooting efforts.

Because debugging mode adversely affects performance, it should not be used for routine operations.

## 7.2.1 Debugging the Core Driver

Individual debug options can be used to get detailed debugging information from very specific driver routines. Several of these options may already be covered by the trace level selected in fanout.conf. When changing these debug options, restarting the driver shim will reset them.

To obtain debugging output for the Core Driver:

1. Specify the destination for debugging information by setting the Debug Log File and Debug to DSTrace configuration parameters as desired.

   For more information, see [Driver Object Configuration Parameters](br3n4tb.html#cegdedii).
2. Specify the debugging information to be produced.

   1. In iManager, click Fan-Out Driver Configuration > Configure Logs. The Log Configuration page is displayed.
   2. Select the Core Driver components you want debugging information for.
   3. Click Apply.

It may be more convenient to obtain debugging using a command-line option. In some cases, it may be the only way to obtain debugging. To obtain debugging output for the Core Driver, via command-line:

1. Turn on debugging:

   ```
   /usr/local/ASAM/bin/CoreDriver/asamcdrv debug
   ```
2. Turn off debugging:

   ```
   /usr/local/ASAM/bin/CoreDriver/asamcdrv nodebug
   ```

*NOTE:*If LDAP client libraries are not in your executable path, you may need to export LD\_LIBRARY\_PATH=/opt/novell/eDirectory/lib64
