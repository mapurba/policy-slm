# 4.6 Installing Oracle

The directory context for Oracle SQL scripts is found in the install-dir\DirXMLUtilities\jdbc\sql\oracle\install directory on Windows or install-dir/lib/dirxml/rules/jdbc/sql/oracle/install directory on UNIX/ Linux platforms.

1. From an Oracle client, such as SQL Plus, log in as the SYSTEM user.

   By default, the password for SYSTEM is MANAGER. If you execute scripts as a user other than SYSTEM with password MANAGER, change all references to SYSTEM in the scripts prior to execution.
2. Execute the installation script 1\_install.sql.

   For example: SQL> @c:\1\_install.sql
