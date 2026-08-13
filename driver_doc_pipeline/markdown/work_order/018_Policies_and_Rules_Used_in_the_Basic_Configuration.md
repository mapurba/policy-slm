# 6.1 Policies and Rules Used in the Basic Configuration

This section describes policies and rules for the Subscriber and Publisher channels in the WorkOrder driver’s basic configuration. For an overview on how the Subscriber and Publisher channels work, see [Subscriber Channel Functions](bfbfkyf.html#bfdgk0b) and [Publisher Channel Functions](bfbfkyf.html#bfdgk0d).

* [Subscriber Channel](policies-rules-used-in-basic-configuration.html#b7owpxw)
* [Publisher Channel](policies-rules-used-in-basic-configuration.html#b7owriw)

## 6.1.1 Subscriber Channel

The Subscriber channel processes only events that pertain to the work orders. The following table lists the rules and policies used in configuring the Subscriber channel:

| Rule or Policy | What it does |
| Subscriber Filter | Allows only events for WorkOrder objects to be processed. |
| Event Transformation | Not used in the packages. |
| Matching Rule | Not used in the packages. |
| Create Rule | Contains rules only for WorkOrder objects.  Requires values for the following attributes on a WorkOrder object:  * nwoStatus * nwoSendToPublisher * nwoDoItNow * nwoContent * nwoType  If the values are not present, the work order is not sent to the Publisher channel and the work order is not updated by the driver.  For a description of these attributes, see [Section C.0, Schema and Policy Rules For Work Order Management](schema-policy-rules-work-order-management.html). |
| Placement Rule | Maps work orders from the work order container you specified to the driver. This mapping is necessary so that the Subscriber channel can check the work orders to see if the DoItNow flag is set to True. |
| Command Transformation | Not used in the packages. |
| Schema Mapping | Maps the eDirectory namespace to the Work Order namespace. |
| Output Transformation | Not used in the packages. |

## 6.1.2 Publisher Channel

The following table lists the rules and policies used to configure the Publisher channel:

| Rule or Policy | What it does |
| Schema Mapping | Maps the Work Order driver namespace to the eDirectory namespace. |
| Event Transformation | Not used in the packages. |
| Publisher Filter | Allows only events for WorkOrder objects to be processed. |
| Matching Rule | Not used in the packages. |
| Placement Rule | Places WorkOrder and WorkToDo objects in the correct container as defined in the driver’s configuration parameters. |
| Command Transformation | Not used in the packages. |
