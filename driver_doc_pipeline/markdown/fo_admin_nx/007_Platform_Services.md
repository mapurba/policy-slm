# 2.2 Platform Services

Platform Services enables a system to utilize the Core Driver functions. A platform can use Authentication Services for some or all users, and can use Identity Provisioning in maintaining some or all local user accounts and groups. For a complete account redirection solution, a platform can use the Name Service Switch and Platform Services Cache Daemon for some or all users.

Some types of platforms communicate with Authentication Services using SSL, and others use DES encryption. All platform communication with Event Journal Services uses SSL.

A platform that uses SSL-based communication must have a valid certificate to communicate with the Core Driver for most functions. A platform that uses DES encryption must use the same DES key as defined for it in the Core Driver configuration.

The Identity Manager Fan-Out Driver does not support authentication or password changes for eDirectory users who have a null password.

*Figure 2-3* Platform Services

![](../graphics/platserv_a.gif)

## 2.2.1 User and Group Management

Management of users and groups on the platform is carried out by Receiver scripts, which are called by the Platform Receiver based on provisioning events obtained from the Core Driver.

### Platform Receiver

The Platform Receiver connects to the Event Journal Services component of the Core Driver, requests provisioning events, and runs a script to carry out the appropriate platform-specific processing for the given type of event. The Platform Receiver provides failover support for connections to Event Journal Services if more than one Core Driver is available.

### Receiver Scripts

Receiver scripts are run by the Platform Receiver to process provisioning events.

The Identity Manager Fan-Out Driver provides a set of fully functional base scripts in the customary scripting language for each supported platform. You can extend these base scripts as appropriate for your needs.

The Receiver script functions are

* Add User
* Modify User
* Delete User
* Delete User Pending
* Enable User
* Disable User
* Rename User
* Add User to Group
* Remove User from Group
* Add Group
* Modify Group
* Delete Group
* Delete Group Pending
* Rename Group

## 2.2.2 User Authentication

Authentication redirection is handled by the Platform Services Process, which is called by the System Intercept. The Platform Services Process is also called by applications using the AS Client API.

Platforms that use password replication receive notification of password changes in eDirectory through the Platform Receiver and send notification of local password changes detected by the password change intercept to the Core Driver using the Platform Services Process.

Account redirection is handled by the Platform Services Cache Daemon, which is called by the Name Service Switch. Platforms that are configured for account redirection use a local memory cache pool for account records and retrieve all account and password information from this cache.

### Platform Services Process

The Platform Services Process establishes and maintains connections to Core Drivers for Authentication Services, and provides load balancing and failover among them. These connections are used to provide Authentication Services to the platform.

### Platform Services Cache Daemon

The Platform Services Cache Daemon establishes and maintains a connection to a Core Driver and receives event data from Event Journal Services. This data is stored away in memory cache and used to supply account information to the Name Service Switch.

### AS Client API

The AS Client API provides a programming interface to Authentication Services. It is furnished as routines that can be called from C and Java\*. The AS Client API induces functions to

* Validate a user ID/password combination
* Change a user's password, given the current password
* Perform an administrative password reset
* Obtain the fully distinguished name for a user ID
* Determine if a user has Security Equal To a given object
* Determine if an object has the specified effective rights to the specified attribute of a given object
* Obtain a list of members of a group
* Obtain a list of security equivalences for a user
* Obtain the eDirectory Home Directory attribute value for a user
* Determine if a given user is in the Authentication Services Include/Exclude list

For details about using the AS Client API, see [Section V, API Development](bexh68d.html).

### System Intercept

The System Intercept is called by the native security system for password verification and password change. Because passwords are checked using eDirectory or, on supported platforms, replicated from eDirectory, a user has the same password throughout the enterprise, regardless of the platform used.

System Intercepts are implemented using standard, vendor-provided mechanisms.

### Authentication Services Methods

There are two methods for providing users with the same password across the platforms in your enterprise.

*Password Redirection:*
Requests to check passwords are intercepted at the platform and redirected to objects in eDirectory. The end result is that the user has the same password on all systems.

*Password Replication:*
Changes to passwords are intercepted and replicated between eDirectory and participating platforms. As with password redirection, the end result is that the user has the same password on all systems.

#### Password Redirection

Platforms that use password redirection employ a System Intercept to gain control when a password is to be verified. The System Intercept passes the request to Authentication Services, through the Platform Services Process. Authentication Services uses the Census to identify the User or Alias object in eDirectory that corresponds to the request. Then Authentication Services verifies the password using that object and returns the result to the platform.

The System Intercepts for z/OS\* and UNIX systems store the password in the local security system upon a successful authentication or password change. For logins, if Authentication Services cannot be reached, the user's password is verified using the local security system.

#### Password Replication

Platforms that use password replication receive notification of password changes through the Platform Receiver.

The Core Driver is notified of changes to passwords as follows:

* By ensuring that your eDirectory is configured to fully support Universal Password, the driver is notified of password changes in eDirectory.

* The Password Validation Program Exit is installed on an IBM i (i5/OS and OS/400) system and captures password change information.

When Authentication Services receives notification of a password change, it verifies the authenticity of the notification and then stores the encrypted password. This is detected by the Event Subsystem, which generates the appropriate provisioning event to notify those platforms that are authorized to receive password information.

By default, passwords are converted to lowercase before they are sent to a platform.

*Account Redirection:*
Requests for Posix user and group information are intercepted at the platform Name Service Switch and redirected to objects in eDirectory. This information includes loginName, uidNumber, gidNumber, gecos, homeDirectory, loginShell, groupName, memberUid and passwords.

## 2.2.3 Platform Configuration File

You use the platform configuration file to specify Platform Services configuration information, such as

* Which users are authenticated using Authentication Services and which users are authenticated using the local security system
* Which user accounts and groups are managed using Identity Provisioning and which are managed locally
* Information used to locate the Core Driver servers.
