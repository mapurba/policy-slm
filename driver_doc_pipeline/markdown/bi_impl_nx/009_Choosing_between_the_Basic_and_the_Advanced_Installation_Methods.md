# 2.5 Choosing between the Basic and the Advanced Installation Methods

When you import the driver, you are prompted to choose either the Basic Installation or the Advanced Installation. Select Advanced Installation for any of the following:

* You plan to maintain RFC 2307 attribute information, such as uidNumber, gidNumber, homeDirectory, loginShell, and gecos, centrally from the Identity Vault. You can do this with a manual process or by an automated process, such as by using the Linux and UNIX Settings driver. You do not want to publish changes to this information from the Linux or UNIX system.
* You plan to maintain RFC 2307 attribute information locally on the connected Linux or UNIX system. You do not want to subscribe to changes to this information from the Identity Vault.
* You only want to publish information.
* You only want to subscribe to information.
* You want to use Role-Based Entitlements.
* You want to override the defaults and configure specific Linux and UNIX driver options, such as the automatic creation of home directories, the automatic deletion of home directories, or the setting of gecos values.

To view the driver import configuration settings offered by each installation method, see [Creating the Driver in Designer](b1bybgrg.html).
