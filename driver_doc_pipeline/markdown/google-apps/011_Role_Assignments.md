# 3.4 Role Assignments

The G Suite connector is able to create and delete role assignments for users into Google admin roles, both custom and default. The connector exposes an attribute on UserEntry objects called roleAssignment which can be used to list, create, or delete role assignments for that user within the environment.

The following sections provide information on role assignments:

## 3.4.1 Understanding Roles and Role Assignments

G Suite domains allow for granting granular rights to certain administrative functions to users within the domain. This is done via a security role assignment.

*NOTE:*Google frequently updates the user interfaces of their web consoles. Your screens may differ from the ones shown in this guide.

To view your domain roles, select the Admin Roles tool from the admin console at <https://admin.google.com>.

*Figure 3-1* Assigning Administrative Roles

![](../graphics/figure45.png)

The default roles are visible in this panel. It is also possible to add custom roles to this list with various privileges.

*Figure 3-2* Creating a New Role

![](../graphics/figure46.png)

These roles can be assigned to users through a role assignment.

*Figure 3-3* Assigning Administrators to Roles

![](../graphics/figure47.png)

*Figure 3-4* Confirming Administrator Assignments

![](../graphics/figure48.png)

For more information on administrator roles and role management, see Google's documentation. <https://support.google.com/a/answer/33325?hl=en&ref_topic=4514341>

The developer documentation for role assignments may also provide additional clarity and assistance. <https://developers.google.com/admin-sdk/directory/v1/guides/manage-roles>

A role assignment consists of the following elements:

* The user to whom the role is assigned
* The role which is being assigned
* The scope of the assignment

  + The entire domain
  + An organizational unit

When assigning a role to a user for multiple organizational units, multiple role assignments are used, one per organizational unit assignment.

## 3.4.2 Identity Manager and Role Assignments

The G Suite Identity Manager connector allows for the creation and deletion of role assignments for users via a structured attribute called roleAssignment.

The roleAssignment attribute is an optional structured attribute on user objects. Added values are interpreted by the connector as a role assignment creation and removed values are interpreted as a deletion of a role assignment. There are several elements of a roleAssignment value:

* roleId

  + Unique internal ID for the role
* roleName

  + The role’s name
* roleDescription

  + The role’s description
* scopeType

  + The scope of the assignment.
  + Must be either:

    - CUSTOMER

      * The entire domain
    - ORG\_UNIT

      * A specified org unit
      * Must specify either orgUnitId or orgUnitPath
    - orgUnitId

      * The unique internal ID for the orgUnit
    - orgUnitPath

      * The path of the orgUnit.

These elements are not all required for add or remove value elements, however, it is necessary to ensure that enough data is present in a value element to perform the task.

When adding a value for roleAssignment, the following requirements must be met:

* A role must be identified
* A scope must be specified
* If the scope is ORG\_UNIT, then an organizational unit must be specified.

When removing a value for roleAssignment, the connector must search the list of that user’s role assignments, identify the correct assignment, and delete it. A role assignment is matched by:

* Using a provided roleAssignmentId value

  + If this value is known, then it is sufficient for a remove value event.
  + roleAssignmentId values can be found by querying roleAssignment on a user.
* If the roleAssignmentId is not known or provided, an attempt will be made to find one using:

  + roleId, roleName, or roleDescription to identify the role
  + scopeType
  + orgUnitId or orgUnitPath if the scope is ORG\_UNIT

To add or remove a value for roleAssignment, the connector needs to know two or three things: the role being assigned, the scope of the assignment, and (depending on the scope) the organizational unit which is the target of the assignment.

Identifying a role can be done in one of three ways:

* Direct reference with the internal role unique ID value, roleId
* An exact match with the role name, roleName
* An exact match with the role description, roleDescription

Role ID values can be found by issuing a query into the connector for object class name “Role” and viewing the returned instance documents in the driver trace logs. Role ID values are also returned on any query for roleAssignments on user objects. Note that role ID values are unique per instance or domain and are not the same for each domain within the Google environment.

As of this writing, the default system roles have the following names and descriptions:

*Table 3-3* Default System Roles

| Admin UI Display Name | Role Name | Role Description |
| Super Admin | \_SEED\_ADMIN\_ROLE | G Suite Administrator Seed Role |
| Groups Admin | \_GROUPS\_ADMIN\_ROLE | Groups Administrator |
| User Management Admin | \_USER\_MANAGEMENT\_ADMIN\_ROLE | User Management Administrator |
| Help Desk Admin | \_HELP\_DESK\_ADMIN\_ROLE | Help Desk Administrator |
| Services Admin | \_SERVICE\_ADMIN\_ROLE | Services Administrator |

There may be other default system roles or changes to this list at any time.

For more information, see <https://support.google.com/a/answer/2405986?hl=en>.

For custom roles, the role name and role description are defined at role creation and are the same for the connector and API as what was entered during creation.

*Figure 3-5* Creating a New Role

![](../graphics/figure49.png)

For the above example custom role, the values to use for roleName and roleDescription are highlighted above.

A simple way to determine role ID, role Name, or role Description for any role would be to assign it to a user managed by the connector then querying that user for the attribute roleAssignment. The connector will populate all these elements for each assigned role.

In the following example, roleAssignment was mapped to siteLocation for testing. This is the result of a query on a test user in iManager:

*Figure 3-6* Example Query from iManager

![](../graphics/figure50.png)

And here’s the trace log:

```
<instance class-name="UserEntry" src-dn="/teststudent1@concensus-test.com">
 <association>teststudent1@concensus-test.com</association>
 <attr attr-name="RoleAssignments">
 <value type="structured">
 <component name="orgUnitPath">/Weaver</component>
 <component name="roleAssignmentId">1498736891002969</component>
 <component name="scopeType">ORG_UNIT</component>
 <component name="roleId">1498736891002894</component>
 <component name="roleName">MW Test Role 1</component>
 <component name="orgUnitId">03gre1hq2n7bt2m</component>
 <component name="roleDescription">Weaver testing role 1</component>
 </value>
 <value type="structured">
 <component name="orgUnitPath"/>
 <component name="roleAssignmentId">1498736891002970</component>
 <component name="scopeType">CUSTOMER</component>
 <component name="roleId">1498736891002893</component>
 <component name="roleName">_PLAY_FOR_WORK_ADMIN_ROLE</component>
 <component name="orgUnitId"/>
 <component name="roleDescription">Play For Work Administrator</component>
 </value>
 <value type="structured">
 <component name="orgUnitPath"/>
 <component name="roleAssignmentId">1498736891002971</component>
 <component name="scopeType">CUSTOMER</component>
 <component name="roleId">1498736891002886</component>
 <component name="roleName">_SEED_ADMIN_ROLE</component>
 <component name="orgUnitId"/>
 <component name="roleDescription">Google Apps Administrator Seed Role</component>
 </value>
 </attr>
</instance>
```

From these examples, you can see how the role identifiers are present in the roleAssignment query.

To specify an organizational unit, either the orgUnitId or orgUnitPath must be specified. The orgUnitId is the internal identifier for the organizational unit within Google. This can be determined by querying the OrgUnit and reading the attribute named OrgUnitId.

Example OrgUnitId:

```
<instance class-name="Organizational Unit" src-dn="/AK/NL">
 <association>/AK/NL</association>
 <attr attr-name="OrgUnitId">
 <value>id:03gre1hq4d6ldwa</value>
 </attr>
 <attr attr-name="OU">
 <value>NL</value>
 </attr>
 <attr attr-name="Description">
 <value/>
 </attr>
 <attr attr-name="BlockPolicy">
 <value>false</value>
 </attr>
</instance>
```

Alternately, the orgUnitPath can be specified. For the above example, the OrgUnitPath is the association value or source DN: /AK/NL.

If the connector cannot find a role, org unit, or role assignment to add/remove role assignments, then no operation is performed, and an error is returned.

Note that when matching on roleName or roleDescription, the first match is used, in the event multiple roles match.

## 3.4.3 Examples

### Add Value

```
<modify-attr attr-name="roleAssignment">
 <add-value>
 <value type="structured">
 <component name="roleDescription">Weaver testing role 1</component>
 <component name="scopeType">ORG_UNIT</component>
 <component name="orgUnitPath">/Weaver</component>
 </value>
 </add-value>
 </modify-attr>
```

### Remove Value

```
<modify-attr attr-name="roleAssignment">
 <remove-value>
 <value type="structured">
 <component name="roleDescription">User Management Administrator</component>
 <component name="scopeType">CUSTOMER</component>
 <component name="orgUnitPath"/>
 </value>
 </remove-value>
 </modify-attr>
</modify>
```
