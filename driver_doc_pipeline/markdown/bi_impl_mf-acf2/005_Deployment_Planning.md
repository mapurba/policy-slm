# 2.1 Deployment Planning

* Review [Section 3.0, Installing the ACF2 Driver](b3r8si5.html) and [Section 5.0, Configuring the ACF2 Driver](b3r8t50.html).
* Is this a new installation or an upgrade?

  + If you are installing the ACF2 driver on a system for the first time, use [Section 3.0, Installing the ACF2 Driver](b3r8si5.html), as your main procedural reference.
  + If you are upgrading a system that already uses an ACF2 driver, begin with [Section 4.0, Upgrading from the Fan-Out Driver](b3r9hzv.html), which includes instructions for upgrading from both the Fan-Out ACF2 driver.
* Consider where and how you will install each component.

  The driver shim libraries (SAMPLIB, IDMLOAD, ACF2EXEC) must be installed on a volume that is shared by each system that shares the security system database.
* If you will use the Publisher channel to track changes made in ACF2, you will need to:

  + Run the driver shim started task on only one system that shares the ACF2 security system database.
  + Create the change log data set on a volume that is shared by all systems that share the security system database.
  + Install the Exit routines on each system that shares the security system database.
  + Schedule an IPL for the Exit installations.
* How will you stage, test and roll out your deployment of the ACF2 driver?
* What are the host names or IP addresses of your Metadirectory server and the ACF2 system that will run the driver shim started task?
* Will you use the default TCP port numbers (see [Table 2-1](b4evgzg.html#b4kgv9q)) and are they accessible through your network infrastructure?

  *Table 2-1* Default TCP Port Numbers

  | Purpose | TCP Port Number |
  | Driver shim connection to the Metadirectory engine | 8090 |
  | Driver shim HTTP services for log viewing | 8091 |
  | Secure LDAP port | 636 |
  | Non-secure LDAP port | 389 |
