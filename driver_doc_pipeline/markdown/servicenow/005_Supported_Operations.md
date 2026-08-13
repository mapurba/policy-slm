# 1.4 Supported Operations

The ServiceNow driver supports the following operations on the Subscriber channel:

| Operation | Supported On |
| Add, Modify, Delete, Migrate, and Query | User and Group Objects  *NOTE:*When a user's password is added or modified on the Subscriber channel, ServiceNow returns the user password in hashed format which is seen in the ServiceNow driver trace. For more information, see the [ServiceNow documentation](https://docs.servicenow.com/) website. |
| Password Synchronization | User Objects |
| Entitlements | * User Accounts * Group Membership * Roles * Departments |
