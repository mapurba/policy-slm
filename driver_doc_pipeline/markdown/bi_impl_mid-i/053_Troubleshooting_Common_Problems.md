# A.2 Troubleshooting Common Problems

* [Driver Rules Installation Failure](b3yee7z.html#b3yfj1c)
* [Driver Certificate Setup Failure](b3yee7z.html#b3ygrta)
* [Driver Start Failure](b3yee7z.html#b3ygzqd)
* [Driver Shim Startup or Communication Failure](b3yee7z.html#b3yh50t)
* [Users or Groups Are Not Provisioned to the Connected System](b3yee7z.html#b3yh9yg)
* [Users or Groups Are Not Provisioned to the Identity Vault](b3yee7z.html#b3yhfcq)
* [Identity Vault User Passwords Are Not Provisioned to the Connected System](b3yee7z.html#b3yhfkf)
* [Connected System User Passwords Are Not Provisioned to the Identity Vault](b3yee7z.html#b3yhkd1)
* [Users or Groups Are Not Modified, Deleted, Renamed, or Moved](b3yee7z.html#b3yin8u)

## A.2.1 Driver Rules Installation Failure

Ensure that you use a version of iManager that is compatible with your version of Identity Manager.

## A.2.2 Driver Certificate Setup Failure

To set up certificates, the driver shim communicates with the Metadirectory server using the LDAP secure port (636).

* Ensure that eDirectory™ is running LDAP with SSL enabled. For details about configuring eDirectory, see the NetIQ eDirectory Administration Guide.
* Ensure that the connected system has network connectivity to the Metadirectory server.

To configure the certificate, use the I5OSDRV menu. For more information about the menu, see [Using the I5OSDRV Menu](b4n1vhs.html).

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
10. Use FTP or another method to store the file on the connected system in the driver IFS path as keys/ca.pem.

    If you installed the driver using the default driver IFS path, store the file as /usr/local/i5osdrv/keys/ca.pem.

## A.2.3 Driver Start Failure

* Examine the [status log](b3xzdtn.html#b3yeaix) and [DSTRACE](b3xzdtn.html#b3ye3ty) output.
* The driver must be specified as a Remote Loader driver. You can set this option in the iManager Driver Edit Properties window.
* You must activate both Identity Manager and the driver within 90 days. The Driver Set Overview page in iManager shows when Identity Manager requires activation. The Driver Overview page shows when the driver requires activation.

  For details about activating NetIQ Identity Manager Products, see the Identity Manager Installation Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/) .

For more information about troubleshooting Identity Manager engine errors, see the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## A.2.4 Driver Shim Startup or Communication Failure

* Examine the [trace file](b3xzdtn.html#b3xzpa5).
* Apply all patches for your operating system.
* Ensure that the Remote Loader and Driver object passwords that you specified while setting up the driver on the Metadirectory server match the passwords stored with the driver shim.

  The passwords are stored in the driver IFS path in the keys directory in encrypted files dpwdlf40 (Driver object password) and lpwdlf40 (Remote Loader password).

  To update these passwords on the connected system, use the I5OSDRV menu. For more information about the menu, see [Using the I5OSDRV Menu](b4n1vhs.html).

  To update these passwords on the Metadirectory server, use iManager to update the driver configuration. For details, see [Driver Configuration Page](b3xub84.html#b4d9ehs).
* Ensure that the correct host name and port number of the connected system are specified in the Driver Configuration Remote Loader connection parameters. You can change the port number (default 8090) in the driver shim configuration file.

## A.2.5 Users or Groups Are Not Provisioned to the Connected System

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, [trace file](b3xzdtn.html#b3xzpa5), and [job log](b3xzdtn.html#b3xzhok).
* To be provisioned, users and groups must be in the appropriate base container. You can view and change the base containers in iManager on the Global Configuration Values page of the Driver Edit Properties window. For more details, see [Global Configuration Values Page](b3xub84.html#b4d9yhs).
* To provision identities from the Identity Vault to the connected system, the driver Data Flow property must be set to Bidirectional or Identity Vault to Application. To change this value, re-import the driver rules file over your existing driver.
* The user that the driver is security equivalent to must have rights to read information from the base container. For details about the rights required, see [Table 2-2, Base Container Rights Required by the Driver Security-Equivalent User](b484ok2.html#b4exk92).

## A.2.6 Users or Groups Are Not Provisioned to the Identity Vault

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, and [trace file](b3xzdtn.html#b3xzpa5).
* Examine the User Base Container and Group Base Container GCV values. For more details, see [Global Configuration Values Page](b3xub84.html#b4d9yhs).
* To provision identities from the connected system to the Identity Vault, the driver Data Flow property must be set to Bidirectional or Application to Identity Vault. To change this value, re-import the driver rules file over your existing driver.
* The user that the driver is security equivalent to must have rights to update the base container. For details about the rights required, see [Table 2-2, Base Container Rights Required by the Driver Security-Equivalent User](b484ok2.html#b4exk92).

## A.2.7 Identity Vault User Passwords Are Not Provisioned to the Connected System

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, and [job log](b3xzdtn.html#b3xzhok).
* There are several password management properties available in iManager on the Global Configuration Values page of the Driver Edit Properties window. Ensure that the connected system accepts passwords from the Identity Vault. To determine the right settings for your environment, view the help for the options, or see the NetIQ Identity Manager 3.6.1 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
* Ensure that the user’s container has an assigned Universal Password policy and that the Synchronize Distribution Password When Setting Universal Password option is set for this policy.

## A.2.8 Connected System User Passwords Are Not Provisioned to the Identity Vault

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, and the [trace file](b3xzdtn.html#b3xzpa5).
* Ensure that the The Identity Vault Accepts Passwords from the i5/OS Connected System GCV is set.
* To publish password change information, you must change passwords with a method that uses the Validate Password exit program. The driver obtains password change information from this exit. Administrative password resets must be performed in the Identity Vault.
* If the Require Password Policy Validation before Publishing Password GCV is set, the user’s password must satisfy the password rules in the password policy assigned to the user container.

## A.2.9 Users or Groups Are Not Modified, Deleted, Renamed, or Moved

* Examine the [status log](b3xzdtn.html#b3yeaix), [DSTRACE](b3xzdtn.html#b3ye3ty) output, [trace file](b3xzdtn.html#b3xzpa5), and [job log](b3xzdtn.html#b3xzhok).
* Examine the driver Data Flow setting to verify the authoritative source for identities.
* Identity Vault and connected system identities must be associated before events are synchronized. To view an identity’s associations, use Modify User/Group in iManager and click the Identity Manager tab. You can migrate identities to establish associations. For details, see [Migrating Identities](b3xxotz.html).
* Renaming profiles is not supported by i5/OS. The driver can optionally process rename commands by deleting and recreating a profile with identical attributes and the new name. Before using this functionality, please review the CL \*PGM source found in rename.cl, renuser.cl, rengroup.cl and make sure it meets the requirements of your environment. For details, see [The Scriptable Framework](b410u7u.html). To enable rename processing, disable the Veto Rename Events policy in the Event Transformation.
* Identity Vault move events can remove the identity from the base container monitored by the driver to a container that is not monitored by the driver. This makes the move appear to be a delete.
