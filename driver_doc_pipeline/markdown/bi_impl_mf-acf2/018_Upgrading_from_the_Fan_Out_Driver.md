# 4.0 Upgrading from the Fan-Out Driver

This section provides information about upgrading the latest Identity Manager driver for ACF2 from the Identity Manager Fan-Out Driver for ACF2.

*NOTE:*At the time of this document’s initial release, the Fan-Out Driver was commonly leveraged to provide an identity solution for ACF2.

Topics include

* [Preparing for Migration](bmn9qf0.html)
* [Migrating Fan-Out Driver Platform Services to the ACF2 Driver](bmn9r3i.html)
* [Configuring the Driver](bmn9rcd.html)
* [Post-Migration Tasks](bmn9rku.html)

The Fan-Out driver provides one-way synchronization to a heterogeneous mix of systems including Linux and UNIX systems, and IBM i5/OS\* (OS/400\* operating system) and z/OS systems. The Fan-Out driver also provides authentication redirection from those systems.

Moving to the Identity Manager 4.8 driver for ACF2 provides a few advantages:

* *Bidirectional Synchronization:*
  The new driver architecture allows you to synchronize every field from the Logonid record of the connected ACF2 system.
* *Identity Manager Policies and Packages:*
  The Fan-Out driver makes minimal use of the Identity Manager policies.
* *Password Phrases:*
  The new driver supports ACF2 password phrases.

Consider the following before migrating from the Fan-Out driver:

* *Heterogeneity:*
  The Fan-Out driver supports operating system environments besides ACF2. You can continue to use the Fan-Out driver for those systems while using the Identity Manager 4.8 driver for ACF2 on your ACF2 systems.
* *Authentication Redirection:*
  The Fan-Out driver provides authentication redirection using the password exit. The Identity Manager 4.8 driver for ACF2 provides bidirectional password synchronization.
