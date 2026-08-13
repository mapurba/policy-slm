# 6.1 The Scriptable Framework

The Linux and UNIX driver provides a comprehensive scriptable framework that you can use to add to the built-in support for files, NIS, and NIS+, and to add support for other applications.

The Linux and UNIX driver scriptable framework includes components that simplify the job of extending the driver to support new applications.

* Embedded Remote Loader

  + Full SSL support, and an installer to easily configure the certificates
  + Web access to debugging information from the embedded Remote Loader
* Encrypted change log that stores changes from the application to the Identity Vault if there is a communication problem
* Loopback detection system to prevent subscribed events from being published back to the Identity Vault
* Shared memory helper programs that provide for securely passing large variables to and from the scripts
* Easily extendable connected system schema file to support any application
* Include/exclude file for simplified testing and deployment by the platform administrator
* Event support, both for applications that have exits or callouts, and for applications that must be polled for changes

The names of objects and attributes in the scripts are the names specified in the connected system schema file.

The following tables describe the major script files.

*Table 6-1* Identity Vault Command Processing Scripts

| Script File | Identity Vault Event |
| add-group.sh | Add Group |
| add-group-member.sh | Add Group Member |
| add-user.sh | Add User |
| delete-group.sh | Delete Group |
| delete-user.sh | Delete User |
| disable-user.sh | Disable User |
| enable-user.sh | Enable User |
| modify-group.sh | Modify Group |
| modify-password.sh | Password Change |
| modify-user.sh | Modify User |
| query-read-group.sh | Entry Query for Group |
| query-read-user.sh | Entry Query for User |
| query-search-group.sh | Subtree Query for Group |
| query-search-user.sh | Subtree Query for User |
| remove-group-member.sh | Remove Group Member |
| rename-group.sh | Rename Group |
| rename-user.sh | Rename User |

*Table 6-2* Other Scripts

| Script File | Purpose |
| subscriber.sh | Sets up file path locations.  Calls the appropriate shell script based on the type of event and object. |
| poll.sh | Examines the account management system files to detect changes. |
| idmlib.sh | Contains a function library to help the scripts access and manipulate Identity Manager data. |
| heartbeat.sh | Sends a status document to report the health of the application. |
| globals.sh | Holds configurable options that all shell scripts can use during event processing. |
| association.sh | Generates an association for a user or group. |
