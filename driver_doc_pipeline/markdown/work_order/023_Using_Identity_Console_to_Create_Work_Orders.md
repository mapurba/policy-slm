# 7.2 Using Identity Console to Create Work Orders

You can use Identity Console to manually create and maintain work orders:

* [Creating a New Work Order](use-imanager-create-work-orders.html#b8yqh49)
* [Editing Work Order Properties](use-imanager-create-work-orders.html#b8yx50m)
* [Filtering the Work Order List](use-imanager-create-work-orders.html#bffknw2)

## 7.2.1 Creating a New Work Order

In Identity Console:

1. In the Identity Manager frame, click Work Order Management to display the Work Order Management page.
2. In the WorkOrder Driver field, browse for and select the WorkOrder driver for which you are creating the work order.
3. Click New, specify a name for the work order, then click OK.

   The name is used for the WorkOrder object’s name in the Identity Vault.
4. Fill in the fields on the WorkOrder page. For information about the fields, see the next section, [Editing Work Order Properties](use-imanager-create-work-orders.html#b8yx50m).

## 7.2.2 Editing Work Order Properties

The Work Order page lets you configure a new work order or edit an existing work order.

1. If you are editing an existing work order and the WorkOrder page is not already open, open the Work Order page:

   1. In the Identity Manager frame, click Work Order Management to display the Work Order Management page.
   2. In the WorkOrder Driver field, browse for and select the WorkOrder driver associated with the work order you want to edit.

      After you select the appropriate WorkOrder driver, all work orders associated with the driver are listed.
   3. Click the work order you want to edit.
2. Fill in the following fields:

   *Status:*
   The status of a new work order can be either Pending or On Hold. Normally, work order status is Pending. You can stop a work order by selecting On Hold. After a work order has been processed, the resulting work order status appears in this field.

   *Due Date:*
   You can choose to have the driver do the work order immediately or schedule the work order. To schedule a due date, click the calendar icon. Use the calendar to choose the date. Use the arrows to select the month, year, and time.

   *Repeat Work Order:*
   Select this option to have the work order processed multiple times. Specify the time interval by choosing the number of weeks, days, hours, or minutes before the work order is to be repeated. The work order stops repeating on the delete date unless it is manually deleted, edited, or the driver sends back an error message.

   *Delete Date:*
   Use the calendar control to select a date to delete work orders that have been configured. Work orders with an error status are not deleted unless you select Delete Work Order Even if the Work Order Has an Error.

   *Dependent Work Orders:*
   When you create a new work order, you can make it dependent on one or more work orders. Click ![](../graphics/browsebutton01_n.png) to browse for and select dependent work orders. To remove a work order from the list, select the work order, then click ![](../graphics/removebutton_n.png).

   *Type:*
   Use this field to specify a work order type. The driver does not change this attribute. The attribute is passed through to the WorkToDo object when the work order is processed.

   *Work Order Number:*
   A unique work order number. This value can be assigned by a corporate work order system other than NetIQ eDirectory, such as a work order database.

   *Contact Information:*
   Contact information for the person responsible for the work order.

   *Work Order Processing Log:*
   After a work order has been processed, the driver logs the results of the work order, including the status, in this field. This allows you to check the work order's current status and identify any problems the driver encountered while attempting to configure the work order.

   The work order's status attribute remains pending until the work order is processed. The work order is processed when the due date has expired or the Do It Now flag is set. The driver reports the processing results by setting the status attribute to Configured, Warning, or Error. If the work order is On Hold, it ignores the work order.

   * *Pending:*
     The driver is waiting for the due date to complete the work order.
   * *Configured:*
     The work order has been successfully processed.
   * *Error:*
     The driver was unable to perform the work order.
   * *Warning:*
     There is a warning regarding the work order. For example, if the work order has a dependent work order with a later due date, the driver sends a warning.

   *Description:*
   The work order description.

   *Work Order Content:*
   The data in this field is used by the driver’s rules to process the work order. For example, it might be the XML that the Command Transformation uses to process the work order.
3. Select one of the following options when you are finished specifying or editing the work order properties:

   * Click Apply to save the current information and continue working.
   * Click OK to save and close the work order.
   * Click Cancel to close the work order without saving the information.

## 7.2.3 Filtering the Work Order List

1. Click Show under Work Order Management.
2. From the drop-down menu, select the filter type:

   *Show all:*
   All work orders associated with the driver are listed.

   *Configured:*
   Only configured work orders associated with the driver are listed.

   *Error:*
   Only work orders with an error status are listed.

   *On Hold:*
   Work orders that have been manually placed on hold are listed.

   *Pending:*
   Work orders that are not yet due are listed.
