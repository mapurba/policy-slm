# 5.4 Sample SCIM Driver Use Cases for Salesforce

This section explains the sample use cases that you can perform in Identity Manager to execute the required operation on resources available in Salesforce.

*IMPORTANT:*All the field values shown in this section are just sample values. You must ensure not use them directly to perform the use case operations.

The following operations can be performed on the subscriber channel:

*NOTE:*You must replace the variable values in the SCIM end point URL as per Salesforce specifications. These are just sample values, replace them as applicable for the SCIM end point examples mentioned in other sections.

* <tenant name> with ap16, ap17, etc.
* <current version> with v2, etc.
* <association> with salesforce-userid, salesforce-groupid, etc.

* Operations performed on a user

  | Operation | Sample SCIM endpoint | Method |
  | Adding a user: A user is added in Identity Manager and synchronized to Salesforce through the SCIM driver. For example, the details of the user such as, user's first name, last name, contact details, email ID, location, department, user name, initial login password are added and synchronized with Salesforce.  *IMPORTANT:*Ensure to add the auxiliary class scim-User to the object class attribute. In case the auxiliary class is not added, the scim related attributes such as, scim-Entitlementsvalue, scim-Address will not be displayed, and the user created in Identity Console will not sync to Salesforce. To sync the created user to Salesforce, you must mandatorily provide the scim-Entitlementsvalue attribute value. For example, <00e2x000000K4Yv>. | https://<tenantname>.salesforce.com/services/scim/<current version>/Users | POST |
  | Deleting a user: Deleting a user in Identity Manager disables the user in Salesforce. | https://<tenantname>.salesforce.com/services/scim/<current version>/Users/<salesforce-userid> | DELETE |
  | Modifying a user: If there are any changes made to the user details such as, contact details, email ID etc, they will be synchronized with Salesforce.  *NOTE:*Salesforce does not support renaming a user. | https://<tenantname>.salesforce.com/services/scim/<current version>/Users/<salesforce-userid> | PUT |
  | Migrating a user: You can migrate an individual or multiple users from Identity Manager to Salesforce and vice-versa. | https://<tenantname>.salesforce.com/services/scim/<current version>/Users | GET/PUT |
  | Polling a user: You can poll a user or multiple users from Salesforce to Identity Manager. | https://<tenantname>.salesforce.com/services/scim/<current version>/Users/ | GET |
  | Querying a User: You can query the synced attributes of resource such as user from Salesforce through Identity Console. Also, you can query through dxcmd utility to fetch required resources or attributes using specific conditions. | https://<tenantname>.salesforce.com/services/scim/<current version>/Users/<salesforce-userid> | GET  *NOTE:*Complex JSON attributes cannot be queried from SCIM compliant applications through dxcmd utility. |
* Operations performed on public groups

  | Operation | Sample SCIM endpoint | Method |
  | Adding a group: A group is added in Identity Manager to manage multiple users with same set of access permissions, rather than managing them individually. | The SCIM end point for Salesforce to add a group: https://<tenantname>.salesforce.com/services/scim/<current version>/Groups | POST |
  | Adding member to a group: A member is added to a group based on the user’s role, department and access permissions that the user qualifies for, so that the access permissions for that designated user role are provisioned accordingly. | The SCIM end point for Salesforce to add a member to a group: https://<tenantname>.salesforce.com/services/scim/<current version>/Groups | PUT |
  | Removing member from a group: A user can be removed from a group if the user’s role or designation, or access permissions provided do not qualify a user to belong to that group. This happens in case of a role or designation change of the user, or separation or termination of the user. | The SCIM end point for Salesforce to remove a member from a group: https://<tenantname>.salesforce.com/services/scim/<current version>/Groups/<salesforce-groupid> | PUT |
  | Renaming group object: The group name can be renamed as required. | The SCIM end point for Salesforce to renaming a group: https://<tenantname>.salesforce.com/services/scim/<current version>/Groups/<salesforce-groupid> | PUT |
  | Deleting a group: Duplicate groups, redundant groups, empty groups or groups that are not required can be deleted, and the group members will be moved to another group as required. | The SCIM end point for Salesforce to delete a group: https://<tenantname>.salesforce.com/services/scim/<current version>/Groups/<salesforce-groupid> | DELETE |
  | Migrating a Group: You can migrate an individual or multiple groups from Identity Manager to Salesforce and vice-versa. | The SCIM end point for Salesforce to add a member to a group: https://<tenantname>.salesforce.com/services/scim/<current version>/Groups | PUT/GET |
  | Polling a Group: You can poll groups from Salesforce to Identity Manager. | The SCIM end point for Salesforce to poll groups: https://<tenantname>.salesforce.com/services/scim/<current version>/Groups | GET |
  | Querying a Group: You can query the synced attributes of resource such as group from Salesforce through Identity Console. Also, you can query through dxcmd utility to fetch required resources or attributes using specific conditions. | The SCIM end point for Salesforce to query groups: https://<tenantname>.salesforce.com/services/scim/<current version>/Groups | GET  *NOTE:*Complex JSON attributes cannot be queried from SCIM compliant applications through dxcmd utility. |

## 5.4.1 Known Observations from Salesforce

The following are a few observations when some specific operations are performed in Salesforce:

* If you try to modify an email ID in Identity Manager and sync with Salesforce, the email ID does not get updated in Salesforce. The success code 200 is returned which appears in the driver log when this operation is performed.
* Salesforce does not support renaming a user from Identity Manager.
* Salesforce does not support the canonical type attribute for the phone number.
* Renaming a group in Identity Manager changes only the label attribute and not the name attribute.
* By default, you can poll only up to 10 users from Salesforce using the GET method.
