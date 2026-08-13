# 9.6 Planning for Account Redirection Platforms

When planning for Account Redirection Platforms, include the following considerations:

* Use the Account Redirection option if you wish to redirect all account information, including loginName, uidNumber, gidNumber, gecos, homeDirectory, loginShell, memberUid fields and passwords.
* If you plan to use Account Redirection, you do not need to run the Platform Receiver or the Platform Services Process. Instead, you need to configure your system for the Name Service Switch and configure the Platform Services Cache Daemon for system startup.
* If you plan to use Account Redirection, you must populate your user and group accounts with the posixAccount and posixGroup auxiliary classes. This can be done manually on a per-object basis or through a bulk LDIF import process. Alternatively, you may run the Linux and UNIX User Settings Driver to automatically populate this information when users and groups are created or modified. For details on this driver, see the Identity Manager Driver documentation for the Linux and UNIX user settings.
