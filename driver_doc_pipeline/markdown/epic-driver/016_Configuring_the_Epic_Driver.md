# 2.11 Configuring the Epic Driver

This section discusses and outlines the configuration to be set to use the Epic Driver.

When configuring the driver, a decision must be made as to whether the driver will provision EMP accounts or SER records. As a driver may only maintain a single association per user, both EMP and SER may not be configured on the same driver instance as that would require two associations for the same instance. The “Epic Base” package is applied to the driver regardless of whether it is intended to provision EMP accounts or SER records. However, the primary functionality of the instance is determined by the application of either the “Epic EMP Default Configuration” package or the “Epic SER Default Configuration” package and the matching entitlement package.

## 2.11.1 Configuration for the Driver Set - Common Settings

| Parameter | Description |
| User Container | DN of base container for user objects. |

## 2.11.2 Configuration for the Epic driver - Authentication

| Parameter | Description |
| Authentication ID | ID of the Epic Service Account. The format is emp$<ID>. |
| Set Password | Password of the Epic Service Account. |
| Connection Information | URL of the Epic Interconnect Server endpoint. |

## 2.11.3 Driver Parameters

The following driver parameters are set for the Epic EMP driver

### Driver Options

| Parameter | Description |
| Epic Version | Version of the Epic implementation. This determines the Epic schema supported by the driver. |
| Epic Environment | Select Production or Non-Production. |
| ID Types | A list of custom ID types (Item 20700/20701) to support. This is implementation specific and generally not needed.  When an ID type is added here it will show in the Schema as IDType-<value>. The value listed here comes from the ID type descriptor under Names in Other Systems in the ID type definition in Epic.  *NOTE:*In the ID Type definition under the ID Rules tab in Epic, the Method must be user entered or system generated. |
| Trust All Certs | Select Yes or No. This configures the driver whether to trust all certs when establishing the https connection to the Epic SOAP endpoint (there are security risks associated with utilizing this functionality as it can open the system to potential MIM attacks). |
| Enable Data Courier Log File | Select Yes or No. |
| Force Contact on all Updates | Select Yes or No. If set to yes, Epic will create a new contact record on every update from the driver. |
| Audit User | External ID of the user in Epic that will be identified as the creator of a new records. Generally, this is left blank. |
| Audit User Password | Audit user’s password. |
| Audit User IDType | ID type of the audit user’s ID. Generally, this is External. |
| SER Configuration | Select Show or Hide. Select Show when the Epic driver is to be used for SER record management. |
| Custom Attribute for SER ID in Epic | SER record identifier INI Descriptor. For example, PDS. Epic requires each customer to have a unique Epic identifier to hold the SER record ID, similar to an NPI identifier. If a desired type does not already exist, a new Epic type will need to be created. |
| Custom Attribute Type for SER ID in Epic | SER record identifier INI # for the above type. For example, 200. |
| SER Blueprint Override | Default value (1) allows overriding assigned Blueprints in Epic. |

### Driver Options (EMP Specific)

These driver options are GCV references to the “Epic EMP Default Configuration” Global Configuration Values. Refer to the package “Readme” for instructions on how to install these parameters.

| Parameter | Description |
| Epic Date Format | Format pattern for dates, as configured in Epic environment. For example, "MM-dd-yyyy" or "yyyy.MM.dd" |
| Custom Epic ID Types | List of custom ID types to support (Example value: "POS\_VENDOR\_ID"). This is implementation specific and generally isn't needed. |
| Matching Attribute | Identity Vault (eDirectory) attribute to use when matching Epic records. For example, “CN” or “workforceID” |
| Matching ID Type | Epic ID Type to use when searching for Epic records. For Example, “SystemLogin” |

### Driver Options (SER Specific)

These driver options are GCV references to the “Epic SER Default Configuration” Global Configuration Values. Refer to the package “Readme” for instructions on how to install these parameters

| Parameter | Description |
| SER Configuration | Select Show or Hide. Select Show when the Epic driver is to be used for SER record management. |
| Custom Attribute for SER ID in Epic | SER record identifier INI Descriptor. For example, PDS. Epic requires each customer to have a unique Epic identifier to hold the SER record ID, similar to an NPI identifier. If a desired type does not already exist, a new Epic type will need to be created. |
| Custom Attribute Type for SER ID in Epic | SER record identifier INI # for the above type. For example, 200. |
| SER Blueprint Override | Default value (1) allows overriding assigned Blueprints in Epic. |

## 2.11.4 Global Configuration Values

Global configuration values (GCVs) are values that can be used to control policy functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set while driver GCVs can only be used by the driver on which they are defined

### Driver GCV Configuration

This section discusses and outlines the GCV configuration of the Epic Driver.

#### Custom Entitlements

| Parameter | Description |
| List of Custom Entitlements | List of entitlement names that the driver will process during a CodeMapRefresh request.  For EMP record management, the default entitlements supported by the driver are AppliedTemplate, AvailableTemplate, DefaultTemplate, ExternalIdentifier, InBasketClassification, Subtemplate, and UserAccount.  For SER record management, the default entitlements supported by the driver are Blueprint and SERRecord. |

#### Common Password Settings

| Parameter | Description |
| Set default password if not available | Select Yes to set a default password if password element is not available in a user add event. This controls how the \*-cp-DefaultPassword policy executes. |

### EMP Default Configuration

#### Account Activation and Deactivation Activities

| Parameter | Description |
| Action to take when ‘User Account’ is deleted in IDV | Select Inactivate Account or Block Account. |
| Value for IsBlocked | Select True or False. When Inactivate Account is selected above, this tells policies to also set the Epic record’s IsBlocked value to True or False. |
| Text to send as ‘Block Comment’ | When True is selected above, this value is included to document the reason why the record was blocked. |
| Text to send as ‘Block Comment’ | When Block Account is selected above, this value is included to document the reason why the record was blocked. |
| Value for IsActive | Select True or False. When Block Account is selected above, this tells policies to also set the Epic record’s IsActive value to True or False. |
| Synchronize ‘Login Disabled’ attribute | Select whether the changes made to the 'Login Disabled' attribute in IDVault should be synced. |
| Value for IsBlocked | Select True or False. When Inactivate Account is selected above, this tells policies to also set the Epic record’s IsBlocked value to True or False. |
| Text to send as ‘Block Comment’ | When True is selected above, this value is included to document the reason why the record was blocked. |
| Text to send as ‘Block Comment’ | When Block Account is selected above, this value is included to document the reason why the record was blocked. |
| Value for IsActive | Select True or False. When Block Account is selected above, this tells policies to also set the Epic record’s IsActive value to True or False. |
| Synchronize Account Lockout | Select Yes or No. This tells policies whether to the set the Epic record’s IsBlocked status when the IDV user account is locked by intruder detection. |

#### Account Naming Activities

| Parameter | Description |
| Should Epic generate the ‘UserInternalID’ value | Select Yes or No. When Yes is selected, the IDV attribute that is mapped to UserInternalID in the Schema Mapping policy will be used for a new Epic record's UserInternalID field.  *NOTE:*If Yes is selected and the mapped IDV user attribute contains no value, then the driver will return an error when attempting to create a new Epic record.  When No is selected, Epic will auto generate the UserInternalID value when creating a new Epic record. |
| Custom Epic ID Types | List of custom ID types to support (Example value: "POS\_VENDOR\_ID"). This is implementation specific and generally isn't needed. |
| Matching Attribute | Identity Vault (eDirectory) attribute to use when matching Epic records. For example, “CN” or “workforceID”. |
| Matching ID Type | Epic ID Type to use when searching for Epic records. For Example, “SystemLogin”. |

#### SER Record Integration

| Parameter | Description |
| Attribute that holds the SER ID for providers | IDV attribute that holds the SER record ID for a linked SER record. Default is CN. |
| Attribute MPI ID type that links the SER ID for providers | What is the MPI ID type of the SER ID link attribute. |
| Attribute that triggers the linking of EMP to SER | The boolean attribute that triggers the linking of an SER record to an EMP record. |

#### Start and End Date Attributes

| Parameter | Description |
| Epic Date Format | Format pattern for dates, as configured in Epic environment. For example, "MM-dd-yyyy" or "yyyy.MM.dd". |
| Start Date Attribute | The attribute in eDirectory that holds the start date. |
| Is the start date attribute a string or timestamp? | Is the start date a string or timestamp (eDirectory attribute type “Time”). |
| Start Date Format | Format pattern for dates, as expected in the source attribute. For example, "MM-dd-yyyy" or "yyyy.MM.dd". |
| End Date Attribute | The attribute in eDirectory that holds the end date. |
| Is the end date attribute a string or timestamp? | Is the end date a string or timestamp (eDirectory attribute type “Time”). |
| End Date Format | Format pattern for dates, as expected in the source attribute. For example, "MM-dd-yyyy" or "yyyy.MM.dd". |

### EMP Entitlements

| Parameter | Description |
| Enable UserAccount Entitlement | Select Yes or No. Entitlements act like an ON/OFF switch to control account access. When the driver is enabled for entitlements, accounts are only created or disabled when the account entitlement is granted to or revoked from user accounts.  Entitlements are granted and revoked by entitlement agents. Three entitlement agents ship with Identity Manager:  * Role-Based Entitlements (RBE): RBE is ideal for simple automation. For example, when a user is added to the HR system, the user is automatically granted accounts in other systems * Workflow: Workflow is ideal for approvals. For example, when a user is added to the HR system, the manager must approve the accounts for the user. * Roles Based Provisioning Module (RBPM): RBPM is ideal for true and full-featured roles based provisioning. For example, when a user is added to the Accounting role, the user automatically receives all accounts associated with the accounting role.  If Yes is selected, one of these entitlement agents must be installed and configured for the driver to create and delete accounts. For more information, see the [Identity Manager Entitlements Guide](https://www.netiq.com/documentation/identity-manager-48/entitlements/data/identity-manager-entitlements.html).  *NOTE:*Synchronization of Login Disabled is independent of this setting. |
| Action to take when ‘UserAccount’ entitlements is revoked | Select Inactivate Account or Block Account. This is the action to take when the UserAccount entitlement is revoked from a user account.  Inactivate Account prohibits record assignments in Epic.  Block Account prevents user login in Epic. |
| Text to send as ‘Block Comment’ | When Block Account is selected above, this value is included to document the reason why the record was blocked. |
| Should the account also be deactivated | Select Yes or No. When Yes is selected and Block Account is selected above, policies also Inactivate Account. |
| Enable External Identifier Entitlement | Select Yes or No. Enables the management of External Identifiers via entitlements. |
| Enable ‘InBasketClassification’ Entitlement | Select Yes or No. Enables the management of In Basket Classifications via entitlements. |
| Enable ‘Subtemplate’ Entitlement | Select Yes or No. Enables the management of Sub-Templates via entitlements. |
| Enable ‘AvailableTemplate’ Entitlement | Select Yes or No. Enables the management of Available Template via entitlements. |
| Enable ‘DefaultTemplate’ Entitlement | Select Yes or No. Enables the management of Default Templates via entitlements. |
| Enable ‘AppliedTemplate’ Entitlement | Select Yes or No. Enables the management of Applied Templates via entitlements. It is recommended that this value is set to "No" as updating Applied Templates to currently logged in users is not supported in Epic. |

### SER Default Configuration

SER ID Configuration – Required Values

| Parameter | Description |
| Identity Vault attribute to map to SER ID | Select Inactivate Account or Block Account. |
| Custom Attribute for SER ID in Epic | SER record identifier INI Descriptor. For example, PDS. Epic requires each customer to have a unique Epic identifier to hold the SER record ID, similar to an NPI identifier. If a desired type does not already exist, a new Epic type will need to be created. |
| Custom Attribute Type for SER ID in Epic | SER record identifier # for the above type. For example, 200. |
| Matching Attribute for SER Record | IDV attribute to use for matching operations. |
| SER Blueprint Override | Enter 0 when a Blueprint is added, and it should not override a pre-existing blueprint.  Enter 1 when a Blueprint is added, and it should override a pre-existing blueprint. |
| Attribute that triggers the linking of EMP to SER | The boolean attribute that triggers the linking of an SER record to an EMP record. |

SER ID Configuration – Provider Address Mapping (Epic 21000 Attributes)

| Parameter | Description |
| Do providers have a single location or multiple locations? | If providers work only at a single location or if the provider address is a JSON formatted attribute, select "Single." If providers have multiple facility addresses associated with their records, select "Multiple."  The attributes listed here MUST BE ENABLED in the driver filter as "notify" attributes on the Subscriber channel. DO NOT map these attributes in the driver's Schema Map. |
| Multiple Addresses – Must be multi-valued string stored in JSON format – Ensure attribute is in the driver filter as ‘notify’ on Subscriber Channel | |
| Provider Address Attribute | The name of the attribute that contains the provider address. This attribute must be a multi-valued attribute and the values must be stored in JSON string format. |
| Single Address – Ensure attributes are in driver filter as ‘notify’ on Subscriber Channel | |
| Provider Street Address Attribute | The name of the attribute that contains the provider street address (Epic SER 21010). |
| Provider Street Address (2) Attribute | The name of the attribute that contains the provider street address (2) (Epic SER 21020). |
| Provider Street Address (3) Attribute | The name of the attribute that contains the provider street address (3) (Epic SER 21030). |
| Provider City Attribute | The name of the attribute that contains the provider city (Epic SER 21040). |
| Provider State Attribute | The name of the attribute that contains the provider state (Epic SER 21050). |
| Provider Zip Code Attribute | The name of the attribute that contains the provider zip code (Epic SER 21060). |
| Provider Country Attribute | The name of the attribute that contains the provider country (Epic SER 21080). |
| Provider Phone Attribute | The name of the attribute that contains the telephone number (Epic SER 21100). |
| Provider Fax Attribute | The name of the attribute that contains the facsimile (fax) number (Epic SER 21110). |
| Provider Email Attribute | The name of the attribute that contains the provider's email address (Epic SER 21130). |

### Epic SER Entitlements Configuration

| Parameter | Description |
| Use SER Account Entitlement | Select true or false. Entitlements act like an ON/OFF switch to control account access. When the driver is enabled for entitlements, accounts are only created or disabled when the account entitlement is granted to or revoked from user accounts.  Entitlements are granted and revoked by entitlement agents. Three entitlement agents ship with Identity Manager:  * Role-Based Entitlements (RBE): RBE is ideal for simple automation. For example, when a user is added to the HR system, the user is automatically granted accounts in other systems * Workflow: Workflow is ideal for approvals. For example, when a user is added to the HR system, the manager must approve the accounts for the user. * Roles Based Provisioning Module (RBPM): RBPM is ideal for true and full-featured roles based provisioning. For example, when a user is added to the Accounting role, the user automatically receives all accounts associated with the accounting role.  When true is selected, one of these entitlement agents must be installed and configured for the driver to create and delete accounts For more information, see the [Identity Manager Entitlements Guide](https://www.netiq.com/documentation/identity-manager-48/entitlements/data/identity-manager-entitlements.html). |
| Use Blueprint Entitlement | Select true or false. Enables the management of Blueprints via entitlements. |
| Blueprint Required for User Create | Select Yes or No. When Yes is selected and Use Blueprint Entitlement is true, user add operations will be vetoed if a Blueprint entitlement is not present. |
