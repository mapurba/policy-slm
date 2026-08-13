# 14.7 Security Issues

To ensure that a secure connection exists between the Identity Manager JDBC driver and a third-party driver, we recommend the following:

* Run the JDBC driver remotely on the database server.
* Use SSL to encrypt communications between the Identity Manager server and the database server.

If you cannot run the JDBC driver remotely, you might want to use a type 2 or type 3 JDBC driver. These driver types often facilitate a greater degree of security through middleware servers or client APIs unavailable to other JDBC driver types. Some type 4 drivers support encrypted transport, but encryption is the exception rather than the rule.
