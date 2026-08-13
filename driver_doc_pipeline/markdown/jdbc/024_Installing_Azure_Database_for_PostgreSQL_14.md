# 4.9 Installing Azure Database for PostgreSQL 14

The directory context for PostgreSQL scripts is found in the install-dir\DirXMLUtilities\jdbc\sql\postgres\install directory on Windows or install-dir/lib/dirxml/rules/jdbc/sql/postgres/install directory on UNIX/Linux platforms. The directory context for executing PostgreSQL commands is postgres-install-dir/pgsql/bin.

1. Login to Azure Portal.

   1. Goto Network Settings of PostgreSQL server.
   2. Download the SSL certificates.
   3. Goto Firewall Settings, click Add and provide the IP address as - 0.0.0.0.
   4. Open PGADMIN and add Server
   5. Navigate to General Tab.
   6. Navigate to Connections Tab, provide hostname as shown in the format below:

      <pgsqlsrvr>.postgres.database.azure.com

      For example: pgsqlsrvr.postgres.database.azure.com
   7. Specify the Port number. By default the port number is 5432 and specify the Maintenance Database value as Postgres.
   8. Click on SSL tab. In Root Certificate field, provide the path for the certificate that has been downloaded in [Step 1.c](t4kh349ocpha.html#step1c) from Azure Portal as shown in the below image.

      *Figure 4-1*

      ![](../graphics/postgre_sql.gif)
2. Running the install script.

   1. Connect to Postgres database using PGADMIN tool.
   2. Right click on the Postgres database and click on Query tool.
   3. In the Query tool run the commands in the install scripts for creating a user and granting permissions / privileges to the user created.
   4. Logout of PGADMIN and login as the user created in [Step 2.c](t4kh349ocpha.html#step2c). Right Click on the Posgres database and click on Query tool. User-name should be the Database Administrator which gets created as part of deployment of Azure Database for PostgreSQL flexible server.
   5. From the install script copy all the contents from CREATE A DATABASE till the end of the script. Paste the copied content in the Query Tool and run the query.
