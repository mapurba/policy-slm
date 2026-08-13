# 15.1 DirXML-Accounts Attribute Shows Incorrect Value When a User is Enabled or Disabled in the Identity Vault on DB2 and Oracle Database Drivers

This issue is observed with certain settings on the driver:

*DB2 driver:*
When the Allow Loopback option is set to Yes on the Publisher channel in the Indirect Triggered mode.

Workaround: Disable the Allow Loopback option.

*Oracle Driver:*
In the Direct Triggerless mode.

There is no workaround.
