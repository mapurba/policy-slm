# 2.2 Installing JDBC Driver Jar Files

To communicate with the JDBC database, the JDBC driver requires that you copy the appropriate JDBC driver jar files to the driver location.

1. Locate the appropriate JDBC driver jar files.

   Information about the jar files you need and where to download them from is found in [Supported Third-Party JDBC Drivers (Recommended)](supported-third-party-jdbc-drivers.html).
2. Place the files in the appropriate location.

   The following tables identify the paths where you need to place JDBC driver jar files on a Identity Manager server or on a Remote Loader server that is running the JDBC driver.

   *Table 2-1* Locations for JAR Files: Identity Manager Server

   | Platform | Directory Path |
   | Solaris, Linux, or AIX | /opt/novell/eDirectory/lib/dirxml/classes |
   | Windows | novell\NDS\lib |

   *Table 2-2* Locations for JAR Files: Remote Loader

   | Platform | Directory Path |
   | Solaris, Linux, or AIX | /opt/novell/eDirectory/lib/dirxml/classes |
   | Windows | novell\RemoteLoader\lib |
