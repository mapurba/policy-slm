# 7.1 Mismatch in Driver Version

Identity Console and the driver trace display different versions of the Fanout driver. This occurs because they fetch the version documents from different sources - the Fanout driver and the JDBC driver. For example, Identity Console’s Version Discovery shows the version of the Fanout driver, but the trace shows both versions for both the drivers.

This is because some documents are directly returned from JDBC driver whereas some are constructed by the Fanout driver.
