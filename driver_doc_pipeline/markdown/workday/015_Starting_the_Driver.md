# 2.11 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Live > Start Driver.

   The driver cannot initialize completely unless it successfully connects to the Remote Loader and loads the Workday driver shim.

For information about management tasks for the driver, see [Section 8.0, Managing the Driver](t4avmq7f8jir.html).
