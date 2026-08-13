# 4.1 Configuration Planning

There are a number of issues to resolve in planning for your deployment of the Identity Manager Fan-Out Driver. Considering these issues now will make your installation go more smoothly.

* Decide how you will deploy the use of the driver throughout your enterprise.

  Do you want to start with a small subset of your platform systems? Do you want to start with a small subset of your user community?

  Platforms can operate with Include/Exclude lists to control which users the driver handles for authentication, and which users the driver defers to the native authentication mechanism. Platforms can also operate with Include/Exclude lists to control which user accounts the driver manages using provisioning events and which user accounts are managed locally. For more information, see [Section III, Platform Services Planning](bexh6ay.html).
* Decide who will administer your driver configuration.

  The Web interface is used to monitor and administer the driver. Make it available to these persons and ensure that they have the necessary rights to use it. For details about the rights needed for administrative functions, see [Rights Required for Web Application Use](chdijbdi.html#bfnnjh3)
* Decide which eDirectory™servers in your network will run Core Drivers.

  A writable replica of the partition holding the ASAM System container must reside on the LDAP host server used by a Core Driver.

  Each object that is covered by a Census Search object must be present in a replica (full or filtered) on the system that hosts the primary Core Driver.
* Will you install additional Core Drivers to provide redundancy for Authentication Services?

  The Platform Services Process includes load balancing and failover support to provide for continued processing should a Core Driver become unavailable.
* Will you install additional Core Drivers to provide redundancy for Identity Provisioning?

  The Platform Receiver includes failover support to provide for continued processing if the Core Driver it normally uses for Identity Provisioning becomes unavailable.
* Decide where in your eDirectory tree the ASAM System container and ASAM Master User objects should go. Creating a special container for them is a good practice.

  Make sure you set password policies appropriate for the ASAM Master User object.

  For more information about requirements for the ASAM Master User, see [ASAM Master User Security](chdfddgg.html#br3n4sp).
* Decide upon your Census parameters.

  Which objects in your eDirectory tree will be used as the source of Enterprise Users and Enterprise Groups? This depends on how you place User and Group objects in your directory.

  When do you want to run a Census Trawl? Because the Census is maintained in real time using provisioning events, Trawls are used primarily to verify the consistency of the Census. Once a day is reasonable for most cases.

  Do you want Enterprise Users whose User objects have been deleted from eDirectory to be automatically removed from the Census? They can be removed after remaining inactive for a specified number of days, or you can choose to manage inactive users manually.

  Do you want to delay user password expiration until the end of the day of expiration? This can result in smoother operation for users on platforms with third-party systems that cache and reuse passwords during the day.

  Do you want to immediately delete users and groups from platforms when they are deleted from eDirectory or are no longer covered by a Search object, or do you want to provide a grace period to recover from accidental changes?

  For information about setting these parameters, see [Configuring the Census](br3n4tb.html#chdfigcf).
* How will you resolve naming exceptions?

  For more information, see [Reviewing Naming Exceptions](br3n4tb.html#brzmejc).
* Decide which systems in your network will run Platform Services.

  User names, passwords, and group names must conform to the character set and length restrictions imposed by the platform operating system in order to participate in Authentication Services and Identity Provisioning on that platform. Determine how you will handle those that do not meet the restrictions.
* Decide how you will organize your Platform Sets. Each platform belongs to exactly one Platform Set. A Platform Set provides the relationship between a group of platforms and the Search objects that define their user and group population.
* Users and Groups have the same UID number and GID number on each Linux/UNIX platform in a Platform Set.

  What UID and GID numbers do you want to reserve for local administrator use on Linux/UNIX platforms?

  Will you use the RFC2307 posixAccount and posixGroup auxiliary object classes for enterprise-wide UID and GID assignments?
* Will any of your platforms use password replication? If so, you must ensure that the driver is notified of changes to passwords.

  If your eDirectory is configured to fully support Universal Password, the driver is notified of password changes in eDirectory.

  If you do not use Universal Password, you must install and configure the appropriate password intercepts.

  For more information, see [Password Replication Requirements](babffihg.html#babdaedd).
* Platforms configured to use password replication do not normally receive provisioning events for user accounts until the passwords for these accounts are known to the driver.

  The driver uses Universal Password to collect password information. Users must either change their passwords where these are installed and configured, or authenticate on a driver platform before they can be populated onto a platform that uses password replication (Permit Password Replication specified as Yes for the Platform object in the Web interface).

  By planning a staged deployment of the Fan-Out Driver to the platforms in your enterprise so that most users have authenticated using other platforms first, you ensure the availability of these users to password replication platforms when you are ready to deploy the driver on them.
* Consider how your own applications could benefit from the use of the Authentication Services (AS) Client API.

  Using the AS Client API is simple and straightforward. For more information about using the Client API, see [Section V, API Development](bexh68d.html).
* Will any of your Platform Receiver scripts need attributes other than those configured in the driver by default?

  For a list of the attributes configured by default, see [Core Driver Requirements](babffihg.html#br3ne7j).

  To configure additional attributes, you must add them to the Event Subsystem Subscriber filter. For details about adding attributes to the Subscriber filter, see the Identity Manager Administration Guide.

  The attribute names that you use in the Subscriber filter must be the eDirectory names.
