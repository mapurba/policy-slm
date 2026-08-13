# 5.8 Microsoft VBScript Developer Guide

The Scripting driver provides a complete Microsoft VBScript API for interacting with identity management systems whose tools (including APIs) are available on Windows. The Identity Vault and Identity Manager can run on any supported operating system. Identity Manager can communicate with any supported system on which the driver is installed via an encrypted network connection.

Before beginning script development, review the preceding topics in this section for information on defining what data is synchronized between identity management systems.

With additional development work, the driver can also be adapted to support any scripting language that supports command line operation.

Developing a custom driver with VBScript is discussed in this section. Topics include

* [Application Tools Evaluation](b8nlv23.html#b8nlxlb)
* [Policy and Script Development](b8nlv23.html#b8nm2b1)
* [Deployment](b8nlv23.html#b8nnc2b)

## 5.8.1 Application Tools Evaluation

To change the data in your external application, you need to know how to use the application’s tools or API (Application Programming Interface). These tools must provide automated operation and not require user input.

### Application Command Line Tools

An application often provides command line tools. These tools are manually executed from the Windows command prompt, and they can be executed from scripts. For example, suppose the application provides a tool to add identities with a program called appadd.exe.

```
appadd -n "Bob Smith" -t "818-555-2100"
```

This command adds an identity named “Bob Smith” with the specified phone number. The strings following the program name are called parameters or arguments. The Scripting driver provides a function called IDMExecute to execute external programs.

```
   CommandLine = "appadd -n " & UserName & " -t " & PhoneNumber
   ExitCode = IDMExecute(CommandLine)
```

There is also a function called IDMExecuteIO that allows you to pass information on the program’s standard input, and receive output from the program’s standard output and standard error.

```
  Dim Input(1)

  Input(0) = "USERNAME=bobsmith"
  Input(1) = "TELEPHONE=818-555-2100"

  Output = IDMExecuteIO("appadd", Input)

  ExitCode = Output(0)
```

IDMExecuteIO's first parameter is the command line, and its second parameter is an array of strings (or Empty) that is submitted as lines to the command program. It returns an array, the first element of which is the program’s exit code, and then strings that represent lines returned on the program’s standard output and standard error.

For command line tools, you can construct the command line’s parameters using the values passed to the script, then execute the program.

### Application Objects

Another way to modify application data is through Windows COM (Common Object Model) objects. Consult your application’s documentation to see whether it exposes any COM objects. These COM objects can be loaded directly in VBScript:

```
   Set AppObject = WScript.CreateObject("MyApplication.MyObject")
   AppObject.AddIdentity("Bob Smith", "818-555-2100")
```

There are no guarantees regarding what types of tools are available, or even whether any tools are available. You must determine if sufficient tools are provided by the application. If they are not, you can contact the application’s developers and request that such tools be made available.

You should make a list of what tools can be used for each event type. The application might provide one program that can be used for any event type, or it might provide multiple tools.

### Application Event Monitoring

You also need to determine what tools are available for monitoring event changes in the application. The Scripting driver works on a polling system. It periodically calls a polling script to determine what has changed in the external application. You can use the following ideas for monitoring changes:

* The first time the polling script is run, a list of identities and relevant attributes is read from the application using an application-provided tool. This list is stored as a file. On subsequent polls, a new list is generated and compared to the old list. Any differences are submitted as events to the driver.
* The application provides a tool that allows you to request all identities that have changed after a certain point in time. The polling script requests events that have occurred since the previous poll.
* The application allows a script to be run when an event occurs. You write a script that stores the event data into a file. When the Scripting driver polling script runs, it consumes this file and submits the data as an event to the driver.

Monitoring the application’s changes might be the most difficult aspect of developing your driver. You must study your application’s tools to determine the best way to achieve synchronization.

## 5.8.2 Policy and Script Development

At this point you should have a list of what data will be synchronized, how events will be handled, and what application tools are available. It is time to develop the heart of your driver in policies and scripts.

Many types of tasks can be handled in driver policies. You can import the driver configuration provided with the Scripting driver, and then edit policies in NetIQ iManager. You can also edit policies and simulate their operation in NetIQ Designer. The extensive functionality of policies is outside the scope of this document, so you should refer to your Identity Manager policy guides on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/) for help.

Tasks that don’t interact with the external application might be more suited to policies. On the other hand, if you are more familiar with your scripting language than policies, you can develop your driver more quickly by using scripts.

### Event Data Format

Event data is submitted to the scripts in name/value pair format. This format consists of lines containing a name, an equal sign (=) and a value. Therefore, each line is a name/value pair. Each name/value pair is unique, but there can be multiple name/value pairs with identical names but different values.

```
   ASSOCIATION=BobUser
   ADD_TELEPHONE=818-555-2100
   ADD_TELEPHONE=818-555-9842
```

You typically don’t need to worry about the format. The script library provides functions for retrieving event data.

### Subscriber Script Development

After all policy processing is complete, Identity Manager submits the event in XML format to the driver shim. The driver shim submits the event data to the scripts.

In the default Scripting driver, the Subscriber.wsf script in the scripts folder is called. This script does some preliminary processing, and then calls a routine from an included script. The included scripts correspond to the Subscriber event types: Add.vbs, Modify.vbs, ModifyPassword.vbs, Delete.vbs, Rename.vbs, Move.vbs, and Query.vbs.

For each event type, you should retrieve the information you need from the event data, submit changes to the external application using application-provided tools and return a status (such as success or failure) to Identity Manager.

Event data is retrieved primarily using the IDMGetEventValues function. This function returns an array of values corresponding to the name specified as the function’s parameter. (IDMGetEventValue is available for single-valued items.) The following table shows many item names.

*Table 5-19* Item Names

| Value | Description |
| COMMAND | The command for the event, usually indicating the event type. |
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

#### Handling Associations

The association value indicates which identity has been changed. If the identity has no association, an association must be generated for it using an implementation-specific rule that you have adopted. When Identity Manager processes an event for an identity with no association, it executes the driver’s Matching policy. This policy attempts to match the event’s identity to an identity on the external application’s system. Doing this usually involves executing a query. The default Matching policy included with the Scripting driver queries for matching Users and Groups based on the CN attribute. If the event’s identity matches an identity on the external application, both identities must be assigned the new association. Assigning this association can be done as part of the query-handling script. (Handling queries is discussed in [Handling Query Events](b8n6ps6.html#b8n6zhb).) If no identity matches, an Add event is issued, and the new association can be assigned as part of the Add event-handling script:

```
   IDMSetCommand "ADD_ASSOCIATION"
   IDMWriteValue "ASSOCIATION", MyAssociation
              (etc.)
```

The example above also illustrates the IDMSetCommand function. This function sets a command value which indicates what action Identity Manager should perform. The ADD\_ASSOCIATION command assigns an association to an identity, as discussed above. The Subscriber can also issue MODIFY\_ASSOCIATION and REMOVE\_ASSOCIATION commands.

#### Returning an Event Status

On the Subscriber channel, you often do not need Identity Manager to perform an action, but simply need to report a status. The IDMStatus subroutines noted below can be used to indicate a status to Identity Manager. They take a message to be logged as the parameter.

*Table 5-20* Subroutines

| Subroutine | Identity Manager Action |
| IDMStatusSuccess | Identity Manager marks the event as a success and submits the next event in the event queue, if any. You should issue this status even if your script does nothing. |
| IDMStatusWarning | The event can be processed, but it might require attention. Identity Manager issues your warning message in its log, and then submits the next event. |
| IDMStatusRetry | The event cannot be processed, but Identity Manager should resubmit the event because it should be able to be processed soon. This status can be issued if your external application appears to be temporarily unavailable. However, this status should be used cautiously because a backlog results if Identity Manager continually retries one event. |
| IDMStatusError | The event cannot be processed and it should not be resubmitted. Identity Manager issues the error message and submits the next event. You should make a detailed error message so the problem can be corrected. |
| IDMStatusFatal | For some reason, the driver must be stopped. Identity Manager issues your message and stops the driver. This could be used if the external application appears to be permanently offline. The event remains in the queue and is resubmitted when the driver is restarted. |

#### Writing Values

IDMSetCommand and/or a status subroutine must be called before specifying values with IDMWriteValues. IDMWriteValues (or its single-valued version IDMWriteValue) is used to set values to return to Identity Manager. It is passed a value name and an array of values. In the ADD\_ASSOCIATION example above, IDMWriteValue is used to set the ASSOCIATION value. You can specify values for items listed in the table above.

#### Handling Query Events

For Query events, Identity Manager submits values that define the parameters of a search of the external application’s identity management system. Queries are usually issued from the policies you have defined for your system. The table below specifies values that can be specified in queries. Not all values are relevant to your external application.

*Table 5-21* Query Values

| Value Name | Description |
| SCOPE | Specifies what identities will be searched. A base object is specified with the ASSOCIATION or DEST\_DN values (see below). The value “entry” means that only the base object is searched. The value “subordinates” means that the immediate subordinates of the base object are searched. The value “subtree” (the default) indicates that the base object and all subordinates are searched. The last two values are only relevant in a hierarchical system. |
| ASSOCIATION | The base object for the search. If both ASSOCIATION and DEST\_DN have values, ASSOCIATION is used. If neither is specified, the base object is the root of the identity management system. |
| DEST\_DN | The base object for the search (see also ASSOCIATION above). |
| CLASS\_NAME | The base class of the base object. |
| EVENT\_ID | An identifier for the event. |
| SEARCH\_CLASSES | A list of classes for which to search. Only identities of these classes are returned. If not specified, all identities in the scope matching SEARCH\_ATTR\_ values are returned (see below). |
| SEARCH\_ATTRS | List of attribute names used in SEARCH\_ATTR\_ values (see below). |
| SEARCH\_ATTR\_attr\_name | A value that the specified attribute must match. Replace attr\_name with the desired attribute name. Only identities matching all SEARCH\_ATTR\_ filters are returned. |
| READ\_ATTRS | List of attribute names whose values returned for each identiy match. |
| ALL\_READ\_ATTRS | The presence of this value indicates that all attribute values should be returned for matching identities. |
| NO\_READ\_ATTRS | The presence of this value indicates that no attribute values should be returned for matching identities. |
| READ\_PARENT | The presence of this value indicates that the parent object of each matching identity should be returned. Only relevant in hierarchical systems. |

Execute the query against the external application using application-provided tools. Then return each identity by setting an INSTANCE command, followed by relevant values from the list below.

*Table 5-22* Query Values

| Value Name | Description |
| CLASS\_NAME | The class of the identity. Required. |
| SRC\_DN | A distinguished name representing the logical location of the identity in the system (optional). |
| ASSOCIATION | The association of the identity, if available (optional). |
| PARENT | The association of the parent object of the identity (optional). Only relevant in hierarchical systems. |
| ATTR\_attr\_name | A list of values for the attribute specified by attr\_name. Return attribute values specified by the READ\_ATTRS value. |

After returning all identities, call IDMStatusSuccess to indicate a successful query.

#### Subscriber Summary and Examples

Below is a more detailed summary of the actions to take for a non-Query event.

1. Gather information about the event using IDMGetEventValues. Return a warning or error if there is a problem.
2. Submit the event data to the external application using application-provided tools.
3. Set a command using IDMSetCommand and/or a status with the IDMStatus subroutines, based on the result of the event.
4. Set event values with IDMWriteValues.
5. If you have not already done so, set a status with an IDMStatus subroutine.

Below is an example of the Add.vbs script, which forms an association from an identity’s CN and class name, and uses a hypothetical tool called appadd.

```
Sub ADD
  ClassName = IDMGetEventValue("CLASS_NAME")
  CN = IDMGetEventValue("CN")
  PhoneNumber = IDMGetEventValue("Telephone")
  If IsEmpty(ClassName) Or IsEmpty(CN) Then
    IDMStatusError "Add event: missing CLASS_NAME and/or CN"
  Else
    Command = "appadd -n """ & CN & """ -t """ & PhoneNumber & """"
    ExitCode = IDMExecute(Command)
    If ExitCode = 0 Then
      IDMSetCommand "ADD_ASSOCIATION"
      IDMWriteValue "ASSOCIATION", CN & ClassName
      IDMWriteValue "DEST_DN", IDMGetEventValue("SRC_DN")
      IDMStatusSuccess "Add event succeeded"
    Else
      IDMStatusError "Add event failed with error code " & ExitCode
    End If
  End If
End Sub
```

Handling a query is similar, except you return INSTANCE items rather than use other commands. Below is an example Query.vbs that searches an external application for a telephone number. It uses a hypothetical tool called appsearch.

```
Sub QUERY
  SearchName = IDMGetEventValue("SEARCH_ATTR_CN")
  If IsEmpty(SearchName) Then
    IDMStatusError "Query: no search value"
  Else
    Command = "appsearch -n " & SearchName
    Results = IDMExecuteIO(Command, Empty)
    If Results(0) = 0 Then
      Phone = Results(1)
      IDMSetCommand "INSTANCE"
      IDMWriteValue "CLASS_NAME", IDMGetEventValue("CLASS_NAME")
      IDMWriteValue "ASSOCIATION", IDMGetEventValue("ASSOCIATION")
      IDMWriteValue "ATTR_Telephone", Phone
      IDMStatusSuccess "Query succeeded"
    Else
      ' Return success with no results
      IDMStatusSuccess "Query succeeded (no matches)"
    End If
  End If
End Sub
```

### Publisher Script Development

Events that occur on the external application are submitted to Identity Manager on the Publisher channel. The Scripting driver periodically polls the external application for events. How this poll detects events is implementation-specific and must be defined by you.

#### Polling for Application Events

The Driver calls Poll.wsf to detect application events. Poll.wsf should be implemented as follows:

1. Use application-provided tools to detect events in your application. (See [Step 2](b8nlv23.html#b8nmxka).)
2. For each event:

   1. Call the IDMPublishInit function to set the appropriate command.
   2. Call IDMPublishValues to set event values.
   3. Call IDMPublish to submit the event to Identity Manager.
3. If there were events, call an IDMStatus function to report the status.

IDMPublishInit takes a command name as its single parameter. Below is a list of valid command names for IDMPublishInit.

*Table 5-23* Command Names

| Command Name | Description |
| ADD | Create an identity. |
| ADD\_ASSOCIATION | Create an association for an identity. |
| DELETE | Remove an identity permanently. |
| MODIFY | Change an identity’s attributes. |
| MODIFY\_ASSOCIATION | Change an identity’s association. |
| MODIFY\_PASSWORD | Change an identity’s password. |
| REMOVE\_ASSOCIATION | Delete an identity’s association. |
| RENAME | Change an identity’s naming attribute. |

Below is an example of a Poll.wsf that checks for a password change. It uses a hypothetical application tool called apppwd.

```
  Results = IDMExecuteIO("apppwd --changes", Empty)
  For I = 1 To UBound(Results)
    ' Entries are in the format "association=password"
    Association = Left(Results(I), InStr(Results(I), "=")-1)
    Password = Mid(Results(I), InStr(Results(I), "=")+1)
    IDMPublishInit "MODIFY_PASSWORD"
    IDMPublishValue "ASSOCIATION", Association
    IDMPublishValue "PASSWORD", Password

    IDMPublish
  Next

  IDMStatusSuccess "Poll succeeded"
```

Events submitted using IDMPublish are processed through your driver’s Publisher channel policies. See the Identity Manager policy guides on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-48/) for more information.

#### Using the Heartbeat Script

Another script executed in the Publisher Channel is Heartbeat.wsf. This script is executed when the Publisher channel is idle for the interval specified in the driver parameters. (You can set the interval to 0 so no heartbeat is issued.) You can use the heartbeat to check the availability of the external system or do “idle state” tasks. The IDMHeartbeatSuccess, IDMHeartbeatWarning, and IDMHeartbeatError subroutines can be used to indicate the result of the heartbeat. Below is an example based on a hypothetical tool called apphealth.

```
  ExitCode = IDMExecute("apphealth")
  If ExitCode = 0 Then
    IDMHeartbeatSuccess "Heartbeat succeeded"
  Else
    IDMHeartbeatError "Heartbeat failed with error code " & ExitCode
  End If
```

The response to the heartbeat is implementation-dependent, and can be defined in policies or in the script itself. You could send a message to auditing using NetIQ Audit. You could store a value in a file, and have Subscriber scripts read the file and call IDMStatusRetry if they find that value in the file.

### Other Scripting Topics

* [Driver Parameters](b8nlv23.html#b8nn0sn)
* [Querying the Identity Vault](b8nlv23.html#b8nn44l)
* [Tracing and Debugging](b8nlv23.html#b8nn85m)

#### Driver Parameters

A driver has values known as driver parameters. The driver parameters are divided into driver settings applicable to the whole driver, and Subscriber and Publisher Settings for their respective channels. The IDMGetDriverParam, IDMGetSubscriberParam, and IDMGetPublisherParam functions can be used to retrieve these values. The table below shows parameters in the default Scripting driver. Other parameters can be added to the driver’s XML Configuration file (see “Managing Identity Manager Drivers” in the NetIQ Identity Manager Administration Guide).

*Table 5-24* Driver Parameters

| Parameter Name | Driver/Channel | Description | Values |
| INSTALL\_PATH | Driver | The installation path of the driver | string value |
| auto-loopback-detection | Driver | Whether to enable automatic loopback detection | true/false |
| script-command | Driver | The command to use to execute scripts | string value |
| script-trace-file | Driver | The file, relative to the driver installation path, to which to write trace messages | string value |
| subscriber-script | Subscriber | The script file for Subscriber events, relative to the driver installation path | string value |
| polling-script | Publisher | The script file that runs when the Publisher polls for application events | string value |
| heartbeat-script | Publisher | The script file that runs when the Publisher checks application status | string value |
| pub-polling-interval | Publisher | The interval in seconds between Publisher polls for application events | number |
| pub-heartbeat-interval | Publisher | The amount of idle time in seconds before a heartbeat event is issued | number |

In the following example, a script retrieves the Publisher polling interval.

```
  PollingInterval = IDMGetPublisherParam("pub-polling-interval")
```

#### Querying the Identity Vault

Scripts might need to retrieve information from the Identity Vault. On the Subscriber channel only, they can do this by issuing a query.

1. Initialize the query with IDMQueryInit.
2. Set query search parameters using functions listed below.

   | Function | Description |
   | IDMQuerySetAssociation(Association) | Sets the association of the object to query. |
   | IDMQuerySetSearchRoot(SearchRoot) | Sets the DN (in slash format) of the object to query. |
   | IDMQueryAddSearchAttr(Name, Value) | Specifies a search condition of the form Name=Value. The query will only return an instance if the named attribute has a value matching Value. |
   | IDMQueryAddReadAttr(Name) | Specifies an attribute whose values will be returned with the instance. |
   | IDMQuerySetReadParent(ReadParent) | Specifies whether the association and DN of the parent of the queried object should be returned (False by default). |
3. Execute the query with IDMQuery.
4. Read the result (instance) using functions listed below.

   Currently query support is limited. It will only return one instance based on the specified association or DN. (If both association and DN are specified, association is used.) The functions below allow you to retrieve information from the instance.

   | Function | Description |
   | IDMGetQueryInstanceAssociation | Returns the association of the instance. |
   | IDMGetQueryInstanceDN | Returns the DN of the instance (in slash format). |
   | IDMGetQueryInstanceClass | Returns the class name of the instance. |
   | IDMGetQueryInstanceParentAssociation | Returns the association of the parent of the instance (if requested). |
   | IDMGetQueryInstanceParentDN | Returns the DN of the parent of the instance (if requested). |
   | IDMGetQueryInstanceAttrNames | Returns an array containing the names of the attributes retrieved for the instance. Returns Empty if no attributes were retrieved. |
   | IDMGetQueryInstanceAttrCount | Returns the number of attributes retrieved for the instance. |
   | IDMGetQueryInstanceAttrValues(AttrName) | Returns an array of values for the attribute AttrName. Returns Empty if no values are available. |
   | IDMGetQueryInstanceAttrValue(AttrName) | Returns a string value for the attribute AttrName. If multiple values are available, the first one is returned. Returns Empty if no values are available. |

The following is an example of a query that retrieves an object’s address and postal code.

```
  IDMQueryInit
  IDMQuerySetAssociation IDMGetEventValue("ASSOCIATION")
  IDMQueryAddReadAttr "SA"          ' Street Address
  IDMQueryAddReadAttr "Postal Code"

  If IDMQuery Then
    Address = IDMQueryGetInstanceAttrValue("SA")
    ZIPCode = IDMQueryGetInstanceAttrValue("Postal Code")
    ' ... etc. ...
  End If
```

#### Tracing and Debugging

The IDMTrace function allows you to write a message to the Script Trace File specified in the Driver Parameters. Tracing is useful for script debugging and auditing.

```
   IDMTrace "Trace message"
```

When developing scripts, you might need to do some debugging to track down problems. The following list indicates some facilities for debugging.

* The Driver traces activity to its Trace file (logs\trace.log by default). The trace level setting in conf\wsdrv.conf controls how much debugging is written to the log.

  | Trace Level | Description |
  | 0 | No debugging. |
  | 1-3 | Identity Manager messages. Higher trace levels provide more detail. |
  | 4 | Previous level plus Remote Loader, driver, driver shim, and Driver connection messages. |
  | 5-7 | Previous level plus Change Log and loopback messages. Higher trace levels provide more detail. |
  | 8 | Previous level plus Driver status log, Driver parameters, Driver command line, Driver security, Driver Web server, Driver schema, Driver encryption, Driver SOAP API, and Driver include/exclude file messages. |
  | 9 | Previous level plus low-level networking and operating system messages. |
  | 10 | Previous level plus maximum low-level program details. |

  The trace level is set using the -trace option in wsdrv.conf, for example. -trace 9.

  You can view the trace file through a Web browser:

  1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
  2. Authenticate by using any username and the password that you specified as the Remote Loader password.
  3. Click Trace.
* The IDMTrace function described above writes output to the trace file specified in the Driver Parameters (logs\script-trace.log by default).
* The eDirectory tool DSTrace can be used to monitor Identity Manager activity. Set the tracing level for the Driver in iManager. DSTrace shows the XML documents being submitted to the Driver for events, and how Policies are evaluated. It also shows the status and message for each event.
* The Status Log is written to logs\dirxml.log. It shows a summary of the events that have been recorded on the Subscriber and Publisher channels.

  You can view the Status Log through a Web browser:

  1. Use a Web browser to access the driver shim at https://driver-address:8091. Substitute the DNS name or IP address of your driver for driver-address.
  2. Authenticate by using any username and the password that you specified as the Remote Loader password.
  3. Click Status.

Although it is best to run the driver as a service in production environments, you can run wsdriver.exe as a standard program. When you do so, a console window displays trace messages (see above) for the driver. Also, text written to standard output from scripts (such as using WScript.Echo in VBScript) is displayed in this window.

VBScript programs can be debugged using programs such as Microsoft Visual Studio and Microsoft Script Debugger. Change the Script Command driver parameter to use the //x option: cscript //nologo //x. When the driver shim executes a script, you are prompted to debug the script execution.

## 5.8.3 Deployment

The Scripting driver is installed by using a setup program. See [Installing the Windows Scripting Driver](b8mow8v.html) for information on installing the default driver.

### Deploying a Custom Driver

To deploy your custom driver, the end user should first run the Windows Scripting driver installation program provided by the installation media (see [Installing the Windows Scripting Driver](b8mow8v.html) for more information.) This program installs core files needed by the driver. Then, your custom driver files can be deployed in any convenient way, whether through an installation program or even simply an archive file. The table below shows the directory structure below the installation directory and what files are installed.

*Table 5-25* Directory Structure and Files

| Directory | Description | Required Files |
| bin\ | Location of executable programs | EventReader.exe  idmevent.exe  wsdriver.exe |
| changelog\ | Used for Publisher event processing | None |
| conf\ | Location of the driver shim configuration file | wsdrv.conf (customized) |
| keys\ | Location of security key files | None |
| logs\ | Location of log files | None |
| loopback\ | Used for automatic loopback detection | None |
| rules\ | Location of Driver configuration file | Scripting.xml (customized) |
| schema\ | Location of schema files | schema.def (customized) |
| scripts\ | Location of script files | Those required by your Driver (customized) |

If you are using an installation program, you can obtain the driver’s installation path from the following registry value:

```
     HKEY_LOCAL_MACHINE\SOFTWARE\Novell\Windows Script Driver\Path
```

Or for the x86 driver running an x64 version of Windows, use the path from the following registry value:

```
     HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Novell
     \Windows Script Driver\Path
```

The formats of wsdrv.conf and schema.def can be viewed in [The Driver Shim Configuration File](b8mqqe6.html) and [The Connected System Schema File](b8n6pr6.html).

If SSL encryption is desired for communication between the driver shim and Identity Manager engine, a certificate must be retrieved from the Identity Vault. Run the following command and follow the prompts to retrieve the certificate:

wsdriver.exe -s

The certificate will be stored in the keys\ directory. You must have LDAP with SSL available for the Metadirectory. When making an installation program for deployment, you might want to include this command as part of the installation:

To ensure that only authorized systems access the Metadirectory, a Driver Object password and Remote Loader password are used. Run the following command and enter the passwords at the prompts:

wsdriver.exe -sp

This action also can be incorporated into an installation program.

You should run a Scripting driver as a service. To the install the service, run the following command or include it as part of an installation program:

wsdriver.exe -installService

The service, which can then be run from the Services applet, can be removed as follows:

wsdriver.exe -removeService

You should distribute the XML configuration file that contains parameters and policies your driver needs. The user can then select it when installing your driver.
