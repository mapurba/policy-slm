# 5.1 Installing on Windows

1. Download the Integration Module for Sentinel (driver shim), sentinel\_driver\_install.exe, from the [NetIQ download Web site](http://download.novell.com/index.jsp).
2. Execute the sentinel\_driver\_install.exe file on the Windows system, which is either the Identity Manger server or the Remote Loader, depending on where you want to install the driver shim.
3. Follow the installer prompts.

Once the installation is complete, ensure that you import the certificate since the driver users TLS/SSL protocol to communicate with the server. The type of certificate depends on the Sentinel server configuration:

* [Self-signed public key certificate](installing-on-windows.html#self_signedcerti)
* [Trusted root certificate of the certificate authority](installing-on-windows.html#trusted_rootcert)

#### Self-signed Certificate

If your organization has not replaced the default Web server certificate, which is created when the Sentinel server is installed, you must obtain the self-signed certificate from the Sentinel server.

You can obtain this certificate either by [using the supplied getcert utility](installing-on-windows.html#using_getcertutil) or [extracting it from the keystore file](installing-on-windows.html#obtaining_certks) on the Sentinel server.

*Using the getcert utility*

1. Run the getcert utility on the system where you are running Identity Manager Designer. If the getcert.jar file is not located on the Identity Manager Designer system, you can either copy the getcert.jar file from the system on which you ran the Integration Module installer or install the getcert.jar file directly on the system using the Integration Module installer:

   *Windows:*
   Locate the getcert.jar file in Windows Explorer and double-click the file.

   *Linux:*
   Execute the /opt/novell/eDirectory/lib/dirxml/util/sentinel\_rest/getcert.jar file by using the following command:

   ```
   java -jar getcert.jar
   ```
2. Specify the address and port of the Sentinel server and click Get Certificate.

   The certificate data is displayed.
3. Verify the certificate data and if the certificate is correct, click Yes.
4. Use this certificate data when prompted for the Sentinel TLS/SSL certificate while creating the driver.

   For more information, see [Step 4](creating-the-driver.html#bzpuulz) in [Creating the Driver](creating-the-driver.html).

*Obtaining the certificate from the keystore file*

Extract the Webserver certificate as the root user, from the following Java keystore file:

```
/etc/opt/novell/sentinel/config/.webserverkeystore.jks
```

The keystore password is password.

#### Trusted Root Certificate of the Certificate Authority

If your organization has replaced the Sentinel server default Web server certificate with a public key certificate signed by a certificate authority, such as Verisign or Entrust, you must obtain the appropriate trusted root certificate that corresponds to the certificate authority. You can obtain the trusted root certificate from your organization or the certificate authority your organization uses.
