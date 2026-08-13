# 2.3 Creating Integration System Group(s) and User(s) in Workday Application

Before you can install and configure the Workday driver, you must create Integration System Security Group(s) containing Integration System User(s) in the Workday application. Ensure that the Integration System User has all the required permissions before installing the driver. Perform the following steps to create Integration System Groups and Users:

* [Creating Integration System Security Group(s)](t4cyxdli4lue.html#t4cyxgwrwqtm)
* [Create Integration System](t4cyxdli4lue.html#t4k2djif90kb)
* [Creating Integration System User(s)](t4cyxdli4lue.html#t4cyxhcnxch0)

## 2.3.1 Creating Integration System Security Group(s)

1. Access the Create Security Group task and create an Integration System Security Group.
2. To grant the security group access to the domains required by your integration, perform the following steps for each domain:

   * Access the View Domain report and find the domain.
   * Select Domain > Edit Security Policy Permissions.
   * Add the security group that you created in [Step 1](t4cyxdli4lue.html#int-sec-grp-wrkdy-step1) to the Integration Permissions and select Get and Put.
   * Access the Activate Pending Security Policy Changes task and activate the changes that you made in previous step.

Once the Integration System Security Group has been created, you must provide the following rights to the group:

* [Domain Rights for the Security Group:](t4cyxdli4lue.html#t4cyzfqqq1v5)
* [Domain Rights for Assignable Role-Based Security Group Entitlement](t4cyxdli4lue.html#t4gen9j2gyw1)
* [Domain Rights for User-Based Security Group Entitlement](t4cyxdli4lue.html#t4gen9s9q8p7)
* [Business Process Types Rights for the Security Group](t4cyxdli4lue.html#t4cyzjmq5l2t)

### Domain Rights for the Security Group:

You can provide the following domain read rights to the security group based on your requirements:

| Domain Rights | Description |
| Job Information | Provide this right if you want to synchronize the job information for the group users. Select only Get option for this right. |
| Manage: Location | Provide this right if you want to synchronize the location data for the group users. Select only Get option for this right. |
| Manage: Organization Integration | Provide this right if you want to synchronize the Organization data. Select only Get option for this right. |
| Person Data: Date of Birth | Provide this right if you want to synchronize the worker’s date of birth. Select only Get option for this right. |
| Person Data: Gender | Provide this right if you want to synchronize the worker’s gender information. Select only Get option for this right. |
| Person Data: ID Information | Provide this right if you want to synchronize the worker’s other IDs. Select both Get and Put options for this right. |
| Person Data: Personal Photo | Provide this right if you want to synchronize the worker’s photo from both channels. Select Get, Put, View and Modify options for this right. |
| Workday Accounts | This right should be provided to the security group by default. Select both Get and Put options for this right. |
| Worker Data: All Positions | Provide this right if you want to synchronize all position data help by the worker. Select both Get and Put options for this right. Select only Get option for this right. |
| Worker Data: Current Job Profile Information | Provide this right if you want to synchronize the worker’s current job profile information. Select only Get option for this right. |
| Worker Data: Organization Information | Provide this right if you want to synchronize the worker’s Organization information. Select only Get option for this right. |
| Worker Data: Public Worker Reports | Provide this right if you want to synchronize the public worker reports. Select only Get option for this right. |

### Domain Rights for Assignable Role-Based Security Group Entitlement

You can provide the following rights to the assignable role entitlement based on your requirements:

| Domain Rights | Description |
| Manage: Organization Roles | Provide this right if you want to synchronize the Organization roles. Select Put option for this right. |
| Org Designs: Assign Roles | Provide this right if you want to assign roles for the organization. Select Put option for this right. |

### Domain Rights for User-Based Security Group Entitlement

You can provide the following domain rights to the user-based security group entitlement based on your requirements:

| Domain Rights | Description |
| User-Based Security Group Administration | The administration rights provided to the user-based security group. Select both Get and Put options for this right. |

### Business Process Types Rights for the Security Group

You can provide the initiate access to the following business process types rights based on your requirements:

| Business Process Types Rights | Description |
| Contact Change | Provide this right if you want to synchronize the contact change information of the worker. |
| Edit Other IDs | Provide this right if you want to synchronize the edit other IDs information of the worker. |

## 2.3.2 Create Integration System

1. Access Create Integration System.
2. Input System Name.
3. Input (optional) Comment and Integration Tags under System ID.
4. Provide “Cloud Integration Template” as value to New Using Template.
5. Click OK.

## 2.3.3 Creating Integration System User(s)

1. Access the Create Integration System User task and configure a system user account for the integration. Set the Session Timeout Minutes to its default value of 0 to prevent session expiration. An expired session can cause the integration to time out before it successfully completes.
2. Select Security Profile > Assign Integration System Security Groups.
3. In the Integration System Security Group to Assign screen, select the security group that you created in [Creating Integration System Security Group(s)](t4cyxdli4lue.html#t4cyxgwrwqtm).
4. Create the Integration System following the steps listed in [Create Integration System](t4cyxdli4lue.html#t4k2djif90kb).
5. Access View Integration System Report and select the Integration System that has been created.
6. Select Workday Account > Edit Account for Integration System and select the Workday account that you created in [Step 1](t4cyxdli4lue.html#int-sys-sec-user-step1).
7. (Optional) Under the Global Preferences option, select a preferred locale and display language for the integration system user.
8. Access the Maintain Password Rules task and add the integration system user to the System Users exempt from password expiration field.
