# 8.9 Receiver Scripts

The Platform Receiver examines the provisioning events it obtains from Event Journal Services and inspects the state of users and groups on the platform. Then the Platform Receiver calls Receiver scripts as needed to make the state of users and groups on the platform consistent with eDirectory.

The Identity Manager Fan-Out Driver provides a set of fully functional base scripts. You can extend these base scripts as appropriate for your needs. For example, if you have a third party system that uses its own user ID database, you can extend the base scripts to add new users to it based on membership in a special group, and to remove users from it when they are removed from the group.

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

*NOTE:*These are the functions performed by Receiver scripts. The actual implementation is platform-OS dependent. Multiple functions might be combined into a single script, or the steps of a single function might be distributed across several scripts. Not all functions are meaningful for all platform-OS types.

In addition to the scripts that perform actions on users and groups, there are utility scripts that are used for such functions as testing for the existence of a user and checking group membership.

The base scripts are extensively commented. For details on the operation of the base scripts, examine the scripts themselves. Become thoroughly familiar with the operation of a base script before you attempt to extend it.
