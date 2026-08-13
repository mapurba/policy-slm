# B.1 New Objects Used by the Driver

The Identity Manager WorkOrder driver uses two new object classes in the Identity Vault to configures work orders and record the results. For a description of a schema for these objects, see [Section C.0, Schema and Policy Rules For Work Order Management](schema-policy-rules-work-order-management.html).

* [DirXML-WorkOrder Object](b8x1wva.html#b92pw8r)
* [DirXML-WorkToDo Object](b8x1wva.html#b92pwrs)

## B.1.1 DirXML-WorkOrder Object

The DirXML-WorkOrder object delays the work order to be processed until the scheduled date and time or until a dependent work order is configured. The driver also repeats work orders if the work order has a repeating interval.

If the work order is marked DoItNow, the driver performs it immediately and does not wait for a polling time or time of day. To learn how to use the DoItNow and SendToPublisher flags, see [DoItNow and SendToPublisher Flags](b7j2hzl.html).

## B.1.2 DirXML-WorkToDo Object

The driver creates this object and writes it to the Identity Vault to process the work order. The value of the WorkOrder Content attribute becomes the value of the DirXML-WorkToDo Content attribute. The driver sends this object to the Identity Vault, returns the status of the work order (Configured, Error, etc.), and writes it in the ProcessLog attribute. Any results or information available to the driver is recorded in the ProcessLog.

If the work order has a repeat attribute, the work order gets a new due date with the interval added and the status remains pending, allowing it to be processed again on the new due date.
