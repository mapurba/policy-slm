# A.2 Troubleshooting Common Problems

* [Driver Shim Installation Failure](b8no2jy.html#b8no39k)
* [Driver Rules Installation Failure](b8no2jy.html#b8no3p1)
* [Driver Certificate Setup Failure](b8no2jy.html#b8no3x4)
* [Driver Start Failure](b8no2jy.html#b8no52c)
* [Driver Shim Startup or Communication Failure](b8no2jy.html#b8no5uz)
* [Users or Groups Are Not Provisioned to the Connected System](b8no2jy.html#b8no6y5)
* [Users or Groups Are Not Provisioned to the Identity Vault](b8no2jy.html#b8no7bc)
* [Identity Vault User Passwords Are Not Provisioned to the Connected System](b8no2jy.html#b8no7qu)
* [Connected System User Passwords Are Not Provisioned to the Identity Vault](b8no2jy.html#b8no83w)
* [Metadirectory Objects Are Not Modified, Deleted, Renamed, or Moved](b8no2jy.html#b8no8yj)

## A.2.1 Driver Shim Installation Failure

* Ensure that you use the correct installation program for your operating system and that you are running on a supported operating system. For details, see [Section 2.0, Planning for the Scripting Driver](b8mnrmz.html).
* Ensure that you run the installation as root (Linux/UNIX) or Administrator (Windows) or equivalent.
* (Linux/UNIX only) Ensure that your package management software, such as RPM, is installed and up-to-date.

## A.2.2 Driver Rules Installation Failure

Ensure that you use a version of iManager that supports your version of Identity Manager.

## A.2.3 Driver Certificate Setup Failure

To set up certificates, the driver shim communicates with the Metadirectory server using the LDAP secure port (636).

* Ensure that eDirectory™ is running LDAP with SSL enabled. For details about configuring eDirectory, see the NetIQ eDirectory Administration Guide.
* Ensure that the connected system has network connectivity to the Metadirectory server.

You can use the command /opt/novell/usdrv/bin/usdrv -s (Linux/UNIX) or wsdriver -s (Windows) to configure the certificate at any time.

If you cannot configure SSL using LDAP, you can install the certificate manually:

1. In iManager, browse the Security container to locate your tree’s Certificate Authority (typically named treeName CA).
2. Click the Certificate Authority object.
3. Click Modify Object.
4. Select the Certificates tab.
5. Click Public Key Certificate.
6. Click Export.
7. Select No to export the certificate without the private key, then click Next.
8. Select Base64 format, then click Next.
9. Click Save to save the exported certificate to a file, then specify a location to save the file.
10. Use FTP or another method to store the file on the connected system as ca.pem in the keys directory under the driver installation directory.

## A.2.4 Driver Start Failure

* Examine the status log and DSTRACE output.
* The driver must be specified as a Remote Loader driver, even if the Identity Vault and connected system are the same computer. You can set this option in the iManager Driver Edit Properties window.
* You must activate both Identity Manager and the driver within 90 days. The Driver Set Overview page in iManager shows when Identity Manager requires activation. The Driver Overview page shows when the driver requires activation.

  For details about activating NetIQ Identity Manager Products, see the Identity Manager Installation Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

For more information about troubleshooting Identity Manager engine errors, see the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## A.2.5 Driver Shim Startup or Communication Failure

* Examine the trace file.
* Ensure that the connected system’s operating system version is supported. For a list of supported operating systems, see [Section 2.0, Planning for the Scripting Driver](b8mnrmz.html).
* Apply all patches for your operating system.
* Ensure that the Remote Loader and Driver object passwords that you specified while setting up the driver on the Metadirectory server match the passwords stored with the driver shim.

  To update these passwords on the connected system, use the /opt/novell/usdrv/bin/usdrv -sp (Linux/UNIX) or use the wsdriver -sp (Windows) command. The passwords are stored under keys in the driver installation directory in encrypted files dpwdlf40 (Driver object password) and lpwdlf40 (Remote Loader password).

  To update these passwords on the Metadirectory server, use iManager to update the driver configuration. For details, see [Driver Configuration Page](b8mp4y6.html#b8mpjjq).
* Ensure that the correct host name and port number of the connected system are specified in the Driver Configuration Remote Loader connection parameters. You can change the port number (default 8090) in usdrv.conf (Linux/UNIX) or wsdrv.conf (Windows).

## A.2.6 Users or Groups Are Not Provisioned to the Connected System

* Examine the status log, DSTRACE output, trace file, and script output file.
* To be provisioned, users and groups must be in the appropriate base container. You can view and change the base containers in iManager on the Global Configuration Values page of the Driver Edit Properties window.
* To provision identities from the Identity Vault to the connected system, the driver Data Flow property must be set to Bidirectional or Identity Vault to Application. To change this value, reimport the driver rules file over your existing driver.
* The user that the driver is security equivalent to must have rights to read information from the base container. For details about the rights required, see [Table 2-1](b8mo9gg.html#b8moaut).

## A.2.7 Users or Groups Are Not Provisioned to the Identity Vault

* Examine the status log, DSTRACE output, and trace file.
* Examine the User Base Container and Group Base Container GCV values. For more details, [Global Configuration Values Page](b8mp4y6.html#b8mqhhb).
* To provision identities from the connected system to the Identity Vault, the driver Data Flow property must be set to Bidirectional or Application to Identity Vault. To change this value, reimport the driver rules file over your existing driver.
* The user that the driver is security equivalent to must have rights to update the base container. For details about the rights required, see [Table 2-1](b8mo9gg.html#b8moaut).

## A.2.8 Identity Vault User Passwords Are Not Provisioned to the Connected System

* Examine the status log, DSTRACE output, and script output file.
* There are several password management properties available in iManager on the Global Configuration Values page of the Driver Edit Properties window. Ensure that the connected system accepts passwords from the Identity Vault. To determine the right settings for your environment, view the help for the options, or see the Identity Manager Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
* Ensure that the user’s container has an assigned Universal Password policy and that the Synchronize Distribution Password When Setting Universal Password GCV is set for this policy.

## A.2.9 Connected System User Passwords Are Not Provisioned to the Identity Vault

* Examine the status log, DSTRACE output, and the trace file.
* There are several password management properties available in iManager on the Global Configuration Values page of the Driver Edit Properties window. Ensure that at least one of the following options is set:

  + The Identity Vault Accepts Passwords from the Connected System
  + The Identity Vault Accepts Administrative Password Resets from the Connected System
  + To determine the right settings for your environment, view the help for the options, or see the Identity Manager Administration Guide on the [Identity Manager 4.8 Documentation Web](https://www.netiq.com/documentation/identity-manager-47/).
  + If the Require Password Policy Validation before Publishing Passwords GCV is set, the user’s password must satisfy the password rules in the password policy assigned to the user container.

## A.2.10 Metadirectory Objects Are Not Modified, Deleted, Renamed, or Moved

* Examine the status log, DSTRACE output, trace file, and script output file.
* Examine the driver Data Flow setting to verify the authoritative source for identities.
* Identity Vault and connected system identities must be associated before events are synchronized. To view an identity’s associations, use Modify User/Group in iManager and click the Identity Manager tab.
* Identity Vault move events can remove the identity from the base container monitored by the driver to a container that is not monitored by the driver. This makes the move appear to be a delete.
