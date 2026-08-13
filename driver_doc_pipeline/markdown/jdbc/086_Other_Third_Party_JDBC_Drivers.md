# 14.6 Other Third-Party JDBC Drivers

This section lists an unsupported driver of interest (IBM Toolbox for Java/JTOpen) and discusses how to assess the feasibility of using unsupported third-party JDBC drivers with this product.

* [IBM Toolbox for Java/JTOpen](unsupported-third-party-jdbc-drivers.html#b4jmqff)
* [Minimum Third-Party JDBC Driver Requirements](unsupported-third-party-jdbc-drivers.html#b4jmj9j)
* [Considerations When Using Other Third-Party JDBC Drivers](unsupported-third-party-jdbc-drivers.html#b4jmjia)

## 14.6.1 IBM Toolbox for Java/JTOpen

*Table 14-33* Settings for IBM Toolbox for Java/JTOpen

| Database | IBM Toolbox for Java/JTOpen  * iSeries Toolbox for Java (alias) * AS/400 Toolbox for Java (alias) |
| Class Name | com.ibm.as400.access.AS400JDBCDriver |
| Type | 4 |
| URL Syntax | jdbc:as400://ip-address/database-name |
| Download Instructions | Download URLs for JTOpen  * [JTOpen](http://jt400.sourceforge.net) * [Toolbox for Java/JTOpen](http://www-03.ibm.com/servers/eserver/iseries/toolbox/downloads.html) |
| Filenames | jt400.jar |
| Documentation URLs | [Toolbox for Java/JTOpen](http://www-03.ibm.com/servers/eserver/iseries/toolbox/) |

If you use the IBM Toolbox for Java/JTOpen driver, you must manually enter values for the JDBC Driver Class Name and Authentication Context parameters. The settings are not automatically populated. See [Third-Party JDBC Driver Class Name](configure-jdbc-driver-specific-parameters.html#b1pu3j9) and [Authentication Context](jdbc-driver-parameters.html#bvqz35i).

## 14.6.2 Minimum Third-Party JDBC Driver Requirements

The JDBC driver might not interoperate with all third-party JDBC drivers. If you use an unsupported third-party JDBC driver, it must meet the following requirements:

* Support required metadata methods

  For a current list of the required and optional java.sql.DatabaseMetaData method calls that the JDBC driver makes, see [Section F.0, java.sql.DatabaseMetaData Methods](java-sql-databasemetadata-jdbc.html).
* Support other required JDBC methods

  For a list of required JDBC methods that the JDBC driver uses, refer to [Section G.0, JDBC Interface Methods](jdbc-interface-methods.html). You can use this list in collaboration with third-party driver documentation to identify potential incompatibilities.

## 14.6.3 Considerations When Using Other Third-Party JDBC Drivers

* Because the JDBC driver is directly dependent upon third-party JDBC driver implementations, bugs in those implementations might cause this product to malfunction.

  To assist you in debugging third-party JDBC drivers, the JDBC driver supports the following:

  + Tracing at the JDBC API level (level 6)
  + Third-party JDBC driver (level 7) tracing
* Stored procedure or function support is a likely point of failure.
* You probably need to write a custom driver descriptor file.

  Specifically, you need to categorize error codes and SQL states for the third-party driver that you are using.
