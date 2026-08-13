# 15.9 Null Pointer Exception Appears in the Trace for JDBC Driver for Connecting to Oracle Database While Using ojdbc10.jar

Issue: The ojdbc10.jar is not supported for the JDBC Driver.

Fix: For the driver to work you must use:

* ojdbc8.jar for Oracle 18c and 19c
* ojdbc7.jar for Oracle 12c

For more information about the jar file to be used refer to [Oracle Thin Client JDBC Driver](supported-third-party-jdbc-drivers.html#bvlst6q).
