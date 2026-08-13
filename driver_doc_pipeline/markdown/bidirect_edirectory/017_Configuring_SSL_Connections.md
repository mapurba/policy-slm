# 6.0 Configuring SSL Connections

The Bidirectional eDirectory driver uses the LDAP protocol to communicate with the eDirectory servers. SSL connections encrypt all traffic on the TCP/IP socket by using a public/private key pair.

If your environment has Identity Manager engine version 4.6 connecting to a target server that has eDirectory 9.0.2 enabled with Suite B, the existing certificates in the Identity Vault do not work when SSL is configured to use the keystore method or when Always Accept Server Certificate option is enabled for the driver. Suite B specifies increased strength of encryption for the certificates used for SSL connections. To increase the encryption level of certificates, include Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy files in the JRE path of your Identity Manager installation and then create new Elliptic Curve (EC) certificates that are compatible with Suite B or use the Always Accept Server Certificate option for SSL communication. For example, download Java 8 JCE files from [Oracle’s download page](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html) and follow the instructions from the Readme.txt file included in the downloaded file.

The Bidirectional eDirectory driver supports mutual authentication to support secure data transfer and data integrity. You can establish mutual authentication on the Identity Manager side for the Bidirectional eDirectory driver to authenticate to the Identity Vault.

* [Importing the Certificate into the Client’s Certificate Store](importing-the-certificate-into-the-clients-certificate.html)
* [Configuring Mutual Authentication](configuring-mutual-authentication.html)
* [Security Considerations](security-considerations.html)
