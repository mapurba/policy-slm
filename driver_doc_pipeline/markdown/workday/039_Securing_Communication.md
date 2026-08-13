# 7.0 Securing Communication

If the remote Web service you are accessing allows HTTPS connections, you can configure the driver to take advantage of this increased security.

*IMPORTANT:*Only certificates from Java keystore are accepted. So, make sure that the keystore of the certificates is a Java keystore and the Workday tenant SSL certificate is available in the Java keystore.

The communication between the Identity vault and Workday is established through the Subscriber and Publisher channels. To establish a secure communication between them, you need a trust store containing a certificate issued by the certificate authority that signed the server’s certificate.

It is recommended to import the chain of CA certificates from issuer's trusted URL. Workday instance uses certificates from a trusted CA. For example, if Workday is using the certificates from Digicert (trusted CA), you must verify the authenticity of the certificates from the Digicert’s website before downloading and importing them into the Java Keystore.

For testing purposes, you can download the certificates from the browser directly but this is not recommended. In case you want to view and download the certificates from browser, perform the following steps:

1. Enter the Workday login URL in your browser (for example Chrome), and click Enter.

   *NOTE:*Different browsers have different procedures to view the certificates. Steps 1 to 6 considers Chrome browser as an example.
2. Click the lock icon near the browser, and select Certificate (Valid). The certificate is displayed.
3. Click Certification Path. The Certification Path displays the hierarchical structure of the structure of all the certificates.
4. Select the root certificate (the top most parent certificate), and click View Certificate. The root certificate is displayed.
5. To save the certificate to your system, click Details > Copy to File > Next > Next.
6. Enter a filename for the certificate and save it to a location as required.
7. Import the saved Workday tenant root CA certificate into your trust store or create a new trust store by entering the following command at the command prompt:

   ```
   keytool -import -file name_of_cert_file -trustcacerts -noprompt -keystore filename -storepass password
   ```

   For example:

   ```
   keytool -import -file tree_ca_root.b64 -trustcacerts -noprompt -keystore dirxml.keystore -storepass novell
   ```
8. Configure the driver to use the trust store you created in Step 1:

   1. In Identity Console, click the IDM Administration tile.
   2. On the Driver Dashboard, click the driver’s icon.
   3. Select the Configuration tab, then expand the Driver Parameters section.
   4. On the Driver Settings tab, in SSL Parameters > Workday Keystore file setting, specify the path to the trust store you created in Step 1.
9. Save.
