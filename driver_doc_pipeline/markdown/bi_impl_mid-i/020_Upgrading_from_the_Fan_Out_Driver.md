# 4.0 Upgrading from the Fan-Out Driver

This section provides the information you need if you are upgrading from the Identity Manager Fan-Out driver to the Identity Manager 4.8 driver for IBM i (i5/OS and OS/400).

Topics include

* [Migrating Fan-Out Driver Platform Services to the IBM i Driver](b3xgi3w.html)
* [Configuring the Driver](b3xgjcz.html)
* [Post-Migration Tasks](b3xgm2l.html)

We recommend that you perform the upgrade in a test environment similar to your production environment before upgrading production systems.

Before beginning the upgrade process, review [Section 3.0, Installing the IBM i Driver](b3r8si5.html).

To prepare for installing the upgrade:

1. Verify that you have the required knowledge and skills.

   For details, see [Required Knowledge and Skills](b3xdcg2.html).
2. Ensure that the prerequisites are met.

   For details, see [Prerequisites](b3xccfu.html).
3. Prepare the distribution files for installation.

   For details, see [Getting the Installation Files](b3xd1sq.html).

The Fan-Out driver provides one-way synchronization to a heterogeneous mix of systems including Linux and UNIX systems, and IBM i and z/OS\* systems. The Fan-Out driver also provides authentication redirection from those systems.

Moving to the IBM i driver provides two main advantages.

* *Bidirectional Synchronization:*
  The IBM i driver allows synchronization from the connected IBM i system.
* *Standard Identity Manager Policies That Simplify Customization:*
  The Fan-Out driver makes minimal use of Identity Manager policies.

Consider the following before migrating from the Fan-Out driver to the IBM i driver.

* *Heterogeneity:*
  The Fan-Out driver supports operating systems in addition to IBM i. You can continue to use the Fan-Out driver for those systems while using the IBM i driver for IBM i systems.
* *Scalability:*
  The Fan-Out driver can fan out identities to any number of systems. The IBM i driver can replicate to only one system.

  One IBM i driver is required for each connected system. For best performance, we recommend no more than a total of 60 drivers.
* *Authentication Redirection:*
  The Fan-Out driver uses authentication redirection from IBM i using the Change Password Validation Program exit. The IBM i driver uses bidirectional password synchronization.
