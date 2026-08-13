# 12.6 Transaction Isolation Level

In addition to grouping statements, you can use transactions to preserve the integrity of data in a database. Transactions can lock data to prevent concurrent access or modification. The isolation level of a transaction determines how locks are set. Usually, the default isolation level that the driver uses is sufficient and should not be altered.

The custom attribute jdbc:isolation-level allows you to adjust the isolation transaction level if necessary. The java.sql.Connection parameter defines five possible values in the interface. See [java.sql.Connection](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Connection.html).

* none
* read uncommitted
* read committed
* repeatable read
* serializable

The driver’s default transaction isolation level is read committed unless overridden by a descriptor file. In manual transactions, place the jdbc:isolation-level attribute on the first element in the transaction. This attribute is ignored on subsequent elements. In the following example. the attribute is in bold text.

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <add class-name="usr" jdbc:transaction-id="0"
                          jdbc:isolation-level="serializable">
        <add-attr name="lname">
            <value>Doe</value>
        </add-attr>
    </add>
    <jdbc:statement jdbc:transaction-type="manual"
                    jdbc:transaction-id="0">
        <jdbc:sql>UPDATE indirect.usr SET fname = 'John'
                  WHERE idu = {$idu}</jdbc:sql>
    </jdbc:statement>
</input>
```

This XML resolves to:

```
SET AUTOCOMMIT OFF
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
INSERT INTO indirect.usr(lname) VALUES('Doe');
UPDATE indirect.usr SET fname = 'John' WHERE idu = 1;
COMMIT; -- explicit commit
```
