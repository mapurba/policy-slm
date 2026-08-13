# 6.1 Configuring the Publisher Channel

1. Create a server certificate in Identity Console:

   1. Under eDirectory, click Certificate Management > Server Certificate Management.
   2. Click Create Server Certificate icon ![](../graphics/create_certificate.png).
   3. Browse to and select the server object where the SOAP driver is installed.
   4. Specify a certificate nickname.
   5. Select Standard as the creation method, then click Next.
   6. Click OK.
2. Export a self-signed certificate from the certificate authority in eDirectory:

   1. Under eDirectory, click Certificate Management > Server Certificate Management.
   2. Select your tree’s certificate authority object.

      It is usually found in the Security container and is named something like TREENAME CA.Security.
   3. Click ![](../graphics/export_certificate.png) Export Server Certificate icon.
   4. Uncheck the Export private key option.
   5. Based on the client to be accessing the Web service, select either File in binary DER format or File in Base64 format for the certificate, then click OK.

      If the client uses a Java-based keystore or trust store, then you can choose either format.
   6. Click Save the exported certificate to a file.
   7. Then click Close.
3. Import the self-signed certificate into the client’s trust store:

   The steps to import the certificate vary depending on the client that connects to the Publisher channel’s HTTPS listener. If the client uses a typical Java keystore, you can perform the following steps to create the keystore:

   1. Use the keytool executable that is included with any Java JDK.

      For more information on keytool, see [Keytool - Key and Certificate Management Tool](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/keytool.html).
   2. Enter the following command at a command prompt:

      ```
      keytool -import -file name_of_cert_file -trustcacerts -noprompt
      -keystore filename -storepass password
      ```

      For example:

      ```
      keytool -import -file tree_ca_root.b64 -trustcacerts -noprompt -keystore dirxml.keystore -storepass novell
      ```
4. Configure the Publisher channel to use the server certificate you created in [Step 1](configure-publisher-channel.html#bw1k1td):

   1. In Identity Console, in the Identity Manager frame, click IDM Administration.
   2. Locate the driver set containing the SOAP driver, then click the driver’s icon to display the configuration page.
   3. Go to Configuration > Driver Parameters, then go to Publisher Settings.
   4. In the KMO name, specify the certificate nickname you used in [Step 1](configure-publisher-channel.html#bw1k1td).
5. Click Apply, then click OK.
