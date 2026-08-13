# 6.2 Configuring the Subscriber Channel

The Subscriber channel sends information from the Identity Vault to the Web service. To establish a secure connection for the Subscriber channel, you need a trust store containing a certificate issued by the certificate authority that signed the server’s certificate. See [Configuring the Publisher Channel](configure-publisher-channel.html) for an example.

1. Make sure you have a server certificate signed by a certificate authority.
2. Import the certificate into your trust store or create a new trust store by entering the following command at the command prompt:

   ```
   keytool -import -file name_of_cert_file -trustcacerts -noprompt -keystore filename -storepass password
   ```

   For example:

   ```
   keytool -import -file tree_ca_root.b64 -trustcacerts -noprompt -keystore dirxml.keystore -storepass novell
   ```

   For more information on keytool, see [Keytool - Key and Certificate Management Tool](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/keytool.html).
3. Configure the Subscriber channel to use the trust store you created in [Step 2](configure-subscriber-channel.html#bw1k6n2):

   1. In Identity Console, in the Identity Manager frame, click IDM Administration.
   2. Locate the driver set containing the SOAP driver, then click the driver’s icon to display the configuration page.
   3. Go to Configuration > Driver Parameters, then go to Subscriber Settings.
   4. In the Keystore File, specify the path to the trust store you created in [Step 2](configure-subscriber-channel.html#bw1k6n2).
4. Click Apply, then click OK.

*NOTE:*To use TLSv1 instead of SSLv3 in the HTTP client, change the JVM setting for the driver by using one of the following methods:

In Designer, right-click the driver set containing this driver. Click Properties >Java and set the JVM option as Dhttps.protocols=TLSv1 in the window that opens up. Click Apply and then click OK.

In Identity Console, click ![](../graphics/action_menu.png), go to Driver Set properties page, click Driver set configuration > Java Environment Parameters tab and set the JVM option as Dhttps.protocols=TLSv1.

If the driver is using the Remote Loader, set the -javaparam option to DHOST\_JVM\_OPTIONS=-Dhttps.protocols=TLSv1 in the configuration file.

A driver with this setting will always initiate a connection only through the TLSv1 protocol and will not connect to servers using SSlv3 protocol.
