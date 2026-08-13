# 9.2 Security Planning

Topics in this section include

* [Users, Passwords, and Groups](brfi74u.html#brfickf)
* [Connection Security](brfi74u.html#brfiaga)
* [Administrative Password Resets](brfi74u.html#brfibau)
* [Securing the AS Client API](brfi74u.html#brfibph)

## 9.2.1 Users, Passwords, and Groups

In order for users to be able to log in to the operating system using Authentication Services, they must be defined to the operating system on the platform. You can automate account maintenance through the use of provisioning events. For details about managing accounts, see [Identity Provisioning](babfiejd.html).

Users, passwords, and groups in eDirectory™ that do not conform to the character set and length restrictions imposed by your operating system cannot participate in Authentication Services or Identity Provisioning on your platform.

The Identity Manager Fan-Out Driver does not support authentication or password change for users having a null password.

In some cases, a system other than eDirectory might contain the users that you want to participate with the Identity Manager Fan-Out Driver. There are tools, such as LDIF, that you can use to import these users into eDirectory. If you cannot extract the passwords for the affected user accounts, you can use the Password Migration component of the Fan-Out Driver. This component can help you accomplish a smooth transition to basing your user accounts in eDirectory.

## 9.2.2 Connection Security

The connection between the Platform Receiver and Event Journal Services uses Secure Sockets Layer (SSL). SSL connections are authenticated through the use of certificates. Some types of the Platform Services Process use SSL for their connections to the Core Drivers for Authentication Services, and others use DES encryption.

Obtaining a security certificate for your platform from the Core Driver requires that you supply the fully distinguished name and password of an eDirectory user with Read and Create object rights to the ASAM System container.

Identity Manager Fan-Out Driver platform certificates are stored in the data\ platformservices\certs subdirectory of the ASAM directory of their host server file system. Ensure that access to the certs directory is limited to the appropriate users.

## 9.2.3 Administrative Password Resets

Administrative password resets must be done through an eDirectory utility, such as iManager, or through a program that uses the AS Client API.

## 9.2.4 Securing the AS Client API

Use of the AS Client API is secured on IBM i and UNIX platforms through SSL and a token that is stored in the asam\data\platformservices\certs directory by the Platform Services Process. Ensure that access to the certs directory is limited to the appropriate users.

Use of the AS Client API is secured on z/OS Platforms through the Authorized Program Facility (APF). Ensure that access to the z/OS Platform Services Load Library is limited to the appropriate users.
