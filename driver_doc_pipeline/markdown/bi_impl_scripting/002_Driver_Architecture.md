# 1.1 Driver Architecture

The Scripting driver synchronizes information between the Identity Vault and an external account management system (the connected system).

The Identity Manager detects relevant changes to identities in the Identity Vault and notifies the Subscriber component of the driver. After customizable policy processing, events are sent to the Subscriber shim of the embedded Remote Loader process on the connected system. The Subscriber shim securely passes the information to customizable scripts that perform the required actions.

A process on the connected system polls the account management system for changes at a configurable interval. If the poll returns identity changes, they are written to the change log.

The Publisher shim of the embedded Remote Loader process submits the changes from the change log to the Metadirectory engine as events. The Metadirectory engine processes these events using customizable policies and posts relevant changes to the Identity Vault.

Topics in this section include

* [Publisher Channel](b8mn84s.html#b8mn91p)
* [Subscriber Channel](b8mn84s.html#b8mnaj8)
* [Scriptable Framework](b8mn84s.html#b8mnaxe)
* [Schema File](b8mn84s.html#b8mnb6n)
* [Include/Exclude File](b8mn84s.html#b8mnbeb)
* [Loopback State Files](b8mn84s.html#b8mnblv)

## 1.1.1 Publisher Channel

The Publisher shim provides identity change information to the Metadirectory engine as XDS event documents. The Metadirectory engine applies policies, takes the appropriate actions, and posts the events to the Identity Vault.

### Change Log

The change log stores identity changes in encrypted form. The polling script uses the change log update command to record identity changes it detects. Events are removed from the change log by the Publisher shim at configurable intervals and submitted to the Metadirectory engine for processing. If communication with the Metadirectory engine is temporarily lost, events remain in the change log until communication becomes available again.

### Change Log Update Command

The change log update command encrypts and writes events to the change log. Any process with rights to update the change log can use the change log update command. The change log update command takes command line arguments and standard input, and stores events in encrypted form in the change log for subsequent publishing. The polling script calls the change log update command to record identity changes. For information about using the change log update command, see the developer guides in [Section 5.0, Customizing the Scripting Driver](b8n5bw5.html).

### Polling Script

The polling script periodically scans the local account management system for modifications that have occurred since the last polling interval. If necessary, the polling script updates the change log by calling the change log update command. You can specify the polling interval during installation and by subsequent configuration of the Driver object.

### Publisher Shim

The Publisher shim periodically scans the change log for events. Before scanning the change log, the driver calls the polling script to check the local system for changes that might have been made since the previous poll.

When the Publisher shim finds events in the change log, it decrypts, processes, and sends them to the Metadirectory engine in XDS format over a Secure Sockets Layer (SSL) network link.

## 1.1.2 Subscriber Channel

The Subscriber channel receives XDS command documents from the Metadirectory engine and calls the appropriate script or scripts to handle the command.

The provided scripts must be customized to handle connected system events. For more information see [Section 5.0, Customizing the Scripting Driver](b8n5bw5.html).

## 1.1.3 Scriptable Framework

The interface between the connected system and the driver shim uses customizable scripts. You must extend the scripts that are provided with the driver to support your connected system. Several utility scripts and helper commands are provided with the driver to facilitate communication with the driver shim and the change log. An extensible connected system schema file allows you to add your own objects and attributes to those already supported by the driver.

For more information about the scriptable framework, see [Section 5.0, Customizing the Scripting Driver](b8n5bw5.html).

## 1.1.4 Schema File

The configuration of class and attribute definitions for the connected system is specified using the schema file. You can modify and extend this file to include new objects and attributes. For details about configuring the schema file, see [The Connected System Schema File](b8n6pr6.html).

## 1.1.5 Include/Exclude File

The include/exclude file allows local system policy to enforce which objects are included or excluded from provisioning, on both the Publisher channel and the Subscriber channel, independently. For details about using the include/exclude file, see [The Connected System Include/Exclude File](b8n6prd.html).

## 1.1.6 Loopback State Files

The loopback state files are used to provide automatic loopback detection for external applications that do not have mechanisms to perform loopback detection. This loopback detection prevents subscribed events from being published back to the Identity Vault.
