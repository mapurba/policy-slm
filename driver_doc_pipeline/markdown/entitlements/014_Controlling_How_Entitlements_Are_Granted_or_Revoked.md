# 7.0 Controlling How Entitlements Are Granted or Revoked

You can control the consequences of granting or revoking an entitlement. Each driver provides a list of supported choices that control the meaning of “grant” or “revoke.”

For example, when you add a GroupWise account, you can specify that grant actually means to grant the user an account in a disabled state, so that the administrator must intervene before the user can access the account. Or, you could choose to enable the account, which is the default.

By default, the driver configurations use the option that is most likely to preserve data. For example, the default meaning of “remove” for a GroupWise account is set to “disable,” to avoid unintentionally losing accounts if a mistake is made when the administrator is making changes to policies. As another example, the Identity Manager driver configurations don’t revoke entitlements that have values from a user account in another system. If a user is granted membership in an e-mail distribution list, then later the user no longer meets the criteria for the entitlement policy, he or she is simply dropped from the policy membership. Accounts are disabled, but group membership and attribute values are not removed. An Identity Manager expert can customize the driver configurations if you want a different result.

The interpretation of revoking an entitlement is especially important because role-based entitlements give you the ability to make sweeping changes in an organization’s entitlements in a production environment, without testing the results in a lab.

You can change the settings for how to grant or revoke entitlements by editing the Global Configuration Variables on a preconfigured driver. If you are creating your own custom configuration, you can add GCVs to interpret how to grant and revoke entitlements.
