# 6.2 Human Resource Example Using an HR Driver

The following example illustrates how the WorkOrder driver can be used with an HR driver (SAP, PeopleSoft, and so forth) to create a new user and postpone activating the new employee’s access to the system until the hire date. [Figure 6-1](hr-example-hr-driver.html#b8ylevn) illustrates how these drivers work together in the example configuration.

*Figure 6-1* Data Flow with an HR Driver

![](../graphics/work_order_decision004_a.png)

In this scenario, assume that the new employee’s name is Albert Hauser. Albert is hired, but does not begin work until a future date and time. He is put into the HR system with the hire date set. Albert is marked as not active and does not have access to the system.

The HR Identity Manager driver writes Albert’s user object to the Identity Vault. A policy in that driver checks to see if he is active. If he is active, the driver performs the work. If he is not active, the policy creates a work order to activate Albert’s account on the hire date. The work order is marked as pending. A policy in the WorkOrder driver processes the work order on the hire date. The policy in the WorkOrder driver sets the user object’s loginDisabled attribute to False, allowingAlbert to log in.

The sample could be extended to allow other Identity Manager drivers to have a Create rule to disallow the creation of the user object in other connected systems until the user object’s loginDisabled attribute is set to False. The result is that the user’s system access is provisioned on his hire date and not before.

## 6.2.1 Human Resource Driver Policies

The following policies or rules show how to implement this sample. In the sample, the WorkOrder driver is acting as the HR system interface. The WorkOrder driver is configured to provide the needed attributes: LastName, FirstName, HireDate, and Disabled.

* [Mapping Rule](hr-example-hr-driver.html#b92p17g)
* [Filter](hr-example-hr-driver.html#b92p1sp)
* [Command Transformation Policy](hr-example-hr-driver.html#b92p29h)

### Mapping Rule

The mapping rule maps the attributes used in the WorkOrder driver to attributes in the Identity Vault. You can view the sample at [hr-drv-schema-map.xml](http://www.novell.com/documentation/idm40drivers/work_order/samples/hr-drv-schema-map.xml).

### Filter

The filter attribute allows only the attributes that are needed by this example to be passed through. The DirXML-DueDate is notify only. This attribute should not be applied to the user object. However, it should be available for the Command Transformation. You can view the sample at [hr-drv-filter.xml](http://www.novell.com/documentation/idm40drivers/work_order/samples/hr-drv-filter.xml)

### Command Transformation Policy

The Command Transformation policy checks to see if a user object is being added to the Identity Vault. It also ensures that the loginDisabled attribute is set to True. If the conditions are satisfied, the policy then creates a work order and places it in the WorkOrder container. The WorkOrder driver looks in this container for work orders to process. The policy puts the DN of the user that was created into the DirXML-nwoContent attribute. You can view the sample at [hr-drv-cmd-transform.xml](http://www.novell.com/documentation/idm40drivers/work_order/samples/hr-drv-cmd-transform.xml).

The policy also puts the DirXML-DueDate from the user into the WorkOrder object DirXML-DueDate and then sets the work order status to Pending.

There is a second policy that sets the status of the work order. You can view the sample at [hr-drv-cmd-transform2.xml](http://www.novell.com/documentation/idm40drivers/work_order/samples/hr-drv-cmd-transform2.xml).

## 6.2.2 WorkOrder Driver Policy

The WorkOrder driver policy uses only the Publisher Command Transformation policy. The Command Transformation policy checks to see that a DirXML-WorkToDo object is being added. If it is, the policy gets the DN of the user from the DirXML-nwoContent attribute. It then sets the user’s Login Disable attribute to False. This allows the user to log in.

*NOTE:*<do-add-dest-attr-value class-name="User" direct="true" name="Login Disabled"> should not be used.

When direct is equal to True, the action is performed as desired, but the results are not returned to the driver. Therefore, the driver cannot correctly report the results of the write. You can view the sample at [hr-wo-drv-pub-cmd-transform.xml](http://www.novell.com/documentation/idm40drivers/work_order/samples/hr-wo-drv-pub-cmd-transform.xml).
