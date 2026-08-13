# 3.1 Establishing a Security-Equivalent User

The driver must run with security equivalent to a user with sufficient rights. You can set the driver equivalent to ADMIN or a similar user. For a stronger security, you can define a user with only the minimal rights necessary for the operations you want the driver to perform.

The driver must be a trustee of the containers where synchronized identities reside, with the rights shown in Table 3-1. Inheritance must be set for [Entry Rights] and [All Attribute Rights].

*Table 3-1*

| Operation | [Entry Rights] | [All Attribute Rights] |
| Subscriber notification of account changes (recommended minimum) | Browse | Compare and Read |
| Retrieving passwords from the Identity Vault | Browse and Supervisor | Compare and Read |
