# 6.5 Publication Parameters

The following table summarizes publisher-level parameters and their properties:

*Table 6-46* Publisher-Level Parameters and Properties

| Display Name | Tag Name | Sample Value | Default Value | Required |
| [Disable Publisher?](how-to-set-publication-parameters.html#bvvpof4) | disable | 1 (yes) | 0 (no) | no |
| [Disable Statement-Level Locking?](how-to-set-publication-parameters.html#bvwo5gx) | disable-locking | 1 (yes) | 0 (no) | no |
| [Publication Mode](how-to-set-publication-parameters.html#bvvpst8) | publication-mode | 2 (triggerless) | 1 (triggered) | yes |
| [Event Log Table Name](how-to-set-publication-parameters.html#bvw4elt) | log-table | indirect\_process | (none) | yes1 |
| [Delete Processed Rows?](how-to-set-publication-parameters.html#bvw4wwk) | delete-from-log | 0 (no) | 1 (yes) | no |
| [Allow Loopback?](how-to-set-publication-parameters.html#bvw4x51) | allow-loopback | 1 (yes) | 0 (no) | no |
| [Enable Future Event Processing?](how-to-set-publication-parameters.html#bvw4xdy) | handle-future-events | 1 (yes) | 0 (no) | no |
| [Startup Option](how-to-set-publication-parameters.html#bvsjvlr) | startup-option |  |  | no |
| [Polling Interval (In Seconds)](how-to-set-publication-parameters.html#bvvpukh) | polling-interval | 60 | 10 | no2 |
| [Publication Time of Day](how-to-set-publication-parameters.html#bvvpxyj) | time-of-day | 15:30:00 | (none) | no2 |
| [Post Polling Statements](how-to-set-publication-parameters.html#bvvq2gw) | post-poll-stmt | DELETE FROM direct.direct\_process | (none) | yes |
| [Batch Size](how-to-set-publication-parameters.html#bvwoevb) | batch-size | 16 | 1 | no |
| [Query Limit (default 10000)](how-to-set-publication-parameters.html#b13cfckw) | query-limit | 1000 | 10000 | no |
| [Heartbeat Interval (In Minutes)](how-to-set-publication-parameters.html#bvwoexw) | pub-heartbeat-interval | 10 | 1 | no |

1 Required for triggered publication mode. 2 These parameters are mutually exclusive.

Publication parameters fall into four major subcategories:

* [Uncategorized Parameters](how-to-set-publication-parameters.html#bvsjfz7)
* [Triggered Publication Parameters](how-to-set-publication-parameters.html#bvsjvfe)
* [Triggerless Publication Parameters](how-to-set-publication-parameters.html#bvsjvlr)
* [Polling Parameters](how-to-set-publication-parameters.html#bvvz5x1)

## 6.5.1 Uncategorized Parameters

* [Disable Publisher?](how-to-set-publication-parameters.html#bvvpof4)
* [Disable Statement-Level Locking?](how-to-set-publication-parameters.html#bvwo5gx)
* [Publication Mode](how-to-set-publication-parameters.html#bvvpst8)
* [Enable Future Event Processing?](how-to-set-publication-parameters.html#bvw4xdy)

### Disable Publisher?

The Disable Publisher? parameter specifies whether the Publisher channel is disabled. When disabled, the Publisher channel does not query for database events. Unlike the [Disable Subscriber?](how-to-set-subscription-parameters.html#bvujptg) parameter, you can still issue database queries on the Publisher channel to facilitate alternative publication algorithms.

When this parameter is set to Boolean True, the Publisher channel is disabled. When this parameter is set to Boolean False, the Publisher channel is active.

*Table 6-47* Disable Publisher?: Properties

| Property | Value |
| Tag Name | disable |
| Required? | no |
| Default Value | 0 (no) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

### Disable Statement-Level Locking?

The Disable Statement-Level Locking? parameter specifies whether database resources should be explicitly locked on this channel before each SQL statement is executed. This parameter is only active if the [Enable Statement-Level Locking?](configure-jdbc-driver-specific-parameters.html#b1pu3mz) parameter is set to Boolean True.

When this parameter is set to Boolean True, database resources are explicitly locked. When this parameter is set to Boolean False, database resources are not explicitly locked.

*Table 6-48* Disable Statement-Level Locking?: Properties

| Property | Value |
| Tag Name | disable-locking |
| Required? | no |
| Default Value | 0 (no) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

### Publication Mode

The Publication Mode parameter specifies which publication algorithm is used.

When set to 1 (triggered), the Publisher channel polls the event log table for events. When set to 2 (triggerless), the Publisher channel searches all tables/views in the synchronization schema for changes, and synthesizes events.

The following table lists the properties of this parameter:

*Table 6-49* Publication Mode: Properties

| Property | Value |
| Tag Name | publication-mode |
| Required? | yes |
| Default Value | 1 (triggered) |
| Legal Values | 1 (triggered) 2 (triggerless) |
| Schema-Dependent | True |

### Enable Future Event Processing?

For triggered publication, Enable Future Event Processing? specifies whether rows in the event log table are ordered and processed by insertion order (the record\_id column) or chronologically (the event\_time column).

When this parameter is set to Boolean False, rows in the event log table are published by order of insertion. When this parameter is set to Boolean True, rows in the event log table are published chronologically.

For triggerless publication, Enable Future Event Processing specifies whether database local time is published with each event. This additional information can be used to force a retry of future-dated events. In order for this to work, a column specifying when an event should be processed must be part of each logical database class utilizing this feature and placed in the Publisher filter as a notification-only attribute.

Database local time is published as an attribute on each XDS event (for example, add, modify, delete). The attribute name is jdbc:database-local-time, where the jdbc namespace prefix is bound to urn:dirxml:jdbc. The format is the Java string representation of a java.sql.Timestamp: yyyy-mm-dd hh:mm:ss.fffffffff. Depending upon the value of the Time Syntax parameter, the value indicating when an event should be processed can be published as an integer, as a canonical string, or as a Java string. See [Time Syntax](configure-jdbc-driver-specific-parameters.html#b1pu3jg).

Regardless of the publication syntax, this value can be parsed and compared to the database local time value. The following table maps the time syntax to the appropriate parse method.

*Table 6-50* Mapping Time Syntax to Parse Methods

| Time Syntax | Parse Method |
| integer | [java.sql.Timestamp(long)](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Timestamp.html) |
| canonical string | com.novell.nds.dirxml.driver.jdbc.db.DSTime(java.lang.String, java.lang.String, java.lang.String, java.lang.String) |
| java string | [java.sql.Timestamp.valueOf(java.lang.String):java.sql.Timestamp](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Timestamp.html) |

After both time values are in a common Timstamp object representation, they can be compared by using the following methods:

* com.novell.nds.dirxml.driver.jdbc.db.TimestampUtil.before(java.sql.Timestamp, java.sql.Timestamp):boolean
* com.novell.nds.dirxml.driver.jdbc.db.TimestampUtil.after(java.sql.Timestamp, java.sql.Timestamp):boolean

An example policy is provided in [Section L.0, Policy Example: Triggerless Future Event Processing](triggerless-future-event-processing-sample-policy.html).

When this parameter is set to Boolean True, local database time is published with each event. When this parameter is set to Boolean False, this information is omitted.

The following table lists the properties of this parameter:

*Table 6-51* Enable Future Event Processing?: Properties

| Property | Value |
| Tag Name | handle-future-events |
| Required? | no |
| Default Value | 0 (no) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

## 6.5.2 Triggered Publication Parameters

The JDBC driver can use any of four triggered publication parameters.

* [Event Log Table Name](how-to-set-publication-parameters.html#bvw4elt)
* [Delete Processed Rows?](how-to-set-publication-parameters.html#bvw4wwk)
* [Allow Loopback?](how-to-set-publication-parameters.html#bvw4x51)

### Event Log Table Name

The Event Log Table Name parameter specifies the name of the event log table where publication events are stored.

The table specified here must conform to the definition of [Section 11.0, The Event Log Table](what-is-event-log-table-in-jdbc-driver.html).

When using [Table/View Names](configure-jdbc-driver-specific-parameters.html#b1pu3kx), you should explicitly schema-qualify this table name. When you use [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka), this table name is implicitly schema-qualified with that schema name. If this table is located in a schema other than the implicit schema, it must be schema-qualified.

The following table lists the properties of this parameter:

*Table 6-52* Event Log Table Name: Properties

| Property | Value |
| Tag Name | log-table |
| Required? | no |
| Case-Sensitive? | See [Undelimited Identifier Case Sensitivity](characteristics-of-databases.html#bvqzikw). |
| Sample Value | eventlog |
| Default Value | (none) |
| Schema-Dependent | True |

This parameter is required if [Publication Mode](how-to-set-publication-parameters.html#bvvpst8) is set to 1 (triggered publication).

### Delete Processed Rows?

The Delete Processed Rows? parameter specifies whether processed rows are deleted from the event log table.

When this parameter is set to a Boolean True, processed rows are deleted. When this parameter is set to Boolean False, processed row’s status field values are updated.

To mitigate the performance hit caused when processed rows remain in the event log table, we recommend periodically moving the rows into a history table. Do one of the following:

* Call a clean-up stored procedure via the parameter [Post Polling Statements](how-to-set-publication-parameters.html#bvvq2gw).
* Place a before-delete trigger on the event log table to intercept delete events executed against the event log table and to move deleted rows to a history table before they are deleted from the event log table.

The following table lists the properties of this parameter:

*Table 6-53* Delete Processed Rows?: Properties

| Property | Value |
| Tag Name | delete-from-log |
| Required? | no |
| Default Value | 0 (no) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

Setting this parameter to Boolean False degrades publication performance unless processed rows are periodically removed from the event log table.

### Allow Loopback?

The Allow Loopback? parameter specifies whether events caused by the driver’s database user account should be published.

When this parameter is set to Boolean True, loopback events are published. When this parameter is set to Boolean False, loopback events are ignored.

The following table lists the properties of this parameter:

*Table 6-54* Allow Loopback?: Properties

| Property | Value |
| Tag Name | allow-loopback |
| Required? | no |
| Default Value | 0 (no) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

Setting this parameter to Boolean True might degrade performance because extraneous events might be published.

## 6.5.3 Triggerless Publication Parameters

The Startup Option parameter specifies what happens when a triggerless publisher starts.

*Table 6-55* Startup Option: Settings and Results

| Setting | Result |
| 1 | All objects are assumed to have changed and are republished. |
| 2 | Past and present changes are ignored. |
| 3 | All past and present changes are published. |

The following table lists the properties of this parameter:

*Table 6-56* Startup Option: Properties

| Property | Value |
| Tag Name | startup-option |
| Required? | no |
| Default Value | 1 (process all changes) |
| Legal Values | 1 (resync all objects) 2 (process future changes only) 3 (process all changes) |
| Schema-Dependent | True |

The following configuration changes can force a full resynchronization:

* Changing anything in the [Authentication Context](jdbc-driver-parameters.html#bvqz35i) parameter other than URL properties forces a resynchronization of all objects when triggerless publication is used.
* Changing the value of the [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka) parameter or the [Table/View Names](configure-jdbc-driver-specific-parameters.html#b1pu3kx) parameter forces a resynchronization of all objects when triggerless publication is used.
* Changing the [State Directory](configure-jdbc-driver-specific-parameters.html#b1pu3ju) parameter value.
* Moving or deleting state files. See [Changes That Can Force Triggerless Publisher Resynchronization](configure-jdbc-driver-specific-parameters.html#b87rk2y).
* Changing the table/view structure in the database (in particular, changing the position or type of key columns).

## 6.5.4 Polling Parameters

* [Polling Interval (In Seconds)](how-to-set-publication-parameters.html#bvvpukh)
* [Publication Time of Day](how-to-set-publication-parameters.html#bvvpxyj)
* [Post Polling Statements](how-to-set-publication-parameters.html#bvvq2gw)
* [Batch Size](how-to-set-publication-parameters.html#bvwoevb)
* [Query Limit (default 10000)](how-to-set-publication-parameters.html#b13cfckw)
* [Heartbeat Interval (In Minutes)](how-to-set-publication-parameters.html#bvwoexw)

### Polling Interval (In Seconds)

The Polling Interval (In Seconds) parameter specifies how many seconds of inactivity elapse between polling cycles.

The following table lists the properties of this parameter:

*Table 6-57* Polling Interval (In Seconds): Properties

| Property | Value |
| Tag Name | polling-interval |
| Required? | no |
| Default Value | 10 (seconds) |
| Legal Values | 1-604800 (1 week) |
| Schema-Dependent | True |

We recommend that you set this value to no less than 10 seconds.

### Publication Time of Day

The Publication Time of Day parameter specifies at what time, each day, publication begins. Time is understood to mean server local time (the time on the server where the driver is running). You can specify a single time each day, or multiple times.

The following table lists the properties of this parameter:

*Table 6-58* Publication Time of Day: Properties

| Property | Value |
| Tag Name | time-of-day |
| Required? | no |
| Sample Value (Single time) | 13:00:00 (1PM) |
| Sample Value (Multiple times) | 13:00:00 (1 PM), 16:00:00 (4 PM), 20:00:00 (8PM) |
| Default Value | (none) |
| Legal Values | hh:mm:ss (h = hour, m = minute, s = second) |
| Schema-Dependent | True |

This parameter overrides the parameter Polling Interval (In Seconds). See [Polling Interval (In Seconds)](how-to-set-publication-parameters.html#bvvpukh).

### Post Polling Statements

The Post Polling Statements parameter specifies the SQL statements that are executed at the end of each active polling cycle. An active polling cycle is one where some publication activity has occurred.

The primary purpose of this parameter is to allow cleanup of the event log table following publication activity.

You should explicitly schema-qualify any database objects (for example, tables, stored procedures, and functions) referenced in these statements.

The following table lists the properties of this parameter:

*Table 6-59* Post Polling Statements: Properties

| Property | Value |
| Tag Name | post-poll-stmt |
| Required? | yes |
| Case-Sensitive? | See [Undelimited Identifier Case Sensitivity](characteristics-of-databases.html#bvqzikw). |
| Delimiters | semicolon |
| Sample Value | DELETE FROM direct.direct\_process |
| Default Value | (none) |
| Legal Values | (any set of legal SQL statements) |
| Schema-Dependent | True |

### Batch Size

The Batch Size parameter specifies how many events are sent in a single publication document.

Basically, the larger the batch, the better the performance.

* Larger batches necessitate fewer trips across the network in both directions.
* More events in a single document require fewer trips from the Publisher channel to the Identity Manager engine (assuming that query-back events are not being used).
* Larger batches minimize the number of trips from the Publisher channel to the database (assuming that the third-party JDBC driver and database support batch processing).
* Larger batches require fewer commits to state files in the local file system.

  Commits can also be costly.

This parameter defines an upper bound. The Publisher channel might override the specified value under certain conditions. The upper bound of 128 was chosen to minimize the likelihood of overflowing the Java heap and to mitigate delaying termination of the Publisher thread on driver shutdown.

The following table lists the properties of this parameter:

*Table 6-60* Batch Size: Properties

| Property | Value |
| Tag Name | batch-size |
| Required? | no |
| Default Value | 1 |
| Legal Values | 1 to 128 |
| Schema-Dependent | True |

### Query Limit (default 10000)

The Query Limit specifies the maximum number of events that should read from connected system per polling cycle. The default is 10000 events.

*Table 6-61* Query Limit (default 10000): Properties

| Property | Value |
| Tag Name | query limit |
| Required? | yes |
| Default Value | 10000 |
| Legal Values | 0 to 2,147,483,647 (java.lang.Integer.MAX\_VALUE) |
| Schema-Dependent | False |

### Heartbeat Interval (In Minutes)

The Heartbeat Interval (In Minutes) parameter specifies how many minutes the Publisher channel can be inactive before it sends a heartbeat document. In practice, more than the number of minutes specified can elapse. That is, this parameter defines a lower bound. The Publisher channel sends a heartbeat document only if the Publisher channel has been inactive for the specified number of minutes. Any publication document sent is, in effect, a heartbeat document.

The following table lists the properties of this parameter:

*Table 6-62* Heartbeat Interval (In Minutes): Properties

| Property | Value |
| Tag Name | pub-heartbeat-interval |
| Required? | no |
| Default Value | 0 |
| Legal Values | 0 to 2,147,483,647 (java.lang.Integer.MAX\_VALUE) |
| Schema-Dependent | False |
