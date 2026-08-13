# 4.1 Upgrading from the Fan-Out Driver

The Identity Manager Fan-Out driver provides one-way synchronization to a heterogeneous mix of systems including Linux and UNIX systems, and IBM\* i5/OS\* and z/OS\* systems. The Fan-Out driver also provides authentication redirection from those systems.

Moving to the Linux and UNIX driver provides two main advantages.

* *Bidirectional Synchronization:*
  The Linux and UNIX driver allows synchronization from the connected Linux or UNIX system.
* *Standard Identity Manager Policies That Simplify Customization:*
  The Fan-Out driver makes minimal use of Identity Manager policies.

Consider the following before migrating from the Fan-Out driver to the Linux and UNIX driver.

* *Heterogeneity:*
  The Fan-Out driver supports operating systems in addition to Linux and UNIX. You can continue to use the Fan-Out driver for those systems while using the Linux and UNIX driver for Linux and UNIX systems.
* *Scalability:*
  The Fan-Out driver can fan out identities to any number of systems. The Linux and UNIX driver can replicate to only one system. (Although that system might provide account management for many computers using NIS or NIS+.)

  One Linux and UNIX driver is required for each connected system. For best performance, we recommend no more than a total of 60 drivers.
* *Authentication Redirection:*
  The Fan-Out driver provides authentication redirection from Linux and UNIX using PAM or LAM. The Linux and UNIX driver provides only bidirectional password synchronization.

## 4.1.1 Preparing for Migration

If necessary, migrate the UID and GID numbers from the appropriate Fan-Out driver Platform Set. You can assign RFC 2307 attributes, such as homeDirectory and loginShell, to objects in the Identity Vault.

To use the Linux and UNIX Settings driver to accomplish this:

1. Install the Linux and UNIX Settings driver on each connected Linux or UNIX system.
2. Set the properties of the Linux and UNIX Settings driver to correspond to the UID/GID ranges that were specified in the Fan-Out driver.
3. Configure the Linux and UNIX Settings driver to populate the desired RFC 2307 attributes.

For details about installing and configuring the Linux and UNIX Settings driver, see the Linux and UNIX Settings Driver Implementation Guide on the [Identity Manager 4.8 Drivers Documentation Web site](https://www.netiq.com/documentation/identity-manager-47-drivers).

## 4.1.2 Migrating Fan-Out Driver Platform Services to the Linux and UNIX Driver

Perform the following steps on your target platform system:

1. Stop the following processes:

   * asamrcvr
   * asampsp
2. Remove the Platform Services startup scripts from /etc/init.d.
3. Install the driver shim on the connected system.

   For details, see [Installing the Driver Shim on the Connected System](b3xehpq.html).
4. Install the Linux and UNIX driver PAM or LAM module.

   For details, see [Installing the PAM or LAM Module](b3xfnmq.html).

## 4.1.3 Configuring the Driver

1. Install and set up the Linux and UNIX driver on the Metadirectory server.

   For details, see [Creating the Driver in Designer](b1bybgrg.html).
2. Make any required policy modifications.

   Create or modify an appropriate policy to use the alternative naming attribute if one was used by the Fan-Out driver. For more information about policy customization, see the policy documentation on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
3. Start the Linux and UNIX driver.

   Click the upper right corner of the driver icon, then click Start driver.
4. Migrate the users to make new associations. For details, see [Migrating Identities from the Identity Vault to the Connected System](b3xxotz.html#b3xxpl3) and [Migrating Identities from the Connected System to the Identity Vault](b3xxotz.html#b3xxw83).

## 4.1.4 Post-Migration Tasks

Perform the steps listed in [Post-Installation Tasks](b3xfpxf.html).

After the new driver is operating properly, you can remove the Fan-Out driver components.

1. Delete the Platform object from the Fan-Out driver configuration.
2. On the connected system, uninstall Platform Services by removing all startup scripts and deleting the /usr/local/ASAM directory.
3. If this is the last platform being served by the Fan-Out driver, you can uninstall the Fan-Out core driver:

   1. Remove the ASAM directory from the file system.
   2. Remove the ASAM System container object and all of its subordinates from the tree.
   3. Uninstall the Fan-Out driver plug-ins.
