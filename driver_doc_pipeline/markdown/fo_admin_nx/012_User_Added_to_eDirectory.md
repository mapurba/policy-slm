# 3.2 User Added to eDirectory

An administrator adds a new user to eDirectory. The user is covered by a Census Search object.

1. An administrator adds the new user to eDirectory.
2. The Event Subsystem receives the change and notifies Object Services.
3. If the user is covered by a Census Search object, Object Services of the primary Core Driver creates an eUser object for the user in the Census container, and associates the user with the Platform Set container objects whose Platform Set Search objects cover the user.

   If the common name of the new user is the same as a name that already exists in the Census container, its eUser object is instead created in the Exceptions container, and the exception must be resolved by an administrator. For guidance in avoiding and resolving exceptions, see the [Section II, Core Driver Administration](bexh6ct.html).
4. Object Services notifies Event Journal Services.
5. When each Platform Receiver of the associated Platform Sets requests an event and this event is the next one for that platform, Event Journal Services obtains detailed information about the new user by reading its object from eDirectory and passes the provisioning event to the Platform Receiver.

   If Event Journal Services cannot obtain the new user information yet because directory synchronization is not complete, the next event for the platform is processed and this one is tried again later.
6. Each Platform Receiver that receives the provisioning event checks to see if a user by that name already exists (unless the user is excluded from processing based on specifications in the platform configuration file).

   If the user already exists, the Platform Receiver notifies Event Journal Services.

   If the user does not exist, the Platform Receiver calls the Add User Receiver script, which adds the new user to the local security system and prepares it for use. The Platform Receiver then notifies Event Journal Services of the script outcome.
7. Event Journal Services notifies Audit Services, which records the action in the Audit Log.
