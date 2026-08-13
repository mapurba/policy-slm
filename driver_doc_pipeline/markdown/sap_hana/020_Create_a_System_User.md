# 5.1 Create a System User

Follow the below steps to create a system user.

1. Go to User Management and click ![](../graphics/create.png) to Create User or to Create Restricted User.
2. Under General Information, specify the User Name, User Group, Email, validity of the user (in Valid From and Valid Up To fields). Select Yes or No for Creation of Objects in Own Schema, PUBLIC Role, and Disable ODBC/JDBC Access.
3. Under Authorization Mode tab, select the Authorization Mode.
4. Under Authentication Mechanism, specify th password parameters for the user.

## 5.1.1 Grant Roles

Follow below steps to assign the roles to the system user.

1. Under User Management, select a user that has been created already.
2. This display the User details in a view mode. Click Assign Roles.
3. Role Assignment for User (the selected user) page appears.
4. Check the role to which the selected user has to be assigned. Toggle to ![](../graphics/toggle-yes.png) if the role assigned is Grantable to Others. Else toggle to ![](../graphics/toggle-no.png).
5. Click Save.

### Assign Privileges

User can be assigned with the following types of privileges.

#### System Privileges

Go to Privilege Management and under System Privileges tab, assign system privileges to the selected user.

#### Object Privileges

Go to Privilege Management and under Object Privileges tab, assign system privileges to the selected user.
