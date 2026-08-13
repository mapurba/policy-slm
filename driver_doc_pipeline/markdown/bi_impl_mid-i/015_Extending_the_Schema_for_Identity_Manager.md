# 3.5 Extending the Schema for Identity Manager

Attributes of IBM i profiles that correspond to attributes of eDirectory User and Group objects are mapped by the default driver mapping policy. You must extend the schema if you want to use the Identity Vault to manage additional IBM i attributes.

For details about the attributes in the default mapping policy, see [Table 1-2, Default eDirectory User to i5/OS UserProfile Mapping](b3wx9up.html#b4r8562) and [Table 1-3, Default eDirectory Group to IBM i GroupProfile Mapping](b3wx9up.html#b4r8dxo).

Extending the schema adds auxiliary classes to eDirectory User and Group objects for the profile and distribution directory attributes.

1. In iManager, select the Extend Schema task under Schema.
2. Select Import data from file on disk, then click Next.
3. Select a file type of Schema File.
4. Type or browse for i5os.sch as the file to import, then click Next.
5. Specify the host name or IP address and the LDAP port number of your Metadirectory server.

   To connect to the non-secure LDAP port (389), you must have the Require TLS for Simple Binds with Password option disabled on your LDAP Group. If necessary, you can edit this option using the LDAP Options task under LDAP in iManager. For details, see the NetIQ eDirectory Administration Guide.
6. Select Authenticated login and log in as ADMIN or another user with rights to extend the schema.
7. Click Next to go to the summary.
8. Click Finish to extend the schema.
