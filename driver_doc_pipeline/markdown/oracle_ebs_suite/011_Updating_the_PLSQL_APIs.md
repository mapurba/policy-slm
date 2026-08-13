# 2.4 Updating the PL/SQL APIs

To update the already installed PL/SQL APIs, perform the following steps:

1. Log in to the Oracle SQL developer tool or Oracle database as an apps user.
2. Run the install\_EBS.sql command.

   Copy the contents from the install\_EBS.sql file and paste them in the Oracle SQL developer editor, then run the copied script to create the database tables.
3. In the left panel of the Oracle SQL developer tool, navigate to Packages and search for the IDM\_DRIVER package.
4. Replace the header of the IDM\_DRIVER package with Publisher.pls and body with Publisher.pkb and save the package.
5. Navigate to Packages and search for the IDM\_DRIVER\_S package.
6. Replace the header of the IDM\_DRIVER\_S package with Subscriber.pls and body with Subscriber.pkb and save the package.
