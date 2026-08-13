# 8.0 Schema Mapping

The policies and filters included in the driver packages provide bidirectional creation, deletion, and modification of user information in the Identity Vault and the Oracle EBS system. The driver is configured to synchronize information from the Identity Vault to the Oracle EBS system (Subscriber channel) and from the Oracle EBS system to the Identity Vault (Publisher channel). You can modify the policies and the filter to work with your specific business environment.

The Schema Mapping policy is referenced by the driver object and applies to both the Subscriber and the Publisher channel. The purpose of the Schema Mapping policy is to map schema names (particularly attribute names and class names) between the Identity Vault and the Oracle User database table (idmusrmgt.idm\_events). Any modification or removal of existing entries in the Schema Mapping policy could destroy the default configuration and policies processing behavior. Adding new attribute mappings is discretionary.

[Table 8-1](schema-mapping.html#b14xhdey), [Table 8-2](schema-mapping.html#b14xhdez), and [Table 8-3](schema-mapping.html#b14xhdff) contain default mappings between the Oracle EBS user attributes for User Management, HR, and TCA modules and the Identity Vault attributes.

*Table 8-1* Oracle User Management Attributes and the Identity Vault Attributes

| Identity Vault Attribute | Oracle User Management Attribute |
| User | inetOrgPerson |
| CN | USER\_NAME |
| Description | DESCRIPTION |
| Facsimile Telephone Number | FAX |
| Internet EMail Address | EMAIL\_ADDRESS |
| Surname | Mapped as default password if the password is not specified for the user. |
| Login Expiration Time | END\_DATE |
| loginActivationTime | START\_DATE |
| Password Expiration Interval | PASSWORD\_LIFESPAN\_DAYS  *IMPORTANT:*If the Password Expiration field is set to Accesses in the Oracle EBS system, the password expiration interval is turned off. The Identity Vault does not have a corresponding attribute for Accesses; therefore, the driver fails to synchronize the password expiration changes with the Identity Vault. However, the changes are successfully synchronized if the password expiration interval is set to number of days. |
| Login Disabled | LOGIN\_DISABLED |
| DirXML-ebsPersonId | EMPLOYEE\_ID |

*Table 8-2* Oracle HR Attributes and the Identity Vault Attributes

| Identity Vault Attribute | Oracle HR Attribute |
| User | inetOrgPerson |
| Internet EMail Address | P\_EMAIL\_ADDRESS |
| Surname | P\_LAST\_NAME |
| Given Name | P\_FIRST\_NAME |
| mailstop | P\_MAILSTOP |
| L | P\_INTERNAL\_LOCATION |
| Initials | P\_MIDDLE\_NAMES |
| DirXML-ebsGender | P\_SEX |

*Table 8-3* Oracle TCA Attributes and the Identity Vault Attributes

| Identity Vault Attribute | Oracle TCA Attribute |
| User | inetOrgPerson |
| CN | USER\_NAME |
| Description | DESCRIPTION |
| Facsimile Telephone Number | FAX |
| Login Expiration Time | END\_DATE |
| loginActivationTime | START\_DATE |
| Password Expiration Interval | PASSWORD\_LIFESPAN\_DAYS |
| Internet EMail Address | TCA\_EMAIL\_ADDRESS |
| Login Disabled | LOGIN\_DISABLED |
| Surname | TCA\_PERSON\_LAST\_NAME |
| Given Name | TCA\_PERSON\_FIRST\_NAME |
| EMail Address | EMAIL\_ADDRESS |
| Initials | TCA\_PERSON\_MIDDLE\_NAME |
