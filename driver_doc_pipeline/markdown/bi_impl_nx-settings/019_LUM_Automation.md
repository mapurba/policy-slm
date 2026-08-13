# B.1 LUM Automation

The Linux and UNIX Settings driver can automate enabling OES users for NetIQ® Linux User Management (LUM). The driver performs the following steps:

1. Assigns uidNumber from the NxSettings style sheet or the Linux/UNIX Config object.
2. Adds Public rights to the following RFC 2307 attributes:

   | Attribute | Rights |
   | uidNumber | Read |
   | gidNumber | Read |
   | loginShell | Read |
   | homeDirectory | Read |
   | gecos | Read |
   | Group Membership | Read |
   | cn | Compare |
3. Adds the user to a group enabled for LUM. (The group is chosen during driver import.)
4. Sets the user’s gidNumber equal to the gidNumber of the LUM-enabled group.
5. Adds the object class uamPosixUser to the user.

If you have a very large number of users, you might not want all users to be in a single static group. You can define a dynamic group as your LUM-enabled group.

To use a dynamic group as your LUM-enabled group:

1. Define the dynamic group according to your needs.
2. Set the global configuration value (GCV) named Add Users to LUM-Enabled Group to No.

   (The GCV named LUM-Enabled Group DN is not used in this case.)

   GCV values can be edited on the Driver Properties page. For more information about editing GCVs, see [Section 4.0, Configuring the Linux and UNIX Settings Driver](b3gg5h4.html)

For details about LUM, see the Linux User Management Technology Guide, which is available from the [NetIQ® OES documentation Web site](http://www.novell.com/documentation/oes/index.html).
