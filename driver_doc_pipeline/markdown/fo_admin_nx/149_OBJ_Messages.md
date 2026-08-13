# D.20 OBJ Messages

Messages beginning with OBJ are issued by Object Services.

OBJ001I Processing Users In search\_object.

Explanation:
The Trawl is detecting all users specified by search\_object and checking those users to determine if updates are needed in the Census.

Action:
None. Informational only.

OBJ002I Checking for deleted users.

Explanation:
The Trawl is looking for Enterprise Users that were not found during the processing of users specified by the Search objects. Any Enterprise Users whose corresponding User object was not found are removed from the Census.

Action:
None. Informational only.

OBJ004I Processing groups in search\_object.

Explanation:
The Trawl is detecting all groups specified by search\_object and checking those groups to determine if updates are needed in the Census.

Action:
None. Informational only.

OBJ005I Checking for deleted groups.

Explanation:
The Trawl is looking for Enterprise Groups that were not found during the processing of groups specified by the Search objects. Any Enterprise Group whose corresponding group object was not found is removed from the Census.

Action:
None. Informational only.

OBJ007I Starting Trawl.

Explanation:
A Census Trawl is starting.

Action:
None. Informational only.

OBJ008I Phase phase\_number: Processing Users.

Explanation:
The Census Trawl is verifying information in the Census pertaining to users.

Action:
None. Informational only.

OBJ009I Phase phase\_number: Processing Groups.

Explanation:
The Census Trawl is verifying information in the Census pertaining to groups.

Action:
None. Informational only.

OBJ010I Trawl complete.

Explanation:
A Census Trawl is ending.

Action:
None. Informational only.

OBJ013W No valid Search objects found for Census\_or\_Platform\_set.

Explanation:
Census\_or\_Platform\_set has no Search objects defined.

Possible Cause:
Configuration of the product might not be complete.

Action:
Define Search objects for the identified component.

OBJ014W No Platforms found in Platform\_set.

Explanation:
Platform Set Platform\_set has no platforms defined for it.

Possible Cause:
Configuration of the Platform Set might not be completed.

Action:
Add desired platforms to the Platform Set.

OBJ015I No UID/GID Sets found.

Explanation:
No UID/GID Sets were found.

Possible Cause:
No UID/GID Set has been created.

Action:
If Linux/UNIX Platforms are to be controlled, define needed UID/GID Sets.

OBJ016W Search object search\_object\_name does not have a value for attribute\_name. It is ignored.

Explanation:
A Search object must have a value for attribute\_name in order to be processed. search\_object\_name does not have this value.

Possible Cause:
The Search object might have been edited manually.

Action:
Determine the intended values for the Search object and set the values.

OBJ017E UID/GID Set UID\_GID\_set\_name, specified for Platform Set Platform\_set\_name, was not found.

Explanation:
The UID/GID Set named UID\_GID\_set\_name could not be found. It is referenced by Platform Set Platform\_set\_name. Identity Provisioning cannot function properly on any Linux/UNIX platforms defined for the Platform Set named Platform\_set\_name.

Possible Cause:
The UID/GID Set container named UID\_GID\_set\_name was manually removed from eDirectory.

Action:
Restore the UID/GID container named UID\_GID\_set\_name from backup.

OBJ018W No Platform Sets found.

Explanation:
No Platform Sets were found. Account information cannot be exported to any platforms.

Possible Cause:
Configuration of the product might not have been completed.

Action:
Define Platform Sets as needed for your installation.

OBJ019I UID/GID number assigned to user in UID/GID Set uidgid\_set\_name.

Explanation:
UID/GID number number has been assigned to user user in UID/GID Set uidgid\_set\_name. This is the ID that is used for Linux/UNIX platforms in Platform Sets that use UID/GID Set uidgid\_set\_name.

Action:
None. Informational only.

OBJ020I Exception resolved for exception\_object.

Explanation:
The condition that caused the creation of Exception object exception\_object has been corrected. The Exception object has been removed.

Action:
None. Informational only.

OBJ021I Added user\_or\_group\_name to Platform Set Platform\_set\_name.

Explanation:
A user or group named user\_or\_group\_name has been added to the Platform Set specified by Platform\_set\_name.

Action:
None. Informational only.

OBJ022I Enterprise object object\_name removed from Census.

Explanation:
The Enterprise object named object\_name was removed from the Census.

Possible Cause:
The user, group, or alias represented by the Enterprise object named object\_name was deleted from the directory, is disabled, or is no longer included by the Search objects.

Action:
None. Informational only.

OBJ023I Enterprise object object\_name renamed to new\_object\_name.

Explanation:
The Enterprise object named object\_name was renamed to new\_object\_name.

Possible Cause:
The user, group, or alias represented by object\_name was renamed to new\_object\_name.

Action:
None. Informational only.

OBJ024I Created Exception object for object\_dn.

Explanation:
A group or user could not be processed.

Possible Cause:
The cn of the Group or User object is not unique among all the users and groups that are represented in the Census.

Two or more objects in the directory have the same GUID.

Action:
Examine the contents of the Exception object to determine the reason it was created.

If the Exception object is because of a create problem, a naming conflict has occurred. Rename the user or group so its name is unique.

If the Exception object is because of a duplicate GUID, look in the operational log for a listing of the objects that use the same GUID, and see TID 10064771 for information on resolving GUID conflicts.

OBJ025I User user\_name, attribute(s) attribute\_list modified in Census.

Explanation:
Information for user user\_name was updated in the Census.

Action:
None. Informational only.

OBJ026I Group group\_name, attribute(s) attribute\_list modified in Census.

Explanation:
Information for group group\_name was updated in the Census.

Action:
None. Informational only.

OBJ027I User user\_name added to Census.

Explanation:
User user\_name was detected and added to the Census.

Possible Cause:
A user was added to eDirectory, or Search objects were expanded to include a user that was not previously in the Census.

Action:
None. Informational only.

OBJ028I Group group\_name added to Census.

Explanation:
Group group\_name was detected and added to the Census.

Possible Cause:
A group was added to eDirectory, or Search objects were expanded to include a group that was not previously in the Census.

Action:
None. Informational only.

OBJ030E Error error\_id authenticating to eDirectory as username.

Explanation:
The Core Driver is unable to authenticate to eDirectory.

Possible Cause:
Incorrect settings for LDAP Host and Port, ASAM Master User, or ASAM Master User Password in the Driver object configuration parameters.

Action:
Check the configuration parameters.

OBJ031E Error error\_id renaming object dn to cn.

Explanation:
The eDirectory error error\_id occurred while trying to rename object dn to cn.

Action:
See the eDirectory documentation for error error\_id.

OBJ032E Out of memory.

Explanation:
The Core Driver ran out of memory.

Possible Cause:
The machine on which the Core Driver runs does not have enough memory to allow operation, or the swap space is not large enough.

Action:
Increase the amount of memory available to the process.

OBJ033E Error error\_id retrieving from dn.

Explanation:
The eDirectory error error\_id occurred while trying to retrieve from dn.

Action:
See the eDirectory documentation for error error\_id.

OBJ034E Error error\_id retrieving attributes for object.

Explanation:
The eDirectory error error\_id occurred while retrieving attributes for object object.

Action:
See the eDirectory documentation for error error\_id.

OBJ035E Error error\_id modifying attributes for object.

Explanation:
The eDirectory error error\_id occurred while trying to modify object.

Possible Cause:
Insufficient rights to the object.

Action:
See the eDirectory documentation for error error\_id.

OBJ036E Error error\_id searching for object object.

Explanation:
The eDirectory error error\_id occurred while trying to determine if object exists.

Action:
See the eDirectory documentation for error error\_id.

OBJ037E Error error\_id creating object object.

Explanation:
The eDirectory error error\_id occurred while trying to create object.

Possible Cause:
Incorrect ASAM System Container setting in the Driver object configuration, or insufficient rights to this container.

Action:
See the eDirectory documentation for error error\_id.

OBJ038E Error error\_id removing object object.

Explanation:
The eDirectory error error\_id occurred while trying to remove object.

Action:
See the eDirectory documentation for error error\_id.

OBJ039E Unexpected error processing information retrieved from the directory in function function\_name.

Explanation:
An unexpected error has occurred during processing.

Possible Cause:
Unknown.

Action:
Turn on debugging information using the command line parameter -d asam\_objectserv,dom, and forward the resulting log to Support.

OBJ040E Unable to load request document.

Explanation:
An eDirectory event could not be processed.

Possible Cause:
Internal error.

Action:
Turn on debugging information using the command line parameter -d asam\_objectserv,dom, and forward the resulting log to Support.

OBJ041E Unable to determine DN for the ASAM System Container.

Explanation:
The ASAM System container cannot be identified.

Possible Cause:
The Driver object configuration parameters do not contain a valid value for the ASAM System Container parameter.

Action:
Correct the ASAM System Container parameter.

OBJ042E Unable to process some users in search\_object.

Explanation:
Appropriate actions for some of the users in search\_object might not have been taken because of errors that occurred.

Action:
See other errors reported during the processing of search\_object for specific troubleshooting information.

OBJ043E Unable to process some groups in search\_object.

Explanation:
Appropriate actions for some of the groups in search\_object might not have been taken because of errors that occurred.

Action:
See other errors reported during the processing of search\_object for specific troubleshooting information.

OBJ044E Unable to process some aliases in search\_object.

Explanation:
The Core Driver was unable to process an Alias object.

Action:
See the log for more information about the specific error.

OBJ046I Updated attribute attribute\_name in object object.

Explanation:
An out-of-date attribute of an Enterprise User or Group object was detected. The attribute was updated.

Possible Cause:
A Core Driver might not be running or might not be functioning properly.

A new user was added to the Census, and a group to which it belongs was updated accordingly.

A new group was added to the Census, and a user in that group was updated accordingly.

Action:
Ensure proper operation of all Core Drivers.

OBJ047I Removed object\_cn from Platform Set Platform\_set.

Explanation:
object\_cn was removed from Platform Set Platform\_set.

Possible Cause:
The user or group is no longer included in the Search objects defined for the Platform Set.

Action:
None. Informational only.

OBJ051E Duplicate GUID found among the listed objects: dn\_list.

Explanation:
Multiple objects exist in the tree with the same GUID.

A list of the objects having duplicate GUIDs is produced in the log.

Action:
As described in TID 10064771, duplicate GUIDs can only be fixed by deleting all but one of the objects and re-creating them. An eDirectory patch is available to prevent multiple GUIDs from being generated in the future. For a complete explanation, see TID 10064771.

OBJ052E Duplicate ASAM-inputGUID found among the listed objects: dn\_list.

Explanation:
Multiple objects exist in the tree with the same GUID.

A list of the objects having duplicate GUIDs is produced in the log.

Action:
As described in TID 10064771, duplicate GUIDs can only be fixed by deleting all but one of the objects and re-creating them. An eDirectory patch is available to prevent multiple GUIDs from being generated in the future. For a complete explanation, see TID 10064771.

OBJ053I Created events of type event\_type for object.

Explanation:
A change in the User or Group object was detected. Affected platforms are notified.

Action:
None. Informational only.

OBJ055E UID/GID Set set\_name was not found.

Explanation:
When assigning a UID/GID for an eUser or eGroup, the requested UID/GID Set could not be found.

Possible Cause:
A UID/GID Set container was manually removed from eDirectory.

Action:
Restore the UID/GID container from backup.

OBJ056E Unable to retrieve object object\_dn referenced by alias alias\_dn.

Explanation:
The object referenced by an alias could not be found.

Possible Cause:
An Alias object refers to a user or group to which the ASAM Master User has insufficient rights.

Action:
Grant necessary rights to the ASAM Master User.

OBJ057E Unable to retrieve attribute attribute\_name from object\_dn.

Explanation:
An attribute needed for processing could not be retrieved.

Possible Cause:
The ASAM Master User does not have sufficient rights.

Action:
Ensure that the ASAM Master User has the necessary rights.

OBJ058E Duplicate UID/GID number uidgid\_number found in both object1 and object2.

Explanation:
Duplicate UID/GID numbers have been discovered. A UID/GID number is used on Linux/UNIX systems to uniquely identify an account or a group. Duplicate UID/GID numbers can indicate that an unintended user has access to Linux/UNIX resources, such as files.

Possible Cause:
Partial restoration of the ASAM System container could result in duplicate UID/GID numbers.

Action:
Determine which user or group should correspond to the associated UID/GID. Manually remove the ASAM-uidgidAssociation value for any other users or groups that are assigned that same number. A new UID/GID will be assigned during the next Trawl for those that have been deleted.

OBJ059E Cannot remove Platform Set Platform\_set\_name. It has associated Platform objects.

Explanation:
A Platform Set has been marked for removal, but it cannot be removed. All platforms must be removed from it first.

Possible Cause:
Platforms were added to a Platform Set that had been marked for removal.

Action:
Remove all platforms from the Platform Set.

OBJ060I Removed Platform Set Platform\_set.

Explanation:
The Platform Set named Platform\_set was removed.

Possible Cause:
The Platform Set was marked for deletion using the Web interface.

Action:
None. Informational only.

OBJ061E Cannot remove UID/GID Set uidgid\_set\_name. It is used by a Platform Set.

Explanation:
A UID/GID Set has been marked for removal, but it cannot be removed. All Platform Sets using the UID/GID Set must be removed first.

Action:
Remove all Platform Sets that use the UID/GID Set.

OBJ062I Removed UID/GID Set uidgid\_set.

Explanation:
The UID/GID Set named uidgid\_set was removed.

Possible Cause:
The UID/GID Set was marked for deletion using the Web interface.

Action:
None. Informational only.

OBJ064W Error error\_id setting LDAP time-out.

Explanation:
An error occurred while trying to use the LDAP Time-Out value.

Action:
See the eDirectory documentation for error error\_id.

OBJ065E Platform Set set\_name not found in directory.

Explanation:
An error occurred while looking up information about the Platform Set named set\_name.

Action:
Gather diagnostic information and contact Support.

OBJ066E Unable to recognize object type of Search object search\_object\_name.

Explanation:
The Search object has as its input reference the dn of an unsupported object type.

Possible Cause:
An incorrect object is specified as the input reference for a Search object.

Action:
Remove the invalid Search object and recreate it using the correct input reference.

OBJ069E Skipping checks for deleted users because of errors during processing of users.

Explanation:
Deleted users are detected during a Trawl when processing of all users has completed. If an error prevents the recognition of all users that should be in the Census, then no users are deleted.

Possible Cause:
Time-outs prevented the detection of all users defined by the Search objects, or a Search object was invalid.

Action:
Check the operational log for errors and determine the actions required to resolve those errors.

OBJ070E Skipping checks for deleted groups because of errors during processing of groups.

Explanation:
Deleted groups are detected during a Trawl when processing of all groups has completed. If an error prevents the recognition of all groups that should be in the Census, then no groups are deleted.

Possible Cause:
Time-outs prevented the detection of all groups defined by the Search objects, or a Search object was invalid.

Action:
Check the operational log for errors and determine the actions required to resolve those errors.

OBJ072E Unrecognized object class for object dn in function\_name.

Explanation:
The Core Driver was unable to determine the object class for dn.

Possible Cause:
The object denoted by dn is an object whose class is not supported.

Action:
Ensure that dn exists and is spelled correctly. Inspect the object denoted by dn to determine whether its object class is supported. If so, contact Support. If not, you cannot manage this object.

OBJ073E Cannot handle object class internal\_objectclass\_identifier for object dn in function\_name.

Explanation:
The Core Driver was unable to process the object class denoted by internal\_objectclass\_identifier for the object given by dn. The problem occurred in the function named function\_name.

Possible Cause:
The object denoted by internal\_objectclass\_identifier has an object class that is not supported for the attempted purpose.

Action:
Ensure that internal\_objectclass\_identifier exists and is spelled correctly. Inspect the object denoted by internal\_objectclass\_identifier to determine whether its object class is supported. If so, contact Support. If not, you cannot manage this object.

OBJ074E Cannot determine Platform Set for dn.

Explanation:
The dn of the Platform object dn could not be parsed to determine the Platform Set name.

Possible Cause:
Internal error.

Action:
Gather diagnostic information and contact Support.

OBJ075I Trawl aborted because of user request.

Explanation:
The Trawl was aborted because of a user request for it to stop.

Possible Cause:
An administrator used the Web interface to stop the Trawl.

The Core Driver was shut down.

Action:
None. Informational only.

OBJ076I Deleting Platform Set set\_name.

Explanation:
The container for Platform Set set\_name and all references to it are being removed. This operation can take some time, depending on the number of users and groups that are managed.

Possible Cause:
The Platform Set set\_name was marked for deletion using the Web interface.

Action:
None.

OBJ077I Deleting UID/GID Set set\_name.

Explanation:
The container for UID/GID Set set\_name and all references to it are being removed. This operation can take some time, depending on the number of users and groups that are managed.

Possible Cause:
The UID/GID Set set\_name was marked for deletion using the Web interface.

Action:
None.

OBJ079E Unable to convert dn dn to required format.

Explanation:
The dn dn could not be converted to the format required for processing.

Possible Cause:
No memory was available.

Action:
Ensure that the process has enough memory to complete.

OBJ080E Unable to create file file\_name. Error = errno.

Explanation:
An attempt to create the file file\_name failed.

Possible Cause:
The directory is write-protected, or there is not enough disk space available.

Action:
Ensure that the ASAM Master User has permission to write to the specified directory. Ensure that disk space is available on the volume.

OBJ081E Unable to write to file file\_name. Error = errno.

Explanation:
An attempt to write to the file file\_name failed.

Possible Cause:
There is not enough disk space available.

Action:
Ensure that disk space is available on the volume.

OBJ082E Unable to delete file file\_name. Error = errno.

Explanation:
An attempt to delete the file file\_name failed.

Possible Cause:
Permissions do not allow the file to be deleted.

Action:
Ensure that the ASAM Master User has permission to delete the specified directory.

OBJ084I Checking UID/GID Set UIDGID\_set.

Explanation:
The Census Trawl is verifying the contents of UID/GID Set UIDGID\_set.

Action:
None. Informational Only.

OBJ086W Unable to start Trawl because a Trawl is already running.

Explanation:
A Trawl could not start because a Trawl is already in progress.

Possible Cause:
The specified scheduled Trawl times are not sufficiently spaced to allow completion of the previous Trawl.

A manual Trawl was started and it had not completed before the scheduled Trawl time arrived.

Action:
Wait until the currently running Trawl has completed, or stop the Trawl and restart it manually.

OBJ087E Cleanup of resources from the previous Trawl failed.

Explanation:
An error occurred while trying to free resources used by the previously run Trawl.

Action:
Wait for the Trawl to complete. Use the Trawl Status screen in the Web interface to confirm that no Trawl is running. If you are still unable to start a Trawl, restart the primary Core Driver.

OBJ088E Unable to allocate resources for starting a Trawl.

Explanation:
A task could not be created for performing a Trawl.

Possible Cause:
The system is low on memory.

Action:
Restart the primary Core Driver. If the problem persists, look for other processes that are consuming excessive memory.

OBJ089E Unable to start the Trawl task.

Explanation:
A task could not be started because of system limitations. The implementation of a task is operating system dependent. For example, a task might be implemented as a thread. In this case, a thread could not be created.

Possible Cause:
The system is low on resources.

Action:
Determine and correct the cause of limited system resources.

OBJ090E Unable to read from file file\_name. Error = errno.

Explanation:
An attempt to read from the file file\_name failed.

Possible Cause:
Internal error.

Action:
Turn on debugging information using the command line parameter: -d asam\_objectserv,dom, and forward the resulting log to Support.

OBJ091W Object type of object\_dn is not recognized.

Explanation:
The object class for the object was not recognized.

Possible Cause:
The given object does not have an object class that can be processed.

Action:
Examine the object named by object\_dn to determine why it cannot be processed.

OBJ092E Unable to determine value of attribute attribute\_name for object object\_name.

Explanation:
An attempt to read the value for attribute attribute\_name failed.

Possible Cause:
System memory is low.

Action:
Increase the amount of memory available to the process.

OBJ093E Unable to create directory search request.

Explanation:
An attempt to read information from the directory failed.

Possible Cause:
System memory is low.

Action:
Increase the amount of memory available to the process.

OBJ094E Unable to create request to modify attributes in the directory.

Explanation:
An attempt to modify information in the directory failed.

Possible Cause:
System memory is low.

Action:
Increase the amount of memory available to the process.

OBJ095E Unable to initialize mutex.

Explanation:
A mutex could not be initialized.

Possible Cause:
The system is low on available resources.

Action:
Ensure adequate resources for the process.

OBJ096E Unable to find object dn during repair of links in Census because of error error\_id.

Explanation:
When attempting to repair Census information for the previously deleted object dn, the reinstated object could not be found.

Possible Cause:
The object has not yet been re-created.

Action:
Re-create or restore the object dn.

OBJ097I ASAM-inputGUID updated in object dn.

Explanation:
Information has been repaired in object dn.

Possible Cause:
Census information is being repaired for the user.

Action:
None.

OBJ098I Processed processed\_count of users\_in\_search\_object users.

Explanation:
Indicates progress in processing the users specified by a Search object.

Action:
None.

OBJ099I Processed processed\_count of groups\_in\_search\_object groups.

Explanation:
Indicates progress in processing the groups specified by a Search object.

Action:
None.

OBJ100I Processed processed\_count of aliases\_in\_search\_object aliases.

Explanation:
Indicates progress in processing the aliases specified by a Search object.

Action:
None.

OBJ102I Processed processed\_count UIDGID objects.

Explanation:
Indicates progress in processing the UID/GID objects in a UID/GID Set.

Action:
None.

OBJ105I Dispatching new event notification to Platform platformName.

Explanation:
Object Services is dispatching a notification to Event Journal Services that a new event is ready to be processed for the specified platform.

Only Platform Receivers that are running in Persistent mode are notified of new events that are pending. Platform Receivers running in other modes discover the new events the next time they poll or connect to Event Journal Services.

Possible Cause:
A new object event has been detected by the Event Subsystem or a Trawl process.

Action:
The Event Journal Services component processes the event and sends it to the Persistent mode Receiver that is running on the specified platform.

OBJ106I Phase phase\_number: Processing Password Updates.

Explanation:
The Census Trawl is updating ePasswords that Core Drivers were previously unable to store.

Action:
None. Informational only.

OBJ107E Attempt to process an event with no DN was aborted.

Explanation:
An event was detected for an eDirectory object, but the dn of that object was unavailable. The event could not be processed.

Possible Cause:
Running a down-level version of the Core Driver.

Action:
Update the Core Driver.

OBJ108I Updated password for user object\_dn.

Explanation:
The password stored for object object\_dn was updated.

Possible Cause:
The password for the object has changed.

Action:
None.

OBJ109E Error error\_id updating password for user object\_dn.

Explanation:
The password for object\_dn could not be updated because of error error\_id.

Action:
Change the password for the given user.

OBJ111I Removed password from temporary storage for user user\_dn.

Explanation:
A password that was held in temporary storage pending processing by the Core Driver was removed.

Possible Cause:
The password was successfully stored, or the user is not managed.

Action:
None.

OBJ112I Error error\_id removing password for user user\_dn from temporary storage.

Explanation:
A password that was held in temporary storage pending processing by the Core Driver could not be removed.

Action:
None.

OBJ113I user\_or\_group\_name updated for driver storage format.

Explanation:
The user or group has been updated for use with the driver. It will no longer function correctly with Account Management 3.0.

Action:
None.

OBJ114I Removed object\_cn from UID/GID Set UIDGID\_set.

Explanation:
object\_cn was removed from UID/GID Set UIDGID\_set.

Possible Cause:
The UID or GID number has been migrated to a new storage format.

Action:
None. Informational only.

OBJ115I Migrating user\_or\_group\_name to driver storage format.

Explanation:
Data for the user or group is being converted to the storage format used by the driver.

Possible Cause:
Software version has been updated.

Action:
None. Informational only.

OBJ116I Updating inclusion in Platform Set platform\_set for user\_or\_group.

Explanation:
Platform Set information for the user or group is being migrated to a new storage format.

Action:
None. Informational only.

OBJ117I Updating association to platform platform for user\_or\_group.

Explanation:
Platform Association information for the user or group is being migrated to a new storage format.

Action:
None. Informational only.

OBJ118I Updating UID/GID in set uidgid\_set for user\_or\_group.

Explanation:
UID/GID information for the user or group is being migrated to a new storage format.

Action:
None. Informational only.

OBJ119I Removed object object\_dn.

Explanation:
Object object\_dn was removed during data migration to a new storage format.

Action:
None. Informational only.

OBJ120I Object Services received an event for object\_dn.

Explanation:
The Event Subsystem notified Object Services of an event.

Possible Cause:
An object was added, changed, or deleted in eDirectory.

Action:
None. Informational only.

OBJ121I Object Services received an event for object with unidentified dn.

Explanation:
The Event Subsystem notified Object Services of an event.

Possible Cause:
An object was added, changed, or deleted in eDirectory.

Action:
None. Informational only.

OBJ122I Processing a pseudo-event for object\_dn.

Explanation:
The object is being processed as if an event occurred.

Possible Cause:
The object was re-populated.

Action:
None. Informational only.

OBJ123E Delete action for object\_cn aborted because of invalid Search object.

Explanation:
One or more Search objects did not contain a valid inputReference.

Possible Cause:
A Search object exists for which the object specified by the inputReference has been deleted, or an error occurred while trying to retrieve information from the object specified by the inputReference.

Action:
Determine which Search object is not valid and correct it.

OBJ124I Obsolete object dn successfully removed.

Explanation:
The information represented by object dn has been updated to a new storage format. The obsolete object has been cleaned up.

After removal of a large number of objects, it can be desirable to use directory maintenance techniques to reduce the size of the directory on disk.

Possible Cause:
A new version of the Fan-Out Driver software has been installed.

Action:
None.

OBJ125I Migration status changed to migration\_status.

Explanation:
Stages of data conversion are Migration (to new data format), Cleanup (removal of obsolete objects), and Complete.

Each user or group is migrated to the new data format the first time it is processed by the Core Driver.

After all users and groups have migrated to the new data format, cleanup of obsolete objects begins.

The status is reported as Complete after all users or groups have been migrated, and all obsolete objects have been cleaned up. The size of the eDirectory database can be reduced by using standard eDirectory maintenance practices when this stage has been reached.

Possible Cause:
A new version of the Fan-Out Driver software has been installed.

Action:
None.

OBJ126I Phase phase\_number: Migration Cleanup.

Explanation:
The Census Trawl is removing obsolete data that has been migrated to a new storage format.

Action:
None. Informational only.

OBJ127E Alternate name attribute alternate\_name must have single value or form <platform set name>:<alt name>.

Explanation:
Attributes used for specifying alternate names must have only a single value, or all values must be of the form <platform set name>:<alternate name>.

Action:
Modify the alternate naming attribute to either have one value, or have values of the form <platform set name>:<alternate name>.

OBJ128I Created Census entry for alternate name alternate\_name.

Explanation:
An entry was created in the Census to represent the alternate name for the object.

Action:
None.

OBJ129E Could not add alternate name alternate\_name to the Census. Name already exists.

Explanation:
Another object already exists in the Census with the specified name.

Possible Cause:
Another user or group has the same name or alternate name.

Action:
Resolve as you would any naming exception.

OBJ130I Removed alternate name alternate\_name from Census.

Explanation:
An alternate name was removed from the Census.

Action:
None.

OBJ131I Name is on the census exclude list.

Explanation:
The user or group has been designated as one to exclude from the Census.

Possible Cause:
The user or group has been manually added to the Census exclude list.

Action:
The user or group may be removed from the Census exclude list from the Provisioning Configuration screen.

OBJ132I Removed obsolete Platform Association association from object\_cn.

Explanation:
The obsolete Platform Association association was removed from Census object object\_cn.

Possible Cause:
The obsolete platform was removed from the Fan-Out Configuration.

Action:
None. Informational only.
