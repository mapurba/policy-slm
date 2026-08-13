# 8.9 No Transactions Are Coming Across the Publisher Channel

* Verify that there are active transactions in the queue ready for processing.
* Ensure that driver parameters are pointing to the correct PeopleSoft database. For example, transactions do not process if they are in the PROD database, and the driver is still pointing to the test database (which is configured to run with the driver, but holds no transactions).
