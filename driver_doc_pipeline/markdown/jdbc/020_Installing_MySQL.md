# 4.5 Installing MySQL

The directory context for MySQL SQL scripts is found in the \products\IDM\windows\setup\drivers\jdbc\tools\sql\ directory on Windows. On Linux platforms, the files are deployed at /opt/novell/eDirectory/lib/dirxml/rules/jdbc/sql when novell-DXMLjdbc-4.1.0-0.noarch.rpm is installed.

1. From a MySQL client, such as mysql, log in as root user or another user with administrative privileges.

   For example, from the command line, execute

   mysql -u root -p

   By default, the root user has no password.
2. Execute the installation script 1\_install\_innodb.sql or 1\_install\_myisam.sql, depending upon which table type you wish to use. For version 5.5.15 use the scripts in subdirectory 5.

   For example: mysql> \. c:\1\_install\_innodb.sql

   Don’t use a semicolon to terminate this statement.
