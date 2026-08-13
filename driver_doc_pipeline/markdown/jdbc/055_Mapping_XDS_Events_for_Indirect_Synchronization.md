# 10.1 Mapping XDS Events for Indirect Synchronization

The following table summarizes how the Subscriber channel maps XDS events to DML SQL statements for indirect synchronization:

*Table 10-1* Mapping XDS Events for Indirect Synchronization

| XML Event | SQL Equivalent |
| <add> | * 0 or more select statements, depending upon the matching policy. * 1 parent table insert statement for all single value <add-attr> elements. * 0 or 1 stored procedure/function calls to retrieve primary key values before or after the parent table insert statement. * 1 child table insert statement for each multivalue <add-attr> element.Â |
| <modify> | * 1 parent table update statement for each single value <add-value> or <remove-value> element. * 1 child table insert statement for each multivalue <add-value> element. * 1 child table delete statement for each <remove-value> element. |
| <delete> | * 1 parent table delete statement. * 1 delete statement for each child table. |
| <query> | * 1 parent table select statement. * 1 select statement for each childtable. |
| <move> <rename> <modify-password> <check-object-password> | * 0 statements unless bound to embedded SQL statements. |
