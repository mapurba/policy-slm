# 4.3 Installing Informix Dynamic Server (IDS)

For Informix Dynamic Server, you must manually create an operating system user account before running the provided SQL scripts.

Because the process of creating user accounts differs between operating systems, Step 1 below is OS-specific. These instructions are for a Windows operating environment. If you rerun the SQL scripts, you should repeat only Steps 2 through 4.

The directory context for Informix SQL scripts is found in the install-dir\DirXMLUtilities\jdbc\sql\informix\_ids\install on Windows or install-dir/lib/dirxml/rules/jdbc/sql/informix\_ids/install directory on UNIX/Linux platforms.

1. In Windows, create a user account for user idm.

   Use novell as the password in User Manager for Domains.

   Remember to deselect User Must Change Password at Next Login for this account.

   You might want to also select Password Never Expires.

   *NOTE:*The remaining instructions are OS-independent.
2. Start a client such as SQL Editor or DBAccess.
3. Log in to your server as the informix user or another user with DBA (database administrator) privileges.

   By default, the password for the informix user is informix. If you execute scripts as a user other than informix, change all references to informix in the scripts prior to execution.
4. Open and execute 1\_install\_9.sql from either the ansi (transactional, ANSI-compliant), log (transactional, non-ANSI-compliant), or no\_log (non-transactional, non-ANSI-compliant) subdirectory, depending upon which type of database you want to create.
5. For version 11 or later, open and execute 2\_install\_10.sql from either the ansi (transactional, ANSI-compliant), log (transactional, non-ANSI-compliant), or no\_log (non-transactional, non-ANSI-compliant) subdirectory, depending upon which type of database you want to create.
