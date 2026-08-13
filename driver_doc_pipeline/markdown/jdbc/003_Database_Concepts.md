# 1.2 Database Concepts

* [Structured Query Language](database-of-jdbc-driver-identity-manager.html#bw592r9)
* [Data Manipulation Language](database-of-jdbc-driver-identity-manager.html#af88atp)
* [Data Definition Language](database-of-jdbc-driver-identity-manager.html#af88axv)
* [View](database-of-jdbc-driver-identity-manager.html#bvle5hd)
* [Identity Columns/Sequences](database-of-jdbc-driver-identity-manager.html#aigh647)
* [Transaction](database-of-jdbc-driver-identity-manager.html#af88eo5)
* [Stored Procedures or Functions](database-of-jdbc-driver-identity-manager.html#aieg1wp)
* [Trigger](database-of-jdbc-driver-identity-manager.html#af88b0z)
* [Instead-Of-Trigger](database-of-jdbc-driver-identity-manager.html#bvleh38)

## 1.2.1 Structured Query Language

Structured Query Language (SQL) is the language used to query and manipulate data in relational databases.

## 1.2.2 Data Manipulation Language

Data Manipulation Language (DML) statements are highly standardized SQL statements that manipulate database data.

DML statements are essentially the same, regardless of the database that you use. The JDBC driver is DML-based. It maps Identity Manager events expressed as XDS XML to standardized DML statements.

The following example shows several DML statements:

```
SELECT * FROM usr;
INSERT INTO usr(lname) VALUES('Doe');
UPDATE usr SET fname = 'John' WHERE idu = 1;
```

## 1.2.3 Data Definition Language

Data Definition Language (DDL) statements manipulate database objects such as tables, indexes, and user accounts.

DDL statements are proprietary and differ substantially between databases. Even though the JDBC driver is DML-based, you can embed DDL statements in XDS events. For additional information, refer to [Section 12.0, Embedded SQL Statements in XDS Events](embed-sql-statements-in-xds-events-for-jdbc-driver.html),

The following examples show several DDL statements:

```
CREATE TABLE usr
(
    idu   INTEGER,
    fname VARCHAR2(64),
    lname VARCHAR2(64)
);

CREATE USER idm IDENTIFIED BY novell;
```

*NOTE:*Examples used throughout this guide are for the Oracle database.

## 1.2.4 View

A view is a logical table.

When queried by using a SELECT statement, the view is created by executing the SQL query supplied when the view was defined. Views are a useful abstraction mechanism for representing multiple tables of arbitrary structure as a single table or logical database class.

```
CREATE VIEW view_usr
(
    pk_idu,
    fname,
    lname
)
AS
SELECT idu, fname, lname from usr;
```

## 1.2.5 Identity Columns/Sequences

Identity columns and sequences are used to generate unique primary key values. Identity Manager can associate with these values, among other things.

An identity column is a self-incrementing column used to uniquely identify a row in a table. Identity column values are automatically filled in when a row is inserted into a table.

A sequence object is a counter that can be used to uniquely identify a row in a table. Unlike an identity column, a sequence object is not bound to a single table. However, if it is used by a single table, a sequence object can be used to achieve an equivalent result.

The following is an example of a sequence object:

```
CREATE SEQUENCE seq_idu
    START WITH 1
    INCREMENT BY 1
    NOMINVALUE
    NOMAXVALUE
    ORDER;
```

## 1.2.6 Transaction

A transaction is an atomic database operation that consists of one or more statements.

When a transaction is complete, all statements in the transaction are committed. When a transaction is interrupted or one of the statements in the transaction has an error, the transaction is said to roll back. When a transaction is rolled back, the database is left in the same state it was before the transaction began.

Transactions are either manual (user-defined) or automatic. Manual transactions can consist of one or more statements and must be explicitly committed. Automatic transactions consist of a single statement and are implicitly committed after each statement is executed.

* [Manual (User-Defined) Transactions](database-of-jdbc-driver-identity-manager.html#bgyky4i)
* [Automatic Transactions](database-of-jdbc-driver-identity-manager.html#bgykyar)

### Manual (User-Defined) Transactions

Manual transactions usually contain more than one statement. DDL statements typically cannot be grouped with DML statements in a manual transaction.

The following example illustrates a manual transaction:

```
SET AUTOCOMMIT OFF
INSERT INTO usr(lname) VALUES('Doe');
UPDATE usr SET fname = 'John' WHERE idu = 1;
COMMIT; -- explicit commit
```

### Automatic Transactions

Automatic transactions consist of only one statement. They are often referred to as auto-committed statements because changes are implicitly committed after each statement. An auto-committed statement is autonomous of any other statement.

The following example illustrates an automatic transaction:

```
SET AUTOCOMMIT ON
INSERT INTO emp(lname) VALUES('Doe');
-- implicit commit
```

## 1.2.7 Stored Procedures or Functions

A stored procedure or function is programmatic logic stored in a database. Stored procedures or functions can be invoked from almost any context.

The Subscriber channel can use stored procedures or functions to retrieve primary key values from rows inserted into tables, to create associations. Stored procedures or functions can also be invoked from within embedded SQL statements or triggers.

The distinction between stored procedures and functions varies by database. Typically, both can return output, but they differ in how they do it. Stored procedures usually return values through parameters. Functions usually return values through a scalar return value or result set.

The following example illustrates a stored procedure definition that returns the next value of a sequence object:

```
CREATE SEQUENCE seq_idu
    START WITH 1
    INCREMENT BY 1
    NOMINVALUE
    NOMAXVALUE
    ORDER;
```

```
CREATE
PROCEDURE sp_idu(    io_idu IN OUT INTEGER)
IS
BEGIN
    IF (io_idu IS NULL) THEN
      SELECT seq_idu.nextval INTO io_idu FROM DUAL;
END IF;
END sp_idu;
```

## 1.2.8 Trigger

A database trigger is programmatic logic associated with a table, which executes under certain conditions. A trigger is said to fire when its execution criteria are met.

Triggers are often useful for creating side effects in a database. In the context of the JDBC driver, triggers are useful to capture event publications. The following is an example of a database trigger on the usr table.

```
CREATE TABLE usr
(
    idu   INTEGER,
    fname VARCHAR2(64),
    lname VARCHAR2(64)
);
```

```
-- t = trigger; i = insert
CREATE TRIGGER t_usr_i
    AFTER INSERT ON usr
    FOR EACH ROW

BEGIN
    UPDATE usr SET fname = 'John';
END;
```

When a statement is executed against a table with triggers, a trigger fires if the statement satisfies the conditions specified in the trigger. For example, using the above table, suppose the following insert statement is executed:

```
INSERT INTO usr(lname) VALUES('Doe')
```

Trigger t\_emp\_i fires after the insert statement is executed, and the following update statement is also executed:

```
UPDATE usr SET fname = 'John'
```

A trigger can typically be fired before or after the statement that triggered it. Statements that are executed as part of a database trigger are typically included in the same transaction as the triggering statement. In the above example, both the INSERT and UPDATE statements are committed or rolled back together.

## 1.2.9 Instead-Of-Trigger

An instead-of-trigger is programmatic logic associated with a view, which executes under certain conditions.

Instead-of-triggers are useful for making views writable or subscribeable. They are often used to define what it means to INSERT, UPDATE, and DELETE from a view. The following is an example of an instead-of-trigger on the usr table.

```
CREATE TABLE usr
(
    idu   INTEGER,
    fname VARCHAR2(64),
    lname VARCHAR2(64)
);
```

```
CREATE VIEW view_usr
(
    pk_idu,
    fname,
    lname
)
AS
SELECT idu, fname, lname from usr;
-- t = trigger; i = insert
CREATE TRIGGER t_view_usr_i
    INSTEAD OF INSERT ON usr
BEGIN
    INSERT INTO usr(idu, fname, lname)
      VALUES(:NEW.pk_idu, :NEW.fname, :NEW.lname);
END;
```

When a statement is executed against a view with instead-of-triggers, an instead-of-trigger executes if the statement satisfies the conditions specified in the trigger. Unlike triggers, instead-of-triggers always execute before the triggering statement. Also, unlike regular triggers, instead-of-triggers are executed instead of, not in addition to, the triggering statement.

For example, using the above view, suppose the following insert statement is executed instead of the original insert statement:

```
INSERT INTO view_usr(pk_idu, fname, lname)
    VALUES(1, ‘John', ‘Doe')
```

Rather than executing the original statement, instead-of-trigger t\_view\_usr\_i fires and executes the following statement:

```
INSERT INTO usr(idu, fname, lname)
    VALUES(:NEW.pk_idu, :NEW.fname, :NEW.lname);
```

In this example, the statements happen to be equivalent.
