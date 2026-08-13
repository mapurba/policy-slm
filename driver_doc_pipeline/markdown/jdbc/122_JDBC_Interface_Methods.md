# G.0 JDBC Interface Methods

This section lists the JDBC interface methods (other than [java.sql.DatabaseMetaData](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/DatabaseMetaData.html) methods) that the JDBC driver uses. Methods are organized by class.

Often, third-party JDBC driver vendors list defects or known issues by method. You can use the following methods in collaboration with third-party JDBC driver documentation to troubleshoot or anticipate potential interoperability problems.

* [java.sql.DriverManager](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/DriverManager.html)
* [java.sql.CallableStatement](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/CallableStatement.html)
* [java.sql.Connection](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Connection.html)
* [java.sql.PreparedStatement](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/PreparedStatement.html)
* [java.sql.ResultSet](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/ResultSet.html)
* [java.sql.ResultSetMetaData](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/ResultSetMetaData.html)
* [java.sql.Statement](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Statement.html)
* [java.sql.Timestamp](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Timestamp.html)

The following table lists [java.sql.DriverManager](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/DriverManager.html) methods that the JDBC driver uses:

*Table G-1* java.sql.DriverManager Methods

| Method Signature | JDBC Version | Required? |
| getConnection(String url, java.util.Properties info):java.sql.Connection | 1 | yes1 |
| getConnection(String url, java.util.Properties info):java.sql.Connection | 1 | yes1 |
| setLogStream(java.io.PrintStream out):void | 1 | no |

1Use one method or the other.

The following table lists [java.sql.CallableStatement](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/CallableStatement.html) methods that the JDBC driver uses:

*Table G-2* java.sql.CallableStatement Methods

| Method Signature | JDBC Version | Required? |
| getBigDecimal(int parameterIndex, int scale):java.math.BigDecimal | 1 | yes |
| getBoolean(int parameterIndex):boolean | 1 | yes |
| getBoolean(String parameterName):boolean | 3 | no |
| getByte(int parameterIndex):byte | 1 | yes |
| getByte(String parameterName):byte | 3 | no |
| getBytes(int parameterIndex):byte[] | 1 | yes |
| getBytes(String parameterName):byte[] | 3 | no |
| getDate(int parameterIndex):java.sql.Date | 1 | yes |
| getDate(String parameterName):java.sql.Date | 3 | no |
| getDouble(int parameterIndex):double | 1 | yes |
| getDouble(String parameterName):double | 3 | no |
| getFloat(int parameterIndex):float | 1 | yes |
| getFloat(String parameterName):float | 3 | no |
| getInt(int parameterIndex):int | 1 | yes |
| int getInt(String parameterName) | 3 | no |
| getLong(int parameterIndex):long | 1 | yes |
| getLong(String parameterName):long | 3 | no |
| getShort(int parameterIndex):short | 1 | yes |
| getShort(String parameterName):short | 3 | no |
| getString(int parameterIndex):String | 1 | yes |
| getString(String parameterName):String | 3 | no |
| getTime(int parameterIndex):java.sql.Time | 1 | yes |
| getTime(String parameterName):java.sql.Time | 3 | no |
| getTimestamp(int parameterIndex):java.sql.Timestamp | 1 | yes |
| getTimestamp(String parameterName):java.sql.Timestamp | 3 | no |
| registerOutParameter(int parameterIndex, int sqlType):void | 1 | yes |
| wasNull():boolean | 1 | yes |

The following table lists [java.sql.Connection](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Connection.html) methods that the JDBC driver uses:

*Table G-3* java.sql.Connection Methods

| Method Signature | JDBC Version | Required? |
| close():void | 1 | yes |
| commit():void | 1 | no |
| createStatement():java.sql.Statement | 1 | yes |
| getAutoCommit():boolean | 1 | no |
| getMetaData():java.sql.DatabaseMetaData | 1 | yes |
| getTransactionIsolation():int | 1 | no |
| getWarnings():java.sql.SQLWarning | 1 | no |
| isClosed():boolean | 1 | no |
| prepareCall(String sql):java.sql.CallableStatement | 1 | no |
| prepareStatement(String sql):java.sql.PreparedStatement | 1 | yes |
| rollback():void | 1 | no |
| setAutoCommit(boolean autoCommit):void | 1 | no |
| setTransactionIsolation(int level):void | 1 | no |

The following table lists [java.sql.PreparedStatement](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/PreparedStatement.html) methods that the JDBC driver uses:

*Table G-4* java.sql.PreparedStatement Methods

| Method Signature | JDBC Version | Required? |
| clearParameters() :void | 1 | no |
| execute():boolean | 1 | yes |
| executeQuery():java.sql.ResultSet | 1 | yes |
| executeUpdate():int | 1 | yes |
| setBigDecimal(int parameterIndex, java.math.BigDecimal x):void | 1 | yes |
| setBoolean(int parameterIndex, boolean x):void | 1 | yes |
| setByte(int parameterIndex, byte x):void | 1 | yes |
| setBytes(int parameterIndex, byte x[]):void | 1 | yes |
| setDate(int parameterIndex, java.sql.Date x):void | 1 | yes |
| setDouble(int parameterIndex, double x):void | 1 | yes |
| setFloat(int parameterIndex, float x):void | 1 | yes |
| setInt(int parameterIndex, int x):void | 1 | yes |
| setLong(int parameterIndex, long x):void | 1 | yes |
| setNull(int parameterIndex, int sqlType):void | 1 | yes |
| setShort(int parameterIndex, short x):void | 1 | yes |
| setString(int parameterIndex, String x):void | 1 | yes |
| setTime(int parameterIndex, java.sql.Time x):void | 1 | yes |
| setTimestamp(int parameterIndex, java.sql.Timestamp x):void | 1 | yes |

The following table lists [java.sql.ResultSet](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/ResultSet.html) methods that the JDBC driver uses:

*Table G-5* java.sql.ResultSet Methods

| Method Signature | JDBC Version | Required? |
| close():void | 1 | yes |
| getBigDecimal(int columnIndex, int scale):java.math.BigDecimal | 1 | yes |
| getBigDecimal(String columnName, int scale):java.math.BigDecimal | 1 | yes |
| getBinaryStream(int columnIndex):java.io.InputStream | 1 | yes |
| getBinaryStream(String columnName)java.io.InputStream | 1 | yes |
| getBoolean(int columnIndex):boolean | 1 | yes |
| getBoolean(String columnName):boolean | 1 | yes |
| getByte(int columnIndex):byte | 1 | yes |
| getByte(String columnName):byte | 1 | yes |
| getBytes(int columnIndex):byte[] | 1 | yes |
| getBytes(String columnName):byte[] | 1 | yes |
| getDate(int columnIndex):java.sql.Date | 1 | yes |
| getDate(String columnName)java.sql.Date | 1 | yes |
| getFloat(int columnIndex):float | 1 | yes |
| getFloat(String columnName):float | 1 | yes |
| getInt(int columnIndex):int | 1 | yes |
| getInt(String columnName):int | 1 | yes |
| getLong(int columnIndex):long | 1 | yes |
| getLong(String columnName):long | 1 | yes |
| getMetaData():java.sql.ResultSetMetaData | 1 | no |
| getShort(int columnIndex):short | 1 | yes |
| getShort(String columnName):short | 1 | yes |
| getString(int columnIndex):String | 1 | yes |
| getString(String columnName):String | 1 | yes |
| getTime(int columnIndex):java.sql.Time | 1 | yes |
| getTime(String columnName):java.sql.Time | 1 | yes |
| getTimestamp(int columnIndex):java.sql.Timestamp | 1 | yes |
| getTimestamp(String columnName):java.sql.Timestamp | 1 | yes |
| getWarnings():java.sql.SQLWarning | 1 | no |

The following table lists [java.sql.ResultSetMetaData](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/ResultSetMetaData.html) methods that the JDBC driver uses:

*Table G-6* java.sql.ResultSetMetaData Methods

| Method Signature | JDBC Version | Required? |
| getColumnCount():int | 1 | yes |
| getColumnName(int column):String | 1 | no |
| getColumnType(int column):int | 1 | no |

The following table lists [java.sql.Statement](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Statement.html) methods that the JDBC driver uses:

*Table G-7* java.sql.Statement Methods

| Method Signature | JDBC Version | Required? |
| addBatch(java.lang.String sql):void | 2 | no |
| clearBatch():void | 2 | no |
| clearWarnings():void | 1 | no |
| close():void | 1 | yes |
| execute(java.lang.String sql):boolean | 1 | yes |
| executeBatch():int[] | 2 | no |
| executeUpdate(String sql):int | 1 | yes |
| executeQuery(String sql):java.sql.ResultSet | 1 | yes |
| getGeneratedKeys():java.sql.ResultSet | 3 | no |
| getMoreResults():boolean | 1 | no |
| getResultSet():java.sql.ResultSet | 1 | yes |
| getUpdateCount():int | 1 | no |
| getWarnings():java.sql.SQLWarning | 1 | no |

The following table lists [java.sql.Timestamp](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Timestamp.html) methods that the JDBC driver uses:

*Table G-8* java.sql.Timestamp Methods

| Method Signature | JDBC Version | Required? |
| getNanos():int | 1 | yes |
| getTime():long | 1 | yes |
| setNanos(int n):void | 1 | yes |
| setTime(long time):void | 1 | yes |
| toString ():String | 1 | yes |
