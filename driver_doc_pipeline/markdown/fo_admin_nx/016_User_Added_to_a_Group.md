# 3.6 User Added to a Group

A user for which there is an eUser object in the Census is added to the member list of a Group object in eDirectory.

1. An administrator adds the user to the member list of the Group object.
2. The Event Subsystem receives the change and notifies Object Services.
3. Object Services notifies Event Journal Services.
4. When each Platform Receiver of the Platform Sets associated with both the eUser and the eGroup requests an event and this event is the next one for that platform, Event Journal Services obtains detailed information about the user by reading its object from eDirectory, and passes the provisioning event to the Platform Receiver.

   If Event Journal Services cannot yet obtain updated user information due to incomplete directory synchronization, the next event for the platform is processed and this one is tried again later.
5. Each Platform Receiver that receives the provisioning event calls its Add User to Group Receiver script, which adds the user to the group in the local security system.
6. Event Journal Services notifies Audit Services, which records the action in the Audit Log.
