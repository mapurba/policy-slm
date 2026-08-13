# 14.1 Third-Party JDBC Driver Interoperability

The Identity Manager JDBC driver is designed to interoperate with a specific set of third-party JDBC drivers, instead of a specific set of databases. In fact, the third-party JDBC driver, not the database, is the primary determinant of whether the JDBC driver works against any given database. As a general rule, if the JDBC driver interoperates well with a given third-party JDBC driver, it interoperates well with databases and database versions that the third-party driver supports.

We strongly recommend that you use the third-party JDBC drivers supplied by major enterprise database vendors whenever possible, such as those listed in [Supported Third-Party JDBC Drivers (Recommended)](supported-third-party-jdbc-drivers.html). They are usually free, mature, and known to interoperate well with the JDBC driver and the databases they target. You can use other third-party drivers, but NetIQ does not support them.

In general, most third-party drivers are backward compatible. However, even if they are backward compatible, they are generally not forward compatible. Anytime a database server is upgraded, the third-party driver used with this product should probably be updated as well.

Also, as a general rule, we recommend that you use the latest version of a third-party driver, unless otherwise noted.
