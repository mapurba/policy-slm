# 1.2 How the Driver Works

Sentinel receives information from various Identity Collectors and then stores the data in the database. If the same user has multiple identifiers for a single account in an application, Sentinel treats each identifier as a unique account.

The driver enables you to track all account identifiers for each user and to track the status of those accounts, so you have a complete picture of user activities. [Figure 1-1](how-the-driver-works.html#b10ewhxl) illustrates how the driver works to capture this information.

*Figure 1-1* Synchronizing Account Data

![](../graphics/sent_idm_integration_a.png)

1. The Active Directory driver creates an account for John Smith in Active Directory and synchronizes the information to the Identity Vault.
2. The Identity Vault, which contains the DirXML-Accounts attribute, creates an account for John Smith. The DirXML-Accounts attribute stores the different account identifiers from Active Directory.
3. The driver detects that the DirXML-Accounts attribute is added and sends this information to the Sentinel REST Interface.
4. The LDAP driver detects the new account created in the Identity Vault, then synchronizes this information to the LDAP database.
5. The LDAP driver creates a new account for John Smith in the LDAP database as follows:

   ```
   cn=jsmith,cn=users,dc=company,dc=com
   ```
6. The LDAP driver synchronizes the new account information back to the Identity Vault. The Identity Vault adds a new entry to the DirXML-Accounts attribute.
7. The Sentinel driver detects the change to the DirXML-Accounts attribute, then sends this information to the Sentinel REST Interface.
8. The Sentinel REST Interface stores the account data in the USR\_IDENTITY table in the Sentinel database.
9. The Sentinel correlation engine uses the information in the USR\_IDENTITY table to generate reports of account activity per identity across all the systems provisioned by Identity Manager.

The second half of this solution allows other Sentinel Collectors to use the account information to track whether your organization enforces business policies. [Figure 1-2](how-the-driver-works.html#b10f088d) shows how Sentinel uses the custom events and the events from other Collectors to provide a complete record of John Smith’s accounts.

*Figure 1-2* Synchronizing Events

![](../graphics/sent_idm_custom_a.png)

1. The Active Directory driver creates an account for John Smith in the Identity Vault.
2. The Sentinel driver detects this new account and sends the account information to the Sentinel REST Interface, which stores the information in the USR\_IDENTITY table.
3. John Smith logs in to Active Directory, and that information is sent to Sentinel through the Active Directory Collector.
4. The Active Directory Collector receives the login event directly from Windows without going through the Identity Vault. Sentinel records this information in the USR\_ACCOUNT table indicating that cn=John Smith,cn=users,dc=company,dc=com logged in at a specific time.
5. If John Smith’s CN in Active Directory is renamed to John D. Smith, the Active Directory driver synchronizes the information to the Identity Vault.
6. The DirXML-Accounts attribute is updated with the new information, and the Sentinel driver detects this change.
7. The Sentinel driver synchronizes the new account information to the Sentinel REST interface.
8. The Sentinel REST interface reads the new account information and writes it to the USR\_IDENTITY table.
9. When John Smith logs in again to Active Directory, the Active Directory Collector records the login information.
10. Sentinel performs a lookup on the USR\_IDENTITY table and detects that John Smith and John D. Smith are the same user account. Sentinel can keep a complete record of user actions.
11. The driver policies define and add custom audit events to each Identity Manager driver. The policies add a layer of intelligence to Identity Manager and Sentinel by defining the business logic. These policies are part of each driver that ships with Identity Manager.
12. You can generate useful reports about user accounts from Sentinel.

The Sentinel Identity Tracking driver provides the infrastructure to allow Sentinel to track each user account. This awareness allows you to enforce business policies.
