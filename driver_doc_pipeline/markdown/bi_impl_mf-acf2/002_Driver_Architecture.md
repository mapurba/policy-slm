# 1.1 Driver Architecture

The driver synchronizes information between the Identity Vault on the Identity Manager platform and ACF2 on the connected z/OS system.

When Identity Manager detects relevant changes to identities in its Identity Vault, it uses the Subscriber channel to process and communicate the updates to all connected systems. Events are received by the Subscriber component of the ACF2 driver, which runs as a started task on the z/OS host system. This Subscriber component securely passes the information to customizable REXX execs that carry out the updates to ACF2.

When changes to passwords and other items relevant to Identity Manager are made at the local ACF2 installation, two security system exit routines are used to capture the changes and place them in a cross memory queue. The change log, another z/OS started task, moves events from the memory queue to the change log data set, where they are stored for processing. At configurable intervals, the Publisher component of the driver polls the change log for events and submits them to Identity Manager, where they are processed for posting to the Identity Vault.

[Figure 1-1](b3wvpsh.html#b6n4rqe) illustrates the driver’s architecture.

*Figure 1-1* ACF2 Driver Architecture

![](../graphics/bi_acf2_archx.png)

The following topics describe the driver architecture in more detail:

* [Component Summary](b3wvpsh.html#blin0t9)
* [Component Discussion](b3wvpsh.html#blk5lb8)

## 1.1.1 Component Summary

Most components of the bidirectional ACF2 driver can be associated with one of the two channels of communication—Subscriber and Publisher—used by the driver and Identity Manager in general.

*Subscriber Channel*
Represents data flowing from Identity Manager to the driver on the connected z/OS system, then on to its final destination in ACF2. In this way, ACF2 functions as a subscriber to Identity Manager events, receiving any updates from the central Identity Vault via the Subscriber channel.

*Publisher Channel*
Represents data flowing from ACF2, through the driver on the host z/OS system, and on to Identity Manager. In this way, ACF2 functions as a publisher of events to Identity Manager, sending any updates from its individual ACF2 installation to the central Identity Vault via the Publisher channel.

*NOTE:*The term “channel,” within the context of Identity Manager data flow, should not be confused with the same term used in mainframe nomenclature to describe a physical cable or connection.

Given this general organization, [Table 1-1](b3wvpsh.html#blj6dnb) provides a summary description for each of the driver’s main components, including the data channel it relates to.

*Table 1-1* Summary of Driver Components

| Data Channel | Component | Description |
| Subscriber | Schema Map | Provides a reference to the hierarchy of objects and attributes available in ACF2. The driver reads the schema map, usually at startup. It’s also used by Identity Manager’s Policy Editor to map the schema of the Identity Vault to the schema for ACF2. |
| Include/Exclude File | Optional configuration file for listing local ACF2 identities that you wish to be included or excluded from the central Identity Vault. Allows local system policy to enforce which objects receive provisioning through the Subscriber channel. |
| REXX Execs | Mainframe scripts that apply the schema map and standard TSO commands to issue changes to ACF2 accounts—including adds, modifies, deletes, and renames—for User objects, and to handle password synchronization. Can be extended to support other object types and events. |
| Publisher | LDXPOST | Exit routine that detects changes to the ACF2 Logonid database. These changes are written to the cross memory queue; the change log started task is notified each time an event is placed in the memory queue. |
| LDXNPXIT | Exit routine that detects password changes to ACF2. These changes are written to the cross memory queue; the change log started task is notified each time an event is placed in the memory queue. |
| LDXNPHXT | Exit routine that detects password phrase changes to ACF2. These changes are written to the cross memory queue; the change log started task is notified each time an event is placed in the memory queue. |
| LDXLOGR | z/OS started task that responds to events stored in the cross memory queue by writing them to the change log data set. The exit routines LDXPOST and LDXNPXIT notify LDXLOGR of each event added to the memory queue. |
| Change Log | z/OS data-set representing the final location where updates are placed in the driver’s portion of the Publisher channel before sending to Identity Manager. The driver’s Publisher component removes events from the change log at configurable intervals and submits them to Identity Manager. |
| Both | ACF2DRV (Driver Shim) | z/OS started task that encapsulates the Remote Loader, Subscriber and Publisher channels. It maintains the network connectivity between the ACF2 system and the Identity Vault; it delivers event data to the REXX scriptable framework, where it is used to modify the ACF2 database; it retrieves event data from the ACF2 change log to be published to the Identity Vault. |
| Remote Loader | Enables communication between Identity Manager and ACF2 as if they were running in a common environment. Identity Manager has no specific knowledge of the Remote Loader. For improved efficiency, the ACF2 driver has its own embedded remote loader, which is used in place of the standard version bundled with Identity Manager. |
| Subscriber Component | Translates XDS event data from the Identity Vault into REXX variables, which are processed by the REXX execs. This component also replies to the Metadirectory engine with XDS status documents. |
| Publisher Component | Polls the change log for new event data and sends it to the Metadirectory engine for processing. It also clears each event entry from the change log after it has been processed. |
| LDXSERV | Custom, APF-authorized, TSO command providing two key services for the driver:  * When updates are passed to ACF2 in the Subscriber channel, LDXSERV is called (with the NOLOG parameter) to flag those items with a token in the Publisher event address space. The token’s presence causes the exit routines to ignore the updates. This prevents redundant loopback to Identity Manager for any changes made through the Subscriber channel. * LDXSERV can also be executed manually (with the STATUS parameter) to display information in the change log data set. |
| ACFQUERY | Tool used by both channels to query the ACF2 Logonid database for records and fields. |
| None (z/OS Components) | ACF2 | (Access Control Facility) CA product option for z/OS security system requirement. |
| Token Address Space | z/OS system memory space used to process changes detected by ACF2 exit routines. Can be flagged with tokens by LDXSERV for changes initiated through Subscriber channel to prevent loopback to Identity Manager. |
| Cross Memory Queue | The memory queue is an encrypted, in-storage buffer used to record events sequentially. Events are added to the memory queue by the ACF2 exit routines, and are removed from the queue by the LDXLOGR started task. The memory queue is located in Subpool 231 (fetch-protected ECSA). |

## 1.1.2 Component Discussion

This section discusses each of the driver components in more detail.

### Driver Shim Started Task

The driver shim, ACF2DRV, runs as a started task. Only one system that shares the security system database runs the driver shim started task. The driver shim started task must be started as part of your normal z/OS system initialization procedure and stopped during normal system shutdown.

### Subscriber Channel Components

The Subscriber channel of the driver shim started task receives XDS command documents from the Metadirectory engine, stores them using z/OS name/token callable services, then calls the appropriate REXX execs to handle the command.

The Subscriber shim calls the LDXSERV command on startup to identify itself to the security system exit routines for loopback detection. This prevents the exit routines from generating events for commands issued by the Subscriber shim.

#### REXX Execs

REXX Execs are essentially scripts that are designed to run on a mainframe. The provided REXX execs support adds, modifies, deletes, and renames for User objects, and handle password synchronization. The REXX execs use standard TSO commands to apply the changes. You can extend the REXX execs to support other object types and events. The REXX execs have secure access to the original XDS command data using the IDMGETV command. IDMGETV accesses z/OS name/token callable services and places the data in REXX variables.

#### Scriptable Framework

The interface between the security system and the driver shim uses customizable REXX execs. You can extend the execs that are provided with the driver to support other applications and databases.

Several utility execs and helper commands are provided with the driver to enable communication with the driver shim and the change log. An extensible connected system schema file allows you to add your own objects and attributes to those already supported by the driver.

For more information about the REXX execs and the scriptable framework, see [The Scriptable Framework](b410u7u.html).

#### Schema File

The configuration of class and attribute definitions for the connected system is specified using the schema file. You can modify and extend this file to include new objects and attributes. For details about configuring the schema file, see [The Connected System Schema File](b3xxapt.html).

The driver uses the keywords of the ACF2 administrative commands to define the schema. The schema includes one class: Logonid. This corresponds to ACF2 Logonid records.

Some items in the schema refer to keywords used to create and modify ACF2 Logonids, but cannot be queried or synchronized. These attributes can be used only by Identity Manager policies to make event-time decisions that affect the behavior of the ACF2 administrative command. The auxiliary schema used to extend eDirectory does not include these attributes.

#### Include/Exclude File

The include/exclude file allows local system policies to enforce which objects are included or excluded from provisioning by the Subscriber channel. This allows for administrative rules to be set and enforced locally rather than having processing decisions made by the Metadirectory engine. For details about using the include/exclude file, see [The Connected System Include/Exclude File](b3xxit1.html).

To control which objects are processed by the Publisher channel, use policies. For details about customizing policies, see the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-48/).

### Publisher Channel Components

The Publisher shim periodically examines the change log for events. When the Publisher shim finds events in the change log, it decrypts, processes, and sends them to the Metadirectory engine over a Secure Sockets Layer (SSL) network link. The Metadirectory engine applies policies, takes appropriate actions, and posts the events to the Identity Vault.

#### Security System Exit Routines

ACF2 provides two exit interfaces. The driver uses these exits to detect activities of interest and to place events in the memory queue. When the driver exit routines place an event in the memory queue, they notify the change log started task. The change log started task then moves the event information to the change log data set. Each system that shares the security system database must run these exit routines provided by the driver in modules LDXPOST, LDXNPXIT and LDXNPHXT.

The driver exit routines perform the following tasks:

* Monitor password changes from the local security system and record user and password information in the memory queue.
* Monitor security system administrative commands entered by users, either directly from the TSO command line, or as generated by the administrative panels. The exit routines record these commands and related information, such as the issuer and time stamp, in the memory queue.

#### Memory Queue

The memory queue is an encrypted, in-storage buffer that holds events. Events are added to the memory queue by the security system exit routines, and are removed from the queue by the change log started task. The memory queue is located in Subpool 231 (fetch-protected ECSA).

#### Change Log Started Task

The change log started task is notified of events added to the memory queue by the driver exit routines and moves them to the change log data set.

Each system that shares a security system database must run the change log started task. The change log started task must be started as part of your normal z/OS system initialization procedure and stopped during normal system shutdown.

#### Change Log Data Set

The change log started task removes encrypted events from the memory queue and stores them in the change log data set for processing by the Publisher shim. The Publisher shim removes events from the change log at configurable intervals and submits them to the Metadirectory engine. If communication with the Metadirectory engine is temporarily lost, events remain in the change log until communication becomes available again.

The change log data set is a standard z/OS direct access (DSORG=DA) data set. There is one change log data set for the set of systems that share the security system database. The change log data set must reside on a shared device unless the security system database is not shared.

### LDXSERV Command

LDXSERV is an APF-authorized, TSO command used in both the Publisher and Subscriber channels.

When updates are passed to ACF2 in the Subscriber channel, LDXSERV is called (with the NOLOG parameter) to flag those items with a token in the Publisher event address space. The token’s presence causes the exit routines to ignore the updates. This prevents redundant loopback to Identity Manager for any changes made through the Subscriber channel.

LDXSERV can also be executed manually (with the STATUS parameter) to display information in the change log data set. To use the command, you must include the driver load library in the logon procedure STEPLIB concatenation.
