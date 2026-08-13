# 1.0 Understanding the Identity Manager Driver for JDBC

The Identity Manager Driver for Java DataBase Connectivity (JDBC) provides a generic solution for synchronizing data between Identity Manager and JDBC-accessible relational databases. The principal value of this driver resides in its generic nature. Unlike most drivers that interface with a single application, this driver can interface with most relational databases and database-hosted applications.

You can connect to a single database using a single JDBC driver. To configure a single JDBC driver to connect to multiple databases of the same type (for example, Oracle, MySQL, or PostgreSQL) use the driver with the Fan-Out agent. For more information, see [NetIQ Identity Manager Driver for JDBC Fanout Implementation Guide](../../jdbc_fanout/data/netiq-identity-manager-for-jdbc-fan-out-driver-implementation-guide.html#netiq-identity-manager-for-jdbc-fan-out-driver-implementation-guide).

* [Components for Data Synchronization](data-sync-components-for-identity-manager-jdbc-driver.html)
* [Database Concepts](database-of-jdbc-driver-identity-manager.html)
* [How the Driver Works](how-jdbc-driver-works.html)
* [Supported Operations](supported-operations-on-jdbc-driver.html)
* [Planning to Install the Driver](prerequisite-to-install-jdbc-driver.html)
