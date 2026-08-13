# C.7 Files and Directories Modified by Installing the Driver Shim

Topics in this section include

* [Main Driver Shim Files](b4ab5n6.html#b4ab5xj)
* [Driver PAM Files](b4ab5n6.html#b4abagx)
* [Driver LAM Files](b4ab5n6.html#b4abdc9)

## C.7.1 Main Driver Shim Files

Main driver ship files include the following:

* [Driver Shim Directory](b4ab5n6.html#b4bb6lz)
* [/usr/sbin Files](b4ab5n6.html#b4bb74u)
* [init.d Files](b4ab5n6.html#b4bb7iv)
* [Man Pages](b4ab5n6.html#b4bb7sq)
* [Driver Shim Configuration File](b4ab5n6.html#b4bb81a)

### Driver Shim Directory

When you install the driver, the /usr/local/nxdrv directory is created and populated with driver-related files and subdirectories.

### /usr/sbin Files

The following commands are added to /usr/sbin:

*Table C-5* Driver Commands Placed in /usr/sbin

| Command | Function |
| nxdrv-uninstall | Uninstalls the Linux and UNIX driver |
| nxdrv-config | Updates the configuration |

### init.d Files

Commands to start, stop, and display the status of the driver are added to the appropriate file for the connected system operating system.

*Table C-6* Commands for Starting, Stopping, and Displaying the Status of the Driver Shim

| Operating System | Command |
| AIX | /etc/rc.d/init.d/nxdrvd |
| HP-UX | /sbin/init.d/nxdrvd |
| Linux | /etc/init.d/nxdrvd |
| Solaris | /etc/init.d/nxdrvd |

### Man Pages

The installation process adds man pages for the driver shim, change log update command, and shared memory tool to /usr/man.

### Driver Shim Configuration File

The installation program places a default driver shim configuration file at /etc/nxdrv.conf.

## C.7.2 Driver PAM Files

The driver installation script adds the driver PAM module to the appropriate library, and adds a line to the PAM configuration file for the pam-password function. The location of these depends on the operating system used by the connected system. For details, see [Table C-3, PAM Modules](b3yj5z9.html#b465rmb) and your operating system’s PAM documentation.

## C.7.3 Driver LAM Files

The installation script installs the LAM module NXDRV into the /usr/lib/security directory of the connected AIX system, and adds an NXDRV stanza to /usr/lib/security/methods.cfg.
