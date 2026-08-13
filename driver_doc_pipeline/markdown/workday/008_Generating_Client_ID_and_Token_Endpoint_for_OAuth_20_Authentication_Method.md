# 2.4 Generating Client ID and Token Endpoint for OAuth 2.0 Authentication Method

Before creating the driver object, you must generate the workday client ID and the end point token URL. It is also recommended to create a public key certificate prior to creating the client ID and token endpoint. The following sections explain the procedure to create a Public Key Certificate, and the Client ID and Token Endpoint.

## 2.4.1 Creating x509 Public Key Certificate

The following steps explain the procedure to create a public key certificate:

1. Run the following keytool command on your platform:

   keytool -genkey -keyalg RSA -alias Workday -keystore JWTkeystore.ks -storetype PKCS12 -storepass <Workday123!> -validity 360 -keysize 2048

   NOTE:

   * The keytool command is common for both Linux and Windows platforms.
   * You must specify the storetype as PKCS12 as shown in the above keytool command.
2. Enter the following details when prompted:

   * First Name
   * Last Name
   * Organizational Unit
   * Organization
   * City
   * Province
   * Country Code
3. Enter Yes to confirm. The keystore file is created, for example: JWTkeystore.pkcs12.
4. Extract the public key and the certificate by entering the following command:

   ```
   keytool -export -alias Workday -keystore JWTkeystore.ks -rfc -file publickey.cert
   ```
5. You will be prompted to enter the password. Enter the password to create the certificate, for example publickey.cert.

   *NOTE:*The password does not display on the screen when entered. Ensure to remember the entered password or save it in a convenient location.
6. Run the following command, to display the certificate.

   cat publickey.cert
7. Copy the certificate from the BEGIN CERTIFICATE line till END CERTIFICATE line, and save it in a convenient location.

## 2.4.2 Generating Client ID and Token Endpoint

Perform the following steps to generate the Client ID and Token Endpoint:

1. Login to Workday application.
2. Search and click on Register API Client.

   1. In the Client Name field, enter the name of the client.
   2. In the Client Grant Type field, select Jwt Bearer Grant.
   3. In the x509 Certificate field, select Create x509 Public Key.
   4. In the Create x509 Public Key page, enter your name and paste the certificate generated as shown in [Creating x509 Public Key Certificate](t4eie9te8d7c.html#t4f4hedopy5q).
   5. Select Access Token Type as Bearer.
   6. Enter the Redirection URL. This could be your organization’s home page URL.
   7. Select the following Scope values from Workday REST API:

      * Contact Information
      * Integration
      * Jobs & Positions
      * Organizations & Roles
      * Personal Data
      * System
      * Tenant Non-configurable
      * Include Workday Owned Scope
3. Click OK to generate the Client ID and the Token Endpoint.
4. Save the Client ID and the Token Endpoint in a convenient location, as these values will be required to configure OAuth 2.0 authentication method for the Workday driver.
