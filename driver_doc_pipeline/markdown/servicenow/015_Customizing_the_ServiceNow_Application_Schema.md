# 4.2 Customizing the ServiceNow Application Schema

The Schema Mapping policy is contained in the driver object and applies to the Subscriber channel. The purpose of the Schema Mapping policy is to map schema names (particularly attribute names and class names) between the Identity Vault namespace and the ServiceNow namespace. Do not modify or remove existing entries in the Schema Mapping policy. You can, however, add entries to the Schema Mapping policy.

[Table 4-1](customize-servicenow-application-schema.html#b1i9ghw4) and [Table 4-2](customize-servicenow-application-schema.html#b1i9hxhz) list the default attributes that are supported in ServiceNow.

*Table 4-1* sys\_user

| Attributes | Type |
| Accumulated roles | String |
| Active | True/False |
| Building | reference to Building |
| Business phone | Phone Number |
| Calendar Integration | Integer |
| City | String |
| Class | System Class Name |
| Company | reference to Company |
| Cost center | reference to Cost Center |
| Country code | String |
| Created | date/Time |
| Created by | String |
| Date Format | String |
| Default perspective | reference to Menu List |
| Department | reference to Department |
| Domain | Domain ID |
| EDU Status | String |
| Email | Email |
| Employee number | String |
| Failed login attempts | Integer |
| First name | String |
| Email | Email |
| Employee number | String |
| Failed login attempts | Integer |
| First name | String |
| Gender | String |
| Home Phone | Phone Number |
| internal Integration User | True/False |
| LDAP Server | reference to LDAP Server |
| Language | String |
| Last login | Date |
| Last login device | String |
| Last login time | date/Time |
| last name | String |
| Last password | String |
| Location | reference to Location |
| Locked out | True/False |
| Manager | reference to User |
| Middle name | String |
| Mobile phone | Phone Number |
| Name | String |
| Notification | Integer |
| Password | Password (1 Way Encrypted) |
| Password needs reset | True/False |
| Photo | Image |
| Prefix | String |
| Roles | User Roles |
| Schedule | reference to Schedule |
| Source | String |
| State/Province | String |
| Street | Two Line Text Area |
| Sys ID | Sys ID |
| Time format | String |
| Time zone | String |
| Title | String |
| Updated | Date/Time |
| Updated by | String |
| Updates | Integer |
| User ID | String |
| VIP | True/False |
| Web service access only | True/False |
| Zip/Postal code | String |

*Table 4-2* sys\_user\_group

| Attributes | Type |
| Active | True/False |
| Cost Center | reference to Cost Center |
| Created | Date/Time |
| Created by | String |
| Default assignee | reference to User |
| Description | String |
| Exclude manager | True/False |
| Group email | Email |
| Hourly rate | Currency |
| Include members | True/False |
| manager | reference to User |
| Name | String |
| Parent | reference to Group |
| Roles | User Roles |
| Source | String |
| Sys ID | Sys ID |
| Type | List |
| Updated | Date/Time |
| Updated by | String |
| Updates | Integer |

ServiceNow also supports other attributes in addition to the default attributes. The attributes are available in the custom schema file packaged in the NIdM\_Driver\_4.5\_ServiceNow.zip file. For more information about using the schema file, see [Use Custom Application Schema.](create-driver-object-designer.html#b1i9wb57)
