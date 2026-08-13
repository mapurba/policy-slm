# 3.4 User Deleted from eDirectory

A User object that is covered by a Census Search object is deleted from eDirectory.

1. An administrator deletes a user from eDirectory.
2. The Event Subsystem receives the deletion and notifies Object Services.
3. If the user is covered by a Census Search object, then Object Services takes one of the following actions based on configuration information that you have specified:

   Object Services marks the corresponding eUser object in the Census as inactive. (Inactive users cannot authenticate through Authentication Services.)

   or

   Object Services marks the eUser object for deletion after the event has been processed by all associated platforms.
4. Object Services notifies Event Journal Services.
5. When each Platform Receiver of the associated Platform Sets requests an event and this event is the next one for that Platform, Event Journal Services passes the provisioning event to the Platform Receiver. When the last Platform Receiver of a Platform Set has received the event, the next Trawl removes the Platform Set association for the eUser (if you have defined your configuration to remove deleted users rather than mark them inactive).
6. Each Platform Receiver that receives the provisioning event calls its Disable/Delete User Receiver script to disable the user in the local security system or to delete it and clean up its resources (unless the user is excluded from processing based on specifications in the platform configuration file).
7. Event Journal Services notifies Audit Services, which records the action in the Audit Log.

If you have specified a Delete Pending Duration, Event Journal Services indicates to the Platform Receiver that a delete is pending for the user. When the Delete Pending Duration has expired, Event Journal Services delivers the delete event.
