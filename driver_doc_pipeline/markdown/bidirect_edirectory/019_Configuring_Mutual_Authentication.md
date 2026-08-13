# 6.2 Configuring Mutual Authentication

Use the following procedure to configure mutual authentication between the Bidirectional eDirectory driver and the Identity Vault:

1. Complete [Step 1](importing-the-certificate-into-the-clients-certificate.html#bwtbvxp) through [Step 9](importing-the-certificate-into-the-clients-certificate.html#bwtbvxx) in [Importing the Certificate into the Client’s Certificate Store](importing-the-certificate-into-the-clients-certificate.html).
2. Create a user certificate that the driver can use:

   1. In Identity Console, log in to the connected eDirectory server with administrator rights.
   2. Go to Certificate Management > User Certificate > Management.
   3. Click ![](../graphics/create_certificate.png) to create new user certificate.
   4. In the right pane of the User Certificate tab, specify the Nickname, then select Standard, and then click Next.
   5. Click OK.
3. Import the user cert.pfx file:

   1. In Identity Console, log in to the connected eDirectory server as the driver’s authenticated user.
   2. Go to Certificate Management > User Certificate > Management, select the user certificate created in [Step 2](configuring-mutual-authentication.html#bx56m0m).

      You are recommended to use Java 1.8 keytool or later.
   3. Click ![](../graphics/export_certificate.png) to export the certificate.
   4. Select Export Private key checkbox, specify the private key password for the certificate, then click OK.
   5. Save the cert.pfx file to a local file system.
4. Copy the cert.pfx file to any directory on the same file system that has the Identity Vault files.
5. Add the private key to the keystore by using the following command at the command line:

   ```
   keytool -importkeystore -srckeystore cert.pfx -srcstoretype PKCS12 -destkeystore mykeystore -alias AliasName
   ```

   The AliasName must be the same as Nickname that you specified for the user certificate. Ensure that you use the same keystore file that you used for the SSL configuration in [Step 2](importing-the-certificate-into-the-clients-certificate.html#bwtbvxq).
6. Adjust the driver’s configuration as needed.
7. Change the LDAP options of the connected eDirectory server to enable mutual authentication with the Identity Vault:

   1. In Identity Console, log in to the connected eDirectory server with administrator rights.
   2. Go to LDAP Configuration, then select the LDAP server that connected eDirectory server from the list of servers with which you want to enable mutual authentication.
   3. In the Modify LDAP Server pane, select the Information drop down.
   4. Change the Client Certificate option to Requested, leave other settings as the defaults.

      To communicate only with mutual authentication, set this option to Required.
   5. Click Save.
8. Start the driver.
