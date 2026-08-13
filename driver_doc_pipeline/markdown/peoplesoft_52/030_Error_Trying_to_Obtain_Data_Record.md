# 8.2 Error Trying to Obtain Data Record

The following are typical reasons for this error:

* The Data record identified in a Transaction record was deleted from the PeopleSoft server before the Transaction was processed.
* The Data record identified in a query or Subscriber channel operation has been deleted from the PeopleSoft server.
* Through a database error or bad configuration, multiple Data records with the same primary key value exist in the PeopleSoft database.

  Verify the reason for the problem by using either an SQL tool, the PSA DirXML Schema 01 sample application, or the PeopleSoft Application Designer’s Test Component Interface tool (see [Section 3.0, Configuring Your PeopleSoft Environment](configure-driver-environment.html).) Correct any errors that might exist.
