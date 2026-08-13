# 7.0 Synchronizing Passwords

The following list contains information that is specific to setting up password synchronization with the Bidirectional eDirectory driver. Use it to supplement the information in the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

The Distribution Password is the default method used to synchronize passwords to and from the Identity Vault with the Bidirectional eDirectory Driver. The Bidirectional eDirectory driver’s default configuration policies and filters are set up to support the password synchronization using the Distribution Password. A Universal Password policy must be assigned to the user in the Identity Vault and connected tree. Ensure the Synchronize Distribution Password when setting Universal Password option is checked, for password synchronization to occur using the Distribution Password.

To synchronize the NDS password between the Identity Vault and the connected eDirectory by using the Bidirectional eDirectory driver, in the [Driver Configuration](driver-configuration.html) section, set the Password Sync Type to NDS password.

Password transfer over a clear-text connection is disabled by default. Password transfer is allowed over a secure connection only. The default behavior for transferring passwords can be changed by setting the Allow password on clear-text connection driver configuration parameter to True. However, this is not a recommended configuration.

To synchronize eDirectory Read-only filtered replica in the connected tree through the Publisher Channel, ensure that the following attributes are enabled on the eDirectory Read-Only filter replica for the user object:

* CN
* Surname
* nspmDistributionPassword
* nspmPasswordKey

*NOTE:*eDirectory Filtered Read-only replica is not the same as Driver Filter on a BiDirectional eDirectory Driver.
