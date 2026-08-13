# 15.4 Driver Shim Is Irresponsive When a Connected Database Server Does Not Respond

This issue is observed in the following cases:

* *Case 1:*
  The driver tries to update a record that is currently being modified through another database connection.

  If you instruct the driver to update this record, the driver will wait to operate on it until the updated record is committed to the database.

  This is an expected behavior. The driver is designed to wait to eliminate the chances of inconsistent results in such situations.
* *Case 2:*
  When the transaction log in a database is filled. For example, Sybase database.

  The database does not allow any operations until the transaction log is cleared.

  It is the responsibility of the database administrator to clear the transactions log. When the log is cleared, the database is unlocked for operations and the driver resumes processing without issues.
