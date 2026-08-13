# 2.9 Configuring the Driver to Include Additional Transaction Type References

Additional transaction type references can be configured in the Publisher driver parameter Transaction Log Criteria Reference List for Normal Polling (wdWorkerTransactLogCritList). By default, if a simple value is added to this parameter, this becomes a Business\_Process\_Type transaction type reference.

In this case, the transaction reference types for each business process types must be obtained from the Workday application. To obtain the business process type values from Workday, login to the Workday application > Go to Transaction Types available for Subscription report > click on the required event > click on Integration IDs > collect the value for the Business Process Types ID as displayed. For example, if the Business Process Type is Termination in the Workday application, the corresponding wdWorkerTransactLogCritList driver configuration transaction type value will be Terminate Employee.

If a transaction type reference other than Business\_Process\_Type is needed, the format of the value entered in Transaction Log Criteria Reference List for Normal Polling should have the name of the transaction type reference, a colon and then the value for that transaction type reference. For example,

```
Event_Lite_Type_ID:Custom Object Non-Effective-Dated Change
```

or

```
WID:08e574a19f6b400fac5dbe71ea854f1d
```

As per the above examples, any values without a colon will default to a Business\_Process\_Type. Values with a colon will be parsed with the value of the transaction type reference on the left of the colon and the value for that transaction type reference on the right of the colon.

Apart from Business\_Process\_Types, Workday 32.0 provides the following transaction type references:

* WID
* Event\_Lite\_Type\_ID
* Rorganization\_Activity\_Type
