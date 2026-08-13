# 6.4 SSL Configuration for PeopleSoft Application

1. Create a Certificate and import to KeyStore file in PeopleSoft System.
2. Add “SSL\_KEY\_STORE\_PATH” in the Identity Manager (IDM) or Development system to set the "SSL\_KEY\_STORE\_PATH" as an environment variable for respective Operating Systems (OS) as follows.

   * Linux OS

     SSL\_KEY\_STORE\_PATH=<path>\keystore

     For Ex: SSL\_KEY\_STORE\_PATH= /root/drivers/psoft/keystore
   * Windows OS

     SSL\_KEY\_STORE\_PATH=<path>\keystore

     For Ex: SSL\_KEY\_STORE\_PATH= E:\PeopleSoft\PeopleSoft\_8\_59\Certificates\keystore
3. Copy the created TrustStore/KeyStore file to the Identity Manager Machine.
4. Follow the steps to add Java Virtual Machine (JVM) Options in Identity Console.

   1. Click the IDM Administration tile.
   2. On the Driver Dashboard, click the upper right corner of the driver set to display the Action menu.
   3. Select Driver Set Properties.
   4. Expand the Java Environment Parameters section to move to JVM Options.

   Enter TrustStore/Keystore file path and password -

   * File Path -Djavax.net.ssl.TrustStore=PeopleSoft created TrustStore/Keystore

     Ex: -Djavax.net.ssl.TrustStore=/home/certificates/keystore
   * Password: -Djavax.net.ssl.TrustStorePassword

     Ex: -Djavax.net.ssl.TrustStorePassword=password
5. Restart eDirectory.

*NOTE:*If the Certificate expires, generate a new KeyStore executing the above steps.
