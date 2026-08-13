# C.5 Subscriber Create Rule

To create a work order, the Subscriber Create rule is set up so all new work orders with the necessary information can be sent to the Subscriber channel. The following attributes must be present to pass the Create rule, or the event cannot be processed further:

| Required Attributes | Description | Values or Examples |
| DirXML-nwoSendToPublisher | Send the work order directly to the Publisher channel. | True or False |
| DirXML-nwoStatus | State of the work order so the driver knows what to do with the work order. | Pending, Configured, Error, On Hold, Warning |
| DirXML-nwoDoItNowFlag | When to perform the work order. | True or False |
| DirXML-nwoContent | Content to be processed by the driver. | XML code |
| DirXML-woType | Information about the work order. The driver does not change this attribute. | Case ignore string |
