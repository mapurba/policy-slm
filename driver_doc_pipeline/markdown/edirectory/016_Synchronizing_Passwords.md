# 6.0 Synchronizing Passwords

To use the eDirectory driver to set up password synchronization between the two Identity Vaults, follow the instructions in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

The following list contains information that is specific to setting up password synchronization with the eDirectory driver. Use it to supplement the information in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

* Universal Password is the standard method to synchronize passwords with Identity Manager. The eDirectory driver’s policies and filters (in the basic configuration file) are set up to support this method. However, you can use the older method of synchronizing passwords through the NDS password. This method is also known as synchronizing the public key and private key. If you choose to use the NDS password method, make sure you follow the instructions in "[Password Synchronization Scenarios](../../../identity-manager-48/password_management/data/password-synchronization-scenarios.html#password-synchronization-scenarios)" in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).
* If you decide to enforce password policies in multiple trees, make sure that the Advanced Password Rules in the password policies are compatible in each tree, so that password synchronization can be successful.

  If you enforce incompatible password policies in multiple eDirectory trees, and choose to reset a password back to the distribution password if it does not comply (with the option If password does not comply, enforce Password Policy on the connected system by resetting user’s password to the Distribution Password), you could encounter a loop in which each Identity Vault server tries to change a noncompliant password.

  Information about password policies is in “Managing Passwords by Using Password Policies” in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).
* The Password Status task in Identity Console does not work for a connected system if the Password policy has Universal Password enabled and does not have the setting selected for synchronizing Universal Password with NDS Password.

  The Password Status task lets you see whether a user’s password in Identity Manager is synchronized with the password on connected systems.

  If you are using the eDirectory driver and the password policy for a user specifies in the Configuration Options tab that the NDS Password should not be updated when the Universal Password is updated, then the Check Password Status task for that user always shows that the password is not synchronized. The password status is shown as not synchronized, even if the Identity Manager Distribution Password and the Universal Password on the connected system are in fact the same.

  This is because the Identity Vault check-password functionality is checking the NDS Password at this time, instead of going through NMAS to refer to the Universal Password.

  By default, the NDS Password is updated when the Universal Password is updated in the password policy. If you select this option, Check Password Status should be accurate for the connected system.
