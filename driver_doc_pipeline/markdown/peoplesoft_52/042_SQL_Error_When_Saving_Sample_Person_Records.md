# 8.14 SQL Error When Saving “Sample Person” Records

Error text example:

```
SQL error.Function: SQLExec
Error Position:  0
 Return:  8601 - [Microsoft][ODBC SQL Server Driver][SQL Server]FOR
 UPDATE cannot be specified on a READ ONLY cursor.
```

The DirXML\_DERIVED.DIRXML\_DRIVER.FieldFormula PeopleCode contains an SQLExec command that performs an exclusive lock on selected rows returned from a query for the current sequential transaction number in the DIRXML\_TRANSNXT table. The command line is:

```
SQLExec("Select DIRXML_INST from DIRXML_TRANSXT Where DIRXML_DRIVER =:1
FOR UPDATE", &Driver, &InstanceID);
```

The “FOR UPDATE” locking clause is not valid for all flavors of SQL (such as SQL Server.) The clause can be safely removed to allow the PSA to function. However, if there is a possibility of simultaneous administrative access to the Transaction row creation functionality, the code should be modified by a qualified DBMS/PeopleSoft Database administrator to appropriately serialize the “Select” and “Insert or Update” of the DIRXML\_TRANSNXT table.
