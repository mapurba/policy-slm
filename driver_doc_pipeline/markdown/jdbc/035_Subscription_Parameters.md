# 6.4 Subscription Parameters

The following table summarizes Subscriber-level parameters and their properties:

*Table 6-37* Subscriber-Level Parameters and Properties

| Display Name | Tag Name | Sample Value | Default Value | Required |
| [Disable Subscriber?](how-to-set-subscription-parameters.html#bvujptg) | disable | 1 (yes) | 0 (no) | no |
| [Generation/Retrieval Method (Table-Global)](how-to-set-subscription-parameters.html#bvul6hv) | key-gen-method | auto | none (subscription event) |  |
| [Retrieval Timing (Table-Global)](how-to-set-subscription-parameters.html#bvul74p) | key-gen-timing | after (after row insertion) | before (before row insertion) | no |
| [Method and Timing (Table-Local)](how-to-set-subscription-parameters.html#bvul7v5) | key-gen | usr("?=indirect.proc\_idu()", before) | (none) | no |
| [Disable Statement-Level Locking?](how-to-set-publication-parameters.html#bvwo5gx) | disable-locking | 1 (yes) | 0 (no) | no |
| [Check Update Counts?](how-to-set-subscription-parameters.html#bvujr8a) | check-update-count | 0 (no) | 1 (yes) | no |
| [Add Default Values on Insert?](how-to-set-subscription-parameters.html#bvujrwk) | add-default-values-on-view-insert | 0 (no) | (dynamic) | no |

This default for the Add Default Values on Insert property is derived dynamically from descriptor files at runtime.

Subscription parameters are in two subcategories:

* [Uncategorized Parameters](how-to-set-subscription-parameters.html#aaxzkgi)
* [Primary Key Parameters](how-to-set-subscription-parameters.html#bvujuhx)

## 6.4.1 Uncategorized Parameters

* [Disable Subscriber?](how-to-set-subscription-parameters.html#bvujptg)
* [Disable Statement-Level Locking?](how-to-set-subscription-parameters.html#bvujr3w)
* [Check Update Counts?](how-to-set-subscription-parameters.html#bvujr8a)
* [Add Default Values on Insert?](how-to-set-subscription-parameters.html#bvujrwk)

### Disable Subscriber?

The Disable Subscriber? parameter specifies whether the Subscriber channel is disabled.

When this parameter is set to Boolean True, the Subscriber channel is disabled. When the parameter is set to Boolean False, the Subscriber channel is active.

*Table 6-38* Disable Subscriber?: Properties

| Property | Value |
| Tag Name | disable |
| Required? | no |
| Default Value | 0 (no) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | False |

### Disable Statement-Level Locking?

The Disable Statement-Level Locking? parameter specifies whether database resources are explicitly locked on this channel before each SQL statement is executed. This parameter is active only if [Enable Statement-Level Locking?](configure-jdbc-driver-specific-parameters.html#b1pu3mz) is set to Boolean True.

When this parameter is set to Boolean True, database resources are explicitly locked. When this parameter is set to Boolean False, database resources are not explicitly locked.

*Table 6-39* Disable Statement-Level Locking?: Properties

| Property | Value |
| Tag Name | disable-locking |
| Required? | no |
| Default Value | 0 (no) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

### Check Update Counts?

The Check Update Counts? parameter specifies whether the Subscriber channel checks to see if a table was actually updated when INSERT, UPDATE, and DELETE statements executed against a table.

When set to Boolean True, update counts are checked. If nothing is updated, an exception is thrown. When set to Boolean False, update counts are ignored.

When statements are redefined in before-trigger logic, set his parameter to Boolean False

When using Microsoft SQL Server, use the default value, because errors in trigger logic (that might roll back a transaction) are not propagated back to the Subscriber channel.

*Table 6-40* Check Update Counts?: Properties

| Property | Value |
| Tag Name | check-update-count |
| Required? | no |
| Default Value | 1 (yes) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

### Add Default Values on Insert?

The Add Default Values on Insert? parameter specifies whether the Subscriber channel provides default values when executing an INSERT statement against a view.

The primary purpose of this parameter is to enable interoperability with Microsoft SQL Server 2000. This database requires that view columns constrained NOT NULL have a non-NULL value in an INSERT statement.

When this parameter is set to Boolean True, default values are provided for INSERT statements executed against views, and explicit values are not already available. When this parameter is set to Boolean False, default values are not provided.

*Table 6-41* Add Default Values on Insert?: Properties

| Property | Value |
| Tag Name | add-default-values-on-view-insert |
| Required? | no |
| Default Value | (dynamic) |
| Legal Values | 1, yes, true (yes) 0, no, false (no) |
| Schema-Dependent | True |

The Default Value property is derived dynamically from descriptor files at runtime.

## 6.4.2 Primary Key Parameters

* [Generation/Retrieval Method (Table-Global)](how-to-set-subscription-parameters.html#bvul6hv)
* [Retrieval Timing (Table-Global)](how-to-set-subscription-parameters.html#bvul74p)
* [Method and Timing (Table-Local)](how-to-set-subscription-parameters.html#bvul7v5)

When processing <add> events, which map to INSERT statements, the Subscriber channel uses primary key values to create Identity Manager associations. These parameters specify how and when the Subscriber channel obtains the primary key values necessary to construct association values. How primary key values are obtained is the primary key generation/retrieval method. The retrieval timing indicates when primary key values are retrieved.

The following table identifies the supported methods and timings:

*Table 6-42* Supported Methods and Timings

| Method | Timing: before (row insertion) | Timing: after (row insertion) |
| None (subscription event) | Y | N1 |
| Driver (Subscriber-generated) | Y | Y |
| Auto (auto-generated/identity column) | N2 | Y |
| (stored procedure/function) | Y | Y |

1 The Subscriber channel automatically overrides this timing and changes it to before.

2 The Subscriber channel automatically overrides this timing and changes it to after.

### Generation/Retrieval Method (Table-Global)

The Generation/Retrieval Method (Table-Global) parameter specifies how primary key values are generated or retrieved for all parent tables and views. The Method and Timing parameter overrides this parameter on a per-table/view basis. See [Method and Timing (Table-Local)](how-to-set-subscription-parameters.html#bvul7v5).

When this parameter is set to none, primary key values are assumed to already exist in the subscription event. When this parameter is set to driver, primary key values are generated by one of the following:

* Using a SELECT (MAX(pk\_columname)+1) statement if retrieval timing is set to before
* Using a SELECT MAX(pk\_columname) statement if retrieval timing is set to after

For string column types, the Subscriber channel generates a value by using the return value of System.CurrentTimeMillis(). Other data types are not supported.

When this parameter is set to auto, primary key values are retrieved via the java.sql.Statement.getGeneratedKeys():java.sql.ResultSet method. The MySQL Connector/J JDBC driver is the only supported third-party JDBC driver that currently implements this method. See [MySQL Connector/J JDBC Driver](supported-third-party-jdbc-drivers.html#bvmdmw4).

*Table 6-43* Generation/Retrieval Method (Table-Global): Properties

| Property | Value |
| Tag Name | key-gen-method |
| Required? | no |
| Default Value | none (subscription event) |
| Legal Values | none (subscription event), driver (Subscriber-generated), auto (auto-generated/identity column) |
| Schema-Dependent | True |

### Retrieval Timing (Table-Global)

The Retrieval Timing (Table-Global) parameter specifies when the Subscriber channel retrieves primary key values for all parent tables and views. The Method and Timing (Table-Local) parameter overrides this parameter. See [Method and Timing (Table-Local)](how-to-set-subscription-parameters.html#bvul7v5).

When this parameter is set to before, primary key values are retrieved before insertion. When this parameter is set to after, primary key values are retrieved after insertion.

*Table 6-44* Retrieval Timing (Table-Global): Properties

| Property | Value |
| Tag Name | key-gen-timing |
| Required? | no |
| Default Value | before (before row insertion) |
| Legal Values | before (before row insertion), after (after row insertion) |
| Schema-Dependent | True |

### Method and Timing (Table-Local)

The Method and Timing (Table-Local) parameter specifies the primary key generation/retrieval method and retrieval timing on a per parent table/view basis. It essentially maps a generation/retrieval method and retrieval timing to a table or view name. The syntax for this parameter mirrors a procedural programming language method call with multiple arguments (such as method-name(argument1, argument2)).

When using the [Table/View Names](configure-jdbc-driver-specific-parameters.html#b1pu3kx) parameter, you probably need to explicitly schema-qualify any tables, views, stored procedures or functions referenced in this parameter’s value. When you use the [Schema Name](configure-jdbc-driver-specific-parameters.html#b1pu3ka) parameter, then tables, views, stored procedures, or functions referenced in this parameter’s value are implicitly schema-qualified with that schema name. If tables, views, stored procedures, or functions referenced in this parameter’s value are located in a different schema than the implicit schema, they must be schema-qualified.

* [BNF](how-to-set-subscription-parameters.html#b1pssae)
* [Generation or Retrieval Method](how-to-set-subscription-parameters.html#b1pssud)
* [Retrieval Timing](how-to-set-subscription-parameters.html#b1psthm)

#### BNF

The BNF (Backus Naur Form) notation for this parameter’s value is the following:

```
<key-gen> ::= <table-or-view-name> "(" <generation-retrieval-method>,
                          <retrieval-timing> ")" {[<delimiter>] <key-gen>}

<generation-retrieval-method> ::= none | driver | auto |
                                  """ <procedure-signature> """ |
                                  """ <function-signature>  """

<table-or-view-name> ::= <legal-undelimited-database-table-or-view-
                         identifier>

<delimiter> ::= ";" | "," | <white-space>

<procedure-signature> ::= <schema-qualifier> "." <stored-routine-
                          name>"("<argument-list>")"

<function-signature> ::= "?=" <procedure-signature>

<schema-qualifier> ::= <legal-undelimited-database-username-identifier>

<stored-routine-name> ::= <legal-undelimited-database-stored-routine
                          -identifier>

<argument-list> ::= <column-name>{"," <column-name>}

<column-name> ::= <column-from-table-or-view-name-previously-specified>
```

#### Generation or Retrieval Method

The generation or retrieval method specifies how primary key values are to be generated, if necessary, and retrieved. The possible methods are None, Driver, Auto, and Stored Procedure/Function:

*None:*
By default, the Subscriber channel assumes that the Identity Vault is the authoritative source of primary key values and that the requisite values are already present in a given <add> event. If this is the case, no primary values need to be generated because they already exist. They only need to be retrieved from the current <add> event. This method is desirable when an eDirectory attribute, such as GUID, is explicitly schema-mapped to a parent table or view’s primary key column.

Assuming the existence of a table named usr and a view named view\_usr where the Identity Vault is the authoritative source of primary key values, this parameter’s value would be similar to the following:

usr(none); view\_usr(none)

When you use this method, we recommend mapping GUID rather than CN to a parent table or view’s primary key column.

*Driver:*
This method assumes that the driver is the authoritative source of primary key values for the specified parent table or view.

When prototyping or in the initial stages of deployment, it is often desirable to have the Subscriber channel generate primary key values before a stored procedure or function is written. You can also use this method against databases that do not support stored procedures or functions. When you use this method in a production environment, however, all SQL statements generated by an <add> event should be contained in a serializable transaction. For additional information, refer to [Transaction Isolation Level](configure-jdbc-driver-specific-parameters.html#b1pu3me).

Instead of making all transactions serializable, you can also set individual transaction isolation levels by using embedded SQL attributes. For additional information, refer to [Transaction Isolation Level](set-transaction-isolation-level-for-jdbc-driver.html).

For any numeric column types, the Subscriber channel uses the following to generate primary key values:

* A simple SELECT(MAX+1)statement for before timing
* A SELECT MAX()statement for after timing

For string column types, the Subscriber channel generates a value by using the return value of System.CurrentTimeMillis(). Other data types are not supported.

Assuming the existence of a table named usr and a view named view\_usr, where the database is the authoritative source of primary key values, this parameter’s value would be similar to the following:

usr(driver); view\_usr(driver)

When you use this method, we recommend that you omit primary key columns from Schema Mapping policies and channel filters.

*Auto:*
This method assumes that the database is the authoritative source of primary key values for the specified parent table or view.

Some databases support identity columns that automatically generate primary key values for inserted rows. This method retrieves auto-generated primary key values through the JDBC 3 interface method java.sql.Statement.getGeneratedKeys():java.sql.ResultSet. The MySQL Connector/J JDBC driver is the only supported third-party JDBC driver that currently implements this method. See [MySQL Connector/J JDBC Driver](supported-third-party-jdbc-drivers.html#bvmdmw4).

Assuming the existence of a table named usr and a view named view\_usr, where the database is the authoritative source of primary key values, this parameter’s value would be similar to the following:

usr(auto); view\_usr(auto)

When you use this method, we recommend that you omit primary key columns from Schema Mapping policies and channel filters.

*Stored-Procedure/Function:*
This method assumes that the stored-procedure / function is the authoritative source of primary key values for the specified parent table or view.

Assuming

* The existence of a table named usr with a primary key column named idu
* A view named view\_usr with a primary key values named pk\_idu
* The existence of a database function func\_last\_usr\_idu and stored procedure sp\_last\_view\_usr\_pk\_idu that both return the last generated primary key value for their respective table/view

This parameter’s value would be similar to the following:

usr("?=func\_last\_usr\_idu()"); view\_usr("sp\_last\_view\_usr\_pk\_idu(pk\_idu)")

In the previous examples, a parameter is passed to the stored procedure. Parameters can also be passed to functions, but this is not usually necessary. Unlike functions, stored procedures usually return values through parameters. For stored procedures, primary key columns must be passed as IN OUT parameters. Non-key columns must be passed as IN parameters.

For both stored procedures and functions, parameter order, number and data type must correspond to the order, number and data type of the parameters expected by the procedure or function.

When you use this method, we recommend that you omit primary key columns from Schema Mapping policies and channel filters.

#### Retrieval Timing

The Retrieval Timing parameter specifies when primary key values are retrieved.

An <add> event always results in at least one INSERT statement against a parent table or view. This portion of this parameter specifies when primary key values are to be retrieved relative to the initial INSERT statement.

*Before:*
This is the default setting. When this setting is specified, primary key values are retrieved before the initial INSERT statement.

This retrieval timing is supported for all generation/retrieval methods except auto. Retrieval timing is required for the none method.

*After:*
When this setting is specified, primary key values are retrieved after the initial INSERT statement.

This retrieval timing is supported for all generation/retrieval methods except none. Retrieval timing is required for the auto method.

The following examples augment the previous ones by adding retrieval timing information:

usr(none, before); view\_usr(none, before)

usr(driver, before); view\_usr(driver, after)

usr(auto, after); view\_usr(auto, after)

usr("?=func\_last\_usr\_idu()", before); view\_usr("sp\_last\_view\_usr\_pk\_idu(pk\_idu)", after)

The following table lists the properties of this parameter:

*Table 6-45* Retrieval Timing: Properties

| Property | Value |
| Tag Name | key-gen |
| Required? | no |
| Case-Sensitive? | See [Undelimited Identifier Case Sensitivity](characteristics-of-databases.html#bvqzikw). |
| Sample Value | usr("?=proc\_idu()", before) |
| Default Value | (none) |
| Legal Values | (any string adhering to the BNF) |
| Schema-Dependent | True |
