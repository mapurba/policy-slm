# 8.11 Transactions Are Left in the “Process” State and Not Processed

* Verify that all of the CI objects can be processed and that the status can be updated to a Success (S), Warning (W), or Error (E) state.

  If e-mail is configured in PeopleSoft and the SMTP gateway is down, an error can occur, causing the update of the transaction to fail. You should verify that all online processing of the application works correctly. PeopleCode attached to the update might sometimes fail, causing the transaction to fail. If system connectivity is lost, the database or application server goes down during processing and causes the driver to abandon the transaction. The transaction is left in the selected state with a status of I.

  *NOTE:*If notification processing is required, we recommend using the Identity Manager Notification Service instead of using SMTP processing as configured in PeopleSoft. For more information, see the [NetIQ Identity Manager E-Mail Notification Guide](../../../identity-manager-48/email_notifications/data/bookinfo.html#bookinfo).
