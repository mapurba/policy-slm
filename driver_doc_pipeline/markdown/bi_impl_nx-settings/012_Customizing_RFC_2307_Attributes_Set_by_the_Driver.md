# 5.1 Customizing RFC 2307 Attributes Set by the Driver

The Linux and UNIX Settings driver sets the following RFC 2307 attributes:

* uidNumber
* gidNumber
* homeDirectory
* loginShell
* uid (represented as uniqueID in the Identity Vault)

You can add other attributes for the driver to set.

To add more attributes for the driver to set, use iManager to modify the creation policy.

* If you are using the driver style sheet to assign UID and GID numbers, modify the creation policy, NOVLNXSPOS-sub-cp-setRequiredPosixAttrbutes.
* If you are using the LUM Linux/UNIX Config object to assign UID and GID numbers, modify the creation policy, NOVLNXSLUM-sub-cp-setRequiredPosixAttributes.
