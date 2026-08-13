# 4.0 Upgrading from the Fan-Out Driver

This section provides the information you need if you are upgrading from the Identity Manager Fan-Out driver to the Identity Manager 4.8 driver for CA Top Secret.

Topics include

* [Preparing for Migration](b3xgfhc.html)
* [Migrating Fan-Out Driver Platform Services to the Top Secret Driver](b3xgi3w.html)
* [Configuring the Driver](b3xgjcz.html)
* [Post-Migration Tasks](b3xgm2l.html)

The Fan-Out driver provides one-way synchronization to a heterogeneous mix of systems including Linux and UNIX systems, and IBM i5/OS\* (OS/400\* operating system) and z/OS systems. The Fan-Out driver also provides authentication redirection from those systems.

Moving to the Identity Manager 4.8 driver for CA Top Secret provides two main advantages.

* *Bidirectional Synchronization:*
  The driver allows synchronization from the connected system.
* *Standard Identity Manager Policies That Simplify Customization:*
  The Fan-Out driver makes minimal use of Identity Manager policies.

Consider the following before migrating from the Fan-Out driver.

* *Heterogeneity:*
  The Fan-Out driver supports operating system environments besides Top Secret. You can continue to use the Fan-Out driver for those systems while using the Identity Manager 4.8 driver for CA Top Secret on your Top Secret systems.
* *Authentication Redirection:*
  The Fan-Out driver provides authentication redirection using the password exit. The Identity Manager 4.8 driver for CA Top Secret provides bidirectional password synchronization.
