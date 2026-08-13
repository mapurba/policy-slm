# C.4 Driver Shim Library and IFS Contents

* [Driver Library](b4ab5n6.html#b4udkdt)
* [Driver IFS Path](b4ab5n6.html#b4udkuz)
* [Driver Shim Configuration File](b4ab5n6.html#b4bb81a)

## C.4.1 Driver Library

The default name for the driver library is I5OSDRV. The driver library contains the following objects:

* Driver shim program and commands
* CL program source and bound programs
* User space
* Menu
* Job description

## C.4.2 Driver IFS Path

The default driver IFS path is /usr/local/i5osdrv. The driver IFS path contains the following directories:

*Table C-2* IFS Path Directories

| Directory | Description |
| changelog | Holds event information until it is sent to the Metadirectory engine |
| conf | Contains the include/exclude file |
| keys | Contains the Driver object password, the Remote Loader password, and SSL certificate information |
| logs | Contains trace and log files |
| loopback | Contains information used by the scriptable framework for loopback detection |
| schema | Contains connected system schema information |
| snapshot | Holds information about the state of users and groups used to complete change event descriptions |

## C.4.3 Driver Shim Configuration File

The default driver shim configuration file is in the IFS /etc directory. So that the exit programs can find the file, its name is the lowercased name of the driver library. For example, if you installed the driver shim into the I5OSDRV library, the configuration file is /etc/i5osdrv.conf.
