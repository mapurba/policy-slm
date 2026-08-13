# 6.1 Importing the Certificate into the Client’s Certificate Store

You need to import the trusted root certificate into a certificate store (also called a keystore) that the driver can use.

1. Import the trusted root certificate from the connected eDirectory server and save it to a file in der format.

   1. Log in to Identity Console.
   2. Under eDirectory, go to Certificate Management > Server Certificate Management, then select a server certificate.

      * Select an Elliptic Curve (EC) certificate if your Identity Vault and connected system have eDirectory 9.0.2.x.
      * Select a non-EC certificate if your Identity Vault and connected system have eDirectory 8.8.8.x.
   3. Click Export.
   4. Select OU=Organizational CA certificate from drop down menu for the Certificate option.
   5. Select der as the Export format, then click OK.
   6. Save the file to a local file system.
2. Add the .der file to the keystore by using the following command at the command line:

   ```
   keytool -import -file PATH_OF_DERFile\PublicKeyCert.der -keystore KEYSTOERPATH\NAME.keystore -storepass keystorepass
   ```

   You are recommended to use Java 1.8 keytool or later.
3. When you are asked to trust this certificate, select Yes, then click Enter.
4. Copy the .keystore file to any directory on the same file system that has the Identity Vault files.
5. In Identity Console, select IDM Administrator.
6. Select the required driveset.
7. Click the Bidirectional eDirectory driver icon, then go to Configuration tab.
8. Change the Use SSL option as Yes, enter the complete path to the keystore file.
9. Enable the driver’s SSL parameter and adjust the other SSL parameters as needed.

   For information, see [Driver Parameters](driver-configuration.html#b957q17).

Continue with [Configuring Mutual Authentication](configuring-mutual-authentication.html).
