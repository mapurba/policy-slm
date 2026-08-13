# B.2 DoItNow and SendToPublisher Flags

The WorkOrder driver has two flags to initiate a work order event.

* [DoItNow Flag](b7j2hzl.html#b7moy1h)
* [SendToPublisherFlag](b7j2hzl.html#b7moyay)

## B.2.1 DoItNow Flag

When this flag is set to True, the Subscriber channel wakes up the Publisher channel by sending the work order to the Publisher channel. This allows the Publisher channel to perform the work order immediately instead of waiting for the next polling time or polling interval.

Use this flag when you want the work order completed immediately. You can set this flag to True when you manually create a work order, or you can use policies in an automated solution to determine whether the flag should be set.

## B.2.2 SendToPublisherFlag

When this flag is set to True for a work order, the Subscriber channel sends the work order to the Publisher channel and the Publisher channel writes the WorkOrder object to the WorkOrder container specified in the configuration parameters.

This flag is usually set to False. However, if a work order is initiated by a policy in response to an event in the Identity Vault, setting the flag to True enables the WorkOrder driver to create the WorkOrder object and add it to the Identity Vault’s work order container. The WorkOrder object can then be processed like any other WorkOrder object added to the container by another driver.
