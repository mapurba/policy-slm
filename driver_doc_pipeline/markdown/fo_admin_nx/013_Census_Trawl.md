# 3.3 Census Trawl

Object Services of the primary Core Driver periodically performs a Trawl to verify the contents of the Census. A Trawl is also run to initially build the Census, or a part of it, whenever you use the Web interface to define a new Census Search object.

The following steps are performed for each Census Search object:

1. Object Services scans the Census Search object for users and groups.
2. For any user or group that does not have a corresponding eUser or eGroup in the Census container:

   1. Object Services creates an eUser or eGroup object in the Census container, and associates the user or group with the Platform Set container objects whose Platform Set Search objects cover the user or group.

      If the common name of the new user or new group is the same as a user or group that already exists in the Census container, the eUser or eGroup object is instead created in the Exceptions container, and the exception must be resolved by an administrator. For guidance in avoiding and resolving exceptions, see [Section II, Core Driver Administration](bexh6ct.html).
   2. Object Services notifies Event Journal Services.
   3. When each Platform Receiver of the associated Platform Sets requests an event and this event is the next one for that Platform, Event Journal Services obtains detailed information about the new user or group by reading its object from eDirectory and passes the provisioning event to the Platform Receiver.

      If Event Journal Services cannot obtain the information yet because directory synchronization is not complete, the next event for the platform is processed and this one is tried again later.
   4. Each Platform Receiver that receives the provisioning event checks to see if a user or group by that name already exists (unless the user or group is excluded from processing based on specifications in the platform configuration file).

      If the user or group already exists, the Platform Receiver notifies Event Journal Services.

      If the user or group does not exist, the Platform Receiver calls the Add User or Add Group Receiver script, which adds the new user or group to the local security system and prepares it for use. The Platform Receiver then notifies Event Journal Services of the script outcome.
   5. Event Journal Services notifies Audit Services, which records the action in the Audit Log.

The following steps are performed for each user and group in the Census.

1. Object Services verifies that the user or group is still covered by a Search object.

   If it does not, the same steps are followed as for [User Deleted from eDirectory](babehjdf.html) or [Group Deleted from eDirectory](babgadhf.html).
2. Object Services verifies that the User object or Group object that corresponds to the user or group still exists in eDirectory.

   If it does not, the same steps are followed as for [User Deleted from eDirectory](babehjdf.html) or [Group Deleted from eDirectory](babgadhf.html).
