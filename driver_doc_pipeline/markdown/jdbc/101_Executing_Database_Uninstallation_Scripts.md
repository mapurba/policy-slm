# A.3 Executing Database Uninstallation Scripts

This section provides helps you execute database uninstallation SQL scripts.

* [IBM DB2 Universal Database (UDB) Uninstallation](executing-database-uninstallation-scripts.html#bw182t9)
* [Informix Dynamic Server (IDS) Uninstallation](executing-database-uninstallation-scripts.html#bw18478)
* [Microsoft SQL Server Uninstallation](executing-database-uninstallation-scripts.html#bw182i2)
* [MySQL Uninstallation](executing-database-uninstallation-scripts.html#bw183zn)
* [Oracle Uninstallation](executing-database-uninstallation-scripts.html#bw182dn)
* [PostgreSQL Uninstallation](executing-database-uninstallation-scripts.html#bw184it)
* [Sybase Adaptive Server Enterprise (ASE) Uninstallation](executing-database-uninstallation-scripts.html#bw182yt)

## A.3.1 IBM DB2 Universal Database (UDB) Uninstallation

The directory context for DB2 is install-dir\DirXMLUtilities\jdbc\sql\db2\_udbl\install.

1. Drop the idm, indirect, and direct operating system user accounts.
2. If you haven’t already done so, change the name of the administrator account name and password in the installation scripts.
3. Using the Command Line Processor (CLP), execute the uninstall.sql script.

   For example: db2 -f uninstall.sql

   This script won’t execute in the Command Center interface beyond version 7 because the script uses the \ line continuation character. Later versions of the Command Center don’t recognize this character.
4. Delete the idm\_db2.jar file.

## A.3.2 Informix Dynamic Server (IDS) Uninstallation

The directory context for Informix SQL scripts is install-dir\DirXMLUtilities\jdbc\sql\informix\_ids\install.

1. Drop the idm operating system user account.
2. Start a client such as SQL Editor.
3. Log on to your server as user informix or another user with DBA (database administrator) privileges.

   By default, the password for informix is informix.

   If you execute scripts as a user other than informix, change all references to informix in the install scripts prior to execution.
4. If you aren’t using the informix account with the default password, change the name of the DBA account name and password in the installation scripts.
5. Open and execute uninstall.sql from the ansi (transactional, ANSI-compliant), log (transactional, non-ANSI-compliant), or no\_log (non-transactional, non-ANSI-compliant) subdirectory, depending upon which type of database you installed.

## A.3.3 Microsoft SQL Server Uninstallation

The directory context for Microsoft SQL Server scripts is install-dir\DirXMLUtilities\jdbc\sql\mssql\install.

1. Start a client such as Query Analyzer.
2. Log on to your database server as user sa.

   By default, the sa user has no password.
3. Open and execute the first installation script, uninstall.sql.

   The execute hotkey in Query Analyzer is F5.

## A.3.4 MySQL Uninstallation

The directory context for MySQL SQL scripts is install-dir\DirXMLUtilities\jdbc\sql\mysql\install.

1. From a MySQL client, such as mysql, log on as user root or another user with administrative privileges.

   For example, from the command line execute mysql -u root -p

   By default, the root user has no password.
2. Execute the uninstall.sql uninstallation script.

   For example: mysql> \. c:\uninstall.sql

   Don’t use a semicolon to terminate this statement.

## A.3.5 Oracle Uninstallation

The directory context for Oracle SQL scripts is install-dir\DirXMLUtilities\jdbc\sql\oracle\install.

1. From an Oracle client, such as SQL Plus, log on as user SYSTEM.

   By default, the password for SYSTEM is MANAGER.

   If you execute scripts as a user other than SYSTEM with password MANAGER, change all references to SYSTEM in the scripts prior to execution.
2. Execute the uninstallation script uninstall.sql.

   For example: SQL> @c:\uninstall.sql

## A.3.6 PostgreSQL Uninstallation

The directory context for PostgreSQL scripts is install-dir\DirXMLUtilities\jdbc\sql\postgres\install. The directory context for executing Postgres commands is postgres-install-dir/pgsql/bin.

1. From a Postgres client such as psql, log on as user postgres to the idm database.

   For example, from the UNIXC command line, execute ./psql -d idm postgres

   By default, the Postgres user has no password.
2. From inside psql, execute the script uninstall.sql.

   For example: idm=# \i uninstall.sql
3. Drop the database idm.

   For example, from the UNIX command line, execute ./dropdb idm
4. Remove or comment out entries for the idm user in the pg\_hba.conf file.

   For example:

   ```
   #host    idm         idm    255.255.255.255   255.255.255.0
   ```
5. Restart the Postgres server to effect changes made to the pg\_hba.conf file.

## A.3.7 Sybase Adaptive Server Enterprise (ASE) Uninstallation

The directory context for Sybase SQL scripts is install-dir\DirXMLUtilities\jdbc\sql\sybase\_ase\install.

1. From a Sybase client, such as isql, log on as user sa.
2. Execute the installation script uninstall.sql.

   For example, from the command line, execute isql -U sa -P -i uninstall.sql

   By default, the sa account has no password.
