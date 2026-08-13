# 6.3 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment. The following table summarizes all driver-level parameters and their properties:

*Table 6-4* Driver Parameters and Properties

| Display Name | Tag Name | Sample Value | Default Value | Required |
| Third-Party JDBC Driver Class Name | jdbc-class | oracle.jdbc.driver.OracleDriver | (none) | yes |
| Preserve white space in SQL statements? | preserve-sqlwhitespace | yes | no | yes |
| Synchronization Filter | sync-filter | schema (include by schema membership) | (none) | no |
| Time Syntax | time-syntax | 1 (integer) | 1 (integer) | no |
| State directory | state-dir | . (current directory) | . (current directory) | no |
| Use Minimal Number of Connections? | use-single-connection | 0 (no) | (dynamic3) | no |
| Connection Initialization Statements | connection-init | USE idm | (none) | no |
| Connection Properties | connection-properties | USER={$username}; PASSWORD={$password} | (dynamic3) | no |
| JDBC Driver Descriptor Filename | jdbc-driver-descriptor | ora\_client\_thin.xml | (none) | no |
| Database Descriptor Filename | database-descriptor | ora\_11i.xml | (none) | no |
| Enable Referential Attribute Support? | enable-refs | 1 (yes) | 1 (yes) | no |
| Enable Meta-Identifier Support? | enable-meta-identifiers | 1 (yes) | 1 (yes) | no |
| Use Manual Transactions? | use-manual-transactions | 1 (yes) | (dynamic2) | no |
| Transaction Isolation Level | transaction-isolation-level | read committed | (dynamic3) | no |
| Reuse Statements? | reuse-statements | 1 (reuse) | (dynamic3) | no |
| Number of Returned Result Sets | handle-stmt-results | one | (dynamic3) | no |
| Enable Statement-Level Locking? | enable-locking | 1 (yes) | 0 (no) | no |
| Force Username Case | force-username-case | upper (to uppercase) | (none) | no |
| Left Outer Join Operator | left-outer-join-operator | (+) | (dynamic3) | no |
| Retrieve Minimal Metadata | minimal-metadata | 0 (no) | (dynamic3) | no |
| Function Return Method | function-return-method | result set | (dynamic3) | no |
| Supports Schemas in Metadata Retrieval? | supports-schemas-in-metadata-retrieval | 1 (yes) | (dynamic3) | no |
| Sort Column Names By | column-position-comparator | com.novell.nds.dirxml.driver.jdbc.util.config.comp.StringByteComparator (hexadecimal value) | (dynamic3) | no |
| Schema Name | sync-schema | indirect | (none) | yes1 |
| Include Filter Expression | include-table-filter | IDM\_.\* | (none) | no |
| Exclude Filter Expression | exclude-table-filter | BIN\$.{22}==\$0 | (none) | no |
| Table/View Names | sync-tables | usr | (none) | yes1 |
| Lock Statement Generator Class | lock-generator-class | com.novell.nds.dirxml.driver.jdbc.db.lock.OraLockGenerator | (dynamic3) | no |

1 One of these mutually exclusive parameters must be present if the Synchronization Filter parameter is not present. See [Synchronization Filter](configure-jdbc-driver-specific-parameters.html#b1pu3k2). 2 This default is derived dynamically at runtime from descriptor files and database metadata. 3 This default is derived dynamically from descriptor files at runtime.

Driver parameters fall into the following subcategories:

* [Uncategorized Parameters](configure-jdbc-driver-specific-parameters.html#b1pu3j8)
* [Database Scoping Parameters](configure-jdbc-driver-specific-parameters.html#b1pu3k1)
* [Connectivity Parameters](configure-jdbc-driver-specific-parameters.html#b1pu3l5)
* [Compatibility Parameters](configure-jdbc-driver-specific-parameters.html#b1pu3ls)

## 6.3.1 Uncategorized Parameters

* [Third-Party JDBC Driver Class Name](configure-jdbc-driver-specific-parameters.html#b1pu3j9)
* [Time Syntax](configure-jdbc-driver-specific-parameters.html#b1pu3jg)
* [State Directory](configure-jdbc-driver-specific-parameters.html#b1pu3ju)

### Third-Party JDBC Driver Class Name

This parameter is the fully-qualified Java class name of your third-party JDBC driver.

The following table lists the properties of this parameter:

*Table 6-5* Third-Party JDBC Driver Class Name: Properties

| Property | Value |
| Tag Name | jdbc-class |
| Required? | yes |
| Case-Sensitive? | yes |
| Sample Value | oracle.jdbc.driver.OracleDriver |
| Default Value | (none) |

For a list of supported third-party JDBC driver classnames, see [JDBC Driver Class Names](supported-third-party-jdbc-drivers.html#bvx38mr).

### Time Syntax

The Time Syntax parameter specifies the format of time-related data types that the driver returns. The format can be any of the following options:

* [Return Database Time, Date, and Timestamp Values as 32-Bit Integers](configure-jdbc-driver-specific-parameters.html#b77q105)
* [Return Database Time, Date, and Timestamp Values as Canonical Strings](configure-jdbc-driver-specific-parameters.html#b77q1sh)
* [Return database Time, Date, and Timestamp Values in their Java String Representation as Returned by the Method toString():java.lang.String](configure-jdbc-driver-specific-parameters.html#b77q2h9)

#### Return Database Time, Date, and Timestamp Values as 32-Bit Integers

This is the default.

eDirectory Time and Timestamp syntaxes are composed of unsigned, 32-bit integers that express the number of whole seconds that have elapsed since 12:00 a.m., January 1st, 1970 UTC. The maximum range of this data type is approximately 136 years. When interpreted as unsigned integers (as originally intended), these syntaxes are capable of expressing dates and times to the second in the range of 1970 to 2106. When interpreted as a signed integer, these syntaxes are capable of expressing dates and times to the second in the range of 1901 to 2038.

This option has two problems:

* Identity Vault Time and Timestamp syntaxes cannot express as large a date range as database Date or Timestamp syntaxes.
* Identity Vault Time and Timestamp syntaxes are granular to the second. Database Timestamp syntaxes are often granular to the nanosecond.

The second and third options overcome these two limitations.

Map the database Time, Date, and Timestamp values to eDirectory attributes of type Time or Timestamp.

#### Return Database Time, Date, and Timestamp Values as Canonical Strings

The following table shows abstract database data types and their corresponding canonical string representations:

*Table 6-6* Database Types and Canonical String Representations

| JDBC Data Type | Canonical String Format1 |
| java.sql.Time | HHMMSS |
| java.sql.Date | CCYYMMDD |
| java.sql.Timestamp | CCYYMMDDHHMMSSNNNNNNNNN |

C = century, Y = year, M = month D = day, H = hour, M= minute, S = second, N = nano

These fixed-length formats collate in chronological order on any platform in any locale. Even though the precision of nanoseconds varies by database, the length of Timestamps does not.

Map the database Time, Date, and Timestamp values to attributes of type Numeric String.

#### Return database Time, Date, and Timestamp Values in their Java String Representation as Returned by the Method toString():java.lang.String

The following table shows abstract database data types and their corresponding Java String representations:

*Table 6-7* Database Types and Java String Formats

| JDBC Data Type | Java String Format1 |
| java.sql.Time | hh:mm:ss |
| java.sql.Date | yyyy-mm-dd |
| java.sql.Timestamp | yyyy-mm-dd hh:mm:ss.fffffffff |

y= year, m= month, d= day, h= hour, m= minute, s= second, f= nano

These fixed-length formats collate in chronological order on any platform in any locale. The precision of nanoseconds, and therefore the length of Timestamps, varies by database.

Map the database Time, Date, and Timestamp values to attributes of type Case Ignore/Case Exact String.

The following table lists the properties of the Time Syntax parameter:

*Table 6-8* Time Syntax: Properties

| Property | Value |
| Tag Name | time-syntax |
| Required? | no |
| Default Value | 1 (integer) |
| Legal Values | 1 (integer) 2 (canonical string) 3 (java string) |
| Schema-Dependent? | True |

### State Directory

The State Directory parameter specifies where a driver instance should store state data. The state data is currently used for both triggered and triggerless publication. For more information, see [Triggered Publication Parameters](how-to-set-publication-parameters.html#bvsjvfe) and [Triggerless Publication Parameters](how-to-set-publication-parameters.html#bvsjvlr). The state data might be used to store additional state information in the future.

Each driver instance can have a maximum of four state files with a unique file format, such as:

* jdbc\_<driver instance guid> - Triggerless Publication (only used for Triggerless configured drivers)
* jdbc\_<driver instance guid>\_0 - Subscriber Query
* jdbc\_<driver instance guid>\_1 - Publisher Query
* jdbc\_<driver instance guid>\_2 - Subscriber Service Query

For example, jdbc\_bd2a3dd5-d571-4171-a195-28869577b87e\_0

Defunct state files (those belonging to deleted drivers) in the state directory are deleted each time a driver instance with the same state directory is started.

#### Changes That Can Force Triggerless Publisher Resynchronization

If you delete state files, the triggerless publisher will build new state files by resynchronizing. If you move the JDBC driver without moving the state files, the triggerless publisher builds new state files by resynchronizing. Changing to and from the Remote Loader is a move. Therefore, if you move the JDBC driver using triggerless publication and want to prevent a full resynchronization, also move the jdbc\_<GUID> file in the state directory.

When you move your driver to a new server, the process includes creating a new driver object on the new server. The newly created driver object will have its own GUID. Therefore, copying the state files of the old driver to the new server does not work even if the driver versions are same (or have the same state file extensions). In order to prevent resynchronization, ensure that Triggerless Publication Legal Values 2 (process future changes only) option is set in the driver properties.

If more than two files exist in the specified state directory, you must look up the GUID to know which files belong to the driver instance being moved. To identify a driver instance’s state files, you can use DSTrace. For convenience, the Identity Manager engine traces each driver's GUID in DSTrace on startup.

If no value is provided for the state directory parameter, or the value is a period (.), the state directory is the current directory. The current directory depends upon the following:

* The platform that the driver is running on
* Whether the driver is running locally or remotely

When a process is started, a default directory in the file system is assigned to it. The default directory is the current directory. If you don't supply a value, the default State Directory is the current directory (the one that the process is running in).

*Table 6-9* Default Directories

| Platform or Environment | Default Directory |
| Linux and Solaris, for the Remote Loader | /opt/novell/dirxml |
| Linux and Solaris, for Identity Manager (local; not on the Remote Loader) | /var/opt/novell/eDirectory/data/dib/ |
| Windows, for the Remote Loader | novell\remoteloader |
| Windows, for Identity Manager (local; not on the Remote Loader) | c:\novell\nds\dibfiles |

The current directory might be different for a custom installation.

No data is lost when resynchronization occurs, although additional data might remain. For example, because deletes are not captured, users that were deleted in the database during the move will not be disabled/deleted (depending upon the policy).

Moving the driver is not to be undertaken whimsically. As a rule of thumb, don't move the driver unless you must do so.

#### Properties

The following table lists the properties of the State Directory parameter:

*Table 6-10* State Directory: Properties

| Property | Value |
| Tag Name | state-dir |
| Required? | no |
| Case-Sensitive? | platform-dependent |
| Sample Value | c:\novell\nds\DIBFiles |
| Default Value | . (current directory) |

## 6.3.2 Database Scoping Parameters

* [Synchronization Filter](configure-jdbc-driver-specific-parameters.html#b1pu3k2)
* [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka)
* [Include Filter Expression](configure-jdbc-driver-specific-parameters.html#b1pu3kh)
* [Exclude Filter Expression](configure-jdbc-driver-specific-parameters.html#b1pu3kp)
* [Table/View Names](configure-jdbc-driver-specific-parameters.html#b1pu3kx)

### Synchronization Filter

The Synchronization Filter parameter determines which database objects, such as tables and views, are members of the synchronization schema (the set of tables/views visible to the driver at runtime). With the addition of this parameter, the driver can now run in two modes: schema-aware or schema-unaware.

#### Schema-Unaware Mode

When the Synchronization Filter parameter is present and set to empty (exclude all tables/views), the driver is schema-unaware. It does not retrieve table/view metadata on startup. Therefore, no metadata methods are required. See [Section F.0, java.sql.DatabaseMetaData Methods](java-sql-databasemetadata-jdbc.html).

When it is schema-unaware, the synchronization schema can be empty. Both the Schema Name and Sync Tables/Views parameters are completely ignored. Neither is required. Both can be absent, present, valued or valueless. See [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka) and [Table/View Names](configure-jdbc-driver-specific-parameters.html#b1pu3kx).

In schema-unaware mode, the driver acts as a passthrough agent for embedded SQL. In this state, standard XDS events (for example, Add, Modify, and Delete) are ignored. See [Section 12.0, Embedded SQL Statements in XDS Events](embed-sql-statements-in-xds-events-for-jdbc-driver.html). Also, triggered or triggerless publication no longer work.

#### Schema-Aware Mode

When the Synchronization Filter parameter is not present or set to a value other than empty (exclude all tables/views), the driver is schema-aware. It retrieves table/view metadata on a limited number of tables/views to facilitate data synchronization. You can cache metadata on all tables/views owned by a single database user (include by schema membership), or cache metadata on an explicit list of table/view names (include by table/view name). When schema-aware, the driver retrieves database table/view metadata on startup. For a list of required metadata methods, see [Section F.0, java.sql.DatabaseMetaData Methods](java-sql-databasemetadata-jdbc.html).

When schema-aware, parameter Schema Name or Table/View Names must be present and have a value. Because these two parameters are mutually exclusive, only one parameter can have a value. See [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka) and [Table/View Names](configure-jdbc-driver-specific-parameters.html#b1pu3kx).

The following table lists the parameters that require the driver to be schema-aware. When the driver is schema-unaware, these parameters do not have any effect on driver behavior.

*Table 6-11* Schema-Dependent Parameters

| Parameter |
| Lock Statement Generator Class |
| Enable Referential Attribute Support? |
| Enable Meta-Identifier Support? |
| Left Outer Join Operator |
| Retrieve Minimal Metadata |
| Supports Schemas in Metadata Retrieval? |
| Sort Column Names By |
| Disable Statement-Level Locking |
| Check Update Counts? |
| Add Default Values on Insert? |
| Generation/Retrieval Method (Table-Global) |
| Retrieval Timing (Table-Global) |
| Retrieval Timing |
| Disable Publisher? |
| Disable Statement-Level Locking? |
| Publication Mode |
| Enable Future Event Processing? |
| Event Log Table Name |
| Delete Processed Rows? |
| Allow Loopback? |
| Startup Option |
| Polling Interval (In Seconds) |
| Publication Time of Day |
| Post Polling Statements |
| Batch Size |

The following table lists the properties of the Synchronization Filter parameter:

*Table 6-12* Synchronization Filter: Properties

| Property | Value |
| Tag Name | sync-filter |
| Required? | no |
| Case-Sensitive? | no |
| Sample Value | list |
| Legal Values | empty (exclude all tables/views), schema (include by schema membership), list (include by table/view name) |
| Default Value: | (none) |

### Schema Name

The Schema Name parameter identifies the database schema being synchronized. A database schema is analogous to the name of the owner of the tables or views being synchronized. For example, to synchronize two tables, usr and grp, each belonging to database user idm, you enter idm as this parameter’s value. For more information about the Schema Name use cases, see [Schema Name Use Cases](schema-name-use-cases-for-jdbc-driver.html).

When using this parameter instead of Table/View Names, names of database objects are implicitly schema-qualified by the driver. As such, parameters referencing stored procedure, function, or table names do not need to be schema-qualified unless they reside in a schema other than the one specified here. In particular, Method and Timing (Table-Local) and Event Log Table Name are affected. See [Table/View Names](configure-jdbc-driver-specific-parameters.html#b1pu3kx), [Method and Timing (Table-Local)](how-to-set-subscription-parameters.html#bvul7v5), and [Event Log Table Name](how-to-set-publication-parameters.html#bvw4elt).

The following table lists the properties of the Schema Name parameter:

*Table 6-13* Schema Name: Properties

| Property | Value |
| Tag Name | sync-schema |
| Required? | yes |
| Case-Sensitive? | See [Undelimited Identifier Case Sensitivity](characteristics-of-databases.html#bvqzikw). |
| Sample Value | indirect |
| Default Value: | (none) |

When the Schema Name parameter is used without the Synchronization Filter parameter, the Table/View Names parameter must be left empty or omitted from a configuration. See [Synchronization Filter](configure-jdbc-driver-specific-parameters.html#b1pu3k2) and [Table/View Names](configure-jdbc-driver-specific-parameters.html#b1pu3kx).

Changing the value of the Schema Name parameter forces a resync of all objects when triggerless publication is used.

### Include Filter Expression

The Include Filter Expression parameter is only operative when the Schema Name parameter is used. See [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka).

The following table lists the properties of the Include Filter Expression parameter:

*Table 6-14* Include Filter Expression: Properties

| Property | Value |
| Tag Name | include-table-filter |
| Required? | no |
| Case-Sensitive? | yes |
| Sample Value | idm\_.\* (all table/view names starting with “idm\_”) |
| Default Value | (none) |
| Legal Values | (any legal Java regular expression) |

### Exclude Filter Expression

This parameter is only operative when the Schema Name parameter is used. See [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka).

The following table lists the properties of the Exclude Filter Expression parameter:

*Table 6-15* Exclude Filter Expression: Properties

| Property | Value |
| Tag Name | exclude-table-filter |
| Required? | no |
| Case-Sensitive? | yes |
| Sample Value | bin.\* (all table/view names starting with “bin”) |
| Default Value | (none) |
| Legal Values | (any legal Java regular expression) |

### Table/View Names

The Table/View Names parameter allows you to create a logical database schema by listing the names of the logical database classes to synchronize. Logical database class names are the names of parent tables and views. It is incorrect to list child table names.

This parameter is particularly useful for synchronizing with databases that do not support the concept of schema, such as MySQL, or when a database schema contains a large number of tables or views of which only a few are of interest. Reducing the number of table/view definitions cached by the driver can shorten startup time as well as reduce runtime memory utilization.

When using this parameter instead of Schema Name, you probably need to schema-qualify other parameters that reference stored procedure, function, or table names. In particular, the Method and Timing (Table-Local) and Event Log Table Name parameters are affected. See [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka), [Method and Timing (Table-Local)](how-to-set-subscription-parameters.html#bvul7v5) and [Event Log Table Name](how-to-set-publication-parameters.html#bvw4elt).

The following table lists the properties of the Table/View Names parameter:

*Table 6-16* Table/View Names: Properties

| Property | Value |
| Tag Name | sync-tables |
| Required? | yes |
| Case-Sensitive? | See [Undelimited Identifier Case Sensitivity](characteristics-of-databases.html#bvqzikw). |
| Delimiters | semicolon, white space, comma |
| Sample Value | indirect.usr; indirect.grp |
| Default Value | (none) |

When this parameter is used without the Synchronization Filter parameter, the Schema Name parameter must be left empty or omitted from a configuration. See [Synchronization Filter](configure-jdbc-driver-specific-parameters.html#b1pu3k2) and [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka).

Changing anything in the Table/View Name parameter other than URL properties forces a resynchronization of all objects when triggerless publication is used.

## 6.3.3 Connectivity Parameters

* [Use Minimal Number of Connections?](configure-jdbc-driver-specific-parameters.html#b1pu3l6)
* [Connection Initialization Statements](configure-jdbc-driver-specific-parameters.html#b1pu3lc)
* [Connection Properties](configure-jdbc-driver-specific-parameters.html#b1pu3lk)

### Use Minimal Number of Connections?

The Use Minimal Number of Connections? parameter specifies whether the driver should use two instead of three database connections.

By default, the driver uses three connections: one for subscription, and two for publication. The Publisher channel uses one of its two connections to query for events and the other to facilitate query-back operations.

When this parameter is set to Boolean True, the number of required database connections is reduced to two. One connection is shared between the Subscriber and Publisher channels. It is used to process subscription and publication query-back events. The other is used to query for publication events.

In previous versions, the driver was able to support bidirectional synchronization by using a single connection. The publication algorithm was redesigned to increase performance, enable support for future event processing, and to overcome limitations of the previous algorithm at the expense of requiring an additional connection.

*Table 6-17* Use Minimal Number of Connections?: Properties

| Property | Value |
| Tag Name | use-single-connection |
| Required? | no |
| Default Value | (dynamic) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | False |

The Default Value property is derived dynamically from descriptor files at runtime. Otherwise, the default value is Boolean False.

Setting this parameter to Boolean True reduces performance.

### Connection Initialization Statements

The Connection Initialization Statements parameter specifies what SQL statements, if any, should be executed immediately after connecting to the target database. Connection initialization statements are useful for changing database contexts and setting session properties. These statements are executed each time the driver, irrespective of channel, connects or reconnects to the target database.

The following table lists the properties of this parameter:

*Table 6-18* Connection Initialization Statements: Properties

| Property | Value |
| Tag Name | connection-init |
| Required? | no |
| Case-Sensitive? | See [Undelimited Identifier Case Sensitivity](characteristics-of-databases.html#bvqzikw). |
| Delimiters | semicolon |
| Sample Value | USE idm; SET CHAINED OFF |
| Default Value | (none) |
| Schema-Dependent | False |

### Connection Properties

The Connection Properties parameter specifies authentication properties. This parameter is useful for specifying properties that cannot be set via the JDBC URL specified in the Authentication Context parameter. See [Authentication Context](jdbc-driver-parameters.html#bvqz35i).

The primary purpose of this parameter is to enable encrypted transport for third-party JDBC drivers. For a list of relevant connection properties, see [Sybase Adaptive Server Enterprise JConnect JDBC Driver](supported-third-party-jdbc-drivers.html#bvng4bc) and [Oracle Thin Client JDBC Driver](supported-third-party-jdbc-drivers.html#bvlst6q).

Connection properties are specified as key-value pairs. The key is specified as the value to the left of the “=” character. The value is the value to the right of the “=” character. You can specify multiple key-value pairs, but each pair must be delimited by the “;” character.

When you use the Connection Properties parameter, authentication information can be passed via the JDBC URL specified in the Authentication Context parameter or here. See [Authentication Context](jdbc-driver-parameters.html#bvqz35i).

If specified as connection properties, value tokens can be used as placeholders for the database username specified in the Authentication ID parameter and the password specified in the Application Password parameter. See [Authentication ID](jdbc-driver-parameters.html#bvqz2y8) and [Application Password](jdbc-driver-parameters.html#bvqz3f5). For username, the token is {$username}. For password, the token is {$password}.

The following table lists the properties of this parameter:

*Table 6-19* Connection Properties: Properties

| Property | Value |
| Tag Name | connection-properties |
| Required? | no |
| Case-Sensitive? | third-party JDBC driver-dependent |
| Delimiters | semicolon |
| Sample Value | user={$username}; password={$password}; oracle.jdbc.defaultNChar=true |
| Default Value | (none) |
| Schema-Dependent | False |

Each connection property is a key value pair. You can add any number of connection properties in the driver configuration. You must append username and password (user={$username}; password={$password}) to the additional connection properties. Separate each connection property using delimiters.

## 6.3.4 Compatibility Parameters

* [JDBC Driver Descriptor Filename](configure-jdbc-driver-specific-parameters.html#b1pu3lt)
* [Database Descriptor Filename](configure-jdbc-driver-specific-parameters.html#b1pu3m0)
* [Use Manual Transactions?](configure-jdbc-driver-specific-parameters.html#b1pu3m7)
* [Transaction Isolation Level](configure-jdbc-driver-specific-parameters.html#b1pu3me)
* [Reuse Statements?](configure-jdbc-driver-specific-parameters.html#b1pu3ml)
* [Number of Returned Result Sets](configure-jdbc-driver-specific-parameters.html#b1pu3ms)
* [Enable Statement-Level Locking?](configure-jdbc-driver-specific-parameters.html#b1pu3mz)
* [Lock Statement Generator Class](configure-jdbc-driver-specific-parameters.html#b1pu3n5)
* [Enable Referential Attribute Support?](configure-jdbc-driver-specific-parameters.html#b1pu3nc)
* [Enable Meta-Identifier Support?](configure-jdbc-driver-specific-parameters.html#b1pu3ni)
* [Force Username Case](configure-jdbc-driver-specific-parameters.html#b1pu3no)
* [Left Outer Join Operator](configure-jdbc-driver-specific-parameters.html#b1pu3nu)
* [Retrieve Minimal Metadata](configure-jdbc-driver-specific-parameters.html#b1pu3o0)
* [Function Return Method](configure-jdbc-driver-specific-parameters.html#b1pu3o6)
* [Supports Schemas in Metadata Retrieval?](configure-jdbc-driver-specific-parameters.html#b1pu3oc)
* [Sort Column Names By](configure-jdbc-driver-specific-parameters.html#b1pu3oi)
* [Preserve white space in SQL statements?](configure-jdbc-driver-specific-parameters.html#bucdlni)

### JDBC Driver Descriptor Filename

The JDBC Driver Descriptor Filename parameter specifies the third-party JDBC descriptor file to use. Descriptor file names must not be prefixed with the underscore character (for example, \_mysql\_jdriver.xml) because such filenames are reserved. Place descriptor files in a jar file beginning with the case-insensitive prefix 'jdbc' (for example jdbcCustomConfig.jar) in the jar file's com/novell/nds/dirxml/driver/jdbc/db/descriptor/db directory.

The following table lists the properties of this parameter:

*Table 6-20* JDBC Driver Descriptor Filename: Properties

| Property | Value |
| Tag Name | jdbc-driver-descriptor |
| Required? | no |
| Case-Sensitive? | platform-dependent |
| Sample Value | my\_custom\_jdbc\_driver\_descriptor.xml |
| Default Value | (none) |
| Schema-Dependent | False |

### Database Descriptor Filename

The Database Descriptor Filename parameter specifies the database descriptor file to use. Do not use the underscore character in prefixes to Descriptor filenames (for example, \_mysql.xml). Such names are reserved. Place Descriptor files in a jar file beginning with the case-insensitive prefix “jdbc” (for example, JDBCCustomConfig.jar). Also, place Descriptor files in the jar file’s com/novell/nds/dirxml/driver/jdbc/db/descriptor/db directory.

The following table lists the properties of this parameter:

*Table 6-21* Database Descriptor Filename: Properties

| Property | Value |
| Tag Name | jdbc-driver-descriptor |
| Required? | no |
| Case-Sensitive? | platform-dependent |
| Sample Value | my\_custom\_database\_descriptor.xml |
| Default Value | (none) |
| Schema-Dependent | False |

### Use Manual Transactions?

The Use Manual Transactions? parameter specifies whether to use manual or user-defined transactions.

This parameter is primarily used to enable interoperability with MySQL MyISAM table types, which do not support transactions.

When set to Boolean True, the driver uses manual transactions. When set to Boolean False, each statement executed by the driver is executed autonomously (automatically).

The following table lists the properties of this parameter:

*Table 6-22* Use Manual Transactions?: Properties

| Property | Value |
| Tag Name | use-manual-transactions |
| Required? | no |
| Case-Sensitive? | no |
| Default Value | (dynamic) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | False |

The Default Value property is derived dynamically from descriptor files and database metadata at runtime.

To ensure data integrity, set this parameter to Boolean True whenever possible.

### Transaction Isolation Level

The Transaction Isolation Level parameter sets the transaction isolation level for connections that the driver uses. Six values exist:

* unsupported
* none
* read uncommitted
* read committed
* repeatable read
* serializable

Five of the values correspond to the public constants defined in the [java.sql Interface Connection](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Connection.html).

Because some third-party drivers do not support setting a connection’s transaction isolation level to none, the driver also supports the additional non-standardized value of unsupported. [PostgreSQL online documentation](http://www.postgresql.org/docs/current/static/transaction-iso.html) has one of the better, concise primers on what each isolation level actually means.

*IMPORTANT:*The list of supported isolation levels varies by database. For a list of supported transaction isolation levels for supported databases, see [Supported Transaction Isolation Levels](characteristics-of-databases.html#bvw1vdv).

We recommend using a transaction isolation level of read committed because it is the minimum isolation level that prevents the driver from seeing uncommitted changes (dirty reads).

The following table lists the properties of this parameter:

*Table 6-23* Transaction Isolation Level: Properties

| Property | Value |
| Tag Name | transaction-isolation-level |
| Required? | no |
| Case-Sensitive? | no |
| Default Value | (dynamic) |
| Legal Values | unsupported, none, read uncommitted, read committed, repeatable read, serializable |
| Schema-Dependent | False |

The Default Value property is derived dynamically from descriptor files at runtime. Otherwise, the default value is read committed.

### Reuse Statements?

The Reuse Statements? parameter specifies whether one or more java.sql.Statement items are active at a time on a given connection. See [java.sql.Statement](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Statement.html).

This parameter is primarily used to enable interoperability with [Microsoft JDBC Driver for SQL Server](supported-third-party-jdbc-drivers.html#t47303hry5lw)

When set to Boolean True, the driver allocates a Java SQL Statement once and then reuses it. When set to Boolean False, the driver allocates/deallocates statement objects each time they are used, ensuring that no more than one statement is active at a time on a given connection.

The following table lists the properties of this parameter:

*Table 6-24* Reuse Statements?: Properties

| Property | Value |
| Tag Name | reuse-statements |
| Required? | no |
| Case-Sensitive? | no |
| Default Value | (dynamic) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | False |

The Default Vault is derived dynamically from descriptor files at runtime. Otherwise, the default value is Boolean True.

Setting this parameter to Boolean False degrades performance.

### Number of Returned Result Sets

The Number of Returned Result Sets parameter specifies how many java.sql.Result objects can be returned from an arbitrary SQL statement. See [java.sql.ResultSet](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/ResultSet.html).

This parameter is primarily used to avoid infinite loop conditions in [Oracle Thin Client JDBC Driver](supported-third-party-jdbc-drivers.html#bvlst6q) when evaluating the results of arbitrary SQL statements.

The following table lists the properties of this parameter:

*Table 6-25* Number of Returned Result Sets: Properties

| Property | Value |
| Tag Name | handle-stmt-results |
| Required? | no |
| Sample Value | one |
| Default Value | (dynamic) |
| Legal Values | none, no (none) single, one (one) multiple, many, yes (multiple) |
| Schema-Dependent | False |

The Default Value property is derived dynamically from descriptor files at runtime. Otherwise, the default value is multiple, many, or yes.

### Enable Statement-Level Locking?

The Enable Statement-Level Locking? parameter specifies whether the driver explicitly locks database resources before executing SQL statements.

The following table lists the properties of this parameter:

*Table 6-26* Enable Statement-Level Locking?: Properties

| Property | Value |
| Tag Name | enable-locking |
| Required? | no |
| Default Value | 0 (no) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

### Lock Statement Generator Class

The Lock Statement Generator Class parameter specifies which DBLockStatementGenerator implementation to use to generate the SQL statements necessary to explicitly lock database resources for a pending SQL statement. Information on the DBLockStatementGenerator interface is in the Java documents that ship with the driver.

The following table lists the properties of this parameter:

*Table 6-27* Lock Statement Generator Class: Properties

| Property | Value |
| Tag Name | lock-generator-class |
| Required? | no |
| Sample Value | com.novell.nds.dirxml.driver.jdbc.db.lock.OraLockGenerator |
| Default Value | (dynamic) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

Th Default Value property is derived dynamically from descriptor files at runtime. Otherwise, the default value is com.novell.nds.dirxml.driver.jdbc.db.lock.DBLockGenerator.

### Enable Referential Attribute Support?

The Enable Referential Attribute Support? parameter toggles whether the driver recognizes foreign key constraints between logical database classes. These are used to denote containment. Foreign key constraints between parent and child tables within a logical database class are unaffected.

When set to Boolean True, foreign key columns are interpreted as referential. When set to Boolean False, foreign key columns are interpreted as non-referential.

The primary purpose of this parameter is to ensure backward compatibility with the 1.0 version of the driver. For 1.0 compatibility, set this parameter to Boolean False.

The following table lists the properties of this parameter:

*Table 6-28* Enable Referential Attribute Support?: Properties

| Property | Value |
| Tag Name | enable-refs |
| Required? | no |
| Default Value | 1 (yes) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

### Enable Meta-Identifier Support?

The Enable Meta-Identifier Support? parameter toggles whether the driver interprets view column name prefixes such as pk\_ and fk\_ strictly as metadata. When interpreted as metadata, such prefixes are not considered part of the view column name.

For example, when meta-identifier support is enabled, column pk\_idu has an effective column name of idu, prohibiting the existence of another column with the same effective name in the same view. When meta-identifier support is disabled, column pk\_idu has the effective column name of pk\_idu, allowing the existence of another column named idu. Furthermore, when meta-identifier support is enabled, a view with a primary key named pk\_idu would conflict with a table having a primary key column named idu. When meta-identifier support is disabled, they would not conflict.

When set to Boolean True, view column prefixes are interpreted as metadata. When set to Boolean False, view column name prefixes are interpreted as part of the column name proper.

The primary purpose of this parameter is to ensure backward compatibility with the 1.5 version of the driver. For 1.5 compatibility, set this parameter to Boolean False.

The following table lists the properties of this parameter:

*Table 6-29* Enable Meta-Identifier Support?: Properties

| Property | Value |
| Tag Name | enable-meta-identifiers |
| Required? | no |
| Default Value | 1 (yes) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

### Force Username Case

The Force Username Case parameter changes the case of the driver’s username used to authenticate to the target database.

The primary purpose of this parameter is to enable interoperability with the Informix JDBC Driver when used against ANSI-compliant databases. See [Informix JDBC Driver](supported-third-party-jdbc-drivers.html#bvotf30).

The following table lists the properties of this parameter:

*Table 6-30* Force Username Case: Properties

| Property | Value |
| Tag Name | force-username-case |
| Required? | no |
| Default Value | (don’t force) |
| Legal Values | lower (to lowercase), mixed (to mixed case), upper (to uppercase), don’t force (default) |
| Schema-Dependent | False |

### Left Outer Join Operator

The Left Outer Join Operator parameter specifies the left outer join operator used in the triggerless publication query. It might be used for other purposes in the future.

The following table lists the properties of this parameter:

*Table 6-31* Left Outer Join Operator: Properties

| Property | Value |
| Tag Name | left-outer-join-operator |
| Required? | no |
| Default Value | (dynamic) |
| Legal Values | \*= (+) LEFT OUTER JOIN |
| Schema-Dependent | True |

The Default Value property is derived dynamically from descriptor files at runtime. Otherwise, the default value is LEFT OUTER JOIN.

### Retrieve Minimal Metadata

When set to Boolean True, the driver calls only required metadata methods. When set to Boolean False, the driver calls required and optional metadata methods. For a list of required and optional metadata methods, refer to [Section F.0, java.sql.DatabaseMetaData Methods](java-sql-databasemetadata-jdbc.html). Optional metadata methods are required for multivalue and referential attribute synchronization.

*Table 6-32* Retrieve Minimal Metadata: Properties

| Property | Value |
| Tag Name | minimal-metadata |
| Required? | no |
| Default Value | (dynamic) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

The Default Value property is derived dynamically from descriptor files at runtime. Otherwise, the default value is Boolean False.

Setting this value to Boolean True improves startup time and third-party JDBC driver compatibility at the expense of functionality.

### Function Return Method

The Function Return Method parameter specifies how data is retrieved from database functions.

The primary purpose of this parameter is to enable interoperability with the Informix JDBC driver. See [Informix JDBC Driver](supported-third-party-jdbc-drivers.html#bvotf30).

When set to result set, function results are retrieved through a result set. When set to return value, the function result is retrieved as a single, scalar return value.

*Table 6-33* Function Return Method: Properties

| Property | Value |
| Tag Name | function-return-method |
| Required? | no |
| Default Value | (dynamic) |
| Legal Values | result set, return value (scalar return value) |
| Schema-Dependent | False |

The Default Value property is derived dynamically from descriptor files at runtime.

### Supports Schemas in Metadata Retrieval?

The Supports Schemas in Metadata Retrieval? parameter specifies whether schema names should be used when retrieving database metadata.

The primary purpose of this parameter is to enable interoperability with the Informix JDBC Driver when used against ANSI-compliant databases. See [Informix JDBC Driver](supported-third-party-jdbc-drivers.html#bvotf30).

When set to Boolean True, schema names are used. When set to Boolean False, they are not.

*Table 6-34* Supports Schemas in Metadata Retrieval?: Properties

| Property | Value |
| Tag Name | supports-schemas-in-metadata-retrieval |
| Required? | no |
| Default Value | (dynamic) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | False |

The Default Value property is derived dynamically from descriptor files at runtime. Otherwise, the default value is Boolean True.

### Sort Column Names By

The Sort Column Names By parameter specifies how column position is to be determined for legacy databases that do not support sorting by column names.

The primary purpose of this parameter is to enable interoperability with legacy databases, such as DB2/AS400.

Sorting columns names by hexadecimal value ensures that if a driver instance is relocated to a different server, it continues to function without modification. Sorting column names by platform or locale string collation order is more intuitive, but might require configuration changes if a driver instance is relocated to a different server. In particular, log table column order and compound column name order might change. In the case of the latter, Schema-Mapping policies and object association values might need to be updated. In the case of the former, log table columns might have to be renamed.

It is also possible to specify any fully-qualified Java class name as long as the following occur:

* The Java class name implements the [java.util.Comparator](http://java.sun.com/j2se/1.5.0/docs/api/java/util/Comparator.html) interface.
* The Java class name accepts [java.lang.String](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html) arguments.
* The class is in the runtime classpath.

*Table 6-35* Sort Column Names By: Properties

| Property | Value |
| Tag Name | column-position-comparator |
| Required? | no |
| Default Value | (dynamic) |
| Legal Values | com.novell.nds.dirxml.driver.jdbc.util.config.comp.StringByteComparator (hexadecimal value), com.novell.nds.dirxml.driver.jdbc.util.config.comp.StringComparator (string collation order), (any java.util.Comparator that accepts java.lang.String arguments) |
| Schema-Dependent | True |

The Default Value property is derived dynamically from descriptor files at runtime. Otherwise, the default value is com.novell.nds.dirxml.driver.jdbc.util.config.comp.StringByteComparator.

*IMPORTANT:*After you set this parameter for a given configuration, don’t change the parameter.

### Preserve white space in SQL statements?

The Preserve white space in SQL statements? parameter specifies whether trailing spaces in the field names of the SQL statements should be removed or not.

The primary purpose of this parameter is to remove the unintentional trailing spaces from the field names.

If the option is set to no, the trailing spaces are removed from the fields. Set the option to yes, if you do not want to remove the trailing whitespaces.

*Table 6-36* Preserve white space in SQL statements?: Properties

| Property | Value |
| Tag Name | preserve-sql-whitespace |
| Required? | yes |
| Default Value | no |
| Legal Values | yes, no |
| Schema-Dependent | False |

*NOTE:*When the Preserve white space in SQL statements? parameter is set to no, ensure that you do not add trailing spaces, because extra spaces are removed while formatting.
