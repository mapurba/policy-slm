# 6.3 Administration Overview

You use the Web interface for most Core Driver configuration and administration tasks. For details about using the Web interface, see [Applications For Configuration](chdijbdi.html).

The ongoing tasks of administering the driver can be grouped into the following categories.

* Monitoring the operation of the Core Drivers
* Monitoring the operation of Platform Services
* Maintaining the Census
* Reviewing your overall system management plan and making changes to the driver as appropriate

## 6.3.1 Monitoring Core Drivers

You can use the Fan-Out Driver Web application to view component status. For additional information, see [Displaying Component Status](br3n4tb.html#chddecge).

From time to time, depending on the size of the organization and the amount of activity, a system administrator should review the logs written by Core Driver components in order to check the health of the system. For example, you might want to investigate the cause of a large number of denied SSL connection requests. For more information about viewing logs, see [Viewing Logs](br3n4tb.html#chdgdcbb).

The Fan-Out Driver also generates its own messages for purposes of monitoring and troubleshooting. These messages, which are documented in [Section D.0, Messages](betxn43.html). can also be redirected into your own custom programs and status documents to free your administrators from manual Fan-Out log-tracking.

*NOTE:*For more about the configuration parameter for using this capability, see [Publish Fan-Out Log Messages](br3n4tb.html#bfprkqf).

## 6.3.2 Monitoring Platform Services

It is a good idea to monitor the logs written by Platform Services. For details about these logs, see the administration guide for your platform operating system.

## 6.3.3 Maintaining the Census

Administrative personnel should periodically use the Web interface to monitor naming exceptions and inactive users and groups. The frequency at which this is done is a function of the size of the organization being managed, the rate at which changes take place, and the rules in place within the organization concerning unique user IDs in eDirectory. If the organizational structure is appropriate, the same people who manage User objects also maintain the Census.

The actions taken depend on the policies of the individual organization. Some lines follow. For a review of the concepts, see the [Section I, Concepts and Facilities](bex00oo.html).

### Naming Exceptions

A naming exception results if a new User object or a new Group object is encountered with the same name as an Enterprise User object or Enterprise Group object that is already in the Census. In an organization with a policy of unique usernames, this is generally the result of a mistake when adding a new user or group. In this case, the name of the new user or group should be changed to a unique name.

It is also possible that the new user or group was inadvertently added to the Census as a result of a mistake in changing the Census parameters so that the driver is now looking in unintended places for users or groups. In this case, correct the Census parameters.

It is also possible that a departmental administrator is attempting to breach security by taking the user ID of a previously existing user.

### Inactive Users and Groups

An inactive user or group is an Enterprise User or Enterprise Group whose corresponding User object or Group object has been deleted from the directory or is no longer covered by a Census Search object. Deletion of a user might be the legitimate result of someone leaving the organization. If this is true, the entry should be removed from the Census.

It is possible that the user or group has been inadvertently omitted from the Census as a result of a mistake in changing the Census parameters. If this is the case, correct the Census parameters.

You can use the Web interface to set Census parameters to automatically remove inactive users and groups from the Census if this is appropriate for your organization. For details, see [Specifying Automatic Removal of Inactive Users and Groups](br3n4tb.html#br3n4y4).

Enterprise User objects in the Census relate to eDirectory User objects using a globally unique identifier (GUID). Identity Provisioning uses the GUID to prevent the reuse of a User object name from resulting in inappropriate access to the old user's accounts on Platform Systems. You must ensure that the deleted ID has been appropriately removed from all target platforms not managed by Identity Provisioning.

A user that is inactive or is not present in the Census, but does exist in eDirectory, is able to log in to eDirectory directly, but is not able to authenticate through the driver where the Enterprise User ID is required (such as is the case with z/OS or UNIX).

A user that is present in the Census but is not present in eDirectory is not able to authenticate through the driver.
