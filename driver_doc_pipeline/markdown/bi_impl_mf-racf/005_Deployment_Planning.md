# 2.1 Deployment Planning

* Review [Section 3.0, Installing the RACF Driver](b3r8si5.html) and [Section 5.0, Configuring the RACF Driver](b3r8t50.html).
* Is this a new installation or an upgrade?

  + If you are installing the RACF driver on a system for the first time, use [Section 3.0, Installing the RACF Driver](b3r8si5.html), as your main procedural reference.
  + If you are upgrading a system that already uses an RACF driver, begin with [Section 4.0, Upgrading the Driver](b3r9hzv.html), which includes instructions for upgrading from both the Fan-Out RACF driver and the Java-based bidirectional RACF driver.
* Consider where and how you will install each component.

  + You must install the driver libraries (samples library, load library, and REXX exec library) on a volume that is shared by each system that shares the security system database.
  + You must run the driver shim started task on only one system that shares the security system database.
  + You must create the change log data set on a volume that is shared by all systems that share the security system database.
  + You must run the change log started task on each system that shares the security system database.
  + You must install the exit routines on each system that shares the security system database.
* Consider how you will respond to the installation prompts and other installation decisions.
* You must provide a connected system schema file during installation. A file with the required classes and attributes is provided in the driver samples library member SCHEMDEF.

  For details about the connected system schema file, see [The Connected System Schema File](b3xxapt.html).
* You must provide a driver shim configuration file during installation. A file that you can customize is provided in the driver samples library member DRVCONF.

  For details about the driver shim configuration file, see [The Driver Shim Configuration File](b4baik6.html).
* You must provide an include/exclude file during installation. A file with basic suggested content is provided in the driver samples library member INCEXC.

  You can use the include/exclude file on the connected system to limit your initial deployment to a small number of users and groups.

  For details about the include/exclude file, see [The Connected System Include/Exclude File](b3xxit1.html).
* How will you prototype, test, and roll out your deployment?
* What are the host names or IP addresses of your Metadirectory server and the system that will run the driver shim started task?
* Will you use the default TCP port numbers?

  *Table 2-1* Default TCP Port Numbers

  | Purpose | TCP Port Number |
  | Driver shim connection to the Metadirectory engine | 8090 |
  | Driver shim HTTP services for log viewing | 8091 |
  | Secure LDAP port | 636 |
  | Non-secure LDAP port | 389 |
