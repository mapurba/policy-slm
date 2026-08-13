# 4.2 Configuring TLS/SSL Communication with the Entity Data Model Database

To ensure that the Entity Data Model driver communicates securely with the Entity Data Model database, you can configure a TLS/SSL connection. You must enable SSL for both the database and the driver.

* [Preparing the Database Platform for SSL Communication](b1fu7np8.html#b1g1f5o7)
* [Enabling the Entity Data Model Databases for SSL Communication](b1fu7np8.html#b1g0zlav)
* [Enabling the Entity Data Model Driver for SSL Communication](b1fu7np8.html#b1fu7r2v)

## 4.2.1 Preparing the Database Platform for SSL Communication

This section provides information for creating an SSL server certificate that the PostgreSQL and Oracle database platforms can use for secure communication with the Entity Data Model driver.

* [Preparing PostgreSQL for SSL Communication](b1fu7np8.html#b1fu7np9)
* [Preparing Oracle for SSL Communication](b1fu7np8.html#b1fyw3nt)

### Preparing PostgreSQL for SSL Communication

1. On the server where you deployed Entity Data Model, stop Tomcat.
2. Log in to the PostgreSQL server for Entity Data Model.
3. Stop Postgres.
4. To generate a passphrase-protected certificate, enter the following command:

   ```
   openssl req -new -text -out cert.req
   ```
5. To remove the passphrase so the server can start the postmaster automatically, enter the following command:

   ```
   openssl rsa -in privkey.pem -out cert.pem
   ```
6. To convert the certificate into a self-signed certificate, enter the following command:

   ```
   openssl req -x509 -in cert.req -text -key cert.pem -out cert.cert
   ```
7. Copy the following files to the data directory of the PostgreSQL installation:

   * cp cert.pem $PGDATA/server.key
   * cp cert.cert $PGDATA/server.crt

     where $PGDATA = /opt/netiq/idm/apps/postgresql/data/
8. To change the permission of the files, navigate to the /opt/netiq/idm/apps/postgresql/data/ directory and enter the following commands:

   ```
   chown postgres:postgres server.key
   chown postgres:postgres server.crt
   chmod 600 server.key
   ```
9. In a text editor, change the SSL setting in the $PGDATA/postgresql.conf file to on. For example:

   ```
   ssl=on
   ssl_cert_file = '/opt/netiq/idm/apps/postgresql/data/server.crt' # (change requires restart)
   ssl_key_file = '/opt/netiq/idm/apps/postgresql/data/server.key'  # (change requires restart)
   ```
10. Save and close the file.
11. Start Postgres.
12. (Optional) To verify that SSL communication is enabled for Postgres, complete the following steps:

    1. Enter $ ./opt/netiq/idm/apps/postgres/bin/psql -U postgres -h localhost.
    2. Verify that the output is similar to the following content:

       ```
       psql (9.0.3)
       SSL connection (cipher: DHE-RSA-AES256-SHA, bits: 256)
       Type "help" for help.
       ```
13. Add the server.crt that you created in [Step 7](b1fu7np8.html#step7certcreation) to the cacert. For example, enter the following command:

    ```
    keytool -import -trustcacerts -alias ar -file server.crt -keystore /opt/netiq/idm/apps/jre/lib/security/cacerts
    ```
14. Start Tomcat.
15. Ensure that you update the Entity Data Model databases to recognize the secured connection.

    For more information, see [Enabling the Entity Data Model Databases for SSL Communication](b1fu7np8.html#b1g0zlav).

### Preparing Oracle for SSL Communication

To enable SSL in Oracle, you must have a certificate for the Oracle Server signed by a certificate authority (CA).

1. Download and unpack the SSL helper scripts named ssl.ca-0.1.tar.gz.
2. Create a certification request using Oracle Wallet Manager (/opt/oracle/product/11gR1/db/owm) using the following commands:

   ```
   su –oracle
   owm
   ```
3. Select Wallet > New.
4. Enter your password, then select Yes to create folders for the wallet.
5. Fill in the requested information, then select OK.
6. Highlight the certification request, then select Operations > Export Certificate Request.
7. Save the file with the extension .csr in the folder where you extracted ssl.ca-0.1.tar.gz then save the wallet.
8. Create a self-signed root certificate by running the new-root-ca.sh script in the ssl.ca-0.1 folder that you extracted in the previous step to create a file called ca.crt.
9. To run the script that creates the self-signed server certificate, enter the following command:

   ```
   ./sign-server-cert.sh CerReq
   ```
10. Import the ca.crt into the Oracle wallet as a trusted certificate and import the certificate-request-filename.crt as a user certificate.
11. Enable auto-login and save the wallet so that it is now ready for use.
12. To configure Oracle advanced security and listener configuration on the database server, run the following commands:

    ```
    su – oracle
    netmgr
    ```
13. Select Profile > Select Network Security > SSL.
14. Ensure that the sqlnet.ora and listener.ora files mention the WALLET.
15. (Conditional) If the SSL\_CLIENT\_AUTHENTICATION parameter is not set, the default setting is TRUE and clients are required to present a certificate during the SSL handshake. If you do not need client authentication, disable it with the following parameter added to the end of the $TNS\_ADMIN/listener.ora and $TNS\_ADMIN/sqlnet.ora files: SSL\_CLIENT\_AUTHENTICATION=FALSE
16. Restart the listener:

    ```
    lsnrctl stop
    lsnrctl start
    ```
17. Ensure that you update the Entity Data Model databases to recognize the secured connection.

    For more information, see [Enabling the Entity Data Model Databases for SSL Communication](b1fu7np8.html#b1g0zlav).

## 4.2.2 Enabling the Entity Data Model Databases for SSL Communication

To use TLS/SSL connections, the three Entity Data Model databases need the server certificate information. This section applies to both Oracle and PostgreSQL platforms.

1. Enable SSL functionality in the database platform.

   For more information, see [Preparing PostgreSQL for SSL Communication](b1fu7np8.html#b1fu7np9) or [Preparing Oracle for SSL Communication](b1fu7np8.html#b1fyw3nt).
2. Log in to the server where you deployed Entity Data Model.
3. Stop Tomcat:

   ```
   /etc/init.d/idmapps_tomcat_init stop
   ```
4. Add the SSL server certificate that you created for the database platform to the cacert. For example:

   PostgreSQL
   :   keytool -import -trustcacerts -alias ar -file server.crt -keystore /opt/netiq/idm/apps/jre/lib/security/cacerts

   Oracle
   :   keytool -import -trustcacerts -alias aroracle -file ca.crt -keystore /opt/netiq/idm/apps/jre/lib/security/cacerts
5. In a text editor, open the server.xml file.
6. For the three Entity Data Model databases listed in the file, specify the URL for the SSL server certificate. For example:

   PostgreSQL
   :   url="jdbc:postgresql://hostname:5432/database\_username?ssl=true"

   Oracle
   :   url="jdbc:oracle:thin:@(DESCRIPTION =(ADDRESS = (PROTOCOL = TCPS)(HOST = hostname)(PORT = 2484))(CONNECT\_DATA =(SERVER = DEDICATED) (SERVICE\_NAME = name))(SECURITY=(SSL\_SERVER\_CERT\_DN='CN=OracleDB,OU=IN,O=IN,L=IN,ST=IN,C=IN')))"

   By default, the databases have the usernames arops, ardcs, and arwf.
7. Start Tomcat:

   ```
   /etc/ini.d/idmapps_tomcat_init start
   ```
8. Ensure that you update the to recognize the secured connection.

   For more information, see [Enabling the Entity Data Model Driver for SSL Communication](b1fu7np8.html#b1fu7r2v).

## 4.2.3 Enabling the Entity Data Model Driver for SSL Communication

The Entity Data Model driver can communicate securely with the Entity Data Model databases. Ensure that you also enable SSL communication in the databases. For more information, see [Preparing PostgreSQL for SSL Communication](b1fu7np8.html#b1fu7np9) or [Preparing Oracle for SSL Communication](b1fu7np8.html#b1fyw3nt).

1. Log in to the server where you installed the Entity Data Model driver and the Remote Loader.
2. Stop the Remote Loader. For example, enter the following command:

   ```
   rdxml -config /home/ARShim.conf -u
   ```
3. In a text editor, open the Remote Loader conf file for the driver, by default ARshim.conf.
4. Add the content of the SSL server certificate to the file. For example:

   PostgreSQL
   :   ```
       -description ARDriver
       -commandport 8000
       -connection "port=8090 rootfile=path/server.crt"
       -trace 5
       -tracefile "/opt/netiq/ar.log"
       -tracefilemax 100M
       -class "com.novell.nds.dirxml.driver.arshim.AccessReviewDriverShim"
       ```

   Oracle
   :   ```
       -description ARDriver
       -commandport 8000
       -connection "port=8090 rootfile=path/ca.crt"
       -trace 5
       -tracefile /tmp/remoteloader.log
       -class com.novell.nds.dirxml.driver.arshim.AccessReviewDriverShim
       ```
5. Save and close the file.
6. Add the server certificate to the Remote Loader Java certs. For example:

   PostgreSQL
   :   keytool -import -trustcacerts -alias ar -file server.crt -keystore /opt/novell/eDirectory/lib64/nds-modules/jre/lib/security/cacerts

   Oracle
   :   keytool -import -trustcacerts -alias aroracle -file ca.crt -keystore /opt/novell/eDirectory/lib64/nds-modules/jre/lib/security/cacerts
7. Start the Remote Loader. For example, enter the following command:

   ```
   rdxml -config /home/ARShim.conf
   ```
8. In the AR Driver configuration, verify that the setting for Entity Data Model Database Connection URL resembles one of the following values:

   PostgreSQL
   :   url="jdbc:postgresql://hostname:5432/database\_username?ssl=true"

   Oracle
   :   jdbc:oracle:thin:@(DESCRIPTION =(ADDRESS = (PROTOCOL = TCPS)(HOST = hostname)(PORT = 2484))(CONNECT\_DATA =(SERVER = DEDICATED) (SERVICE\_NAME = name))(SECURITY=(SSL\_SERVER\_CERT\_DN='CN=OracleDB,OU=IN,O=IN,L=IN,ST=IN,C=IN')))

   By default, the databases have the usernames arops, ardcs, and arwf.
9. Restart the Entity Data Model driver.
