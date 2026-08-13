# 6.2 Driver System Security Overview

System security is maintained through connection certificates between driver components and password-protected access to objects in NetIQ eDirectory™.

## 6.2.1 Connection Security

The connections between Core Driver components and between Event Journal Services and Platform Receivers use Secure Sockets Layer (SSL). Some types of the Platform Services Process use SSL for their connections to Authentication Services, and others use DES encryption. SSL connections are authenticated through the use of certificates.

The certificates used by the Identity Manager Fan-Out Driver are minted by the Certificate Services component of the Core Driver. When you install and configure a new component, you obtain a certificate.

Because platforms cannot examine the configuration objects for the Core Driver in the ASAM System container, Core Driver network address information is included in their certificates under the X.509 Alternate Subject field. This address is specified at installation time and must contain a reverse-lookup DNS record for the Platform Services components to establish trust to the Core Driver. If the address is not resolvable, the Platform Services installation will fail. Likewise, if the address associated with the Platform object does not have a reverse-resolvable DNS record, the Core Driver will not trust the Platform component and therefore will not establish an SSL connection.

The Core Driver certificate is minted when you start the Core Driver for the first time. When you update network address information for a Core Driver, a new certificate is automatically minted for it. You must restart a Core Driver after changing its network address information in order for the new certificate to take effect.

Obtain a new certificate for a platform by starting the Platform Receiver with the appropriate command line parameter. For details, see [Section IV, Platform Services Administration](bexh69n.html).

Identity Manager Fan-Out Driver components store their security certificates and related information in their certs directory. Ensure that access to the certs directory is restricted to the driver system itself and to its administrators.

* *Core Driver:*
  asam\data\coredriver\certs
* *Platform Services:*
  asam\data\platformservices\certs

## 6.2.2 ASAM Master User Security

The Core Driver performs an LDAP bind as the ASAM Master User to gain access to eDirectory. You must not place restrictions on the ASAM Master User object that would interfere with its use by the driver. Set maximum password length for the ASAM Master User to at least 32 characters. Disable intruder detection for the ASAM Master User object so that it cannot be disabled by someone without the appropriate rights.

The ASAM Master User must have Supervisor rights to the container in eDirectory that holds the users and groups that can be added to the Census. This is known as the User and Group Subtree. These rights are granted during installation.

To use the AS Client API to access objects outside of the User and Group subtree, you must grant additional rights to the ASAM Master User.

* You must grant the ASAM Master User Browse object rights and Compare property rights to any object that is accessed through the AS Client API.
* You must grant the ASAM Master User Read property rights to any object whose Security Equals list or Group Membership list, or other attribute value is accessed through the AS Client API.

Because the ASAM Master User is granted significant rights, you must ensure that its password remains secure.

The Core Driver obtains the password of the ASAM Master User from the Driver object. If your security practices prescribe periodic password changes, you can create a second User object to be used as an alternate ASAM Master User. Then you can swap back and forth between these User objects when it is necessary to change the password.

### Creating an Alternate ASAM Master User Object

1. Use iManager to create a new User object. We recommend that you use the same directory context as the original ASAM Master User object.
2. Use iManager to assign the new User object Security Equivalence to the original ASAM Master User object.

Now you have two User objects with the necessary rights to act as the ASAM Master User.

### Changing the Password and Updating the Configuration

The following procedure assumes you have created a second ASAM Master User object as described in the preceding section. It assumes one object is named ASAM1 and the other is named ASAM2. We also assume that ASAM1 is in use and that it is the one listed in the driver configuration parameters.

To change the ASAM Master User object to use a new password:

1. Use iManager to set the new password for ASAM2.
2. Update the Driver object for each Core Driver, specifying ASAM2 for the Authentication ID, and the new password for the Application Password.

   1. In iManager, select Identity Manager Management > Overview.
   2. Locate the driver in its driver set.
   3. Click the driver status indicator in the upper right corner of the driver icon, then click Edit Properties.
   4. Click Identity Manager > Driver Configuration. Authentication ID and Application Password are located under the Authentication heading.
3. Use iManager to change the password of ASAM1 to an undisclosed randomly chosen value.

ASAM2 is now the ASAM Master User, using a new password. The old password (of the ASAM1 user) can no longer be used.

*NOTE:*The Core Driver does an LDAP bind as the ASAM Master User upon startup. There is no need to restart the driver now. It will use ASAM2 the next time it is started.
