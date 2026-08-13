# 5.1 Configuring the Subscriber Channel

The Subscriber channel sends information from the Identity Vault to the Web service. To establish a secure connection for the Subscriber channel, you need a truststore containing a certificate issued by the certificate authority that signed the server’s certificate.

1. Make sure you have a server certificate signed by a certificate authority.
2. Import the certificate into your truststore or create a new trust store by entering the following command at the command prompt:

   keytool -import -file name\_of\_cert\_file -trustcacerts -noprompt -truststore filename -storepass password

   For example:

   keytool -import -file tree\_ca\_root.b64 -trustcacerts -noprompt -truststore dirxml.truststore -storepass novell
3. Configure the Subscriber channel to use the trust store you created in [step 2:](configure-subscriber-channel.html#b1i9vrdr)

   1. In Identity Console, click the IDM Administration tile.
   2. On the Driver Dashboard, click the driver’s icon.
   3. Select the Configuration tab, then expand the Driver Parameters section.
   4. On the Driver Settings tab, select No for Always accept server certificate.
   5. In the Truststore file path, specify the path to the trust store you created in [step 2](configure-subscriber-channel.html#b1i9vrdr).
4. Save.
