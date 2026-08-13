# 5.1 Configuring Secure Data Transfers

All eDirectory driver communication is secured through SSL. You can configure your eDirectory drivers through Designer.

For information about configuring eDirectory drivers through Designer, see Designer for Identity Manager Administration Guide

* [Understanding Secure Connections via the eDirectory Driver](configuring-secure-data-transfers.html#understanding-secure-connections-via-the-driver-edirectory-driver)
* [Creating Certificates Using Designer](configuring-secure-data-transfers.html#creating-certificates-using-designer)
* [Establishing Secure Connections Using KMO](configuring-secure-data-transfers.html#establishing-secure-connections-using-kmo)
* [Establishing Secure Connections Using Keystore](configuring-secure-data-transfers.html#establishing-secure-connections-using-keystore)

## 5.1.1 Understanding Secure Connections via the eDirectory Driver

The following items can help you understand how secure connections are established when using the eDirectory driver:

* The driver uses SSL sockets to provide authentication and a secure connection. SSL uses digital certificates to allow the parties to an SSL connection to authenticate one another. Identity Manager in turn uses NetIQ Certificate Server certificates for secure management of sensitive data.
* To use the driver, you must have the NetIQ Certificate Server running in each tree. We recommend that you use the certificate authority from one of the trees containing the driver to issue the certificates used for SSL. If your tree does not have a certificate authority, you need to create one. You can use an external certificate authority. For information about NetIQ Certificate Server, see the [NetIQ Certificate Server 3.3 Documentation Web site](http://www.NetIQ.com/documentation/crt33/).
* The NetIQ implementation of SSL that the driver uses is based on NetIQ Secure Authentication Services (SAS) and NTLS for eDirectory. These must be installed and configured on the server where the driver runs. eDirectory usually does this automatically.
* To configure driver security, it is necessary to create and reference certificates in the eDirectory trees that will be connected using the driver. The two SSL types for securing the connection are Key Material Objects (KMOs) and Keystore.
* Certificate objects in eDirectory are called KMO because they securely contain both the certificate data including the public key and the private key associated with the certificate.

  A minimum of two KMOs (one KMO per tree) must be created for use with the eDirectory drivers. This section explains using a single KMO per tree.

  The NDS-to-NDS Driver Certificate Wizard sets up the KMOs.

## 5.1.2 Creating Certificates Using Designer

To provide security while transmitting information between two Identity Vaults, you must configure the eDirectory driver to communicate with the destination eDirectory driver through an SSL connection.

In addition, you can provide additional security by requiring the two eDirectory drivers to authenticate to one another. Although this is optional, it is strongly recommended.

The following section explains how to set up SSL and configure driver authentication using designer.

#### Establishing Secure Connection and Creating Certificates Using Designer

Perform the following actions to configure two eDirectory drivers and communicate with each other over a secure channel.

1. Open your project in Designer.
2. Select two Identity Vaults from the palette between which you wish to secure a connection.
3. The Driver Configuration Wizard appears. The purpose of the Driver Configuration Wizard is to help you install drivers. For more information on creating a driver, see [Section 3.0, Creating a New Driver Object](creating-a-new-driver-object.html).

   To create a driver with packages, select the available base package listed. If there are no packages listed, then the packages are not imported into the package catalog. For more information about importing and installing packages, see [Installing or Upgrading Packages.](https://www.netiq.com/documentation/identity-manager-46/designer_admin/data/packman.html)
4. Configure the drivers. For more information on configuring the driver, see [Configuring the Driver](creating-the-driver-object-in-designer.html#configuring-the-driver).

   To create a driver with a driver configuration file, click Import Driver Configuration. All of the driver configurations files for the version of your Identity Manager server are listed. For more information about importing a driver configuration file, see [Importing a Driver Configuration File.](https://www.netiq.com/documentation/identity-manager-46/designer_admin/data/importfromfile.html)
5. Deploy the driver.
6. Configure the driver settings to communicate the two eDirectory drivers. For more information, see [Configure TLS for eDir-to-eDir drivers](https://www.netiq.com/documentation/identity-manager-46/designer_admin/data/importfromfile.html).

   To configure the driver settings, navigate to Preferences > NetIQ > Identity Manager > > Configuration > eDir-to-eDir SSL/TLS tab settings.

   *Table 5-1* Preferences: NetIQ > Identity Manager > Configuration > eDir-to-eDir SSL/TLS Tab Settings

   | Setting | Description |
   | Preferred key size | Specifies the preferred key size that is generated when drivers are encrypted and stored in eDirectory: 256, 384, 512, 768, 1024, or 2048 bytes. |
   | Preferred secure hash algorithm | Specifies the preferred hash algorithm to use when encrypting drivers: SHA1-RSA, MD2-RSA, MD5-RSA, SHA256-ECDSA, or SHA384-ECDSA.  * For 256 key size, Designer provides SHA256-ECDSA algorithm. * For 384 key size, Designer provides SHA384-ECDSA algorithm.  SHA256-ECDSA and SHA384-ECDSA are Suite B-compliant algorithms. |
   | Preferred validity period | Specifies the validity period for a driver certificate, ranging from 6 months to 10 years. |
   | Always overwrite existing certificates | Specifies that existing driver certificates are overwritten with each deployment. If you select this option, Designer deletes existing certificates and creates new ones. The new certificates are then good for another two years (assuming the default value is two years, as defined in the Preferred Validity Period field.) If you select Live > Create eDir-to-eDir Certificates, Designer deletes old certificates and creates new ones. |
   | Overwrite certificates only if they have expired | Specifies that only expired driver certificates are overwritten with each deployment. This is the default setting. The default expiration length is two years. If a certificate expires, SSL/TLS stops working. If a certificate is expired, Designer deletes it and creates a new one. |
   | Never overwrite existing certificates | Never overwrites driver certificates. |
   | Restart drivers after building certificates | Restarts drivers after certificates have been updated or created. |
7. Enable TLS.

   Perform the following actions to enable TLS:

   1. Right-click eDir-to-eDir in the Outline view, then click Secure Connection Settings.
   2. Right-click an eDir-to-eDir driver, click Properties > Driver Configuration > Authentication, then click Configure TLS. The Configure TLS icon displays only on eDir-to-eDir driver pages.
   3. Click Enable SSL/TLS.

      ![](../graphics/apptlscfg_a.png)
   4. Select a direction of trust.

      These options apply to certificates that NetIQ creates for eDirectory. The options do not apply to third-party security certificates.

      The default is Mutual Trust, which is considered to be the most secure.

      Unless you want to use the certificate for authentication, the option that you select doesn’t matter. If only encryption is important, you can select any one of the three options.

      If authentication is important, select the option that gives you the appropriate trust.

      *Scenario: JJ Infrastructure Tree Trusts JT ID Vault.*
      JJ Infrastructure Tree is the organizational certificate authority. JJ Infrastructure Tree signed a certificate and placed it in JT IDVault. JT ID Vault trusts JJ Infrastructure Tree. The two vaults synchronize data through a secure connection.

      If the two vaults break their trusted relationship, JJ Infrastructure Tree can prevent sensitive data from being synchronized by revoking its certificate.

      *Scenario: JT ID Vault Trusts JJ Infrastructure Tree.*
      JJ Infrastructure Tree creates two certificates. One is placed in JJ Infrastructure Tree, and the other is placed in JT ID Vault. The two vaults synchronize data through a secure connection.

      If the two vaults break their trusted relationship, JJ Infrastructure Tree can prevent sensitive data from being synchronized by revoking its certificate.

      *Scenario: Mutual Trust.*
      JT ID Vault and JJ Infrastructure Tree both sign certificates.
   5. (Optional) Use the Advanced TLS Configuration to select key size, hash algorithm, and validity period.

      The validity period is important for when a certificate has expired and you need to overwrite or create a new one.
8. Click OK.

   You can enable or configure TLS without immediately deploying the drivers. You can turn the settings on. However, you can’t create SSL/TLS certificates unless the drivers have been deployed into their respective Identity Vaults. If you enable SSL/TLS but want to create certificates later, you can do so. When you later deploy the eDir-to-eDir drivers, Designer guides you through steps to automatically create certificates.
9. Perform the following actions to create certificate.

   The first time you enable and configure SSL/TLS on driver’s Authentication tab, click OK, then follow the prompts. A Create Certificates dialog box appears. Click Yes.

   You can also create certificate by right-clicking the eDir2eDir application.

   Click Live > Create eDir-to-eDir Certificates.

   For more information, see [Configuration](https://www.netiq.com/documentation/identity-manager-46/designer_admin/data/appprefsnovell.html#appprefsconfig) in Designer Administrator guide.

*NOTE:*If the settings are not configured, the certificate is created using the default settings.

To view the details of the certificate in Identity Console, navigate to Certificate Management. Click the name of the certificate to view the summary of the certificate. Click ![](../graphics/validate_certificate.png) Validate on top of the screen to view if the certificate is valid or if it has expired.

## 5.1.3 Establishing Secure Connections Using KMO

To configure your Identity Vault system to handle secure Identity Manager data transfers:

#### Creating the Certificate Manually

Perform the following actions to manually create the certificate and establish a secure communication between the two eDirectory drivers.

The following example explains how to manually create the certificate.

Prerequisites

* Two Linux servers

  *NOTE:*1 server is a SLES 12.2 which is the main IDV (vault) tree and the other is a Red Hat 7.2 server.
* Both servers have eDirectory installed
* Both servers have Identity Manager 4.6 installed
* Both servers have eDirectory driver installed

Perform the following actions to create the certificate using KMO method:

1. Create a normal server certificate by navigating to Certificate Management > Server certificate Management, click ![](../graphics/create_certificate.png) to create server certificate.
2. Browse for the Server. Provide a Nickname. Choose the Creation method as Custom as we would manually make some changes. Click Next.
3. Select Organizational certificate authority (default) and click Next.
4. Select SSL or TLS as Key type. Select Server under Extended key type.
5. Select SHA 256-RSA(SHA2) as the Signature algorithm as it is considered more secure. Change the validity period as Maximum (as per your choice). Click Next.
6. Select Your organization’s certificate (default). Click Next.
7. The summary of the certificate information is listed. Click OK.
8. The KMO object is successfully created and listed under Tree view > system > servers.

Log into the Red Hat server and repeat the above procedure to create the certificate. However, the following changes needs to be made:

1. In [Step 3](configuring-secure-data-transfers.html#step3_kmocertificate), select External certificate authority.
2. After [Step 7](configuring-secure-data-transfers.html#step7_kmocertificate), click Save Certificate Signing Request and save it in a preferred location.

   *NOTE:*This is a .csr file.

   Exit the Red Hat server and log into the main server (SLES).
3. Navigate to Certificate Management > Issue certificate. Browse for the saved .csr file and click Next.
4. The Key Type and Extended Key Type remains same as mentioned in [Step 4](configuring-secure-data-transfers.html#step4_kmocertificate), click Next. The Certificate Type and Path length remains with default settings. Click Next.Validity period is set to Maximum. Click Next.
5. Save the File in Base 64 format and click Next.
6. Click Finish.
7. Save the file to a preferred location. This file is saved in a .b64 format.
8. Navigate to Certificate Management > CA Management. In the Certificate tab, check the Self Signed Certificate CA certificate and click ![](../graphics/export_certificate.png) to export.
9. Uncheck the Export private key checkbox. Select the format as Base64 and click OK.

   Save the exported certificate to a preferred location. The saved file is in .b64 format.

   Exit from the main vault.

Login to the Red Hat server and perform the following actions to synchronize data:

1. Navigate to View Objects and browse for the KMO object. Click the KMO object. Click the Certificate tab >Trusted Root certificate tab and click Import.
2. Browse and select the self signed certificate. Click OK.
3. Click New on the top left hand corner and browse for the issued certificate. Click OK.

   ![](../graphics/kmo_step3.png)
4. Two certificates to import are listed. Click Next, Finish and Ok.

   For KMO method, configure and start the eDirectory driver.
5. Exit from the Red Hat server and login to the main vault server.

   Configure and start the driver on the vault. Both the connections are secure.
6. Navigate to View objects and make a change (edit) to an object.

   For example: changing the description of a user.

Exit from the main server and login to the Red Hat server. The changes made to the user can be noticed here. The data is successfully synchronized.

## 5.1.4 Establishing Secure Connections Using Keystore

To establish a secure connection between two eDirectory servers using eDirectory driver, you need to import the trusted root certificate into keystore of connected eDirectory server and vice versa.

1. Create a server certificate in Identity Console.

   1. In the eDirectory frame, click Certificate Management > Server Certificate Management.
   2. Click ![](../graphics/create_certificate.png), browse to and select the server object where the eDirectory driver is installed.
   3. Specify a certificate nickname. For example maincert.

      *NOTE:*NetIQ recommends that you avoid using spaces in the certificate nickname. For example, use maincert instead of main cert.

      Also, make a note of the certificate nickname. This nickname is used for the KMO name in the driver properties.
   4. Select Custom in the certificate creation method, then click Next.
   5. Keep the default Organizational Certificate Authority selection, then click Next.
   6. Uncheck Enable extended key usage check box.
   7. Accept the default settings and review the summary, click OK.
2. Export the certificate.

   1. In the eDirectory frame, click Certificate Management > Server Certificate Management.
   2. Select the KMO object that you created in [Step 1](configuring-secure-data-transfers.html#b1fhbv9u) and click Validate. For example, maincert.
   3. Select the validated KMO object and click Export.
   4. Select the KMO object from the Certificates list.
   5. Ensure the Export private key check box is checked.
   6. Provide a password and click Next.

      Use this as a source password while generating a keystore.
   7. Save the certificate to a file in .pfx format, click Close.
3. Generate a keystore from the exported certificate using the following command at the command line:

   ```
   keytool -importkeystore -srckeystore <file saved in step 2> -srcstoretype PKCS12 -destkeystore <name of the keystore> -alias <kmo name provided in Step 1>
   ```

   For example:

   ```
   keytool -importkeystore -srckeystore maincert.pfx -srcstoretype PKCS12 -destkeystore new.keystore -alias maincert
   ```

   After executing this command, specify the destination password, then provide the source password which you want to use as a Keystore password while configuring the driver.
4. Import the trusted root certificate from the connected eDirectory server and save it to a file in der format.

   1. In Identity Console, log in to the connected eDirectory server with administrator rights.
   2. In the eDirectory view, click Certificate Management > Server Certificate Management.
   3. Select any server KMO object and click Validate. For example, SSL CertificateDNS.
   4. Select the validated KMO object and click Export.
   5. Select OU=Organizational CA certificate from drop down menu for the Certificate option.
   6. Select DER > as the Export format, then click Next.
   7. Save the file to a local file system in der format. For example PublicKeyCert.der.
5. Add the DER file to the keystore created in [Step 3](configuring-secure-data-transfers.html#b1fhbydq) by using the following command at the command line:

   ```
   keytool -import -file <Certificate name> -keystore KEYSTOERPATH\new.keystore -storepass <keystorepass>
   ```

   For example,

   ```
   keytool -import -file PATH_OF_DERFile\PublicKeyCert.der -keystore KEYSTOERPATH\new.keystore -storepass keystorepass
   ```

   In this command, storepass value is same as the destination password that you have provided in [Step 3](configuring-secure-data-transfers.html#b1fhbydq).

   NetIQ recommends that you use Java 1.6 or higher version keytool. This command might not work with versions earlier than Java 1.6.
6. When you are asked to trust this certificate, type YES, then press Enter.
7. Copy the new.keystore file to any directory on the same file system that has the Identity Vault files.
8. In Identity Console, select IDM Administrator.
9. Select the required driverset.
10. Click the eDirectory driver icon, then go to Configuration tab.
11. Click the Driver Parameters drop down.
12. Change the Use SSL option as Yes, enter the complete path to the keystore file.
13. Enable the driver’s SSL parameters and configure the other SSL parameters as needed.

    For information, see [Driver Parameters](driver-configuration.html#driver-parameters).
14. Repeat this procedure for the eDirectory driver deployed in the connected eDirectory server.
