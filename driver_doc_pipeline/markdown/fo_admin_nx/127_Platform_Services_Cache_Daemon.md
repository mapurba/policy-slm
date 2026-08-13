# B.7 Platform Services Cache Daemon

The Platform Services Cache Daemon provides Account information for account redirection. It establishes and maintains a connection to the Core Driver and synchronizes Posix profile and password information from eDirectoryÂ® to a local memory cache.The Platform Services Cache Daemon must be running if you plan to use Account Redirection through the Name Service Switch on the platform.

## B.7.1 Platform Services Process Command Line Parameters

*Table B-5* Platform Services Process Command Line Parameters

| Option | Argument | Explanation |
| -a | Configuration File Path | Specifies the platform configuration file to use. |

## B.7.2 Maintaining Files Used by the Platform Services Process

This involves three types of files.

### The Platform Configuration File

The Platform Services Cache Daemon reads the platform configuration file to locate Core Drivers and to find other configuration information. For details about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html).

### Log Files

The Linux/UNIX Platform Services Cache Daemon writes messages to log files in the SYSLOG facility specified by the SYSLOGFACILITY statement in the platform configuration file. Log messages are documented in the Messages Reference.

### Permanent Cache File

The Linux/UNIX Platform Services Cache Daemon writes the memory cache to a protected, encrypted file on the local file system in the /usr/local/ASAM/data/PlatformServices/certs directory. This file is written upon shutdown and read upon startup in order to provide quick retrieval of account information without having to synchronize with eDirectory upon every startup.
