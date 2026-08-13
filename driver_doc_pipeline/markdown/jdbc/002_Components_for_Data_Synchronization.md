# 1.1 Components for Data Synchronization

This section provides information about the components required to integrate a connected system (database) with Identity Manager.

* [JDBC](data-sync-components-for-identity-manager-jdbc-driver.html#bvlr3cw)
* [Third-Party JDBC Driver](data-sync-components-for-identity-manager-jdbc-driver.html#ail8qxr)
* [Identity Vault](data-sync-components-for-identity-manager-jdbc-driver.html#bw58ykp)
* [Schema](data-sync-components-for-identity-manager-jdbc-driver.html#b1iivnba)
* [Logical Database Class](data-sync-components-for-identity-manager-jdbc-driver.html#ail8z7h)
* [XDS](data-sync-components-for-identity-manager-jdbc-driver.html#bvx42ot)

## 1.1.1 JDBC

Java DataBase Connectivity (JDBC) is a cross-platform database interface standard that Sun Microsystems developed.

Most enterprise database vendors provide a unique implementation of the JDBC interface. Four versions of the JDBC interface are available:

* JDBC 1 (Java 1.0)
* JDBC 2 (Java 1.2 or 1.3)
* JDBC 3 (Java 1.4 or 1.5)
* JDBC 4 (Java 1.6 or 1.7)

The JDBC driver primarily uses the JDBC 1 interface. It uses a small subset of JDBC 2, JDBC 3, or JDBC 4 methods when supported by third-party JDBC drivers.

## 1.1.2 Third-Party JDBC Driver

A third-party JDBC driver is one of the numerous JDBC interface implementations that the Identity Manager JDBC driver uses to communicate with a particular database.

For example, ojdbc6.jar is one of the Oracle JDBC drivers. Different third-party JDBC drivers implement different portions of the JDBC interface specification and implement the interface in a relatively consistent manner.

The following illustration indicates the relationship between the Identity Manager JDBC driver and third-party JDBC drivers.

*Figure 1-1* Identity Manager JDBC Driver vs. Third-Party JDBC Drivers

![](../graphics/jdbc_jdbcdriver_a.png)

## 1.1.3 Identity Vault

An Identity Vault is the data store that Identity Manager uses.

The Identity Vault is a persistent database powered by eDirectory and used by Identity Manager to hold data for synchronization with a connected system. The vault can be viewed narrowly as a private data store for Identity Manager or more broadly as a metadirectory that holds enterprise-wide data. Data in the vault is available to any protocol supported by eDirectory, including NetWare Core Protocol (NCP) and LDAP.

## 1.1.4 Schema

* [Directory Schema](data-sync-components-for-identity-manager-jdbc-driver.html#b1iivnbb)
* [Application Schema](data-sync-components-for-identity-manager-jdbc-driver.html#b1iivnbc)
* [Database Schema](data-sync-components-for-identity-manager-jdbc-driver.html#b1iivnbd)
* [Synchronization Schema](data-sync-components-for-identity-manager-jdbc-driver.html#b1iivnbe)

### Directory Schema

The directory schema is the set of object classes and attributes in the directory.

A database schema is a way to logically group objects such as tables, views, and stored procedures.

For example, the eDirectory User class and Given Name attribute are part of the eDirectory schema.

### Application Schema

The application schema is the set of classes and attributes in an application.

Because databases have no concept of classes or attributes, the JDBC driver maps eDirectory classes to tables or views, and maps eDirectory attributes to columns.

### Database Schema

Database schema is essentially synonymous with ownership. A database schema consists of database objects (for example, tables, views, triggers, stored procedures, and functions) that a database user owns.

With the JDBC driver, schema is useful to scope the database (reduce the number of database objects visible to the driver at runtime).

Ownership is often expressed by using a qualified dot notation (for example, indirect.usr, where indirect is the name of the database user that owns the table usr). All of the database objects owned by indirect constitute the indirect database schema.

### Synchronization Schema

The synchronization schema is the database schema visible to the driver at runtime.

## 1.1.5 Logical Database Class

The logical database class is the set of tables or view used to represent an eDirectory class in a database.

## 1.1.6 XDS

XDS format is the defined NetIQ subset of possible XML formats that Identity Manager can use.

XDS is the initial format for data coming from the Identity Vault. By modifying default rules and changing the style sheets, you can configure the JDBC driver to work with any XML format.
