# N.2 Procedures and Modes

* [Using Stored Procedure sp\_proxmode](how-to-use-stored-procedures-and-modes-in-jdbc.html#b6tdxdp)
* [Chained and Unchained Modes](how-to-use-stored-procedures-and-modes-in-jdbc.html#b6te18b)
* [Managing Transactions in a Policy](how-to-use-stored-procedures-and-modes-in-jdbc.html#b6tef86)
* [Useful Links](how-to-use-stored-procedures-and-modes-in-jdbc.html#b6tegn4)

## N.2.1 Using Stored Procedure sp\_proxmode

The preferred way to avoid errors 7112 and 7113 is to alter all stored procedures invoked directly or indirectly by the driver (via triggers, for example) to run in both chained and unchained mode. To alter a procedure, invoke the sp\_procxmode procedure with two arguments:.

* The procedure name
* The mode

The following example illustrates how to invoke the sp\_procxmode procedure from the isql command line:

client:sp\_procxmode my\_procedure, anymode go

Of course, not all customers are willing to alter stored procedure modes. Altering a procedure's mode might alter its runtime behavior, which could alter the behavior of other applications that invoke the procedure.

## N.2.2 Chained and Unchained Modes

Unchained mode is Sybase's native way of executing SQL. A second mode, chained mode, was later added to make the database compatible with SQL standards.

*Table N-1* Modes and Compatibility

| Mode | Compatibility |
| Chained | SQL-compatible mode |
| Unchained | Sybase native mode |

Sybase provides a third-party JDBC driver called jConnect. The default mode of jConnect is unchained. Whenever the method Connection.setAutoCommit(boolean autoCommit):void is invoked, jConnect switches modes. See [java.sql Interface Connection](http://java.sun.com/j2se/1.4.2/docs/api/java/sql/Connection.html).

*Table N-2* Methods and Switches

| Method | Effect |
| Connection.setAutoCommit(true) | Switches to unchained mode |
| Connection.setAutoCommit(false) | Switches to chained mode |

If the [Use Manual Transactions?](configure-jdbc-driver-specific-parameters.html#b1pu3m7) parameter is set to False, the driver invokes Connection.setAutoCommit(true). That is, the driver enters unchained mode. This is the normal processing mode for SELECT statements and SQL embedded in a policy where the transaction type is set to auto. See [Manual vs. Automatic Transactions](manual-and-automatic-jdbc-transactions.html). When the driver is in this state, any chained stored procedures invoked directly or indirectly by the driver yield the 7112 error.

If the [Use Manual Transactions?](configure-jdbc-driver-specific-parameters.html#b1pu3m7) parameter is set to True, the driver invokes Connection.setAutoCommit(false). That is, the driver enters chained mode. This is the normal processing mode for all statements except SELECT statements and SQL embedded in a policy where the transaction type is set to manual. See [Manual vs. Automatic Transactions](manual-and-automatic-jdbc-transactions.html). When the driver is in this state, any unchained stored procedures invoked directly or indirectly by the driver yield the 7113 error.

## N.2.3 Managing Transactions in a Policy

For information on managing transactions in a policy, see [Manual vs. Automatic Transactions](manual-and-automatic-jdbc-transactions.html)

## N.2.4 Useful Links

* [Transaction modes and stored procedures](http://manuals.sybase.com/onlinebooks/group-as/asg1250e/sqlug/%40Generic__BookTextView/55096;hf=0;pt=55096#X) in the Transact-SQL User's Guide
* [Selecting the transaction mode and isolation level](http://manuals.sybase.com/onlinebooks/group-as/asg1250e/sqlug/%40Generic__BookTextView/53713;pt=53001) in the Transact-SQL User's Guide
