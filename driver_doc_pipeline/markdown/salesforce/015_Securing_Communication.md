# 6.0 Securing Communication

If the remote Web service you are accessing allows HTTPS connections, you can configure the driver to take advantage of this increased security.

*IMPORTANT:* Only certificates from Java keystore are accepted. So, make sure that the keystore of the certificates is a Java keystore.

The Subscriber channel sends information from the Identity Vault to Salesforce.com. To establish a secure connection for the Subscriber channel, you need a trust store containing a certificate issued by the certificate authority that signed the server’s certificate.

Import this certificate into a trust store using Java’s keytool. For more information on keytool, see [Keytool - Key and Certificate Management Tool](http://java.sun.com/j2se/1.4.2/docs/tooldocs/windows/keytool.html).

1. Import the certificate into your trust store or create a new trust store by entering the following command at the command prompt:

   ```
   keytool -import -file name_of_cert_file -trustcacerts -noprompt -keystore filename -storepass password
   ```

   For example:

   ```
   keytool -import -file tree_ca_root.b64 -trustcacerts -noprompt -keystore dirxml.keystore -storepass novell
   ```
2. Configure the Subscriber channel to use the trust store you created in [Step 1](secure-communication.html#bw1k6n2):

   1. In Identity Console, click the IDM Administration tile.
   2. On the Driver Dashboard, click the driver’s icon.
   3. Click Configuration > Driver Settings.
   4. In the Truststore file field, specify the path to the trust store you created in [Step 1](secure-communication.html#bw1k6n2).
3. Save.
