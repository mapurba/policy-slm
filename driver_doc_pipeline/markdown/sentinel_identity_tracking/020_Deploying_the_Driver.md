# 6.3 Deploying the Driver

After you create the driver in Designer, you must deploy the driver into the Identity Vault, because Designer is an offline tool.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](deploying-the-driver.html#b1025c17); otherwise, specify the followinginformation to authenticate:

   * *Host:*
     Specify the IP address or DNS name of the server hosting the Identity Vault.
   * *Username:*
     Specify the DN of the user object used to authenticate to the Identity Vault.
   * *Password:*
     Specify the user’s password.
4. Click OK.
5. Read through the deployment summary, then click Deploy.
6. Click OK.
7. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault that are involved in synchronization. The Admin user object is most often used to supply these rights. However, you might want to create an object, for example, DriversUser and assign security equivalence to that user. The DriversUser object must have the same security rights on the server as the driver. The driver needs read rights for the following attributes: Full Name, mail, Given Name, Surname, OU, Title, photo, mailstop, Telephone Number, workforceID, manager, GUID, DirXML-Accounts, and Login Disabled.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK.
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects, such as Admin and DriversUser from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat [Step 8.a](deploying-the-driver.html#b1025lje) and [Step 8.b](deploying-the-driver.html#b1025lm7) for each object you want to exclude.
   4. Click OK.
9. Click OK.
