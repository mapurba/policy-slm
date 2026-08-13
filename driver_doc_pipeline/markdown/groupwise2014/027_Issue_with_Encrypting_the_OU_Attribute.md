# 8.5 Issue with Encrypting the OU Attribute

The Organizational Unit (OU) attribute of a user in the Identity Vault is mapped to the CN attribute of GroupWise's Post Office class. When this attribute is encrypted in the Identity Vault, it also encrypts the value of the CN attribute in the driver trace.

There is no workaround at this time.
