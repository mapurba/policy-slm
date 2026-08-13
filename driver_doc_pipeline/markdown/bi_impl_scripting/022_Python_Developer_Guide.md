# 5.7 Python Developer Guide

The Scripting driver provides a complete Python API for interacting with identity management systems whose tools (including APIs) are available on Linux and UNIX. The Identity Vault and Identity Manager can run on any supported operating system. Identity Manager can communicate with any supported system on which the driver is installed via an encrypted network connection.

Before beginning script development, review the preceding topics in this section for information on defining what data is synchronized between identity management systems.

With additional development work, the driver can also be customized to support any scripting language that supports command-line operation.

Developing a custom driver with Python scripts is discussed in this section. Topics include

* [Application Tools Evaluation](bf1lm3e.html#bf1lm3j)
* [Policy and Script Development](bf1lm3e.html#bf1lm3m)
* [Deployment](bf1lm3e.html#bf1lm68)

## 5.7.1 Application Tools Evaluation

To change the data in your external application, you need to know how to use the application’s tools or API (Application Programming Interface). These tools must provide automated operation and not require user interaction.

### Application Command Line Tools

An application often provides command line tools. These tools are manually executed from the command line, and they can be executed from scripts. For example, suppose the application provides a tool to add identities with a program called appadd.

```
appadd -n "Bob Smith" -t "818-555-2100"
```

This command adds an identity named “Bob Smith” with the specified phone number. The strings following the program name are called parameters or arguments. The Linux and UNIX Scripting driver provides a function called exec to execute external programs, log the command to the system log, and produce a status document indicating the level of success.

```
from idmlib import *
CommandLine = "appadd -n $UserName -t $PhoneNumber"
exec(CommandLine($CommandLine)
```

For command line tools, you can construct the command line’s parameters using the values passed to the script, then execute the program.

### Application Event Monitoring

You also need to determine what tools are available for monitoring event changes in the application. The Scripting driver works on a polling system. It periodically calls a polling script to determine what has changed in the external application. You can use the following ideas for monitoring changes:

* The first time the polling script is run, a list of identities and relevant attributes is read from the application using an application-provided tool. This list is stored as a file. On subsequent polls, a new list is generated and compared to the old list. Any differences are submitted as events to the driver.
* The application provides a tool that allows you to request all identities that have changed after a certain point in time. The polling script requests events that have occurred since the previous poll.
* The application allows a script to be run when an event occurs. You can write a script that stores the event data into a file. When the Script driver polling script runs, it consumes this file and submits the data as an event to the driver using the usclh change log tool. For detailed information on usclh, see [Publisher Change Log Tool](b8nrft0.html).

Monitoring the application’s changes might be the most difficult aspect of developing your driver. You must study your application’s tools to determine the best way to achieve synchronization.

## 5.7.2 Policy and Script Development

At this point you should have a list of what data will be synchronized, how events will be handled, and what application tools are available. It is time to develop the heart of your driver in policies and scripts.

Many types of tasks can be handled in driver policies. You can import the driver configuration provided with the Scripting driver, and then edit policies in NetIQ iManager. You can also edit policies and simulate their operation in NetIQ Designer. The extensive functionality of policies is outside the scope of this document, and so you should refer to your Identity Manager policy guides on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/) for help.

It’s often difficult to write complex tasks inside policies, such as executing external commands, processing input and output, and file I/O. Tasks requiring such operations are better suited in scripts, where an entire language environment and tools are available. You can also accomplish many of the operations performed in policies, so if you are more familiar with your scripting language than policies, you can develop your driver more quickly by using scripts. Scripting languages such as Perl, Python and Shell scripts offer an environment that is often well suited for your target application’s APIs or developer kits. For example, your target application might already contain Perl of Python library routines for manipulating the application’s identities.

### Event Data Format

Event data is submitted to the scripts in name/value pair format. This format consists of lines containing a name, an equal sign (=) and a value. Therefore, each line is a name/value pair. Each name/value pair is unique, but there can be multiple name/value pairs with identical names but different values.

```
   ASSOCIATION=BobUser
   ADD_TELEPHONE=818-555-2100
   ADD_TELEPHONE=818-555-9842
```

You typically don’t need to worry about the format. The script library provides functions for retrieving event data independent of its format.

### Subscriber Script Development

After all Policy processing is complete, Identity Manager submits the event in XML format to the driver shim. The driver shim submits the event data to the scripts.

In the default Scripting driver, the subscriber.py script in the scripts folder is called. This script does some preliminary processing, and then calls a routine from an included script. The included scripts correspond to the Subscriber event types: add.py, modify.py, modify-password.py, delete.py, rename.py, move.py, and query.py.

For each event type, you should retrieve the information you need from the event data, submit changes to the external application using application-provided tools and return a status (such as success or failure) to Identity Manager.

Event data is retrieved primarily by using the idmgetvar() function. This function returns an array of values corresponding to the name specified as the function’s parameter. The following table shows many item names.

*Table 5-13* Item Names

| Name | Description |
| COMMAND | The command for the event, usually indicating the event type. Possible values are: add, modify, delete, rename, modify-password, check-object-password. |
| ASSOCIATION | The identifier that distinguishes an identity on both identity management systems. |
| CLASS\_NAME | An identity’s class, such as User or Group. |
| SRC\_DN | An identity’s distinguished name (DN) in the namespace of the source (sender), in slash format. |
| EVENT\_ID | An identifier for the event, for internal use. |
| SRC\_ENTRY\_ID | An identifier for the identity that generated the event, in the namespace of the source (sender). |
| DEST\_DN | An identity’s distinguished name (DN) in the namespace of the destination (receiver), in slash format. |
| DEST\_ENTRY\_ID | An identifier for an entry in the namespace of the destination (receiver). |
| ADD\_attr\_name | A value to be added to an identity, for attribute attr\_name. |
| REMOVE\_attr\_name | A value to be removed from an identity, for attribute attr\_name. |
| ADD\_REF\_attr\_name | A value to be added to attribute attr\_name, where the value is an association referring to another identity. |
| REMOVE\_REF\_attr\_name | A value to be removed from attribute attr\_name, where the value is an association referring to another identity. |
| OLD\_PASSWORD | The previous password for an identity that has changed its password. Used in Modify Password events. |
| PASSWORD | The new password for an identity. Used in Add and Modify Password events. |
| OLD\_SRC\_DN | The distinguished name of an identity before a Move or Rename event. |
| REMOVE\_OLD\_NAME | Specifies whether an old relative distinguished name should be deleted or retained. Used in Rename events. |
| STATUS\_LEVEL | The status of an event: success, warning, retry, error or fatal. |
| STATUS\_MESSAGE | A message to report with a status. |
| STATUS\_TYPE | A type of status, such as heartbeat. |

#### Examples Of Obtaining Event Data

Example 1:

```
from idmlib import *

command = idmgetvar("COMMAND")
# check for an add event
if command = "add":
  # call the add script
  os.system("add.py")
```

Example 2:

```
from idmlib import *

# obtain the event's association and CN attribute
association = idmgetvar("ASSOCIATION")
CN = idmgetvar("CN")
if CN = "bob":
  # for "bob", check to see if he's been enabled
  ENABLE = idmgetvar("REMOVE_Login Disabled")
  if ENABLE = "true":
    # bob is enabled again
    cmd = "appenable -association " + ASSOCIATION
    exec(cmd)
```

#### Handling Associations

The association value indicates which identity has been changed. If the identity has no association, an association must be generated for it using an implementation-specific rule that you have adopted. When Identity Manager processes an event for an identity with no association, it executes the driver’s Matching policy. This policy attempts to match the event’s identity to an identity on the external application’s system. Doing this usually involves executing a query. The default Matching policy included with the Scripting driver queries for matching Users and Groups based on the CN attribute. If the event’s identity matches an identity on the external application, both identities must be assigned the new association. Assigning this association can be done as part of the query-handling script. (Handling queries is discussed in [Handling Query Events](b8n6ps6.html#b8n6zhb).) If no identity matches, an Add event is issued, and the new association can be assigned as part of the Add event-handling script:

```
# Adding an association
from idmlib import *

idmsetvar("COMMAND", "ADD_ASSOCIATION")
idmsetvar("ASSOCIATION", MyAssociation)
idmsetvar("EVENT_ID", EVENT_ID)
idmsetvar("DEST_DN", SRC_DN)
idmsetvar("DEST_ENTRY_ID", SRC_ENTRY_ID)
```

The above example demonstrates each name/value pair that must be set for an association to be assigned by the Identity Manager engine. The values of EVENT\_ID, SRC\_DN and SRC\_ENTRY\_ID are always sent by the engine during an add event, and therefore, are available for your add script to obtain using idmgetvar(). The example above also illustrates the idmsetvar() function. For detailed information on how to use idmsetvar(), see [Python (idmlib.py) Reference](bf1m36m.html). This function sets a name and value which indicates what action Identity Manager should perform. For example, the pair “COMMAND" and “ADD\_ASSOCIATION" instructs the shim to create an add-association document to assign an association to an identity, as discussed above. The pair "EVENT\_ID” and EVENT\_ID instruct the shim to assign add-association document an event-id described by the variable EVENT\_ID. This is important for the engine to match documents sent and returned on the subscriber channel.

The Subscriber can also issue MODIFY\_ASSOCIATION and REMOVE\_ASSOCIATION commands:

```
# Removing an association
from idmlib import *

idmsetvar("COMMAND", "REMOVE_ASSOCIATION")
idmsetvar("ASSOCIATION", MyAssociation)
idmsetvar("EVENT_ID", EVENT_ID)
idmsetvar("DEST_DN", SRC_DN)
idmsetvar("DEST_ENTRY_ID", SRC_ENTRY_ID)

# Modifying an association
my idmlib import *

idmsetvar("COMMAND", "MODIFY_ASSOCIATION")
idmsetvar("ASSOCIATION", OldAssociation)
idmsetvar("ASSOCIATION", NewAssociation)
idmsetvar("EVENT_ID", EVENT_ID)
idmsetvar("DEST_DN", SRC_DN)
idmsetvar("DEST_ENTRY_ID", SRC_ENTRY_ID)
```

#### Returning an Event Status

On the Subscriber channel, you often do not need Identity Manager to perform an action, but simply need to report a status. The status\_ subroutines noted below can be used to indicate a status to Identity Manager. They take a message to be logged as the parameter.

*Table 5-14* STATUS Subroutines

| Subroutine | Identity Manager Action |
| status\_success() | Identity Manager marks the event as a success and submits the next event in the event queue, if any. You should issue this status even if your script does nothing. |
| status\_warning() | The event can be processed, but it might require attention. Identity Manager issues your warning message in its log, and then submits the next event. |
| status\_retry() | The event cannot be processed, but Identity Manager should resubmit the event because it should be able to be processed soon. This status can be issued if your external application appears to be temporarily unavailable. However, this status should be used cautiously because a backlog results if Identity Manager continually retries one event. |
| status\_error() | The event cannot be processed and it should not be resubmitted. Identity Manager issues the error message and submits the next event. You should make a detailed error message so the problem can be corrected. |
| status\_fatal() | For some reason, the driver must be stopped. Identity Manager issues your message and stops the driver. This could be used if the external application appears to be permanently offline. The event remains in the queue and is resubmitted when the driver is restarted. |

#### Examples Using the Status() Functions

```
rc = exec(cmd)
if (rc = 0):
  status_success("Command was successful")
rc = exec(cmd)
if (rc == 0):
  if (password eq "")
    # created, but no password
    status_warning("User added without password")

rc = exec(cmd)
if (rc != 0):
  status_error("Command failed")
```

#### Writing Values

The idmsetvar() function is used to set values to return to Identity Manager. It is passed a name and value. For detailed information on how to use idmsetvar(), see [Python (idmlib.py) Reference](bf1m36m.html). In the previous ADD\_ASSOCIATION example, idmsetvar() is used to set the ASSOCIATION value. You can specify values for items listed in the table above. Generally, idmsetvar() is used is to add, modify and delete associations or return information for a query operation. Other information is returned to the shim through other command functions, such as status\_success(), which use idmsetvar() indirectly.

#### Handling Query Events

For Query events, Identity Manager submits values that define the parameters of a search of the external application’s identity management system. Queries are usually issued from the Policies you have defined for your system. The table below specifies values that can be specified in queries. Not all values are relevant to your external application.

*Table 5-15* Query Values

| Value Name | Description |
| SCOPE | Specifies what identities are searched. A base object is specified with the ASSOCIATION or DEST\_DN values (see below). The value entry means that only the base object is searched. The value subordinates means that the immediate subordinates of the base object are searched. The value subtree (the default) indicates that the base object and all subordinates are searched. The last two values are only relevant in a hierarchical system. |
| ASSOCIATION | The base object for the search. If both ASSOCIATION and DEST\_DN have values, ASSOCIATION is used. If neither is specified, the base object is the root of the identity management system. |
| DEST\_DN | The base object for the search (see also ASSOCIATION above). |
| CLASS\_NAME | The base class of the base object. |
| EVENT\_ID | An identifier for the event. |
| SEARCH\_CLASSES | A list of classes for which to search. Only identities of these classes are returned. If not specified, all identities in the scope matching SEARCH\_ATTR\_ values are returned (see below) |
| SEARCH\_ATTRS | A list of the attribute names specified in SEARCH\_ATTR\_ values (see below). |
| SEARCH\_ATTR\_attr\_name | A value that the specified attribute must match. Replace attr\_name with the desired attribute name. Only identities matching all SEARCH\_ATTR\_ filters are returned. |
| READ\_ATTRS | A list of the attribute names whose values are returned for each matching identity. |
| ALL\_READ\_ATTRS | The presence of this value indicates that all attribute values should be returned for matching identities. |
| NO\_READ\_ATTRS | The presence of this value indicates that no attribute values should be returned for matching identities. |
| READ\_PARENT | The presence of this value indicates that the parent object of each matching identity should be returned. Only relevant in hierarchical systems. |

When a query invokes your query script, use the parameter information to query your external application using application-provided tools. Then return each identity by setting an INSTANCE command, followed by relevant values from the list below.

*Table 5-16* Query Values

| Value Name | Description |
| CLASS\_NAME | The class of the identity. Required. |
| SRC\_DN | A distinguished name representing the logical location of the identity in the system (optional). |
| ASSOCIATION | The association of the identity, if available (optional). |
| PARENT | The association of the parent object of the identity (optional). Only relevant in hierarchical systems. |
| ATTR\_attr\_name | A list of values for the attribute specified by attr\_name. Return attribute values specified by the READ\_ATTRS value. |

After returning all identities, call status\_success() to indicate a successful query.

#### Subscriber Summary and Examples

Below is a more detailed summary of the actions to take for a non-Query event.

1. Gather information about the event using idmgetvar(). Return a warning or error if there is a problem.
2. Submit the event data to the external application using application-provided tools.
3. Set event values with idmsetvar().
4. If you have not already done so, set a status with a status() subroutine.

Below is an example add.py, which forms an association from an identity’s CN and class name, and uses a hypothetical tool called appadd.

```
#!/usr/bin/python

from idmlib import *

ClassName = idmgetvar("CLASS_NAME")
CN = idmgetvar("CN")
PhoneNumber = idmgetvar("Telephone")
EventId = idmgetvar("EVENT_ID")
SrcDn = idmgetvar("SRC_DN")
SrcEntryId = idmgetvar("SRC_ENTRY_ID")
if ClassName = "" || CN = "":
  status_error("Add event: missing CLASS_NAME and/or CN")
else:
  Command = "appadd -n " + CN + -t " + PhoneNumber
  rc = exec(Command)
  if rc = 0:
    idmsetvar("COMMAND", "ADD_ASSOCIATION")
    idmsetvar("ASSOCIATION", CN + ClassName)
    idmsetvar("EVENT_ID", EventId)
    idmsetvar("DEST_DN", SrcDn)
    idmsetvar("DEST_ENTRY_ID", SrcEntryId)
    status_success("Add event succeeded")
  else:
    status_error("Add event failed with error code" + rc)
```

Handling a query is a similar process, except that you return INSTANCE items rather than using other commands. Below is an example query.py that searches an external application for a telephone number. It uses a hypothetical tool called appsearch.

```
#!/usr/bin/python

import os
from idmlib import *

SearchName = idmgetvar("SEARCH_ATTR_CN")
EventId = idmgetvar("EVENT_ID")
Association = idmgetvar("ASSOCIATION")
ClassName = idmgetvar("CLASS_NAME")
if SearchName = "":
  status_error("Query: no search value")
else:
  Command = "appsearch -n " + SearchName
  Results = os.popen(Command, ‘r').readlines()
  if Results != "":
    phoneinfo = split(" ", Results)
    Phone = phoneinfo[0]
    idmsetvar("COMMAND", "INSTANCE")
    idmsetvar("CLASS_NAME", ClassName)
    idmsetvar("EVENT_ID", EventId)
    idmsetvar("ASSOCIATION", Association)
    idmsetvar("ATTR_Telephone", Phone)
    status_success("Query succeeded")
  else:
    # Return success with no results
    status_success("Query succeeded (no matches)")
```

### Publisher Script Development

Events that occur on the external application are submitted to Identity Manager on the Publisher channel. The Scripting driver polls the external application for events periodically. How this poll detects events is implementation-specific and must be defined by the user.

#### Polling for Application Events

The Driver calls poll.py to detect application events. poll.py should be implemented as follows:

1. Use application-provided tools to detect events in your application (see discussion in Step 2).
2. For each event, call the usclh changelog tool to submit the event to be published. The changelog tool allows for additional information to be supplied through standard input. This is an appropriate mechanism for passing data that might be too large for command line or too sensitive to appear in a shell’s history or environment. For more information on usclh, see [Publisher Change Log Tool](b8nrft0.html)

Below is an example of a poll.py that checks for a password change. It uses a hypothetical application tool called appchg.

```
#!/usr/bin/python

import os
from idmlib import *

# look for password changes with our ficticious app, appchg
results = os.popen("appchg --passwd-changes", 'r').readlines()
for result in results:
  fields = result.split(":")
  Association = fields[0]
  Password = fields[1]
  # submit event to the publisher changelog
  usclh = os.popen(usclh -t modify-password -a " + Association, 'w')
  usclh.write(Password)
  usclh.close()

# look for attribute values being added to each user
results = os.popen("appchg --add-attr-changes")
for result in results:
  # Entries are in the format "association:attribute:value"
  fields = result.split(":")
  Association = fields[0]
  Attribute = fields[1]
  Value = fields[2]
  # submit event to the publisher changelog
  local_usclh = os.environ.get('INSTALL_PATH') + "bin/usclh"
  usclh = os.popen(local_usclh + " -t modify -c User -a " + Association, 'w')
  usclh.write("ADD_" + Attribute + "=" + Value)
  usclh.close()

# look for attribute values being removed from each user
results = os.popen("appchg --add-attr-changes")
for result in results:
  # Entries are in the format "association:attribute:value"
  fields = result.split(":")
  Association = fields[0]
  Attribute = fields[1]
  Value = fields[2]
  # submit event to the publisher changelog
  local_usclh = os.environ.get('INSTALL_PATH') + "bin/usclh"
  usclh = os.popen(local_usclh + " -t modify -c User -a " + Association, 'w')
  usclh.write("REMOVE_" + Attribute + "=" + Value)
  usclh.close()
```

In the above example, three separate events are submitted to the publisher change log, using the changelog tool, usclh. The first invocation submits a modify-password event to be published. The second event submits a modify event to be published for an attribute add. The third invocation submits another modify event to be published for an attribute removal. The second and third invocations can be combined into a single modify event, if desired.

Events submitted using usclh are processed through your driver’s Publisher Channel’s policies. See the Identity Manager policy guides on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/) for more information.

#### Using the Heartbeat Script

Another script executed in the Publisher Channel is heartbeat.py. This script is executed when the Publisher Channel is idle for the interval specified in the Driver parameters. (You can set the interval to 0 so no heartbeat is issued.) You can use the heartbeat to check the availability of the external system or do “idle state” tasks. The heartbeat\_success(), heartbeat\_warning(), and heartbeat\_error() subroutines can be used to indicate the result of the heartbeat. Below is an example based on a hypothetical tool called apphealth.

```
from idmlib import *

rc = os.sytem("apphealth")
if (rc = 0):
  heartbeat_success("Heartbeat succeeded")
else:
  heartbeat_error("Heartbeat failed with error code " + rc)
```

### Other Scripting Topics

* [Driver Parameters](bf1lm3e.html#bf1lm5m)
* [Querying the Identity Vault](bf1lm3e.html#bf1lm5v)
* [Tracing and Debugging](bf1lm3e.html#bf1lm5z)

#### Driver Parameters

A driver has values known as driver parameters. The driver parameters are divided into driver settings applicable to the whole driver, and Subscriber and Publisher Settings for their respective channels. The idmgetdrvvar(), idmgetsubvar() and idmgetpubvar() functions can be used to retrieve these values. The table below shows parameters in the default Scripting driver. Other parameters can be added to the driver’s XML Configuration file (see the NetIQ Identity Manager 3.6.1 Administration Guide).

*Table 5-17* Scripting Driver Parameters

| Parameter Name | Driver/Channel | Description | Values |
| INSTALL\_PATH | Driver | The installation path of the Driver | string value |
| auto-loopback-detection | Driver | Whether to enable automatic loopback detection | true/false |
| subscriber-script | Subscriber | The root script file for Subscriber events, relative to the driver installation path | string value |
| pub-polling-interval | Publisher | The interval in seconds between Publisher polls for application events | number |
| pub-heartbeat-interval | Publisher | The amount of idle time in seconds before a heartbeat event is issued | number |
| pub-disabled | Publisher | Whether the Publisher Channel (such as for polling) is disabled | true/false |

In the following example, a script retrieves the Publisher polling interval:

```
 PollingInterval = idmgetpubvar("pub-polling-interval")
```

#### Querying the Identity Vault

Scripts might need to retrieve information from the Identity Vault. They can do this by issuing a query.

1. Execute the query by calling idmquery(class, association, readattrs) with the appropriate parameters:

   * The first parameter is the class-name
   * The second parameter is the association of the object to query
   * The third parameter are the attributes to read, comma-separated
2. Read the result (instance) using idmgetqvar().

Query support is currently limited. It returns only one instance based on the specified association or DN. If both association and DN are specified, association is used. The functions below allow you to retrieve information from the instance.

The following is an example of a query of the Identity Vault that retrieves the address and ZIP code for user Bob.

```
from idmlib import *

idmquery("User", "Bob", "SA,Postal Code")
Address = idmgetqvar("SA")
ZIPCode = idmgetqvar("Postal Code")
# ... etc. ...
```

#### Tracing and Debugging

The function trace() allows you to write a message to the Trace Log. Tracing is useful for script debugging and auditing.

```
from idmlib import *

trace("Trace Message")
```

When you develop scripts, you might need to do some debugging to track down problems. The following list indicates some facilities for debugging.

* The Driver traces activity to its Trace file (logs/trace.log by default). The trace level setting in conf/usdrv.conf controls how much debugging is written to the log.

  | Trace Level | Description |
  | 0 | No debugging. |
  | 1-3 | Identity Manager messages. Higher trace levels provide more detail. |
  | 4 | Previous level plus Remote Loader, driver, driver shim, and Driver connection messages. |
  | 5-7 | Previous level plus Change Log and loopback messages. Higher trace levels provide more detail. |
  | 8 | Previous level plus Driver status log, Driver parameters, Driver command line, Driver security, Driver Web server, Driver schema, Driver encryption, Driver SOAP API, and Driver include/exclude file messages. |
  | 9 | Previous level plus low-level networking and operating system messages. |
  | 10 | Previous level plus maximum low-level program details. |

  The trace level is set using the -trace option in usdrv.conf, for example -trace 9.

  You can view the trace file through a Web browser:

  1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
  2. Authenticate by using any username and the password that you specified as the Remote Loader password.
  3. Click Trace.
* The eDirectory tool DSTrace can be used to monitor Identity Manager activity. Set the tracing level for the Driver in iManager. DSTrace shows the XML documents being submitted to the driver for events and how policies are evaluated. It also shows the status and message for each event.
* The Status Log is written to logs/dirxml.log. It shows a summary of the events that have been recorded on the Subscriber and Publisher channels.

  You can view the Status Log through a Web browser:

  1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
  2. Authenticate by using any username and the password that you specified as the Remote Loader password.
  3. Click Status.

Although it is best to start the driver in production environments from the startup script, you can run usdrv manually. When you do so, any text written to standard output from scripts is displayed in the interactive shell.

## 5.7.3 Deployment

The Scripting driver is installed by using a setup program. See [Installing the Linux and UNIX Scripting Driver Shim](b8moq22.html), for more information on installing the default driver.

### Deploying a Custom Driver

To deploy your custom driver, the end user should first run the Scripting driver installation program provided by the installation media (see[Installing the Linux and UNIX Scripting Driver Shim](b8moq22.html)). This program installs core files needed by the driver. Then, your custom driver files can be deployed in any convenient way, whether through an installation program or even simply an archive file. The table below shows the directory structure below the installation directory and what files are installed.

*Table 5-18* Directory Structure and Files

| Directory | Description | Required Files |
| bin/ | Location of executable programs | usdrv  ussmh  usclh |
| changelog/ | Used for Publisher event processing | None |
| conf/ | Location of the driver shim configuration file | usdrv.conf (customized) |
| keys/ | Location of security key files | None |
| logs/ | Location of log files | None |
| loopback/ | Used for automatic loopback detection | None |
| rules/ | Location of Driver configuration file | Scripting.xml (customized) |
| schema/ | Location of schema files | schema.def (customized) |
| scripts/ | Location of script files | Those required by your Driver (customized) |

On Linux and UNIX, the Scripting driver is installed to /opt/novell/usdrv.

The formats of usdrv.conf and schema.def can be viewed in [The Driver Shim Configuration File](b8mqqe6.html) and [The Connected System Schema File](b8n6pr6.html).

If SSL encryption is desired for communication between the driver shim and Identity Manager engine, a certificate must be retrieved from the Identity Vault. Run usdrv -s and follow the prompts to retrieve the certificate, which will be stored in the keys/ directory. You must have LDAP with SSL available for the Metadirectory. When making an installation program for deployment, you might want to run usdrv -s as part of the installation.

To ensure that only authorized systems access the Metadirectory, a Driver object password and Remote Loader password are used. Run usdrv -sp and enter the passwords at the prompts. This action can be incorporated into an installation program.

You should distribute the XML configuration file that contains parameters and policies your Driver needs. The user can then select it when installing your Driver.
