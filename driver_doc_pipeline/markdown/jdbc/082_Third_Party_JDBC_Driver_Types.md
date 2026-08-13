# 14.2 Third-Party JDBC Driver Types

The following sections describe four third-party JDBC driver types and explains the recommended type for use with the Identity Manager JDBC driver:

* [Driver Types](types-of-jdbc-driver-types.html#bgz0z3g)
* [Which Type To Use?](types-of-jdbc-driver-types.html#bvmbajo)

## 14.2.1 Driver Types

There are four types of third-party drivers:

* *Type 1:*
  A third-party JDBC driver that is partially Java and communicates indirectly with a database server through a native ODBC driver.

  Type 1 drivers serve as a JDBC-ODBC bridge. Sun provides a JDBC-ODBC bridge driver for experimental use and for situations when no other type of third-party JDBC driver is available.
* *Type 2:*
  A third-party JDBC driver that is part Java and communicates indirectly with a database server through its native client APIs.
* *Type 3:*
  A third-party JDBC driver that is pure Java and communicates indirectly with a database server through a middleware server.
* *Type 4:*
  A third-party JDBC driver that is pure Java and communicates directly with a database server.

## 14.2.2 Which Type To Use?

Type 3 and 4 drivers are generally more stable than type 1 and 2 drivers. Type 1 and 2 drivers are generally faster than type 3 and 4 drivers. Type 2 and 3 drivers are generally more secure than type 1 and 4 drivers.

Because Identity Manager uses a directory as its datastore, and because databases are usually significantly faster than directories, performance isn’t a primary concern. Stability, however, is an issue. For this reason, we recommend that you use a type 3 or 4 third-party JDBC driver whenever possible.

Because third-party code is being executed within the environment, it is recommended to always use the Remote Loader to execute third-party code on its own to ensure the integrity of the directory process. This also makes upgrades of the shim or third-party code simple and safe because the directory does not need to be restarted.
