# A.2 Troubleshooting Common Problems

* [Driver Shim Installation Failure](b3yee7z.html#b3yexuy)
* [Schema Update Failure](b3yee7z.html#b3yfkmw)
* [Driver Certificate Setup Failure](b3yee7z.html#b3ygrta)
* [Driver Start Failure](b3yee7z.html#b3ygzqd)
* [Driver Shim Startup or Communication Failure](b3yee7z.html#b3yh50t)
* [Users or Groups Are Not Provisioned to the Connected System](b3yee7z.html#b3yh9yg)
* [Users or Groups Are Not Provisioned to the Identity Vault](b3yee7z.html#b3yhfcq)
* [Identity Vault User Passwords Are Not Provisioned to the Connected System](b3yee7z.html#b3yhfkf)
* [Connected System User Passwords Are Not Provisioned to the Identity Vault](b3yee7z.html#b3yhkd1)
* [Users or Groups Are Not Modified, Deleted, Renamed, or Moved](b3yee7z.html#b3yin8u)

## A.2.1 Driver Shim Installation Failure

* Ensure that you use the correct installation program for your operating system and that you are running on a supported operating system. For details, see [Table 3-1, Linux and UNIX Installation Script Filenames](b3xd1sq.html#b48oqe8).

  Also, for more information about required systems and software, as well as supported platforms and operating environments, see [the Identity Manager 4.8 Drivers Documentation Web site](https://www.netiq.com/documentation/identity-manager-47-drivers). From this index page, you can select a readme file associated with the platform(s) for which you need support.
* Ensure that you run the installation as root.
* Ensure that your package management software, such as RPM, is installed and up-to-date.

## A.2.2 Schema Update Failure

Examine the log file at /var/nds/schema.log.

Ensure that you specify the correct parameters (host name, ADMIN FDN in dotted format, and password).

Ensure that you have network connectivity to the Metadirectory server.

## A.2.3 Driver Certificate Setup Failure

To set up certificates, the driver shim communicates with the Metadirectory server using the LDAP secure port (636).

* Ensure that eDirectory™ is running LDAP with SSL enabled. For details about configuring eDirectory, see the NetIQ eDirectory Administration Guide.
* Ensure that the connected system has network connectivity to the Metadirectory server.

You can use the command /usr/local/nxdrv/bin/nxdrv -s to configure the certificate at any time.

If you cannot configure SSL using LDAP, you can install the certificate manually.

1. In iManager, browse the Security container to locate your tree’s Certificate Authority (typically named treeName CA).
2. Click the Certificate Authority object.
3. Click Modify Object.
4. Select the Certificates tab.
5. Click Public Key Certificate.
6. Click Export.
7. Select No to export the certificate without the private key, then click Next.
8. Select Base64 format, then click Next.
9. Click Save the exported certificate to a file, then specify a location to save the file.
10. Use FTP or another method to store the file on the connected system as /usr/local/nxdrv/keys/ca.pem.

## A.2.4 Driver Start Failure

* Examine the [status log](b3xzdtn.html#b3yeaix) and [DSTRACE](b3xzdtn.html#b3ye3ty) output.
* The driver must be specified as a Remote Loader driver, even if the Identity Vault and connected system are the same computer. You can set this option in the iManager Driver Edit Properties window.
* You must activate both Identity Manager and the driver within 90 days. The Driver Set Overview page in iManager shows when Identity Manager requires activation. The Driver Overview page shows when the driver requires activation.

  For details about activating NetIQ Identity Manager Products, see the Identity Manager 4.8 Installation Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/) .

For more information about troubleshooting Identity Manager engine errors, see the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## A.2.5 Driver Shim Startup or Communication Failure

* Examine the [trace file](b3xzdtn.html#b3xzpa5).
* Ensure that the connected system’s operating system version is supported. For information about required systems and software, as well as supported platforms and operating environments, see [the Identity Manager 4.8 D\rivers Documentation Web site](https://www.netiq.com/documentation/idm45/). From this index page, you can select a readme file associated with the platform(s) for which you need support.
* Apply all patches for your operating system.
* Ensure that the Remote Loader and Driver object passwords that you specified while setting up the driver on the Metadirectory server match the passwords stored with the driver shim.

  To update these passwords on the connected system, use the nxdrv-config command. The passwords are stored under /usr/local/nxdrv/keys in encrypted files dpwdlf40 (Driver object password) and lpwdlf40 (Remote Loader password).

  To update these passwords on the Metadirectory server, use iManager to update the driver configuration. For details, see [Driver Configuration Page](b3xub84.html#b4d9ehs).
* Ensure that the correct host name and port number of the connected system are specified in the Driver Configuration Remote Loader connection parameters. You can change the port number (default 8090) in /etc/nxdrv.conf.

## A.2.6 Users or Groups Are Not Provisioned to the Connected System

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, [trace file](b3xzdtn.html#b3xzpa5), and [script output file](b3xzdtn.html#b3ye15d).
* To be provisioned, users and groups must be in the appropriate base container. You can view and change the base containers in iManager on the Global Configuration Values page of the Driver Edit Properties window. For more details, see [Global Configuration Values Page](b3xub84.html#b4d9yhs).
* To provision identities from the Identity Vault to the connected system, the driver Data Flow property must be set to Bidirectional or Identity Vault to Application. To change this value, re-import the driver rules file over your existing driver.
* If the POSIX Management Mode is Manage from Identity Vault, ensure that the identities to be provisioned have RFC 2307 information. Manage from Identity Vault sets the Require POSIX Attributes When Subscribing GCV.
* The user that the driver is security equivalent to must have rights to read information from the base container. For details about the rights required, see [Table 2-2, Base Container Rights Required by the Driver Security-Equivalent User](b484ok2.html#b4exk92).

## A.2.7 Users or Groups Are Not Provisioned to the Identity Vault

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, and [trace file](b3xzdtn.html#b3xzpa5).
* Examine the User Base Container and Group Base Container GCV values. For more details, see [Global Configuration Values Page](b3xub84.html#b4d9yhs).
* To provision identities from the connected system to the Identity Vault, the driver Data Flow property must be set to Bidirectional or Application to Identity Vault. To change this value, re-import the driver rules file over your existing driver.
* The user that the driver is security equivalent to must have rights to update the base container. For details about the rights required, see [Table 2-2, Base Container Rights Required by the Driver Security-Equivalent User](b484ok2.html#b4exk92).

## A.2.8 Identity Vault User Passwords Are Not Provisioned to the Connected System

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, and [script output file](b3xzdtn.html#b3ye15d).
* There are several password management properties available in iManager on the Global Configuration Values page of the Driver Edit Properties window. Ensure that the connected system accepts passwords from the Identity Vault. To determine the right settings for your environment, view the help for the options, or see the NetIQ Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
* Ensure that the user’s container has an assigned Universal Password policy and that the Synchronize Distribution Password When Setting Universal Password option is set for this policy.

## A.2.9 Connected System User Passwords Are Not Provisioned to the Identity Vault

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, and the [trace file](b3xzdtn.html#b3xzpa5).
* There are several password management properties available in iManager on the Global Configuration Values page of the Driver Edit Properties window. Ensure that at least one of the following options is set:

  + The Identity Vault Accepts Passwords from the Linux or UNIX Connected System
  + The Identity Vault Accepts Administrative Password Resets from the Linux or UNIX Connected System

  To determine the right settings for your environment, view the help information for the options, or see the NetIQ Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
* To set a password, use passwd, not yppasswd or passwd -r, because they bypass the authentication module.
* Do not specify a password with useradd. This bypasses the authentication module.
* If the Require Password Policy Validation before Publishing Passwords GCV is set, the user’s password must satisfy the password rules in the password policy assigned to the user container.
* To capture passwords, PAM or LAM and the driver PAM or LAM module must be installed and enabled. For details about installing the driver PAM or LAM module, see [Installing the PAM or LAM Module](b3xfnmq.html).

  You can use the nxdrv-config command on the connected system to configure the PAM or LAM module. For details, see [Using the nxdrv-config Command](b4339kg.html).
* Ensure that remote NIS or NIS+ clients have the driver PAM module installed, that they have a source of entropy, and that they have network connectivity to the driver shim system.
* If you are using Red Hat AS 2.1 or 3.0, ensure that you are using the pam\_pwdb.so PAM module. For details, see [Installing the PAM or LAM Module](b3xfnmq.html).

## A.2.10 Users or Groups Are Not Modified, Deleted, Renamed, or Moved

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, [trace file](b3xzdtn.html#b3xzpa5), and [script output file](b3xzdtn.html#b3ye15d).
* Examine the driver Data Flow setting to verify the authoritative source for identities.
* Identity Vault and connected system identities must be associated before events are synchronized. To view an identity’s associations, use Modify User/Group in iManager and click the Identity Manager tab. You can migrate identities to establish associations. For details, see [Migrating Identities](b3xxotz.html).
* Identity Vault move events can remove the identity from the base container monitored by the driver to a container that is not monitored by the driver. This makes the move appear to be a delete.
* Renaming a user or group is not supported by AIX.
