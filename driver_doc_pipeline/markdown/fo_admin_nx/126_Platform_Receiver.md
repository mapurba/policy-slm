# B.6 Platform Receiver

The Platform Receiver obtains provisioning events from Event Journal Services and calls the appropriate Receiver script to process the given type of event. For more information about Receiver scripts, see [Receiver Scripts](bbcjcgif.html#cjabcdif).

The Platform Receiver must be running if you plan to use Identity Provisioning on the platform.

## B.6.1 Platform Receiver Command Line Parameters

*Table B-4* Platform Receiver Command Line Parameters

| Option | Argument | Explanation |
| -a | Configuration File Path | Specifies the platform configuration file to use.  If you do not specify this option, the default is /usr/local/ASAM/data/asamplat.conf. |
| -i | None | The Platform Receiver uses Polling Mode. |
| -c | None | The Platform Receiver uses Check Mode. |
| -p | None | The Platform Receiver uses Persistent Mode. |
| -f | None | The Platform Receiver uses Full Sync Mode. |
| -r | None | The Platform Receiver uses Scheduled Mode. |
| -s | None | Obtain a security certificate for the Platform and end.  This is needed only during the initial configuration process. |

The following options determine the mode of operation for the Platform Receiver.: -i, -c, -p, -f, and -r. They are mutually exclusive. If none of them is present, the mode of operation specified by the RUNMODE statement in the platform configuration file is used. If there is no RUNMODE statement, the Platform Receiver uses Persistent Mode.

For more information, see [Modes of Operation](babdcabj.html#babfijbb).

## B.6.2 Maintaining Files Used by the Platform Receiver

This involves three types of files.

### The Platform Configuration File

The Platform Receiver reads the platform configuration file to locate the Core Driver, to determine which users and groups are managed using provisioning events, and to find other configuration information. For details about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html).

### Receiver Scripts

Receiver scripts for Linux/UNIX platforms are implemented as shell scripts. The Platform Receiver runs the Receiver scripts from ASAM/bin/PlatformServices/PlatformReceiver/scripts. The installation process stores the base scripts in subdirectories of the scripts directory. For information about Receiver scripts, see [Receiver Scripts](bbcjcgif.html#cjabcdif).

### Log Files

The Linux/UNIX Platform Receiver writes messages to log files in the SYSLOG facility specified by the SYSLOGFACILITY statement in the platform configuration file. Log messages are documented in the Messages Reference.
