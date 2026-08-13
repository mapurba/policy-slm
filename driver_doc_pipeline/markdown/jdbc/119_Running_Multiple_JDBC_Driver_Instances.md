# D.11 Running Multiple JDBC Driver Instances

*Question:*
How do I run multiple JDBC driver instances in the same driver set? The instances require different versions of the same third-party JBDC driver (for example, the Oracle JDBC driver or the IBM DB2 Type 3 JDBC driver).

*Answer:*
Use the Remote Loader to load each JDBC driver instance in a separate Java Virtual Machine (JVM). When run locally in the same JVM, different versions of the same third-party classes collide.
