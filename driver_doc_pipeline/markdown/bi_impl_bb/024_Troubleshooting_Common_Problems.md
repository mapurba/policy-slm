# 6.3 Troubleshooting Common Problems

* [Driver Shim Installation Failure](fdfds.html#fdfdjsklfd)
* [Driver Rules Installation Failure](fdfds.html#fdsfd)
* [Driver Certificate Setup Failure](fdfds.html#dsfdsdfsf)
* [Driver Start Failure](fdfds.html#fdsfdsfdsfad)
* [Driver Shim Startup or Communication Failure](fdfds.html#fdfddsfds)
* [Users or Groups Are Not Provisioned to Blackboard Learn](fdfds.html#fdsfdsfdd)
* [Identity Vault User Passwords Are Not Provisioned to Blackboard Learn](fdfds.html#fdsfdafd)
* [Metadirectory Objects Are Not Modified, Deleted, Renamed or Moved](fdfds.html#fdsfdfds)

## 6.3.1 Driver Shim Installation Failure

* Ensure that you used the correct installation program for your operating system and that you are running on a supported operating system.
* Ensure that you run the installation as root or equivalent.
* Ensure that your package management software, such as RPM, is installed and up-to-date.

## 6.3.2 Driver Rules Installation Failure

Ensure that you are using a version of iManager or Designer that supports your version of Identity Manager.

## 6.3.3 Driver Certificate Setup Failure

* Ensure that eDirectory is running LDAP with SSL enabled. For details about configuring eDirectory, see NetIQ eDirectory Administration Guide.
* Ensure that the connected system has network connectivity to the Metadirectory server.

You can use the command /opt/novell/bbdrv/bin/bbdrv -s to configure the certificate at any time.

If you cannot configure SSL using LDAP, you can install the certificate manually:

1. In iManager, browse to the Security container to locate your tree’s Certificate Authority (typically named treeName CA).
2. Click the Certificate Authority object.
3. Click Modify Object.
4. Select the Certificates tab.
5. Click Public Key Certificate.
6. Click Export.
7. Select No to export the certificate without the private key, then click Next.
8. Select Base64 format, then click Next.
9. Click Save to save the exported certificate to a file, then specify a location to save the file.
10. Use FTP, SSH or any other method to store the file on the connected system as ca.pem in the keys directory under the driver installation directory.

## 6.3.4 Driver Start Failure

* Examine the status log and DSTRACE output.
* The driver must be specified as a Remote Loader driver, even if the Identity Vault and connected system are the same computer. You can set this option in the iManager Driver Edit Properties window.
* You must activate both Identity Manager and the driver within 90 days. The Driver Set Overview page in iManager shows when Identity Manager requires activation. The Driver Overview page shows when the driver requires activation.
* For details about activating NetIQ Identity Manager Products, see the Identity Manager Installation Guide at

## 6.3.5 Driver Shim Startup or Communication Failure

* Examine the trace file.
* Ensure the connected systems’ operating system version is supported. Apply all patches for your operating system.
* Ensure that the Remote Loader and Driver Object passwords that you specified while setting up the driver on the Metadirectory server match the passwords stored with the driver shim.
* To update these passwords on the connected system, us the /opt/novell/bbdrv/bin/bbdrv -sp command. The passwords are stored under keys in the driver installation directory in encrypted files dpwdl1f40 (Driver object password) and lpwd1f40 (Remote Loader password).
* To update these passwords on the Metadirectory server, use iManager to update the driver configuration. For details, see [Section 5.0, Managing the Driver](b3r8tx2.html).

## 6.3.6 Users or Groups Are Not Provisioned to Blackboard Learn

* Examine the status log, DSTRACE output, trace file and script output file.
* To be provisioned, users and groups must be in the appropriate base container. You can view and change the base containers in iManager on the Global Configuration Values page of the Driver Edit Properties window.
* To provision identities from the Identity Vault to Blackboard Learn, the driver Data Flow property must be set to Identity Vault to Application. To change this value, re-import the driver rules file over your existing driver.
* The user that the driver is security equivalent to must have rights to read information from the base container. For details about the rights required, see [Table 3-1](saddsa.html#b23ii0h9).

## 6.3.7 Identity Vault User Passwords Are Not Provisioned to Blackboard Learn

* Examine the status log, DSTRACE output, and script output file.
* There are several password management properties available in iManager on the Global Configuration Values page of the Driver Edit Properties window. Ensure that the connected system accepts passwords from the Identity Vault. To determine the right settings for your environment, view the help for the options, or see the Identity Manager Administration Guide.
* Ensure that the user’s container has an assigned Universal Password policy and that the Synchronize Distribution Password When Setting Universal Password GCV is set for this policy.

## 6.3.8 Metadirectory Objects Are Not Modified, Deleted, Renamed or Moved

* Examine the status log, DSTRACE output, trace file and script output file.
* Examine the driver Data Flow. Identity Vault and connected system identities must be associated before events are synchronized. To view an identity’s associations, use Modify User/Group in iManager and click the Identity Manager tab.
* Identity Vault move events can remove the identity from the base container monitored by the driver to a container that is not monitored by the driver. This makes the move appear to be a delete
