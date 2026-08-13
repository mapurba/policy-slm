# 6.3 Human Resource Example without an HR Driver

This example creates a new user and postpones activating the new employee’s access to the system until the hire date by putting policies into the WorkOrder driver to create the work order. [Figure 6-2](hr-example-without-hr-driver.html#b8ylff6) illustrates this sample configuration.

*Figure 6-2* Data Flow without an HR Driver

![](../graphics/work_order_decision005_a.png)

When a new user object is created in the Identity Vault, a policy in the WorkOrder driver checks to see if the loginDisabled attribute is set to True. If it is not set to True, the Create rule blocks the event. If it is set to True, the policy creates a work order to set the loginDisabled attribute on the user to False on the loginActivationTime.

The following policies or rules show how to implement the sample configuration:

* [Filter Additions](hr-example-without-hr-driver.html#bg9wmyb)
* [Subscriber Create Rule](hr-example-without-hr-driver.html#bg9wnaj)
* [Subscriber Command Transform](hr-example-without-hr-driver.html#bg9wnhi)
* [Work Order E-Mail Notification of Work Order Completion](hr-example-without-hr-driver.html#bg9wns1)

## 6.3.1 Filter Additions

These additions modify the filter to allow user objects with loginActivationTime and loginDisabled attributes to synchronize on the Subscriber channel. You can view the sample at [wo-filter.xml](http://www.novell.com/documentation/idm40drivers/work_order/samples/wo-filter.xml).

## 6.3.2 Subscriber Create Rule

The Create rule vetoes this event if the loginActivationTime or the loginDisabled attributes are not present. It also vetoes this event if the loginDisabled attribute is set to False. You can view the sample at [wo-create.xml](http://www.novell.com/documentation/idm40drivers/work_order/samples/wo-create.xml).

## 6.3.3 Subscriber Command Transform

This policy checks to see if the event is an Add of a user object. If that is true, the policy creates a WorkOrder object. The DN of the user object is added to the DirXML-nwoContent attribute. The DirXML-DueDate is set to the loginActivationTime. The DirXML-nwoStatus is set to pending. The DirXML-nwoSendToPublisher attribute is set to True.

This work order has not yet been created in the Identity Vault, so the sample configuration creates the work order in the Identity Vault by setting the SendToPublisher attribute to True. This tells the publisher in the WorkOrder driver to write the policy to the work order container that it looks in for work orders to be processed. You can view the sample at [wo-sub-cmd-transform.xml](http://www.novell.com/documentation/idm40drivers/work_order/samples/wo-sub-cmd-transform.xml).

## 6.3.4 Work Order E-Mail Notification of Work Order Completion

This policy can be used with the WorkOrder driver to send e-mail notification of a completed work order. This policy is in the Publisher Command Transform. The policy checks to see if a DirXML-WorkOrder modify event is happening. If it is, it builds an e-mail from the status, description, and process log of the work order and then sends it to an administrator. This notifies the administrator that a work order has been processed and gives them the results. You can view the sample at [wo-pub-cmd-transform.xml](http://www.novell.com/documentation/idm40drivers/work_order/samples/wo-pub-cmd-transform.xml).
