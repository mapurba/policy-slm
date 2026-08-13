# 12.10 Logical Operations

Because it is not generally possible to mix DML and DDL statements in a single transaction, a single event can consist of one or more transactions. You can use the jdbc:op-id and jdbc:op-type to group multiple transactions together into a single logical operation. When grouped in this way, all members of the operation are handled as a single unit with regard to status. If one member has an error, all members return the same status level. Similarly, all members share the same status type.

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <add class-name="usr" jdbc:op-id="0"
                          jdbc:op-type="password-set-operation">
        <add-attr name="fname">
            <value>John</value>
        </add-attr>
        <add-attr name="lname">
            <value>Doe</value>
        </add-attr>
        <password>Doe{$idu}</password>
    </add>
    <jdbc:statement jdbc:op-id="0">
        <jdbc:sql>CREATE USER jdoe IDENTIFIED BY {$$password}
        </jdbc:sql>
    </jdbc:statement>
</input>
```

The jdbc:op-type attribute is ignored on all elements except the first element in a logical operation.
