# 6.4 Shared Memory Errors

Shared memory is used by the driver shim to safely and securely communicate with the scripts on Linux. If the system shared memory segments become unusable, you must shut down the process and fix the shared memory segments.

Shared memory segments can become unusable on some Linux systems if the driver shim is improperly terminated without detaching from the segments. For information about how to properly stop the driver shim, see [Section 5.0, Managing the Driver](b3r8tx2.html). You can use the ipcs system tool to locate these segments and the ipcrm tool to manually clear them as shown in the following example:

```
> ipcs -m
------ Shared Memory Segments --------
key        shmid    owner     perms     bytes    nattch    status
0x2a065bbd 1802241  root      600       16384    1
> ipcrm -m 1802241
```

The driver shim generates default segments of 16384 bytes with permissions at 600.
