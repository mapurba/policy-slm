# 14.4 Supported Third-Party JDBC Drivers (Not Recommended)

This section identifies third-party JDBC drivers that are supported but whose use with the Identity Manager JDBC driver is not recommended:

* [Third-Party JDBC Driver Features](supported-third-party-jdbc-drivers-not-recommended.html#bbd14b4)
* [JDBC URL Syntaxes](supported-third-party-jdbc-drivers-not-recommended.html#bbd14ba)
* [JDBC Driver Class Names](supported-third-party-jdbc-drivers-not-recommended.html#bbd14bo)
* [IBM DB2 Universal Database JDBC Driver](supported-third-party-jdbc-drivers-not-recommended.html#bbd14c1)
* [Microsoft SQL Server 2008 JDBC Driver](supported-third-party-jdbc-drivers-not-recommended.html#cddbggeg)
* [Microsoft SQL Server 2008 R2 JDBC Driver](supported-third-party-jdbc-drivers-not-recommended.html#bwcdy1d)

For information about supported third-party drivers that are recommended, see [Supported Third-Party JDBC Drivers (Not Recommended)](supported-third-party-jdbc-drivers-not-recommended.html).

## 14.4.1 Third-Party JDBC Driver Features

The following table summarizes third-party JDBC driver features:

*Table 14-25* Third-Party JDBC Driver Features

| Driver | Supports Encrypted Transport? | Supports Retrieval of Auto-Generated Keys? |
| IBM DB2 UDB Type 3 | No | No |
| Microsoft 2008 | Yes | Yes |
| Microsoft 2008 R2 | Yes | Yes |

## 14.4.2 JDBC URL Syntaxes

The following table lists URL syntaxes for supported third-party JDBC drivers:

*Table 14-26* URL Syntaxes

| Third-Party JDBC Driver | JDBC URL Syntax |
| IBM DB2 UDB Type 3 | jdbc:db2://ip-address:6789/database-name |
| Microsoft SQL Server 2008 | jdbc:sqlserver://ip-address-or-dns-name:1433;databaseName=database-name |
| Microsoft SQL Server 2008 R2 | jdbc:sqlserver://ip-address-or-dns-name:1433;databaseName=database-name |

This information is used in conjunction with the Authentication Context parameter. For information on this parameter, see [Authentication Context](jdbc-driver-parameters.html#bvqz35i).

## 14.4.3 JDBC Driver Class Names

The following table lists the fully-qualified Java class names of supported third-party JDBC drivers:

*Table 14-27* Class Names of Third-Party JDBC Drivers

| Third-Party JDBC Driver | Class Name |
| IBM DB2 UDB Type 3 | COM.ibm.db2.jdbc.net.DB2Driver |
| Microsoft 2008 | com.microsoft.sqlserver.jdbc.SQLServerDriver |
| Microsoft 2008 R2 | com.microsoft.sqlserver.jdbc.SQLServerDriver |

This information is used in conjunction with the JDBC Driver Class Name parameter. For information on this parameter, see [Third-Party JDBC Driver Class Name](configure-jdbc-driver-specific-parameters.html#b1pu3j9).

## 14.4.4 IBM DB2 Universal Database JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers-not-recommended.html#bgz1gl9)
* [Compatibility](supported-third-party-jdbc-drivers-not-recommended.html#bbd14cb)
* [Security](supported-third-party-jdbc-drivers-not-recommended.html#bbd14cc)
* [Known Issues](supported-third-party-jdbc-drivers-not-recommended.html#bbd14cd)

### Driver Information

*Table 14-28* IBM DB2 Driver Settings

|  | Type 4 Driver |
| Supported Database Versions | 11.x and 12.x |
| Class Name | com.ibm.db2.jcc.DB2Driver |
| URL Syntax | jdbc:db2://ip-address:50000/ database-name |
| Download Instructions | Copy the file from the database server.  file:///database-installation-directory/java |
| File Name | db2jcc.jar |
| Documentation URLs | [DB2 Information Center](http://publib.boulder.ibm.com/infocenter/db2v7luw)  [JDBC Programming](http://publib.boulder.ibm.com/infocenter/db2v7luw/index.jsp?topic=/com.ibm.db2v7.doc/db2a0/db2a0159.htm) |

### Compatibility

The IBM DB2 driver can best be characterized as version-hypersensitive. It is not compatible across major or minor versions of DB2, including FixPacks. For this reason, we recommend that you use the file installed on the database server.

The IBM DB2 driver must be updated on the Identity Manager or Remote Loader server every time the target database is updated, even if only at the FixPack level.

### Security

The IBM DB2 driver does not support encrypted transport.

### Known Issues

* A version mismatch usually results in connectivity-related failures.

  The most common problem experienced with the IBM DB2 driver is because of a driver/database version mismatch. The symptom of a version mismatch is connectivity-related failures such as CLI0601E Invalid statement handle or statement is closed. To remedy the problem, overwrite the db2java.zip file on the Identity Manager or Remote Loader server with the version installed on the database server.
* It’s very difficult to diagnose and remedy Java-related errors on the database server.

  Numerous error conditions and error-codes can arise when you attempt to install and execute user-defined stored procedures and functions written in Java. Diagnosing them can be time consuming and frustrating. A log file (db2diag.log on the database server) can often provide additional debugging information. In addition, all error codes are documented and available online.

## 14.4.5 Microsoft SQL Server 2008 JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers-not-recommended.html#bgz1jp0)
* [Compatibility](supported-third-party-jdbc-drivers-not-recommended.html#bbk49vk)
* [Security](supported-third-party-jdbc-drivers-not-recommended.html#bbk49vl)
* [URL Properties](supported-third-party-jdbc-drivers-not-recommended.html#bbk49vm)

### Driver Information

*Table 14-29* Microsoft SQL Server 2008 Driver Settings

| Supported Database Versions | 2008 |
| Class Name | com.microsoft.sqlserver.jdbc.SQLServerDriver |
| Type | 4 (2 if integrated security is enabled) |
| URL Syntax | jdbc:sqlserver://ip-address-or-dns-name:1433;databaseName=database-name |
| Download Instructions | [Microsoft SQL Server 2008 JDBC Driver](http://msdn2.microsoft.com/en-us/data/aa937724.aspx) |
| Filenames | sqljdbc.jar |

The filename, URL syntax, and classname differ (often subtly) from those of the 2000 driver.

### Compatibility

The SQL Server 2008 driver works only with SQL Server 2005. Database server and driver updates are infrequent.

### Security

The SQL Server 2008 driver supports encrypted transport.

### URL Properties

Delimit URL properties by using a semicolon (;).

The following table lists values for the integratedSecurity URL property for the SQL Server 2005 driver.

*Table 14-30* Values for the integratedSecurity URL Property

| Legal Value | Description |
| false | The default value. JDBC authentication is used. |
| true | Windows process-level authentication is used. |

## 14.4.6 Microsoft SQL Server 2008 R2 JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers-not-recommended.html#bwcdy1e)
* [Compatibility](supported-third-party-jdbc-drivers-not-recommended.html#bwcdy1m)
* [Security](supported-third-party-jdbc-drivers-not-recommended.html#bwcdy1n)
* [URL Properties](supported-third-party-jdbc-drivers-not-recommended.html#bwcdy1o)

### Driver Information

*Table 14-31* Microsoft SQL Server 2008 Driver Settings

| Supported Database Versions: | 2008 R2 |
| Class Name | com.microsoft.sqlserver.jdbc.SQLServerDriver |
| Type | 4 (2 if integrated security is enabled) |
| URL Syntax | jdbc:sqlserver://ip-address-or-dns-name:1433;databaseName=database-name |
| Download Instructions | [Microsoft SQL Server 2008 JDBC Driver](http://msdn2.microsoft.com/en-us/data/aa937724.aspx) |
| Filenames | sqljdbc.jar |

The filename, URL syntax, and classname differ (often subtly) from those of the 2000 driver.

### Compatibility

The SQL Server 2008 R2 driver works only with SQL Server 2008. Database server and driver updates are infrequent.

### Security

The SQL Server 2008 driver supports encrypted transport.

### URL Properties

Delimit URL properties by using a semicolon (;).

The following table lists values for the integratedSecurity URL property for the SQL Server 2008 driver.

*Table 14-32* Values for the integratedSecurity URL Property

| Legal Value | Description |
| false | The default value. JDBC authentication is used. |
| true | Windows process-level authentication is used. |
