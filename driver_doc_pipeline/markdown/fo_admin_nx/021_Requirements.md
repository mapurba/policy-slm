# 4.3 Requirements

The system requirements for driver components are described in the following sections. Identity Manager Fan-Out Driver components do not require the systems they run on to be dedicated solely to them.

Topics in this section include

* [User Rights Requirements](babffihg.html#br3ne7i)
* [Password Replication Requirements](babffihg.html#babdaedd)
* [Core Driver Requirements](babffihg.html#br3ne7j)
* [Requirements for Workstations Used for Installation and Administration](babffihg.html#babjhige)
* [Platform Services Requirements](babffihg.html#br3ne7k)

## 4.3.1 User Rights Requirements

The installation and configuration of the driver requires a user with full administrative rights and privileges in eDirectory and on the target systems. You can grant more limited rights to other users to use the Fan-Out Driver Web interface for administrative functions. For details of rights needed for administrative functions, see [Rights Required for Web Application Use](chdijbdi.html#bfnnjh3).

## 4.3.2 Password Replication Requirements

If you use password replication, you must ensure that the driver is notified of changes to passwords.

* If your eDirectory is configured to fully support Universal Password, the driver is notified of password changes in eDirectory.
* When configuring the policy for Universal Password, be sure to select the option that allows administrative users to retrieve the Universal Password.

For information about installing and configuring the password intercepts, see [Section IV, Platform Services Administration](bexh69n.html).

## 4.3.3 Core Driver Requirements

* NetIQ Identity Manager.
* NetIQ eDirectory versions supported by the Identity Manager version in use.
* NetIQ iManager versions supported by Identity Manager version in use.
* One of the following OS platforms, in a version supported by the Identity Manager and eDirectory version in use:

  + Windows
  + Linux
* TCP/IP network connectivity.
* A writable replica of the partition that will hold the ASAM System container must reside on the LDAP host server used by the Core Driver.
* Replicas (full or filtered) of objects that will be covered by a Census Search object (primary Core Driver only).

  The Fan-Out Driver will be configured for the attributes in the following lists. If you use filtered replicas, include the attributes shown in the following lists. If you add other attributes to the Subscriber filter, you must ensure that they are also available in your filtered replicas.

  Alias Attributes

  + Aliased Object Name
  + CN
  + GUID

  User Attributes

  + CN
  + Group Membership
  + GUID
  + Login Disabled
  + Surname

  ASAM-enterpriseUser Attributes

  + ASAM-addTime
  + GUID

  Group Attributes

  + CN
  + GUID
  + Member

  Organizational Role Attributes

  + CN
  + GUID
  + Role Occupant

*HINT:*iManager provides a wizard for setting up filtered replicas.

## 4.3.4 Requirements for Workstations Used for Installation and Administration

The workstations used to install, configure, and administer the driver must meet the following requirements.

* TCP/IP network connectivity
* The ability to run iManager
* Connectivity to the Identity Vault (eDirectory) tree to be managed by the driver
* If the installation computer runs UNIX, gzip and tar utilities
* Connectivity to the file system of the computer that is to receive components being installed; if the installation computer is not the same as the target host, a drive must be mapped to the target host

## 4.3.5 Platform Services Requirements

For information about required systems and software, as well as supported platforms and operating environments, see the [Identity Manager 4.8 Drivers Documentation Web site](https://www.netiq.com/documentation/identity-manager-48-drivers). From this index page, you can select a Readme file associated with the platform(s) for which you need Fan-Out Driver support.
