# 5.3 Configuring the Subscriber Channel

The Subscriber channel sends information from the Identity Vault to the Web service. To establish a secure connection for the Subscriber channel, you need a trust store containing a certificate issued by the certificate authority that signed the server’s certificate.

Oracle Wallet Manager is an application used to manage and edit security credentials in Oracle wallets. A wallet is a password-protected container that stores authentication and signing credentials, including private keys, certificates, and trusted certificates, all of which are used by SSL for strong authentication. For more information, see [Managing Wallets and Certificates.](http://docs.oracle.com/cd/B15904_01/core.1012/b13995/wallets.htm)

1. If you are not using the default wallet.

   1. Change the SSLWallet property in the ssl.conf file to point the path of the wallet. For example, if SSL wallet file is present in the /etc/ORACLE/WALLETS/pub location, enter this path in the ssl.conf file (for example, /u01/app/VIS/inst/apps/VIS\_hostname/ora/10.1.3/conf/ssl.conf).
   2. Add the path of the wallet in the sqlnet.ora file:

      ```
      WALLET_LOCATION=
       (SOURCE=
            (METHOD=file)
            (METHOD_DATA=
               (DIRECTORY=/etc/ORACLE/WALLETS/pub)))
      ```

      The sqlnet.ora file is present in the <ORACLE\_HOME>/network/admin/<VIS\_hostname> location.
2. Specify the HTTPS port as Listen in the ssl.conf file. For example, Listen 4443.
3. Start the Oracle Wallet Manager and create the certificate in the Oracle EBS system:

   * *UNIX:*
     At the command line, enter owm.
   * *Windows:*
     Select Start > Programs > Oracle-HOME\_NAME > Network Administration > Wallet Manager.

   1. Add a certificate request to an Oracle wallet. Click Operations > Add Certificate Request.

      The Common Name must match with the hostname (don't include port). This is same as the Server Name entry in the httpd.conf file (for example, sles11sp164-ora.novell.com)
   2. Export the certificate request created in 3a. Click Operations > Export Certificate Request, then save the exported file with a .csr extension (for example, subreq.csr).
   3. (Conditional) Create a new Certificate Authority.

      ```
      openssl req -new -x509 -keyout cakey.pem -out cacert.crt -days 365
      ```

      Omit this step if you are using an existing Certificate Authority.
   4. Create the user certificate.

      ```
      openssl x509 -req -in subreq.csr -CA cacert.crt -CAkey cakey.pem -CAcreateserial -days 365 > server.crt
      ```
   5. Add the cacert.crt certificate to the wallet. Click Operations > Import Trusted Certificate.
   6. Add the server.crt certificate to the wallet. Click Operations > Import User Certificate.
   7. Save the wallet, then restart the Oracle EBS system.

      If you are not using default wallet location, copy the wallet files to the custom location.
4. Download the certificate created in [Step 3](configuring-the-subscriber-channel.html#b120j4nn) from the Oracle EBS system.

   * Export the certificate using the Oracle Wallet Manager.

     Or
   * Type the URL in a Web browser and download the certificate.

     For example, type https://sles11sp164-ora.novell.com:4443.
5. Copy the certificate to the Identity Vault machine.
6. Add the certificate to the trust store using the keytool.

   ```
   keytool -import -file subscriber.cer -trustcacerts -noprompt -keystore dirxml.keystore -storepass novell
   ```

   where subscriber.cer is the certificate downloaded in [Step 4](configuring-the-subscriber-channel.html#b120jpzk).
7. Configure the Subscriber channel to use the keystore name (dirxml.keystore) created in [Step 6](configuring-the-subscriber-channel.html#b120jpzl):

   1. In Identity Console, click the IDM Administration tile.
   2. On the Driver Dashboard, locate the Oracle EBS driver icon, then click the upper right corner of the driver icon to display the driver’s properties page.
   3. Click the Configuration tab, then expand the Driver Parameters section.
   4. Click the Subscriber Settings tab.
   5. In the Truststore File field, specify the path to the keystore created in [Step 6](configuring-the-subscriber-channel.html#b120jpzl).
8. Save the configuration.

*NOTE:*For setting up mutual authentication on the Subscriber channel, follow the instructions from [Configuring the Publisher Channel Using the Keystore File](configuring-the-publisher-channel-using-the-keystore-file.html) and add the certificate to the keystore file in the Subscriber channel mutual authentication settings.
