# A.2 Troubleshooting Common Problems

* [Driver Shim Installation Failure](b3yee7z.html#b3yexuy)
* [Driver Certificate Setup Failure](b3yee7z.html#b3ygrta)
* [Driver Start Failure](b3yee7z.html#b3ygzqd)
* [Driver Shim Startup or Communication Failure](b3yee7z.html#b3yh50t)
* [Users Are Not Provisioned to the Connected System](b3yee7z.html#b3yh9yg)
* [Users Are Not Provisioned to the Identity Vault](b3yee7z.html#b3yhfcq)
* [Identity Vault User Passwords Are Not Provisioned to the Connected System](b3yee7z.html#b3yhfkf)
* [Connected System User Passwords Are Not Provisioned to the Identity Vault](b3yee7z.html#b3yhkd1)
* [Users Are Not Modified, Deleted, Renamed, or Moved](b3yee7z.html#b3yin8u)
* [Change Log Errors](b3yee7z.html#b6aqr0h)

## A.2.1 Driver Shim Installation Failure

Ensure that you use binary mode to FTP the driver samples library, load library, and REXX exec library XMT files to the target system.

## A.2.2 Driver Certificate Setup Failure

To set up certificates, the driver shim communicates with the Metadirectory server using the LDAP secure port (636).

* Ensure that eDirectory™ is running LDAP with SSL enabled. For details about configuring eDirectory, see the NetIQ eDirectory Administration Guide.
* Ensure that the connected system has network connectivity to the Metadirectory server.

You can use the driver REXX exec library member SETCERT to configure the certificate at any time.

If you cannot configure SSL using LDAP, you can install the certificate manually.

1. In iManager, browse the Security container to locate your tree’s certificate authority (typically named treeName CA).
2. Click the certificate authority object.
3. Click Modify Object.
4. Select the Certificates tab.
5. Click Public Key Certificate.
6. Click Export.
7. Select No to export the certificate without the private key, then click Next.
8. Select Base64 format, then click Next.
9. Click Save the exported certificate to a file, then specify a location to save the file.
10. Use FTP or another method to store the file on the connected system as /opt/novell/acf2drv/keys/ca.pem.

## A.2.3 Driver Start Failure

* Examine the [status log](b3xzdtn.html#b3yeaix) and [DSTRACE](b3xzdtn.html#b3ye3ty) output.
* The driver must be specified as a Remote Loader driver. You can set this option in the iManager Driver Edit Properties window.
* You must activate both Identity Manager and the driver within 90 days. The Driver Set Overview page in iManager shows when Identity Manager requires activation. The Driver Overview page shows when the driver requires activation.

  For details about activating NetIQ Identity Manager Products, see the Identity Manager 4.8 Installation Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/) .
* Ensure that the driver load library is APF-authorized.

  You can use the DISPLAY PROG,APF operator command to display your APF-authorized libraries.
* Ensure that the LDXSERV and SAFQUERY commands are listed as authorized TSO commands in your active IKJTSOxx member.

  You can use the DISPLAY IKJTSO,AUTHCMD operator command to display authorized TSO commands.

For more information about troubleshooting Identity Manager engine errors, see the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## A.2.4 Driver Shim Startup or Communication Failure

* Examine the [trace file](b3xzdtn.html#b3xzpa5).
* Ensure that the connected system’s operating system and security system versions are supported. For a list of supported operating systems, see [Connected System Requirements](b3xccfu.html#b3xcf2n).
* Apply all maintenance for your operating system and security system.
* Ensure that the Remote Loader and Driver object passwords that you specified while setting up the driver on the Metadirectory server match the passwords stored with the driver shim.

  To update these passwords on the connected system, use the SETPWDS REXX exec. The passwords are stored under /opt/novell/acf2drv/keys in encrypted files dpwdlf40 (Driver object password) and lpwdlf40 (Remote Loader password).

  To update these passwords on the Metadirectory server, use iManager to update the driver configuration.
* Ensure that the correct host name and port number of the connected system are specified in the Driver Configuration Remote Loader connection parameters. You can change the port number (default 8090) in the driver shim configuration file.
* Ensure that the driver shim started task has been set up properly. For details, see [Setting Up the Started Tasks](b3xehpq.html#b6gwofm).
* Ensure that only one system in a complex that shares the security system database is running the driver shim started task.

## A.2.5 Users Are Not Provisioned to the Connected System

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, [trace file](b3xzdtn.html#b3xzpa5), and [REXX exec output file](b3xzdtn.html#b3ye15d).
* To be provisioned, users must be in the appropriate base container. You can view and change the base containers in iManager on the Global Configuration Values page of the Driver Edit Properties window.
* To provision identities from the Identity Vault to the connected system, the driver Data Flow property must be set to Bidirectional or Identity Vault to Application. To change this value, re-import the driver rules file over your existing driver.
* The user that the driver is security equivalent to must have rights to read information from the base container. For details about the rights required, see [Table 2-2, Base Container Rights Required by the Driver Security-Equivalent User](b484ok2.html#b4exk92).

## A.2.6 Users Are Not Provisioned to the Identity Vault

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, and [trace file](b3xzdtn.html#b3xzpa5).
* Examine the User Base Container GCV values.
* To provision identities from the connected system to the Identity Vault, the driver Data Flow property must be set to Bidirectional or Application to Identity Vault. To change this value, re-import the driver rules file over your existing driver.
* The user that the driver is security equivalent to must have rights to update the base container. For details about the rights required, see [Table 2-2, Base Container Rights Required by the Driver Security-Equivalent User](b484ok2.html#b4exk92).
* Ensure that the security system exit has been installed, that LLA has been refreshed, and that the exit has been activated. For details, see [Installing the Driver Security System Exits](b3xehpq.html#cegbjdbc).

## A.2.7 Identity Vault User Passwords Are Not Provisioned to the Connected System

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, and [REXX exec output file](b3xzdtn.html#b3ye15d).
* Several password management properties are available in iManager on the Global Configuration Values page of the Driver Edit Properties window. Ensure that the connected system accepts passwords from the Identity Vault. To determine the right settings for your environment, view the help for the options, or see the NetIQ Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
* Ensure that the user’s container has an assigned Universal Password policy and that the Synchronize Distribution Password When Setting Universal Password option is set for this policy.

## A.2.8 Connected System User Passwords Are Not Provisioned to the Identity Vault

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, and the [trace file](b3xzdtn.html#b3xzpa5).
* Several password management properties are available in iManager on the Global Configuration Values page of the Driver Edit Properties window. Ensure that at least one of the following options is set:

  + The Identity Vault Accepts Passwords from the ACF2 Connected System
  + The Identity Vault Accepts Administrative Password Resets from the ACF2 Connected System

  To determine the right settings for your environment, view the help for the options, or see the NetIQ Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
* If the Require Password Policy Validation before Publishing Passwords GCV is set, the user’s password must satisfy the password rules in the password policy assigned to the user container.
* Ensure that the change log started task is running on all systems that share the security system database.
* Ensure that the security system exit has been installed, that LLA has been refreshed, and that the exit has been activated. For details, see [Installing the Driver Security System Exits](b3xehpq.html#cegbjdbc).

## A.2.9 Users Are Not Modified, Deleted, Renamed, or Moved

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, [trace file](b3xzdtn.html#b3xzpa5), and [REXX exec output file](b3xzdtn.html#b3ye15d).
* Examine the driver Data Flow setting to verify the authoritative source for identities.
* Identity Vault and connected system identities must be associated before events are synchronized. To view an identity’s associations, use Modify User/Group in iManager and click the Identity Manager tab. You can migrate identities to establish associations. For details, see [Migrating Identities](b3xxotz.html).
* Identity Vault move events can remove the identity from the base container monitored by the driver to a container that is not monitored by the driver. This makes the move appear to be a delete.
* Moving a user is not supported by ACF2.

## A.2.10 Change Log Errors

* Examine the [change log started task messages](b3xzdtn.html#b6m584r).
* Ensure that the change log started task is running on all systems that share the security system database.
* Ensure that the change log started task has been set up properly. For details, see [Setting Up the Started Tasks](b3xehpq.html#b6gwofm).
* Ensure that you initialized the change log data set during installation. For details about initializing the change log data set, see [Allocating and Initializing the Change Log Data Set](b3xehpq.html#b689r3r).
* You can use the LDXSERV TSO command to display information about the change log data set. Enter the following TSO command:

  ```
    LDXSERV STATUS
  ```

  To use the LDXSERV command, you must include the driver load library in your STEPLIB concatenation.
