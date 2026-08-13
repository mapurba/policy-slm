# 6.5 Management Tasks

This section describes tasks you can complete in iManager, using the Fan-Out Driver Web Interface plug-in, to manage the Driver:

* [Configuring the Census](br3n4tb.html#chdfigcf)
* [Configuring Core Drivers](br3n4tb.html#chdbejce)
* [Configuring the iManager Plug-In](br3n4tb.html#brzmsp3)
* [Configuring Logs](br3n4tb.html#brzmzia)
* [Configuring Platform Sets](br3n4tb.html#chddcggj)
* [Configuring Platforms](br3n4tb.html#bfijtk0)
* [Configuring Provisioning](br3n4tb.html#brznubl)
* [Configuring Search Objects](br3n4tb.html#chdebihg)
* [Configuring Linux/UNIX UID/GID Sets](br3n4tb.html#chdjdaff)
* [Displaying Component Status](br3n4tb.html#chddecge)
* [Viewing Driver Documentation](br3n4tb.html#bs01xrw)
* [Viewing Logs](br3n4tb.html#chdgdcbb)
* [Displaying Provisioning Details](br3n4tb.html#chdchcfa)
* [Reviewing Naming Exceptions](br3n4tb.html#brzmejc)
* [Reviewing Platform Errors](br3n4tb.html#br3n4x9)
* [Managing Trawls](br3n4tb.html#bs029sv)

## 6.5.1 Configuring the Census

Configuring the Census includes the following tasks:

* [Specifying Search Objects](br3n4tb.html#chdcheab)
* [Specifying Trawl Times](br3n4tb.html#chdjgegg)
* [Specifying Automatic Removal of Inactive Users and Groups](br3n4tb.html#br3n4y4)
* [Delaying Password Expiration Until Midnight](br3n4tb.html#br3n4y7)
* [Specifying a Platform Object Delete Pending Duration](br3n4tb.html#br3n4ya)

*NOTE:*Core Driver installation adds additional indexes for attributes of the objects added to the Identity Vault. Depending on the size of the existing directory tree, these indexes can take some time to bring online. Before you begin your first Trawl, verify that the indexes are in the online state as detailed in [Core Driver Indexes](blxyqwd.html).

### Specifying Search Objects

Search objects specify how users and groups are selected from eDirectory to be included in the Census. For details about Search objects, see [Configuring Search Objects](br3n4tb.html#chdebihg).

To update the Census after you make Search object changes, start a Trawl. For details about starting a Trawl, see [Starting a Census Trawl](br3n4tb.html#chdgcgid).

To add a new Census Search object:

1. Click Fan-Out Driver Configuration > Configure Census. The Census Configuration page is displayed.
2. Click Search Objects > Add. The Add a Search Object page is displayed.
3. Specify the Search object distinguished name and attributes as desired, then click Apply.

   For details about Search object attributes, see [Search Object Attributes](br3n4tb.html#chdfhdeb).

To change a Census Search object:

1. Click Fan-Out Driver Configuration > Configure Census. The Census Configuration page is displayed.
2. In the list of Search objects, click the name of the Search object to modify. The Modify Search Object page is displayed.
3. Update the attributes of the Search object as desired, then click Apply.

   For details about Search object attributes, see [Search Object Attributes](br3n4tb.html#chdfhdeb).

To remove a Census Search object:

1. Click Fan-Out Driver Configuration > Configure Census. The Census Configuration page is displayed.
2. In the list of Search objects, click the name of the Search object to be deleted. The Modify Search Object page is displayed.
3. In the list of Platform Sets under Platform Set Associations, click each Remove button. The Remove Search Object confirmation page is displayed each time you click a Remove button. Click Yes for each.
4. Under the In Census heading, click the Remove button. The Remove Search Object confirmation page is displayed. Click Yes.

### Specifying Trawl Times

Object Services is notified by the Event Subsystem of events in eDirectory that affect the Census. Objects Services also periodically verifies the consistency of the Census by examining objects in the directory in a procedure known as a Trawl. Use the Web interface to specify the times when a Trawl runs.

1. Click Fan-Out Driver Configuration > Configure Census. The Census Configuration page is displayed.
2. Trawl times are listed (24-hour clock) under Trawl Time Configuration. If no times are listed, Object Services does not automatically start any Trawls.

   Time of day values used by the driver are specified in Universal Time, formerly known as GMT, and commonly abbreviated as Z.

   To add a new Trawl time, click Add.

   To remove a Trawl time from the list, click its Remove button.

### Specifying Automatic Removal of Inactive Users and Groups

You can choose to have Enterprise Users and Enterprise Groups whose corresponding User object or Group object is deleted from eDirectory or no longer covered by a Census Search object remain in the Census in an inactive state. This prevents another person from receiving access to resources as an unintended result of the reuse of a user name. Inactive users cannot authenticate through Authentication Services.

You can also specify that inactive users and groups be removed from the Census automatically during a Trawl after they have reached a given number of inactive days.

To specify inactive user and group options:

1. Click Fan-Out Driver Configuration > Configure Census. The Census Configuration page is displayed.
2. Inactive user and group options are listed on the Census Configuration page under Inactive Enterprise User and Group Actions. Specify the action you want, then click Apply.

To view inactive users and groups, use the Provisioning Details utility and specify Search Type > Inactive Users and Groups. For more information about using the Provisioning Details utility, see [Displaying Provisioning Details](br3n4tb.html#chdchcfa).

### Delaying Password Expiration Until Midnight

You can choose to delay the expiration of user passwords by Authentication Services from the exact date and time set for them in eDirectory until the end of the day (local time of the Core Driver host server) on which they expire. This can result in smoother operation for users on platforms with third-party systems that cache and reuse passwords during the day.

To specify password expiration options:

1. Click Fan-Out Driver Configuration > Configure Census. The Census Configuration page is displayed.
2. Password expiration options are listed on the Census Configuration page under Delay User Password Expiration. Select the option you prefer, then click Apply.

### Specifying a Platform Object Delete Pending Duration

You can use the Web interface to specify a Delete Pending Duration. During this interval, User and Group objects associated with a platform that have either been deleted from eDirectory or are no longer covered by a Search object, are not deleted from their corresponding platforms. The results of a Delete User or Delete Group Receiver script can be difficult to reverse. This provides a grace period to allow recovery from a mistake affecting many users.

The User Delete Pending or Group Delete Pending script is called when a delete event becomes pending for a user or group, but the Delete User or Delete Group script is not called until the Delete Pending Duration expires.

To specify when users and groups are deleted from platforms:

1. Click Fan-Out Driver Configuration > Configure Census. The Census Configuration page is displayed.
2. Deletion options are listed under Platform Object Delete Pending Duration. Select the option you prefer, then click Apply.

## 6.5.2 Configuring Core Drivers

Core Drivers provide the Web interface, perform Census maintenance functions, and provide Authentication Services and Identity Provisioning to platforms.

### Starting a Core Driver

1. In iManager, select Identity Manager Management > Overview.
2. Locate the driver in its driver set.
3. Click the driver status indicator in the upper right corner of the driver icon, then click Start Driver.

### Stopping a Core Driver

1. In iManager, select Identity Manager Management > Overview.
2. Locate the driver in its driver set.
3. Click the driver status indicator in the upper right corner of the driver icon, then click Stop Driver.

### Driver Object Configuration Parameters

The Core Driver uses Driver object configuration parameters to identify the ASAM System container, the ASAM Master User object, an LDAP Services for eDirectory host server, and to obtain other related information. The Driver object is created during Core Driver installation.

To view and modify Driver object configuration parameters:

1. In iManager, select Identity Manager Management > Overview.
2. Locate the driver in its driver set.
3. Click the driver status indicator in the upper right corner of the driver icon, then click Edit Properties.
4. Click Identity Manager > Driver Configuration. Driver configuration parameters are located under the Driver Settings heading.
5. Update the settings as desired. Then click OK or Apply. To end without saving any changes, click Cancel.

#### Core Driver Config DN

Displays the name of this Driver object.

#### LDAP Host and Port

Specifies the IP address or DNS name and the TCP port of the LDAP Services for eDirectory host server that the Core Driver components use to access the ASAM System container. The LDAP host server must hold a writable replica of the ASAM System container.

The default is port 636 on the local host. For best performance, use the local host.

#### ASAM System Container

Specifies the fully distinguished name of the ASAM System container. The ASAM System container holds system configuration and operational objects.

#### Activation Group

Displays the Identity Manager integration modules that you have activated.

#### Publish Fan-Out Log Messages

Enables/disables redirection of Fan-Out messages into your own custom programs and status documents to free your administrators from manual Fan-Out log-tracking.

#### Locale

Specifies the two-character ISO 639 language identifier for the language to be used by the Core Driver. The default value of Locale is en (English)

#### Lower Password Case

Specifies whether Event Journal Services changes password case when sending password replication information to Platform Receivers.

Password replication information is provided to the Core Driver from many different sources. Maintaining password case can be undesirable because some sources of password information present passwords in uppercase.

By default, Event Journal Services converts passwords to lowercase before sending password replication events to Platform Receivers.

#### Migration Mode Password

Specifies the special password that is used with Password Migration on the z/OS operating system. Users with this password and with Login Disabled set are in the migration state. For more information about Password Migration, see the Identity Manager Fan-Out Driver for Mainframes Administration Guide.

#### Change Password Exit Library

Specifies the file path for the optional Password Change Validation Exit library. For information about the Password Change Validation Exit, see [Section A.0, Core Driver Technical Notes](babefbih.html).

#### Change Password Exit Function

Specifies the function name for the optional Password Change Validation Exit exported in the library identified by the Change Password Exit Library parameter. For information about the Password Change Validation Exit, see [Section A.0, Core Driver Technical Notes](babefbih.html).

#### Verify serial number of incoming platform connection

Enables/disables whether Core Driver checks the platform’s certificate serial number against the serial number listed in the Core Driver configuration. This is a useful security measure to detect and reject certificates that may have been compromised.

#### Network Connect Timeout

Specifies timeout in seconds for the Core Driver to use when opening a network connection to another network system.

#### Network Read Timeout

Specifies timeout in seconds for the Core Driver to use when reading data from a network connection. Higher timeout values can prevent premature disconnects.

#### Network Write Timeout

Specifies timeout in seconds for the Core Driver to use when writing data to a network connection. Higher timeout values can prevent premature disconnects.

#### Agent Resolve Strict

When the Core Driver’s Authentication Services resolves objects for platform authentication, this option allows Authentication Services to exclude objects that are not in the scope of the platform set.

When this option is set to false (default), Authentication Services will resolve requests against the entire Census. Setting this option to true is useful if you intend to delete users after a specified duration in the Census and must immediately revoke access to a remote platform system that has been configured for authentication redirection.

#### Agent Disable Last Contact

When Platform Services contact the Authentication Services for password checks, changes or other API calls, the Last Contact time is updated for that platform. Often, this can be excessive, causing performance issues for LDAP.

When this option is set to true, Authentication Services will not update the ASAM-lastContactTime attribute for the platform making the request.

#### Aggressive Delete Processing

When processing events for a platform, this option instructs Event Journal Services to send all appropriate Delete and Delete Pending events, regardless of the Platform Set Association state.

The Driver attempts to be judicial in sending out events, as to not send out events unnecessarily. However, in some circumstances, a platform may be in a state where it needs to re-process Delete or Delete Pending events, regardless of its association status. Set this option to true to enable this feature.

#### Resolve Groups using Platform Cache

When resolving Groups against Census Search Objects, caching is used to improve performance. In rare scenarios, where the Search Objects change very frequently, re-building the cache too often can also be a performance problem. Set this option to false to disable using cache in this scenario.

### Core Driver System Configuration Object Attributes

Descriptions for each attribute follow.

#### Network Address

The Core Driver configuration must list all of the network addresses of the Core Driver's host server. Network address information for the host server is entered when the Core Driver is installed. You must update this information if the host server network address is changed or if an additional network interface is installed in the server.

One network address is designated as the default. Identity Manager Fan-Out Driver Core Driver components use the default address to connect to each other.

The platform configuration file used by a Platform Services component specifies the network address of each Core Driver that is used by that component. If you change the network address of a Core Driver that is specified in a platform configuration file, you must update that platform configuration file. For details about the platform configuration file, see [Section III, Platform Services Planning](bexh6ay.html).

If you change the network address configuration of a Core Driver, a new certificate is automatically minted for the Core Driver.

*IMPORTANT:*You must restart the Core Driver for the new certificate to take effect.

#### Core Driver Port

The TCP port number used by the Core Driver defaults to 3451. You can change the Core Driver TCP port number if necessary.

If you change a Core Driver TCP port number, you must also make the corresponding changes to each platform configuration file that references the Core Driver.

#### Authentication Services z/OS and NDS-AS Compatibility Port

The TCP port number used by the Core Driver to communicate with Platform Services for z/OS and with NDS® Authentication Services (NDS-AS) version 3 Clients. The default is 2000.

#### Cache Size and Time to Live

Authentication Services maintains an encrypted cache of recent successful authentication requests to provide better performance for applications, such as Web servers, that make large bursts of requests to authenticate the same user in a short period of time.

You can specify the amount of memory that is allocated for this cache and the maximum length of time an entry is to be kept in the cache.

#### Primary Core Driver

One Core Driver is designated as the primary Core Driver. Other Core Drivers are known as secondary Core Drivers. The primary Core Driver serves the Web interface and provides environmental information during the installation process for other Core Drivers. Only the primary Core Driver listens for events from eDirectory and performs Trawls.

### Designating the Primary Core Driver

1. In the Web interface, click Fan-Out Driver Configuration > Configure Core Drivers. The Core Driver Configuration page is displayed.
2. Click Set as Primary.
3. Click Yes to confirm.
4. Restart the previous and new Core Drivers. For details about this procedure, see [Stopping a Core Driver](br3n4tb.html#br4s00s) and [Starting a Core Driver](br3n4tb.html#br4rzmy).
5. Configure the iManager plug-in to use the new primary Core Driver. For details, see [Configuring the iManager Plug-In](br3n4tb.html#brzmsp3).

Before changing which Core Driver is the primary Core Driver, ensure that the proposed new primary Core Driver holds replicas of all objects covered by Census Search objects.

### Adding a Core Driver

For step-by-step instructions to add a Core Driver, see [Section 5.0, Installing the Core Driver](bcgicacb.html).

### Changing the Core Driver Configuration

1. In the Web interface, click Fan-Out Driver Configuration > Configure Core Drivers. The Core Driver Configuration page is displayed.
2. Click the name of the Core Driver whose configuration you want to change. The Modify Core Driver page is displayed.
3. Specify attributes for the Core Driver as appropriate.

### Removing a Core Driver

1. Remove the Core Driver from the platform configuration file of all platforms where it is present. For information about the platform configuration file, see the [Section III, Platform Services Planning](bexh6ay.html).
2. Stop the Core Driver.

   For details, see [Stopping a Core Driver](br3n4tb.html#br4s00s).
3. Uninstall the Core Driver software and related files from the Core Driver host.

   * If the host server operating system is Linux/UNIX, delete the ASAM directory from the file system.
   * If the host server operating system is Windows, use Windows Control Panel > Add/Remove Programs.
4. Remove the Driver object from Identity Manager.

   1. In iManager, select Identity Manager Management > Overview.
   2. Locate the driver set for the driver, then click Delete Driver.
   3. Select the Core Driver from the list and confirm its deletion.
5. In the Web interface, click Fan-Out Driver Configuration > Configure Core Drivers. The Core Driver Configuration page is displayed.
6. Click the Remove button for the Core Driver to be removed. The Remove Core Driver confirmation page is displayed. Click Yes to confirm.

### Maintaining Logs Used by the Core Driver

Audit Services writes operational and audit log messages for the Core Driver to the asam\data\coredriver\logs directory.

You can use the Web interface to view logs and to configure how messages are managed. For information about viewing the logs, see [Viewing Logs](br3n4tb.html#chdgdcbb). For details about configuring the logs, see [Configuring Logs](br3n4tb.html#brzmzia).

## 6.5.3 Configuring the iManager Plug-In

Each administrative user must configure the iManager plug-in to use the primary Core Driver.

1. In the Web interface, click Fan-Out Driver Configuration > Configure iManager Plug-In. The Configure iManager Plug-In page is displayed.
2. Specify the DNS name or IP address of the primary Core Driver host server.
3. Specify the TCP port number for the primary Core Driver. The default is 3451.
4. Click Apply.

## 6.5.4 Configuring Logs

Audit Services maintains the Operational Log and Audit Log files written by the Core Driver. You can use the Web interface to manage log files. You can choose to have log messages kept for a given number of days, or you can choose to have log messages kept permanently. You can also specify the components whose messages are written to the logs.

1. Click Fan-Out Driver Configuration > Configure Logs. The Log Configuration page is displayed.
2. Select the option that you want for log retention.
3. Select the components whose messages you want included in the logs.
4. Click Apply.

You can use the Web interface to view log messages. For more information, see [Viewing Logs](br3n4tb.html#chdgdcbb).

The Log Configuration page is also used to configure debugging logging. For more information, see [Obtaining Debugging Output](brhj9dm.html).

## 6.5.5 Configuring Platform Sets

A Platform Set contains one or more Platform objects that share the same users and groups.

When you add a new Platform Set, you first need to give it a name and associate it with a UID/GID Set. If the Platform Set is for Linux or UNIX systems, you have the option of using Posix attributes instead of a UID/GID set.

You also may specify an Alternate Naming Attribute. When a user or group is provisioned to a Platform within this Platform Set, the Alternate Naming Attribute indicates the name that will be used. Then you add Search objects that describe what users and groups are provisioned to the platforms that belong to the Platform Set.

*IMPORTANT:*If you specify an Alternate Naming Attribute for a Platform Set, you must also include that attribute in the Subscriber filter.

After you have defined a Platform Set, you can create the Platform objects that represent its target platforms. For information about creating Platform objects, see [Configuring Platforms](br3n4tb.html#bfijtk0).

The Platform Set object's user and group population is described by one or more Search objects. For details about Search objects, see [Configuring Search Objects](br3n4tb.html#chdebihg).

### Platform Set Attributes

Descriptions for each attribute follow.

#### UID/GID Set Association

When you create a Platform Set, you specify a UID/GID Set that is used to assign UID numbers and GID numbers to Linux/UNIX platforms that are members of the Platform Set. You cannot change the UID/GID Set assigned to Platform Set after the Platform Set has been created.

Leave this option empty to use the posixAccount and posixGroup uidNumber and gidNumber attributes.

#### Alternate Naming Attribute

By default the name given to a user on each platform is the CN. By using the Alternate Naming Attribute, you also can indicate a name associated with each platform within the Platform Set. If you use this extra attribute in eDirectory, then each user or group must include a value for it.

*IMPORTANT:*If you specify an Alternate Naming Attribute for a Platform Set, you must also include that attribute in the Subscriber filter.

The content of an attribute that is designated as an Alternate Naming Attribute should be either a single value or multiple values of the form <platformset>:<name>.

The actual entry you make on the Modify Platform Set window should reflect the attribute name used by LDAP. You can find this information under the LDAP group object for the server, which includes the mapping between eDirectory and LDAP attribute names.

#### Search Objects

Search Objects designate the users and groups from the Census that are used to populate the platforms that are members of the Platform Set. For information about Search objects, see [Configuring Search Objects](br3n4tb.html#chdebihg).

#### Platforms

Upon creation, each Platform object is associated with exactly one Platform Set.

### Adding a Platform Set

1. In the Web interface, click Fan-Out Driver Configuration > Configure Platform Sets. The Platform Set page is displayed.
2. Click Add. The New Platform Set page is displayed.
3. Specify an Alternate Naming Attribute if one should be used.
4. Type a name for the new Platform Set, select the UID/GID Set that is to be used by the new Platform Set, then click Apply. The Modify Platform Set page is displayed.
5. Add one or more Search objects to describe the user and group population for the Platform Set. Click Search Objects > Manage.

   For details about Search objects, see [Configuring Search Objects](br3n4tb.html#chdebihg).
6. Add one or more Platform objects to describe the target platforms that constitute the Platform Set. Click Platforms > Add to create a new Platform object and add it to the Platform Set.

   For details about adding Platform objects, see [Configuring Platforms](br3n4tb.html#bfijtk0).

### Changing Platform Set Attributes

1. In the Web interface, click Fan-Out Driver Configuration > Configure Platform Sets. The Platform Set page is displayed.
2. In the list of Platform Sets, click the name of the Platform Set to modify. The Modify Platform Set page is displayed.
3. Update the attributes of the Platform Set as desired.

### Removing a Platform Set

1. Remove all platforms associated with the Platform Set.

   For information about removing a platform, see [Removing a Platform](br3n4tb.html#bfijtkl).
2. In the Web interface, click Fan-Out Driver Configuration > Configure Platform Sets. The Platform Set page is displayed.
3. Click the Remove button of the Platform Set you want to remove. The Remove Platform Set confirmation page is displayed. Click Yes to confirm.

## 6.5.6 Configuring Platforms

A Platform object contains the configuration information the Core Driver uses to serve a platform for Authentication Services and Identity Provisioning. Additional configuration of Platform Services is performed on the platform. For detailed information about configuring and administering Platform Services, see the [Section III, Platform Services Planning](bexh6ay.html).

### Authentication Mode

For platforms that may restrict password length or case sensitivity (mainframes, for example), the Authentication Mode can be used to allow case-sensitive, shorter passwords. This mode allows you to continue to use and enforce complex passwords in eDirectory while providing an authentication method for systems that do not or cannot adhere to the same password policies.

* Check Passwords

  + Select Case Insensitive if you want the Core Driver to check passwords without considering case.
  + Select Case Sensitive to enforce case sensitive passwords.
* Check only the first number of characters

  Enter an integer, greater than or equal to 0, to indicate how many characters should be checked in the correct password. Examples:

  + If you select 8, the Core Driver will only check the first 8 characters of the password for validity.
  + Indicating 0 disables the entire Authentication Mode feature.

### Platform Attributes

Descriptions for each attribute follow.

#### Platform Set

Each platform is a member of exactly one Platform Set. The Platform Set is used to associate users and groups with its member platforms. You specify the Platform Set that a platform belongs to when you create the Platform object. The Platform Set a platform belongs to cannot be changed after the Platform object is created.

#### Permit Password Replication

You can specify whether or not requests from a platform for password replication information are honored. Enable this only for those platforms that need, and are trusted with, password information from eDirectory.

*No:*
No password information is provided to the platform.

*Yes:*
Password information is provided to the platform. No events for an account are sent to the platform unless password information for the account is available to the driver.

*If Available:*
Password information is provided to the platform when it is available. Events for an account are sent to the platform even if no password information is available for the account. This setting can result in accounts being unprotected if it is used without password redirection.

After you enable password replication for a platform, you must restart the Platform Receiver if it is running in Persistent Mode or Polling Mode.

In order for password replication information to be available to a platform, the appropriate password change intercepts must be installed and correctly configured on all systems that can change passwords in eDirectory. For more information, see [Password Replication Requirements](babffihg.html#babdaedd) and the [Section I, Concepts and Facilities](bex00oo.html).

#### Platform Network Address

The DNS name or IP address of the platform system. If the platform system has more than one network interface, list all of the network addresses.

#### DES Key

Information about the DES key that is used to encrypt communications with platforms that use the DES interface is stored in the Platform Configuration object. The platform configuration file of platforms that use the DES interface must contain the same DES key as the Platform Configuration object or communication attempts fail.

When you change the DES key, the previous key is saved in the Platform Configuration object. You can specify a time interval during which communications using the old key are accepted from the platform system. Specify an interval that gives you enough time to update the platform configuration file with the new DES key.

### Adding a New Platform

1. In the Web interface, click Fan-Out Driver Configuration > Configure Platforms. The Platform Configuration page is displayed.
2. Click Add. The New Event Driven Platform page is displayed.
3. Type a name for the platform, select the Platform Set the new platform is to join, then click Apply. The Modify Platform page is displayed.
4. Specify attributes for the platform as appropriate.

   For details, see [Platform Attributes](br3n4tb.html#bfijtk1).
5. Install the platform distribution package on the target server. For details, see [Section IV, Platform Services Administration](bexh69n.html) and the Quick Start for your platform operating system type.

### Changing Platform Attributes

1. In the Web interface, click Fan-Out Driver Configuration > Configure Platforms. The Platform Configuration page is displayed.
2. In the list of platforms, click the name of the platform to modify. The Modify Platform page is displayed.
3. Update the attributes of the platform as desired. For details, see [Platform Attributes](br3n4tb.html#bfijtk1).

### Removing a Platform

1. Remove the driver installation from the platform system. For details, see [Section IV, Platform Services Administration](bexh69n.html).
2. In the Web interface, click Fan-Out Driver Configuration > Configure Platforms. The Platform Configuration page is displayed.
3. In the list of platforms, click the Remove button of the Platform object that you want to remove. The Remove Platform confirmation page is displayed. Click Yes to confirm.

## 6.5.7 Configuring Provisioning

Provisioning configuration involves three attributes.

### Provisioning Configuration Attributes

Descriptions of each attribute follow.

#### Objects Excluded from Provisioning

You can specify that certain objects are globally excluded from Identity Provisioning by the Identity Manager Fan-Out Driver. You can list a fully distinguished LDAP object name or a simple common name. If you add an object that has already been provisioned to target platforms, the object is deleted from the target platforms.

#### Web Interface LDAP Time-Out

The time-out interval, in seconds, for LDAP operations initiated by the Web interface. If an LDAP request does not return within the time-out value, the operation fails.

#### Trawl and Provisioning LDAP Time-Out

The time-out interval, in seconds, for Core Driver LDAP operations. If an LDAP request by a Core Driver does not return within the time out-value, the operation fails.

### Changing Provisioning Attributes

1. In the Web interface, click Fan-Out Driver Configuration > Configure Provisioning. The Provisioning Configuration page is displayed.
2. Modify provisioning attributes as desired.

## 6.5.8 Configuring Search Objects

Search objects determine the users and groups that are included in the Census and Platform Set populations.

Start a Trawl after you make Search object changes. For details about starting a Trawl, see [Starting a Census Trawl](br3n4tb.html#chdgcgid).

### Search Object Types

Search objects can be any of the following:

* *User Objects:*
  Users who are Search objects are added to the Census.
* *Group Objects:*
  Groups that are Search objects are added to the Census. Members of groups that are Search objects are added to the Census.
* *Organizational Role Objects:*
  Occupants of Organizational Role objects that are Search objects are added to the Census.
* *Organization Objects and Organizational Unit Objects:*
  Container objects are scanned for users and groups to add to the Census.
* *Dynamic Group Objects:*
  Members of Dynamic Group objects that are Search objects are added to the Census.

The settings of the Include Users and Include Groups attributes described in the following section take precedence in determining which objects are added to the Census.

### Search Object Attributes

*Include Users:*
Determines if users covered by the Search object are added to the Census.

*Include Groups:*
Determines if groups covered by the Search object are added to the Census.

*Expand:*
Determines if users who are members of Group objects or occupants of Organizational Role objects found inside a container Search object are added to the Census.

*Include Aliases:*
Determines if Alias objects covered by the Search object are added to the Census. The User or Group object that is represented by an Alias object is provisioned to platforms.

*Depth:*
Determines how many steps down the eDirectory tree hierarchy the Core Driver looks beyond the container object for users and groups to add to the Census. A Depth of zero causes the search to stop at the Search object container.

*In Census:*
Determines if users and groups covered by this Search object are included in the Census.

*Platform Set Associations:*
Specifies which Platform Sets this Search object is used to populate.

### Adding Search Objects

1. Click Fan-Out Driver Configuration > Configure Search Objects. The Search Objects page is displayed.
2. Click Add. The Add a Search Object page is displayed.
3. Specify the Search object distinguished name and attributes as desired, then click Apply.

   For details about Search object attributes, see [Search Object Attributes](br3n4tb.html#chdfhdeb).

### Changing Search Object Attributes

1. Click Fan-Out Driver Configuration > Configure Search Objects. The Search Objects page is displayed.
2. In the list of Search objects, click the name of the Search object to modify. The Modify Search Object page is displayed.
3. Update the attributes of the Search object as desired, then click Apply.

   For details about Search object attributes, see [Search Object Attributes](br3n4tb.html#chdfhdeb).

### Removing Search Objects

1. Click Fan-Out Driver Configuration > Configure Search Objects. The Search Objects page is displayed.
2. In the list of Search objects, click the name of the Search object to be deleted. The Modify Search Object page is displayed.
3. In the list of Platform Sets under Platform Set Associations, click each Remove button. The Remove Search Object confirmation page is displayed each time you click a Remove button. Click Yes for each.
4. Under the In Census heading, click the Remove button. The Remove Search Object confirmation page is displayed. Click Yes.

## 6.5.9 Configuring Linux/UNIX UID/GID Sets

A UID/GID Set contains entries for users and groups, together with their corresponding Linux/UNIX UID and GID numbers.

A UID/GID Set is associated with each Platform Set so that the UID and GID numbers of users and groups managed by driver are the same on all Linux/UNIX platforms within the Platform Set.

When a new user or group is added to a Platform Set, it receives the next available UID/GID number.

You can reserve a range of numbers for local use by the platform administrators. The driver does not assign UID or GID numbers within the reserved range.

Leave this option empty to use the posixAccount and posixGroup uidNumber and gidNumber attributes.

### UID/GID Set Attributes

Descriptions of each attribute follow.

#### Highest Used UID/GID

The highest UID/GID number that has been assigned to a user or group.

#### Reserved UID/GID Range

Specifies a range of UID/GID numbers that the driver does not assign to users or groups.

#### Associated Platform Sets

The Platform Sets that use this UID/GID Set.

### Adding a UID/GID Set

1. In the Web interface, click Fan-Out Driver Configuration > Configure UID/GID Sets. The UID/GID Set Configuration page is displayed.
2. Click Add. The New UID/GID Set page is displayed.
3. Type a name for the UID/GID Set configuration object in the ASAM System container.
4. Specify the lowest and highest numbers to be reserved for local system administrator use, then click Apply.

   The value for these numbers cannot be changed after you create the UID/GID Set.

### Viewing UID/GID Set Details

1. In the Web interface, click Fan-Out Driver Configuration > Configure UID/GID Sets. The UID/GID Set Configuration page is displayed.
2. In the list, click the name of the UID/GID Set you want to view. The UID/GID Set Details page is displayed.

### Removing a UID/GID Set

1. Remove all Platform Sets associated with the UID/GID Set.

   For information about removing a Platform Set, see [Removing a Platform Set](br3n4tb.html#br3n4wm).
2. In the Web interface, click Fan-Out Driver Configuration > Configure UID/GID Sets. The UID/GID Set Configuration page is displayed.
3. Click the Remove button of the UID/GID Set you want to remove. The Remove UID/GID Set confirmation page is displayed. Click Yes.

## 6.5.10 Displaying Component Status

To display a status overview of your Identity Manager Fan-Out Driver system, click Fan-Out Driver Utilities > Component Status in the Web interface.

To display status details for a component, click the component name on the Status Overview page.

## 6.5.11 Viewing Driver Documentation

You can use the Web interface to view documentation for the Identity Manager Fan-Out Driver. To view the documentation, click Fan-Out Driver Utilities > Documentation.

## 6.5.12 Viewing Logs

You can use the Web interface to view log files. You can also use Audit to view log information.

### Starting the Log Viewer

To start the Log Viewer, click Fan-Out Driver Utilities > Log Viewer. The Component Log Viewer page is displayed.

### Controlling the Display

You can control the display of log files by setting the values of the following fields. Click Update Criteria after you have specified new values.

* *Component:*
  The component whose log you want to view.
* *Log Type:*
  The type of log for the selected component that you want to view. This can be the Operational Log or the Audit Log.
* *Lines to Return:*
  The number of lines to be returned at one time. This value determines the size of a set of lines used in scrolling operations, such as Next and Find Next.
* *Date:*
  The date of the log information that you want to display. Type this date in yyyy-mm-dd format. For example, specify June 26, 2020 as 2020-06-26.
* *Time:*
  The time of the first log record to display. Type the time in hh:mm:ss (24-hour clock) format. Seconds are optional. For example, specify 1:30 p.m. as 13:30.
* *Find:*
  A search string. The first set of lines containing the Find String, written after the time specified, is displayed. All lines containing the find string are marked with an icon so that they can be easily identified as you scroll through the log.

### Obtaining an Explanation for a Message

To view the documentation for a given message, click its Message ID in the log display. An explanation for the message is displayed.

### Navigating through a Log

Navigation links are provided for the following functions:

* *Beginning of Day:*
  Scrolls the log display to the beginning of the day specified by Date.
* *End of Day:*
  Scrolls the log display to the end of the day specified by Date.
* *Most Current:*
  Scrolls the log display to most current set of lines.
* *Previous:*
  Scrolls the display to the previous set of lines. Scrolling stops at the beginning of the day specified by Date.
* *Next:*
  Scrolls the display to the next set of lines. Scrolling stops at the end of the day specified by Date.
* *Find Previous:*
  Scrolls the display to the previous set of lines that include the find string. Scrolling stops at the beginning of the day specified by Date.
* *Find Next:*
  Scrolls the display to the next set of lines that include the find string. Scrolling stops at the end of the day specified by Date.

## 6.5.13 Displaying Provisioning Details

You can use the Web interface to search for and display objects in the Census and in the user and group population of a Platform Set.

1. Click Fan-Out Driver Utilities > Provisioning Details. The Provisioning Details page is displayed.
2. Select the Search Type you want.
3. Type the Search String.

   Objects whose name begins with the string you type are matched. If you leave this field blank, all objects are matched.
4. Select the maximum number of results to be returned.
5. Click Search.

   Objects matching the search string are returned, up to the maximum count that you specified.
6. Click the name of an object in the results list to view its attributes. The Object Details page is displayed for that object.

## 6.5.14 Reviewing Naming Exceptions

Naming exceptions are produced when a new User or Group object covered by a Census Search object is found with the same name as an Enterprise User or Enterprise Group object that is already present in the Census.

To review naming exceptions in the Web interface, click Fan-Out Driver Utilities > Review Naming Exceptions.

### Resolving Naming Exceptions

1. In the Web interface, click Fan-Out Driver Utilities > Review Naming Exceptions.
2. Use iManager or a similar utility to change the name of the User or Group object that is causing the conflict.
3. To remove the record of the naming exception, click the Remove button for the exception in the list on the Review Naming Exceptions page of the Web interface.

   Trawl processing automatically removes naming exceptions from the list after you have resolved them.

### Excluding Recurring Exceptions

If you have recurring exceptions that are normal for you, you can permanently exclude them from the Census and the exception list.

1. In the Web interface, click Fan-Out Driver Utilities > Review Naming Exceptions.
2. In the desired row, click the button for the action you want to take.

   * To exclude all users and groups with this common name, click Exclude Name.

     If the user or group already exists in the Census and on platforms, the platforms receive a Delete Pending event and, after the Delete Pending Duration, a Delete event. The object is not provisioned to the platform again.
   * To exclude this specific user or group, click Exclude DN.

## 6.5.15 Reviewing Platform Errors

The Platform Receiver can return an error indication for its processing of a provisioning event. Such events remain pending for the platform, but are marked in an error state. You can use the Web interface to clear these events or to mark them to be sent to the Platform Receiver again.

1. In the Web interface, click Fan-Out Driver Utilities > Review Platform Errors. The Review Platform Errors page is displayed.
2. Click the name of the platform whose errors you want to handle. The Errors on Platform page is displayed.
3. Select the desired action for the events that are in error.

If additional events for a user or group associated with a platform are created (by a Trawl or by the Event Subsystem), pending events that are in error are cleared for that user or group.

## 6.5.16 Managing Trawls

Object Services examines portions of eDirectory specified by Census Search objects to build and maintain the Census. This process is known as a Trawl. Only the primary Core Driver performs Trawls. For information about setting the primary Core Driver, see [Designating the Primary Core Driver](br3n4tb.html#bs02yiq).

You can use the Web interface to display information about the last Trawl, to start a Trawl, and to stop a Trawl that is in progress.

*NOTE:*Core Driver installation adds additional indexes for attributes of the objects added to the Identity Vault. Depending on the size of the existing directory tree, these indexes can take some time to bring online. Before you begin your first Trawl, verify that the indexes are in the online state as detailed in [Core Driver Indexes](blxyqwd.html).

### Displaying Trawl Information

To display Trawl information, click Fan-Out Driver Utilities > Trawl.

### Starting a Census Trawl

1. Click Fan-Out Driver Utilities > Trawl. The Trawl Status page is displayed.
2. Click Start.

For information about scheduling Trawls to run automatically, see [Specifying Trawl Times](br3n4tb.html#chdjgegg).

### Stopping a Census Trawl

You can use the Web interface to stop a Trawl.

1. Click Fan-Out Driver Utilities > Trawl. The Trawl Status page is displayed.
2. Click Stop. It can take a few moments for the Trawl to stop.
