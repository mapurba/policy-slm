# 3.1 Preventing Loopback on the Publisher Channel

The change-log mechanism implements loopback detection by ignoring events that are detected in the connected system made by the account that is used in the driver configuration. All changes made in the connected system by the account used in the driver configuration are not published in the Identity Vault on the Publisher channel. For example, if the driver is configured with user account as “jdoe”, use any other user account except “jdoe” to make changes on the connected system. To create an account with proper rights to be used in the driver configuration, see, see [Security Considerations](security-considerations.html).

*NOTE:*If the connected eDirectory is a Read/Write replica, the move events from the Subscriber channel is looped back to the Publisher channel. This is because move operation happens on the Master Replica.
