# 4.2 Installing IBM DB2 Universal Database (UDB)

*IMPORTANT:*For IBM DB2, you must manually create operating system user accounts before running the provided SQL scripts.

Because the process to create user accounts differs between operating systems, [Step 1](install-ibm-db2-universal-database-udb.html#bvqf2tx) below is OS-specific. These instructions are for a Windows NT operating environment. If you rerun the SQL scripts, repeat only [Step 2](install-ibm-db2-universal-database-udb.html#af0mmu6) through [Step 4](install-ibm-db2-universal-database-udb.html#aesxowg).

The directory context for DB2 is found in the install-dir\DirXMLUtilities\jdbc\sql\db2\_udb\install directory on Windows or install-dir/lib/dirxml/rules/jdbc/sql/db2\_udb/install directory on UNIX/Linux platforms.

1. Create user accounts for users idm, indirect and direct.

   Use novell as the password in User Manager for Domains.

   Remember to deselect User Must Change Password at Next Login for this account.

   You might want to also select Password Never Expires.

   *NOTE:*The remaining instructions are OS-independent.
2. Adjust the file path to idm\_db2.jar in the 1\_install.sql installation script. The file path to idm\_db2.jar should reflect the location of this file on your client machine.
3. Execute the 1\_install.sql script from the Command Line Processor (CLP.)

   For example: db2 -f 1\_install.sql

   *IMPORTANT:*The scripts won’t execute in the Command Center interface beyond version 7. The scripts use \ as the line continuation character. Later versions of the Command Center don’t recognize this character.
4. For versions 9 or later, execute the 2\_install\_9.sql script.

   For example: db2 -f 2\_install\_9.sql
