# 6.0 Securing Driver Communication

The GroupWise driver uses REST APIs to communicate with Groupwise. Groupwise internally uses an SSL connection. SSL connections encrypt all traffic on the TCP/IP socket by using a public/private key pair.

You can configure the driver to always accept the GroupWise server's certificate for establishing a SSL connection with the Identity Manager server. To do so, change the Always accept server certificate setting to True during driver configuration. For more information, see [Step 11](create-driver-object-designer.html#brymlf8). If you leave the setting as is, you can use an alternative method and import the server certificate from GroupWise into a keystore on your Identity Manager server.

1. Import the server certificate from GroupWise and save it to a file in the der format.

   1. Open a web browser and connect to GroupWise with administrator rights at the first time.

      The browser prompts you to accept the server certificate.
   2. Go to the properties of the browser and download the certificate to your Identity Manager server in the der format.
   3. Save the file to a local file system.
2. Add the .der file to the keystore by using the following command at the command line:

   ```
   keytool -import -file PATH_OF_DERFile\PublicKeyCert.der -keystore KEYSTOERPATH\NAME.keystore -storepass keystorepass
   ```

   NetIQ recommends that you use Java 1.7 keytool. The command might not work with versions earlier than Java 1.7.
3. When you are asked to trust this certificate, select Yes.
4. Copy the .keystore file to any directory on the same file system where Identity Manager is running.
5. In Identity Console, Click IDM Administration.
6. Select the driverset where your driver is running and then click the GroupWise driver icon.
7. Navigate to Configuration > Driver Parameters.
8. In the Subscriber Settings, enter the complete path to the keystore file.
9. Specify the keystore password.
10. Click Save to save the configuration.
