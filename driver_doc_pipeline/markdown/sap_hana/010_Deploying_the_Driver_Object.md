# 2.6 Deploying the Driver Object

After the driver object is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to Step 5; otherwise, specify the following information:

   * *Host:*
     Specify the IP address or DNS name of the server hosting the Identity Vault.
   * *Username:*
     Specify the DN of the user object used to authenticate to the Identity Vault.
   * *Password:*
     Specify the user’s password.
4. Click OK.
5. Read through the deployment summary, then click Deploy.
6. Read the successful message, then click OK.
7. Click Define Security Equivalence to assign rights to the driver and all required jobs.

   The driver and all required jobs require the rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.

      For more information about defining a Security Equivalent User in objects for drivers in the Identity Vault, see [Establishing a Security Equivalent User](https://www.netiq.com/documentation/idm45/pdfdoc/idm_security/idm_security.pdf) in the [NetIQ Identity Manager Security Guide](https://www.netiq.com/documentation/idm45/pdfdoc/idm_security/idm_security.pdf).
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat Step 8a and Step 8b for each object you want to exclude.
   4. Click OK.
9. Click OK.
