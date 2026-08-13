# 1.3 Supported Operations

The Fanout driver supports the following operations on the Subscriber channel:

* [Password Synchronization](supported-jdbc-fan-out-operations.html#b1ijocrw)
* [Data Synchronization](supported-jdbc-fan-out-operations.html#b1ijodhb)

## 1.3.1 Password Synchronization

The Fanout driver supports password set and check operations on the Subscriber channel. The driver does not support bidirectional password synchronization.

## 1.3.2 Data Synchronization

The Fanout driver supports direct and indirect data synchronization models.

| Model | Association | Description |
| Direct | Usually associated with views | Views provide the abstraction mechanism that facilitates integration with existing customer tables. |
| Indirect | Usually associated with tables | Customer tables may not match the structure required by the driver. Therefore, you should create intermediate staging tables that match the structure that the driver requires. |

For more information about data synchronization models see [Supported Operations](../../jdbc/data/supported-operations-on-jdbc-driver.html#supported-operations-on-jdbc-driver) in the [NetIQ Identity Manager Driver for JDBC Implementation Guide](../../jdbc/data/netiq-identity-manager-driver-for-jdbc.html#netiq-identity-manager-driver-for-jdbc).
