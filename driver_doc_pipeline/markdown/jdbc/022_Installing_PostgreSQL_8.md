# 4.7 Installing PostgreSQL 8

The directory context for PostgreSQL scripts is found in the install-dir\DirXMLUtilities\jdbc\sql\postgres\install directory on Windows or install-dir/lib/dirxml/rules/jdbc/sql/postgres/install directory on UNIX/Linux platforms. The directory context for executing PostgreSQL commands is postgres-install-dir/pgsql/bin.

1. Create the idm database.

   For example, from the UNIX command line, execute the following command:

   ./createdb idm
2. From a PostgreSQL client such as psql, log in to the idm database as postgres user.

   For example, from the UNIX command line, execute the following command:

   ./psql -d idm postgres

   By default, the postgres user has no password.
3. From inside psql, execute the script 1\_install\_8.sql. For example:

   idm=# \i 1\_install\_8.sql
4. Update the pg\_hba.conf file.

   In PostgreSQL 8, you can update the file through pgAdminIII. After you start, go to Tools > Connect to connect to the server, select the idm database, then go to Tools > Server Configuration > pg\_hba.conf. In the pgAdminIII pg\_hba.conf editor, the IP-ADDRESS and IP-MASK columns in the file are combined into a single field named as IP-Address. Place the values of IP-ADDRESS and IP-MASK columns in this field separated by a single whitespace character.

   For example, add entries for the idm database user. Adjust the IP-ADDRESS and IP-MASK as necessary:

   ```
   # TYPE DATABASE    USER   IP-ADDRESS        IP-MASK           METHOD# allow driver user idm to connect to database idm
   host    idm     idm    <ip-address>   <net-mask>     password
   ```
5. Restart the PostgreSQL server to effect changes made to the pg\_hba.conf file.
6. (Conditional) If you are using pgAdminIII, in the pg\_hba.conf editor select the disk icon (save file) in the toolbar. When prompted, press Yes.
