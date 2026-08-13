# 9.4 Planning for Identity Provisioning

When planning for Identity Provisioning, include the following considerations:

* If you don't plan to use Identity Provisioning, you don't need to run the Platform Receiver.
* You might need to permanently exclude some users and groups from Identity Provisioning. You might want to phase in your implementation by using a subset of your users and groups to start with. For details about excluding users and groups from Identity Provisioning, see [AM.USER.INCLUDE Statement / AM.USER.EXCLUDE Statement](beiffigc.html#chdiefij) and [AM.GROUP.INCLUDE Statement / AM.GROUP.EXCLUDE Statement](beiffigc.html#chddjjje).
* If the base Receiver scripts do not meet your needs, you can write your own extensions. Decide what additional processing you will perform and how you will test your extensions.
* All platforms in a Platform Set have the same population of users and groups associated with them for Identity Provisioning. Users and groups on Linux/UNIX platforms in Platform Sets that share a common UID/GID Set have the same UID or GID on each participating platform. Decide how you will organize your Platform Sets and UID/GID Sets.
* You must specify which Core Drivers are used for Identity Provisioning. For details, see [PROVISIONING Statement](beiffigc.html#bhf0ezv).
* You must choose the mode of operation used by the Platform Receiver to obtain events. For details, see [Modes of Operation](babdcabj.html#babfijbb) and [Selecting a Mode of Operation](babdcabj.html#babjheej).
