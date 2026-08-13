# 11.1 Event Log Columns

This section describes columns in the event log table. Columns are ordered by position.

* [record\_id](jdbc-event-log-columns.html#bgz0aiw)
* [table\_key](jdbc-event-log-columns.html#bgz0aro)
* [status](jdbc-event-log-columns.html#bgz0b60)
* [event\_type](jdbc-event-log-columns.html#bgz0hg5)
* [event\_time](jdbc-event-log-columns.html#bgz0hsv)
* [perpetrator](jdbc-event-log-columns.html#bgz0hx1)
* [table\_name](jdbc-event-log-columns.html#bgz0i3m)
* [column\_name](jdbc-event-log-columns.html#bgz0i7u)
* [old\_value](jdbc-event-log-columns.html#bgz0ibg)
* [new\_value](jdbc-event-log-columns.html#bgz0ifp)

## 11.1.1 record\_id

The record\_id column is used to uniquely identify rows in the event log table and order publication events. This column must contain sequential, ascending, positive, unique integer values. Gaps between record\_id values no longer prematurely end a polling cycle.

## 11.1.2 table\_key

Format values for this column are exactly the same in all triggers for a logical database class. The BNF or Backus Naur Form of this parameter is defined below:

```
<table-key> ::= <unique-row-identifier> {"+"
                <unique-row-identifier>}

<unique-row-identifier> ::= <primary-key-column-name> "=" <value>
```

For example, for the usr table referenced throughout this chapter, this column’s value might be idu=1.

For the view\_usr view referenced throughout this chapter, this column’s value might be pk\_empno=1.

For a hypothetical compound primary key (one containing multiple columns), this column’s value might be pkey1=value1+pkey2=value2.

If primary key values placed in the table\_key field contain any of the special characters {, ; ' + " = \ < >}, where { and } contain the set of special characters, delimit the value with double quotes. You also need to escape the double quote character " as \" and the literal escape character \ as \\ when they are contained inside a pair of double quotes.

For a hypothetical primary key containing special characters, this column’s value might be pkey=", ; ' + \" = \\ < >". (Note the double quotes and escaped characters.)

Differences in padding or formatting might result in out-of-order event processing. For performance reasons, remove any unnecessary white space from numeric values. For example, idu=1 is preferred over idu= 1.

## 11.1.3 status

The status column indicates the state of a given row. The following table lists permitted values:

*Table 11-1* Permitted Values for Status Columns

| Character Value | Interpretation |
| N | new |
| S | success |
| W | warning |
| E | error |
| F | fatal |

To be processed, all rows inserted into the event log table must have a status value of N. The remainder of the status characters are used solely by the Publisher channel to designate processed rows. All other characters are reserved for future use.

Status values are case sensitive.

## 11.1.4 event\_type

Values in this column must be between 1 and 8. All other numbers are reserved for future use.

The following table describes each event type:

*Table 11-2* Event Types

| Event Type | Interpretation |
| 1 | insert field |
| 2 | update field |
| 3 | update field (remove all values) |
| 4 | delete row |
| 5 | insert row (query-back) |
| 6 | update row (query-back) |
| 7 | insert field (query-back) |
| 8 | update field (query-back) |

For additional information on this field, see [Event Types](jdbc-event-types.html).

## 11.1.5 event\_time

This column serves as an alternative ordering column to record\_id. It contains the effective date of the event. It must not be NULL. For this column to become the ordering column, set the Enable Future Event Processing parameter to Boolean True. See [Enable Future Event Processing?](how-to-set-publication-parameters.html#bvw4xdy).

## 11.1.6 perpetrator

This column identifies the database user who instigated the event. A NULL value is interpreted as a user other than the driver user. Rows with a NULL value or value not equal to the driver’s database username are published. Rows with a value equal to the driver’s database username are not published unless the Allow Loopback Publisher parameter is set to Boolean True. See [Allow Loopback?](how-to-set-publication-parameters.html#bvw4x51).

## 11.1.7 table\_name

The name of the table or view where the event occurred.

## 11.1.8 column\_name

The name of the column that was changed. This column is used only for per-field (1-3, 7-8) event types. Nevertheless, it must always be present in the event log table. If it is missing, the Publisher channel cannot start.

## 11.1.9 old\_value

The field’s old value. This column is used only for per-field, non-query-back event types (1-3). Nevertheless, it must always be present in the event log table. If it is missing, the Publisher channel cannot start.

## 11.1.10 new\_value

The field’s new value. This column is used only by per-field, non-query-back event types (1-3). Nevertheless, it must always be present in the event log table. If it is missing, the Publisher channel cannot start.
