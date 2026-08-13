# 5.2 Configuring the Publisher Channel Using the Keystore File

1. Create a keystore and its alias:

   ```
   keytool -genkey -alias publisher10 -dname "cn=172.18.4.15:6060" -keypass novell -keystore publisherstore10.keystore -keyalg RSA
   ```

   where publisher10 is the alias and publisherstore10.keystore is the name of the keystore. CN is the IP address of the Publisher listener (port). RSA algorithm is required for creating certificates in the Oracle wallets.
2. Self-sign the certificate:

   ```
   keytool -selfcert -alias publisher10 -dname "cn=172.18.4.15:6060" -keypass novell -keystore publisherstore10.keystore
   ```
3. Export the certificate to a file called publisher10.cert:

   ```
   keytool -export -alias publisher10 -file publisher10.cert -keystore publisherstore10.keystore -storepass novell
   ```
4. Import the certificate in the Wallet Manager.
5. Start Oracle Wallet Manager.

   * *UNIX:*
     At the command line, enter owm.
   * *Windows:*
     Select Start > Programs > Oracle-HOME\_NAME > Network Administration > Wallet Manager.
6. Add the certificate (publisher10.cert) to the list of trusted certificates in the Oracle Wallet Manager:

   1. Click Operations > Import Trusted Certificate, the Import Trusted Certificate dialog appears. Select the certificate created in [Step 3](configuring-the-publisher-channel-using-the-keystore-file.html#b120in06) and click OK.

      A message informs you that the trusted certificate was successfully imported into the wallet. The trusted certificate appears at the bottom of the Trusted Certificates tree in the Oracle Wallet Manager main panel.
   2. Save the wallet.
   3. The trusted certificate appears at the bottom of the Trusted Certificates tree in the Oracle Wallet Manager main panel.
   4. Copy the Wallet Manager folder to a new location (for example, /opt/wallet).
   5. Execute the following SQL statements in the Oracle EBS system to configure the wallet:

      ```
      insert into idmusrmgt.idm_config values('WALLET_PATH','fi le:/etc/ORACLE/WALLETS/pub')
      ```

      ```
      insert into idmusrmgt.idm_config values('WALLET_PASSWORD','test123');
      ```
   6. Add the required permissions for the folder in [Step 6.d](configuring-the-publisher-channel-using-the-keystore-file.html#b120iner).

   *NOTE:*The certificate generated using Java 7 is not compatible with the Oracle Wallet Manager. To generate a new certificate, use Java 6 in the /opt/novell/eDirectory/lib64/nds-modules/embox/jre/bin/java directory.
7. Configure the Publisher channel to use the server certificate created in [Step 1](configuring-the-publisher-channel-using-the-kmo-file.html#bw1k1td):

   1. In Identity Console, click the IDM Administration tile.
   2. On the Driver Dashboard, locate the Oracle EBS driver icon, then click the upper right corner of the driver icon to display the driver’s properties page.
   3. Click the Configuration tab, then expand the Driver Parameters section.
   4. Click the Subscriber Settings tab.
   5. In the Keystore File field, specify the certificate nickname you used in [Step 1](configuring-the-publisher-channel-using-the-kmo-file.html#bw1k1td).
   6. Save the settings.

*NOTE:*For setting up mutual authentication on a Publisher channel (by using either the KMO or the keystore file), set the Require mutual authentication flag status to Required.
