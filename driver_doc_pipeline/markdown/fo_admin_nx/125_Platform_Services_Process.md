# B.5 Platform Services Process

The Platform Services Process provides Authentication Services and the interface for the AS Client API. It establishes and maintains connections to Core Drivers and provides load balancing and failover among them.

The Platform Services Process must be running if you plan to use Authentication Services on the platform.

## B.5.1 Platform Services Process Command Line Parameters

*Table B-3* Platform Services Process Command Line Parameters

| Option | Argument | Explanation |
| -a | Configuration File Path | Specifies the platform configuration file to use.  If you do not specify this option, the default is /usr/local/ASAM/data/asamplat.conf. |
| -s | None | Obtain a security certificate for the Platform and end.  This is needed only during the initial configuration process. |

## B.5.2 Maintaining Files Used by the Platform Services Process

This involves two types of files.

### The Platform Configuration File

The Platform Services Process reads the platform configuration file to locate Core Drivers, to determine which users are authenticated using Authentication Services, and to find other configuration information. For details about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html).

### Log Files

The Linux/UNIX Platform Services Process writes messages to log files in the SYSLOG facility specified by the SYSLOGFACILITY statement in the platform configuration file. Log messages are documented in the Messages Reference.
