# B.2 Limitations

* The JDBC driver does not support the use of delimited (quoted) database identifiers (for example, “names with spaces”).
* JDBC 2 data types are not supported, with the exception of Large Object data types (LOBs) such as CLOB and BLOB.
* JDBC 3 data types are not supported.
* PostgreSQL does not support <check-object-password> events. Authentication is controlled by manually inserting entries into the pg\_hba.conf file.
