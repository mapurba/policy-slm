# 12.5 Manual vs. Automatic Transactions

You can manually group embedded SQL and XDS events by using two custom attributes:

* jdbc:transaction-type
* jdbc:transaction-id

#### jdbc:transaction-type

This attribute has two values: manual and auto. By default, most XDS events of interest (<add>, <modify>, and <delete>) are implicitly set to the manual transaction type. The manual setting enables XDS events to resolve to a transaction consisting of one or more SQL statement.

By default, embedded SQL events are set to auto transaction type because some SQL statements, such as DDL statements, cannot usually be included in a manual transaction. In the following example, the attribute is in bold text.

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <add class-name="usr" jdbc:transaction-type="auto">
        <add-attr name="lname">
            <value>Doe</value>
        </add-attr>
    </add>
    <jdbc:statement>
        <jdbc:sql>UPDATE indirect.usr SET fname = 'John' WHERE
                  idu = {$idu}</jdbc:sql>
    </jdbc:statement>
</input>
```

This XML resolves to:

```
SET AUTOCOMMIT ON
INSERT INTO indirect.usr(lname) VALUES('Doe');
-- implicit commit
UPDATE indirect.usr SET fname = 'John' WHERE idu = 1;
-- implicit commit
```

#### jdbc:transaction-id

The Subscriber channel ignores this attribute unless the element’s jdbc:transaction-type attribute value defaults to or is explicitly set to manual. The following XML shows an example of a manual transaction. The attribute is in bold text.

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <add class-name="usr" jdbc:transaction-id="0">
        <add-attr name="lname">
            <value>Doe</value>
        </add-attr>
    </add>
     <jdbc:statement jdbc:transaction-type="manual"                      jdbc:transaction-id="0">
           <jdbc:sql>UPDATE indirect.usr SET fname = 'John' WHERE
                     idu = {$idu}</jdbc:sql>
     </jdbc:statement>
</input>
```

This XML resolves to:

```
SET AUTOCOMMIT OFF
INSERT INTO indirect.usr(lname) VALUES('Doe');
UPDATE indirect.usr SET fname = 'John' WHERE idu = 1;
COMMIT; -- explicit commit
```
