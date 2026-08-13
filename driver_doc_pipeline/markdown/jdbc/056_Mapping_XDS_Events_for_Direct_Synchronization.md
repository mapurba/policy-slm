# 10.2 Mapping XDS Events for Direct Synchronization

The following table summarizes how the Subscriber channel maps XDS events to DML SQL statements for direct synchronization:

*Table 10-2* Mapping XDS Events for Direct Synchronization

| XML Event | SQL Equivalent |
| <add> | * 0 or more select statements, depending upon the matching policy. * 1 view insert statement for all single value <add-attr> element. * 0 or 1 stored procedure/function call to retrieve primary key values before or after the view insert statement. * 1 view insert statement for each multivalue <add-attr> element. |
| <modify> | * 1 view update statement for each single value <add-value> or <remove-value> element. * 1 view insert statement for each multivalue <add-value> element. * 1 view delete statement for each <remove-value> element. |
| <delete> | * 1 view delete statement. |
| <query> | * 1 view select statement. |
| <move> <rename> <modify-password> <check-object-password> | * 0 statements unless bound to embedded SQL statements. |
