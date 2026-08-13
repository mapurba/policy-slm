# N.1 Error Codes

* [Error 226: SET CHAINED command not allowed within multi-statement transaction](list-of-error-codes-sybase-jdbc.html#h4un2qmv)
* [Error 7112: Stored procedure 'x' may be run only in chained transaction mode](list-of-error-codes-sybase-jdbc.html#b6tdr3w)
* [Error 7113: Stored procedure 'x' may be run only in unchained transaction mode](list-of-error-codes-sybase-jdbc.html#b6tdr3x)

Error 226: SET CHAINED command not allowed within multi-statement transaction

Effect:
Throws the exception of com.sybase.jdbc2.jdbc.SybSQLException with error code 226 and an SQL state of ZZZZZ.

Cause:
This exception is usually caused by a defect in older versions of jConnect.

Solution:
Download and upgrade to the latest version. Downloads are available at the [jConnect for JDBC Web page](http://www.sybase.com/products/informationmanagement/softwaredeveloperkit/jconnect).

Error 7112: Stored procedure 'x' may be run only in chained transaction mode

Effect:
Throws the exception of com.sybase.jdbc2.jdbc.SybSQLException with error code 7712 and an SQL state of ZZZZZ.

Cause:
The stored procedure was created in chained mode, or later altered to run in chained mode, but the driver is currently running in unchained mode. The probable cause is that the [Use Manual Transactions?](configure-jdbc-driver-specific-parameters.html#b1pu3m7) parameter is set to False. Another possibility is that the transaction type has been overridden to auto in a policy.

Solution:
Do one of the following:

* Use stored procedure sp\_procxmode to change the stored procedure's mode to unchained or anymode (preferred).
* Change the driver's [Use Manual Transactions?](configure-jdbc-driver-specific-parameters.html#b1pu3m7) parameter to True, or change the policy transaction type to manual.

Error 7113: Stored procedure 'x' may be run only in unchained transaction mode

Effect:
Throws the exception com.sybase.jdbc2.jdbc.SybSQLException with error code 7713 and an SQL state of ZZZZZ.

Cause:
The stored procedure was created in unchained mode, or later altered to run in unchained mode, but the driver is currently running in chained mode. The probable cause is that the [Use Manual Transactions?](configure-jdbc-driver-specific-parameters.html#b1pu3m7) parameter is set to True. Another possibility is that the transaction type has been overridden to manual in policy.

Solution:
Do one of the following:

* Use stored procedure sp\_procxmode to change the stored procedure's mode to chained or anymode (preferred).
* Change the driver's [Use Manual Transactions?](configure-jdbc-driver-specific-parameters.html#b1pu3m7) parameter to False, or change the policy transaction type to auto.

If you set use-manual-transactions to False, all transactions consist of a maximum of one statement.
