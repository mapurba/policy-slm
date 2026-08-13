# 6.2 Starting and Stopping the Driver Shim

To start the driver shim, perform the task appropriate for your operating system as shown in the following table:

*Table 6-1* Starting the Driver Shim

| Operating System | Command/Task |
| AIX | /etc/rc.d/init.d/usdrvd start |
| FreeBSD | /usr/local/etc/rc.d/usdrvd start |
| HP-UX | /sbin/init.d/usdrvd start |
| Linux | /etc/init.d/usdrvd start |
| OSX | /opt/novell/usdrv/startup/usdrvd start |
| Solaris | /etc/init.d/usdrvd start |
| Tru64 | /sbin/init.d/usdrvd start |
| Windows | Use the Windows Services application to start the NetIQ Identity Manager Windows Script Driver service. |

To stop the driver shim, perform the task appropriate for your operating system as shown in the following table:

*Table 6-2* Stopping the Driver Shim

| Operating System | Command/Task |
| AIX | /etc/rc.d/init.d/usdrvd stop |
| FreeBSD | /usr/local/etc/rc.d/usdrvd stop |
| HP-UX | /sbin/init.d/usdrvd stop |
| Linux | /etc/init.d/usdrvd stop |
| OSX | /opt/novell/usdrv/startup/usdrvd stop |
| Solaris | /etc/init.d/usdrvd stop |
| Tru64 | /etc/init.d/usdrvd stop |
| Windows | Use the Windows Services application to stop the NetIQ Identity Manager Windows Script Driver service. |

You can also run the driver shim on Windows from the command line by executing wsdriver.exe in the bin directory under the driver installation directory. Output is written to the console. Stop the driver shim by pressing Ctrl+Break. Running the driver shim this way is recommended only for development and testing.
