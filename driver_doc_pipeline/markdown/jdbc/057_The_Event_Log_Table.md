# 11.0 The Event Log Table

The event log table stores publication events. This section describes the structure and capabilities of the event log table.

You can customize the name of the event log table and its columns to avoid conflicts with reserved database keywords. The order, number, and data types of its columns, however, are fixed. In databases that are unaware of column position, order is determined by the Sort Column Names By parameter. See [Sort Column Names By](configure-jdbc-driver-specific-parameters.html#b1pu3oi).

Events in this table can be ordered either by order of insertion (the record\_id column) or chronologically (the event\_time column). Ordering events chronologically allows event processing to be delayed. To order publication events chronologically, set the Enable Future Event Processing parameter to Boolean True. See [Enable Future Event Processing?](how-to-set-publication-parameters.html#bvw4xdy).

* [Event Log Columns](jdbc-event-log-columns.html)
* [Event Types](jdbc-event-types.html)
