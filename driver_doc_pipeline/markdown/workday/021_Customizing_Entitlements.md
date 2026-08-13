# 3.3 Customizing Entitlements

The Workday Driver supports entitlements to manage assigned permissions and revocations. This feature is available as an optional package. You can use the entitlements feature to manage the user memberships in User-Based Security Groups, and for assigning or revoking organizational roles to workers. From the Workday driver perspective, a User-Based Security Group grants the rights to the users in Workday. Similarly, the Organizational Role entitlement grants permissions to workers to perform certain tasks based on roles in the organization.

The driver must be enabled for configuring the supported entitlements, and managing the permissions of a user account in Identity Manager. The entitlements can be granted or revoked only by the entitlement permission administrators.

* [Prerequisites](t4finm19niw9.html#t4finn8ocl1l)
* [Supported Entitlements](t4finm19niw9.html#t4finnefpau2)

## 3.3.1 Prerequisites

To configure entitlements, you must have the following drivers, and a user with the applicable role as follows:

* Role and Resource Driver
* User Application Driver
* Administrative privileged user

## 3.3.2 Supported Entitlements

The Workday Driver supports the following entitlement types:

* [User-Based Security Group](t4finm19niw9.html#t4fil341o0nu)
* [Assignable Role](t4finm19niw9.html#t4finnujte1b)

### User-Based Security Group

The User-Based Security Group entitlement is a set of access permissions provided for a user belonging to a user-based security group in Workday. This entitlement grants or revokes the membership to a User-Based Security group for a user. If the User-Based Security Group entitlement is granted, the user is added to the user-based security group, and if revoked, the user is removed.

When configuring the driver, in the Entitlement Configuration page, select Enable User-Based Security Group Entitlement as true.

You can synchronize the user memberships of the User-Based Security Groups from Workday to Identity Manager through this entitlement using the Controlled Permission Reconciliation Services (CPRS) feature. For more information, see [Using Controlled Permission Reconciliation Services](https://www.netiq.com/documentation/identity-manager-49/identity_apps_admin/data/netiq-identity-manager-cprs-controlled-permission-reconciliation-services.html) in the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](https://www.netiq.com/documentation/identity-manager-49/identity_apps_admin/data/bookinfo.html#bookinfo).

*NOTE:*Prior to using the CPRS feature, you must migrate all users from Workday at least once post upgrading to Workday driver 1.3. During the migration process, a cache mapping for user-name and worker-id is created.

For more information, see the Migrate on Startup field settings in [Step 8](t4avmq79xc47.html#cust_attr_xslt).

### Assignable Role

Every Workday organization defines certain roles, which can be assigned directly to workers in Workday. The role assignments that are defined in one Workday organization is independent from the assignment defined in another Workday organization. As a result of this, the Workday assignable role entitlement for a role contains the name of the organization in its entitlement association.

For example, consider the Organizations as Org1 and Org2 and the defined roles as Role1 and Role2. Also assume the following associations in Workday organization:

* Org1 defines Role1 and Role2, and
* Org2 defines only Role1

In such a case, the Identity Manager would fetch three entitlement associations from both the Workday organizations as follows:

* Role1#Org1
* Role2#Org1
* Role1#Org2

Now, if Role1#Org1 is assigned or revoked, the assignment changes in Workday will be applicable only in Org1 for Role1, and the Org2 assignment for Role1 remains unchanged.

You must ensure to grant sufficient privileges to the Workday integration user in order to execute the Assign Roles Web Service task in Workday. For more information, see [Prerequisites to be Performed in Workday for Assignable Roles](t4finm19niw9.html#t4fjtfovj0vp).

You can synchronize the worker assignments for organizational roles from Workday to IDM through this entitlement, using the Controlled Permission Reconciliation Services (CPRS) feature. For more information, see [Using Controlled Permission Reconciliation Services](https://www.netiq.com/documentation/identity-manager-49/identity_apps_admin/data/netiq-identity-manager-cprs-controlled-permission-reconciliation-services.html) in the [NetIQ Identity Manager - Administrator’s Guide to the Identity Applications](https://www.netiq.com/documentation/identity-manager-49/identity_apps_admin/data/bookinfo.html#bookinfo).

*NOTE:*Workday supports inherited role assignment from a supervisory organization to its sub organization. But, the Resource catalog in Identity Manager stores the information of assigned resources only, and that information is specific to organizations. Hence, by publishing the CPRS computation, you can store all the inherited role assignments.

For the procedure to configure entitlements in Designer, see [Configuring Entitlements](t4fiw0ox336m.html).

#### Prerequisites to be Performed in Workday for Assignable Roles

To enable role provisioning from Workday, refer to the following steps:

1. Login to the Workday tenant.
2. Start Proxy session with a super user.
3. Create a User-Based Security Group, and assign the Workday integration user to this group.
4. Search for the User-Based Security Group name as created in [Step 3](t4finm19niw9.html#step3), and click the link from the search results.
5. Click ![](../graphics/wd_search_icon.png) > Security Group > Maintain Domain Permissions for Security Group.
6. Navigate to the Integration Permission section > Domain Security Policies permitting Put access field, and search and select Org Designs: Assign Roles > OK > Done.
7. Search for Activate Pending Security Policy Changes and click the link from the search results.
8. Add a comment, and click OK.
9. In the Activate Pending Security Policy Changes page, check the Confirm checkbox and click OK.
10. Search for View Security for Securable Item, and select the link from the search results.
11. Provide a name in the Assign Roles field, and click OK.
12. In the Tasks list, click View Security button corresponding to the Assign Roles Web Service task.
13. In the Business Process Security table, navigate to Initiating Action for Business Process > Assign Roles ![](../graphics/wd_search_icon.png) > Business Process Policy > Edit.
14. Scroll to find the Assign Roles Web Service task.
15. In the corresponding Security Groups field, search and select the name of the User-Based Security Group as created in Step 3, and click OK > Done.
16. To activate these changes, repeat [Step 7](t4finm19niw9.html#step7) to [Step 9](t4finm19niw9.html#step9).
