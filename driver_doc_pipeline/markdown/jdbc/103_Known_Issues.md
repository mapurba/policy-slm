# B.1 Known Issues

#### JDBC Driver

* Identity Vault Time and Timestamp syntaxes are inadequate for expressing the range and granularity of their database counterparts. This is a publication problem because database time-related types typically have a wider range and greater degree of granularity (typically nanoseconds). The converse is not true. For more information, see [Time Syntax](configure-jdbc-driver-specific-parameters.html#b1pu3jg).
* The JDBC driver is unable to parse proprietary database time stamp formats. Some databases, such as Sybase and DB2, have proprietary time stamp formats that the [java.sql.Timestamp](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Timestamp.html) class can’t parse. When synchronizing time stamp columns from these databases, the JDBC driver, by default, assumes that time stamp values placed in the event log table are in ODBC canonical format (that is, yyyy-mm-dd hh:mm:ss.fffffffff). The recommended method for enabling the JDBC driver to handle proprietary database time stamp formats is to implement a custom DBTimestampTranslator class. This interface is documented in the JavaDoc Tool that ships with the JDBC driver. Using this approach avoids the problem of reformatting time stamps in the database before they are inserted into the event log table or reformatted in style sheets. The JDBC driver ships with default implementations for the native DB2 time stamp format and the Sybase style 109 time stamp format.
* Statements executed against the database server might block indefinitely.

  Typically, blocking is caused by a database resource being exclusively locked. Because the locking mechanisms and locking SQL vary by database, the general solution to this problem is to implement a custom DBLockStatementGenerator class. For additional information, see [Lock Statement Generator Class](configure-jdbc-driver-specific-parameters.html#b1pu3n5). The JDBC driver ships with a default implementation for Oracle.

  Many factors can cause blocking. To mitigate the likelihood of blocking, we recommend that you do not set the [Transaction Isolation Level](configure-jdbc-driver-specific-parameters.html#b1pu3me) parameter to a level greater than read committed.

  The JDBC interface defines a method [java.sql.Statement.setQueryTimeout(int):void](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Statement.html) that allows a statement to time out after a specified number of seconds. Unfortunately, implementations of this method between third-party JDBC drivers range from not being implemented to having bugs. For this reason, this method was deemed unsuitable as a general-purpose solution.
* The JDBC displays an exception error “User is unassociated" when performing a Modify and/or Delete event with dest-dn. This is because the JDBC driver does not support CRUD operation.
* In MSSQL database you can only add new values to the view only if the view is created from a single base table. If multiple base tables are used to create the view, you cannot update the view.

#### JDBC Fan-Out Driver

* If the Cached Priority Synchronisation event is a modify of the Referential Attribute, the driver sends a Success status. However, the modified change is not updated in the target database.
