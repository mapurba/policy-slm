# 1.1 Driver Architecture

The IBM i driver synchronizes information between the Identity Vault and the IBM i security system.

The Identity Manager detects relevant changes to identities in the Identity Vault and notifies the Subscriber component of the driver. After customizable policy processing, events are sent to the Subscriber shim of the embedded Remote Loader process on the connected system. The Subscriber shim uses a user space to securely pass the information to customizable CL programs that perform the required actions.

The driver uses exits on the IBM i system for notification of identity and password changes. These changes are submitted to the change log. The Publisher shim of the embedded Remote Loader process submits the changes from the change log to the Metadirectory engine as events. The Metadirectory engine processes these events using customizable policies and posts relevant changes to the Identity Vault.

The following illustration shows an overview of the architecture.

*Figure 1-1* IBM i Driver Architecture

![This graphic shows the relationships and data flow between driver components as described in the sections that follow.](../graphics/i5os-arch_a.png "This graphic shows the relationships and data flow between driver components as described in the sections that follow.")

## 1.1.1 Publisher Channel

The Publisher shim provides identity change information to the Metadirectory engine as XDS event documents. The Metadirectory engine applies policies, takes the appropriate actions, and posts the events to the Identity Vault.

### Identity Changes

The Publisher shim uses standard operating system exits for notification that an account has changed.

*Table 1-1* Exit Programs

| Description | Exit Point Name |
| Directory Maintenance Exit Program | QIBM\_QOK\_NOTIFY |
| Change User Profile Exit Program | QIBM\_QSY\_CHG\_PROFILE |
| Create User Profile Exit Program | QIBM\_QSY\_CRT\_PROFILE |
| Delete User Profile Exit Program | QIBM\_QSY\_DLT\_PROFILE |
| Restore User Profile Exit Program | QIBM\_QSY\_RST\_PROFILE |

The exit program notifies the Publisher shim of a change. The Publisher shim compares the state of changed objects and the account snapshot files to determine the details of the change, then submits the event to the change log.

### Password Changes

The Publisher shim uses QIBM\_QSY\_VLD\_PASSWRD, which is the Validate Password exit program, to capture password change information, and submits it to the change log.

### Change Log

The change log stores identity changes in encrypted form. Events are removed from the change log by the Publisher shim at configurable intervals and submitted to the Metadirectory engine for processing. If communication with the Metadirectory engine is temporarily lost, events remain in the change log until communication becomes available again.

### Account Snapshot Files

The account snapshot files hold information about the state of users and groups. The Publisher shim maintains the account snapshot files to determine details about changes, because the exits do not provide complete information.

### Publisher Shim

The Publisher shim periodically scans the change log for events. When the Publisher shim finds events in the change log, it decrypts, processes, and sends them to the Metadirectory engine in XDS format over a Secure Sockets Layer (SSL) network link.

IBM i profile names are uppercase. The Publisher shim converts profile names to lowercase when sending events to the Metadirectory engine.

## 1.1.2 Subscriber Channel

The Subscriber channel receives XDS command documents from the Metadirectory engine, stores them as name-value variables in a user space, then calls the appropriate CL programs to handle the command.

The provided CL programs support adds, modifies, renames, and deletes for User and Group objects, and handle password synchronization. You can extend the CL programs to support other object types and events. The CL programs securely access the original command data by calling GETIDMVAR, which provides access to the user space.

## 1.1.3 Scriptable Framework

The interface between the IBM i security system and the driver shim uses customizable CL programs. You can extend the programs that are provided with the driver to support other applications and databases.

Several helper commands are provided with the driver to enable communication with the driver shim and the change log. An extensible connected system schema file allows you to add your own objects and attributes to those already supported by the driver.

For more information about the CL programs and the scriptable framework, see [The Scriptable Framework](b410u7u.html).

## 1.1.4 Schema File

The configuration of class and attribute definitions for the connected IBM i system is specified using the schema file. You can modify and extend this file to include new objects and attributes. For details about configuring the schema file, see [The Connected System Schema File](b3xxapt.html).

The schema for the connected system includes two classes: UserProfile and GroupProfile. UserProfile contains fields from both the \*USRPRF object and the distribution directory. Exactly one distribution directory entry can be associated with each user profile.

## 1.1.5 Include/Exclude File

The include/exclude file allows local system policy to enforce which objects are included or excluded from provisioning, on both the Publisher channel and the Subscriber channel, independently. For details about using the include/exclude file, see [The Connected System Include/Exclude File](b3xxit1.html).

## 1.1.6 Loopback State Files

The loopback state files are used to provide automatic loopback detection for external applications that do not have mechanisms to perform loopback detection. This loopback detection prevents subscribed events from being published back to the Identity Vault.
