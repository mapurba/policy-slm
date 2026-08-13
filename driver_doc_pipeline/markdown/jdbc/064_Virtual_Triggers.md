# 12.4 Virtual Triggers

In the same way that database triggers can fire before or after a triggering statement, embedded SQL can be positioned before or after the triggering XDS event. The following examples show how you can embed SQL before or after an XDS event.

#### Virtual Before Trigger

```
<input xmlns:jdbc"urn:dirxml:jdbc">
     <jdbc:statement>
          <association>idu=1,table=usr,schema=indirect</association>
          <jdbc:sql>UPDATE indirect.usr SET fname = 'John' WHERE                     idu = {$idu}</jdbc:SQL>
횂혻횂혻횂혻횂혻</jdbc:statement>
횂혻횂혻횂혻횂혻<modify class-name="usr">
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<association>idu=1,table=usr,schema=indirect</association>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<modify-attr name="lname">
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<remove-all-values/>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<add-value>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<value>Doe</value>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻</add-value>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻</modify-attr>
횂혻횂혻횂혻횂혻</modify>
</input>
```

This XML resolves to:

```
SET AUTOCOMMIT OFF
UPDATE indirect.usr SET fname = 'John' WHERE idu = 1;
COMMIT; --explicit commit
UPDATE indirect.usr SET lname = 'Doe'  WHERE idu = 1;
COMMIT; --explicit commit
```

#### Virtual After Trigger

```
<input xmlns:jdbc"urn:dirxml:jdbc">
횂혻횂혻횂혻횂혻<modify class-name="usr">
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<association>idu=1,table=usr,schema=indirect</association>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<modify-attr name="lname">
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<remove-all-values/>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<add-value>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<value>Doe</value>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻</add-value>
    횂혻횂혻횂혻횂혻</modify-attr>
횂혻횂혻횂혻횂혻</modify>
횂혻횂혻횂혻횂혻<jdbc:statement>
횂혻횂혻횂혻횂혻횂혻횂혻횂혻횂혻<jdbc:sql>UPDATE indirect.usr SET fname = 'John' WHERE          idu = {$idu}</jdbc:sql>
횂혻횂혻횂혻횂혻</jdbc:statement>
</input>
```

This XML resolves to:

```
SET AUTOCOMMIT OFF
UPDATE indirect.usr SET lname = 'Doe' WHERE idu = 1;
COMMIT; --explicit commit
UPDATE indirect.usr SET fname = 'John' WHERE idu = 1;
COMMIT; --explicit commit
```
