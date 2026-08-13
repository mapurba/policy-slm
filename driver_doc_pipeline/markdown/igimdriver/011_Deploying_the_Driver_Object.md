# 2.6 Deploying the Driver Object

After you create, configure, or modify the driver, you must deploy the IGIM driver to the Identity Vault.

1. In Designer, open your project.
2. In the Modeler view, right-click the driver icon ![IGIM-driver-icon](../graphics/driver_icon_n.png "IGIM-driver-icon") or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to [Step 5](deploying-the-netiq-idm-igim-driver.html#bfvehvl); otherwise, specify the following information:

   *Host:*
   Specify the IP address or DNS name of the server hosting the Identity Vault.

   *Username:*
   Specify the DN of the user object used to authenticate to the Identity Vault.

   *Password:*
   Specify the user’s password.
4. Click OK.
5. Read through the deployment summary, then click Deploy.
6. Read the success message, then click OK.
7. Click Define Security Equivalence to assign rights to the driver as specified.

   *NOTE:*You must use the credentials of the one (1) user object that is security equivalent of the driver object. The collector configuration must also use the same one (1) user.
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat [Step 8.a](deploying-the-netiq-idm-igim-driver.html#bfvehvr) and [Step 8.b](deploying-the-netiq-idm-igim-driver.html#bfvehvs) for each object you want to exclude.
   4. Click OK.
9. Click OK.
