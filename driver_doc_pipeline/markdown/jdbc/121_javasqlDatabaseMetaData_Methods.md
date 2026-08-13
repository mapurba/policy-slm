# F.0 java.sql.DatabaseMetaData Methods

This section lists the required and optional [java.sql.DatabaseMetaData](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/DatabaseMetaData.html) methods.

The following JDBC 1 methods are required only if the [Synchronization Filter](configure-jdbc-driver-specific-parameters.html#b1pu3k2) parameter is set to something other than Exclude all tables/views:

* getColumns(java.lang.String catalog, java.lang.String schemaPattern, java.lang.String tableNamePattern, java.lang.String columnNamePattern):java.sql.ResultSet
* getPrimaryKeys(java.lang.String catalog, java.lang.String schema, java.lang.String table):java.sql.ResultSet
* getTables(java.lang.String catalog, java.lang.String schemaPattern, java.lang.String tableNamePattern, java.lang.String[] types):java.sql.ResultSet
* storesLowerCaseIdentifiers():boolean
* storesMixedCaseIdentifiers():boolean
* storesUpperCaseIdentifiers():boolean

Optional JDBC 1 methods:

* dataDefinitionCausesTransactionCommit():boolean
* dataDefinitionIgnoredInTransactions():boolean
* getColumnPrivileges(String catalog, String schema, String table, String columnNamePattern):java.sql.ResultSet
* getDatabaseProductName():java.lang.String
* getDatabaseProductVersion():java.lang.String
* getDriverMajorVersion():int
* getDriverMinorVersion():int
* getDriverName():java.lang.String
* getDriverVersion():java.lang.String
* getExportedKeys(java.lang.String catalog, java.lang.String schema, java.lang.String table):java.sql.ResultSet
* getMaxStatements():int
* getMaxConnections():int
* getMaxColumnsInSelect():int
* getProcedureColumns(String catalog, String schemaPattern, String procedureNamePattern, String columnNamePattern):java.sql.ResultSet
* getSchemas():java.sql.ResultSet
* getTableTypes():java.sql.ResultSet
* getUserName():java.lang.String
* supportsColumnAliasing():bolean
* supportsDataDefinitionAndDataManiuplationTransactions():boolean
* supportsDataManipulationTransactionsOnly():boolean
* supportsLimitedOuterJoins():boolean
* supportsMultipleTransactions():boolean
* supportsSchemasInDataManipulation():boolean
* supportsSchemasInProcedureCalls():boolean
* supportsTransactionIsolationLevel(int level):boolean
* supportsTransactions():boolean

Optional JDBC 2 methods:

* supportsBatchUpdates():boolean

Optional JDBC 3 methods:

* supportsGetGeneratedKeys():boolean
