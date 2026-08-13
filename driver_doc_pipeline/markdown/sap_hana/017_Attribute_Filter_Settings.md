# 3.4 Attribute Filter Settings

This section provides information about the Identity Vault Filter settings in the driver. The SAP HANA will be the authoritative source for all the above attributes except user ID and Email address which are generated in the Identity Manager.

* [User Attributes Filter Settings](t4b2ostg4jt0.html#t4b2ow226dn9)
* [User Group Filter Settings](t4b2ostg4jt0.html#t4b2owbqc9zo)
* [Role Filter Settings](t4b2ostg4jt0.html#t4b2p77xx51q)

## 3.4.1 User Attributes Filter Settings

The following table provides information about the Users Attributes Filter settings:

*Table 3-4* User Attributes Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| nspmDistributionPassword | default | ignore | notify |
| CN | default | sync | sync |
| Description | default | sync | sync |
| DirXML-Associations | default | ignore | notify |
| Group Membership | default | sync | sync |
| employeeType | default | sync | sync |
| Login Disabled | default | sync | sync |
| Internet EMail Address | default | sync | sync |
| DirXML-EntitlementRef | default | ignore | notify |

## 3.4.2 User Group Filter Settings

The following table provides information about the User Group Filter settings:

*Table 3-5* User Group Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| CN | default | sync | ignore |
| sapHanaComments | default | sync | ignore |
| DirXML-Associations | default | ignore | notify |

## 3.4.3 Role Filter Settings

The following table provides information about the Role settings:

*Table 3-6* Role Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| CN | default | sync | ignore |
| DirXML-Associations | default | ignore | notify |
| sapHanaComments | default | sync | ignore |
| sapHanaRoleMode | default | sync | ignore |
| sapHanaRoleSchemaName | default | sync | ignore |
| sapHanaRoleGroupName | default | sync | ignore |
