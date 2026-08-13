# 12.15 Best Practices

For performance reasons, it is better to call a single stored procedure/function that contains multiple SQL statements than to embed multiple statements in an XDS document.

In the following examples, the single stored procedure or function is preferred.

#### Single Stored Procedure

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <add class-name="usr">
        <add-attr name="fname">
            <value>John</value>
        </add-attr>
        <add-attr name="lname">
            <value>Doe</value>
        </add-attr>
    </add>
    <jdbc:statement>
        <jdbc:sql>CALL PROCEDURE set_name('John', 'Doe')</jdbc:sql>
    </jdbc:statement>
</input>
```

#### Multiple Embedded Statements

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <add class-name="usr">
        <add-attr name="lname">
            <value>Doe</value>
        </add-attr>
    </add>
    <jdbc:statement>
        <jdbc:sql>UPDATE indirect.usr SET fname = 'John'                   WHERE idu = {$idu}</jdbc:sql>
    </jdbc:statement>
    <jdbc:statement>
        <jdbc:sql>UPDATE indirect.usr SET lname = 'Doe'                   WHERE idu = {$idu}</jdbc:sql>
    </jdbc:statement>
</input>
```

The syntax used to call stored procedures or functions varies by database. For additional information, see [Syntaxes for Calling Stored Procedures and Functions](characteristics-of-databases.html#bvowm5a).
