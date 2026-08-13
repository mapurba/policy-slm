# 1.5 Supported SCIM Driver Use Cases for SAP Cloud

The following operations can be performed on the subscriber channel:

* Operations performed on a user

  + Adding a user: A user is added in Identity Manager and synced to SAP Cloud through the SCIM driver. The details of the user such as, user's first name, last name, contact details, email ID, location, department, user name, initial login password are added and synchronized to the SAP Cloud.

    The SCIM end point for SAP Cloud to add a user: https://<tenant ID>.accounts.ondemand.com/service/scim/Users

    Method: POST
  + Modifying a user: If there are any changes made to the user details such as, user's first name, last name, contact details, email ID etc, they will be synchronized with SAP Cloud.

    The SCIM end point for SAP Cloud to modify a user: https://<tenant ID>.accounts.ondemand.com/service/scim/Users/<sapcloud-userid>

    Method: PUT

    *NOTE:*The user can be disabled in case of separation or termination of their services.
  + Migrate a user: You can migrate an individual or multiple users from Identity Manager to SAP Cloud and vice-versa.
  + Polling a user: You can poll a user from SAP Cloud to Identity Manager.

    The SCIM end point for SAP Cloud to poll users: https://<tenant ID>.accounts.ondemand.com/service/scim/Users

    Method: GET
  + Query a User: You can query the synced attributes of resource such as user from SAP Cloud through iManager. Also, you can query through dxcmd utility to fetch required resources or attributes using specific conditions.

    The SCIM end point for SAP Cloud to query users: https://<tenant ID>.accounts.ondemand.com/service/scim/Users/<sapcloud-userid>

    Method: GET

    *NOTE:*Complex JSON attributes cannot be queried from SCIM compliant applications through dxcmd utility.
* Operations performed on public groups

  + Adding a group: A group is added in Identity Manager to manage multiple users with same set of access permissions, rather than managing them individually.

    The SCIM end point for SAP Cloud to add a group: https://<tenant ID>.accounts.ondemand.com/service/scim/Groups

    Method: POST
  + Modifying a group

    - Adding member to a group: A member is added to a group based on the user’s role, department and access permissions that the user qualifies for, so that the access permissions for that designated user role are provisioned accordingly.

      The SCIM end point for SAP Cloud to add a member to a group: https://<tenant ID>.accounts.ondemand.com/service/scim/Groups/<sapcloud-groupid>

      Method: POST
    - Removing member from a group: A user can be removed from a group if the user’s role or designation, or access permissions provided do not qualify a user to belong to that group. This happens in case of a role or designation change of the user, or separation or termination of the user.

      The SCIM end point for SAP Cloud to remove a member from a group: https://<tenant ID>.accounts.ondemand.com/service/scim/Groups/<sapcloud-groupid>

      Method: POST
  + Deleting a group: Duplicate groups, redundant groups, empty groups or groups that are not required can be deleted, and the group members will be moved to another group as required.

    The SCIM end point for SAP Cloud to delete a group: https://<tenant ID>.accounts.ondemand.com/service/scim/Groups/<sapcloud-groupid>

    Method: DELETE
  + Migrate a Group: You can migrate an individual or multiple groups from Identity Manager to the SAP Cloud and vice-versa.
  + Polling a Group: You can poll all created groups from SAP Cloud to Identity Manager.

    Method: GET

    The SCIM end point for SAP Cloud to poll groups: https://<tenant ID>.accounts.ondemand.com/service/scim/Groups
  + Query a Group: You can query the synced attributes of groups from SAP Cloud. Also, you can query through dxcmd utility to fetch required resources or attributes using specific conditions.

    The SCIM end point for SAP Cloud to query groups: https://<tenant ID>.accounts.ondemand.com/service/scim/Groups/<sapcloud-userid>

    Method: GET

    *NOTE:*Complex JSON attributes cannot be queried from SCIM compliant applications through dxcmd utility.
