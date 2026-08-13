# 4.1 Configuring TLS/SSL Communication with Identity Manager

To ensure that the Entity Data Model driver communicates securely with the Entity Data Model server and the User Application, you can configure a TLS/SSL connection. The driver supports the following types of certificates for secure communication:

* Self-signed public key certificate for the server
* Trusted root certificate of the certificate authority (CA) used to sign the server’s public key certificate

## 4.1.1 Using a Self-Signed Public Key Certificate

To use a self-signed public key certificate, you need the iac-certtool utility. You can download the utility from the Entity Data Model customer portal.

1. Log in to the Entity Data Model server as an administrator.
2. Run the iac-certtool utility.
3. Specify the URL for the Entity Data Model application or the User Application.
4. Select Get Certificate.
5. If the content of the certificate is correct, select Yes.
6. Copy the certificate content to a text file.
7. In Designer, run the configuration wizard for the Entity Data Model driver.
8. In the Publisher configuration section, paste the certificate content in the certificate input field.
9. Complete the configuration, and then deploy the updated driver.

## 4.1.2 Using a Trusted Root Certificate from a Certificate Authority

If your organization uses a public key certificate signed by a certificate authority, such as Verisign or Entrust, you must obtain the appropriate trusted root certificate that corresponds to the certificate authority. You can obtain the trusted root certificate from your organization or the certificate authority your organization used.

1. Acquire the trusted root certificate.
2. In Designer, run the configuration wizard for the Entity Data Model driver.
3. In the Publisher configuration section, import the trusted root certificate.
4. Complete the configuration, and then deploy the updated driver.
