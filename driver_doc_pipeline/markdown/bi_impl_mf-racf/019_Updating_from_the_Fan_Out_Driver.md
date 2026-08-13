# 4.1 Updating from the Fan-Out Driver

The Fan-Out driver provides one-way synchronization to a heterogeneous mix of systems including Linux and UNIX systems, and IBM i5/OS\* (OS/400\* operating system) and z/OS systems. The Fan-Out driver also provides authentication redirection from those systems.

Moving to the Identity Manager 4.8 driver for RACF provides two main advantages:

* *Bidirectional Synchronization:*
  The driver allows synchronization from the connected system.
* *Standard Identity Manager Policies That Simplify Customization:*
  The Fan-Out driver makes minimal use of Identity Manager policies.

Consider the following before migrating from the Fan-Out driver:

* *Heterogeneity:*
  The Fan-Out driver supports operating system environments besides RACF. You can continue to use the Fan-Out driver for those systems while using the Identity Manager 4.8 driver for RACF on your RACF systems.
* *Authentication Redirection:*
  The Fan-Out driver provides authentication redirection using the password exit. The Identity Manager 4.8 driver for RACF provides bidirectional password synchronization.

## 4.1.1 Preparing for Migration

NetIQ® recommends that you perform the upgrade in a test environment similar to your production environment before upgrading production systems.

Before beginning the upgrade process, review [Section 3.0, Installing the RACF Driver](b3r8si5.html).

To prepare for installing the upgrade:

1. Verify that you have the required knowledge and skills.

   For details, see [Required Knowledge and Skills](b3xdcg2.html).
2. Ensure that the prerequisites are met.

   For details, see [Prerequisites](b3xccfu.html).
3. Prepare the distribution files for installation.

   For details, see [Getting the Installation Files](b3xd1sq.html).

## 4.1.2 Migrating Fan-Out Driver Platform Services to the RACF Driver

To migrate, follow these tasks on your target platform system:

1. Stop the following started tasks:

   * PLATRCVR
   * ASCLIENT
2. Remove ASCLIENT and PLATRCVR from your system startup and shutdown procedures.
3. Remove the Fan-Out driver’s RACF exit.
4. Install the driver shim on the connected system.

   For details, see [Installing the Driver Shim on the Connected System](b3xehpq.html).

## 4.1.3 Configuring the Driver

To configure the driver:

1. Install and set up the Identity Manager driver for RACF on the Metadirectory server.

   For details, see [Creating the Driver in Designer](b1bybgrg.html).
2. Make any required policy modifications.

   Create or modify an appropriate policy to use the alternative naming attribute if one was used by the Fan-Out driver. For more information about policy customization, see the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
3. Start the driver.

   Click the upper right corner of the driver icon, then click Start driver.
4. Migrate the users to make new associations. For details, see [Migrating Identities from the Identity Vault to the Connected System](b3xxotz.html#b3xxpl3) and [Migrating Identities from the Connected System to the Identity Vault](b3xxotz.html#b3xxw83).

## 4.1.4 Post-Migration Tasks

Perform the tasks listed in [Post-Installation Tasks](b3xfpxf.html).

After the new driver is operating properly, you can remove the Fan-Out driver components:

1. Delete the Platform object from the Fan-Out driver configuration.
2. On the connected system, uninstall Platform Services.
3. If this is the last platform being served by the Fan-Out driver, you can uninstall the Fan-Out core driver.

   1. Remove the ASAM directory from the file system.
   2. Remove the ASAM System container object and all of its subordinates from the tree.
   3. Uninstall the Fan-Out driver plug-ins.
