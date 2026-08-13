# 2.0 Implementation Checklist

Use the following checklist to ensure that you complete all of the tasks required to set up and use the WorkOrder driver.

*Table 2-1* WorkOrder Implementation Checklist

| Task | Details |
| * Install the WorkOrder driver files | By default, the WorkOrder driver files (driver shim and configuration file) are copied to the Identity Manager server when the Identity Manager engine is installed. If the driver is not on the Identity Manager server (because a custom installation was performed, or you want to run the driver on a server other than the Identity Manager server), see [Section 3.0, Installing Driver Files](work-order-install-driver-files.html). |
| * Create a new WorkOrder driver  or  Upgrade an existing WorkOrder driver to the new version | You need to import the basic configuration file to create the driver. For instructions, see [Section 4.0, Creating a New Driver Object](b94c4u0.html).  If you have an existing driver, you can upgrade its configuration to this version. For instructions, see [Section 5.0, Upgrading an Existing Driver](upgrade-existing-driver.html). |
| * Customize the driver | The basic configuration for the WorkOrder driver enables it to create WorkOrder objects and WorkToDo objects. This is the extent of what the WorkOrder driver does when using the base configuration. For any additional work to be done, you must customize the WorkOrder driver or other Identity Manager drivers to perform the desired work.  For instructions, see [Section 6.0, Customizing the Driver](customize-driver.html). |
| * Create work orders | Most work orders are likely created by other drivers as part of the work order process you establish while customizing the driver (see the previous task). However, you can also create work orders manually as well as modify existing work orders.  For instructions, see [Section 7.0, Creating and Managing Work Orders](create-manage-work-orders.html). |
