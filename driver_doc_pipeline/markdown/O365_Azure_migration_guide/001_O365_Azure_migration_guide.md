# Office365 to Azure AD Migration Tool Readme

As Microsoft has called out the end of support for Basic Authentication access to Exchange Online API’s for Office365, the Office365 driver will be deprecated. As there will be no further updates to Office365 driver, you must now use the Azure AD driver to connect to the Office365/Azure account. A migration tool is developed for customers to migrate from the existing O365 driver to the Azure AD driver. The tool automates the migration of resources from the Office365 driver to Azure AD driver, but retains the historical data, such as Resource assignments and its history.

This document comprises the following sections:

* [Overview](#Overview)
* [System Requirements](#System_Requirements)
* [Handling License Resources and Custom License Resources](#Handling_Licenses)
* [Migrating Custom Polices from Office365 to Azure AD Driver](#migrate_cust_policies)
* [Test the Python Version on your Machine](#test_python_version)
* [Verifying the Availability of the Required Modules](#verify_required_modules)
* [Migrating Office365 Driver to Azure AD Driver](#migrate_o365toAzure)
* [Steps Executed as a Part of Migration Process](#Execution_steps)

## Overview

The migration tool helps a user to:

* Automate the migration of resources from Office365 to Azure AD driver.
* Manage the access permissions of existing resources and their roles without any data loss.
* Retain the historical data of all the operations that were performed on resources in Office365 driver.
* Manage all the resources of Office365 driver using the new Azure AD driver post migration.

**IMPORTANT**: Prior to running the migration tool, it is mandatory to migrate all the Office365 license and custom license resources manually.

The migration tool does not migrate the following:

+ Licence and custom license resources. For more information, see [Handling License Resources and Custom License Resources](#Handling_Licenses).
+ The custom policies configured in the Office365 driver. (They should be manually configured in Azure AD driver. For more information, see [Migrating Custom Polices from Office 365 to Azure AD Driver](#migrate_cust_policies)).

## System Requirements

* Identity Manager running on Linux or Windows
* Python 3.6 or later with *request*, *ldap3* and *urllib3* modules

## Handling License Resources and Custom License Resources

**Important**: Migrating Licence Resources and Custom Licence Resources would trigger a sync and generate traffic.

### Migrating License Resources

1. Make a note of all the license resources that were created using the Office365 driver.
2. Log in to the Identity Manager Dashboard.
3. Using the Azure AD driver, create a resource for every service plan. The number of resources must be individually created per service plan.
4. Create a role that will represent a license and map the resources (to the role) for every service plan that the license contains. Repeat this step if there are multiple licenses in your environment.
5. Assign the role, with the corresponding entitled licenses, to each user.

### Migrating Custom License Resources

1. Review all the created Custom License Resources with the Office365 Driver, and make a note of all the resource assignments and the service plans that are restricted by each Custom License Resource.
2. Remove the existing assignments of Licence and Custom License Resources that were created using the Office365 driver.
3. Create new resources using Azure AD Driver for each License (service plan).
4. In the Identity Manager Dashboard, create a role and map all the licence resources, excluding the one that is specified in the custom license.
5. Repeat step 4, for all the custom resources identified in your environment you want to grant permissions or assign to a particular user or users.

For example, if a configured Custom License restricts a user from assigning the service plan *EXCEL\_PREMIUM* and assigns all other plans, then you must first create a Role and then map all the License resources except for the resource for *EXCEL\_PREMIUM* service plan. You can then assign this Role to all the desired users.

## Migrating Custom Polices from Office365 to Azure AD Driver

You must migrate the custom policies from Office365 driver to Azure AD driver manually. To migrate, you must first export the custom policies from Office365 driver and then import them to the Azure AD driver.

### Exporting Custom Policies from Office365 Driver

1. Open the project in Designer.
2. In the Outline view, navigate to Office365 driver and select the custom policies of the Office365 driver to export.
3. Right-click and select **Export to Configuration File**.
4. Select a location to export the policies.
5. Click **Save > OK**.

### Importing Custom Policies to Azure AD Driver

1. Open the project in Designer.
2. In the Outline view, right-click the Azure AD driver and select **Import from Configuration File**.
3. Click **Browse** and navigate to the location where the custom policies of Office365 are exported.
4. Select the exported policies and click **Open > OK**.

## Test the Python Version on your Machine

Enter the following commands as required to test the python versions installed in your machine:

* *python3 --version* - if your machine is having both python 2 and 3 versions.
* *python --version* - if your machine is having only python 3.

## Verifying the Availability of the Required Modules

1. Enter the command to verify the required module is present in your machine:

* *pip3 list*: If both python 2 and 3 are present in the machine.
* *pip list*: If only python 3 is present in the machine.

- Ensure the modules *request*, *ldap3* and *urllib3* entries are present. If the entries are not listed, install the required module with the command:
  *pip install [module name]* or *pip3 install [module name]*.

  ## Migrating Office365 Driver to Azure AD Driver

  You must perform the following steps to migrate Office365 to Azure AD driver:

  **NOTE**: It is recommended to run the migration tool on a different server to avoid high utilization of CPU memory in Identity Manager server.

  1. Ensure that the Azure AD driver is deployed and running.

  2. Shutdown and disable the Office365 driver.

  **NOTE**: Disabling this driver ensures that none of the events are stored in the driver cache.

  3. Perform one of the following procedures to flush the Identity Manager Dashboard cache.

  1. Log in to the Identity Manager Dashboard.
  2. Navigate to the **Configuration** page.
  3. Click **Cache and Cluster**.
  4. Select **All Cache**, if not defaulted already.
  5. Click **Flush Cache**.

  or
  1. Stop the Tomcat service.
  2. Delete the *permindex* directory from the Tomcat temp directory.
  * **Linux**: */opt/netiq/idm/apps/tomcat/temp*
  * **Windows**: *C:\NetIQ\IDM\apps\tomcat\temp*3. Start the Tomcat service.
  **NOTE**: Migration tool sends queries to the Identity Manager Dashboard cache to fetch roles, resources, and their assignments. Hence, it is recommended to flush the cache of the Identity Manager Dashboard prior to running the migration tool. This ensures that all the recent changes in IDMDash are fetched.

- (Conditional) On Linux, run the following commands:

1. NCPCLIENT\_REQ\_TIMEOUT= <timeout in seconds>

For example, NCPCLIENT\_REQ\_TIMEOUT= 9000

2. export NCPCLIENT\_REQ\_TIMEOUT

**NOTE**: This setting is valid until the session is closed. By default, the NCP connection has a timeout of 115 seconds. If the total time of the query plus returning results exceeds that value, *dxcmd* exits with error 143. By setting the NCPCLIENT\_REQ\_TIMEOUT to a larger value (for example, 1200 seconds), increases the amount of time that the operation is allowed to execute. Since the value is in seconds, a setting of 1200 seconds would allow the operation to execute up to 20 minutes.

- (Conditional) On Windows, perform the following steps to add the NCPCLIENT\_REQ\_TIMEOUT as an environment variable:

1. On the Windows taskbar, right-click the **Windows** icon and then select **System**.
2. Click **Advanced system settings** under **Related settings**.
3. On the **Advanced** tab, click **Environment Variables**.
4. Click **New** and add the environment variable.
5. Click **OK** and then click **OK**.

- Create a custom directory to extract the contents of migration tool.

- Unzip the <*migrationtool.zip*> file.

- Run the *python36 Driv-AzureAD-Office365MigrationTool.py* script.

*python36 Driv-AzureAD-Office365MigrationTool.py -host <IP address or hostname of the Identity Vault server> -user <Identity Vault Administrator name> -password <Identity Vault Administrator password> -ncp 524 -ssl <specify whether you want to connect through SSL> -ldaps 636 -uauser <Identity Applications Administrator Name> -uapass <Identity Applications Administrator Password> -container <User Search Container DN> -log <log level> -url <Identity Applications URL> -o365 <Office365 Driver DN> -azure <Azure AD Driver DN>*

For example:

*python36 Driv-AzureAD-Office365MigrationTool.py -host 192.168.0.25 -user cn=admin,ou=sa,o=system -password novell -ncp 524 -ssl Yes -ldaps 636 -uauser uaadmin -uapass novell -container o=data -log DEBUG -url https://identityapplications.example.com/IDMProv -o365 "cn=MSOffice365,cn=driverset1,o=system" -azure cn="AzureDriver,cn=driverset1,o=system"*

**NOTE:** For help on using the migration script, run the *python36 Driv-AzureAD-Office365MigrationTool.py -h* command.

Alternatively, you can run the *python36 Driv-AzureAD-Office365MigrationTool.py* script and then specify the following details when prompted:

| Input Prompt | Sample Values |
| --- | --- |
| Enter IP Address of the IDM Server (IDVault) | *<IP address or hostname of the Identity Vault server>*  For example, *192.168.0.25* |
| Enter the IDM Server admin | *<Identity Vault Administrator name>*  For example, *cn=admin,ou=sa,o=system* |
| Enter Password for the IDM Server admin | *<Identity Vault Administrator password>*  For example, *novell* |
| Enter the IDM Server NCP port | Enter the NCP port to run *dxcmd* commands. The default port is 524. **NOTE**: The default port is used, if a custom port is not specified. The port must be specified manually. | Enter the base container of the users | Enter the container where the user objects exist.  For example, *o=data* | | SSL enabled? Yes or No | Enter Yes if "Require TLS for Simple Bind is Yes". | | Enter the IDM Server LDAP port | Enter the LDAP port. You must specify these values manually. The default values are appended, if no values are specified. The default values are:  * For SSL enabled LDAP port: 636 * For non SSL LDAP port: 389 | | Enter Office365 driver DN | *<Office365 Driver DN>*  For example, *cn=MSOffice365,cn=driverset1,o=system* | | Enter Azure driver DN | *<Azure AD Driver DN>*  For example, *cn=AzureDriver,cn=driverset1,o=system* | | Enter name of userapp admin | *<Identity Applications Administrator Name>*  For example, *uaadmin* | | Enter Password for userapp admin | *<Identity Applications Administrator Password>*  For example, *novell* | | Enter IDM UserApps URL | *<Identity Applications URL>*  For example, *https://identityapplications.example.com/IDMProv* | |

The migration tool executes once all the values are provided. For more information on the execution steps, see [Steps Executed as part of Migration.](#Execution_steps)

**NOTE**: You must ensure that the migration tool executes with no errors. The migration will be unsuccessful if errors persist.

## Steps Executed as a Part of Migration Process

1. During the execution process, all the entitlements are queried based on the driver DN provided.
2. Post querying, a mapping file is created which contains the list of driver and entitlement DN to be converted from Office365 to Azure.
3. The mapping file also contains the entitlement mapping values of Office365 to Azure AD. Based on the mapping file values, the tool updates the following attributes:
   * *nrfAssignedResources* and *DIRXML-EntitlementRef* of user objects.
   * *nrfEntitlementRef* and *nrfResourceParms* of resource objects.
   * *nrfDynamicParmVals* of resource association objects in advanced installation edition, and
   * only the *DIRXML-EntitlementRef* attributes of the user in the standard installation edition.

   **NOTE**: The updates for the above mentioned attributes are executed through LDAP commands.
