# 5.1 Configuring the Publisher Channel Using the KMO File

The Publisher channel sends information from the Web service to the Identity Vault. To establish a secure connection for the Publisher channel, you need a keystore or a KMO containing a certificate issued by the certificate authority that signed the server’s certificate.

Oracle Wallet Manager is an application used to manage and edit security credentials in Oracle wallets. A wallet is a password-protected container that stores authentication and signing credentials, including private keys, certificates, and trusted certificates, all of which are used by SSL for strong authentication. For more information, see [Managing Wallets and Certificates.](http://docs.oracle.com/cd/B15904_01/core.1012/b13995/wallets.htm)

1. Create a server certificate in Identity Console:

   1. Click Certificate Management > Server Certificate Management.
   2. Click + to create server certificate.
   3. Specify the server and a certificate nickname.
   4. Select Standard as the creation method, then click Next.
   5. Click OK.
2. Export a self-signed certificate from the certificate authority in eDirectory:

   1. Click Certificate Management > CA Management.
   2. On the Certificates tab, select the check box for the certificate you have created.
   3. Click Export CA Certificate.
   4. Depending on the client to be accessing the Web service, select either the export format, DER or Base64 for the certificate, then click OK.
   5. Click Save the exported file.
   6. Save the certificate in the Wallet Manager.
3. Start the Oracle Wallet Manager and create the certificate in the Oracle EBS system:

   * *UNIX:*
     At the command line, enter owm.
   * *Windows:*
     Select Start > Programs > Oracle-HOME\_NAME > Network Administration > Wallet Manager.
4. Import the certificate to the list of trusted certificates in the Oracle Wallet Manager:

   1. Click Operations > Import Trusted Certificate, the Import Trusted Certificate dialog appears. Select the certificate created in [Step 2](configuring-the-publisher-channel-using-the-kmo-file.html#bw1k1wf) and click OK.

      A message informs you that the trusted certificate was successfully imported into the wallet. The trusted certificate appears at the bottom of the Trusted Certificates tree in the Oracle Wallet Manager main panel.
   2. Save the wallet.
   3. Copy the Wallet Manager folder to a new location (for example, /opt/wallet).
   4. Execute the following SQL statements in the Oracle EBS system to configure the wallet:

      ```
      insert into idmusrmgt.idm_config values('WALLET_PATH','file:/etc/ORACLE/WALLETS/pub')
      ```

      ```
      insert into idmusrmgt.idm_config values('WALLET_PASSWORD','test123');
      ```
   5. Add the required permissions for the folder in [Step 4.c](configuring-the-publisher-channel-using-the-kmo-file.html#b120iggf), then click OK.
5. Configure the Publisher channel to use the server certificate created in [Step 1](configuring-the-publisher-channel-using-the-kmo-file.html#bw1k1td):

   1. In Identity Console, click the IDM Administration tile.
   2. On the Driver Dashboard, locate the Oracle EBS driver icon, then click the upper right corner of the driver icon to display the driver’s properties page.
   3. Click the Configuration tab, then expand the Driver Parameters section.
   4. Click the Publisher Settings tab.
   5. In the KMO name setting, specify the certificate nickname used in [Step 1](configuring-the-publisher-channel-using-the-kmo-file.html#bw1k1td).
6. Save the settings.
