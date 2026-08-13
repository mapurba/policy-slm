# C.1 Using the nxdrv-config Command

You can use /usr/sbin/nxdrv-config to change the driver shim configuration. When you run this command, you are prompted for the function to perform.

```
> nxdrv-config
Which configuration do you want to perform?
1) Set the Remote Loader and Driver object passwords
2) Configure the driver for Secure Sockets Layer (SSL)
3) Configure the driver to allow for remote client publishing,
   such as NIS or NIS+ clients
4) Extend the schema for Identity Manager (must be run on a
   Metadirectory server)
5) Configure PAM for publishing password changes
6) Configure LAM for publishing password changes
Select one configuration option [q/?]:
```

Enter the number of the function you want to configure, then respond to the prompts as discussed in the following topic:

* [Setting the Remote Loader and Driver Object Passwords](b4339kg.html#b4aazqy)
* [Configuring the Driver for SSL](b4339kg.html#b4ab1fy)
* [Configuring Remote Client Publishing](b4339kg.html#b4ab1fz)
* [Configuring PAM](b4339kg.html#b4ab1g1)
* [Configuring LAM](b4339kg.html#b4ab215)

## C.1.1 Setting the Remote Loader and Driver Object Passwords

The nxdrv-config command prompts you to enter and confirm the Remote Loader password and the Driver object password.

```
Enter Remote Loader password:
Confirm Remote Loader password:
Enter Driver object password:
Confirm Driver object password:
```

The Remote Loader password is used by the Metadirectory engine to authenticate itself to the driver shim (embedded Remote Loader). The Driver object password is used by the driver shim to authenticate itself to the Metadirectory engine.

The Remote Loader and Driver object passwords set by nxdrv-config are stored on the connected system. The Remote Loader and Driver object passwords set for the driver using iManager are stored in the Identity Vault. Each password on the connected system must exactly match its counterpart in the Identity vault.

To change the passwords after driver installation:

1. In iManager, navigate to the Driver Overview for the driver.
2. Click the driver icon.
3. Specify the Driver object password.
4. Specify the Remote Loader password.

   The Remote Loader password is below the Authentication heading.
5. Click Apply.
6. Restart the driver.

## C.1.2 Configuring the Driver for SSL

The nxdrv-config command prompts you to enter the LDAP server host address and port, then displays the Certificate Authority for that server and asks you if you accept it.

```
You are about to connect to the eDirectory LDAP server to retrieve
the eDirectory Tree Trusted Root public certificate.

Enter the LDAP Server Host Address [localhost]: sr.digitalairlines.com
Enter the LDAP Server Port [636]:

Certificate Authority:
   Subject:       ou=Organizational CA,o=TREENAME
   Not Before:    20150321144845Z
   Not After:     20250321144845Z
Do you accept the Certificate Authority? (Y/N) y
```

Enter the host name or IP address and TCP port number of an LDAP server for your Identity Vault. The LDAP server must be configured for SSL, and it must be listening on the SSL port. The default SSL port is 636.

The driver shim connects to the specified server and displays information about the Certificate Authority. If you accept the Certificate Authority, the driver shim saves it to the local file system.

If you do not have LDAP configured for SSL, you can use a manual process to configure the driver for SSL. For details, see [Driver Certificate Setup Failure](b3yee7z.html#b3ygrta).

## C.1.3 Configuring Remote Client Publishing

The nxdrv-config command generates a new certificate and key, used to authenticate remote publishing clients, such as NIS and NIS+ clients.

```
New certificate authority keys were generated:

  Subject:       /CN=soap api certificate authority
  Serial Number: 0
  Valid From:    20160411002823Z
  Valid To:      20260409002823Z
```

The keys are 2048-bit, Base64-encoded, RSA public/private key pairs. They are written to /usr/local/nxdrv/keys/soap-ca-cert.pem (public certificate) and /usr/local/nxdrv/keys/soap-ca-key.pem (private key). These keys are used to issue and sign certificates for remote publishing when you configure PAM on a remote client. The default time duration for the certificate authority is 10 years. You can change the time duration and other remote publisher parameters in the configuration file /usr/local/nxdrv/conf/remote-publisher.conf. For details about the configuration file, see [The Remote Publisher Configuration File](b4dwo69.html).

## C.1.4 Configuring PAM

The nxdrv-config command asks you if you are configuring PAM on a remote client.

If you are configuring PAM on a remote client, the nxdrv-config command does the following:

1. Prompts you for the host name or IP address and port number of the Linux or UNIX connected system.
2. Calls the command to mint a security certificate for the remote client. This command requires you to enter the Remote Loader password.
3. Sets up the PAM configuration file.

If you are configuring PAM on the connected system, the nxdrv-config command sets up the PAM configuration file.

```
Are you configuring PAM from a remote NIS client? (Y/N) [N]
Configuring PAM...
Using PAM configuration file: [/etc/pam.conf]
Inserting line [/usr/lib/security/pam_nxdrv.so.1 mechanism=api]
original PAM file backed up to /etc/pam.conf.nxdrv.04152006151641
```

The nxdrv-config command locates the PAM configuration file, makes a backup copy, and inserts a line for the Linux and UNIX driver PAM module.

## C.1.5 Configuring LAM

The nxdrv-config command makes a backup copy of the /usr/lib/security/methods.cfg file, then appends the stanza for the Linux and UNIX driver to the methods.cfg file.

```
original methods.cfg backed up to
/usr/lib/security/methods.cfg.nxdrv.04152006154047
```
