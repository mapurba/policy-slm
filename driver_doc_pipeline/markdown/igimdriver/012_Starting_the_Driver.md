# 2.7 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs. You can use Identity Console or dxevent commands to start the driver.

To start the driver using Designer:

1. In Designer, open your project.
2. In the Modeler view, right-click the driver icon ![IGIM-driver-icon](../graphics/driver_icon_n.png "IGIM-driver-icon") or the driver line, then select Live > Start Driver.

To start the driver using Identity Console:

1. In Identity Console, click IDM Administration.
2. Browse to and select the driver set object that contains the driver you want to start.
3. Click the upper right corner of the driver, then click Start driver.

For instructions about starting and stopping the Remote Loader and driver instances on Linux and Windows, see [Starting and Stopping the Remote Loader](../../../identity-manager-48/driver_admin/data/b18xta1v.html#b192fqcb) in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).
