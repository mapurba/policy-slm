# 12.0 Embedded SQL Statements in XDS Events

Embedded SQL allows you to embed SQL statements in XDS-formatted XML documents. You can use embedded SQL statements along with XDS events or use them alone. When embedded SQL statements are used alone, embedded SQL processing does not require that the driver know anything about tables/view in the target database. Therefore, the driver can run in schema-unaware mode. See [Synchronization Filter](configure-jdbc-driver-specific-parameters.html#b1pu3k2). When using embedded SQL alone, you must establish associations manually. The driver won’t establish them for you.

When used in conjunction with XDS events, embedded SQL can act as a virtual database trigger. In the same way that you can install database triggers on a table and cause side effects in a database when certain SQL statements are executed, embedded SQL can cause side effects in a database in response to certain XDS events.

All examples in this section reference the following indirect.usr table.

```
CREATE TABLE indirect.usr
(
    idu   INTEGER  NOT NULL,
    fname VARCHAR2(64),
    lname VARCHAR2(64),

    CONSTRAINT pk_usr_idu PRIMARY KEY(idu)
);
```

* [Common Uses of Embedded SQL](use-of-embedded-sql-for-jdbc-driver.html)
* [Embedded SQL Basics](basics-of-embedded-sql-for-jdbc-driver.html)
* [Token Substitution](token-substitution-for-jdbc-driver.html)
* [Virtual Triggers](set-virtual-triggers-for-jdbc-drivers.html)
* [Manual vs. Automatic Transactions](manual-and-automatic-jdbc-transactions.html)
* [Transaction Isolation Level](set-transaction-isolation-level-for-jdbc-driver.html)
* [Statement Type](methods-for-executing-sql-statements.html)
* [SQL Queries](how-sql-queries-work-in-jdbc-driver.html)
* [Data Definition Language (DDL) Statements](how-to-execute-ddl-statements-in-jdbc-driver.html)
* [Logical Operations](logical-operations-in-jdbc-driver.html)
* [Implementing Password Set with Embedded SQL](how-to-implement-the-set-password-with-embedded-sql.html)
* [Implementing Modify Password with Embedded SQL](how-to-implement-the-modify-password-with-embedded-sql.html)
* [Implementing Check Object Password](how-to-implement-check-object-password.html)
* [Calling Stored Procedures and Functions](how-to-call-stored-procedures-and-functions.html)
* [Best Practices](best-practices-to-use-stored-procedures-and-functions.html)
