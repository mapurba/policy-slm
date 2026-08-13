# 4.2 Migrating Fan-Out Driver Platform Services to the Top Secret Driver

Perform the following steps on your target platform system:

1. Stop the following started tasks:

   * PLATRCVR
   * ASCLIENT
2. Remove ASCLIENT and PLATRCVR from your system startup and shutdown procedures.
3. Remove the Fan-Out driver Top Secret exit.
4. Install the driver shim on the connected system.

   For details, see [Installing the Driver Shim on the Connected System](b3xehpq.html).
