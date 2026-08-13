# 2.3 Installing the PL/SQL APIs

The PL/SQL scripts handle the parsing of events in the Oracle EBS database. The PL/SQL scripts configure database objects such as tables and procedures for data synchronization with the driver. If you don’t configure the database objects, the data communication might not work properly.

Installing the PL/SQL scripts includes performing the following tasks:

* Installing the install\_EBS.sql PL/SQL scripts in the Oracle EBS system.
* Creating packages for the Publisher and Subscriber channels.

Locate the install\_EBS.sql PL/SQL scripts from /mnt/products/IDM/scripts/OracleEBS installation directory and install them in the Oracle EBS system.

1. Log in to the Oracle SQL developer tool or Oracle database as a system user (Oracle EBS user name).
2. Run the install\_EBS.sql command.

   Copy the contents from the install\_EBS.sql file and paste them in the Oracle SQL developer editor, then run the copied script to create the database tables.
3. Log out of the Oracle SQL developer tool or the Oracle database.

To create packages for the Publisher channel, do the following:

1. Log in to the Oracle SQL developer tool or Oracle database as an apps user.
2. In the left panel of the Oracle SQL developer tool, navigate to Packages and create a new package and name it IDM\_DRIVER.
3. Add the publisher.pls script to the IDM\_DRIVER package and save the package.
4. Right-click the IDM\_DRIVER package, select create body and paste the contents of the publisher.pkb file from the Identity Manager installation directory.
5. Save the package.

Repeat this procedure for creating the IDM\_DRIVER\_S package for the Subscriber channel and add subsciber.pls and subsciber.pkb files from the Identity Manager installation directory to the package and save it.
