# 4.8 Installing PostgreSQL 9

The directory context for PostgreSQL scripts is found in the install-dir\DirXMLUtilities\jdbc\sql\postgres\install directory on Windows or install-dir/lib/dirxml/rules/jdbc/sql/postgres/install directory on UNIX/Linux platforms. The directory context for executing PostgreSQL commands is postgres-install-dir/pgsql/bin.

1. Create the idm database.

   For example, from the UNIX command line, execute the following command:

   ./createdb idm
2. Install the plpgsql procedural language to the idm database.

   For example, from the UNIX command line, execute the following command:

   ./createlang plpgsql idm
3. From a PostgreSQL client such as psql, log in to the idm database as postgres user.

   For example, from the UNIX command line, execute the following command:

   ./psql -d idm postgres

   By default, the postgres user has no password.
4. From inside psql, execute the script 1\_install\_8.sql. For example:

   idm=# \i 1\_install\_8.sql
5. Update the pg\_hba.conf file.

   For example, add entries for the idm database user. Adjust the IP-ADDRESS and IP-MASK columns as necessary:

   ```
   # TYPE  DATABASE    USER   IP-ADDRESS        IP-MASK           METHOD# allow driver user idm to connect to database idm
   host    idm         idm    <ip-address>   <net-mask>     password
   ```
6. Restart the PostgreSQL server to effect the changes made to the pg\_hba.conf file.
