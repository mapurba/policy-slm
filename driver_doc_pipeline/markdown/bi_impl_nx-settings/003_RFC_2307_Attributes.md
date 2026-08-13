# 1.2 RFC 2307 Attributes

The Linux and UNIX Settings driver sets the following RFC 2307 attributes:

* uidNumber
* gidNumber
* homeDirectory
* loginShell
* uid (represented as uniqueID in the Identity Vault)

You can customize the driver to set additional attributes. For details, see [Customizing RFC 2307 Attributes Set by the Driver](b3gepk9.html).

The uidNumber and gidNumber attributes can be assigned using an Identity Manager Stylesheet object, or they can be assigned from a LUM Linux/UNIX Config object. The style sheet allows configuration of multiple ranges of UIDs and GIDs. The driver can skip over ranges of numbers that you do not want UIDs and GIDs allocated from. For details about configuring the UID and GID ranges in the style sheet, see [Customizing UID/GID Ranges](b3gdtex.html).
