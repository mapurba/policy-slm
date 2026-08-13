# 3.5 Group Deleted from eDirectory

A Group object that is covered by a Census Search object is deleted from eDirectory.

1. An administrator deletes a group from eDirectory.
2. The Event Subsystem receives the deletion and notifies Object Services.
3. If the group is covered by a Census Search object, then Object Services takes one of the following actions based on configuration information that you have specified:

   Object Services marks the corresponding eGroup object in the Census inactive.

   or

   Object Services marks the eGroup object for deletion after the event has been processed by all associated platforms.
4. Object Services notifies Event Journal Services.
5. When each Platform Receiver of the associated Platform Sets requests an event and this event is the next one for that platform, Event Journal Services passes the provisioning event to the Platform Receiver. When the last Platform Receiver of a Platform Set has received the event, the next Trawl removes the Platform Set association for the eGroup.
6. Each Platform Receiver that receives the provisioning event calls its Delete Group Receiver script to delete the group from the local security system and clean up its resources.
7. Event Journal Services notifies Audit Services, which records the action in the Audit Log.

If you have specified a Delete Pending Duration, Event Journal Services indicates to the Platform Receiver that a delete is pending for the group. When the Delete Pending Duration has expired, Event Journal Services delivers the delete event.
