# 8.0 Understanding the Schema Mapping

The default Sentinel Identity Tracking packages apply a schema mapping between Identity Vault attributes and the corresponding Sentinel attributes. At a high level, information about each user identity in the Identity Vault is mapped to the USR\_IDENTITY table in the Sentinel database and information from each identity's multi-value DirXML-Accounts attribute is mapped to the USR\_ACCOUNT table. The driver maps each account to the incoming event stream, retrieves the associated Identity information from the Identity Vault, and sends the information about the user identity to the Sentinel database.

The following table describes how the Identity Vault attributes are mapped to the Sentinel USR\_IDENTITY table and where the associated value is placed for events that match any associated accounts:

*Table 8-1* Mapping in USR\_IDENTITY Table

| Identity Vault Attribute/Metadata | Sentinel Column | Event Field and Comments |
| Not applicable (NA) | IDENTITY\_GUID | InitiatorUserIdentityID  TargetUserIdentityID  Sentinel generates these fields internally. |
| srcDN | DN |  |
| NA | CUST\_ID | This field is set based on the tenant ID assigned to each Identity Tracking Integration Module for Sentinel, when Sentinel is receiving data for multiple tenants. |
| NA | VAULT\_NAME | This is field is set to the eDirectory tree name. |
| GUID | SRC\_IDENTITY\_ID | Stores the Identity Vault GUID. |
| workforceID | WFID | pInitiatorUserWorkforceID  TargetUserWorkforceID |
| Given Name | FIRST\_NAME |  |
| Surname | LAST\_NAME |  |
| Full Name | FULL\_NAME | InitiatorUserFullName  TargetUserFullName |
| Title | JOB\_TITLE |  |
| OU | DEPARTMENT\_NAME | InitiatorUserDepartment  TargetUserDepartment |
| mailstop | OFFICE\_LOC\_CD |  |
| Internet Email Address | PRIMARY\_EMAIL | InitiatorEmail  TargetEmail |
| Telephone Number | PRIMARY\_PHONE |  |
| manager | MGR\_GUID | Stores the Sentinel GUID that represents the identity of this person's manager. The mapping is not direct. Sentinel uses the object referenced by the Identity Vault “manager” attribute to determine the manager's Sentinel Identity object and thereby obtains the actual GUID value that forms the reference in Sentinel. |
| photo | PHOTO |  |

In addition to the Identity information, Sentinel stores information about accounts associated with this Identity. The Identity Manager drivers that are provisioning accounts to connected systems store information about those accounts in a multi-valued attribute on the DirXML-Accounts source User object. The format of each value in DirXML-Accounts is as follows:

```
<driver guid>#<account id type>#<account id>#<idv account status>#<app account status>#<app Name>
```

The following table describes how these fields are mapped to the internal USR\_ACCOUNTS table in Sentinel:

*Table 8-2* Mapping in USR\_ACCOUNTS Table

| Identity Vault Value | Sentinel Column | Event Field and Comments |
| <account id> | USR\_NAME | This field and USR\_NAME are parsed out from the account information. |
| (calculated) | AUTHORITY | This field and USR\_NAME are parsed out from the account information.  This field and AUTHORITY are parsed out from the account information. |
| <idv account status> | BEGIN\_EFFECTIVE\_DATE | This value is set based on the settings of this field and the <app account status> field, plus Sentinel records a temporal record of when the account status was changed. |
| <app account status> | END\_EFFECTIVE\_DATECURRENT\_F | This value is set based on the settings of this field and the <idv account status> field, plus Sentinel records a temporal record of when the account status was changed. |

*NOTE:*If the default schema mapping does not meet your requirements, you can customize most of the schema mappings between the Identity Vault and Sentinel to suit your requirements. The framework is fully extensible to store arbitrary Identity attributes in Sentinel by using the Extended Attributes table (USR\_IDENTITY\_EXT\_ATTR).
