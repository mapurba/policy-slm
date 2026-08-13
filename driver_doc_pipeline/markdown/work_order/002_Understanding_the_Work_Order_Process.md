# 1.1 Understanding the Work Order Process

From a high-level perspective, work orders are processed as follows:

1. A work order is created, either through an automated process (another driver) or a manual process (Identity Console), and is added as a WorkOrder object in a the Identity Vault芒聙聶s work order container.
2. At the scheduled time (as defined in the WorkOrder object), the driver begins processing the work order.
3. The driver applies any policies to the work order (performing any actions associated with the policies) and creates a WorkToDo object in the Identity Vault芒聙聶s work order container.
4. Depending on how you configure the WorkOrder driver and the other drivers in your system, either the WorkOrder driver performs the desired work or other drivers use the information in the WorkToDo object to perform the work. Because the WorkOrder driver is designed to accommodate a variety of configuration scenarios, sample scenarios are provided in [Section 6.0, Customizing the Driver](customize-driver.html).

The following sections provide detailed information about the work performed by the driver芒聙聶s Subscriber and Publisher channels. Because the WorkOrder driver channels function differently than with other drivers, you should carefully review the information.

* [Subscriber Channel Functions](bfbfkyf.html#bfdgk0b)
* [Publisher Channel Functions](bfbfkyf.html#bfdgk0d)

## 1.1.1 Subscriber Channel Functions

This section provides a basic understanding of the functions the Subscriber channel performs in the WorkOrder driver.

First, Placement and Create rules are configured so all new work orders that contain the required attributes are sent to the Subscriber channel. The following attributes must be present for a work order to pass the Create rule and go to the Subscriber channel:

* DirXML-nwoContent
* DirXML-nwoStatus
* DirXML-DoItNow Flag
* DirXML-SendToPublisher Flag

Figure 3-1 shows what happens when the Subscriber channel receives a work order.

*Figure 1-1* Subscriber Channel Configuration

![](../graphics/work_order_decision007_a.png)

The Subscriber channel performs the following actions:

1. Creates an association for each WorkOrder object it receives.
2. Checks if the DoItNow and SendToPublisher flags are set to True. If these attributes are set to True, the Subscriber channel builds a work order and sends it immediately to the Publisher channel.
3. If the DoItNow and SendToPublisher flags are not set to True, the Subscriber channel waits until the next event.

## 1.1.2 Publisher Channel Functions

This section reviews the functions of the Publisher channel.

* [The Publisher Channel Wakes Up](bfbfkyf.html#bfdgk0e)
* [How the Publisher Channel Processes Work Orders](bfbfkyf.html#bfdgk0g)
* [How the Publisher Channel Deletes Work Orders](bfbfkyf.html#bfdgk0i)

### The Publisher Channel Wakes Up

The following flowchart illustrates the Publisher channel芒聙聶s action when it wakes up.

*Figure 1-2* Publisher Channel Configuration

![](../graphics/work_order_decision008_a.png)

* The Publisher channel wakes because the Subscriber channel sends a WorkOrder object. If the SendToPublisher flag is set to True, the work order is written out to the work order container. If the DoItNow flag is set to True, the work order is processed immediately.
* The Publisher channel wakes when the polling time has expired and queries the work order container for work orders that are pending and due. The driver processes these work orders. Work orders with delete due dates are deleted.

  1. The Publisher channel queries the work order container for work orders that are pending and due. See [How the Publisher Channel Processes Work Orders](bfbfkyf.html#bfdgk0g).
  2. The Publisher channel queries all work orders for expired DeleteDueDates. See [How the Publisher Channel Deletes Work Orders](bfbfkyf.html#bfdgk0i).
* If the driver heartbeat is configured, the driver wakes to report the driver status.

### How the Publisher Channel Processes Work Orders

After the Publisher channel queries the Identity Vault for work orders, it configures the work orders in the driver. The following flowchart illustrates how the Publisher channel processes work orders.

*Figure 1-3* How the Publisher Processes Work Orders

![](../graphics/work_order_decision003_a.png)

1. Before a work order is processed, the driver checks the DependentWorkOrder attribute to see if the work order is dependent on another work order. If there is a dependent work order, the Publisher channel queries Identity Manager to see the status of the dependent work order. If the dependent work order status is configured, the Publisher channel processes the work order. If not, the work order waits until the next polling loop to see if the dependent work order has been configured.
2. The Publisher channel performs the work orders that are due, completing the appropriate action based on the attributes of the DirXML-WorkOrder objects.
3. To process the work order, the driver writes a DirXML-WorkToDo object to the WorkToDo container. The DirXML-nwoContent attribute of the WorkToDo object contains the value of the DirXML-nwoContent attribute of the WorkOrder object. The default configuration does not do anything else with the WorkToDo object. A policy could use the WorkToDo object to process the work order. For example, the content attribute might contain the DN of a user object whose LogOnDisabled flag should be changed from True to False at the due date.
4. The Publisher channel updates the DirXML-WorkOrder with the results. If the WorkToDo object was processed without an error, the status of the work order is changed to Configured. If an error occurred, then the status is changed to Error. The work order process log is updated to contain the results.
5. If the WorkOrder object has a repeat interval value, the value is added to the Due Date and the work order status remains Pending. This allows for the work order to be repeated as many times as specified in the repeat interval count value, or indefinitely if no repeat interval count value is specified. The process log contains the results.

### How the Publisher Channel Deletes Work Orders

The Publisher channel now queries the work order container for work orders with an expired DeleteDueDate attribute. If the status of the work order is Pending or Configured, and the DeleteDueDate has expired, the work order is deleted. The work order is also deleted if it has an error status and the DeleteOnError attribute is set to True. The following flowchart illustrates this process.

*Figure 1-4* The DeleteDueDate Process

![](../graphics/work_order_decision009_a.png)
