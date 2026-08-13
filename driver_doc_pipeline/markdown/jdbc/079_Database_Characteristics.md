# 13.3 Database Characteristics

* [Database Features](characteristics-of-databases.html#bvowloe)
* [Current Time Stamp Statements](characteristics-of-databases.html#bvowlyp)
* [Syntaxes for Calling Stored Procedures and Functions](characteristics-of-databases.html#bvowm5a)
* [Left Outer Join Operators](characteristics-of-databases.html#bvowmei)
* [Undelimited Identifier Case Sensitivity](characteristics-of-databases.html#bvqzikw)
* [Supported Transaction Isolation Levels](characteristics-of-databases.html#bvw1vdv)
* [Commit Keywords](characteristics-of-databases.html#bvx56zn)
* [IBM DB2 Universal Database (UDB)](characteristics-of-databases.html#bvnc76v)
* [Informix Dynamic Server (IDS)](characteristics-of-databases.html#bvnc79z)
* [Microsoft SQL Server](characteristics-of-databases.html#bvnc7ki)
* [MySQL/MariaDB](characteristics-of-databases.html#bvnc7nt)
* [Oracle](characteristics-of-databases.html#bvnc7qt)
* [PostgreSQL](characteristics-of-databases.html#bvnc7vn)
* [Sybase Adaptive Server Enterprise (ASE)](characteristics-of-databases.html#bvnc805)

## 13.3.1 Database Features

*Table 13-2* Database Features

| Database | Schemas | Views | Identity Columns | Sequences | Stored Procedures | Functions | Triggers | Instead-Of-Triggers |
| IBM DB2 UDB 9.x | Y | Y | Y | N | Y1 | Y1 | Y | Y |
| Informix IDS 11.x | Y | Y | Y2 | N | Y3 | Y | Y | Y |
| MS SQL 2008, 2008 R2, 2012, 2014, and 2016 | Y | Y | Y | N | Y | Y | Y | Y |
| MySQL 5.5.x and 5.6.x | Y | Y | Y4 | N | Y | Y | Y | N |
| Oracle 12c, 18c and 19c | Y | Y | N | Y | Y | Y | Y | Y |
| Postgres 8.4.x, 9.0.x, and 9.6.3 | Y | Y | Y5 | Y | Y | Y | Y6 | Y6 |
| Sybase ASE 15.0 | Y | Y | Y | N | Y | N | Y | N |
| MariaDB 10.2.13 | Y | Y | Y4 | N | Y | Y | Y | N |

1 DB2 natively supports stored procedures or functions written in Java. To write procedures by using the native SQL procedural language, install a C compiler on the database server.

2 The Informix identity column keyword is SERIAL8.

3 Informix stored procedures cannot return values through OUT parameters.

4 The identity column keyword is AUTO\_INCREMENT for MySQL and MariaDB.

5 You can use a PostgreSQL sequence object to provide default values for primary key columns, effectively simulating an identity column.

6PostgreSQL has a native construct called rules. This construct can be used to effectively simulate triggers and instead-of-triggers. It also supports the use of triggers or instead-of-triggers written in a variety of procedural programming languages.

## 13.3.2 Current Time Stamp Statements

The following table lists SQL statements used to retrieve the current date and time by database:

*Table 13-3* Time Stamp Statements

| Database | Current Time Stamp Statement | ANSI-Compliant |
| IBM DB2 UDB | SELECT (CURRENT TIMESTAMP) FROM SYSIBM.SYSDUMMY1 FETCH FIRST 1 ROW ONLY | No |
| Informix IDS | SELECT FIRST 1 (CURRENT YEAR TO FRACTION(5)) FROM INFORMIX.SYSTABLES | No |
| MSSQL | SELECT (CURRENT\_TIMESTAMP) | Yes |
| MySQL/MariaDB | SELECT (CURRENT\_TIMESTAMP) | Yes |
| Oracle | SELECT (SYSDATE) FROM SYS.DUAL | No |
| PostgreSQL | SELECT (CURRENT\_TIMESTAMP) | Yes |
| Sybase ASE | SELECT GETDATE() | No |

## 13.3.3 Syntaxes for Calling Stored Procedures and Functions

The following table lists the syntaxes for calling a stored procedure or function by database vendor. There’s also a vendor-neutral JDBC escape syntax (see [JDBC Escape Syntax](http://edocs.bea.com/wls/docs81/jdbc_drivers/sqlescape.html)). Whenever possible, it is more secure to call a stored procedure or function by using the jdbc:call-function or jdbc:call-procedure syntax. See [Calling Stored Procedures and Functions](how-to-call-stored-procedures-and-functions.html).) Other syntaxes should be used only when specifying procedure or function calls in driver parameters (for example, [Post Polling Statements](how-to-set-publication-parameters.html#bvvq2gw) and [Connection Initialization Statements](configure-jdbc-driver-specific-parameters.html#b1pu3lc)).

*Table 13-4* Calling a Stored Procedure or Function

| Database | Stored Procedure/Function JDBC Call Syntax |
| IBM DB2 UDB | {call schema-name.procedure-name(parameter-list)} |
| Informix IDS | EXECUTE [PROCEDURE | FUNCTION] schema-name.routine-name(parameter-list) |
| MSSQL | EXECUTE schema-name.procedure-name(parameter-list) |
| MySQL/MariaDB | CALL schema-name.procedure-name(parameter-list) |
| Oracle1 | CALL schema-name.procedure-name(parameter-list) |
| PostgreSQL | SELECT schema-name.procedure-name(parameter-list) |
| Sybase ASE | EXECUTE schema-name.procedure-name(parameter-list) |

1 Oracle’s JDBC implementation does not support calling functions as a string.

## 13.3.4 Left Outer Join Operators

The following table lists outer join operators by database.

*Table 13-5* Outer Join Operators

| Database | Left Outer Join Operator | ANSI-Compliant |
| IBM DB2 UDB | LEFT OUTER JOIN | Yes |
| Informix IDS | LEFT OUTER JOIN | Yes |
| MSSQL 2005 | LEFT OUTER JOIN | Yes |
| MySQL/MariaDB | LEFT OUTER JOIN | Yes |
| Oracle | LEFT OUTER JOIN | Yes |
| PostgreSQL | LEFT OUTER JOIN | Yes |
| Sybase ASE | \*= | No |

## 13.3.5 Undelimited Identifier Case Sensitivity

*Table 13-6* Case Sensitivity for Undelimited Identifiers

| Database | Case-Sensitive? |
| IBM DB2 UDB | No |
| Informix IDS | No |
| MSSQL | No |
| MySQL/MariaDB | Yes |
| Oracle | No |
| PostgreSQL | No |
| Sybase ASE | Yes |

## 13.3.6 Supported Transaction Isolation Levels

*Table 13-7* Supported Transaction Isolation Levels

| Database | None | Read Uncommitted | Read Committed | Repeatable Read | Serializable | URL |
| IBM DB2 UDB | N | Y | Y1 | Y | Y | [Setting JDBC Transaction Isolation Levels](http://publib.boulder.ibm.com/infocenter/db2help/index.jsp?topic=/com.ibm.db2.udb.doc/ad/tjvjdiso.htm) |
| MySQL/MariaDB (InnoDB\* Table Type) | N | Y | Y | Y1 | Y | [InnoDB Transaction Isolation Levels](http://dev.mysql.com/doc/mysql/en/innodb-transaction-isolation.html) |
| Oracle | N | N | Y1 | N | Y | [JDBC Transaction Optimization](http://www.oracle.com/technology/oramag/oracle/02-jul/o42special_jdbc.html) |
| PostgreSQL | N | N2 | Y1 | N2 | Y | [Transaction Isolation](http://www.postgresql.org/docs/current/static/transaction-iso.html) |

1 This is the default isolation level for this database. 2 Can be set, but it is aliased to a supported isolation level.

## 13.3.7 Commit Keywords

The following table identifies the commit keywords for supported databases:

*Table 13-8* Commit Keywords

| Database | Commit Keyword |
| IBM DB2 UDB | COMMIT |
| Informix IDS | COMMIT WORK1 |
| MSSQL | GO |
| MySQL/MariaDB | COMMIT |
| Oracle | COMMIT |
| PostgreSQL | COMMIT |
| Sybase ASE | GO |

1 For logging and ANSI-compliant databases. Non-logging databases do not support transactions.

## 13.3.8 IBM DB2 Universal Database (UDB)

* [Database Properties](characteristics-of-databases.html#bgz0sm9)
* [Dynamic Defaults](characteristics-of-databases.html#bvox482)
* [Known Issues](characteristics-of-databases.html#bvouqyl)

### Database Properties

*Table 13-9* Properties for IBM DB2 UDB

| Property | Value |
| Current Timestamp Statement | SELECT (CURRENT TIMESTAMP) FROM SYSIBM.SYSDUMMY1 FETCH FIRST 1 ROW ONLY |
| Case-Sensitive? | No |
| Commit Keyword | COMMIT |
| Left Outer Join Operator | LEFT OUTER JOIN |

### Dynamic Defaults

The following table lists database compatibility parameters that the JDBC driver implicitly sets at runtime. Do not explicitly override these settings.

*Table 13-10* Dynamically Configured IBM DB2 Universal Database Settings

| Display Name | Tag Name | Value |
| Current Timestamp Statement: | current-timestamp-stmt | SELECT (CURRENT TIMESTAMP) FROM SYSIBM.SYSDUMMY1 FETCH FIRST 1 ROW ONLY |
| Timestamp Translator class: | time-translator-class | com.novell.nds.dirxml.driver.jdbc.db.DB2Timestamp |

### Known Issues

The timestamp format is proprietary. See [Known Issues](characteristics-of-databases.html#btezy6z).

## 13.3.9 Informix Dynamic Server (IDS)

* [Database Properties](characteristics-of-databases.html#bgz0tpr)
* [Dynamic Defaults](characteristics-of-databases.html#bvoxb8v)
* [Known Issues](characteristics-of-databases.html#btezy71)

### Database Properties

*Table 13-11* Settings for Informix Dynamic Server

| Property | Value |
| Current Timestamp Statement | SELECT FIRST 1 (CURRENT YEAR TO FRACTION(5)) FROM INFORMIX.SYSTABLES |
| Case-Sensitive? | No |
| Commit Keyword | COMMIT WORK1 |
| Left Outer Join Operator | LEFT OUTER JOIN |

1 For logging and ANSI-compliant databases. Nonlogging databases do not support transactions.

### Dynamic Defaults

The following table lists database compatibility parameters that the JDBC driver implicitly sets at runtime. Do not explicitly overwrite these settings.

*Table 13-12* Dynamically Configured Informix Dynamic Server Settings

| Display Name | Tag Name | Value |
| Current Timestamp Statement: | current-timestamp-stmt | SELECT FIRST 1 (CURRENT YEAR TO FRACTION(5)) FROM INFORMIX.SYSTABLES |

### Known Issues

* NUMERIC or DECIMAL columns cannot be used as primary keys unless the scale (the number of digits to the right of the decimal point) is explicitly set to 0 when the table is created. By default, the scale is set to 255.
* DBAs cannot grant privileges to objects they don’t own.

## 13.3.10 Microsoft SQL Server

* [Database Properties](characteristics-of-databases.html#bgz0ube)
* [Dynamic Defaults](characteristics-of-databases.html#bvoxmfi)

### Database Properties

*Table 13-13* Settings for Microsoft SQL Server

| Property | Value |
| Current Timestamp Statement | SELECT (CURRENT\_TIMESTAMP) |
| Case-Sensitive? | No |
| Commit Keyword | GO |
| Left Outer Join Operator (2005,2008,2008 R2, 2012, 2014) | LEFT OUTER JOIN |

### Dynamic Defaults

The following table lists database compatibility parameters that the JDBC driver implicitly sets at runtime. Do not explicitly overwrite these settings.

*Table 13-14* Dynamically Configured Microsoft SQL Server Settings

| Display Name | Tag Name | Value |
| Add default values on insert? | add-default-values-on-view-insert | True |
| Left outer-join operator (2005,2008,2008 R2, 2012, 2014) | left-outer-join-operator | LEFT OUTER JOIN |

## 13.3.11 MySQL/MariaDB

* [Database Properties](characteristics-of-databases.html#bgz0uy7)
* [Dynamic Defaults](characteristics-of-databases.html#bvoxktg)
* [Known Issues](characteristics-of-databases.html#btezy70)

### Database Properties

*Table 13-15* Settings for MySQL/MariaDB

| Property | Value |
| Current Timestamp Statement | SELECT (CURRENT\_TIMESTAMP) |
| Case-Sensitive? | Yes |
| Commit Keyword | COMMIT |
| Left Outer Join Operator | LEFT OUTER JOIN |

### Dynamic Defaults

The following table lists database compatibility parameters that are dynamically configured at runtime for this database.

*Table 13-16* Dynamically Configured MySQL/MariaDB Settings

| Display Name | Tag Name | Value |
| Supports schemas in metadata retrieval? | supports-schemas-in-metadata-retrieval | false |

### Known Issues

* TIMESTAMP columns, when they are updated after being initially set to 0 or NULL, are always set to the current date and time. To compensate for this behavior, we recommend that you map Identity Vault Time and Timestamp syntaxes to DATETIME columns.

## 13.3.12 Oracle

* [Database Properties](characteristics-of-databases.html#bgz0vqi)
* [Dynamic Defaults](characteristics-of-databases.html#bvoxrbr)
* [Limitations](characteristics-of-databases.html#bw6x31n)

### Database Properties

*Table 13-17* Settings for Oracle

| Property | Value |
| Current Timestamp Statement | SELECT (SYSDATE) FROM SYS.DUAL |
| Case-Sensitive? | No |
| Commit Keyword | COMMIT |
| Left Outer Join Operator | (+) |

### Dynamic Defaults

The following table lists database compatibility parameters that the JDBC driver implicitly sets at runtime. Do not explicitly overwrite these settings.

*Table 13-18* Dynamically Configured Oracle Settings

| Display Name | Tag Name | Value |
| Left outer-join operator | left-outer-join-operator | (+) |
| Exclude filter expression | exclude-table-filter | BIN\$.{22}==\$0 |
| Lock statement generator class | lock-generator-class | com.novell.nds.dirxml.driver.jdbc.db.lock.OraLockGenerator |

The default exclusion filter omits dropped tables from the synchronization schema.

### Limitations

LONG, LONG RAW, and BLOB columns cannot be referenced in a trigger. You can’t reference columns of these types by using the :NEW qualifier in a trigger, including instead-of-triggers.

## 13.3.13 PostgreSQL

* [Database Properties](characteristics-of-databases.html#bgz0wui)
* [Known Issues](characteristics-of-databases.html#bw1tu6a)

### Database Properties

*Table 13-19* Settings for PostgreSQL

| Property | Value |
| Current Timestamp Statement | SELECT (CURRENT\_TIMESTAMP) |
| Case-Sensitive? | No |
| Commit Keyword | COMMIT |
| Left Outer Join Operator | LEFT OUTER JOIN |

### Known Issues

PostgreSQL does not support <check-object-password> events. You control authentication by manually inserting entries into the pg\_hba.conf file.

## 13.3.14 Sybase Adaptive Server Enterprise (ASE)

* [Database Properties](characteristics-of-databases.html#bgz0xb5)
* [Dynamic Defaults](characteristics-of-databases.html#bvoxw0o)
* [Known Issues](characteristics-of-databases.html#btezy6z)

### Database Properties

*Table 13-20* Settings for Sybase ASE

| Property | Value |
| Current Timestamp Statement | SELECT GETDATE() |
| Case-Sensitive? | Yes |
| Commit Keyword | GO |
| Left Outer Join Operator | \*= |

### Dynamic Defaults

The following table lists database compatibility parameters that the JDBC driver implicitly sets at runtime. Do not explicitly overwrite these settings.

*Table 13-21* Dynamically Configured Sybase ASE Settings

| Display Name | Tag Name | Value |
| Current timestamp statement | current-timestamp-stmt | SELECT GETDATE() |
| Left outer-join operator | left-outer-join-operator | \*= |
| Timestamp Translator class | time-translator-class | com.novell.nds.dirxml.driver.jdbc.db.SybaseTimestamp |

### Known Issues

* Padding and truncation of binary values.

  To ensure ANSI-compliant padding and truncation behavior for binary values, make sure that binary column types (other than IMAGE) meet the following criteria:

  + They are exactly the size of the eDirectory™ attribute that maps to them.
  + They are constrained NOT NULL.
  + They are added to the Publisher and Subscriber Creation policies.

  If they are constrained NULL, trailing zeros, which are significant to eDirectory, are truncated. If binary columns exceed the size of their respective eDirectory attributes, extra 0s are appended to the value.

  The recommended solution is to use only the IMAGE data type when synchronizing binary values.
* DATETIME fractions of a second are rounded. Sybase Timestamps are at best accurate to 1/300th of a second (approximately.003 seconds). The database server rounds to the nearest 1/300th of a second as opposed to the nearest 1/1000th of a second (.001 seconds or 1 millisecond).
* Timestamp formats are proprietary.
