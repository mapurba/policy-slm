# E.0 Supported Data Types

The JDBC driver can synchronize all JDBC 1 data types and a small subset of JDBC 2 data types. How JDBC data types map to a database’s native data types depends on the third-party driver.

The following list includes the supported JDBC 1 [java.sql.Types](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Types.html).

Numeric Types:

* java.sql.Types.BIGINT
* java.sql.Types.BIT
* java.sql.Types.DECIMAL
* java.sql.Types.DOUBLE
* java.sql.Types.NUMERIC
* java.sql.Types.REAL
* java.sql.Types.FLOAT
* java.sql.Types.INTEGER
* java.sql.Types.SMALLINT
* java.sql.Types.TINYINT

String Types:

* java.sql.Types.CHAR
* java.sql.Types.LONGCHAR
* java.sql.Types.VARCHAR

Time Types:

* java.sql.Types.DATE
* java.sql.Types.TIME
* java.sql.Types.TIMESTAMP

Binary Types:

* java.sql.Types.BINARY
* java.sql.Types.VARBINARY
* java.sql.Types.LONGVARBINARY

The following list includes the supported JDBC 2 [java.sql.Types](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Types.html).

Large Object (LOB) Types:

* java.sql.Types.CLOB
* java.sql.Types.BLOB
