# 4.0 Securing Communication

SAP HANA provides secure communication using TLS/SSL. You can configure the driver to take advantage of this increased security.

The communication between the Identity vault and SAP HANA is established through the Subscriber and Publisher channels. To establish a secure communication between them, you need a trust store containing a certificate issued by the certificate authority that signed the server’s certificate.

It is recommended to import the chain of CA certificates from issuer's trusted URL. SAP HANA instance uses certificates from a trusted CA. For example, if SAP HANA is using the certificates from Digicert (trusted CA), you must verify the authenticity of the certificates from the Digicert’s website before downloading and importing them into the Java Keystore.

For testing purposes, you can download the certificates from the browser directly but this is not recommended. In case you want to view and download the certificates from browser, perform the following steps:

1. Enter the SAP HANA login URL in your browser (for example Chrome), and click Enter.

   *NOTE:*Different browsers have different procedures to view the certificates. Steps 1 to 6 considers Chrome browser as an example.
2. Click the lock icon near the browser, and select Certificate (Valid). The certificate is displayed.
3. Click Certification Path. The Certification Path displays the hierarchical structure of the structure of all the certificates.
4. Select the root certificate (the top most parent certificate), and click View Certificate. The root certificate is displayed.
5. To save the certificate to your system, click Details > Copy to File > Next > Next.
6. Enter a filename for the certificate and save it to a location as required.
7. Import the saved SAP HANA tenant root CA certificate into your trust store or create a new trust store by entering the following command at the command prompt:

   ```
   keytool -import -file name_of_cert_file -trustcacerts -noprompt -keystore filename -storepass password
   ```

   For example:

   ```
   keytool -import -file tree_ca_root.b64 -trustcacerts -noprompt -keystore dirxml.keystore -storepass novell
   ```
8. Configure the driver to use the trust store you created in Step 1:

   1. Log into the Identity Console. Click Identity Manager > Identity Manager Overview.
   2. Locate the driver set containing the SAP HANA driver, when click the driver’s icon to display the Identity Manager Driver Overview page.
   3. On the Identity Manager Driver Overview page, click the driver’s icon again, then scroll to Driver Options.
   4. In the Keystore File setting, specify the trust store password and the path to the trust store you created in Step 1.
9. Click Apply, then click OK.
