# D.15 EJS Messages

Messages beginning with EJS are issued by Event Journal Services.

EJS0001E No Platform object FDN was provided with the Platform Receiver request.

Explanation:
The Platform object FDN was missing from the Platform Receiver request. The Platform object FDN is required for every Platform Receiver request and is used to identify the corresponding Platform object in eDirectory.

Possible Cause:
The security certificate was not found by the Platform Receiver, or an invalid security certificate is installed.

Action:
Install a security certificate on the platform.

EJS0002E Unable to create an instance of the string handler.

Explanation:
An instance of the string handler object could not be created.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0003E Unable to create an instance of the memory manager.

Explanation:
An instance of the memory manager object could not be created.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0004E Unable to create an instance of the ASAM directory interface, direrr= DirectoryError (DirectoryErrorText).

Explanation:
An instance of the ASAM directory interface object could not be created.

Possible Cause:
There are several possible causes of this error:

An invalid ASAM Master User or ASAM Master User Password is specified in the Driver object parameters.

An invalid DNS name or IP address, or port number is specified for the LDAP Host and Port in the Driver object parameters.

The LDAP host is down or not responding to requests.

Action:
Ensure that the correct ASAM Master User Password is specified in the Driver object parameters.

Ensure that the correct network address and port is specified for the LDAP Host and Port in the Driver object parameters.

Ensure that the host running the LDAP server is functioning correctly.

EJS0005E Directory Search object DirectorySearchObjectFDN not found with scope= DirectorySearchScopeLevel.

Explanation:
The object was not found using the specified directory search scope. The scope can be one of the following values: DirectoryScopeBase, DirectoryScopeOneLevel, DirectoryScopeSubtree.

This message is accompanied by messages EJS0007W and EJS0008W.

Possible Cause:
The search did not find any results that matched the search criteria.

Action:
No action is required.

EJS0006E Directory search error for object DirectorySearchObjectFDN, direrr= DirectoryError (DirectoryErrorText), numRows= DirectoryEntriesReturned, scope= DirectorySearchScopeLevel.

Explanation:
An error occurred while searching for the specified object. This message is accompanied by messages EJS0007W and EJS0008W.

Possible Cause:
See the direrr value to determine the cause of the error.

Action:
Correct the cause of the error and retry the Platform Receiver request.

EJS0007W Directory search requested attributes=DirectoryAttributes.

Explanation:
This message shows the attributes that were requested for the search. This message is accompanied by messages EJS0005E, or EJS0006E, and EJS0008W.

Action:
No action is required.

EJS0008W Directory search for values= DirectorySearchValues.

Explanation:
This message shows the matching criteria for the search request.

Action:
No action is required.

EJS0009E Directory modification error for object DirectoryObjectFDN, direrr= DirectoryError ( DirectoryErrorText), actions= ActionsToPerform.

Explanation:
An error occurred while trying to modify an attribute value for the specified object. The displayed actions are the actions and attributes that were to be modified.

Possible Cause:
See the direrr value to determine the cause of the error.

Action:
Correct the cause of the error and retry the Platform Receiver request.

EJS0010E Directory modification error for object DirectoryObjectFDN, direrr= DirectoryError ( DirectoryErrorText).

Explanation:
An error occurred while trying to modify an attribute value for the specified object.

Possible Cause:
See the direrr value to determine the cause of the error.

Action:
Correct the cause of the error and retry the Platform Receiver request.

EJS0011E Unable to create or obtain the Event Journal Services Platform item.

Explanation:
An instance of the Event Journal Service item could not be created.

Possible Cause:
There are several possible causes of this error:

There might not be enough free memory available on the system.

A string handler interface could not be created (look for message EJS0002E).

A memory manager interface could not be created (look for message EJS0003E).

An ASAM directory interface object could not be created (look for message EJS004E).

The Platform FDN provided by the Platform Receiver is invalid (look for message EJS0031E).

Action:
Ensure that there is adequate free memory available. Perform the actions for any additional messages that were issued.

EJS0012W Event EventType for object DirectoryObjectFDN could not be processed.

Explanation:
An event for the specified Platform FDN could not be processed.

Possible Cause:
Required information needed to process the event was not found. If this was a change password event, the Platform object does not have the Permit Password Replication attribute enabled.

Action:
Look for other messages beginning with the EJS prefix to determine what information that is needed to process this event is missing.

EJS0013W Unable to obtain UID/GID information for object DirectoryObjectFDN.

Explanation:
No UID or GID information exists for the specified object.

Possible Cause:
The specified object has no corresponding UID/GID object in the UID/GID Set for the platform, or the UID/GID object contains no value for the UIDGIDNumber attribute.

Action:
Ensure that a UID/GID Set is defined for the Platform Set. Run a Trawl to create the appropriate UID/GID objects.

EJS0014E Unable to create a directory search request.

Explanation:
A directory search request object could not be created.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0015E Unable to delete attribute DirectoryAttribute for object DirectoryObjectFDN.

Explanation:
The attribute could not be deleted for the specified object.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0016E Unable to add attribute DirectoryAttribute with value AttributeValue for object DirectoryObjectFDN.

Explanation:
The attribute could not be added for the specified object.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0017E Unable to create a directory modify attributes request.

Explanation:
A directory modification request object could not be created.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0018E Unable to delete value AttributeValue for attribute DirectoryAttribute for object DirectoryObjectFDN.

Explanation:
The attribute value could not be deleted for the specified object.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0019E Unable to replace attribute DirectoryAttribute value OldAttributeValue with new value NewAttributeValue for object DirectoryObjectFDN.

Explanation:
The attribute value could not be replaced by the new value for the specified object.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0020E Unable to obtain the CN of the Platform object DirectoryObjectFDN.

Explanation:
No common name attribute exists for the specified object.

Possible Cause:
This situation should not occur under normal circumstances.

Action:
Collect diagnostic information and contact Support.

EJS0021E No Census object was found for the Platform object DirectoryObjectFDN.

Explanation:
No corresponding Census object was found for the specified object.

Possible Cause:
This situation should not occur under normal circumstances.

Action:
Collect diagnostic information and contact Support.

EJS0022E Unable to parse the journal value for object DirectoryObjectFDN.

Explanation:
The events could not be parsed for the specified object.

Possible Cause:
This situation should not occur under normal circumstances.

Action:
Collect diagnostic information and contact Support.

EJS0023I No UID/GID number was found for object DirectoryObjectFDN.

Explanation:
The UID/GID number attribute was not found for the specified object.

Possible Cause:
The Platform Set that contains the associated user or group object might not have a UID/GID Set defined.

Action:
Ensure that the Platform Set that contains the associated User or Group object has a UID/GID Set defined.

EJS0024W No Platform Receiver attribute list was loaded for object class DirectoryObjectClass.

Explanation:
The Platform Receiver attribute list was not loaded for the specified object class.

Possible Cause:
No attributes that are to be sent to the Platform Receivers are defined for the specified object type.

The LDAP server is down or not responding properly.

Action:
Add the appropriate attributes to the Subscriber filter.

EJS0026W The password could not be retrieved for object DirectoryObjectFDN.

Explanation:
The object's password could not be retrieved.

Possible Cause:
The object might not have the old password set in ePassword.

Action:
None. Normal processing continues.

EJS0029E ElementTagName SOAP element could not be created in the Platform response document.

Explanation:
The specified SOAP structure element tag name could not be created.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0031E Invalid Platform FDN platformFDN was specified by the Platform Receiver.

Explanation:
The Platform FDN provided in the Platform Receiver request was invalid.

Possible Cause:
The object referenced by the FDN does not exist in eDirectory.

Action:
Ensure that the correct security certificate has been installed on the platform. Also ensure that the Platform object has been created in eDirectory.

EJS0032E Unable to search for pending events for Platform platformFDN.

Explanation:
The search criteria was empty for the search request during a Polling or Persistent Mode request. The search for events is not performed.

Possible Cause:
This situation should not occur under normal circumstances.

Action:
Collect diagnostic information and contact Support.

EJS0033I Platform PlatformName returned ReturnCode for event EventType for object DirectoryObjectFDN.

Explanation:
The Platform Receiver running on the specified platform returned the return code after processing the event for the specified object. The possible return codes values are:

prrcSuccess - The event was successfully processed by the Platform Receiver.

prrcIgnored - The event was ignored by the Platform Receiver.

prrcExcluded - The event was excluded by the Platform Receiver.

prrcWarning - The event was processed by the Platform Receiver, but all necessary actions were not completed.

prrcError - The event was not processed successfully by the Platform Receiver.

Action:
No action is required.

EJS0034I Processed event EventType for Platform PlatformName was removed for object DirectoryObjectFDN.

Explanation:
The event was successfully processed by the specified platform. The event is now being removed for this platform.

Action:
No action is required.

EJS0035I Platform PlatformName added association PlatformAssociation for object DirectoryObjectFDN.

Explanation:
The Platform Receiver assigned the specified association name to the directory object.

Action:
No action is required.

EJS0037I Platform PlatformName has NumberOfEvents events pending.

Explanation:
The platform has the specified number of pending events that are waiting to be processed by the Platform Receiver.

Action:
No action is required.

EJS0038W A Platform Receiver is already active for Platform platformName.

Explanation:
A Platform Receiver made a request to the Event Journal Services component of the Core Driver, but a Platform Receiver is already active for the specified platform. Only one Platform Receiver can be active at a time for a Platform object.

Possible Cause:
Multiple Platform Receivers are attempting requests for the same Platform object.

It is also possible that a Platform Receiver has abended and left its connection token active with Event Journal Services.

Action:
Run only one instance of the Platform Receiver at a time for each Platform object.

If a Platform Receiver abended, and you are trying to start a new one, allow several minutes for Event Journal Services to release control to a new instance of the Platform Receiver.

EJS0041I Searching for objects with pending events for Platform platformName.

Explanation:
The Event Journal Services component of the Core Driver is searching for events that are pending for the specified platform.

Possible Cause:
This message is in response to a get next event request from the Platform Receiver.

Action:
None.

EJS0042I Pending event search for Platform platformName returned numObjects objects.

Explanation:
A search for pending events for the specified platform returned the displayed number of user or group objects that have one or more pending events.

Possible Cause:
This message is in response to a get next event request from the Platform Receiver.

Action:
None

EJS0043I Ready to send events to Platform platformName.

Explanation:
The Event Journal Services component of the Core Driver has finished processing the list of objects with pending events. Event Journal Services now begins sending these events to the Platform Receiver running on the specified platform.

Possible Cause:
This message is in response to a get next event request from the Platform Receiver.

Action:
None.

EJS0044I Removing all error events for Platform platformName.

Explanation:
All error events for the specified platform are being removed.

Possible Cause:
A Full Sync operation being performed by a Platform Receiver

An administrator is clearing the events using the Web interface.

Action:
None.

EJS0045I Re-sending all error events for Platform platformName.

Explanation:
All error events for the specified Platform are being re-sent to the Platform Receiver for retry.

Possible Cause:
This action is the result of an administrator using the Web interface to specify that all error events for the platform be re-sent to the Platform Receiver.

Action:
None.

EJS0046I Removing event eventType for object objectCN.

Explanation:
An error event is being removed for the specified object.

Possible Cause:
This can be in response to a request to remove all errors for a platform, or a request to remove the error for the individual object that is specified.

Action:
None.

EJS0047I Re-sending error event eventType for object objectCN.

Explanation:
An error event is being re-sent to the Platform Receiver for the specified object.

Possible Cause:
This can be in response to a request to re-send all errors for a platform or a request to re-send the error for the individual object that is specified.

Action:
None.

EJS0048I Platform Receiver platformName version is version build level build.

Explanation:
The Platform Receiver is running the specified version and build level code.

Action:
None.

EJS0049E Event event for object objectCN was changed to an error state.

Explanation:
The event for the specified object could not be processed. The event has been set to an internal error state so that it will not be processed again until an administrator re-sends the error events for the platform.

Possible Cause:
The Platform Receiver could not process the event and returned an error to the Core Driver.

The Core Driver was trying to process the event, but it could not obtain the object's password from ePassword.

Action:
An Administrator can use the Web interface to re-send all error events to the platform.

EJS0050E Unable to open temporary file fileName for event processing (error= errno, reason= reason).

Explanation:
The Event Journal Services component of the Core Driver could not open the specified temporary file that is needed for processing of queued events.

Possible Cause:
The path might be invalid.

The Core Driver might not have the proper permissions to the file system.

The file system might be full.

Action:
Make sure the file path exists.

Make sure the Core Driver has read/write permission to the path.

Make sure enough space exists on the volume.

EJS0051E Unable to obtain a directory connection.

Explanation:
A connection could not be established to eDirectory.

Possible Cause:
The replica could be down or not responding.

Action:
Try the action again.

EJS0052E Unable to create temporary work files.

Explanation:
The Event Journal Services component of the Core Driver could not create any temporary work files.

Possible Cause:
The path might be invalid.

The Core Driver might not have the proper permissions to the file system.

The file system might be full.

Action:
Make sure the file path exists.

Make sure the Core Driver has read/write permission to the path.

Make sure enough space exists on the volume.

EJS0053I Now attempting to process event eventType for object objectDN.

Explanation:
The Event Journal Services component of the Core Driver is processing the event for the specified object.

Action:
None.

EJS0054E Unable to add attribute attributeName value attributeValue for object objectCN.

Explanation:
The attribute value could not be added for the specified object.

Possible Cause:
There might not be enough free memory available on the system.

Action:
Ensure that there is adequate free memory available.

EJS0055E Populate event was generated for object objectCN on platform platformName.

Explanation:
A populate event was generated for the specified object for the single platform.

Possible Cause:
The generation of the event is usually in response to a Web request to repopulate the user on the desired platforms.

Action:
None.

EJS0056I Updated event timestamps for platform PlatformName.

Explanation:
One or more attributes used for tracking event processing have been updated for the platform object.

Action:
None.

EJS0057I Removing error event eventType for object objectCN.

Explanation:
An error event is being removed for the specified object.

Possible Cause:
This can be in response to a request to remove all errors for a platform, or a request to remove the error for the individual object that is specified.

Action:
None.

EJS0058E Unable to create ASAM Directory Interface item.

Explanation:
The Event Journal Services component of the Core Driver could not create a directory interface object.

Possible Cause:
The LDAP server is down.

The server is low on memory.

Action:
Retry the attempted operation.

EJS0059E Ignoring event for objectDN because of error status.

Explanation:
The pending event for the specified object is ignored because an error state currently exists for the object.

Possible Cause:
There are several possible causes for this error.

The platform returned an error while attempting to process the event.

If the event was for a User object, the eUser password was not available, and the platform's permit password replication setting is YES, an error state is returned for that User object.

Invalid event data.

Action:
Check the platform logs to see if script errors are being reported for that object.

Check for platform errors using the Web interface, and re-send the error events to the platform.

Use the Web interface to clear error events for the platform if needed.

EJS0060W Unable to obtain the alternate name of the Platform object DirectoryObjectFDN.

Explanation:
No Alternate Naming Attribute exists for the specified object.

Possible Cause:
An Alternate Naming Attribute was specified for the Platform Set, but no alternate name has been specified for this user/group.

An Alternate Naming Attribute was specified for the Platform Set, but that attribute has not been included in the Subscriber filter.

Action:
Specify an alternate name for the object.
