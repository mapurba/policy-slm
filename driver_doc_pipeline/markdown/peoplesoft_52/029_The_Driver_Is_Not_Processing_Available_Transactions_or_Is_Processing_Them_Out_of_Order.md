# 8.1 The Driver Is Not Processing Available Transactions or Is Processing Them Out of Order

* Set the driver trace level to 5 and verify that the DIRXML\_DTTM and DIRXML\_CURRDTTM values of the Transaction records being processed are in proper lexicographic format.
* If the records are not in the correct format, refer to [Section 3.0, Configuring Your PeopleSoft Environment](configure-driver-environment.html).
* If the records are in the correct format, verify that Transaction date and time field values are correct and correspond to the system date and time.
