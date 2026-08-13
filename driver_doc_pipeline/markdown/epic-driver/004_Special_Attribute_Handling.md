# 1.3 Special Attribute Handling

Login Disabled: When mapping Login Disabled in the Identity Vault to IsActive in Epic the value must be reversed for the desired outcome. When Login Disabled is set to true in the Identity Vault the matching result in Epic for IsActive would be false. If the attribute us synced straight through without changing the value, the result will be the opposite of what is desired.

![](../graphics/img02.png)

CustomUserDictionaries: This attribute has been deprecated in Epic and is no longer available since Epic version 2014.
