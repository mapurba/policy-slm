# 7.0 Security Best Practices

This section contains a description of the security parameters unique to the SAP Portal driver.

For additional information about securing your Identity Manager system, see the [NetIQ Identity Manager Security Guide](../../../identity-manager-48/security/data/identity-manager-security-guide.html#identity-manager-security-guide).

To increase security, use the following procedure to configure the SAP Portal driver to communicate over HTTPS, then create a secure connection for it to use.

To create a secure connection:

1. Create a server certificate in Identity Console:

   1. Click Certificate Management > Server Certificate Management.
   2. Click + to create server certificate.
   3. Specify the server and a certificate nickname.
   4. Select Standard as the creation method, then click Next.
   5. Click OK.
2. Export this self-signed certificate from the certificate authority in eDirectory.

   1. Click Certificate Management > CA Management.
   2. On the Certificates tab, select the check box for the certificate you have created.
   3. Click Export CA Certificate.
   4. Depending on the client to be accessing the Web service, select either the export format, DER or Base64 for the certificate, then click OK.
   5. Click Save the exported file.
   6. Save the downloaded certificate to a known location in your computer.
3. Import the self-signed certificate into the client’s trust store:

   1. Use the keytool executable that is included with any Java JDK.

      For more information on keytool, see [Keytool - Key and Certificate Management Tool](http://java.sun.com/j2se/1.4.2/docs/tooldocs/windows/keytool.html).
   2. Import the certificate into your trust store or create a new trust store by entering the following command at a command prompt:

      ```
      keytool -import -file name_of_cert_file -trustcacerts -noprompt
      -keystore filename -storepass password
      ```

      For example:

      ```
      keytool -import -file tree_ca_root.b64 -trustcacerts -noprompt -keystore dirxml.keystore -storepass novell
      ```
4. Configure the Subscriber channel to use the trust store you created in [Step 3](understanding-security-best-practices-for-identity-manager-sap-portal-driver.html#bw1k21x):

   1. In Identity Console, click the IDM Administration tile.
   2. On the Driver Dashboard, click the driver’s icon.
   3. Select Configuration > Subscriber Settings.
   4. Specify the path to the trust store you created in [Step 3](understanding-security-best-practices-for-identity-manager-sap-portal-driver.html#bw1k21x) in the Truststore file field.
5. Save.
