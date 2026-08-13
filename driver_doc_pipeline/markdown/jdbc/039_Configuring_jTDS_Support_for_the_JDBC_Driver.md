# 6.8 Configuring jTDS Support for the JDBC Driver

The JDBC driver can be configured to support jTDS classes. The jTDS classes (jTDS jar files) improve the performance of the driver. The following table defines the set of databases and the driver classes that support the jTDS jar files:

| Database Name | Class Name | Connection URL | Jar File Name |
| MS SQL version 2000/2005 | net.sourceforge.jtds.jdbc.Driver | jdbc:jtds:sqlserver://<server>:<port1433>;DatabaseName=<database> | jtds-1.2.2.jar |
| Sybase | net.sourceforge.jtds.jdbc.Driver | jdbc:jtds:sybase://<server>:<port5000>;DatabaseName=<database> | jtds-1.2.2.jar |

Use the latest jTDS jar file available(jtds-1.2.2.jar).

Place the jar file in the specific directory path for the platform being used. For information on placing the jar files, refer to [Supported Third-Party Jar File Placement](supported-third-party-jdbc-drivers.html#b152m0b7).
