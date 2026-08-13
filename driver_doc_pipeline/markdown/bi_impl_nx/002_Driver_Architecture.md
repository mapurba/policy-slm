# 1.1 Driver Architecture

The Linux and UNIX driver synchronizes information between the Identity Vault and the account management system (files, NIS, or NIS+) on connected Linux and UNIX systems.

The Identity Manager detects relevant changes to identities in the Identity Vault and notifies the Subscriber component of the driver. After customizable policy processing, events are sent to the Subscriber shim of the embedded Remote Loader process on the connected system. The Subscriber shim uses shared memory to securely pass the information to customizable shell scripts that perform the required actions.

A process on the connected Linux or UNIX system polls the account management system for changes at a configurable interval. If the poll returns identity changes, they are written to the change log. An authentication module on the connected system monitors password changes and submits them to the change log.

The Publisher shim of the embedded Remote Loader process submits the changes from the change log to the Metadirectory engine as events. The Metadirectory engine processes these events using customizable policies and posts relevant changes to the Identity Vault.

The following illustration shows an overview of the architecture.

*Figure 1-1* Linux and UNIX Driver Architecture

![This graphic shows the relationships and data flow between driver components as described in the sections that follow.](../graphics/nx-arch_a.png "This graphic shows the relationships and data flow between driver components as described in the sections that follow.")

## 1.1.1 Publisher Channel

The Publisher shim provides identity change information to the Metadirectory engine as XDS event documents. The Metadirectory engine applies policies, takes the appropriate actions, and posts the events to the Identity Vault.

### PAM and LAM

Pluggable Authentication Modules (PAM) and AIX Loadable Authentication Modules (LAM) are modules installed on the local system to intercept password changes for participating applications, such as the passwd command. These changes are written to the change log and are later presented to the Metadirectory engine by the Publisher shim. For details about the PAM and LAM configurations, see [PAM Configuration Details](b3yj5z9.html) and [LAM Configuration Details](b3yj64d.html).

### Change Log

The change log stores identity changes in encrypted form. The polling script uses the change log update command to record identity changes it detects. Password changes are written to the change log by the PAM and LAM modules. Events are removed from the change log by the Publisher shim at configurable intervals and submitted to the Metadirectory engine for processing. If communication with the Metadirectory engine is temporarily lost, events remain in the change log until communication becomes available again.

### Change Log Update Command

The change log update command, nxclh, encrypts and writes events to the change log. Any process with rights to update the change log can use the change log update command. The change log update command takes command line arguments and standard input, and stores events in encrypted form in the change log for subsequent publishing. The polling script calls the change log update command to record identity changes. For information about using the change log update command, see the [NetIQÂ® Identity Manager Linux and UNIX Driver Developer Kit Web site](https://www.netiq.com/documentation/identity-manager-developer/driver-developer-kit.html).

### Polling Script

The polling script, poll.sh, is a native shell script that periodically scans the local account management system for modifications that have occurred since the last polling interval. If necessary, the polling script updates the change log by calling the change log update command. You can specify the polling interval during installation and by subsequent configuration of the Driver object.

### Account Snapshot Files

The account snapshot files hold information about the state of users and groups. These files are used by the polling script to detect changes made to users and groups in the account management database (files, NIS, or NIS+).

### Publisher Shim

The Publisher shim periodically scans the change log for events. Before scanning the change log, the driver calls the polling script to check the local system for changes that might have been made since the previous poll.

When the Publisher shim finds events in the change log, it decrypts, processes, and sends them to the Metadirectory engine in XDS format over a Secure Sockets Layer (SSL) network link.

## 1.1.2 Subscriber Channel

The Subscriber channel receives XDS command documents from the Metadirectory engine, stores them as name-value variables in shared memory, then calls the appropriate shell script or scripts to handle the command.

The provided shell scripts support adds, modifies, deletes, moves, and renames for User and Group objects, and handle password synchronization. You can extend the shell scripts to support other object types and events. The shell scripts have secure access to the original command data using the shared memory tool (nxsmh) that accesses shared memory from the driver shim.

## 1.1.3 Scriptable Framework

The interface between the account management database (files, NIS or NIS+) and the driver shim uses customizable shell scripts. You can extend the scripts that are provided with the driver to support other applications and databases.

Several utility scripts and helper commands are provided with the driver to facilitate communication with the driver shim and the change log. An extensible connected system schema file allows you to add your own objects and attributes to those already supported by the driver.

For more information about the shell scripts and the scriptable framework, see [The Scriptable Framework](b410u7u.html).

## 1.1.4 Schema File

The configuration of class and attribute definitions for the connected Linux and UNIX system is specified using the schema file. You can modify and extend this file to include new objects and attributes. For details about configuring the schema file, see [The Connected System Schema File](b3xxapt.html).

The schema for the connected system includes two classes: User and Group. These correspond to the passwd and group maps commonly found in /etc/passwd and /etc/group in the files environment.

By default, the User class contains the attributes loginName, uidNumber, gidNumber, gecos, homeDirectory, and loginShell. These refer to the fields in the passwd map.

```
loginName:x:uidNumber:gidNumber:gecos:homeDirectory:loginShell
```

By default, the Group class contains the attributes groupName, gidNumber, and memberUid. These refer to the fields in the group map.

```
groupName:!:gidNumber:memberUid
```

## 1.1.5 Include/Exclude File

The include/exclude file allows local system policy to enforce which objects are included or excluded from provisioning, on both the Publisher channel and the Subscriber channel, independently. For details about using the include/exclude file, see [The Connected System Include/Exclude File](b3xxit1.html).

## 1.1.6 Loopback State Files

The loopback state files are used to provide automatic loopback detection for external applications that do not have mechanisms to perform loopback detection. This loopback detection prevents subscribed events from being published back to the Identity Vault.
