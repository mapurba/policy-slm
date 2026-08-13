# C.1 DirXML-WorkOrder Object

The DirXML-WorkOrder object (sometimes referred to as the WorkOrder object in this documentation) is used to tell the driver what tasks to perform. It delays the work order until a date and time or until another work order is configured. It also repeats work orders at a given interval.

The following table shows the work order attributes you need to specify:

| Work Order Attributes (eDirectory Namespace) | Description | Type |
| Description | Description of the work order. The driver does not change this attribute. It is passed through to the WorkToDo object when the work order is processed. | Case ignore string |
| Common Name | The naming attribute for eDirectory | Case ignore string |
| DirXML-nwoContact Name | Information about the work order. The driver does not change this attribute. It is passed through to the WorkToDo object when the work order is processed. | Case ignore string |
| DirXML-nwoContent | This attribute is passed through to the WorkToDo object. It is used by policies to process the work order. | Case ignore string |
| DirXML-DueDate | The date and time the work order is to be processed. | Time |
| DirXML-nwoDoItNowFlag | If this attribute is set to True, the Subscriber channel sends the work order to the Publisher channel to be processed immediately. | Boolean |
| DirXML-nwoSendToPublisher | If this attribute is set to True, the Subscriber channel sends the work order to the Publisher channel to be written to the WorkOrder container. For example, if the work order was created by a policy as a result of an event in the Identity Vault. | Boolean |
| DirXML-woType | Information about the work order. The driver does not change this attribute. It is passed through to the WorkToDo object when the work order is processed. | User defined |
| DirXML-nwoCreationDate | Information about the work order. The driver does not change this attribute. | Time |
| DirXML-nwoDependentWorkOrder | The DN of the dependent work order. The work order is not processed until the dependent work order has a status of Configured. If the attribute is nonexistent or empty, it is ignored. | Distinguished Name |
| DirXML-nwoRepeatInterval | The amount of time, in minutes, before the work order is repeated. This value is added to the due date after the work order is processed. | Case ignore string |
| DirXML-nwoRepeatCount | Repeats the work order as many times as the number specifies. Use this attribute in association with the DirXML-nwoRepeatInterval attribute. | Case ignore string |
| DirXML-nwoStatus | Status of the work order.  Pending: The work order will be processed on the due date.  Configured: The work order was processed.  Error: An error occurred when processing.  On Hold: The work order is not to be processed. | Case ignore string |
| DirXML-nwoWorkOrderNumber | Information about the work order. The driver does not change this attribute. It is passed through to the WorkToDo object when the work order is processed. | Case ignore string |
| DirXML-nwoDeleteOnError | If this attribute is set to True, the work order is deleted if the status is Error and the DeleteDueDate has expired. | Boolean |
| DirXML-nwoProcessLog | Contains information relating to the processing of the work order. | Case ignore string |
| DirXML-nwoDeleteDueDate | If the status is Pending or Configured, this attribute shows the date and time the work order will be deleted. | Time |
| DirXML-CreatorName | Information about the work order. The driver does not change this attribute. It is passed through to the WorkToDo object when the work order is processed. | Distinguished Name |
| DirXML-Other1 | Information about the work order. The driver does not change this attribute. It is passed through to the WorkToDo object when the work order is processed. | Case ignore string |
| DriXML-Other2 | Information about the work order. The driver does not change this attribute. It is passed through to the WorkToDo object when the work order is processed. | Case ignore string |
