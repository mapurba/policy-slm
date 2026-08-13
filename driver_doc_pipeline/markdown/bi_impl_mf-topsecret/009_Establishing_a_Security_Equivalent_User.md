# 2.5 Establishing a Security-Equivalent User

The Driver object must run with Security Equivalence to a user with sufficient rights. You can set the driver equivalent to Admin or a similar user. For stronger security, you can define a user with only the minimal rights necessary for the operations you want the driver to perform.

The driver user must be a trustee of the containers where synchronized users and groups reside, with the rights shown in [Table 2-2](b484ok2.html#b4exk92). Inheritance must be set for [Entry Rights] and [All Attribute Rights].

*Table 2-2* Base Container Rights Required by the Driver Security-Equivalent User

| Operation | [Entry Rights] | [All Attribute Rights] |
| Subscriber notification of account changes (recommended minimum) | Browse | Compare and Read |
| Creating objects in the Identity Vault without group synchronization | Browse and Create | Compare and Read |
| Creating objects in the Identity Vault with group synchronization | Browse and Create | Compare, Read, and Write |
| Modifying objects in the Identity Vault | Browse | Compare, Read, and Write |
| Renaming objects in the Identity Vault | Browse and Rename | Compare and Read |
| Deleting objects from the Identity Vault | Browse and Erase | Compare, Read, and Write |
| Retrieving passwords from the Identity Vault | Browse and Supervisor | Compare and Read |
| Updating passwords in the Identity Vault | Browse and Supervisor | Compare, Read, and Write |

If you do not set Supervisor for [Entry Rights], the driver cannot set passwords. If you do not want to set passwords, set the Subscribe setting for the User class nspmDistributionPassword attribute to Ignore in the filter to avoid superfluous error messages. For details about accessing and editing the filter, see the policy documentation on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

For complete information about rights, see the NetIQ eDirectory™ Administration Guide.
