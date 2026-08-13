# 4.2 Migrating Fan-Out Driver Platform Services to the ACF2 Driver

To migrate, follow these tasks on your target platform system:

1. Stop the following started tasks:

   * PLATRCVR
   * ASCLIENT
2. Remove ASCLIENT and PLATRCVR from your system startup and shutdown procedures.
3. Remove the Fan-Out driver’s ACF2 exits.

   For details on uninstalling ACF2 exits, see the Identity Manager 4.8 Fan-Out Driver for Mainframes Administration Guide, which is available at the [Identity Manager 4.8 Drivers Documentation Web site](https://www.netiq.com/documentation/identity-manager-47-drivers)
4. Install the driver shim on the connected system.

   For details, see [Installing the Driver Shim on the Connected System](b3xehpq.html).
