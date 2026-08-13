# D.4 Files and Directories Modified by Installing the Driver Shim

* [Driver Shim Directory](b8nrgni.html#b8nrhfi)
* [/usr/sbin Files (Linux/UNIX only)](b8nrgni.html#b8nri48)
* [init.d Files (Linux/UNIX only)](b8nrgni.html#b8nrixq)
* [Man Pages (Linux/UNIX only)](b8nrgni.html#b8nrk6j)
* [Driver Shim Configuration File](b8nrgni.html#b8nrkf1)
* [Windows Support Files (Windows only)](b8nrgni.html#b8nrkn8)

## D.4.1 Driver Shim Directory

When you install the driver, the /opt/novell/usdrv or C:\Program Files\Novell\WSDriver directory is created and populated with driver-related files and subdirectories.

## D.4.2 /usr/sbin Files (Linux/UNIX only)

The following commands are added to /usr/sbin:

*Table D-4* Driver Commands Placed in /usr/sbin

| Command | Function |
| usdrv-uninstall | Uninstalls the Scripting driver |
| usdrv-config | Updates the configuration |

## D.4.3 init.d Files (Linux/UNIX only)

Commands to start, stop, and display the status of the driver are added to the appropriate file for the connected system operating system.

*Table D-5* Commands for Starting, Stopping, and Displaying the Status of the Driver Shim

| Operating System | Command |
| AIX | /etc/rc.d/init.d/usdrvd |
| HP-UX | /sbin/init.d/usdrvd |
| Linux | /etc/init.d/usdrvd |
| Solaris | /etc/init.d/usdrvd |

## D.4.4 Man Pages (Linux/UNIX only)

The installation process adds man pages for the driver shim, change log update command, and shared memory tool to /usr/man.

## D.4.5 Driver Shim Configuration File

The installation program places a default driver shim configuration file at /etc/usdrv.conf on Linux and UNIX. On Windows, this file is wsdrv.conf in the conf directory in the installation directory.

## D.4.6 Windows Support Files (Windows only)

Support files such as DLLs for the Visual C++ runtime are installed on Windows systems in the WinSxS directory (usually C:\Windows\WinSxS). If the driver shim is uninstalled, these files are removed.
