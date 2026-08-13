# 14.3 Supported Third-Party JDBC Drivers (Recommended)

This section discusses supported third-party drivers. Using one of these supported drivers is recommended.

* [Third-Party JDBC Driver Features](supported-third-party-jdbc-drivers.html#bvx3a4x)
* [JDBC URL Syntaxes](supported-third-party-jdbc-drivers.html#bvx364n)
* [JDBC Driver Class Names](supported-third-party-jdbc-drivers.html#bvx38mr)
* [Supported Third-Party Jar File Placement](supported-third-party-jdbc-drivers.html#b152m0b7)
* [IBM DB2 Universal Database Type 4 JDBC Driver](supported-third-party-jdbc-drivers.html#bvlsriy)
* [Informix JDBC Driver](supported-third-party-jdbc-drivers.html#bvotf30)
* [Microsoft JDBC Driver for SQL Server](supported-third-party-jdbc-drivers.html#t47303hry5lw)
* [jTDS JDBC Driver](supported-third-party-jdbc-drivers.html#cddedjig)
* [MySQL Connector/J JDBC Driver](supported-third-party-jdbc-drivers.html#bvmdmw4)
* [Oracle Thin Client JDBC Driver](supported-third-party-jdbc-drivers.html#bvlst6q)
* [Oracle OCI JDBC Driver](supported-third-party-jdbc-drivers.html#b67r61v)
* [PostgreSQL JDBC Driver](supported-third-party-jdbc-drivers.html#bvotrr6)
* [Sybase Adaptive Server Enterprise JConnect JDBC Driver](supported-third-party-jdbc-drivers.html#bvng4bc)
* [MariaDB Connector/J JDBC Driver](supported-third-party-jdbc-drivers.html#t4604owjzh0u)

Additional drivers are supported but not recommended. For a list of these drivers, see [Supported Third-Party JDBC Drivers (Not Recommended)](supported-third-party-jdbc-drivers-not-recommended.html).

## 14.3.1 Third-Party JDBC Driver Features

The following table summarizes third-party JDBC driver features:

*Table 14-1* Third-Party JDBC Driver Features

| Driver | Supports Encrypted Transport? | Supports Retrieval of Auto-Generated Keys? |
| IBM DB2 UDB Type 4 | No | No |
| Informix | No | No |
| MySQL Connector/J | Yes | Yes |
| jTDS | Yes | Yes |
| Oracle Thin Client | Yes | No |
| Oracle OCI | Yes | No |
| PostgreSQL | Yes, for JDBC 3 (Java 1.4) versions and later | No |
| Sybase jConnect | Yes | No |

## 14.3.2 JDBC URL Syntaxes

The following table lists URL syntaxes for supported third-party JDBC drivers:

*Table 14-2* URL Syntaxes

| Third-Party JDBC Driver | JDBC URL Syntax |
| IBM DB2 UDB Type 4, Universal | jdbc:db2://ip-address:50000/database-name |
| Informix | jdbc:informix-sqli://ip-address:1526/database-name:informixserver=server-id |
| jTDS | jdbc:jtds:sqlserver://ip-address/database-name |
| MySQL Connector/J | jdbc:mysql://ip-address:3306/database-name |
| Oracle OCI | jdbc:oracle:oci8:@tns-name |
| Oracle Thin Client | sid - jdbc:oracle:thin:@ip-address:1521:<sid>  cdb - jdbc:oracle:thin:@ip-address:1521/<service> |
| PostgreSQL | jdbc:postgresql://ip-address:5432/database-name |
| Sybase jConnect | jdbc:sybase:Tds:ip-address:2048/database-name |

This information is used in conjunction with the Authentication Context parameter. For information on this parameter, see [Authentication Context](jdbc-driver-parameters.html#bvqz35i).

## 14.3.3 JDBC Driver Class Names

The following table lists the fully qualified Java class names of supported third-party JDBC drivers:

*Table 14-3* Class Names of Third-Party JDBC Drivers

| Third-Party JDBC Driver | Class Name |
| IBM DB2 UDB Type 4, Universal | com.ibm.db2.jcc.DB2Driver |
| Informix | com.informix.jdbc.IfxDriver |
| jTDS | net.sourceforge.jtds.jdbc.Driver |
| MySQL Connector/J | org.gjt.mm.mysql.Driver |
| Oracle OCI | oracle.jdbc.driver.OracleDriver |
| Oracle Thin Client | oracle.jdbc.driver.OracleDriver |
| PostgreSQL | org.postgresql.Driver |
| Sybase jConnect 6.0 | com.sybase.jdbc3.jdbc.SybDriver |
| Sybase jConnect 7.0 | com.sybase.jdbc4.jdbc.SybDriver |

This information is used in conjunction with the JDBC Driver Class Name parameter. For information on this parameter, see [Third-Party JDBC Driver Class Name](configure-jdbc-driver-specific-parameters.html#b1pu3j9).

## 14.3.4 Supported Third-Party Jar File Placement

The following tables identify the paths where third-party JDBC driver jar files should be placed on an Identity Manager or Remote Loader server, assuming default installation paths. Ensure to restart eDirectory, after placing the jar files in the corresponding directory, for the change to take effect.

*Table 14-4* Locations for jar Files: Identity Manager Server

| Platform | Directory Path |
| Solaris, Linux, or AIX | /opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8.x) |
| Windows | novell\NDS\lib |

*Table 14-5* Locations for jar Files: Remote Loader Server

| Platform | Directory Path |
| Solaris, Linux, or AIX | /opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8.x) |
| Windows | novell\RemoteLoader\lib |

## 14.3.5 IBM DB2 Universal Database Type 4 JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers.html#bgz153w)
* [Compatibility](supported-third-party-jdbc-drivers.html#bvmt1f2)
* [Security](supported-third-party-jdbc-drivers.html#bvnezdh)
* [Known Issues](supported-third-party-jdbc-drivers.html#bvmtmxd)

### Driver Information

*Table 14-6* IBM DB2 Driver: Type 4

| Supported Database Versions | 11.0 or later |
| Class Name | com.ibm.db2.jcc.DB2Driver |
| Type | 4 |
| URL Syntax | jdbc:db2://ip-address:50000/database-name |
| Download Instructions | Download as part of the latest FixPack (recommended).  [IBM Support & Downloads](http://www.ibm.com/support/us/)  or  Copy the file from the database server.  file:///database-installation-directory/java |
| Filename | db2jcc.jar, db2jcc\_license\_cu.jar, db2jcc\_javax.jar (optional), db2jcc\_license\_cu-9.5.jar, db2jcc-9.5.jar |
| Documentation URLs | [DB2 Information Center](http://publib.boulder.ibm.com/infocenter/db2help)  [DB2 Universal JDBC Driver](http://publib.boulder.ibm.com/infocenter/db2help/index.jsp?topic=/com.ibm.db2.udb.doc/ad/t0010264.htm)  [Security under the DB2 Universal JDBC Driver](http://publib.boulder.ibm.com/infocenter/db2help/index.jsp?topic=/com.ibm.db2.udb.doc/ad/cjvjcsec.htm) |

Unlike the type 3 driver, the type 4 driver has only a minimal set of defined error codes. This absence inhibits the JDBC driver’s ability to distinguish between connectivity, retry, authentication, and fatal error conditions.

### Compatibility

The IBM DB2 driver is backward compatible. Database server updates are frequent. Driver updates are infrequent.

### Security

The IBM DB2 driver supports a variety of authentication security mechanisms but does not support encrypted transport.

### Known Issues

It’s very difficult to diagnose and remedy Java-related errors on the database server.

Numerous error conditions and error codes can arise when you attempt to install and execute user-defined stored procedures and functions written in Java. Diagnosing these can be time consuming and frustrating. A log file (db2diag.log on the database server) can often provide additional debugging information. In addition, all error codes are documented and available online.

## 14.3.6 Informix JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers.html#bgz161s)
* [Compatibility](supported-third-party-jdbc-drivers.html#bvou7po)
* [Security](supported-third-party-jdbc-drivers.html#bvou7pp)
* [Required Parameter Settings for ANSI-Compliant Databases](supported-third-party-jdbc-drivers.html#bvpbo71)
* [Dynamic Parameter Defaults](supported-third-party-jdbc-drivers.html#bvuie8u)
* [Known Issues](supported-third-party-jdbc-drivers.html#bvou7pq)

### Driver Information

*Table 14-7* Informix JDBC Driver

| Supported Database Versions | Dynamic Server 11.5 or later |
| Class Name | com.informix.jdbc.IfxDriver |
| Type | 4 |
| URL Syntax | jdbc:informix-sqli://ip-address:1526/database-name:informixserver=server-id |
| Download Instructions | [Download URL](http://www-306.ibm.com/software/data/informix/tools/jdbc) |
| Filenames (11) | ifxjdbc.jar, jdbcx.jar (optional) |
| Documentation URLs | [Informix Information Center](http://publib.boulder.ibm.com/infocenter/ids9help/index.jsp)  For more information on Informix JDBC Driver, see [Informix Library](http://www-306.ibm.com/software/data/informix/pubs/library/) |

### Compatibility

The Informix driver is backward compatible. Database server updates and driver updates are infrequent.

### Security

The Informix driver does not support encrypted transport.

### Required Parameter Settings for ANSI-Compliant Databases

The following table lists driver parameters that must be explicitly set for the JDBC driver to interoperate with the Informix driver against ANSI-compliant databases.

*Table 14-8* Driver Settings for ANSI-Compliant Databases

| Display Name | Tag Name | Value |
| Supports schemas in metadata retrieval? | supports-schemas-in-metadata-retrieval  See [Supports Schemas in Metadata Retrieval?](configure-jdbc-driver-specific-parameters.html#b1pu3oc). | false |
| Force username case: | force-username-case  See [Force Username Case](configure-jdbc-driver-specific-parameters.html#b1pu3no). | upper |

### Dynamic Parameter Defaults

The following table lists driver compatibility parameters that the JDBC driver implicitly sets at runtime. Do not override these settings.

*Table 14-9* Informix JDBC Settings Not to Override

| Display Name | Tag Name | Value |
| Function return method: | function-return-method  See [Function Return Method](configure-jdbc-driver-specific-parameters.html#b1pu3o6). | result set |

### Known Issues

* Schema names cannot be used to retrieve metadata against an ANSI-compliant database. Set the driver compatibility parameter [Supports Schemas in Metadata Retrieval?](configure-jdbc-driver-specific-parameters.html#b1pu3oc) to Boolean False. The database objects available for metadata retrieval are those visible to the database user who authenticated to the database. Schema qualifiers cannot be used to identify database objects. Therefore, to avoid naming collisions (such as owner1.table1, owner2.table1), give the database authentication user only SELECT privileges on objects being synchronized.
* When used against ANSI-compliant databases, usernames must be in uppercase. Set the driver compatibility parameter [Force Username Case](configure-jdbc-driver-specific-parameters.html#b1pu3no) to upper.

## 14.3.7 Microsoft JDBC Driver for SQL Server

* [Driver Information](supported-third-party-jdbc-drivers.html#t47303hrydbp)
* [Compatibility](supported-third-party-jdbc-drivers.html#t47303hrysrb)
* [Security](supported-third-party-jdbc-drivers.html#t47303hrz0h4)
* [URL Properties](supported-third-party-jdbc-drivers.html#t47303hrz86x)

### Driver Information

*Table 14-10* Microsoft JDBC Driver for SQL Server Settings

| Supported Database Versions: | Microsoft SQL Server 2022, Microsoft SQL Server 2019, Microsoft SQL Server 2016 Service Pack 1 |
| Class Name | com.microsoft.sqlserver.jdbc.SQLServerDriver |
| Type | 4 |
| URL Syntax | jdbc:sqlserver://<host>[:<port1433>];databaseName=<database> |
| Download Instructions | [Microsoft JDBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-2017) |
| Filenames | mssql-jdbc-9.4.0.jre8.jar for 4.8.6, mssql-jdbc-7.2.2.jre11.jar for 4.8.7, mssql-jdbc-12.8.0.jre11.jar for 4.9 |

### Compatibility

The Microsoft JDBC driver works with all supported versions of Microsoft SQL Server.

### Security

The Microsoft JDBC driver supports encrypted transport.

*NOTE:*For more information on SSL encryption, see [Connection String Options page](https://docs.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?view=sql-server-2017).

### URL Properties

Delimit URL properties by using a semicolon (;).

The following table lists values for the integratedSecurity URL property for JDBC driver for SQL Server.

*Table 14-11* Values for the integratedSecurity URL Property

| Legal Value | Description |
| false | The default value. JDBC authentication is used. |
| true | Windows process-level authentication is used. |

## 14.3.8 jTDS JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers.html#bgz19a1)
* [Limitations](supported-third-party-jdbc-drivers.html#bbxg432)
* [Compatibility](supported-third-party-jdbc-drivers.html#bbk49uz)
* [Security](supported-third-party-jdbc-drivers.html#bbk49v0)
* [URL Properties](supported-third-party-jdbc-drivers.html#bbk49v1)

### Driver Information

*Table 14-12* jTDS Driver Settings

| Supported Database Versions: | Microsoft SQL Server 2005 Service Pack 1 or later, 2008 and 2008 R2, Sybase Adaptive Server Enterprise (ASE) 15 or later |
| Class Name | net.sourceforge.jtds.jdbc.Driver |
| Type | 4 (2 if NTLM or SSO authentication is enabled) |
| URL Syntax | jdbc:jtds:sqlserver://ip-address/database-name  jdbc:jtds:sybase://ip-address/database-name |
| Download Instructions | [The jTDS Project](http://jtds.sourceforge.net/) |
| Filenames | jtds-<version>.jar |

### Limitations

The jTDS JDBC driver does not support views or stored procedures. NetIQ Corporation recommends that you use the Microsoft 2000 JDBC driver when Subscribing to views.

### Compatibility

The jTDS driver works with all versions of Microsoft SQL Server. It also supports all versions of Sybase ASE, but it has not been tested by NetIQ against that database server yet. Driver updates are infrequent.

### Security

The jTDS driver supports encrypted transport.

### URL Properties

Delimit URL properties by using a semicolon (;).

The following table lists values for the domain URL property for the jTDS driver.

*Table 14-13* Values for the Domain URL Property

| Legal Value | Description |
| <any-domain-name> | When a domain name is specified, either NTLM or SSO authentication can be used. NTLM authentication is selected when a username and password are supplied. SSO authentication is selected when a username and password are not supplied. |
| <no-value> | JDBC authentication is used. |

The following table lists values for the SSL URL property for the jTDS driver.

*Table 14-14* Values for the SSL URL Property

| Legal Value | Description |
| off | SSL is not used. This is the default. |
| request | SSL is used if the server supports it. |
| require | SSL is required. An exception is thrown if the server doesn’t support it. |
| authenticate | SSL is required. An exception is thrown if the server doesn’t support it. In addition, the server’s certificate must be signed by a trusted certificate authority. |

## 14.3.9 MySQL Connector/J JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers.html#bgz1at6)
* [Compatibility](supported-third-party-jdbc-drivers.html#bvnf3lu)
* [Security](supported-third-party-jdbc-drivers.html#bvnf2k5)
* [Required Parameter Settings for MyISAM Tables](supported-third-party-jdbc-drivers.html#bvpbrdx)

### Driver Information

*Table 14-15* MySQL Connector/J JDBC Driver Settings

| Supported Database Versions | 8 or later |
| Class Name | com.mysql.cj.jdbc.Driver |
| Type | 4 |
| URL Syntax | jdbc:mysql://ip-address:3306/database-name |
| Download Instructions | Download and extract. The jar file is located in the extract-dir/mysql-connector-java-version directory.  [MySQL Connector/J](http://www.mysql.com/products/connector/j/) |
| Filename | mysql-connector-java-version-bin.jar, mysql-connector-j-8.0.33.jar |
| Documentation URLs | For more information on MySQL Connector/J Documentation, see [MySQL Refereal manual](http://dev.mysql.com/doc/refman/5.0/en/)  For more information on Connecting Over SSL, see [MySQL Refereal manual](http://dev.mysql.com/doc/refman/5.0/en/) |

Also see [Generation/Retrieval Method (Table-Global)](how-to-set-subscription-parameters.html#bvul6hv).

### Compatibility

The Connector/J driver is backward compatible. Database server updates are frequent. Driver updates are infrequent.

### Security

The Connector/J driver supports JSSE (Java Secure Sockets Extension) SSL-encrypted transport.

### Required Parameter Settings for MyISAM Tables

The following table lists driver parameters that you must set so that the JDBC driver can interoperate with the Connector/J driver against MyISAM tables.

*Table 14-16* Settings for MyISAM Tables

| Display Name | Tag Name | Value |
| Use manual transactions? | use-manual-transactions | false |

## 14.3.10 Oracle Thin Client JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers.html#bgz1bb8)
* [Compatibility](supported-third-party-jdbc-drivers.html#bvnf54l)
* [Security](supported-third-party-jdbc-drivers.html#bvnfvfd)
* [Dynamic Parameter Defaults](supported-third-party-jdbc-drivers.html#bvox4g5)
* [Connection Properties](supported-third-party-jdbc-drivers.html#b1igbst)
* [Known Issues](supported-third-party-jdbc-drivers.html#bvnf54m)

### Driver Information

*Table 14-17* Oracle Thin Client Settings

| Supported Database Versions | 19c and 21c |
| Class Name | oracle.jdbc.driver.OracleDriver |
| Type | 4 |
| URL Syntax | sid - jdbc:oracle:thin:@ip-address:1521:<sid>  cdb - jdbc:oracle:thin:@ip-address:1521/<service> |
| Filenames | * For 18c and 19c: ojdbc8.jar available in [Oracle Download](https://www.oracle.com/database/technologies/jdbc-ucp-122-downloads.html) site. |
| Documentation URLs | For more information on Oracle Advanced Security, see [Stanford University](http://www.stanford.edu/) page  For more information on JDBC FAQ, see [Oracle Technology](http://www.oracle.com/technology/) page. |

### Compatibility

The Thin Client driver is backward compatible. Database server updates and driver updates are infrequent.

Oracle releases thin client drivers for various JVMs. Even though all of them work with this product, we recommend that you use the 1.6 version.

### Security

The Thin Client driver supports Oracle Advanced Security encrypted transport.

### Dynamic Parameter Defaults

The following table lists driver compatibility parameters that the JDBC driver implicitly sets at runtime. Do not explicitly override these settings.

*Table 14-18* Oracle Thin Client Settings Not to Override

| Display Name | Tag Name | Value |
| Number of returned result sets: | handle-stmt-results | single |

### Connection Properties

The following table lists important connection properties for this driver.

*Table 14-19* Oracle Thin Client: Connection Properties

| Property | Significance |
| includeSynonyms | If the value of this property is true, synonym column metadata is available. |
| ORACLE.NET.ENCRYPTION\_CLIENT | Defines the level of security that the client wants to negotiate with the server. |
| ORACLE.NET.ENCRYPTION\_TYPES\_CLIENT | Defines the encryption algorithm to be used. |
| ORACLE.NET.CRYPTO\_CHECKSUM\_CLIENT | Defines the level of security that it wants to negotiate with the server for data integrity. |
| ORACLE.NET.CRYPTO\_CHEKSUM\_TYPES\_CLIENT | Defines the data integrity algorithm to be used. |

### Known Issues

* High CPU utilization triggered by execution of embedded SQL statements:

  The most common problem experienced with this driver is high CPU utilitization. As a result, this driver always indicates that more results are available from calls to method java.sql.Statement.execute(String stmt), which can lead to an infinite loop condition. This condition occurs only if all the following happen:

  + A value other than single, no, or one in the driver compatibility parameter [Number of Returned Result Sets](configure-jdbc-driver-specific-parameters.html#b1pu3ms) is being executed.
  + An embedded SQL statement is being executed.
  + The type of statement is not explicitly specified.

  To avoid the conditions that produce high CPU utilization:

  + Do not explicitly set this parameter. Defer to the dynamic default value.
  + Always place a jdbc:type attribute on embedded <jdbc:statement> elements.

    *NOTE:*The jdbc namespace prefix must map to urn:dirxml:jdbc.
* Can’t retrieve synonym column metadata.

  The connection property includeSynonyms must be set to true.
* Can’t see synonym table primary key constraint.

  The only known solution to this problem is to use a view.

## 14.3.11 Oracle OCI JDBC Driver

*Table 14-20* Oracle OCI JDBC Driver Settings

| Supported Database Versions | 12c, 18c, 19c, 21c and 23c |
| Class Name | oracle.jdbc.driver.OracleDriver |
| Type | 2 |
| URL Syntax | jdbc:oracle:oci8:@tns-name |
| Filenames | * For 12c: ojdbc7.jar available in [Oracle Download](https://www.oracle.com/database/technologies/jdbc-upc-downloads.html) site. * For 18c and 19c: ojdbc8.jar available in [Oracle Download](https://www.oracle.com/database/technologies/jdbc-ucp-122-downloads.html) site. |
| Documentation URLs | [Oracle Call Interface](http://www.oracle.com/technology/)  [OCI FAQ](http://www.oracle.com/technology/)  [Oracle Advanced Security](http://www.stanford.edu/)  [Instant Client](http://www.oracle.com/technology/tech/oci/instantclient/index.html)  [Instant Client](https://docs.oracle.com/cd/B19306_01/server.102/b14357/ape.htm) |

You can install SQLNet by doing either of the following:

* Use the Instant Client, which bypasses unneeded components of the full version.
* Download the full package from Oracle.

If the database is running on the same server as Identity Manager, you don’t need to install SQLNet because SQLNet comes as standard on the database server.

The Oracle OCI driver is essentially the same as the Thin Client driver. See [Oracle Thin Client JDBC Driver](supported-third-party-jdbc-drivers.html#bvlst6q). The OCI client differs in the following ways:

* The OCI Client supports clustering, failover, and high availability.
* The OCI Client has additional security options.

For information on setting up the Oracle OCI Client, see [Section M.0, Setting Up an OCI Client on Linux](setup-oci-client-on-linux-for-jdbc-driver.html).

## 14.3.12 PostgreSQL JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers.html#bgz1dal)
* [Compatibility](supported-third-party-jdbc-drivers.html#bvotrre)
* [Security](supported-third-party-jdbc-drivers.html#bvotrrf)

### Driver Information

*Table 14-21* PostgreSQL JDBC Driver Settings

| Supported Database Versions | 14, 15, 16 and 17 |
| Class Name | org.postgresql.Driver |
| Type | 4 |
| URL Syntax | jdbc:postgresql://ip-address:5432/database-name |
| Download Instructions | [JDBC Driver Download](http://jdbc.postgresql.org/download.html) |
| Filename | postgresql-42.6.1.jar |
| Documentation URLs | [JDBC Driver Documentation](http://jdbc.postgresql.org/)  [Using SSL](http://jdbc.postgresql.org/documentation/80/ssl.html) |

The filename of the PostgreSQL varies by database version.

### Compatibility

The latest builds of the PostgreSQL driver are backward compatible through server version 8.4.3. Database server updates and driver updates are frequent.

### Security

The PostgreSQL driver supports SSL-encrypted transport for JDBC 3 driver versions.

## 14.3.13 Sybase Adaptive Server Enterprise JConnect JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers.html#bgz1dva)
* [Compatibility](supported-third-party-jdbc-drivers.html#bvngfym)
* [Security](supported-third-party-jdbc-drivers.html#bvngdlr)
* [Connection Properties](supported-third-party-jdbc-drivers.html#bw19mi8)

### Driver Information

*Table 14-22* Sybase Adaptive Server Enterprise Driver Settings

| Supported Database Versions | Adaptive Server Enterprise 15.0 or later |
| Class Name | com.sybase.jdbc3.jdbc.SybDriver (for jconn3.jar) com.sybase.jdbc4.jdbc.SybDriver (for jconn4.jar) |
| Type | 4 |
| URL Syntax | jdbc:sybase:Tds:ip-address:2048/database-name |
| Download Instructions | [Sybase Downloads](http://www.sybase.com/downloads) |
| Filenames | jconn3.jar or jconn4.jar |
| Documentation URLs | For more information on jConnect Documentation, see [Sybase inforcenter](http://infocenter.sybase.com/) page. |

For JDBC 3 (Java 1.4) versions and later.

### Compatibility

The Adaptive Server driver is backward compatible. Database server updates and driver updates are infrequent.

### Security

The Adaptive Server driver supports SSL-encrypted transport. To enable SSL encryption, you must specify a custom socket implementation via the SYBSOCKET\_FACTORY connection property. For additional information on how to set connection properties, see [Connection Properties](configure-jdbc-driver-specific-parameters.html#b1pu3lk).

### Connection Properties

The SYBSOCKET\_FACTORY property can be used to specify the class name of a custom socket implementation that supports encrypted transport.

## 14.3.14 MariaDB Connector/J JDBC Driver

* [Driver Information](supported-third-party-jdbc-drivers.html#t4604owk1m6m)
* [Security](supported-third-party-jdbc-drivers.html#t4604owk81ny)
* [Required Parameter Settings for MyISAM Tables](supported-third-party-jdbc-drivers.html#t4604owka6tq)

### Driver Information

*Table 14-23* MariaDB Connector/J JDBC Driver Settings

| Supported Database Versions | 10.11 or later |
| Class Name | org.mariadb.jdbc.Driver |
| Type | 4 |
| URL Syntax | jdbc:mysql://ip-address:3306/database-name |
| Download Instructions | Download and extract. The jar file is located in the extract-dir/mysql-connector-java-version directory.  [MariaDB Connector](https://downloads.mariadb.org/connector-java/2.2.2/) |
| Filename | mariadb-java-client-version.jar |
| Documentation URLs | For more information on MariaDB Connector/J Documentation, see [MariaDB Connector/J Referral manual](https://mariadb.com/kb/en/library/about-mariadb-connector-j/) |

Also see [Generation/Retrieval Method (Table-Global)](how-to-set-subscription-parameters.html#bvul6hv).

### Security

The Connector/J driver supports JSSE (Java Secure Sockets Extension) SSL-encrypted transport.

### Required Parameter Settings for MyISAM Tables

The following table lists driver parameters that you must set so that the JDBC driver can interoperate with the Connector/J driver against MyISAM tables.

*Table 14-24* Settings for MyISAM Tables

| Display Name | Tag Name | Value |
| Use manual transactions? | use-manual-transactions | false |
