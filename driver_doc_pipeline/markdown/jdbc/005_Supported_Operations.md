# 1.4 Supported Operations

* [Supported Databases](supported-operations-on-jdbc-driver.html#b94bcef)
* [Supported Third Party JDBC Drivers](supported-operations-on-jdbc-driver.html#b1iivfrh)
* [Support for Password Synchronization](supported-operations-on-jdbc-driver.html#b94bceh)
* [Supported Data Synchronization Models](supported-operations-on-jdbc-driver.html#afexaon)
* [Triggerless vs. Triggered Publication](supported-operations-on-jdbc-driver.html#bvldqov)

## 1.4.1 Supported Databases

For information on supported databases, see[Supported Databases](supported-databases-for-jdbc-driver.html).

## 1.4.2 Supported Third Party JDBC Drivers

For information on supported third-party JDBC drivers, see [Third-Party JDBC Driver Interoperability](third-party-jdbc-driver-interoperability.html).

## 1.4.3 Support for Password Synchronization

The JDBC driver supports password set and check on the Subscriber channel. The driver does not support bidirectional password synchronization.

## 1.4.4 Supported Data Synchronization Models

The JDBC driver supports two data synchronization models: direct and indirect. Both terms are best understood with respect to the final destination of the data being synchronized.

| Model | Association | Description |
| Indirect | Usually associated with tables | Target database tables probably don’t match the structure required by the driver. Therefore, it’s usually necessary to create intermediate staging tables that do match the structure that the driver requires. |
| Direct | Usually associated with views | Views provide the abstraction mechanism that best facilitates integration with the target database tables. |

The following sections describe how direct and indirect synchronization work on both the Subscriber and Publisher channels.

* [Indirect Synchronization](supported-operations-on-jdbc-driver.html#aescgok)
* [Direct Synchronization](supported-operations-on-jdbc-driver.html#aesce87)

### Indirect Synchronization

Indirect synchronization uses intermediate staging tables to synchronize data between the Identity Vault and a database. You can have one or more customer tables and intermediate staging tables.

Subscriber Channel
:   The Subscriber channel updates the intermediate staging tables in the synchronization schema. This action triggers an update to customer tables elsewhere in the database.

    ![](../graphics/jdbc_indirsyncsub_a.png)

Publisher Channel
:   Synchronization triggers update the intermediate staging tables when target database tables are updated. Publication triggers then insert one or more rows into the event log table. The Publisher channel then reads the inserted rows and updates the Identity Vault.

    Depending on the contents of the rows read from the event log table, the Publisher channel might need to retrieve additional information from the intermediate tables before updating the Identity Vault. After updating the Identity Vault, the Publisher channel then deletes or marks the rows as processed.

    ![](../graphics/jdbc_indirsyncpub_a.png)

### Direct Synchronization

Direct synchronization typically uses views to synchronize data between Identity Manager and a database. You can use tables if they conform to the structure that the JDBC driver requires. You can have one or more customer views or tables.

Subscriber Channel
:   Updates existing customer tables through a view in the synchronization schema.

    Direct synchronization without a view is possible only if the target database tables match the structure that the JDBC driver requires. For additional information, see [Indirect Synchronization](indirect-synchronization.html).

    ![](../graphics/jdbc_dirsyncsub_a.png)

Publisher Channel
:   When a target database table is updated, publication triggers insert rows into the event log table. The Publisher channel then reads the inserted rows and updates the Identity Vault.

    ![](../graphics/jdbc_dirsyncpub_a.png)

    Depending on the contents of the rows read from the event log table, the Publisher channel might need to retrieve additional information from the view before updating the Identity Vault. After updating the Identity Vault, the Publisher channel then deletes or marks the rows as processed.

## 1.4.5 Triggerless vs. Triggered Publication

Triggers are not required to log events for the Publisher channel. In situations where triggers cannot be used to capture granular events, the Publisher channel can derive database changes by inspecting database data.

Triggerless publication is particularly useful when support contracts forbid the use of triggers on database application tables or for rapid prototyping.

However, triggerless publication is less efficient than triggered publication. With triggered publication, what changed is already known. With triggerless publication, change calculation must occur before events can be processed.

Triggerless publication, unlike triggered publication, does not preserve event order. It only guarantees that, by the end of a polling cycle, objects in the database and the Identity Vault are in sync.

Triggerless publication, unlike triggered publication, does not provide historical data such as old values. It provides information on the current state of an object, not the previous state.

Triggerless publication does have the advantage of being much simpler because it reduces database-side dependencies. Writing database triggers can be complicated and requires extensive knowledge of database-specific SQL syntaxes.

The following figure illustrates direct triggerless publication:

*Figure 1-2* Direct Triggerless Publication

![](../graphics/jdbc_dirsyncpub_notrigg_a.png)

The following figure illustrates indirect triggerless publication:

*Figure 1-3* Indirect Triggerless Publication

![](../graphics/jdbc_indirsyncpub_notrigg_a.png)

If you move the driver without moving the state files, the driver must build up new state files by resynchronizing. For information on this situation, see [State Directory](configure-jdbc-driver-specific-parameters.html#b1pu3ju).
