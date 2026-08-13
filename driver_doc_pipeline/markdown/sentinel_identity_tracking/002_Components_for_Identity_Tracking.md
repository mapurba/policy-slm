# 1.1 Components for Identity Tracking

This section provides information about the components required to integrate Sentinel with Identity Manager.

## 1.1.1 DirXML-Accounts Attribute

The DirXML-Accounts attribute on an Identity Vault User object tracks information about accounts that a user has in different applications. Identity Manager drivers that manage the account information for a user in an application, create and maintain the DirXML-Accounts attribute values. For example, the Active Directory driver maintains the DirXML-Accounts values for the account identifiers that a user has in Active Directory.

The Driver for Sentinel uses the DirXML-Accounts values to create and manage account records in Sentinel. If the application has multiple ways of identifying a single application account, there might be multiple account records in Sentinel for a single account. For example, Active Directory has five different identifiers for the same account. The Active Directory driver provides information about four of these identifiers in the DirXML-Accounts attribute. The driver synthesizes the fifth value from one of the identifiers provided by the Active Directory driver.

[Table 1-1](components-for-identity-tracking.html#bzvlpgy) shows that the DirXML-Accounts attribute stores the different identifiers for John’s account. Active Directory has four different account identifiers for the same account and the LDAP directory has one.

*Table 1-1* Contents of the DirXML-Accounts Attribute

| Driver/Application | Account Identifier Type | Account Identifier Sample Data |
| Active Directory | sAMAccountName | jsmith |
| Active Directory | userPrincipalName | jsmith@company.com |
| Active Directory | LDAPDN | cn=John Smith,cn=users,dc=company,dc=com |
| Active Directory | association | 5d377f84f3ab534babbf12edd6540d77 |
| LDAP | LDAPDN | cn=jsmith,cn=users,dc=company,dc=com |

This allows for correlation between all of the account identities in the systems managed by Identity Manager. You can also validate business policies with this information.

## 1.1.2 Driver for Sentinel

The driver is an Identity Manager driver that sends the account identifier and the account status from the Identity Vault to the Sentinel REST API interface. The account identifier data is used to track the accounts, the status of the identities, and the account access information.

The driver implements data sharing policies with Sentinel. You can control the actions by using Identity Console to define filters and policies.

## 1.1.3 Sentinel REST API Interface

The Sentinel REST API interface integrates the data from the driver to Sentinel. The interface performs functions, such as remote protocol connections and data mapping.
