# 2.3 Directory Objects

The Identity Manager Fan-Out Driver maintains objects in eDirectory with configuration information for the Core Driver and platforms as well as users and groups of users available to the platforms. These are stored in the ASAM System container.

You maintain configuration information by using the Web interface. Do not use any other method of changing objects in the ASAM System container unless advised by support personnel.

A writable replica of the partition holding the ASAM System container must reside on the LDAP host server used by a Core Driver.

## 2.3.1 The ASAM Master User Object

The Core Driver processes perform an LDAP Bind as the ASAM Master User to gain access to eDirectory. The ASAM Master User object can be specified during installation.

The ASAM Master User must have Supervisor rights to the container in eDirectory that holds the users and groups that can be added to the Census. This is known as the User and Group Subtree. These rights are granted during installation.

To use the AS Client API to access objects outside of the User and Group Subtree, you must grant additional rights to the ASAM Master User.

* You must grant the ASAM Master User Browse object rights and Compare property rights to any object that is accessed through the AS Client API.
* You must grant the ASAM Master User Read property rights to any object whose Security Equals list or Group Membership list, or other attribute value is accessed through the AS Client API.

## 2.3.2 Configuration-Oriented Objects

Configuration information for Identity Manager Fan-Out Driver components is stored in objects that correspond to them.

* Audit Services object
* Certificate Services object
* Event Journal Services object
* Object Services object
* Web Services object
* Event Subsystem objects
* Authentication Services objects
* UID/GID Set objects
* Platform Set objects
* Platform objects

Identity Manager Fan-Out Driver program component configuration objects list each of their host server network addresses. Before accepting a communication connection from another component, driver components verify that the connection originates from a network address listed in the corresponding configuration object.

## 2.3.3 Census Container

Based on your specifications, Object Services maintains a Census of users and groups of users for use with target platforms. Users in the Census are represented by Enterprise User (eUser) objects. Groups of users in the Census are represented by Enterprise Group (eGroup) objects.

Object Services uses events from the Event Subsystem to maintain the Census. Object services of the primary Core Driver also periodically trawls eDirectory for information to ensure the validity of the Census.

Authentication Services uses eUser objects in the Census to locate the corresponding User objects in eDirectory for password verification and other functions. For information about associating eUsers and eGroups from the Census with sets of platforms for provisioning purposes, see [Platform Set Objects](br12c66.html#babffida).

You use the Web interface to specify Census Search objects that identify the users and groups that are to be included in the Census.

Search objects can get Enterprise Users from

* Specifically identified User objects
* Group object membership
* Organizational Role object occupant lists
* Objects in containers (and subcontainers, to whatever depth you set)

Search objects can get Enterprise Groups from

* Specifically identified Group objects
* Group objects in containers (and subcontainers, to whatever depth you set)
* Identity Manager entitlements

### Dynamic Groups as Search Objects

Dynamic groups use an LDAP search filter to define a set of rules that, when matched by eDirectory User objects, define the members of the group. Membership in the group is evaluated dynamically by eDirectory. There is no actual list of members for a dynamic group like there is for a static group.

Events involving users who are already in the Census that affect their membership in a dynamic group that is a Search object are seen by the Event Subsystem as they happen. This is because the Core Driver interrogates Search objects to discover if an event involving a given User object is of interest.

Events involving users not already in the Census and events involving the LDAP search filter of a dynamic group that is a Search object are not seen by the Event Subsystem. This is because there is nothing to drive the LDAP search. Such changes are not detected until the next Trawl is run.

### Naming Exceptions

Because Enterprise User objects and Enterprise Group objects share the same name space, their names must be unique. If a duplicate name is found based on your Census Search objects, the resulting Enterprise User or Enterprise Group object is placed in the Exceptions container rather than being made available in the Census. You can use the Web interface to review naming exceptions.

### Enterprise User Objects

Enterprise User (eUser) objects reside in the Census container. An eUser object represents a single User object, or an Alias object that references a User object, in eDirectory.

An eUser object includes a reference to the User object or Alias object that it represents in eDirectory. The User object referenced by an Alias object is provisioned to platforms, not the Alias object itself.

### Enterprise Group Objects

Enterprise Group (eGroup) objects reside in the Census container. An eGroup object represents a group of users, and is based on a Group object, or an Alias object that references a Group object, in eDirectory. Enterprise Group objects must be based on static Group objects. Dynamic Group objects are not provisioned.

An eGroup object includes a reference to the Group object or Alias object that it represents in eDirectory. The Group object referenced by an Alias object is provisioned to platforms, not the Alias object itself.

Enterprise Group objects in the Census contain a list of the eUser objects that are represented in the corresponding Group object in eDirectory (but not any users that are not present in the Census).

### Inactive Users and Groups

You can choose to have Enterprise User and Enterprise Group objects whose corresponding User or Group object is deleted from eDirectory or is no longer covered by a Census Search object remain in the Census in an inactive state. Because Enterprise User objects relate to User objects in eDirectory through a globally unique identifier, this prevents another person from receiving access to resources as an unintended result of the reuse of the user name. Inactive users cannot authenticate through Authentication Services.

### Delete Pending Duration

You can use the Web interface to specify a Delete Pending Duration. During this interval, eUser and eGroup objects whose corresponding User and Group objects have either been deleted from eDirectory or are no longer covered by a Search object are not deleted from target platforms. The results of a Delete User or Delete Group Receiver script can be difficult to reverse. Delete Pending Duration provides a grace period to allow recovery from a disastrous mistake affecting many users.

The Delete User Pending or Delete Group Pending Receiver script is called when a delete event becomes pending for a user or group. The Delete User or Delete Group script is not called until the Delete Pending Duration expires.

## 2.3.4 Platform Objects

A Platform object represents a specific target platform that runs Platform Services.

## 2.3.5 Platform Set Objects

Platform Set objects provide the relationship between Search objects and Platform objects. You can use Platform Sets to group together multiple platforms that share the same user and group population.

The following example illustrates how you can fan out your user and group population to platforms that are grouped into Platform Sets.

*Table 2-1* Platform Set Example

| Containers with Users | *OU=Students* Henri Markus Rie | *OU=Faculty* Carmen Eleu Mario | *OU=Staff* Isabel Claire Kenji |
| Search Objects | OU: Students Include Users: Yes | OU: Faculty Include Users: Yes | OU: Staff Include Users: Yes |
| Platform Sets | *Academic* Search Objects: Students, Faculty Platforms: StudentDataServer, LabWorkstation1, LabWorkstation2, LabWorkstation3 | *Employee* Search Objects: Faculty, Staff Platforms: BenefitsServer, EmployeeDataServer | *Everyone* Search Objects: Students, Faculty, Staff Platforms: MailServer, LibraryServer |
| Platforms | *StudentDataServer* Platform Set: Academic Users: Henri, Markus, Rie, Carmen, Eleu, Mario  *LabWorkstation1* Platform Set: Academic Users: Henri, Markus, Rie, Carmen, Eleu, Mario  *LabWorkstation2* Platform Set: Academic Users: Henri, Markus, Rie, Carmen, Eleu, Mario  *LabWorkstation3* Platform Set: Academic Users: Henri, Markus, Rie, Carmen, Eleu, Mario | *BenefitsServer* Platform Set: Employee Users: Carmen, Eleu, Mario, Isabel, Claire, Kenji  *EmployeeDataServer* Platform Set: Employee Users: Carmen, Eleu, Mario, Isabel, Claire, Kenji | *MailServer Platform Set: Everyone* Users: Henri, Markus, Rie, Carmen, Eleu, Mario, Isabel, Claire, Kenji  *LibraryServer* Platform Set: Everyone Users: Henri, Markus, Rie, Carmen, Eleu, Mario, Isabel, Claire, Kenji |
