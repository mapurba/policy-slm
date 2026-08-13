# 2.3 Creating an Identity Manager Provisioning Service Account for the Driver

The Entity Data Model driver needs a user account in Identity Manager to grant and revoke permissions. The account must have Resource Administrator permissions in the identity applications.

1. Log in to Identity Manager Home as an administrator.
2. To create the new system account, complete the following steps:

   1. Select Create Users and Groups.
   2. Create a new User object for a system account. For example, in the OU=sa,O=data container, create an object called driverProvServiceAcct.
   3. Specify values for the required fields for the new user, and then select Continue.
   4. Specify a password for the new user object.
3. To assign resource administrator permissions to the account, complete the following steps:

   1. Select Administration > RBPM Provisioning and Security.
   2. Select Administrator Assignments > Assign.
   3. Specify a description for this assignment request. For example, Resource Provisioning Account.
   4. For Domain, specify Resource.
   5. For User(s), specify the name that you assigned to the new User object.
   6. Select All Permissions.
   7. Select Assign.
4. Log out of Identity Manager Home.
