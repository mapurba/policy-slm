# 4.10 Installing Sybase Adaptive Server Enterprise (ASE)

The directory context for Sybase SQL scripts is found in the install-dir\DirXMLUtilities\jdbc\sql\sybase\_ase\install directory on Windows or install-dir/lib/dirxml/rules/jdbc/sql/sybase\_ase/install directory on UNIX/Linux platforms.

1. From a Sybase client, such as isql, log in as the sa user and execute the 1\_install.sql installation script.

   For example, from the command line, execute:

   isql -U sa -P -i 1\_install.sql

   By default, the sa account has no password.
